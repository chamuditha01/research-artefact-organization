"""
extract_event_geometry.py

Run this LOCALLY, after you've downloaded the one-time export from
export_all_ref_geometries.js (REF_screening_queue_ALL_geometries.geojson,
from your Google Drive).

Pulls out ONE event's geometry + properties + centroid coordinates from
that big file, and writes it as a standalone <event_id>_geometry.geojson -
the same shape demonstrate_ref031.py / demonstrate_ref044.py already expect.

No more GEE console copy-pasting, ever - this file has every REF event's
real geometry already in it.

Usage:
    python extract_event_geometry.py REF_013
    python extract_event_geometry.py REF_053
    (run once per event you want to demo; prints the centroid coordinates
    too, so you don't need a separate step for that)
"""

import sys
import json

ALL_GEOMETRIES_FILE = "REF_screening_queue_ALL_geometries.geojson"


def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_event_geometry.py <EVENT_ID>")
        print("Example: python extract_event_geometry.py REF_013")
        sys.exit(1)

    event_id = sys.argv[1]

    with open(ALL_GEOMETRIES_FILE) as f:
        data = json.load(f)

    match = None
    for feat in data["features"]:
        props = feat.get("properties", {})
        if props.get("queue_id") == event_id:
            match = feat
            break

    if match is None:
        print(f"'{event_id}' not found in {ALL_GEOMETRIES_FILE}. "
              f"Check the exact queue_id spelling (case-sensitive).")
        sys.exit(1)

    out = {"type": "FeatureCollection", "features": [match]}
    out_path = f"{event_id.lower()}_geometry.geojson"
    with open(out_path, "w") as f:
        json.dump(out, f)
    print(f"Wrote {out_path}")

    # centroid, for a quick coordinate check / Google Maps paste
    try:
        from shapely.geometry import shape
        poly = shape(match["geometry"])
        c = poly.centroid
        print(f"Centroid: {c.y:.7f}, {c.x:.7f}  (paste into Google Maps as lat, lon)")
        print(f"Geometry type: {match['geometry']['type']}")
    except ImportError:
        print("(install shapely to also get a centroid printed: pip3 install shapely)")

    print(f"\nProperties: {json.dumps(match.get('properties', {}), indent=2)}")


if __name__ == "__main__":
    main()
