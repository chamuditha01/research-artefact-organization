# project.md - Progressive Driver Attribution for Satellite-Detected Forest Loss
 
> **RESUME POINTER (2026-09-19).** The 30-event curated reference set is **COMPLETE and
> FROZEN** (REF_001-REF_058 screened: 30 confirmed, 18 uncertain, 10 false positive). It
> is idle - no threshold work, no driver labels - until the calibration batch is done.
> Current task: screening a **separate 20-event calibration batch, CAL_001-CAL_020**, to
> set the sustained-loss duration threshold and the remaining `[T#]` values
> (decisions.md 2026-09-19). Queue CSV `CAL_screening_queue_seed99.csv`, seed 99, same
> four sites. Polygon asset `projects/gsignin-501704/assets/CAL_screening_queue_poly`
> (rebuilt 2026-09-19 - the original CSV upload had EMPTY geometry; see issues.md B16).
> Logging file `calibration_batch.csv`. **Screened so far: CAL_001 (uncertain),
> CAL_002 (pending A/B decision). 18 to go.**
> **Do not touch the REF set.** Full history in decisions.md and issues.md.
> The Kahalla random batch (seed 42) failed 0/10 and is closed; do not restart it.
 
> **STALE - NOT UPDATED SINCE 2026-09-19.** This whole resume pointer, and the "Where I
> am right now" section below, describe the CAL batch and REF driver-labelling as
> still pending. Both are actually done as of 2026-09-27: CAL batch complete (20/20,
> class shares recorded in labelling_protocol.md), REF set driver-labelled (30/30, see
> ref_labelling_record.md), including three post-completion reclassifications
> (REF_025, REF_012, REF_058) under a corrected `[T7]` rule that closed issues.md B18
> (decisions.md, 2026-09-27). This file needs a proper rewrite of its resume pointer
> and "Where I am right now" section before it's trusted again for planning - flagged,
> not yet done, since that's a bigger edit than this session had time for.
 
> **Three days to the internal design freeze (2026-09-22). 31 days to the panel.**
> **The freeze date has now passed (today: 2026-09-27) with at least one open item -
> issues.md B18 - still being worked past it; see decisions.md 2026-09-27 entries.**
> Before the freeze, decide what is NOT being built. See "Build status" below.
 
_Last updated: 2026-09-19 (see staleness note above - not yet rewritten)_
 
> Paste this whole file at the start of every session (warm start, §5.2 of the guide).
> Keep it current. Anything in [square brackets] is still mine to fill in.
 
## Identity
- Student: [name / ID]
- Module: [code] · Supervisor: [name]
- Full title: Progressive Driver Attribution for Satellite-Detected Forest Loss in
  Sri Lanka's Protected Areas: A Design Science Study
_Working title, changed 2026-08-20: detection + classification is the core; the
accountability component is removed and alerting is no longer claimed as a
contribution. **This was my own scoping decision, not supervisor guidance** - I
decided and argued for the removal. It was then **raised with the supervisor on
2026-08-21 and approved**, which he treated as a scope change rather than as
something never in scope; his reading governs, so the removal is now sanctioned as
well as reasoned. His word was "blockchain", and the removal also covers the mobile
field-evidence prototype - confirm that in writing (A10). See decisions.md. The
title remains a working one and needs settling before submission, not before a
supervision meeting._
 
## Problem statement (current version)
Satellite monitoring can detect that forest cover has changed, but a detection on
its own does not give the likely disturbance driver - and the driver is what
determines whether a response is needed and what kind. Three things follow.
 
First, the final distinction between drivers is often unavailable at first
detection. Cultivation and permanent encroachment separate only once later
persistence or recovery evidence arrives, so a system that waits for certainty
reports late, and a system that forces an immediate final label reports wrongly.
 
Second, disturbance signals are confounded by season. Normal phenological
variation can resemble canopy loss, and the seasonal rhythm of the cleared land is
itself part of what distinguishes cultivation from permanent conversion. A method
that removes all seasonality destroys the signal it needs; a method that removes
none produces false detections.
 
Third, both problems change form across the country. Sri Lanka's protected areas
span different climatic zones with different phenology and different dominant
disturbance patterns, so a method calibrated on one area does not transfer without
explicit, documented recalibration.
 
