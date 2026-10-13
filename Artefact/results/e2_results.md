# E2 results - per-stage and end-to-end classification accuracy
 
_Logged 2026-10-02. This is a measurement/result, not a design decision, so it
sits in its own file rather than decisions.md. Cross-reference: issues.md's
critical path lists "E2 (per-stage + end-to-end accuracy)" as the next step
after D6 closed (2026-09-29) - this closes that step._
 
## Method
 
Population: the **frozen REF evaluation set only** (never the CAL calibration
batch - mixing them would violate the evaluation-integrity rule). Of REF's 30
confirmed events, the **20 with a resolved 3-class label**: 13 cultivation-side
(12 `cultivation` + 1 `cultivation_pasture`), 6 `permanent_encroachment`,
1 `natural`. The 10 `uncertain` REF events (including the 3 logging-pooled
ones) are excluded - they have no resolved ground truth to score against.
 
- **Stage 1** (human vs natural): the hand-set threshold rule from
  `classifiers.py` (decisions.md, 2026-09-28) is a fixed rule, not a fitted
  model, so it was run directly on all 20 events - no retraining needed.
- **Stage 2** (cultivation vs permanent_encroachment): logistic regression,
  **leave-one-out cross-validation** over the 19 Stage-1-"human" events - for
  each event, fit on the other 18, predict the held-out one. Same method as
  `stage2_loocv.py` (decisions.md, 2026-09-29); numbers match.
- **End-to-end**: for each of the 20 events, run Stage 1 first. If it says
  `candidate_natural`, the final prediction is `natural` (no Stage 2 call -
  matches real pipeline behaviour). If `candidate_human`, the final
  prediction is that event's Stage 2 LOOCV prediction. A Stage 1 mistake is
  therefore unrecoverable in this count, same as the cascade-error limitation
  already stated in decisions.md (2026-08-20 two-stage entry).
Script: `claude/run_e2.py` (reproducible from `features_REF_merged.csv`).
 
## Result
 
| Measure | Result | n |
|---|---|---|
| Stage 1 alone | 19/20 = **95.0%** | 20 (1 natural) |
| Stage 2 alone (LOOCV) | 15/19 = **78.9%** | 19 (human subset only) |
| **End-to-end (cascade)** | **15/20 = 75.0%** | 20 |
 
Per-event misses:
- Stage 1: REF_020 (the one natural event - called `candidate_human`,
  confirming the existing finding that Stage 1 cannot currently call anything
  natural).
- Stage 2 (LOOCV): REF_058, REF_053, REF_013, REF_025.
- End-to-end: same four Stage 2 misses, plus REF_020 (misrouted by Stage 1,
  then scored against the full-fit Stage 2 model since it was never part of
  Stage 2's training/LOOCV population).
**End-to-end (75.0%) is lower than Stage 2 alone (78.9%)** - this is the
measured cascade cost. It is not large here because Stage 1 only ever
misroutes the one natural event; it would cost more with a larger or more
error-prone natural class.
 
## Caveats (do not drop these when this number is quoted elsewhere)
 
1. **n=1 for natural.** Stage 1's 95% is not a reliable rate for that class -
   SKILL.md's own guardrail. It is reported here only as a component of the
   end-to-end figure, never as a standalone Stage 1 accuracy claim.
2. **Feature-window mismatch, already flagged and accepted.** The features
   used here were extracted under `feature_extraction_v1.js`'s original
   fixed windows (T1=12mo, T2a=60d, T2b=12mo), not decisions.md's later
   design (T1=6mo, T2a=90-day floor, T2b=12-month floor, quarterly recheck).
   Stated as a known, accepted gap in `classifiers.py`'s own module
   docstring - not re-litigated here.
3. **Confidence bands are not validated by this result.** Stage 2's
   high/medium/low confidence labels are fixed margin bands, not calibrated
   against this accuracy figure. Whether "high confidence" predictions are
   actually more often correct is a separate check, not yet done.
4. **REF set only.** This is the frozen evaluation set, drawn from 4 sites,
   one climatic zone (dry). No claim is made beyond that - same coverage
   guardrail as everywhere else in this project.
## What this closes / what's still open
 
- Closes: issues.md critical path step "E2 (per-stage + end-to-end
  accuracy)".
- Still open, unaffected by this result: E3 (progressive revision /
  accuracy-over-time), demonstration (already done, REF_031), and every
  standing question in issues.md's open-questions list.
 