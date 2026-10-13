// ============================================================================
// candidate_screen.js
// Candidate-generation screen for the calibration batch.
//
// WHAT THIS IS: a crude change-detection screen whose only job is to produce a
// pile of candidate polygons to sample from and label by hand.
//
// WHAT THIS IS NOT: the artefact's detector. It has no seasonal correction, no
// held forest reference, no monitoring loop. Do not report any number from this
// script as a detection result, and do not describe it as the detector in the
// meeting. It is a candidate generator for building a reference set.
//
// UNTESTED: written without GEE access. Expect to debug. Run section by section.
// ============================================================================
 
 
// ---------------------------------------------------------------------------
// STEP 0 - find your polygons first. Run this alone, look at the console,
// then comment it out. Names in WDPA are not always what you expect.
// ---------------------------------------------------------------------------
var wdpa = ee.FeatureCollection('WCMC/WDPA/current/polygons')
             .filter(ee.Filter.eq('ISO3', 'LKA'));
 
print('All LKA names', wdpa.aggregate_array('NAME').distinct().sort());
 
 
// ---------------------------------------------------------------------------
// STEP 1 - site selection
// Adjust the name filters after looking at STEP 0 output. Sinharaja in
// particular carries several records (M14) - check whether you are getting one
// geometry or several stacked ones. Dissolve if several.
// ---------------------------------------------------------------------------
var SITE_NAME = 'Wilpattu';        // switch to 'Sinharaja' for the second run
 
var site = wdpa
  .filter(ee.Filter.stringContains('NAME', SITE_NAME))
  .filter(ee.Filter.eq('STATUS', 'Designated'))
  .filter(ee.Filter.eq('GIS_M_AREA', 0));       // drop marine (M9)
 
print(SITE_NAME + ' records', site.size(), site.aggregate_array('NAME'));
 
// Dissolve to one geometry so overlapping designations do not duplicate events
var aoi = site.geometry().dissolve({maxError: 10});
Map.centerObject(aoi, 10);
Map.addLayer(aoi, {color: 'yellow'}, SITE_NAME + ' AOI', true);
 
 
// ---------------------------------------------------------------------------
// STEP 2 - screen parameters
// EVERY ONE OF THESE IS A SCREEN PARAMETER, NOT AN ARTEFACT PARAMETER.
// Write the values you used into your notes. If you change one, the candidate
// pool changes, and so does any prevalence figure drawn from it.
// ---------------------------------------------------------------------------
var YEARS        = [2019, 2020, 2021, 2022, 2023, 2024];
var FOREST_NBR   = 0.40;   // NBR above this in year t0 counts as forest
var DNBR_DROP    = 0.15;   // NBR drop from t0 to t1 that flags a candidate
var MIN_PIXELS   = 10;     // 10 px at 10 m = 0.1 ha; drops speckle
var SEED         = 42;     // record this - it makes the random draw reproducible
var SAMPLE_N     = 30;
 
 
// ---------------------------------------------------------------------------
// STEP 3 - cloud-masked annual NBR composites
// SCL-based masking. Coarse, but adequate for a screen. Your real pipeline
// should use something better (s2cloudless) and mask per pixel, not per scene.
// ---------------------------------------------------------------------------
function maskSCL(img) {
  var scl = img.select('SCL');
  // keep: 4 veg, 5 bare, 6 water, 7 unclassified
  // drop: 3 shadow, 8 cloud med, 9 cloud high, 10 cirrus
  var keep = scl.eq(4).or(scl.eq(5)).or(scl.eq(6)).or(scl.eq(7));
  return img.updateMask(keep).divide(10000)
            .copyProperties(img, ['system:time_start']);
}
 
