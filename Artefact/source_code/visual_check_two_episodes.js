// ============================================================================
// visual_check_two_episodes.js  -  2026-09-28
// For REF_058 and REF_014: dist_to_prior_loss_m = 0, and roughly half of
// each polygon's area is Hansen-dated to a year clearly before the
// labelled event (REF_058: ~51% dated 2020, 3 years before its 2023
// event; REF_014: ~55% dated 2022/2023, 1-2 years before its 2024 event -
// see visual_check_prior_loss_zeros.js histogram output and decisions.md
// 2026-09-28 revisit condition).
//
// This puts real Sentinel-2 imagery on the map, bracketing BOTH the older
// Hansen-flagged year and the labelled event date, so the polygon can be
// checked by eye: does it contain two distinct clearing episodes (an
// older one + a newer one, sharing one vector boundary), or does the
// "older" loss turn out to be part of the same visible clearing (i.e.
// Hansen's per-year dating is what's off here, not the polygon)?
//
// Read-only, no export.
// ============================================================================
 
var SAMPLE_ASSET = 'projects/gsignin-501704/assets/REF_screening_queue';
var coll = ee.FeatureCollection(SAMPLE_ASSET);
 
function maskClouds(img) {
  var scl = img.select('SCL');
  var keep = scl.eq(4).or(scl.eq(5)).or(scl.eq(6)).or(scl.eq(7));
  return img.updateMask(keep);
}
 
function composite(geom, start, end) {
  return ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
    .filterBounds(geom).filterDate(start, end)
    .map(maskClouds)
    .median();
}
 
// event_id, t_forest, t_loss, old-episode bracket [oldStart, oldEnd]
// (wide 2-year brackets since Hansen only gives a year, not a date, for
// the older loss - narrow this if the composite looks too washed out)
var CASES = [
  { id: 'REF_058', tForest: '2023-01-20', tLoss: '2023-03-26', oldStart: '2019-06-01', oldEnd: '2021-06-01' },
  { id: 'REF_014', tForest: '2024-08-14', tLoss: '2024-09-18', oldStart: '2021-06-01', oldEnd: '2023-06-01' }
];
 
var TRUE_COLOR = { bands: ['B4', 'B3', 'B2'], min: 300, max: 2500 };
 
CASES.forEach(function (c) {
  var feat = ee.Feature(coll.filter(ee.Filter.eq('queue_id', c.id)).first());
  var geom = feat.geometry();
  var region = geom.buffer(200);
 
  // Older episode: one composite before it, one after.
  var oldPre = composite(region, ee.Date(c.oldStart), ee.Date(c.oldStart).advance(6, 'month'));
  var oldPost = composite(region, ee.Date(c.oldEnd).advance(-6, 'month'), ee.Date(c.oldEnd));
 
  // Labelled event: same before/after logic as the feature extraction script.
  var newPre = composite(region, ee.Date(c.tForest).advance(-4, 'month'), ee.Date(c.tForest));
  var newPost = composite(region, ee.Date(c.tLoss), ee.Date(c.tLoss).advance(4, 'month'));
 
  Map.addLayer(oldPre.clip(region), TRUE_COLOR, c.id + ' 1-OLD PRE (' + c.oldStart + ')', false);
  Map.addLayer(oldPost.clip(region), TRUE_COLOR, c.id + ' 2-OLD POST (' + c.oldEnd + ')', false);
  Map.addLayer(newPre.clip(region), TRUE_COLOR, c.id + ' 3-EVENT PRE (' + c.tForest + ')', false);
  Map.addLayer(newPost.clip(region), TRUE_COLOR, c.id + ' 4-EVENT POST (' + c.tLoss + '+4mo)', false);
  Map.addLayer(ee.Image().paint(ee.FeatureCollection([feat]), 0, 2), { palette: ['yellow'] }, c.id + ' polygon outline', true);
});
 
Map.centerObject(ee.Feature(coll.filter(ee.Filter.eq('queue_id', 'REF_058')).first()).geometry(), 17);
print('Turn on REF_058 layers 1-OLD PRE and 2-OLD POST first - look for a clearing boundary appearing between them, INSIDE the yellow polygon.');
print('Then turn those off, turn on 3-EVENT PRE and 4-EVENT POST - look for a SECOND, separate clearing boundary appearing between them.');
print('If both pairs show separate clearing boundaries, at different times, inside the same polygon: two real episodes - the polygon is too generous.');
print('If the OLD PRE image already looks cleared, or OLD PRE/POST look unchanged: inconclusive at this date range - narrow or shift oldStart/oldEnd.');
print('Repeat the same read for REF_014 (turn its layers on after REF_058, and re-center the map on it manually).');
 