**Gap.** The Global Drivers of Forest Loss product covering Sri Lanka
(Sims et al., 2025) assigns a dominant driver to approximately 1 km grid cells
over a multi-year mapping period. This differs from the event-level attribution
needed for protected-area management, where decisions concern a specific
forest-loss event rather than the dominant driver of the surrounding grid cell.
The temporal mismatch is not simply how often the product is updated, but that it
does not maintain an individual event whose driver attribution can be revised as
new post-disturbance evidence becomes available. There is also a spatial mismatch
because a single 1 km cell may contain several smaller forest-loss events with
different causes. Although the current dataset provides class probabilities at
cell level, it does not maintain event-specific confidence together with a
history of successive attribution revisions. This study therefore designs and
evaluates an event-level, confidence-aware and progressively revisable
driver-attribution artefact for forest-loss events in Sri Lankan protected areas,
enabling each detected event to be interpreted and updated individually as new
evidence accumulates.
 
<!-- Written 2026-08-21, closing G1b. RESTORED 2026-09-27: the class-probabilities
     sentence was cut on 2026-08-21 because it was unverified. Verified 2026-09-27
     against the actual paper (via a WRI-hosted mirror PDF, not the IOPscience page
     directly - that page blocks automated fetching) and logged in sources.md: the
     product does produce per-class probability maps in addition to the dominant-
     driver map. The paragraph above now reads with that sentence restored. Still
     worth reading the primary IOPscience article yourself before final submission,
     per sources.md's own caveat on this entry. -->
 
## Research aim
To design and evaluate an integrated artefact that detects new forest canopy-loss
events across Sri Lanka's protected-area network and progressively attributes the
likely disturbance driver, carrying an explicit confidence and revising the
attribution as later evidence arrives.
 
The artefact is designed to be **site-independent**: season- and zone-dependent
quantities (forest/reference baseline, detection threshold, phenological
correction) are treated as calibrated parameters of one method, not as constants.
 
**Coverage claim, stated precisely.** Detection is *applied* across the protected-
area network. Detection performance is *measured* on a stratified sample of areas
spanning the climatic zones. Classification performance is *measured* on a labelled
subset only. No performance figure is reported for any area that was not evaluated,
and the distinction between applied and evaluated is stated wherever coverage is
discussed - including in the abstract.
 
## Solution objectives (v2)
 
1. **[must-have, testable]** Develop a multi-temporal satellite-based **monitoring
   approach** that detects and maps new forest canopy-loss events across Sri Lankan
   protected areas round by round, using Sentinel-2, with Sentinel-1 as complementary information where the
   feasibility assessment supports a defensible role, and with a
   seasonally-corrected forest/reference baseline calibrated per climatic zone.
   _Tested by:_ E1 - precision / recall / F1 and spatial agreement against reference
   interpretation and a simple change-detection baseline, on a stratified sample of
   areas; E4 - detection latency with cloud/revisit gap reported separately.
2. **[must-have, testable]** Create a framework that attributes detected loss events
   to an initial bounded class set (cultivation, natural disturbance, permanent
   encroachment) in **two stages**: an early human-vs-natural decision from
   Sentinel-2-derivable geometry and context, and a later cultivation-vs-permanent-
   encroachment decision from the recovery trajectory. Each stage carries an
   explicit confidence, permits `uncertain`, revises as later evidence arrives, and
   is robust to the season in which the event occurred.
   _Tested by:_ E2 - Stage 1 and Stage 2 accuracy separately **and** the end-to-end
   three-class result, on held-out labelled events vs a simple baseline classifier,
   reported by label provenance; E3 - revision accuracy as a function of time since
   detection; E6 - performance stratified by event season and by climatic zone.
3. **[must-have, testable]** Evaluate the artefact at network scale, establishing
   where the method holds, where it needs recalibration, and what remains
   unevaluated.
   _Tested by:_ E1-E7 in methodology.md, including E7 - which parameters required
   per-zone recalibration and how much performance is lost without it - and an
   explicit statement of evaluated vs unevaluated coverage.
_Nice-to-have (only if the pilot leaves room):_ comparison of detection timing
against an existing public alert product; analysis of how early in an event's life
the driver becomes reliably predictable.
 
## The artefact
- **What it is:** one integrated detection-and-attribution pipeline, not separate
  systems.
- **How it runs:** as a **monitoring loop**, not a one-off analysis. Each round takes
  the next usable observation over a protected area and compares it against the
  stored reference. A change that survives the seasonal adjustment becomes a
  candidate event and enters classification. Events are therefore *produced by* the
  pipeline; they are not supplied to it.
