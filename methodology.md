# methodology.md - How I'm Doing This (and the Evaluation Plan)

_Last updated: 2026-08-16_

## Approach in one paragraph
This project follows a Design Science Research approach: a real problem in forest
protection is identified, an integrated artefact is designed and built to address
it, the artefact is demonstrated on real cases from a selected Sri Lankan protected
area, and it is then evaluated against the solution objectives before the process
and findings are communicated. The artefact is one integrated system - satellite
detection, progressive driver classification, event-based alert management,
evidence-backed field response and tamper-evident verification are components of
it, not separate deliverables. Design choices and their trade-offs are recorded in
decisions.md as they are taken, and every model-supplied claim is verified against
a primary source before use (sources.md).

## How each step is being carried out

**1. Problem.** Established from the research gap, peer-reviewed literature on
satellite-based forest-change detection and alerting, existing operational alert
products, relevant Sri Lankan policy or institutional documents where available,
technical literature on tamper-evident logging and independent verification, and an
explicit threat model. Requirement gathering is deliberately bounded to artefact
design needs rather than framed as a broad investigation of every limitation in
current institutional systems.

**2. Objectives.** Four solution objectives derived from the problem and threat
model (see project.md). Each is written so that a specific test in the evaluation
plan below can decide whether it was met. Requirements R1–R6 trace to design
features and to those tests (traceability table at the end of this file).

**3. Design & build.** Approach chosen and recorded in decisions.md - persistent
event model, progressive classification, maintained event registry, three initial
driver classes, minimal field-evidence prototype, tamper-evident (not
truth-guaranteeing) accountability. Build sequence:

- *3a. Feasibility pilot before design freeze.* Compare a short list of candidate
  protected areas on usable Sentinel-2 observations, Sentinel-1 archive coverage,
  candidate disturbance-event count and size, and availability of historical
  reference imagery. Inspect a sample of candidate events to check the three
  proposed classes are visually interpretable and sufficiently represented. The
  pilot fixes: study area, study and monitoring periods, practical mapping-unit
  range, initial class definitions, and the intended role of Sentinel-1. Every
  resulting choice and trade-off goes into decisions.md.
- *3b. Detection and mapping.* Process multi-temporal Sentinel-2 observations in
  Google Earth Engine; use Sentinel-1 as complementary information where the pilot
  shows a defensible role. Account for seasonal and phenological variation and use
  an appropriate forest/reference baseline so normal seasonal change is not read as
  new canopy loss. Output spatial event candidates with geometry, observation
  timing and supporting change evidence.
- *3c. Classification framework.* Extract candidate temporal, spectral, geometric
  and contextual features. Train and test an interpretable feature-based classifier
  appropriate to the final sample size, compared against a simple baseline rather
  than committing to an algorithm before data inspection. Produce a driver label
  plus confidence; permit uncertain and provisional classifications and later
  revisions; preserve classification versions as event history rather than
  overwriting earlier beliefs.
- *3d. Alert/event engine.* Maintain an event registry holding event identities,
  geometries, timestamps and current state. Compare each new candidate detection
  against that registry using calibrated spatial and temporal matching logic.
  Measure duplicate, fragmentation and merge errors rather than demonstrating a
  single successful duplicate-prevention case.
- *3e. Field response and accountability.* A minimal mobile prototype captures the
  required field-response evidence: current GPS, current timestamp, newly captured
  media, event ID and response finding. Record hashes/signatures or equivalent
  integrity references for evidence and for event transitions. Use an
  append-only/verifiable log with an external trust anchor or public-verification
  mechanism, selected from the requirements and threat model after comparing
  practical alternatives.

**4. Demonstration.** _(To be designed - keep it separate from evaluation.)_
Proof of life on at least one real case: a genuine canopy-loss event in the
selected area carried end-to-end - detection, alert creation with provisional
driver, a later observation attaching to the same event, a classification revision,
a field-response update with GPS and captured media, and an integrity check
verifying against the external anchor. The demonstration case must not be chosen
because it is the easiest one; record what conditions it did and did not cover, and
state plainly that it shows the artefact works at all, not how well.
- Demonstration case selected: [fill in]
- What it showed: [fill in]
- What it did **not** show: [fill in]

**5. Evaluation.** See the plan below. Strategy notes recorded there.

**6. Communication.** Dissertation drafted from this file and decisions.md rather
than from scratch, with gaps marked rather than filled with plausible fiction. AI
use declared in the methodology or acknowledgements per programme policy.

## Evaluation plan

