// ============================================================================
// visual_check_prior_loss_zeros.js  -  2026-09-28
// One-off diagnostic for the decisions.md 2026-09-28 (later still again)
// "revisit if" condition: dist_to_prior_loss_m = 0 for REF_058, REF_053,
// REF_016, REF_014 in the v5 (no-buffer) run. Checks whether the "prior
// loss" pixel found inside each event's own polygon is a genuinely older,
// separate clearing, or a same-clearing edge-dating artifact (Hansen
// sometimes splits one contiguous clearing across an annual compositing
// boundary, tagging part of it with the following year).
//
// Two checks per event:
//   1. YEAR GAP - histogram of lossyear codes found inside the polygon,
//      restricted to strictly-prior years (same mask logic as the feature
//      itself). A gap of 1 year from the event's own year is consistent
//      with a same-clearing edge artifact. A bigger gap is evidence of a
//      genuinely separate, older clearing.
//   2. SPATIAL PATTERN - map layers, so the older pixel(s) can be seen: a
//      scattered sliver hugging the polygon boundary looks different from
//      a solid separate patch sitting next to it.
//
// Read-only. No export. Standalone - does not depend on
// feature_extraction_batch_REF.js having been run first in this editor
// session.
//
// HOW TO READ THE OUTPUT: the printed histogram is a dictionary like
// {"20": 3} meaning year code 20 (2020), 3 pixels. Compare each code to
// that event's own year code (printed alongside it). Then turn on that
// event's two map layers (they start OFF, one event at a time, so four
// events' pixels don't overlap) and look at where the highlighted pixels
// sit relative to the white polygon outline.
// ============================================================================
 
var SAMPLE_ASSET = 'projects/gsignin-501704/assets/REF_screening_queue';
var HANSEN_ID = 'UMD/hansen/global_forest_change_2025_v1_13';
var HANSEN_LOSSYEAR = ee.Image(HANSEN_ID).select('lossyear');
var coll = ee.FeatureCollection(SAMPLE_ASSET);
 
// event_id, t_loss (for the year code) - matches feature_extraction_batch_REF.js v5
var TARGETS = [
  ['REF_058', '2023-03-26'],
  ['REF_053', '2024-05-31'],
  ['REF_016', '2022-04-30'],
  ['REF_014', '2024-09-18']
];
 
TARGETS.forEach(function (row) {
  var eventId = row[0], tLossStr = row[1];
  var feat = ee.Feature(coll.filter(ee.Filter.eq('queue_id', eventId)).first());
  var geom = feat.geometry();
  var eventYearCode = ee.Date(tLossStr).get('year').subtract(2000);
 
  // CHECK 1: year-code histogram of loss pixels strictly before the event's
  // own year, inside the polygon - identical mask logic to dist_to_prior_loss_m.
  var priorMask = HANSEN_LOSSYEAR.gt(0).and(HANSEN_LOSSYEAR.lt(eventYearCode));
  var hist = HANSEN_LOSSYEAR.updateMask(priorMask).reduceRegion({
    reducer: ee.Reducer.frequencyHistogram(),
    geometry: geom, scale: 30, maxPixels: 1e9
  });
  print(eventId + ' - event year code ' + eventYearCode.getInfo() +
        ' - prior-year lossyear codes found INSIDE the polygon:', hist.get('lossyear'));
 
  // CHECK 2: map layers - polygon outline + nearby Hansen lossyear pixels,
  // so the pixel(s) driving the histogram above can be seen against the
  // polygon boundary. Layers start OFF - turn on one event's pair at a time.
  var buffered = geom.buffer(150);
  Map.addLayer(HANSEN_LOSSYEAR.updateMask(HANSEN_LOSSYEAR.gt(0)).clip(buffered),
    {min: 1, max: 24, palette: ['yellow', 'orange', 'red', 'purple', 'blue']},
    eventId + ' - lossyear (yellow=old, blue=recent)', false);
  Map.addLayer(ee.Image().paint(ee.FeatureCollection([feat]), 0, 2),
    {palette: ['white']}, eventId + ' - polygon outline', false);
});
 
Map.centerObject(ee.Feature(coll.filter(ee.Filter.eq('queue_id', 'REF_058')).first()).geometry(), 17);
print('Done. Turn on REF_058 layers first in the Layers panel, inspect, then switch to the next event.');
 