- **Components:** (a) multi-temporal Sentinel-2 (+ Sentinel-1) detection in Google
  Earth Engine, run per monitoring round; (b) **reference management** - a forest
  state that is held stable plus a per-zone seasonal norm that is updated each
  round; (c) progressive, confidence-aware two-stage driver classifier; (d) event
  registry that maintains persistent event identity so repeated observations of one
  disturbance update one record rather than creating several.
- **Baseline creep is the named failure mode.** If the forest reference is refreshed
  to match current conditions every round, a slowly expanding clearing never
  registers as change, because each round differs only slightly from the last. The
  seasonal norm updates; the forest state does not. Forest state changes only when a
  loss is confirmed and classified, and that change is logged.
- **Core design principle:** an event is persistent. Detections and classification
  revisions attach to the same event; earlier classification states are retained,
  never overwritten. This is **supporting machinery, not a claimed contribution**
  (supervisor guidance 2026-08-20).
- **Hard constraints:** one final-year individual project; free/open satellite data
  only; classification limited to what a modest labelled sample supports; labelling
  is single-labeller and does not scale with area.
## Build status (added 2026-09-19)
 
**Nothing in "Components" above is built yet.** What exists is shared GEE plumbing -
cloud masking, NBR, polygon reduction, tile handling, export - plus the screening and
time-series tooling used to make reference data. That plumbing feeds (a), (b) and the
feature extractor, but it is not the artefact.
 
| Component | Blocked by labelling? | Status |
|---|---|---|
| Seasonal correction (per-zone) | no | not started; method not chosen (D3) |
| Detection loop vs held reference | no | not started; screen v1/v2 both rejected |
| Reference management (held forest state + seasonal norm) | no | not started (D10) |
| Event registry + duplicate handling | no | **first version built 2026-09-27** - `event_registry.py`, matching rule per D7 (decisions.md), tested against real B17 coordinates (`test_event_registry.py`, 6/6 passing). Not yet wired to real detection output (detection loop still not started) or to the classifier (`add_classification` exists but nothing calls it yet). |
| Feature extraction + window firewall assertions | **yes, was** | driver labels now exist (REF 30/30, 2026-09-27) - status not re-checked this session, needs confirming |
| Stage 1 classifier | **yes, was** | driver labels now exist - not re-checked this session |
| Stage 2 classifier | **yes, was** | driver labels now exist - not re-checked this session |
| Progressive revision + confidence + version history | **yes, was** | blocked on the above |
 
**Roughly 60% of the build is NOT blocked by the calibration batch.** The detection
half can be built in parallel with labelling. Do not queue it behind it - and now
that labels exist, check whether the labelling-blocked rows above have actually been
started, since this table has not been re-verified since 2026-09-19.
 
## Scope
 
**In:**
- Detection applied across Sri Lankan protected areas, subject to a usable
  boundary dataset existing and GEE processing being feasible at that extent
  (both to be confirmed in the feasibility assessment).
- Detection evaluated on a **stratified sample** of protected areas spanning
  climatic zones, with the sampling rule documented before evaluation.
- Classification evaluated on a labelled event subset, with label provenance
  recorded per event.
- Three initial driver classes: cultivation, natural disturbance, permanent
  encroachment - probabilistic attribution, not legal or enforcement
  determination. Reducible to two classes if the data does not support three.
- Seasonal correction and per-zone parameter calibration, with the recalibration
  itself recorded and reported as a result.
- Event registry and duplicate handling as machinery, checked for correctness but
  not claimed as novelty.
- Historical data for reference construction, reference labelling and retrospective
  evaluation; operational simulation of the monitoring loop after a defined
  monitoring start point.
- The incident source used **on the evaluation side only** - as a recall check
  (which reported events did the pipeline find?) and to seed labelling. It is not a
  pipeline input, because the pipeline generates its own events.
**Out:**
- **Response accountability, tamper-evident logging, the ledger/anchoring mechanism
  and the mobile field-evidence prototype.** Removed 2026-08-20 as an own scoping
  decision - never in the approved scope; see decisions.md. All associated
  requirements, threat-model rows and evaluation items are withdrawn with them.
- Alerting framework as a claimed contribution. Event identity is retained as
  machinery; no novelty claim is made for it.
