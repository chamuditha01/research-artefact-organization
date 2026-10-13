"""
demonstrate_ref031.py
 
THE dissertation demonstration case (methodology.md Step 4, decisions.md
2026-09-29 "Demonstration case selected: REF_031"). Kept separate from
evaluation (SKILL.md guardrail) - this shows the artefact works AT ALL on
one real event, not how well it performs in general. No accuracy claim is
made or implied anywhere in this script.
 
REAL INPUTS ONLY, nothing synthetic:
  - Real polygon geometry: claude/ref031_geometry.geojson, pulled from GEE
    2026-09-29 (claude/pull_ref031_geometry.js), verified against
    features_REF_merged.csv's stored area (matches to 5 significant
    figures) and against ref_labelling_record.md's "2-part MultiPolygon"
    note (confirmed: 2 parts, one with an interior ring).
  - Real Stage 1 / Stage 2 features: features_REF_merged.csv's REF_031 row,
    already extracted from real Sentinel-2 imagery.
  - Real dates: t_forest=2022-06-26, t_loss=2022-08-10
    (ref_labelling_record.md #29).
 
WHAT THIS DEMONSTRATES (per methodology.md Step 4's four required parts):
  1. Detection            - round 1: the real footprint enters the registry
                             as a brand-new tracked event.
  2. Event creation with
     provisional driver     - round 1: Stage 1 runs on the real Stage-1-
     and stated confidence   window features, producing a provisional
                             candidate_human / candidate_natural call.
  3. A later observation
     attaching to the
     same event             - round 2: the SAME real footprint is seen
                             again (it has not recovered - see
                             ref_labelling_record.md's note that REF_031
                             was still "mid-dip" as of 2026-09-23). The
                             registry's location-only matching rule
                             (decisions.md 2026-09-27) attaches this to
                             the existing event, not a new one.
  4. A classification
     revision                - round 2: Stage 2 runs on the real Stage-2-
                             window features, producing a specific driver
                             label (cultivation / permanent_encroachment)
                             that supersedes round 1's coarser call - a
                             real revision, appended to history, not
                             overwritten (event_registry.py's own design
                             rule).
 
WHAT THIS DOES NOT SHOW (state this plainly in the write-up, per
methodology.md's own instruction):
  - It does NOT show the classifier generalising to unseen data. REF_031
    is one of Stage 2's 19 training events (decisions.md 2026-09-29,
    "Demonstration case selected: REF_031" - "What I gave up"). This is a
    stated limitation, not a hidden one.
  - It does NOT show quarterly re-classification. The built system
    classifies each stage once, at a fixed window (decisions.md
    2026-09-29 "even later" entry, the scope-gap decision). Round 1 and
    round 2 here are Stage 1 and Stage 2's single fixed-window classifi-
    cations, not two points on a repeating quarterly cycle.
  - It does NOT show detection itself (the detection loop is out of
    scope - issues.md, 2026-09-28 scope-cut note). Round 1's "detection"
    is the real, already-confirmed REF_031 polygon fed in directly, not
    output from a running monitoring loop.
  - It is ONE event. No claim of typicality - SKILL.md's "never present a
    cherry-picked best case as if it were typical" guardrail applies.
"""
 
import json
from datetime import date
 
from event_registry import EventRegistry, ClassificationState
from classifiers import stage1_classify, Stage2Classifier, STAGE2_FEATURES
 
EVENT_ID = "REF_031"
T_FOREST = date(2022, 6, 26)
T_LOSS = date(2022, 8, 10)
 