| # | Objective / area | Metric | Data / conditions | Baseline | Success threshold |
|---|---|---|---|---|---|
| E1 | Forest-loss detection (Obj 1) | Precision, recall, F1, omission/commission error, spatial agreement | Held-out reference interpretation over the study area and period; separate from any tuning data | Simple change-detection baseline (e.g. index-differencing with a fixed threshold); an existing alert product where suitable | [set before running - state it now, not after seeing results] |
| E2 | Driver classification (Obj 2) | Per-class precision/recall/F1, macro-F1, confusion matrix, confidence/error analysis | Held-out events across the three classes; class balance reported | Simple classifier baseline (e.g. majority class + a single-feature rule) | [set before running] |
| E3 | Progressive classification (Obj 2) | Revision accuracy: how often a provisional label is corrected, and in which direction | Events with both early and later observations, where data permits | Immediate-final-label variant of the same classifier | [set before running] |
| E4 | Alert latency (Obj 3) | Observation-to-alert latency; cloud/revisit gap reported **separately** so pipeline delay is not hidden inside satellite revisit delay | Retrospective operational simulation from first eligible observation | Alert timing of an existing product, if comparable | [set before running] |
| E5 | Event matching / duplicates (Obj 3) | Duplicate rate, fragmentation rate, merge-error rate; trade-off curve across thresholds | Full historical event set at alternative spatial/temporal thresholds | Stateless alerting (one alert per qualifying observation) | [set before running] |
| E6 | Alert update mechanism (Obj 3) | Same event ID retained; evidence and history appended; prior classification still verifiable | Replay of later observations and classification revisions over existing events | — (behavioural test) | All replays retain event identity and full prior history |
| E7 | Field-response evidence (Obj 3) | Expected reject / flag / accept behaviour; distance-to-event checks | Designated inspection updates attempted with missing evidence, distant evidence, and valid evidence | — (behavioural test) | Every case behaves as specified; no silent acceptance |
| E8 | Tamper evidence (Obj 4) | Integrity verification detects unauthorised historical alteration | Controlled modify / delete / reorder / backdate operations on records | — (behavioural test) | All four alteration types detected |
| E9 | Independent verification (Obj 4) | Untampered record verifies; modified record fails | Verification performed against the external anchor, **not** by trusting the application database | — (behavioural test) | Verification outcome correct in both directions |

- **Strategy:** predominantly naturalistic (real imagery, real disturbances, real
  study area) and ex post (the built artefact is evaluated) for E1–E5; artificial
  and controlled for E6–E9, where the point is to test specified behaviour under
  adversarial conditions that cannot be waited for in the field.
  _(These choices are organised in the FEDS framework - Venable, Pries-Heje &
  Baskerville. Verify the citation in sources.md before it goes in the chapter.)_

- **Known threats to validity (fill in as the adversarial pass finds more):**
  - Reference labels for driver class are interpreted, not ground-truthed; label
    error propagates directly into E2. Record who labelled, on what evidence, and
    ideally a second-labeller agreement check on a subset.
  - Class imbalance: accuracy would flatter the majority class, hence macro-F1 and
    the confusion matrix rather than headline accuracy.
  - Matching thresholds calibrated on historical events and then evaluated on
    events from the same pool would be circular - hold out an event set for E5.
  - Cloud and revisit gaps confound latency; they must be reported separately (E4)
    or the pipeline looks slower or faster than it is.
  - Single study area limits external validity; state this rather than generalising.
  - Tamper tests are performed by me against my own scheme - they demonstrate the
    mechanism detects the modelled attacks, not that the scheme is secure against
    an unmodelled adversary.
  - GPS and media evidence strengthen a response claim but do not prove officer
    identity, physical presence, or the truth of the finding.

- **Adversarial pass:** run prompt A5b (hostile viva examiner) against this plan
  once thresholds are filled in, and again after the first results. Log any design
  change it forces in decisions.md.
  - Date run: [fill in] · What it found: [fill in] · What I changed: [fill in]

## Requirements traceability

| Requirement | Design feature | Evaluation link |
|---|---|---|
| R1 Detect qualifying new canopy loss | Multi-temporal detection + forest/reference baseline | E1, E4 |
| R2 Represent uncertain/evolving driver attribution | Provisional confidence + versioned reclassification | E2, E3 |
| R3 Avoid duplicate alerts for the same ongoing disturbance | Maintained event registry/baseline + spatial/temporal matching | E5 |
| R4 Preserve one event lifecycle from detection to closure | Persistent event ID + append-only state/evidence transitions | E6 |
| R5 Strengthen physical-inspection claims | Current GPS + newly captured media + timestamp linked to event | E7 |
| R6 Detect unauthorised historical alteration | Cryptographic log + external/public verification anchor | E8, E9 |

## Results (fill in as they come)
- [date]: [what I ran, what happened, where the outputs are saved]