- Any performance claim for protected areas not actually evaluated. National
  applicability is argued as a design property tested on a stratified sample, never
  as measured nationwide performance.
- Near-real-time or deployed notification delivery. Evaluation is retrospective
  operational simulation; there is no institutional deployment and no operator.
- Real-time on-satellite processing; production infrastructure of any kind.
## Where I am right now
 
> **This section is STALE - see the note at the top of the file.** It still says
> step 3 is "barely started" and lists the calibration batch and REF labelling as
> not-yet-done next actions. Both are done (2026-09-27). Read ref_labelling_record.md,
> issues.md and decisions.md for current state until this section is properly
> rewritten.
 
- Current step: **1-2 complete; 3 (design & build) barely started.** See Build status.
- ~~**Hard deadline: supervisor meeting 2026-08-21**~~ **PASSED.** Feasibility report
  delivered; accountability removal approved (A1 closed, residual A10 open).
- **Current deadlines (set 2026-09-08):**
  - **2026-10-20 - panel.** Deliverable is **artefact + results**, not the written
    dissertation. Writing follows.
  - **2026-10-31 - submission.** Eleven days of writing tail, survivable only because
    Chapter 1 and Chapter 3 drafts already exist. Chapter 2 is written *during* the
    build, not after the panel.
  - **2026-09-22 - internal design freeze.** No new design decisions after this date.
    Anything found later becomes a Chapter 5 limitation, not a redesign. This project
    has improved structurally every week; that has to stop for it to ship.
    **Passed 2026-09-22. At least one post-freeze design decision was made anyway
    (the [T7]/B18 correction, decisions.md 2026-09-27) - judged necessary rather than
    deferred to Chapter 5. Worth a conscious, stated call on whether that was the
    right choice, not something to let slide unremarked.**
- **Sinharaja is detection-only (decisions.md 2026-09-08).** No labelled subset, no
  classification result, no classification transfer figure. E7 measures zonal
  recalibration cost on **detection** alone. Classification is measured at the
  calibration site only and every classification figure is stated as dry-zone.
  Taken on schedule grounds before M13 was measured - recorded as such in the entry.
- ~~**Sequencing (decisions.md 2026-08-20):** build and calibrate on **Wilpattu** (dry
  zone, primary), transfer to **Sinharaja** (wet zone) to measure recalibration cost,
  then apply detection across the network.~~
  **SUPERSEDED 2026-09-09 and 2026-09-12. Do not act on the struck text above.**
  **Wilpattu is demoted to a low-disturbance dry-zone DETECTION CONTRAST site** - it
  contains ~18 loss events in six years and cannot support calibration (decisions.md
  2026-09-09). **Kahalla - Pallekele (Sanctuary, Dry Zone) is the frozen
  classification / calibration site** (decisions.md 2026-09-12). Sinharaja remains the
  wet-zone detection-transfer site. All three are frozen; any change is a new entry.
  Reference and calibration events are drawn from **four** sites - Kahalla-Pallekele,
  Nuwaragala, Maduroad, Victoria Randenigala Rantambe. This is the order of work,
  **not** the scope - network-scale application and stratified-sample evaluation are
  unchanged. Two purposive sites are not a stratified sample and no result from them
  may be described as one. Climatic-zone assignment is **unverified** until logged
  against a primary source in sources.md (B8).
