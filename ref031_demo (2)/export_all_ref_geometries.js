// ============================================================================
// export_all_ref_geometries.js - ONE-TIME export
//
// Replaces the manual per-event console copy-paste (pull_ref031_geometry.js /
// pull_ref044_geometry.js) with a single export that pulls EVERY feature in
// the REF screening queue asset at once - all properties AND geometry - as
// one GeoJSON file to Drive. Run this once; after that, any event's
// geometry can be pulled locally (see extract_event_geometry.py) with no
// further GEE Code Editor work.
// ============================================================================

var SAMPLE_ASSET = 'projects/gsignin-501704/assets/REF_screening_queue';

var coll = ee.FeatureCollection(SAMPLE_ASSET);

print('Total features in queue:', coll.size());
print('Sample feature (check this looks right before exporting):', coll.first());

Export.table.toDrive({
  collection: coll,
  description: 'REF_screening_queue_ALL_geometries',
  fileFormat: 'GeoJSON'
});

// After this finishes (check the Tasks tab in GEE, top right), download
// "REF_screening_queue_ALL_geometries.geojson" from your Google Drive and
// send it back - or run extract_event_geometry.py against it locally for
// any queue_id you need, any time, without opening GEE again.
