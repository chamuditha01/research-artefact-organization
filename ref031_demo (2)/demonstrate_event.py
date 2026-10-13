"""
demonstrate_event.py

GENERIC version of demonstrate_ref031.py / demonstrate_ref044.py - works for
ANY event, instead of needing a hand-written script per event. Requires
<event_id_lower>_geometry.geojson to already exist (from
extract_event_geometry.py) and the event's row to exist in
features_REF_merged.csv.

t_forest / t_loss are not in features_REF_merged.csv - they're looked up
automatically from event_dates.csv (pulled from ref_labelling_record.md's
per-event table). You only need to pass dates manually if you want to
override the lookup.

Usage:
    python demonstrate_event.py REF_013
    python demonstrate_event.py REF_013 2023-03-06 2023-03-16   (manual override)

Same guardrails as demonstrate_ref031.py / demonstrate_ref044.py: this is a
DEMONSTRATION, not an evaluation. Every event run through this is, unless
stated otherwise, one of Stage 2's 19 training events - it shows the
mechanism works, not that it generalises. State that plainly whenever this
is shown.
"""

import sys
import json
from datetime import date


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


def lookup_dates(event_id):
    import csv
    with open("event_dates.csv") as f:
        for row in csv.DictReader(f):
            if row["event_id"] == event_id:
                if not row["t_forest"] or not row["t_loss"]:
                    print(f"'{event_id}' has no clean t_forest/t_loss in event_dates.csv "
                          f"({row['note']}). Pass dates manually if you want to proceed anyway:")
                    print(f"    python demonstrate_event.py {event_id} <t_forest> <t_loss>")
                    sys.exit(1)
                if row["note"]:
                    print(f"NOTE on {event_id}'s dates: {row['note']}")
                return date.fromisoformat(row["t_forest"]), date.fromisoformat(row["t_loss"])
    print(f"'{event_id}' not found in event_dates.csv. Pass dates manually:")
    print(f"    python demonstrate_event.py {event_id} <t_forest> <t_loss>")
    sys.exit(1)


def main():
    if len(sys.argv) == 2:
        event_id = sys.argv[1]
        t_forest, t_loss = lookup_dates(event_id)
    elif len(sys.argv) == 4:
        event_id = sys.argv[1]
        t_forest = date.fromisoformat(sys.argv[2])
        t_loss = date.fromisoformat(sys.argv[3])
    else:
        print("Usage: python demonstrate_event.py <EVENT_ID>")
        print("       python demonstrate_event.py <EVENT_ID> <t_forest YYYY-MM-DD> <t_loss YYYY-MM-DD>  (override)")
        print("Example: python demonstrate_event.py REF_013")
        sys.exit(1)

    from event_registry import EventRegistry, ClassificationState
    from classifiers import stage1_classify, Stage2Classifier

    STAGE1_WINDOW_DAYS = 60
    STAGE2_WINDOW_MONTHS = 12

    rows = load_rows("features_REF_merged.csv")
    try:
        event_row = next(r for r in rows if r["event_id"] == event_id)
    except StopIteration:
        print(f"'{event_id}' not found in features_REF_merged.csv. "
              f"Check it's one of the 29 rows with real features.")
        sys.exit(1)

    geom_path = f"{event_id.lower()}_geometry.geojson"
    try:
        with open(geom_path) as f:
            geojson = json.load(f)
    except FileNotFoundError:
        print(f"'{geom_path}' not found. Run first:")
        print(f"    python extract_event_geometry.py {event_id}")
        sys.exit(1)
    real_geometry = geojson["features"][0]["geometry"]

    stage2 = Stage2Classifier.fit_from_labelled_events(rows)
    print(f"Event: {event_id}  (known_class in dataset: {event_row['known_class']})")
    print(f"Stage 2 fitted on n={stage2._n_train} labelled events "
          f"({'this event IS one of them' if event_row['known_class'] in ('cultivation','cultivation_pasture','permanent_encroachment') else 'this event is NOT one of the 19 training events'})\n")

    registry = EventRegistry()
    round1_date = date.fromordinal(t_loss.toordinal() + STAGE1_WINDOW_DAYS)
    round2_date = add_months(t_loss, STAGE2_WINDOW_MONTHS)

    print("=" * 78)
    print(f"ROUND 1 - {round1_date.isoformat()} (t_loss + {STAGE1_WINDOW_DAYS} days)")
    print("=" * 78)
    summary1 = registry.process_round(
        round_id="round_1", round_date=round1_date,
        raw_candidate_geoms_wgs84=[real_geometry],
    )
    event_db_id = summary1["new_events"][0]
    print(f"Detection: new event created (registry id {event_db_id})")
    print(f"Real footprint area: {event_row['area_ha']:.3f} ha")

    s1 = stage1_classify(event_row)
    registry.add_classification(event_db_id, ClassificationState(
        round_id="round_1", date=round1_date, stage="stage1",
        label=s1.label, confidence=s1.confidence, evidence_note=s1.evidence_note,
    ))
    print(f"\nStage 1: label={s1.label}  confidence={s1.confidence}  ({s1.evidence_note})")

    print()
    print("=" * 78)
    print(f"ROUND 2 - {round2_date.isoformat()} (t_loss + {STAGE2_WINDOW_MONTHS} months)")
    print("=" * 78)
    summary2 = registry.process_round(
        round_id="round_2", round_date=round2_date,
        raw_candidate_geoms_wgs84=[real_geometry],
    )
    print(f"Registry match: {summary2}")

    if s1.label == "candidate_human":
        s2 = stage2.classify(event_row)
        registry.add_classification(event_db_id, ClassificationState(
            round_id="round_2", date=round2_date, stage="stage2",
            label=s2.label, confidence=s2.confidence, evidence_note=s2.evidence_note,
        ))
        print(f"\nStage 2: label={s2.label}  confidence={s2.confidence}  "
              f"P(permanent_encroachment)={s2.probability_permanent:.3f}")
    else:
        print("\nStage 1 called candidate_natural - Stage 2 does not run.")

    print()
    print("=" * 78)
    print("FULL CLASSIFICATION HISTORY")
    print("=" * 78)
    ev = registry.events()[event_db_id]
    for i, state in enumerate(ev.classification_history, start=1):
        print(f"  [{i}] {state.date.isoformat()}  stage={state.stage:7s} "
              f"label={state.label:25s} confidence={state.confidence}")


if __name__ == "__main__":
    main()
