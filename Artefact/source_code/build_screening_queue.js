// ============================================================================
// build_screening_queue.js  -  2026-09-12
// Builds the screening queue for the curated confirmed-forest-loss reference
// set. Pre-filters candidate LOCATIONS only - NO forest/non-forest decision.
// Final inclusion is always manual (Step 0) then trajectory. NOT a prevalence
// sample. RUN THIS FIRST; it creates the asset the time-series tool reads.
// ============================================================================
 
// STEP 1 - candidate sites (exact WDPA NAME strings).
// Excluded: Gal Oya (0/8 check), Wilpattu (~18 events).
var SITES = [
  'Kahalla - Pallekele', 'Nuwaragala', 'Maduroad',
  'Victoria Randenigala Rantambe'
];
 
var wdpa = ee.FeatureCollection('WCMC/WDPA/current/polygons')
             .filter(ee.Filter.eq('ISO3', 'LKA'))
             .filter(ee.Filter.eq('STATUS', 'Designated'))
             .filter(ee.Filter.inList('NAME', SITES));
 
print('STEP 1 - sites matched (want 4)', wdpa.size(), wdpa.aggregate_array('NAME'));
 
// STEP 2 - parameters
var HANSEN_ID  = 'UMD/hansen/global_forest_change_2025_v1_13';
var LOSS_MIN   = 19;   // 2019
var LOSS_MAX   = 24;   // 2024
var MIN_AREA_HA  = 0.5;   // sub-0.5 ha were false positives every time
var WATER_OCC    = 25;    // JRC occurrence >= this = permanent water
var WATER_BUFF_M = 60;    // exclude centroids within this of permanent water
                          // (PARTIAL - JRC misses small seasonal tanks)
var SEED     = 7;         // fresh; rejected batch used 42
var EXPORT_N = 250;
 
// STEP 3 - Hansen loss patches per site, loss year attached, site name kept
var hansen   = ee.Image(HANSEN_ID);
var lossyear = hansen.select('lossyear');
var perSite  = wdpa.toList(wdpa.size());
 
var candidates = ee.FeatureCollection(
  ee.List.sequence(0, wdpa.size().subtract(1)).map(function (i) {
    var pa = ee.Feature(perSite.get(i));
    var g  = pa.geometry();
    var name = pa.get('NAME'), desig = pa.get('DESIG_ENG');
    var inPeriod = lossyear.clip(g).gte(LOSS_MIN).and(lossyear.lte(LOSS_MAX)).selfMask();
    var patches = inPeriod.rename('mask').reduceToVectors({
      geometry: g, scale: 30, geometryType: 'polygon', eightConnected: true,
      labelProperty: 'patch_id', maxPixels: 1e10, bestEffort: true
    });
    var withYear = lossyear.rename('ly').reduceRegions({
      collection: patches, reducer: ee.Reducer.mode(), scale: 30
    }).filter(ee.Filter.notNull(['mode']));
    return withYear.map(function (f) {
      var geom = f.geometry();
      var c = geom.centroid({maxError: 1}).coordinates();
      return f.set({
        site: name, designation: desig,
        hansen_lossyear: ee.Number(f.get('mode')).add(2000),
        area_ha: geom.area({maxError: 1}).divide(10000),
        geom_type: geom.type(), lon: c.get(0), lat: c.get(1),
        sampling_origin: 'gfw_seeded', hansen_version: HANSEN_ID
      });
    });
  })
).flatten();
 
print('STEP 3 - raw candidates', candidates.size());
 
// STEP 4 - inclusion filters (no forest decision)
var water   = ee.Image('JRC/GSW1_4/GlobalSurfaceWater').select('occurrence');
var permWat = water.gte(WATER_OCC).selfMask();
var waterDist = permWat.fastDistanceTransform().sqrt()
                  .multiply(ee.Image.pixelArea().sqrt());
 
var withWater = candidates.map(function (f) {
  var d = waterDist.reduceRegion({
    reducer: ee.Reducer.min(), geometry: f.geometry().centroid({maxError: 1}),
    scale: 30, maxPixels: 1e9
  }).values().get(0);
  d = ee.Number(ee.Algorithms.If(d, d, 9999));
  return f.set('dist_water_m', d);
});
 
var included = withWater
  .filter(ee.Filter.gte('area_ha', MIN_AREA_HA))
  .filter(ee.Filter.gte('dist_water_m', WATER_BUFF_M))
  .map(function (f) {
    return f.set('prescreen_reason',
      ee.String('area>=').cat(ee.Number(MIN_AREA_HA).format('%.1f'))
        .cat('ha & water_dist>=').cat(ee.Number(WATER_BUFF_M).format('%d'))
        .cat('m (').cat(ee.Number(f.get('area_ha')).format('%.2f'))
        .cat('ha, ').cat(ee.Number(f.get('dist_water_m')).format('%.0f')).cat('m)'));
  });
 
print('STEP 4 - after filters', included.size());
print('STEP 4 - by site', included.aggregate_histogram('site'));
 
// STEP 5 - screening queue: shuffle with seed 7, number REF_001...
var shuffled = included.randomColumn('rnd', SEED).sort('rnd');
var nQueue   = shuffled.size().min(EXPORT_N);
var queueList= shuffled.toList(EXPORT_N);
var queue = ee.FeatureCollection(
  ee.List.sequence(0, ee.Number(nQueue).subtract(1)).map(function (i) {
    i = ee.Number(i);
    return ee.Feature(queueList.get(i))
             .set('queue_id', ee.String('REF_').cat(i.add(1).format('%03d')));
  })
);
print('STEP 5 - queue size', queue.size());
 
// STEP 6 - exports. RUN the ASSET one; the time-series tool reads it.
var CSV_COLS = ['queue_id','site','designation','hansen_lossyear','area_ha',
                'geom_type','lat','lon','dist_water_m','prescreen_reason',
                'sampling_origin','hansen_version','rnd'];
Export.table.toDrive({collection: queue, description: 'REF_screening_queue',
  fileFormat: 'CSV', selectors: CSV_COLS});
Export.table.toDrive({collection: queue, description: 'REF_screening_queue_polygons',
  fileFormat: 'GeoJSON'});
Export.table.toAsset({collection: queue, description: 'REF_screening_queue',
  assetId: 'REF_screening_queue'});
 
// SEED 7. Screen REF_001 down. Two gates: manual Step 0, then trajectory.
// Stop at 30 CONFIRMED, any class mix.
 