# decisions.md 2026-09-28 "later still, again" (Stage 1) / 2026-09-28
# "[T2b] set as a rounded conservative floor" (Stage 2) - these are the
# FLOOR lengths the classifiers were actually built and calibrated against
# (feature_extraction_v1.js's fixed one-shot windows - see decisions.md
# 2026-09-29 "even later" entry for the stated gap against the later
# quarterly design). Round dates below mark when each floor is first met.
STAGE1_WINDOW_DAYS = 60
STAGE2_WINDOW_MONTHS = 12
 
 
def add_months(d: date, months: int) -> date:
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    day = min(d.day, 28)  # simple, safe day-of-month floor for this script's purposes
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
    ref031 = next(r for r in rows if r["event_id"] == EVENT_ID)
 
    with open("ref031_geometry.geojson") as f:
        geojson = json.load(f)
    real_geometry = geojson["features"][0]["geometry"]
 
    stage2 = Stage2Classifier.fit_from_labelled_events(rows)
    print(f"Stage 2 fitted on n={stage2._n_train} labelled events "
          f"(REF_031 is one of them - see script docstring, 'What this does not show')\n")
 
    registry = EventRegistry()
 
    round1_date = T_LOSS.__class__(T_LOSS.year, T_LOSS.month, T_LOSS.day)
    round1_date = date.fromordinal(T_LOSS.toordinal() + STAGE1_WINDOW_DAYS)
    round2_date = add_months(T_LOSS, STAGE2_WINDOW_MONTHS)
 
    # --- Round 1: detection + event creation + Stage 1 provisional label ---
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
    print(f"Real footprint: MultiPolygon, {ref031['area_ha']:.3f} ha "
          f"(area_ha column, features_REF_merged.csv)")
 
    s1 = stage1_classify(ref031)
    registry.add_classification(event_id, ClassificationState(
        round_id="round_1", date=round1_date, stage="stage1",
        label=s1.label, confidence=s1.confidence, evidence_note=s1.evidence_note,
    ))
    print(f"\nStage 1 classification (provisional):")
    print(f"  label:      {s1.label}")
    print(f"  confidence: {s1.confidence}")
    print(f"  evidence:   {s1.evidence_note}")
 
    # --- Round 2: later observation of the SAME footprint + Stage 2 revision ---
    print()
    print("=" * 78)
    print(f"ROUND 2 - {round2_date.isoformat()} "
          f"(t_loss + {STAGE2_WINDOW_MONTHS} months, Stage 2 window closes)")
    print("=" * 78)
 
    summary2 = registry.process_round(
        round_id="round_2",
        round_date=round2_date,
        raw_candidate_geoms_wgs84=[real_geometry],  # same real footprint, seen again
    )
    print(f"Registry match: {summary2}")
    assert summary2["updated_events"] == [event_id], (
        "expected round 2 to attach to the SAME event as round 1, not create a new one"
    )
    print(f"Confirmed: round 2's detection attached to the SAME event ({event_id}), "
          f"not a new one - the registry's location-only matching rule "
          f"(decisions.md 2026-09-27) at work, on real repeated data.")
 
    if s1.label == "candidate_human":
        s2 = stage2.classify(ref031)
        registry.add_classification(event_id, ClassificationState(
            round_id="round_2", date=round2_date, stage="stage2",
            label=s2.label, confidence=s2.confidence, evidence_note=s2.evidence_note,
        ))
        print(f"\nStage 2 classification (revision):")
        print(f"  label:      {s2.label}")
        print(f"  confidence: {s2.confidence}")
        print(f"  P(permanent_encroachment): {s2.probability_permanent:.3f}")
        print(f"  evidence:   {s2.evidence_note}")
    else:
        print("\nStage 1 called candidate_natural - Stage 2 does not run "
              "(cascade design, decisions.md 2026-08-20). No revision this round.")
 
    # --- Full classification history, as the registry actually holds it ---
    print()
    print("=" * 78)
    print("FULL CLASSIFICATION HISTORY (event_registry.py - append-only, nothing overwritten)")
    print("=" * 78)
    event = registry.events()[event_id]
    for i, state in enumerate(event.classification_history, start=1):
        print(f"  [{i}] {state.date.isoformat()}  round={state.round_id:8s} "
              f"stage={state.stage:7s} label={state.label:25s} confidence={state.confidence}")
 
    label_changed = (
        len(event.classification_history) == 2
        and event.classification_history[0].label != event.classification_history[1].label
    )
    print()
    if label_changed:
        print(f"REVISION CONFIRMED: round 1 called '{event.classification_history[0].label}', "
              f"round 2 revised this to '{event.classification_history[1].label}'.")
    elif len(event.classification_history) == 2:
        print(f"Both rounds reached the same specific label "
              f"('{event.classification_history[1].label}') - Stage 1's coarser "
              f"'{event.classification_history[0].label}' call was REFINED into a specific "
              f"driver class, which is still a revision (a coarse provisional call becoming a "
              f"specific one), even though the two labels are not literally different strings.")
 
 
if __name__ == "__main__":
    main()
 