- Next actions, in order (issue IDs per issues.md):
  1. **~~Write the gap statement (G1b).~~ DONE 2026-08-21**, sentence restored
     2026-09-27 once verified - see the paragraph above and sources.md.
  2. **~~Record the Sims et al. 2025 verification in sources.md (A6).~~ DONE
     2026-09-05, extended 2026-09-27.** Resolution, class list, logging definition,
     validation method and accuracy, and the class-probabilities claim are now
     confirmed - see sources.md. Still open: exact "dominant" tie-breaking rule,
     and training/reference sample counts by region (G5).
  3. **~~Settle the 2017 start date.~~ DONE 2026-09-08** - period is 2019-2024,
     fixed by measured L2A archive completeness. Landsat is **not** an input;
     Sentinel-2 with Sentinel-1 by availability. S1 optional-vs-necessary is still D2,
     decided by M1 (partly answered 2026-09-27 - REF by-month figure now exists,
     CAL by-month still pending).
  4. **~~Rerun candidate_screen.js over the decided period.~~ SUPERSEDED** - the
     self-built screen was rejected twice and the sampling frame is now Hansen
     (decisions.md 2026-09-08).
  5. **~~Create the batch CSV header before labelling anything.~~ DONE.** REF used
     `calibration_batch_record.csv`; CAL uses `calibration_batch.csv`, corrected
     2026-09-19 to restore the twelve protocol §7 fields the first header dropped
     (`t_forest`, `t_loss`, `interval_days`, `decision_path`, `structural_indicators`,
     `R_at_T3`, `R_at_T4`, the three `n_clear_*`, `highres_provider`,
     `logging_or_harvest`) plus `core_pixels_after_erosion` and `uncertain_triggers`.
  6. **~~Screen the 20-event calibration batch (CAL_001-020).~~ DONE.** 20/20
     labelled, class shares recorded in labelling_protocol.md (frozen v1.0,
     2026-09-22): uncertain 35%, cultivation 25%, permanent_encroachment 15%,
     false_positive 15%, natural 10%.
  7. **~~Freeze labelling_protocol.md.~~ DONE**, frozen v1.0, 2026-09-22.
  8. **~~Driver-label the 30 REF events under the frozen protocol.~~ DONE
     2026-09-27.** 30/30 labelled; three reclassified same day under a corrected
     `[T7]` rule (REF_025, REF_012 -> permanent_encroachment; REF_058 ->
     cultivation) - see ref_labelling_record.md and decisions.md.
  9. **Start the unblocked build components in parallel** - event registry first (plain
     code, no labels needed), then reference management and the detection loop.
     **Status not verified this session - check before assuming not started.**
  10. **~~Measure clear observations inside the event polygon, by month (M1).~~
      PARTLY DONE 2026-09-27.** REF-side by-month figure computed (see issues.md
      M1): clear March-April, sparse November-December, consistent with the NE
      monsoon. Pooled across all 4 sites, not yet split by climatic zone. CAL-side
      by-month still not computed (only by-year exists).
  11. **Test GEE processing cost at network extent (B5/M5).** Still open.
- **Gate after the calibration batch:** measured M4 x target reference-sample size must
  fit the available hours. **CAL batch is done - this gate should be checked now,
  not left as a future step.**
- **Closed since this file was last accurate:** loss-date method decided (B1 -
  interval, not point estimate); boundary dataset found (B2 - WDPA, 679 Sri Lankan
  polygons); external training data settled (D1 - Sri Lankan events only); site
  selection frozen (2026-09-12, Kahalla-Pallekele); home-garden rule frozen (B9);
  30-event curated reference set complete and frozen (2026-09-19); **CAL batch
  complete (2026-09-22 or before); labelling_protocol.md frozen v1.0 (2026-09-22);
  30-event REF set driver-labelled (2026-09-27); G2 logging-class question decided
  (2026-09-24, REF-side count added 2026-09-27); M10/B3/B4 prevalence question
  answered (2026-09-27); issues.md B18 gradual-event-dating problem resolved
  (2026-09-27).**
- **Live and unresolved:** the labelling protocol is now frozen and both batches are
  labelled, so the earlier "driver labels do not exist" framing below is out of
  date - kept struck-through rather than deleted, per the reversal-tracking rule.
  ~~driver labels do not exist in the incident source, so per-class counts cannot be
  obtained by counting it. The curated REF set cannot give prevalence either (M20),
  so B3/B4 are answerable only in the narrow form the random CAL batch supports -
  prevalence among Hansen-detected loss in four dry-zone protected areas, n small.
  The labelling protocol (labelling_protocol.md) is in draft and cannot be frozen
  until the CAL batch is run and every `[T#]` is set.~~ **All of this is now done.**
## Open questions (deliberately deferred, not vague)
- **Is selective logging observable, and if so where does it go (G2)?** **CLOSED
  2026-09-24, REF-side count added 2026-09-27 - see issues.md.** Logging stays
  pooled into `uncertain`, flagged `logging_or_harvest`, excluded from the taxonomy
  with a stated reason. Measured on both sets independently: CAL 2/20 (10%), REF
  3/30 (10%).
- **What counts as a protected area (A9/D11).** \"Other State Forest\" and \"Reserved
  Forest\" may carry weaker legal protection than a national park. The project claims
  to monitor *protected areas*; pooling designations of different legal status needs
  justifying before detection runs. **Live in the data:** the CAL batch is 12
  Sanctuary and 8 Reserved Forest events pooled in one calibration sample. **Still
  open as of 2026-09-27.**
