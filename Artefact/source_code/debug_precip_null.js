// ============================================================================
// debug_precip_null.js  -  2026-09-29
// ISOLATED DIAGNOSTIC ONLY - not part of the pipeline. assign_climatic_zone.js
// has failed 4 times straight (v1-v4) with mean_annual_precip_mm coming back
// null for ALL 679 WDPA polygons, even after removing every plausible cause
// guessed so far (bestEffort arg, chained year-sum computation, geometry
// repair). Rather than guess a 5th time, this isolates each moving part on
// ONE known geometry (Wilpattu) so the actual failure point is visible.
// Run this, paste back ALL of STEP A-E's output.
// ============================================================================
 
// STEP A - the image itself. Check band name and whether it prints sane
// metadata at all (not a computed error object).
var chirps = ee.ImageCollection('UCSB-CHG/CHIRPS/DAILY')
               .filterDate('1991-01-01', '2021-01-01')
               .select('precipitation');
var meanDailyRate = chirps.mean();
print('STEP A - meanDailyRate image (check band name = precipitation, and that this prints at all)',
  meanDailyRate);
 
var meanAnnualPrecip = meanDailyRate.multiply(365.25).rename('mean_annual_precip_mm');
print('STEP A2 - meanAnnualPrecip image (check band name = mean_annual_precip_mm)',
  meanAnnualPrecip);
 
// STEP B - ONE known geometry, Wilpattu, fetched fresh (no buffer/repair).
var wilpattu = ee.FeatureCollection('WCMC/WDPA/current/polygons')
                 .filter(ee.Filter.eq('ISO3', 'LKA'))
                 .filter(ee.Filter.eq('NAME', 'Wilpattu'))
                 .first();
print('STEP B - Wilpattu feature itself (check it is not null/empty)', wilpattu);
print('STEP B2 - Wilpattu geometry area, sq meters (sanity: should be ~1.3 billion, ~131700 ha)',
  wilpattu.geometry().area(1));
 
// STEP C - reduceRegion (SINGULAR - one region, one number) on Wilpattu's
// geometry directly. This is the simplest possible version of the operation
// - if this alone comes back null, the problem is the image or the
// geometry, not the batch reduceRegions machinery.
var singleResult = meanAnnualPrecip.reduceRegion({
  reducer: ee.Reducer.mean(),
  geometry: wilpattu.geometry(),
  scale: 5566,
  maxPixels: 1e9,
  bestEffort: true  // valid here - reduceRegion (singular) does accept it
});
print('STEP C - reduceRegion (singular) result on Wilpattu directly', singleResult);
 
// STEP D - same thing but sampling ONLY the centroid point, bypassing
// region-averaging entirely. If STEP C is null but STEP D works, the
// problem is in how the polygon geometry interacts with the reducer, not
// the image itself.
var centroidResult = meanAnnualPrecip.reduceRegion({
  reducer: ee.Reducer.first(),
  geometry: wilpattu.geometry().centroid(1),
  scale: 5566,
  bestEffort: true
});
print('STEP D - value at Wilpattu centroid point only', centroidResult);
 
// STEP E - sanity check the image has data ANYWHERE, using a huge fixed
// bounding box over Sri Lanka's known lat/lon range, not a WDPA geometry
// at all. If this is also null, the problem is upstream in the CHIRPS
// collection or date filter, not any geometry.
var sriLankaBox = ee.Geometry.Rectangle([79.5, 5.8, 82.0, 10.0]);
var boxResult = meanAnnualPrecip.reduceRegion({
  reducer: ee.Reducer.mean(),
  geometry: sriLankaBox,
  scale: 5566,
  maxPixels: 1e9,
  bestEffort: true
});
print('STEP E - value over a fixed Sri Lanka bounding box (not WDPA at all)', boxResult);