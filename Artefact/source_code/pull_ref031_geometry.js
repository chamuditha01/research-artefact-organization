// ============================================================================
// pull_event_geometry.js - one-off - 2026-09-29
// Pulls the real polygon footprint for ONE event from the REF screening
// queue asset, for the dissertation's demonstration case (methodology.md
// Step 4, decisions.md 2026-09-29 "Demonstration case selected: REF_031").
// Geometry only - no NBR trajectory, no time-series stats. REF_031's
// trajectory already exists in REF_all_timeseries.csv.
// ============================================================================
 
var SAMPLE_ASSET = 'projects/gsignin-501704/assets/REF_screening_queue';
var EVENT_ID     = 'REF_031';   // queue_id
 
var coll = ee.FeatureCollection(SAMPLE_ASSET);
var feat = ee.Feature(coll.filter(ee.Filter.eq('queue_id', EVENT_ID)).first());
 
print('Feature properties', feat.toDictionary());
print('Geometry type', feat.geometry().type());
print('Geometry parts (1 = single patch)', feat.geometry().geometries().size());
print('Area (ha)', feat.geometry().area({maxError: 1}).divide(10000));
 
// This is the line to actually copy: the GeoJSON geometry object.
// Click the expand arrow on this printed line in the Console, then copy
// the whole {"type": ..., "coordinates": [...]} block and paste it back
// in chat.
print('GEOMETRY (copy this whole object) ->', feat.geometry());
 
Map.centerObject(feat, 16);
Map.addLayer(feat, {color: 'yellow'}, EVENT_ID);
 
// Backup to copy-pasting from the console: exports the same feature
// (properties + geometry) as a GeoJSON file to your Drive.
Export.table.toDrive({
  collection: ee.FeatureCollection([feat]),
  description: 'geom_' + EVENT_ID,
  fileFormat: 'GeoJSON'
});
 