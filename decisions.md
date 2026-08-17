# decisions.md - Design Decisions & Rationale

<!-- One entry per real decision. Newest at the top.
     The six entries below were transcribed from the research blueprint on
     2026-08-16; replace each date with the date the decision was actually
     taken if you can reconstruct it. From here on, log at the time. -->

## 2026-08-17 - Minimum detectable area is an evaluation output, not a design parameter
- Decision:           Do not state a minimum mapping unit in the objectives or fix one
                      before detection is built. Report detection performance stratified by
                      reference-event size, and derive the practical minimum reliable size
                      from where recall crosses a pre-stated threshold.
- Options considered: Fix an MMU up front from nominal sensor resolution; state a single
                      minimum-area figure in Objective 1.
- Why this one:       Supervisor guidance (2026-08-17). A minimum detectable area is not a
                      property of the sensor alone - it depends on the detection method,
                      image quality, geolocation error and event contrast. Stating it in
                      advance would assert as a design premise the thing the study should
                      measure. A size-stratified curve is also more informative than a
                      single threshold.
- What I gave up:     E1 needs enough reference events per size bin to support stratification,
                      which raises the reference-sample requirement. The dissertation cannot
                      quote one tidy MMU number early on; the answer arrives late.
- Revisit if:         Reference-event counts are too thin to populate size bins - then report
                      a coarser two- or three-bin split and say so, rather than reverting to
                      an assumed figure.

## 2026-08-17 - Hierarchical reference-labelling strategy
- Decision:           Label each historical forest-loss event by, in order: (1) an
                      authoritative event-level record from the responsible agency where one
                      exists and matches the satellite event under a written matching rule;
                      (2) manual interpretation of historical imagery under a documented
                      labelling protocol; (3) "uncertain" where neither supports a confident
                      class. Record the provenance of every label.
- Options considered: Manual interpretation only; authoritative records only; forcing every
                      event into one of the three classes.
- Why this one:       Authoritative records carry independent evidential weight where they
                      exist, but coverage cannot be assumed - administrative records tend to
                      capture what passed through the agency's own processes. Manual
                      interpretation fills the gap. An explicit "uncertain" outcome prevents
                      label noise being silently injected as confident classes.
- What I gave up:     Label quality is now heterogeneous and may correlate with driver class,
                      so E2 must be reported by provenance rather than pooled. Manual
                      interpretation is currently single-labeller (no confirmed second
                      labeller), so inter-rater agreement is unavailable; mitigation is a
                      protocol written before labelling, frozen dated labels, and a blind
                      re-label of a subset by me after a gap to give an intra-rater
                      consistency figure - which is weaker evidence and must be described as
                      such. Authoritative event-level records are excluded from classifier
                      inputs to avoid circularity, so their information is not exploited for
                      prediction.
- Revisit if:         A second labeller becomes available (supervisor, peer, or agency
                      contact) for even a subset - take it, and log the agreement figure;
                      or the responsible agency turns out to hold no event-level records,
                      in which case labelling is manual-only and the strategy simplifies.

## 2026-08-16 - Tamper-evident, not truth-guaranteeing
- Decision:           Protect the integrity and history of recorded claims; do not claim the ledger proves what happened in the forest.
- Options considered: Treat the blockchain/ledger as proof of truth; no integrity mechanism at all.
- Why this one:       It matches what cryptographic guarantees actually provide. A hash chain proves a record was not altered after the fact; it says nothing about whether the record was true when written (the oracle problem). Overclaiming here is the fastest way to lose credibility in a viva.
- What I gave up:     Requires explicit evidence requirements and a written threat-model boundary, and a weaker-sounding claim in the abstract.
- Revisit if:         A stronger, independently validated sensing mechanism is introduced that narrows the oracle gap.

## 2026-08-16 - Minimal field-evidence prototype
- Decision:           Require current GPS + newly captured media (+ timestamp, event ID) for designated inspection updates; keep the mobile app minimal.
- Options considered: Manual status entry only; a full production mobile app with auth, offline sync and user management.
- Why this one:       Adds real evidential support to a response claim without turning a remote-sensing and accountability project into a mobile-app engineering project.
- What I gave up:     Does not eliminate GPS spoofing or device-sharing risks; the app will look unfinished next to a production tool.
- Revisit if:         Privacy or device constraints make live capture infeasible in the evaluation setting.

