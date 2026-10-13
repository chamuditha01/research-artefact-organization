"""
demonstrate_ref044.py

SECOND demonstration case, mirroring demonstrate_ref031.py exactly, but for
a permanent_encroachment event instead of cultivation. Same structure, same
guardrails (SKILL.md: kept separate from evaluation; no accuracy claim).

REAL INPUTS ONLY:
  - Real polygon geometry: ref044_geometry.geojson, pulled from GEE just now
    (pull_ref044_geometry.js), queue_id REF_044, single Polygon, 9 vertices
    (closed ring).
  - Real Stage 1 / Stage 2 features: features_REF_merged.csv's REF_044 row.
  - Real dates: t_forest=2019-11-17, t_loss=2019-12-27
    (ref_labelling_record.md #15).

WHY THIS EVENT: REF_044 is the real event with a genuine Step1-vs-trajectory
conflict in your own labelling record - a building confirmed directly at the
pin for 4+ years, while the spectral trajectory looked like partial recovery
(actually home-garden regrowth around the building, not forest returning).
Structural evidence was given precedence, high confidence,
permanent_encroachment. It is also one of the 3 events (of 6
permanent_encroachment total) Stage 2 gets right under honest LOOCV
evaluation (run_e2.py) - so showing it is not cherry-picking a case outside
what's already documented, it's the same case decisions.md already discusses.

WHAT THIS DOES NOT SHOW (same caveats as demonstrate_ref031.py):
  - Not a generalization test - REF_044 is one of Stage 2's 19 training
    events.
  - Not quarterly re-classification - two fixed windows, not a repeating
    cycle.
  - Not detection itself - the real, already-confirmed polygon is fed in
    directly, not found by a running monitoring loop.
  - ONE event. No claim of typicality.
"""

import json
from datetime import date

from event_registry import EventRegistry, ClassificationState
from classifiers import stage1_classify, Stage2Classifier, STAGE2_FEATURES

EVENT_ID = "REF_044"
T_FOREST = date(2019, 11, 17)
T_LOSS = date(2019, 12, 27)

STAGE1_WINDOW_DAYS = 60
STAGE2_WINDOW_MONTHS = 12


def add_months(d: date, months: int) -> date:
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    day = min(d.day, 28)
    return date(year, month, day)


def load_rows(path):
    import csv
    with open(path) as f:
        rows = []
        for r in csv.DictReader(f):
            row = dict(r)
            for k in ["shape_compactness", "slope_deg", "dist_to_prior_loss_m",
                      "trend_nbr_per_day", "wobble_std", "cycle_count_provisional",
                      "area_ha"]:
                row[k] = float(row[k])
            rows.append(row)
        return rows


def main():
    rows = load_rows("features_REF_merged.csv")
    ref044 = next(r for r in rows if r["event_id"] == EVENT_ID)

    with open("ref044_geometry.geojson") as f:
        geojson = json.load(f)
    real_geometry = geojson["features"][0]["geometry"]

    stage2 = Stage2Classifier.fit_from_labelled_events(rows)
    print(f"Stage 2 fitted on n={stage2._n_train} labelled events "
          f"(REF_044 is one of them - see script docstring)\n")

    registry = EventRegistry()

    round1_date = date.fromordinal(T_LOSS.toordinal() + STAGE1_WINDOW_DAYS)
    round2_date = add_months(T_LOSS, STAGE2_WINDOW_MONTHS)

    print("=" * 78)
    print(f"ROUND 1 - {round1_date.isoformat()} "
          f"(t_loss + {STAGE1_WINDOW_DAYS} days, Stage 1 window closes)")
    print("=" * 78)

    summary1 = registry.process_round(
        round_id="round_1",
        round_date=round1_date,
        raw_candidate_geoms_wgs84=[real_geometry],
    )
    assert len(summary1["new_events"]) == 1, "expected exactly one new event on first detection"
    event_id = summary1["new_events"][0]
    print(f"Detection: new event created (registry id {event_id})")
    print(f"Real footprint: Polygon, {ref044['area_ha']:.3f} ha "
          f"(area_ha column, features_REF_merged.csv)")

    s1 = stage1_classify(ref044)
    registry.add_classification(event_id, ClassificationState(
        round_id="round_1", date=round1_date, stage="stage1",
        label=s1.label, confidence=s1.confidence, evidence_note=s1.evidence_note,
    ))
    print(f"\nStage 1 classification (provisional):")
    print(f"  label:      {s1.label}")
    print(f"  confidence: {s1.confidence}")
    print(f"  evidence:   {s1.evidence_note}")

    print()
    print("=" * 78)
    print(f"ROUND 2 - {round2_date.isoformat()} "
          f"(t_loss + {STAGE2_WINDOW_MONTHS} months, Stage 2 window closes)")
    print("=" * 78)

    summary2 = registry.process_round(
        round_id="round_2",
        round_date=round2_date,
        raw_candidate_geoms_wgs84=[real_geometry],
    )
    print(f"Registry match: {summary2}")
    assert summary2["updated_events"] == [event_id], (
        "expected round 2 to attach to the SAME event as round 1, not create a new one"
    )
    print(f"Confirmed: round 2's detection attached to the SAME event ({event_id}), "
          f"not a new one.")

    if s1.label == "candidate_human":
        s2 = stage2.classify(ref044)
        registry.add_classification(event_id, ClassificationState(
            round_id="round_2", date=round2_date, stage="stage2",
            label=s2.label, confidence=s2.confidence, evidence_note=s2.evidence_note,
        ))
        print(f"\nStage 2 classification (revision):")
        print(f"  label:      {s2.label}")
        print(f"  confidence: {s2.confidence}")
        print(f"  P(permanent_encroachment): {s2.probability_permanent:.3f}")
    else:
        print("\nStage 1 called candidate_natural - Stage 2 does not run.")

    print()
    print("=" * 78)
    print("FULL CLASSIFICATION HISTORY")
    print("=" * 78)
    event = registry.events()[event_id]
    for i, state in enumerate(event.classification_history, start=1):
        print(f"  [{i}] {state.date.isoformat()}  round={state.round_id:8s} "
              f"stage={state.stage:7s} label={state.label:25s} confidence={state.confidence}")


if __name__ == "__main__":
    main()
