# project.md - Driver-Aware Forest-Loss Alerting with Tamper-Evident Response Accountability

_Last updated: 2026-08-16_

> Paste this whole file at the start of every session (warm start, §5.2 of the guide).
> Keep it current. Anything in [square brackets] is still mine to fill in.

## Identity
- Student: Chamuditha Heshan
- Module: Research Project · Supervisor: Mr. Niranga Dharmarathne
- Full title: Driver-Aware Forest-Loss Alerting with Tamper-Evident Response
  Accountability: A Design Science Study in a Sri Lankan Protected Area

## Problem statement (current version)
Satellite monitoring can detect that forest cover has changed, but a detection on
its own gives neither the likely disturbance driver nor the response context a
ranger or protection officer needs to act. Three things follow. First, the final
distinction between drivers is often unavailable at first detection - cultivation
and permanent encroachment separate only once later persistence or recovery
evidence arrives - so a system that waits for certainty alerts late, and a system
that forces an immediate final label alerts wrongly. Second, repeated satellite
observations of the same ongoing disturbance produce redundant notifications
unless the system maintains event identity against a baseline of known events.
Third, a response status such as "inspected" carries little weight if it can be
entered without contemporaneous location-associated field evidence, and a
conventional editable database gives an external verifier no assurance that the
earlier alert and response history has not been silently changed.

**Gap:** how forest-loss detection can be coupled with progressive driver
attribution, persistent event-based alerting, evidence-backed response updates,
and independently verifiable tamper-evidence, as one integrated artefact.

## Research aim
To design and evaluate an integrated artefact that detects new forest canopy-loss
events, progressively characterises their likely disturbance driver, manages each
disturbance as a persistent non-duplicating alert event, and preserves
evidence-backed response actions in a tamper-evident and independently verifiable
history.

## Solution objectives (v1)
1. **[must-have, testable]** Develop a multi-temporal satellite-based approach for
   detecting and mapping new forest canopy-loss events in the selected protected
   area using Sentinel-2 imagery supported by Sentinel-1 data.
   _Tested by:_ precision / recall / F1 and spatial agreement against reference
   interpretation and a simple change-detection baseline.
2. **[must-have, testable]** Create a framework classifying detected loss events
   into cultivation, natural disturbance and permanent encroachment from temporal,
   spectral, geometric and contextual evidence, carrying a confidence value and
   able to revise the label as new evidence arrives.
   _Tested by:_ per-class and macro-F1 on held-out events vs a simple baseline
   classifier; confusion matrix; revision accuracy.
3. **[must-have, testable]** Create an event-based alerting and
   response-accountability framework that maintains persistent event identity,
   checks new detections against a baseline of existing events to prevent
   duplicate alerts, supports evidence-backed field response updates, and
   preserves the alert-response lifecycle.
   _Tested by:_ duplicate / fragmentation / merge-error rates across thresholds;
   observation-to-alert latency; replay tests preserving event ID and history;
   missing / distant / valid evidence scenarios.
4. **[must-have, testable]** Evaluate the integrated artefact across detection and
   classification performance, alert latency and event management, evidence-backed
   response verification, and tamper-evident record integrity.
   _Tested by:_ the full evaluation plan in methodology.md, including independent
   verification against the external anchor rather than the application database.

_Nice-to-have (only if the pilot leaves room):_ comparison of alert timing against
an existing public alert product; analysis of provisional-vs-final classification
accuracy over time.

## The artefact
- **What it is:** one integrated computing artefact - a monitoring and
  accountability pipeline, not four separate systems.
- **Components:** (a) multi-temporal Sentinel-2/Sentinel-1 detection in Google
  Earth Engine; (b) progressive, confidence-aware driver classifier;
  (c) event registry + matching engine that maintains persistent event identity;
  (d) minimal mobile field-response prototype capturing current GPS, timestamp and
  newly captured media; (e) append-only verifiable log with an external trust
  anchor.
- **Core design principle:** an alert is a persistent *event*, not a one-time
  notification. Detections, classification revisions, response evidence and status
  changes attach to the same event; earlier states are retained, never overwritten.
- **Hard constraints:** one final-year individual project; free/open satellite data
  only; classification limited to what a modest labelled sample supports;
  large media stays off-chain; prototype-level mobile app; no production
  authentication, offline sync or institutional user management.

## Scope
**In:**
- One Sri Lankan protected area, selected via a short data-feasibility assessment.
- Three initial driver classes: cultivation, natural disturbance, permanent
  encroachment - probabilistic attribution, not legal determination.
- Historical data for baseline construction, reference labelling, retrospective
  evaluation; operational simulation of new events after a defined monitoring
  start point.
- Minimal field app: event selection, current GPS, newly captured media, response
  entry / signing / submission.
- Integrity/provenance anchoring; off-chain payloads.

**Out:**
- Production authentication, offline synchronisation, institutional user management.
- Proof that a field report is factually true (oracle limitation - stated explicitly).
- Compromised operating systems, sophisticated GPS spoofing, device sharing /
  identity fraud, production-scale key custody.
- Nationwide or multi-site deployment; real-time on-satellite processing.

## Threat model (bounded)
| Actor / failure | Risk | Design response |
|---|---|---|
| Field responder | Claims inspection without contemporaneous evidence | Designated inspection states require current GPS + timestamp + newly captured media; evidence reference retained |
| App / DB administrator | Alters, deletes, reorders or backdates history | Append-only cryptographic history + external anchoring, so silent rewriting is detectable |
| Detection / duplicate logic | Repeat observations create duplicates, or distinct disturbances merge | Maintained event baseline + calibrated spatial/temporal matching, with measured fragmentation and merge rates |
| Classification uncertainty | Early evidence cannot separate cultivation from permanent encroachment | Provisional confidence-aware label + versioned reclassification |

## Where I am right now
- Current step: **1–2 (problem and objectives are sharp; design decisions taken in
  principle, feasibility pilot not yet run).**
- Next action: run the feasibility pilot (§9.2 of the blueprint) - shortlist
  candidate protected areas and compare usable Sentinel-2 observations, Sentinel-1
  archive coverage, candidate event count/size, and historical reference imagery.
  This unblocks four deferred decisions at once.

## Open questions (deliberately deferred, not vague)
- **Study setting:** final protected area / AOI, and historical + operational
  periods. Deferred because usable S1/S2 observations, event frequency, class
  representation and reference imagery all vary by place and time. Fixed by the
  feasibility pilot.
- **Operating parameters:** practical minimum mapping unit and the exact
  classification algorithm. Deferred because the reliable minimum event size
  depends on real image quality and reference-event sizes; the classifier follows
  from sample size, feature behaviour, class balance and interpretability.
- **Event lifecycle parameters:** spatial/temporal matching thresholds and the
  final response-state workflow. Thresholds must be calibrated against historical
  events to trade duplicates and fragmentation against incorrect merges.
- **Accountability implementation:** the requirement is fixed (tamper evidence +
  independent verification); the mechanism - public testnet vs periodic Merkle-root
  anchoring/timestamping vs signing-only - is chosen after comparing durability,
  cost, privacy and prototype complexity.
- Reference-sample size and sampling design are methodology outputs: the pilot
  estimates available events and class balance, then the sampling plan is
  documented before any training or evaluation.
