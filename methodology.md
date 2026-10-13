# methodology.md - How I'm Doing This (and the Evaluation Plan)
 
_Last updated: 2026-09-08_
 
## Approach in one paragraph
This project follows a Design Science Research approach: a real problem in forest
protection is identified, an integrated artefact is designed and built to address
it, the artefact is demonstrated on real cases from Sri Lankan protected areas, and
it is then evaluated against the solution objectives before the process and findings
are communicated. The artefact is one integrated pipeline - satellite detection,
seasonal correction, progressive driver classification and event identity are
components of it, not separate deliverables. Design choices and their trade-offs are
recorded in decisions.md as they are taken, and every model-supplied claim is
verified against a primary source before use (sources.md).
 
_Scope change 2026-08-20: the response-accountability component (field prototype,
tamper-evident log, external anchoring) is removed. **This was an own scoping
decision** - the component was never in the approved scope (decisions.md). Former
evaluation items E6-E9 are withdrawn. The evaluation plan below is renumbered._
 
## How each step is being carried out
 
**1. Problem.** Established from the research gap, peer-reviewed literature on
satellite-based forest-change detection and driver attribution, existing operational
alert products, and relevant Sri Lankan policy or institutional documents where
available. Requirement gathering is deliberately bounded to artefact design needs
rather than framed as a broad investigation of every limitation in current
institutional systems.
 
**2. Objectives.** Three solution objectives derived from the problem (see
project.md). Each is written so that a specific test in the evaluation plan below
can decide whether it was met. Requirements R1-R5 trace to design features and to
those tests (traceability table at the end of this file).
 
**3. Design & build.**
 
- *3a. Feasibility assessment before design freeze.* **Blocking check first:**
  confirm a usable protected-area boundary dataset exists for Sri Lanka, and that
  GEE can process the network extent for the study period. If either fails,
  network-scale detection is not feasible and the scope reverts to a sampled set of
  areas - log it rather than absorbing the failure silently.
  Then, per candidate area: usable Sentinel-2 observations measured **inside event
  polygons and broken down by month**, Sentinel-1 archive coverage, candidate event
  count and size, per-class event counts, and availability of historical
  high-resolution reference imagery. Inspect a random sample of candidate events -
  not the clearest ones - to check the three proposed classes are visually
  interpretable and sufficiently represented.
  The assessment fixes: climatic-zone strata and the stratified sampling rule,
  study and monitoring periods, initial class definitions, class count (three or
  two), and the intended role of Sentinel-1.
  *Build order (decisions.md 2026-08-20):* the assessment and the design build run
  first on **Wilpattu** (dry zone), then transfer to **Sinharaja** (wet zone) to
  produce the E7 recalibration figure, before network-wide application. This is
  sequencing only - it does not narrow the scope, and results from the pair are
  reported as a contrasting-pair transfer, never as a stratified sample.
  **Sinharaja is a detection-only transfer site (decisions.md 2026-09-08).** It
  carries no labelled subset and no classification result. This was fixed in advance
  on schedule grounds, not on measured event yield - M13 was not measured before the
  decision was taken, and that is recorded in the entry. E7 therefore reports zonal
  recalibration cost on **detection only**; classification is measured at Wilpattu
  (dry zone) alone and every classification figure is stated as such.
  **Abort rule:** if natural disturbance is absent from the incident source, or
  per-class counts cannot support held-out evaluation, drop to two classes and amend
  Objective 2 - do not proceed with a class the data does not contain.
- *3b. Detection as a monitoring loop.* The pipeline runs in rounds over each
  protected area rather than as a single retrospective pass. Each round: take the
  next usable Sentinel-2 observation (with Sentinel-1 as complementary information
  where the assessment shows a defensible role - low clear-observation counts may
  make radar necessary rather than optional), compare it against the stored
  reference after seasonal adjustment, and emit any surviving change as a candidate
  event with geometry, timing and supporting evidence. **Events are outputs of this
  loop, not inputs to it.**
- *3b-i. Reference management (and baseline creep).* Two stores, doing different
  jobs, updated on different rules:
  **Forest state** - what counts as forest at this location. Held stable. It changes
  only when a loss has been confirmed and classified, and the change is logged with
  its reason.
  **Seasonal norm** - what this forest normally looks like in this month, in this
  climatic zone. Updated each round; this is phenology, not loss.
  If the forest state is instead refreshed to current conditions every round, a
  slowly expanding clearing never triggers detection, because each round differs
  only slightly from the last. That failure mode is called **baseline creep** and it
  hides precisely the gradual encroachment the project exists to catch. The update
  rule is a decisions.md entry, and E1 must include at least one gradual-expansion
  event to show the loop catches it.