## 2026-08-16 - Three initial driver classes
- Decision:           Cultivation, natural disturbance, permanent encroachment.
- Options considered: A more detailed driver taxonomy; a two-class human/natural split.
- Why this one:       Locally meaningful in the Sri Lankan protected-area context, but still bounded enough to label and evaluate within a feasibility pilot.
- What I gave up:     Class imbalance or poor separability may force a reduction to two classes later.
- Revisit if:         Reference data does not support three defensible classes (decide during the pilot, before training).

## 2026-08-16 - Maintained baseline / event registry
- Decision:           Check every new detection against a registry of historical and active known events before issuing a new alert.
- Options considered: Stateless alerting (every observation alerts); deduplicate only after alerts are sent.
- Why this one:       Prevents pre-existing disturbances from being republished as new alerts merely because the system was deployed later, and prevents repeat observations of one disturbance from spamming the operator.
- What I gave up:     Requires baseline construction from historical imagery and calibrated spatial/temporal matching thresholds - a real piece of extra work and a new source of error (fragmentation vs merge).
- Revisit if:         A different event-definition method performs better on the historical event set.

## 2026-08-16 - Progressive classification
- Decision:           Allow provisional/uncertain driver labels at alert time, revised as later evidence arrives; preserve every classification version.
- Options considered: Delay all alerts until the final driver is known; force an immediate final class.
- Why this one:       Resolves the latency-vs-certainty conflict honestly. Cultivation and permanent encroachment separate only on later persistence or recovery evidence, so an early alert with a stated confidence is more useful than either a late alert or a confident wrong one.
- What I gave up:     Some alerts initially carry uncertain driver information, which complicates the operator interface and the evaluation (accuracy now has a time dimension).
- Revisit if:         Pilot evidence shows the three classes are reliably separable at initial detection.

## 2026-08-16 - Persistent event model
- Decision:           Treat an alert as a persistent forest-loss event whose evidence, classification and response status evolve over time.
- Options considered: One-shot alert messages; an independent alert per satellite observation.
- Why this one:       Resolves duplicate alerts and the classification-vs-latency conflict at once, and creates a coherent lifecycle from detection through inspection to closure - which is what makes response accountability meaningful.
- What I gave up:     Requires event matching and versioned event history; the system now carries state, which is harder to build and harder to evaluate.
- Revisit if:         Historical-event testing shows stable event identity cannot be maintained.

---

## Deferred decisions (not yet made - do not treat as open-ended)

Each of these is waiting on specific evidence. Log it as a normal entry above the
moment it is taken.

| Deferred decision | Waiting on | Expected by |
|---|---|---|
| Final protected area / AOI + historical and operational periods | Feasibility pilot: usable S2 observations, S1 coverage, event count/size, reference imagery | End of pilot |
| Practical minimum reliable event size | E1 recall stratified by reference-event size - now an evaluation output, not a pre-set parameter (see 2026-08-17 entry) | After E1 |
| Record-to-event matching rule (spatial + temporal tolerance) for authoritative labels | Format and granularity of the records the responsible agency actually holds | Before reference labelling |
| Boundary between permitted contextual features and agency decision layers | Feature selection during 3c; agency decision layers about a specific event must not become classifier inputs | Before training |
| Exact classification algorithm | Final sample size, feature behaviour, class balance, interpretability, baseline performance | After feature extraction |
| Spatial/temporal event-matching thresholds | Calibration against historical events (duplicate vs fragmentation vs merge trade-off) | After event set is built |
| Final response-state workflow | Requirements analysis; must map to accountability requirements and stay simple | After requirement derivation |
| Ledger / public anchoring mechanism | Comparison of public testnet vs periodic Merkle-root anchoring vs signing, against durability, cost, privacy, prototype complexity | Before accountability build |
| Reference-sample size and sampling design | Pilot estimate of available events and class balance (treated as a methodology output) | Before any training or evaluation |