- **How to date a GRADUAL event (opened 2026-09-19, issues.md B18).** **RESOLVED
  2026-09-27** - see decisions.md. `[T7]`'s reject-to-`uncertain` rule does not
  override a class when Step 1 structural evidence and Step 3/4 trajectory
  independently and clearly agree, even without a clean date bracket. This
  corrects an inconsistency found by checking how CAL_005 (this issue's original
  example) was actually labelled - it never went through `[T7]` at all. Reopened
  and reclassified REF_025, REF_012 (both now permanent_encroachment) and REF_058
  (now cultivation) under the corrected rule.
- **Stage 2's feature window (see labelling_protocol.md §3).** Stage 1 and Stage 2
  cannot share one feature window - Stage 2 needs recovery trajectory, which takes
  longer to accumulate. Two windows, with the later one still closing before the
  label window opens.
- **What counts as \"recovered\" (opened 2026-09-19).** `sustained_drop_duration_days`
  cannot be computed without a recovery level. On CAL_001 the first drop lasts 160
  days or 295 days depending only on where that level is set. **The rule must be
  written down before the batch continues**, or the 20 durations are not comparable
  and the threshold derived from them means nothing. **Status not re-checked this
  session - the CAL batch is complete, so this should already be resolved somewhere;
  confirm where.**
- **Class count.** Three classes or two. Decided from the calibration batch, not
  before. **CAL batch is done (see above) - this should be checked now rather than
  left as still-pending; final REF breakdown (cultivation 13, permanent_encroachment
  6, natural 1, uncertain 10) and CAL breakdown (cultivation 5, permanent_encroachment
  3, natural 2, false_positive 3, uncertain 7) both show all three classes populated
  with real events, which is evidence for keeping three, not a decision to do so.**
- **Stratified sampling rule for evaluation.** How many areas per climatic zone,
  and selected how. Must be written down *before* evaluation, not after seeing
  results. **Still open.**
- **Seasonal correction method.** How background phenology is removed while
  event-level seasonal cycling is preserved as a classification feature. These pull
  in opposite directions and the method must do both. **Still open.**
- **Monitoring round trigger.** Every new usable observation, or a fixed interval?
  Measured in-polygon cadence is 18-34 clear observations a year at most CAL sites
  and ~72 at one, so this varies by orbit geometry, not only by cloud. REF-side
  figure now also exists (22.5-34.2/yr, no comparable outlier) - see issues.md M1.
  Affects E4 latency directly. **Still open as a design decision.**
- **Reference update rule.** Exactly when the forest state is allowed to change, and
  on what evidence. Must be written down - this is where baseline creep enters.
  **Still open.**
- **Sentinel-1's role.** Given the low clear-observation count, radar may be
  necessary rather than optional for narrowing loss dates and filling the feature
  window. Decided from the observation-count measurement (M1, now partly answered).
  **Still open as a decision, though M1's REF-side figure is now available to
  inform it.**
- **Practical minimum reliable event size** - an evaluation output stratified by
  reference-event size, not a pre-set parameter (decisions.md 2026-08-17).
  **First real evidence, 2026-09-19:** half the CAL batch is under 1 ha. A 0.53 ha
  patch is ~53 pixels at 10 m; eroding two pixels leaves 4-10, and eroding three
  leaves nothing for ten of the twenty events. `[T5]` and `[T15]` are not independent
  choices (issues.md M22). **Still open.**
- **Exact classification algorithm** - follows from final sample size, feature
  behaviour, class balance and interpretability. **Still open; sample size question
  is now answerable since both batches are labelled.**
## Claims I am not making (guardrail list)
- No nationwide *performance* claim. Applied nationally, measured on a sample.
- No near-real-time claim.
- No legal or enforcement determination from a driver label.
- No figure about Sri Lankan forest cover, protected-area extent, Sentinel revisit
  or cloud cover that is not either my own recorded measurement or a primary source
  logged in sources.md.
- No calibrated-parameter claim for any `[T#]` derived from the CAL batch until the
  usable-event count behind it is stated. **CAL batch is now complete - check
  whether this guardrail's premise ("likely under ten events") still holds, or
  whether it needs updating now that the real count is known.**