function nbrComposite(year) {
  var col = ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
    .filterBounds(aoi)
    .filterDate(year + '-01-01', year + '-12-31')
    .map(maskSCL);
 
  var nbr = col.map(function (img) {
    return img.normalizedDifference(['B8', 'B12']).rename('NBR');
  });
 
  // valid observation count per pixel - this is the M1-shaped number,
  // annual here rather than monthly, but it is the right SHAPE of number
  var nObs = nbr.count().rename('n_obs');
 
  return nbr.median().rename('NBR')
            .addBands(nObs)
            .clip(aoi)
            .set('year', year);
}
 
 
// ---------------------------------------------------------------------------
// STEP 4 - difference consecutive years, vectorise candidates
// ---------------------------------------------------------------------------
function candidatesForPair(y0, y1) {
  var c0 = nbrComposite(y0);
  var c1 = nbrComposite(y1);
 
  var wasForest = c0.select('NBR').gte(FOREST_NBR);
  var dropped   = c0.select('NBR').subtract(c1.select('NBR')).gte(DNBR_DROP);
  var change    = wasForest.and(dropped).selfMask();
 
  // remove speckle
  var big = change.updateMask(
    change.connectedPixelCount(MIN_PIXELS + 1, true).gte(MIN_PIXELS)
  );
 
  var vectors = big.reduceToVectors({
    geometry: aoi,
    scale: 10,
    geometryType: 'polygon',
    eightConnected: true,
    maxPixels: 1e10,
    bestEffort: true
  });
 
  return vectors.map(function (f) {
    var g = f.geometry();
    var c = g.centroid({maxError: 1}).coordinates();
    return f.set({
      site:       SITE_NAME,
      year_from:  y0,
      year_to:    y1,
      area_ha:    g.area({maxError: 1}).divide(10000),
      lon:        c.get(0),
      lat:        c.get(1)
    });
  });
}
 
var allCandidates = ee.FeatureCollection(
  YEARS.slice(0, -1).map(function (y, i) {
    return candidatesForPair(y, YEARS[i + 1]);
  })
).flatten();
 
// THIS COUNT IS THE MEETING NUMBER. For Sinharaja it is M13.
print('CANDIDATE COUNT - ' + SITE_NAME, allCandidates.size());
print('Area distribution (ha)', allCandidates.aggregate_array('area_ha'));
 
Map.addLayer(allCandidates, {color: 'red'}, 'Candidates', true);
 
 
// ---------------------------------------------------------------------------
// STEP 5 - random draw with a recorded seed
// Random, not hand-picked. A convenience sample invalidates the prevalence
// estimate (labelling_protocol.md §8).
// ---------------------------------------------------------------------------
var sample = allCandidates
  .randomColumn('rnd', SEED)
  .sort('rnd')
  .limit(SAMPLE_N)
  .map(function (f, i) { return f; });
 
print('Random sample size', sample.size());
Map.addLayer(sample, {color: 'cyan'}, 'Random sample', true);
 
 
// ---------------------------------------------------------------------------
// STEP 6 - export
// The CSV gives you lat/lon to paste into Google Earth Pro's search box, then
// use the historical imagery slider for the structural-evidence step (§5 Step 1).
// ---------------------------------------------------------------------------
Export.table.toDrive({
  collection:  sample,
  description: SITE_NAME + '_calibration_sample_seed' + SEED,
  fileFormat:  'CSV',
  selectors:   ['site', 'year_from', 'year_to', 'area_ha', 'lon', 'lat', 'rnd']
});
 
Export.table.toDrive({
  collection:  allCandidates,
  description: SITE_NAME + '_all_candidates',
  fileFormat:  'GeoJSON'
});
 
 
// ---------------------------------------------------------------------------
// RECORD THESE IN YOUR NOTES BEFORE YOU FORGET
// ---------------------------------------------------------------------------
// Site name and WDPA record count:
// Screen parameters: FOREST_NBR, DNBR_DROP, MIN_PIXELS, YEARS
// Random seed:
// Candidate count:
// Query date:
// Collection: COPERNICUS/S2_SR_HARMONIZED
// Boundary: WCMC/WDPA/current/polygons, ISO3=LKA
//
// Without all of the above, this is "a number I remember", not a measurement
// (SKILL.md, Sources).
// ---------------------------------------------------------------------------
 