- *3c. Seasonal correction.* Background phenology (the seasonal signal of the
  surrounding forest) is removed or normalised per climatic zone. **Event-level
  seasonal behaviour of the cleared patch is preserved**, because a clear-grow-
  reclear cycle is a primary separator between cultivation and permanent
  conversion. These two requirements pull in opposite directions; the method must
  satisfy both, and the chosen approach is a decisions.md entry with its cost.
- *3d. Classification framework (two-stage).* Extract candidate temporal, spectral,
  geometric and contextual features from the **feature window only** (see
  labelling_protocol.md §3 firewall).
  **Stage 1 - human vs natural, early.** Features limited to what Sentinel-2
  resolves: patch shape and edge regularity, compactness, size, slope and terrain
  position, adjacency to existing cleared land or roads. The fine structural
  indicators used in labelling (buildings, tracks, plot subdivision) come from
  high-resolution imagery and are deliberately **not** available to the model - this
  is the resolution firewall, and it must be stated rather than glossed.
  **Stage 2 - cultivation vs permanent encroachment, later.** Applies to Stage 1
  "human" events only, using recovery-trajectory features.
  > **UNRESOLVED - fix in labelling_protocol.md §3 before any feature code is
  > written.** "As they accumulate" and the §3 firewall contradict each other. §3
  > defines a single feature window ending at `t_loss + [T2]` and forbids any later
  > observation from entering feature extraction, for any event, for any reason.
  > Stage 2 cannot work inside that window - recovery trajectory takes longer than
  > Stage 1 geometry. So Stage 2 needs its own, longer feature window, and that
  > window must still close before the label window opens, with a gap between them.
  > If Stage 2 features and Stage 2 labels are read off the same observations, E2
  > measures nothing. The two window lengths are calibration-batch outputs; the
  > *structure* is a decision to take now.
  Both stages produce a label plus confidence, permit `uncertain`, and revise as
  later evidence arrives; classification versions are preserved as event history
  rather than overwritten. Interpretable feature-based classifiers appropriate to
  the final sample size, compared against a simple baseline rather than committing
  to an algorithm before data inspection.
- *3e. Event registry (machinery).* Maintain a registry holding event identities,
  geometries, timestamps and current state, so repeated observations of one
  disturbance update one record. Compare each new candidate detection against the
  registry using calibrated spatial and temporal matching. Correctness is checked
  (E5) but **no novelty is claimed** for this component.
**4. Demonstration.** _(Keep separate from evaluation.)_
Proof of life on at least one real case: a genuine canopy-loss event carried
end-to-end - detection, event creation with a provisional driver and stated
confidence, a later observation attaching to the same event, and a classification
revision. The demonstration case must not be chosen because it is the easiest one;
record what conditions it did and did not cover, and state plainly that it shows the
artefact works at all, not how well.
- Demonstration case selected: **REF_031** (Nuwaragala, Reserved Forest; real
  polygon geometry, 2 parts, 2.58 ha; `t_forest`=2022-06-26, `t_loss`=2022-08-10).
  Selected by discussion, not for convenience - see decisions.md, 2026-09-29
  "Demonstration case selected: REF_031", for the full reasoning and the two
  rejected alternatives.
- What it showed: Run end-to-end on real inputs only (real GEE-pulled polygon,
  real extracted Stage 1/Stage 2 features, real dates - `claude/demonstrate_ref031.py`).
  Round 1 (2022-10-09, Stage 1 window closes): the real footprint entered the
  registry as a new tracked event; Stage 1 produced a provisional
  `candidate_human` label at high confidence. Round 2 (2023-08-10, Stage 2 window
  closes): the same real footprint was observed again (it had not recovered) and
  the registry's location-only matching rule (decisions.md 2026-09-27) correctly
  attached it to the SAME event, not a new one; Stage 2 then produced a specific
  driver label, `cultivation` at medium confidence (P(permanent_encroachment)=0.254)
  - a genuine revision from Stage 1's coarser call, appended to the event's
  classification history without overwriting round 1's entry. This confirms the
  two-stage cascade, the registry's spatial-matching/append-only design, and the
  classifiers all work together on one real event, not just in isolation.
