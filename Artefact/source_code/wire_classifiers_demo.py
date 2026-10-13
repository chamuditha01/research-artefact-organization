"""
wire_classifiers_demo.py
 
Demonstrates the wiring: registry <- Stage 1 <- Stage 2, using the real
labelled REF features. NOT a demonstration case for the dissertation
(methodology.md Step 4) - this uses PLACEHOLDER square polygons, not real
event geometry, because no GeoJSON footprints are available in this
session (features_REF_merged.csv carries feature values only, no
geometry column). A real demonstration case needs real polygons pulled
from GEE for the chosen event(s) - flagged as a separate remaining task,
not done here.
 
What this script actually proves: that stage1_classify() and
Stage2Classifier.classify() produce ClassificationState objects the
registry accepts via add_classification(), and that Stage 1's
"never calls natural" finding (decisions.md) and Stage 2's cascade
(only human-routed events reach Stage 2) both work as coded, not just
as described.
 
RUN RESULT, 2026-09-29 (see decisions.md / chat for the finding this
surfaced): REF_018 (uncertain_logging) is called candidate_natural by
Stage 1 - the ONLY event in the full 29-row REF set to do so. This was
not caught by the decisions.md 2026-09-28 false-positive check, because
that check only tested the 19 KNOWN-HUMAN events (cultivation +
permanent_encroachment) - REF_018 is neither, it's one of the 3
logging-pooled uncertain events (G2, issues.md). This is plausibly a
live example of exactly the G2 Stage-1 confound already named in
decisions.md/issues.md (scattered selective logging reads as natural at
Stage 1, coupe felling reads as human) - not necessarily a bug, but not
yet logged as a decisions.md/issues.md finding either. Flagged, not
acted on, pending discussion.
"""
 
import csv
import sys
from datetime import date
 
sys.path.insert(0, ".")
from event_registry import EventRegistry, ClassificationState
from classifiers import stage1_classify, Stage2Classifier, STAGE2_FEATURES
 
 
def load_rows(path):
    with open(path) as f:
        reader = csv.DictReader(f)
        rows = []
        for r in reader:
            row = dict(r)
            for k in ["shape_compactness", "slope_deg", "dist_to_prior_loss_m",
                      "trend_nbr_per_day", "wobble_std", "cycle_count_provisional"]:
                row[k] = float(row[k])
            rows.append(row)
        return rows
 
 
def square_around(lon, lat, half_side_deg=0.0003):
    return {
        "type": "Polygon",
        "coordinates": [[
            [lon - half_side_deg, lat - half_side_deg],
            [lon + half_side_deg, lat - half_side_deg],
            [lon + half_side_deg, lat + half_side_deg],
            [lon - half_side_deg, lat + half_side_deg],
            [lon - half_side_deg, lat - half_side_deg],
        ]]
    }
 
 
def main():
    rows = load_rows("features_REF_merged.csv")
    stage2 = Stage2Classifier.fit_from_labelled_events(rows)
    print(f"Stage 2 fitted on n={stage2._n_train} labelled events\n")
 
    registry = EventRegistry()
 
    base_lon, base_lat = 80.30, 8.10
    event_ids = {}
 
    print(f"{'event_id':10s} {'known_class':22s} {'stage1':17s} {'stage2':22s} {'s2_prob':>8s}")
    print("-" * 90)
 
    for i, row in enumerate(rows):
        lon = base_lon + i * 0.01
        geom = square_around(lon, base_lat)
        summary = registry.process_round(
            round_id="demo_round_1",
            round_date=date(2026, 9, 29),
            raw_candidate_geoms_wgs84=[geom],
        )
        eid = summary["new_events"][0]
        event_ids[row["event_id"]] = eid
 
        s1 = stage1_classify(row)
        registry.add_classification(eid, ClassificationState(
            round_id="demo_round_1", date=date(2026, 9, 29), stage="stage1",
            label=s1.label, confidence=s1.confidence, evidence_note=s1.evidence_note,
        ))
 
        s2_label = "n/a (routed natural)"
        s2_prob_str = "-"
        if s1.label == "candidate_human":
            s2 = stage2.classify(row)
            registry.add_classification(eid, ClassificationState(
                round_id="demo_round_1", date=date(2026, 9, 29), stage="stage2",
                label=s2.label, confidence=s2.confidence, evidence_note=s2.evidence_note,
            ))
            s2_label = s2.label
            s2_prob_str = f"{s2.probability_permanent:.3f}"
 
        print(f"{row['event_id']:10s} {row['known_class']:22s} {s1.label:17s} {s2_label:22s} {s2_prob_str:>8s}")
 
    natural_calls = sum(
        1 for r in rows
        if stage1_classify(r).label == "candidate_natural"
    )
    print(f"\nStage 1 called 'candidate_natural' for {natural_calls}/{len(rows)} events "
          f"(decisions.md: expected 0 among the 19 known-human events, since REF_020 "
          f"fails the compactness leg - but this counts across all 29 REF rows).")
 
    ref020 = next(r for r in rows if r["event_id"] == "REF_020")
    s1_ref020 = stage1_classify(ref020)
    print(f"REF_020 (the one known natural event): stage1 -> {s1_ref020.label} "
          f"({s1_ref020.evidence_note})")
 
 
if __name__ == "__main__":
    main()
 