- What it did **not** show:
  - Generalisation to unseen data. REF_031 is one of Stage 2's 19 training events
    (decisions.md 2026-09-29), so this does not show the classifier working on
    data it never saw - only that the pipeline runs correctly. E2 (held-out
    accuracy) is the test that would show generalisation, and remains separate.
  - Quarterly re-classification. The design calls for re-classifying every quarter
    on an accumulating window (decisions.md 2026-09-28); the built prototype
    classifies each stage once, at a fixed window (decisions.md 2026-09-29, "even
    later" entry - a stated scope gap, not an oversight). Round 1 and round 2 here
    are Stage 1's and Stage 2's single fixed-window classifications, not two points
    on a repeating cycle.
  - Detection itself. The monitoring/detection loop is out of scope for this build
    (issues.md, 2026-09-28 scope-cut note). Round 1's "detection" is the real,
    already-confirmed REF_031 polygon supplied directly, not the output of a
    running detection loop.
  - Typical performance, of any kind. This is one event. No claim is made or
    implied that it represents system-wide behaviour.
**5. Evaluation.** See the plan below.
 
**6. Communication.** Dissertation drafted from this file and decisions.md rather
than from scratch, with gaps marked rather than filled with plausible fiction. AI
use declared in the methodology or acknowledgements per programme policy.
 
## Evaluation plan
 
| # | Objective / area | Metric | Data / conditions | Baseline | Success threshold |
|---|---|---|---|---|---|
| E1 | Forest-loss detection (Obj 1) | Precision, recall, F1, omission/commission error, spatial agreement; reported **per climatic zone** and pooled; plus recall against the incident list as a separate figure, and at least one gradual-expansion case to test for baseline creep | Retrospective run of the monitoring loop over a **stratified sample** of protected areas; held-out reference interpretation; sampling rule written before evaluation; set disjoint from any threshold calibration data | Simple change-detection baseline (e.g. index-differencing at a fixed threshold); an existing alert product where suitable | [set before running - state it now, not after seeing results] |
| E2 | Driver classification (Obj 2) | **Stage 1** (human/natural) precision/recall/F1; **Stage 2** (cultivation/encroachment) precision/recall/F1; **and the end-to-end three-class** macro-F1 and confusion matrix. Per-stage figures alone flatter the system, because a Stage 1 error is unrecoverable - always report the cascade result alongside. Reported **by label provenance** (structurally confirmed vs trajectory-only) | Held-out labelled events; class balance reported per stage; Stage 2 trains on the human subset only, so its counts are smaller than the event total - report them; training and test events strictly disjoint | Simple classifier baseline (majority class + a single-feature rule) at each stage | [set before running] |
| E3 | Progressive classification (Obj 2) | Revision accuracy: how often a provisional label is corrected and in which direction; **accuracy as a function of time since detection** | Events with both early and later observations | Immediate-final-label variant of the same classifier | [set before running] |
| E4 | Detection latency (Obj 1) | Rounds-to-detection and observation-to-detection latency; **cloud/revisit gap reported separately** so pipeline delay is not hidden inside satellite revisit delay; state the round trigger used | Retrospective operational simulation of the monitoring loop from first eligible observation | Detection timing of an existing product, if comparable | [set before running] |
| E5 | Event identity (machinery) | Duplicate rate, fragmentation rate, merge-error rate; trade-off curve across thresholds | Historical event set held out from matching-threshold calibration | Stateless detection (one record per qualifying observation) | [set before running] |
| E6 | Seasonal robustness (Obj 2) | Detection F1 and classification macro-F1 **stratified by the season in which the event occurred**; false-detection rate during peak phenological change | Events binned by season; monsoon and dry-season periods analysed separately | Uncorrected baseline with no seasonal normalisation - the difference *is* the result | [set before running] |
| E7 | Zonal generalisation (Obj 3) | **Detection F1 across climatic zones** (classification transfer is not measured - Sinharaja is detection-only, decisions.md 2026-09-08); **which parameters required recalibration and by how much**; error modes unique to each zone | Method calibrated on one zone, applied to others with documented site-level recalibration only, no method redesign | Same parameters applied with **no** recalibration at all, to isolate how much of the method is zone-independent | [set before running - state the tolerable drop now, and state that a large drop is a reportable finding, not a failed objective] |
 
- **Strategy:** predominantly naturalistic (real imagery, real disturbances, real
  protected areas) and ex post throughout. There are no longer any artificial
  behavioural tests, since the accountability component that required them has been
  removed.
  _(Evaluation strategy organised in the FEDS framework - Venable, Pries-Heje &
  Baskerville. Verify the citation in sources.md before it goes in the chapter.)_
- **Known threats to validity (fill in as the adversarial pass finds more):**
  - Reference labels for driver class are interpreted, not ground-truthed; label
    error propagates directly into E2. Record who labelled, on what evidence, and
    the provenance split. Single-labeller: only intra-rater consistency is
    available, and it must be described as weaker than inter-rater agreement.
  - Labels are predominantly trajectory-derived, so the structural-evidence tier is
    the only fully independent evidence. Hence the provenance split in E2.
  - **Classification is measured in one climatic zone only.** Sinharaja is
    detection-only (decisions.md 2026-09-08), so no measurement exists of whether
    the two-stage classifier transfers between zones. Classification portability is
    argued from the method's design, not demonstrated. This narrows what E7 supports
    for Objective 3, and it must be stated wherever zonal generalisation is claimed.
    The decision was taken on schedule grounds before M13 was measured; that is a
    limitation of the study's execution, not a finding about Sinharaja.
  - **Applied nationally, measured on a sample.** A stratified sample supports a
    claim about the sampled strata, not about every protected area. Watch for this
    drifting upward in the abstract. Unevaluated areas remain unevaluated.
  - The incident source records *reported* events, so absence from it does not mean
    absence of loss. It is a **recall check only**: a detection missing from the list
    is not a false positive. Detection false positives must be checked against
    imagery, not against the incident list, or precision will be understated.
  - **Baseline creep.** A forest reference refreshed each round to current conditions
    silently suppresses gradual expansion. Report the update rule, and include
    gradual-expansion cases in E1 rather than only abrupt clearings.
  - Training data is Sri Lankan only (decisions.md 2026-08-20), so no domain-shift
    threat from foreign data - but equally no external route to enlarge a thin
    sample. If counts fail, the class set reduces; it is not topped up.
  - Class imbalance: accuracy would flatter the majority class, hence macro-F1 and
    the confusion matrix rather than headline accuracy. Provenance x class x zone
    may leave cells too thin to report - watch at the assessment, not after training.
  - Natural disturbance may be absent or near-absent from the incident source. If
    so, three-class results are not obtainable and the class set reduces.
  - **Terrain confound in Stage 1.** If natural-class events are predominantly
    steep-slope landslides while human events are not, Stage 1 can achieve high
    accuracy by learning slope rather than disturbance character. Report per-class
    slope and elevation distributions, run Stage 1 with and without terrain
    features, and report a terrain-matched subset separately.
  - **Season-class entanglement.** Landslides cluster in the monsoon, when clear
    observations are scarcest, so natural-class events will carry systematically
    wider loss intervals and are disproportionately likely to be rejected to
    `uncertain`. This entangles season with driver class and directly affects E6 -
    report the interval-width distribution by class, not pooled.
  - Seasonal correction is a double-edged requirement: over-correction removes the
    cultivation cycling signal, under-correction produces false detections. E6 must
    report both failure directions, not only the favourable one.
  - Low clear-observation counts (measured, not assumed) mean short feature windows
    may contain very few usable observations. Report the observation count
    distribution alongside E3.
  - Matching thresholds calibrated on historical events and then evaluated on events
    from the same pool would be circular - hold out an event set for E5.
  - **Cascade error in the two-stage classifier.** A human event misclassified as
    natural at Stage 1 never reaches Stage 2 and can never be corrected. Per-stage
    metrics therefore overstate end-to-end performance; the three-class cascade
    result must be reported alongside them, and the Stage 1 error breakdown given.
  - Stage 2 trains on the Stage 1 "human" subset, so its effective sample is smaller
    than the labelled total. Report per-stage counts, not just the overall count.
- **Adversarial pass:** run prompt A5b (hostile viva examiner) against this plan
  once thresholds are filled in, and again after the first results. Log any design
  change it forces in decisions.md.
  - Date run: [fill in] · What it found: [fill in] · What I changed: [fill in]
## Requirements traceability
 
| Requirement | Design feature | Evaluation link |
|---|---|---|
| R1 Detect qualifying new canopy loss across the network | Monitoring loop over rounds + held forest state + per-zone seasonal norm | E1, E4 |
| R2 Represent uncertain and evolving driver attribution | Two-stage attribution (early human/natural, later cultivation/encroachment) + provisional confidence + versioned reclassification | E2, E3 |
| R3 Remain valid across seasons | Background phenology normalised; event-level cycling preserved as a feature | E6 |
| R4 Apply beyond the calibration zone | Site-independent method with explicitly separated per-zone calibrated parameters | E7 |
| R5 One disturbance yields one record | Persistent event identity + calibrated spatial/temporal matching (machinery) | E5 |
 
## Results (fill in as they come)
- [date]: [what I ran, what happened, where the outputs are saved]
- 2026-09-29: Demonstration case (REF_031) run end-to-end - `claude/demonstrate_ref031.py`.
  See Section 4 above for what it showed / did not show. Full script output not
  re-pasted here; reproducible by running the script (reads `claude/features_REF_merged.csv`,
  `claude/ref031_geometry.geojson`).
 