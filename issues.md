# issues.md - Open Issue Registry
 
<!-- Rewritten 2026-08-20 after two scope changes: accountability component removed,
     scope raised to the national protected-area network, two-stage classification
     adopted. The pre-2026-08-20 register (I1-I12) tracked an artefact that no
     longer exists; superseded items are listed at the bottom rather than deleted.
     STATUS: BLOCKER (work stops) / DECISION (needs a decisions.md entry) /
     MEASURE (needs a number, not an argument) / ADMIN / CLOSED. -->
 
_Last updated: 2026-09-29_
_~~Next supervisor meeting: 2026-08-21~~ **held.** Feasibility report delivered._
 
> **DATE CORRECTION, 2026-09-28.** Every "2026-10-20 panel / 2026-10-31 submission"
> reference below and throughout this file (and project.md) is **stale**. Confirmed
> by the student this session: **submission is 2026-10-20, viva is 2026-10-30** -
> the reverse order this file assumed, and 11 days tighter to the harder deadline
> than previously planned around. Historical entries below that cite the old dates
> describe reasoning that was correct *at the time* and are left as-is per this
> project's own reversal-tracking rule; only the live "Current deadlines" block just
> below is corrected. **Do not plan against any other date mentioned further down
> in this file without checking it against this banner first.**
 
**Current deadlines:**
- **2026-10-20 - submission.** Both the artefact + results and the written
  dissertation are due here, not staggered as previously assumed.
- **2026-10-30 - viva.** 10 days after submission, not 11 days before it.
- **2026-09-22 - internal design freeze.** No new design decisions after this date.
  Anything found later is a Chapter 5 limitation, not a redesign. **Already passed
  with three logged exceptions** (issues.md B18/decisions.md 2026-09-27; D6 Stage 1,
  decisions.md 2026-09-28; D6 Stage 2, decisions.md 2026-09-29) - all judged
  necessary, all stated as exceptions, not silently made.
> **The register is now schedule-bound.** ~~Six weeks~~ **Three weeks to submission,
> not the panel-then-writing-tail structure previously assumed.** Items below are no
> longer ranked by how interesting they are but by whether they block the critical
> path. Anything that does not block it and does not cost a paragraph in Chapter 5
> is being carried, not worked.
 
## Measured 2026-09-08 - first real numbers on this project
 
| ID | Measurement | Value | How |
|---|---|---|---|
| M4 | Minutes per labelled event | **~6 min** (30 min / 5 events) | Timed pilot, Google Earth Pro only. **Floor, not average** - four of the five were obvious false positives and resolved fast. Real events need the index graph and the decision tree; plan 10-15 min. **Confirmed 2026-09-19:** CAL_001 took 6 min and also stopped early at Step 0b. Still a floor. |
| M3 | High-resolution imagery availability | **Available, but usually brackets the window rather than falling inside it** | Of 5 events, most had images either side of the loss window, few within it. Google Earth imagery is irregular - commercial acquisition, cloud, low priority for unpopulated parks. Step 1 structural evidence is therefore often unavailable, exactly as the protocol anticipated. **CAL_001 and CAL_002 both `highres_in_window = no`.** |
| B5/M5 | GEE processing cost | **~5 min** for Wilpattu, 6 years, 3 exports | Console prints time out on this workload; exports do not. **Network-scale extrapolation done 2026-09-27** - see B5 row below for the full measurement and its caveat. |
| M13 | Candidate count, Wilpattu NP | Screen v1 **1,035**; screen v2 **201**; **Hansen 18 real events** | Both screen pools rejected. The Hansen figure is the meaningful one: 18 loss events in 6 years across 131,700 ha. 9 at MIN_PIXELS 5, 18 at MIN_PIXELS 1 - the size filter was never the constraint. **M13 was demoted 2026-09-08 and this is exactly the question it would have answered.** |
| M17 | National PA loss-pixel census | **151 PAs.** Wilpattu 249 px (19/100km2, national floor). Kahalla-Pallekele 6,652 px (3,067/100km2). Paddawiya 12,283/100km2 and Ralapanawa 17,334/100km2, both under 35 km2. | Hansen v1.13, 2019-2024, MIN_PIXELS 1, WDPA Designated, REP_AREA>20 km2. Query 2026-09-09. Part B (real event counts, 6-site shortlist) pending. |
 
**Screen rejected the same day** - see decisions.md 2026-09-08. These four measurements
survive the rejection; the candidate pool does not.
 
> **Standing consequence.** B3 and B4 are outputs of the 30-event calibration batch.
> Until it is run and timed, the three-classes-or-two question has no answer and no
> reference-sample size can be committed to. Say "method stated, number pending" -
> do not imply a prevalence figure exists.
 
---
 
## A. Blockers - nothing downstream moves until these clear
 
| ID | Issue | Why it blocks | Next action |
|---|---|---|---|
| B1 | ~~Loss-date method undecided~~ | **CLOSED 2026-08-20** | Interval method adopted (decisions.md). Protocol structure is unblocked; only `[T7]`, the maximum tolerable interval width, remains a calibration-batch output. Method and threshold were previously conflated - that is why this looked like it was blocked on a measurement. |
| B2 | **Boundary dataset - FOUND, 679 polygons (2026-08-20)** | Network-scale scope survives: usable polygons exist. Remaining sub-questions are scoping, not existence. | **Closed as an existence question.** WDPA `WCMC/WDPA/current/polygons`, ISO3=LKA, 679 polygons, sum REP_AREA 22,362 km2 (inflated by overlaps). Logged in sources.md. Follow-ups moved to M6-M8 and D11. |
| B3 | **Per-class event prevalence unknown** | Decides three classes or two, decides whether held-out evaluation is possible at all, decides Stage 2 sample size. | **Corrected 2026-08-20: the incident source carries no driver labels, so counting "by class" in it is impossible.** Estimate prevalence instead: label a **random** sample of ~30 events by hand (not the clearest ones) and count classes in that sample. This doubles as the calibration batch, which is discarded from the reference set afterwards. **Narrowed again 2026-09-19:** the curated REF set cannot give prevalence (M20), and the random CAL batch is 20 events over four dry-zone protected areas, of which perhaps half will pass Step 0. Whatever comes out is prevalence among Hansen-detected loss in those four areas at n<10 - a signal, not an estimate. Word it that way everywhere. |
| B4 | **Natural disturbance may be absent or too rare** | If the source is incident/enforcement reporting it may contain near-zero natural events. Stage 1 would be degenerate and Objective 2 must be amended. | Answered by the same 30-event sample. **Early signal: the GFW Sri Lanka dashboard showed permanent agriculture at 1.6 kha against wildfire + other natural disturbance at roughly 8 ha.** Those are areas, not counts, from an unrecorded query - a signal, not a finding. But go into the meeting with the two-class fallback already thought through. |
| B5 | **GEE feasibility at network extent - PARTIALLY ANSWERED 2026-09-27** | Decides whether nationwide application is real or aspirational. | **Measured `candidate_screen.js` on two sites:** Wilpattu, 131,700 ha, ~5 min; Kahalla-Pallekele, 24,983 ha (measured via `aoi.area()`), ~1-2 min (eyeballed from GEE Tasks tab, not stopwatched - less precise than the Wilpattu figure). Rates: Wilpattu ~26,340 ha/min; Kahalla-Pallekele ~12,500-25,000 ha/min depending on which end of "1-2 min" is real. **The two rates roughly agree - cost tracks AREA, not candidate count**, which is notable because Kahalla-Pallekele produced 13x more raw candidates (2,688 vs Wilpattu's screen-era counts) yet ran faster, being 5x smaller in area. **Extrapolated to network extent** (679 polygons, ~2,236,200-2,307,500 ha per the WDPA sum, M7 still unsettled on which area figure is right): **roughly 1.5 to 3 hours for one full pass**, assuming the network is processed as one continuous AOI the way both test runs were. **Caveat that matters more than the number itself:** this assumes a single big combined-geometry run. The actual detection loop's architecture is not decided (D9 - one AOI vs. per-polygon loop, and monitoring cadence). 679 separate per-polygon calls, most of them small, would each carry fixed GEE call overhead independent of area - a real cost driver this measurement does not capture and that could dominate over the area-based estimate above. **So: "one national historical screening pass is cheap" is answered. "What the actual repeated monitoring loop costs" is not, and depends on D9, which is still open.** **Architecture decided 2026-09-27 (decisions.md): batched groups of polygons, not one merged shape (likely hits GEE's memory limit, per B22 precedent) and not 679 separate calls (pays per-call overhead 679 times). The 1.5-3 hour figure above no longer describes the real architecture - batch size itself is now an open follow-up measurement, not yet run.** **Note 2026-09-28: this whole row may be moot for the panel/submission deliverable - see the detection-loop scope-cut note under "Critical path" below.** |
 
## B. Raised 2026-08-20 by the Global Forest Watch discovery
 
The GFW / Land & Carbon Lab / Google DeepMind drivers dataset (Sims et al. 2025,
*Environmental Research Letters*) assigns a **dominant driver to each ~1 km cell over
a multi-year mapping period**. It is **not** annual, event-by-event driver attribution
- that phrasing was wrong in this register until 2026-08-20 and is corrected here.
This is real driver-labelled data covering Sri Lanka.
| ID | Issue | Status | Next action |
|---|---|---|---|
| G1a | **Gap structure agreed** | **CLOSED 2026-08-20** | Three mismatches against the GFW drivers product, settled after checking Sims et al. 2025: **(1) spatial** - GFW gives a dominant driver for a ~1 km cell; this project attributes a driver to an individual detected loss-event polygon. **(2) temporal** - GFW does not progressively revise an individual event's driver as later observations arrive; this project does. **(3) output/epistemic** - GFW gives a dominant class at cell level; this project carries event-level confidence and retains attribution revisions over time. Note the correction: the product is **not** annual event-level attribution, so the temporal mismatch is about *absence of a revision mechanism for a single event*, not about timestep granularity. Do not let it drift back to a granularity argument - granularity can be answered with "so run it more often". |
| G1b | **Final gap text written into project.md** | **CLOSED 2026-08-21** | Paragraph written into the project.md Problem statement; flag box deleted. Verified as *in the file*, not merely agreed - the premature 2026-08-20 close is not repeated. Rests on the two confirmed Sims claims only. The drafted concession that the product reports cell-level class probabilities was **cut**, being a third and unverified claim; restore text is in a comment beside the paragraph, and it goes back only after sources.md records it. |
| G2 | **Is selective logging observable at Sentinel-2 resolution - and if detected, where does it go?** | **CLOSED 2026-09-24** (was REFRAMED 2026-08-20) | Observability question stands as before: low-intensity selective removal may never produce a resolvable canopy-loss signal, so it never becomes an event and never reaches the classifier - practical detectability by size/intensity remains an evaluation output (decisions.md 2026-08-17). **Class question resolved 2026-09-24 (decisions.md, own scoping decision):** logging/harvest events that ARE detected stay pooled into `uncertain`, flagged `logging_or_harvest` in notes, excluded from the taxonomy with a stated reason rather than given a fourth class. Measured on the calibration batch: 2/20 (10%), CAL_013 and CAL_015 (answers M15). **REF-side count now in (2026-09-27, REF set complete): 3/30 (10%) - REF_039, REF_026, REF_018.** Same rate as CAL, independently. Confirms the 2026-09-24 decision rather than reopening it - decided to report this 10% as a named sub-share of `uncertain` (not genuinely ambiguous, just outside the three-class scope) wherever the uncertain rate is written up, rather than treating it as unexplained noise. Reason: logging is a **Stage 1 confound** (coupe felling reads human via straight edges, scattered selective removal reads natural via irregular edges - same driver, opposite Stage 1 signal), so a fourth class would need a cascade redesign this close to the 2026-09-22 freeze, for a thin (n=2) sample. **Not raised with the supervisor first** - logged as the labeller's own scoping decision, per the 2026-08-20 accountability-removal precedent; to be mentioned to him after the fact, same as A10/A11. Counterpoint on record (2026-09-05): logging is one of GFW's seven driver classes, so the honest framing is that logging has nowhere to sit in **my** narrower class set, not that no class set anywhere accommodates it. Ties to A9/D11 unchanged: plantation harvest is legal and likely concentrated in Forest Reserve/Other State Forest, so a confident detection there is a false positive on a lawful activity, not an attribution error. **Live instance surfaced 2026-09-29:** wiring Stage 1's hand-set rule (decisions.md 2026-09-28) against the full 29-row REF feature set - not just the 19 known-human events the 2026-09-28 false-positive check covered - shows REF_018 (one of the three logging-pooled `uncertain` events named above) passes all three Stage 1 legs (compactness=0.115 < 0.36; slope=4.92 > 4.43; dist_to_prior_loss=429.4m > 212m) and is called `candidate_natural`. It is the only event among all 29 REF rows to trigger `candidate_natural`. This was never checked before now, because the 2026-09-28 verification pass only tested the 19 cultivation/permanent_encroachment events, not the uncertain-pooled logging ones. Plausible confirming evidence for the confound just described (scattered selective logging reading as natural at Stage 1) - not proof, n=1, and not acted on: REF_018 keeps its `uncertain_logging` label, Stage 1's rule is unchanged. Flagged as a finding, not a decision - worth a Chapter 5 line either way. |
| G3 | **Sims et al. 2025 - citation complete, content partly verified** | **PARTIAL, updated 2026-09-05** | Confirmed directly from the paper: (1) spatial unit ~1 km cell; (2) temporal - dominant driver per cell over a multi-year mapping period, **not** annual event-level attribution. **Full citation now recorded in sources.md (2026-09-05).** Class list obtained from the Zenodo dataset description, not the paper - seven classes, logging among them - and marked unconfirmed there until read in the article. **Still unchecked:** how logging is defined; what "dominant" means procedurally (area share, threshold, tie-breaking); training/reference data and how many samples fall in Sri Lanka (G5); validation method and reported accuracy. **Blocks G2 and G4, not G1b** - the three mismatches rest only on the two confirmed claims. Record all of it in sources.md (A6); a verification that is not written down is not a verification. |
| G4 | **Baseline for E1/E2 undecided** | DECISION | Should the 1 km product replace or join "simple change-detection baseline"? A published comparator is stronger, but the resolution mismatch must be handled explicitly. |
| G5 | **Training-sample coverage for Sri Lanka unknown** | MEASURE | Their training and validation samples are public (Zenodo / WRI Data Explorer). Count how many fall in Sri Lanka. A low number is quotable justification for local calibration. |
| G6 | **Risk: 1 km labels used as event labels** | CLOSED | Decided 2026-08-20: comparator and sampling aid only, never reference labels. Weak-label pre-training retained as a documented fallback if counts are thin. |
 
## C. Decisions needed (each becomes a decisions.md entry)
 
| ID | Decision | Waiting on | Note |
|---|---|---|---|
| D2 | Sentinel-1 - optional or necessary | In-polygon observation counts by month | Low optical counts may make radar necessary, not complementary. Especially for early study years. **Clearest justification is now narrowing wide loss intervals (B1)** - a concrete role, not "supporting data". **Weakened slightly 2026-09-19:** measured in-polygon clear counts are 18-34/yr, better than the scene-level figures suggested. |
| D3 | Seasonal correction method | Whether background phenology and event-level cycling separate at S2 resolution | Must remove background, preserve event-level cycling. Both directions evaluated in E6. |
| D4 | Stratified sampling rule for E1 | Zone strata + per-area event yield | **Write before evaluation, not after results.** |
| D5 | Class count: three or two | B3, B4 | Fallback already anticipated. If forced to two, drop natural disturbance and keep cultivation vs permanent encroachment - that preserves the progressive claim. |
| D6 | ~~Classification algorithm (per stage)~~ | **CLOSED 2026-09-29** | Interpretable, compared against a simple baseline. **Stage 1 CLOSED 2026-09-28 (later still, again)** - hand-set thresholds, 3-of-3 unanimous vote, calibrated against the 19 known-human events. **Stage 2 CLOSED 2026-09-29** - logistic regression on the three fixed features, LOOCV over the 19-event population, adopted over a higher-scoring (89.5%) decision stump/tree on small-sample overfitting grounds (stump's rule rests on only 6 permanent_encroachment examples). See decisions.md, 2026-09-29. **D6 is now fully closed.** |
| D7 | Event-matching thresholds - **DECIDED 2026-09-27** | Calibration against a held-out historical event set | Match by location (buffered overlap), no time cutoff, chained/transitive union of same-round fragments, merges logged not silently combined. See decisions.md 2026-09-27 for full reasoning and the measured 10m buffer. |
| D8 | Reference-sample size and design | Pilot estimate of available events and class balance | Target ~50 usable events per class per stage; check against labelling speed. |
| D9 | Monitoring round trigger - **DECIDED for classification 2026-09-28** | M1/M2 observation cadence | Every usable observation, or fixed interval? Feeds E4 directly. **Updated 2026-09-19:** measured in-polygon cadence is 18-34 clear observations/yr at most CAL sites but ~72/yr at CAL_005, which sits in an orbit-overlap zone (M23). The trigger cannot assume a single national cadence. **Split 2026-09-28 (decisions.md):** detection keeps the per-usable-observation trigger (2026-08-20, unchanged). Classification (Stage 1 + Stage 2) re-runs on a fixed **quarterly** grid instead - chosen over per-observation (incomparable per-event timelines) and monthly (finer than the R(t) test showed the trajectory signal actually resolves) - flagged as possibly too coarse for Stage 1 specifically, revisit if so. |
| D12 | Size of the GFW-independent event subset | Candidate set build | Events found *via* GFW cannot provide a clean comparison *against* GFW. A GFW-independent subset must be reserved for the E1/E2 baseline comparison, and its size stated. **If natural-class events are sourced entirely via GFW, that class has no non-circular baseline comparison - state it rather than reporting a pooled figure that hides it.** |
| D13 | Terrain confound in Stage 1 | Natural-class event set | If natural events are mostly steep-slope landslides and human events mostly are not, Stage 1 can score well by learning slope rather than disturbance. Mitigation: report slope/elevation distributions per class, run Stage 1 with and without terrain features, and reserve a terrain-matched subset. Decide which mitigations are in scope. |
| D11 | WDPA inclusion rule | M7-M9 + verification of Sri Lankan designation types | **Proposed:** monitor the dissolved union of the forest/wildlife designations (National Park, Nature Reserve, Strict Nature Reserve, Sanctuary, Forest Reserve, Conservation Forest, Reserved Forest, Other State Forest, National Heritage Wilderness Area, Jungle Corridor), filtered `STATUS = Designated` and `GIS_M_AREA = 0`. Treat UNESCO-MAB / World Heritage / Ramsar as **attributes**, not separate geometry, so one clearing yields one event. Exclude Marine National Park. EPA status to be checked. Write it up before detection runs. |
| D10 | Forest-reference update rule | Detection build | When is forest state allowed to change, and on what evidence? This is where **baseline creep** enters. Seasonal norm updates each round; forest state must not. |
| D14 | **What counts as "recovered"** | **NOTHING - this is blocking NOW** | Opened 2026-09-19. `sustained_drop_duration_days` cannot be computed without a recovery level. On CAL_001 the first drop lasts **160 days or 295 days** depending only on where that level is set. The rule ("duration = days from `t_loss` until the first clear observation reaching X% of the pre-event median") must be written down **before the batch continues**, or the twenty durations are not comparable and the threshold derived from them is meaningless. **Status not re-checked since 2026-09-19 - needs confirming whether this was actually resolved somewhere during the CAL batch, or whether it's still genuinely open.** |
 
## D. Measurements outstanding
 
| ID | Measurement | Why | Note |
|---|---|---|---|
| M1 | Clear observations **inside the event polygon**, **by month** - **CLOSED 2026-09-27** (REF-side answered; CAL-side gap stated, not redone) | Sets feature window length, `[T7]` max interval width, and D2 | Current figures (39 at <60% scene cloud, 13 at <20%, per year, one area) are **scene-level** and are not the number the design needs. Cloud over the tile ≠ cloud over the polygon. **PARTLY ANSWERED 2026-09-19** by the CAL batch exports - by year, not yet by month. See M23. **BY-MONTH FIGURE ADDED 2026-09-27**, computed directly from `REF_all_timeseries.csv` (valid_pct>=60, all 30 REF events, all years pooled): clear-obs count by calendar month - Jan 457, Feb 506, Mar 876, Apr 762, May 516, Jun 573, Jul 603, Aug 483, Sep 494, Oct 455, Nov 392, Dec 366 (6,483 total). Shape: clearly higher in Mar-Apr, lowest in Nov-Dec - consistent with the NE monsoon window. Per-event annual average: 22.5-34.2/yr, no orbit-overlap outlier like CAL_005's ~72/yr. Per-site annual average: Nuwaragala 28.2, Maduroad 25.9, Kahalla-Pallekele 24.8, Victoria Randenigala Rantambe 31.2 (n=4-10 events per site). **Caveat: pooled across all 4 sites, not yet split by climatic zone** - per SKILL.md's own guardrail, seasonal parameters need to be per-zone, not national, and site != verified climatic zone (B8 still open). **CAL-side by-month: attempted and abandoned 2026-09-27.** `CAL_all_timeseries.csv` (the merged raw export) turned out to be the **pre-fix** batch export, not a cleaned equivalent of REF's - it reproduces B14's exact bad-row counts (CAL_007 270/290, CAL_008 254/305, thirteen other events 1-8 dates each; 561/5,436 rows dataset-wide, 10.3%, all `valid_pct > 100%`). Unlike REF, CAL's batch export was never re-run through the B23 fix (v3, separate `count()` call) and re-merged clean - the 2026-09-25 "CAL side: RESOLVED" note only confirmed the frozen `[T6]`/`[T7]` thresholds were safe, because those came from the separate clean `event_timeseries_v6.js` tool, not this batch file. **Decision: not redoing the GEE export under deadline pressure. CAL-side by-month is left unanswered** - the REF-side figure above already answers M1's design question (feature window length, `[T7]`, D2). Only the CAL by-year number (M23) stands as CAL's contribution to M1. If a clean CAL-side by-month figure is wanted later, it needs the same fix REF got: re-export via a corrected mosaic-first + separate-`count()` script, then recompute. |
| M2 | Same counts **by year** | Sentinel-2 was single-satellite in the early archive, so early years may have roughly half the observations | **Period decided: 2019-2024 (decisions.md 2026-09-08).** **ANSWERED per event 2026-09-19** for the CAL batch; see M23. |
| M3 | High-resolution imagery availability per event and date | Decides how much Tier A (structural) evidence is available vs Tier C (trajectory-only) | Check Google Earth Pro's historical slider on a handful of events. If Tier A is thin, E2 leans on trajectory labels and the classification claim weakens - state it. |
| M4 | Labelling speed (minutes per event) | Sets the realistic ceiling on reference-sample size | Time yourself on the calibration batch. Record it per event, not as an impression afterwards. |
| M11 | **Count of GFW 1 km cells with a natural-disturbance dominant driver that intersect the WDPA polygons** | B4, D5 - decides three classes or two before any labelling | This is the searchable pool for the natural class, and it is a *count*, not an area. Record the query: area filter, years, loss threshold, query date. **Caveat that must travel with the number: GFW is a model, and models under-predict rare classes. A low count is not proof that natural disturbance is rare in reality - it is proof that GFW rarely assigned it. B4 still needs the random sample.** |
| M10 | The 30-event calibration sample itself | B3, B4, M3, M4, A3 | One exercise answers five register items. Record per event: id, class call, deciding evidence tier, confidence, whether high-res imagery existed, minutes taken. Random selection - a convenience sample invalidates the prevalence estimate. **2026-09-19: now the 20-event CAL batch, not 30.** |
| M5 | GEE processing cost for one area | B5 | **ANSWERED 2026-09-27.** Two sites measured, extrapolated - see B5 row above for the full figures and the D9-architecture caveat. |
| M15 | **Share of detected events that are logging or plantation harvest** | G2, D5, A9 | **ANSWERED 2026-09-24: 2/20 (10%) of the calibration batch (CAL_013, CAL_015).** Decision taken on this figure: excluded from the taxonomy with a stated reason (G2, decisions.md 2026-09-24) rather than given its own class - see the G2 row. Still also a Stage 1 confound, independent of the taxonomy decision: coupe felling has straight edges and reads human, scattered selective removal has irregular edges and may read natural - same driver, opposite Stage 1 calls; this remains open for detection design. |
| M12 | **M1 measured separately for the dry-zone and wet-zone sites** | Sequencing decision (2026-08-20); D2; E7 | Wet-zone cloud will not resemble dry-zone cloud. **Narrowed 2026-09-08:** the `[T2b]`-plus-blackout-gap question no longer applies at Sinharaja, which carries no classification. What still matters there is whether the **detection** loop has enough usable observations per round, and whether S1 becomes necessary in the wet zone while remaining optional in the dry zone - that asymmetry is itself an E7 result and one of the few zonal findings still obtainable. |
| M13 | ~~**Candidate event count inside each of the two boundaries**~~ | **DEMOTED 2026-09-08 - no longer a decision input** | Sinharaja was fixed as **detection-only** (decisions.md 2026-09-08) on schedule grounds, *before* this was measured. M13 no longer decides anything; it is now reporting material only. **Lesson already logged in decisions.md 2026-09-09: a check demoted because one of its consumers disappeared may still be load-bearing for another.** |
| M14 | **Sinharaja's WDPA record count and designation overlap** | D11 | Sinharaja carries multiple designations. The D11 rule (overlaps are attributes, not separate geometry) has to be verified on this case specifically, or one clearing yields several events. |
| M7 | `sum(GIS_AREA)` vs dissolved area, and the `GIS_AREA` size distribution | B5, D4 | Dissolved (23,075) exceeded the `REP_AREA` sum (22,362), so the two are not comparable - `REP_AREA` is reported, `GIS_AREA` is geometric. Redo with `GIS_AREA`. The size distribution decides real GEE load: 679 areas is not 679 equal areas. |
| M8 | Which designations carry the 103 `STATUS_YR = 0` records | Study period, framing | Only 6 areas designated after 2018, so the period is barely constrained. But if the missing years cluster in one designation type (e.g. Forest Reserves), that is a systematic gap needing a sentence. |
| M9 | Marine extent: count and area where `GIS_M_AREA > 0` | D11 | No `MARINE` field exists. Marine areas must be excluded or clipped before forest detection runs over water. |
 
## E. Admin and risk
 
| ID | Item | Note |
|---|---|---|
| A3 | Every `[T#]` in labelling_protocol.md is blank | All are calibration-batch outputs. Protocol cannot freeze until B1 clears and the batch runs. |
| A4 | Every success threshold in E1-E7 is blank | Must be stated **before** running, not after seeing results. |
| A5 | No demonstration case selected | Step 4 in methodology.md. Keep separate from evaluation. **Note 2026-09-19:** dropping demonstration was considered and rejected - it is a required Design Science step and it is cheap once the artefact exists. Cut expensive things, not cheap ones. |
| A9 | Designation semantics **PARTIALLY ANSWERED 2026-09-27** | Reserved Forest and Conservation Forest are real Gazette-declared categories with statutory clearing offences (Forest Conservation Ordinance S.3, S.6, S.7). **"Other State Forest" is not a legal category the Ordinance defines at all** - unreserved state land, no statutory clearing prohibition, administration set by executive circular rather than statute (exact circular history unconfirmed - two secondary sources disagree, see sources.md). **Live tension with D11:** D11 pools OSF into the same monitored boundary union as Reserved Forest/National Park/Sanctuary under one "protected area" label, but a clearing event's legal status differs by designation even inside that one union. **Framing decision still open** (raised in chat 2026-09-27, three options sketched, not decided): (1) define "protected area" in the write-up as "within the monitored WDPA boundary set," not "under statutory protection"; (2) drop OSF from the monitored network and note the coverage loss as a limitation; (3) keep OSF but carry designation type as a per-event attribute so results can be split by legal status. **Also unconfirmed:** whether OSF actually appears as a `DESIG_ENG` value in the 679-polygon WDPA extract D11 assumes it's in. **Live in the data 2026-09-19:** the CAL batch pools 12 Sanctuary and 8 Reserved Forest events in one calibration sample. |
| A8 | WDPA boundary accuracy vs national gazette | WDPA is compiled from government submissions and may lag official designations. Cross-check a sample against Department of Wildlife Conservation / Forest Department sources before any enforcement-adjacent claim. |
| A6 | sources.md: partly cleared 2026-09-05 | Sentinel-2 revisit and per-band resolution now **verified** against the ESA handbook (Issue 1 Rev 2, 2015). Sims et al. 2025 citation now complete; four content claims still unconfirmed. Remaining unverified: Peffers, FEDS, forest-cover figures, designation semantics, climatic-zone assignment. |
| A7 | Adversarial pass not run | Run once thresholds are filled in, again after first results. |
| A11 | **Supervisor not yet told that Objective 3 has narrowed** | **Opened 2026-09-08. Do this before building against the decision.** Sinharaja is now detection-only, so E7 measures detection transfer only and classification is dry-zone. He raised the scope to the network on 2026-08-20; this narrows what Objective 3 can claim. One paragraph, stating that it is schedule-driven and taken before M13 was measured. **A10 closed separately (2026-09-24) - no longer needs bundling with this one, but still worth raising together if the same conversation covers it.** |
## F. Closed or superseded
 
| ID | Item | Resolution |
|---|---|---|
| I1 | Event definition / duplicate handling | Retained as **machinery**, no novelty claim (2026-08-20). Re-notify rule no longer relevant - notification is out of scope. |
| I3 | Feature design and leakage | Handled by the window firewall + resolution firewall in labelling_protocol.md §3. Remaining work is the feature list itself, which is scheduled work. |
| I4 | Progressive classification transition rules | Two-stage design adopted 2026-08-20. Initial label is `uncertain`, never a default lean toward the majority class. |
| I7 | Landsat / sensor mismatch | Closed by construction - Obj 1 specifies Sentinel-2 + Sentinel-1. **Reopens only via G4**: any GFW comparison inherits a resolution and temporal-granularity mismatch that must be stated. **UNVERIFIED 2026-08-20:** this row previously asserted the GFW baseline is built on Landsat-derived *annual* loss. That is a claim about the underlying tree-cover-loss data, which is a **different thing** from the driver label - the driver-label correction does not settle it either way. Check against the primary source before the mismatch is described anywhere in the dissertation. |
| I10 | Field evidence reliability | Withdrawn - accountability component removed. |
| I11 | Tamper-evident ledger design | Withdrawn - accountability component removed. |
| D1 | External training data - in or out | **Closed 2026-08-20: local only.** Sri Lankan events only; no foreign labelled events. Fallbacks for thin counts are longer period, more areas, or two classes - not more data. |
| I-inc | Incident source treated as a pipeline input | Corrected 2026-08-20. The pipeline generates its own events from the monitoring loop. The incident source sits on the **evaluation** side: a recall check and a labelling seed. |
| I12 | End-to-end timing / "near-real-time" | Resolved: **no near-real-time claim is made.** Evaluation is retrospective operational simulation. Now a standing guardrail in SKILL.md. |
| A1 | Accountability removal not in writing | **Closed 2026-08-21 - raised and approved.** Previously closed 2026-08-20 on the reasoning that the component was never in approved scope, so no sign-off was needed. Raised with the supervisor anyway on 2026-08-21; reported words: *"no issue to remove blockchain."* He treated it as a **scope change he was approving**, not as something outside scope all along - his reading governs, so the earlier "no sign-off needed" reasoning is superseded even though the outcome is the same. The decision itself remains my own (decisions.md 2026-08-20); he approved it, he did not direct it. **Residual, now A10:** his word was *blockchain*, and the removal also covers the mobile field-evidence prototype. |
| A2 | Title change not confirmed | **Closed 2026-08-20 (later same day).** The title is a working title, not a registered one. It needs to be settled before submission, not before a supervision meeting. |
| A10 | Scope of the supervisor's accountability approval | **Closed 2026-09-24.** Opened 2026-08-21 because his "no issue to remove blockchain" was ambiguous on whether it covered the mobile field-evidence prototype, not just the ledger/anchoring mechanism. Asked him directly; his words as reported: *"not mandatory, classifier is enough"*, with a timeline reason alongside it. His approval covers all three withdrawn items. See decisions.md 2026-08-20 (amended 2026-09-24). |
 
---
 
## Opened 2026-09-08 by the calibration pilot
 
| ID | Issue | Why it matters |
|---|---|---|
| B6 | **The forest test is single-year and cannot identify forest** | `FOREST_NBR >= 0.40` on one year's median NBR passed cropland, scrub and open water in the pilot. Needs a multi-year stable-forest mask: land above the threshold in **every** year of a baseline period, not one. Blocks the screen rebuild. |
| B7 | **`WATER_OCC = 25` did not exclude a seasonal tank** | Event 5 (Kalukolawala) passed the JRC mask. Edge pixel or JRC gap on small seasonal tanks. Needs a lower occurrence threshold, a buffer around water, or a second water source. |
| A12 | **Farmland and settlement inside the legal park boundary** | Confirmed inside the AOI: paddy plots, a road, a village, a shop. "Protected area" does not mean "all forest" in Sri Lanka. Affects A9, affects how the artefact's coverage claim is worded, and is a genuine finding worth stating in Chapter 5 rather than a nuisance to mask away. |
| M15b | **Step 0 false-positive rate** | New protocol Step 0 produces a `false_positive` count. That rate is a screen-quality measurement and belongs in the results, not a labelling failure. Report it. |
| M16 | **Fraction of events with high-res imagery INSIDE the loss window** | Distinct from M3 (imagery exists at all). Step 1 needs an image in the window; bracketing images cannot show what happened between them. Record `highres_in_window` per event. |
 
## Opened 2026-09-09 by the national census
 
| ID | Issue | Why it matters |
|---|---|---|
| A13 | **The sites with events are not national parks** | The top of the pixel census is almost entirely Reserved Forest and Sanctuary. Sites with measurable loss have weaker legal protection. This turns A9 from a footnote into a live constraint: the calibration site will probably not be a national park, so "protected areas" in the title and abstract must be **defined**, not assumed. Also a genuine Chapter 5 finding about where loss actually occurs. |
| B8 | **Climatic zone of every shortlisted site is UNVERIFIED** | Kahalla-Pallekele, Gal Oya Valley South-East, Nuwaragala, Maduroad, Victoria Randenigala Rantambe. The dry/wet contrast with Sinharaja depends entirely on this, and that contrast now carries E7 alone. Needs a primary source in sources.md before the site choice is logged. |
| M18 | **Temporal spread of events at the chosen site** | A site with 200 events in one year is one incident, not six years of driver activity. Checked on `n_2019`..`n_2024` in Part B. Criterion (d) of the selection rule. |
| A14 | **Wilpattu's near-zero loss may itself be reportable** | A well-protected dry-zone park with ~18 events in 6 years says something about protection effectiveness in Sri Lanka. Useless as a training site, possibly useful as a result. Chapter 5. |
 
## Opened 2026-09-12 by the site sanity checks
 
| ID | Issue | Why it matters |
|---|---|---|
| B9 | ~~**Home-garden tree cover is indistinguishable from forest**~~ | **CLOSED 2026-09-12.** Frozen Step 0 rule added to labelling_protocol.md: four pre-event indicators (settlement proximity, regular planted spacing, plot boundaries, heterogeneous planted canopy); >=2 clearly present -> `prior_landcover = home_garden`, candidate excluded from the forest-loss reference set; contradictory or insufficient evidence -> `uncertain`, no forced decision. Rule was written before re-inspection and unchanged after. Applied to the two pending Kahalla cases: **#1 = home_garden (indicators 1, 3); #4 = home_garden (indicators 1, 3, 4)**. Both excluded. **Kahalla's confirmed forest-loss rate is therefore 4 of 8, final.** Site decision unaffected (4 vs Gal Oya's 0). |
| B10 | **Water-edge false positives are systematic across all sites** | Four cases, three sites, two methods: Wilpattu tank edge (Kalukolawala), Wilpattu villu margins x2, Gal Oya reservoir shoreline. Drawdown zones cycle green-to-bare with water level. `WATER_OCC = 10` + 30 m buffer did not catch them, and **Hansen has the same blind spot** - the reservoir case came from the Hansen frame, not from a screen. Sri Lankan PAs are full of tanks and reservoirs. Chapter 5 material as well as a masking problem. |
| M19 | **Step 0 needs the EARLIEST available image, not just one before the window** | Events resolved confidently used three dates including 2013-2014. Events left uncertain used two. Going back far enough is what makes Step 0 work - and it raises minutes-per-event above the 6 min measured on obvious false positives. **Confirmed again 2026-09-19:** CAL_001 went to `uncertain` precisely because the oldest usable image was 2019-05, about three years before the drop, and the 2022 image was clouded. |
 
## 2026-09-12 (later) - Kahalla random batch failed; pivoted to curated reference set
 
**The Kahalla 30-event random batch (seed 42) is CLOSED at 0/10 confirmed.** Screened
KAH_001-010 by Step 0 then trajectory:
- 001, 002: cropland (false positive)
- 003, 004, 007: home_garden (Step 0a)
- 005, 006, 009: tank / water margin (B10)
- 008: plantation (Kandegama)
- 010: passed Step 0 as forest, but the NBR trajectory showed NO sustained drop -
  withdrawn at the second gate. The 0.09 ha pin likely sits off the visible clearing.
This does NOT estimate the population rate and is not claimed to. It is enough to reject
Hansen-at-Kahalla as the SOLE random sampling frame operationally (decisions.md 2026-09-12
curated-reference-set entry).
 
**PIVOT: curated confirmed-forest-loss reference set.** Candidate LOCATIONS from Hansen
across four sites - Nuwaragala, Maduroad, Victoria Randenigala Rantambe, Kahalla-Pallekele
(Gal Oya and Wilpattu excluded). Two manual gates per candidate: Step 0a/0b in Google
Earth, then trajectory confirmation. Target: 30 confirmed events, any class mix.
 
**Screening queue built (build_screening_queue.js, seed 7):**
- 1,513 raw Hansen candidates -> 591 after filters (area_ha >= 0.5; centroid >= 60 m from
  JRC permanent water). By site: Kahalla 163, Victoria 171, Nuwaragala 153, Maduroad 104.
- Queue of 250 exported: asset `projects/gsignin-501704/assets/REF_screening_queue`,
  CSV `REF_screening_queue.csv`, GeoJSON `REF_screening_queue_polygons`.
~~**CURRENT STATE (where a new session resumes):** about to screen REF_001 downward.
Nothing in the REF queue screened yet.~~
**SUPERSEDED 2026-09-19 - see the CURRENT STATE block at the foot of this file.**
REF screening is complete: REF_001-REF_058 screened, **30 confirmed, 18 uncertain,
10 false positive.** The set is frozen.
 
## New issues opened 2026-09-12 (later)
 
| ID | Issue | Why it matters |
|---|---|---|
| B11 | **Step 0a fires on open cropland, not only home gardens** | Indicators 1 (settlement) + 3 (plot boundaries) are both present in ordinary farmland beside a village. KAH_001, KAH_002 fired 0a but are cropland, not garden tree cover. The EXCLUSION is correct; the LABEL is not. Consider an ordering change or a canopy-presence precondition on 0a AFTER the batch, never during it. |
| B12 | **A Step-0 pass can be withdrawn by the trajectory** | KAH_010 passed Step 0 as forest but the NBR series showed no sustained drop, so it does not count. This is the second gate working as intended, not a bug. On sub-0.5 ha events, pin-vs-clearing offset is the likely cause - the reference queue's 0.5 ha floor reduces it. Record trajectory-withdrawn events separately from Step-0 fails. |
| M20 | **B3 (class prevalence) is now unanswerable from the reference set** | A curated reference set cannot estimate prevalence by construction (decisions.md 2026-09-12). B3/B4 must be reported as not-estimated, not left implying a number exists. The random CAL batch gives a narrow substitute only - see B3. |
 
---
 
## Opened 2026-09-24 by building the REF-set export
 
| ID | Issue | Why it matters |
|---|---|---|
| B21 | **`[T5]` core-pixel erosion was never actually applied to any trajectory data** | Found while building `REF_batch_timeseries_export.js`: the real script that produced `calibration_batch.csv` (`cal_batch_timeseries_v72.js`) measures NBR/valid_pct on the raw, uneroded polygon. Erosion was only ever a separate diagnostic used to pick `[T5]=10m` itself (issues.md M22-adjacent finding, decisions.md 2026-09-22), never applied to the NBR series actually used to date or classify any of the 20 CAL events. REF is now built the same (uneroded) way, so CAL and REF stay comparable, but the "mixed edge pixels do not drive the signal" protection labelling_protocol.md §4 claims does not exist in practice, for either set. **DECISION PENDING: check whether this matters (re-extract a few CAL events eroded, compare labels/thresholds) - if it does, both CAL and REF need redoing.** See decisions.md, 2026-09-24 (later still). |
| B22 | **REF export blew GEE's memory limit at 30 events in one call** | Same failure mode already hit and fixed on the CAL batch (mosaic-first per-day processing is heavy). Fixed the same way: run in groups of five, six exports instead of one (`REF_batch_timeseries_export.js` v2). Not a data-quality issue, just a compute-limit one - noted so the pattern is recognised faster next time a batch script is written. |
| B23 | **`STAT_REDUCER`'s combined count() is wrong - a third, separate valid-pixel bug, distinct from B14/B15** | Confirmed on REF via a single-date diagnostic (bare `count()`=54, combined-reducer `count()`=72, same image/geometry/scale) and matched by symptom in CAL group 1 (77.9% of rows have valid_pct>100%, 98.6% single-tile - same signature as REF's 79%). Not B14 (same-date multi-tile combine) or B15 (mosaic/projection) - `.reproject()` vs `.setDefaultProjection()` made no difference, isolating this to the `.combine()` chain itself. B15's own validation rule only checked NBR equality on a single-image mosaic, never count, which is why this slipped through. **CAL side: RESOLVED 2026-09-25.** `[T6]`/`[T7]` were set from dates read via `event_timeseries_v6.js` (and its per-event copies), a *different* tool that computes `n_valid`/`n_total` via separate `reduceRegion()` calls and never had this bug - confirmed by direct code read. `[T6]`/`[T7]` are back to frozen; see decisions.md, 2026-09-25. **REF side: CLOSED 2026-09-25.** `REF_batch_timeseries_export.js` fixed to v3 (separate `count()` call, same fix as CAL's v7.3) and all six groups re-run, including group 1. Merged as `claude/REF_all_timeseries.csv`: 7,818 rows, all 30 REF events present, 0 rows with `valid_pct>100`, 0 rows with `n_valid>n_total`, 0 rows with `NBR` outside [-1,1]. The old `REF_timeseries_v1_g1.csv` is superseded and should not be used. |
 
## Opened 2026-09-19 by the calibration batch (CAL_001-CAL_020)
 
> Three tooling bugs and six method findings, all surfaced while screening the first
> two events. Every one of them would have propagated silently into the frozen
> thresholds if the batch had been run without checking. **This is what the
> calibration batch is for** - the findings are results, not embarrassments, and they
> belong in Chapter 5.
 
### Tooling bugs
 
| ID | Issue | Why it matters |
|---|---|---|
| B14 | **`valid_pct` same-date combine was wrong (v6 of the time-series tool)** | The combine took `sum(n_valid)` against `max(n_total)`. That is only correct when tiles **split** the polygon. When two tiles each **cover** it - orbit overlap - `n_valid` doubles while `n_total` does not. **Measured across the CAL batch: CAL_007 wrong on 270 of 290 dates (worst 400%), CAL_008 on 254 of 305 (worst 361%), thirteen other events on 1-8 dates each.** Effect: partly cloudy dates pass the clear-observation filter, so cadence counts and **four of the seven mandatory §6 `uncertain` triggers** are computed from inflated numbers. NBR values were NOT affected - a weighted mean stays a valid mean. Fixed by mosaicking each day before reducing (v7). |
| B15 | **`mosaic()` silently drops the projection** | The v7 fix was correct in principle but produced **`valid_pct > 100` on 78% of rows** and moved NBR by up to 0.60. Cause: a mosaic has no native projection, so GEE substitutes a default; `reduceRegion(scale: 10)` then resamples the masked image and the `unmask(-99)` image onto **different grids**, and the two counts stop being comparable. Same class of fault as the original v5 bug, in a new place. Fixed in v7.2 with `setDefaultProjection` taken from the source image. **Validation rule for any future version: on a date with one image, a mosaic of one image is that image, so NBR must be identical to the single-image tool. If it is not, the grid is wrong.** **Superseded in part 2026-09-24 (B23): this rule checked NBR equality only, never count - which is why B23's combined-reducer bug passed it undetected. Any future validation rule must also check count() equality.** |
| B16 | **A CSV uploaded to GEE as a table asset has EMPTY geometry** | `CAL_screening_queue_seed99` was uploaded from the CSV. A CSV carries `lat`/`lon` columns, not polygons, so every feature came back `geometry: Empty` and the time-series tool returned **zeros for everything, with no error**. The `geom_type: Polygon` column is text carried over from the build, not real geometry. Silent zeros are worse than a crash. Polygons rebuilt from Hansen and matched to the 20 rows by centroid (`rebuild_cal_polygons.js`, 2026-09-19): worst match distance **0 m**, area ratios **0.9999993-1.0000007**, zero loss-year mismatches. New asset `CAL_screening_queue_poly`. **Delete or rename the broken asset** so nothing points at it again. |
| B17 | **`bestEffort: true` in `reduceToVectors` makes patch vectorisation non-reproducible** | It lets GEE change the working scale with region size, so the same parameters can return a different decomposition. **CAL_002 came back as a 2-part MultiPolygon and CAL_008 as a 3-part MultiPolygon, where the queue CSV recorded both as `Polygon`.** Areas still match to 0.4%, so these are the right patches - but the shape breakdown differs, and that changes every core-pixel and erosion number. **This affects `build_screening_queue.js`, so it affects the FROZEN REF queue too.** Chapter 5 at minimum; a reproducibility caveat on the whole sampling frame. |
 
### Method findings
 
| ID | Issue | Why it matters |
|---|---|---|
| B18 | **A GRADUAL event cannot be dated by the §4 interval method** | §4 assumes a step - `t_forest` is the last clear observation at forest level, `t_loss` the first showing loss. **CAL_005 declines steadily from ~0.50 to ~0.20 over roughly 18 months and never recovers** (four years of tail confirm it). No step exists, so any date pair yields an enormous interval, which `[T7]` then rejects. **A gradual event is therefore discarded for being gradual.** This project names **baseline creep** as its central failure mode and `project.md` requires E1 to include gradual-expansion cases. If §4 discards them, the method is never evaluated on the case it was designed for. Needs a design answer, not a patch. **RESOLVED 2026-09-27.** Checked how CAL_005 itself was actually labelled (2026-09-20): it never went through `[T7]` at all - classified directly from agreeing Step 1 (structural) + Step 3/4 (trajectory) evidence, no interval computed. Formalised as a rule: `[T7]` only rejects to `uncertain` when the date genuinely can't be pinned down *and* nothing else settles the class - it does not override when Step 1 and Step 3/4 independently and clearly agree. See decisions.md, 2026-09-27. Reopened and reclassified three REF events under the corrected rule: REF_025 (`uncertain`→`permanent_encroachment`), REF_012 (`uncertain`→`permanent_encroachment`), REF_058 (`uncertain`→`cultivation`, labeller judgement call, trajectory only partially agrees). |
| B19 | **Hansen's `lossyear` does not match the observed change in several events** | CAL_001 (`lossyear` 2023) has **two** drops - 2022-07 and 2023-08 - each followed by full recovery; Hansen's year matches only the second. CAL_003 (`lossyear` 2019) sits stable at ~0.45 from 2019H2 to 2023H1 and then declines from late 2023. Hansen supplies WHERE and WHEN-approximately, and the protocol already says its year is a hint and never `t_loss`. **The new part is the rate:** this is not occasional. Count it across the batch and report it. |
| B20 | **`lossyear = 2019` events may have lost their forest BEFORE the archive starts** | CAL_002: Google Earth shows dense canopy in 2018-02 and bare ground in 2020-03, so the loss is real - but the Sentinel-2 series starts 2019-01-01 already at NBR 0.208 and goes negative by March 2019, and then cycles bare/green annually for eight years. **There is no observation of this patch as forest anywhere in the series, so `t_forest` cannot be established.** Hansen compares annual composites, so `lossyear = 2019` can reflect change from 2018. **The protocol has no outcome for this case** - it is not `false_positive` (it was genuinely forest), not `home_garden`, and calling it `uncertain` pools it with events that merely had weak evidence. Affects CAL_002, CAL_003, CAL_012 in this batch, and an unknown number in the frozen REF set. **DECISION PENDING: `uncertain`, or a new `loss_predates_archive` outcome.** |
| M21 | **Hansen-year mismatch rate and archive-predating rate** | Count both across the CAL batch and report them. Together they measure how well an annual global product anchors event-level work - which is a contribution-relevant number, not a nuisance. |
| M22 | **The 0.5 ha screen floor and the §4 erosion rule are in conflict** | A 0.53 ha patch is ~53 pixels at 10 m. Measured across the CAL batch: **erode 1 px (10 m)** and the smallest event keeps 16; **erode 2 px (20 m)** and five events drop to 4 or fewer, CAL_007 to **zero**; **erode 3 px (30 m)** and **ten of twenty events vanish.** `[T5]` and `[T15]` are therefore **not independent choices** - together they decide whether half the sample survives. **Half the CAL batch is under 1 ha**, and the REF set was drawn from the same floor, so expect the same split there. This is also the first real evidence for the open "practical minimum reliable event size" question. |
| M23 | **In-polygon observation cadence varies about 2x with orbit overlap, not just cloud** | Measured clear observations per year inside the polygon: **18-34/yr for most CAL events, but ~72/yr for CAL_005**, which sits in a Sentinel-2 orbit-overlap zone. Two consequences: the old scene-level figures (39/yr at <60% cloud, 13/yr at <20%) were both wrong in different directions, and **cadence is not a national constant** - it depends where the polygon falls relative to the satellite tracks. Feeds M1, D2, D9 and the blackout-gap width. |
| A15 | **The CAL sampling script is not saved anywhere** | `build_screening_queue.js` in the project is the **REF** builder - seed 7, `queue_id`, `sampling_origin: gfw_seeded`. The CAL queue uses seed 99, `cal_id` and `hansen_seeded`, so a modified copy exists but is not in the project. **The calibration batch's sampling method is therefore unrecorded**, which breaks the SKILL.md rule that a measurement counts as primary only if the method was recorded. It also means the open question *"did the CAL draw exclude the already-screened REF rows?"* cannot be answered. `rebuild_cal_polygons.js` is a RECOVERY script and must never be cited as the sampling method. **Save the real script as `build_calibration_queue.js`.** |
| A16 | **Two things the register refers to but does not define** | (1) `decisions.md` 2026-09-19 cites **"B13 data-quality corruption"** as a known failure mode, but no B13 row has ever existed in this file. Either write it or stop citing it. (2) `labelling_protocol.md` §7 says `confidence` is assigned "by your own stated rule" - **that rule has never been written down.** Working rule adopted 2026-09-19: **high** = both evidence types agree and nothing is missing; **medium** = one is weak or missing but the call is clear; **low** = the call could reasonably have gone the other way. Note that confidence applies to the label written, including when that label is `uncertain` - "high confidence + uncertain" means *I am sure this cannot be resolved*. Write it into the protocol before the freeze. |
| A17 | **`sampling_origin` has two names for the same thing** | REF rows carry `gfw_seeded` (from `build_screening_queue.js`); CAL rows carry `hansen_seeded`. Same method, two labels - and `hansen_seeded` is not one of the three values labelling_protocol.md §2a permits. Pick one, use it everywhere, and add it to §2a if it is the new one. |
 
---
 
## CURRENT STATE (where a new session resumes) - 2026-09-19
 
**REF set: COMPLETE and FROZEN.** REF_001-REF_058 screened; **30 confirmed, 18
uncertain, 10 false positive.** Queue frame `REF_seed7_0.5ha_60m`. The 30 are
**confirmed forest loss only - none has a driver label.** The set is idle until the
protocol is frozen (decisions.md 2026-09-19). Three are date-unreliable: REF_040,
REF_049, REF_058.
 
**CAL batch: IN PROGRESS, 2 of 20.**
- **CAL_001** - Victoria Randenigala Rantambe, 0.53 ha, `lossyear` 2023. `class =
  uncertain`, `prior_landcover = uncertain`, `hg_indicators = none`, stopped at
  Step 0b, confidence **medium**, 6 min. Two loss episodes in one polygon; oldest
  usable high-res image ~3 years before the drop and the closest one clouded.
- **CAL_002** - Kahalla-Pallekele, 0.80 ha, `lossyear` 2019. Passes Step 0b (dense
  canopy 2018-02, bare 2020-03) but `t_forest` is not observable - see B20.
  **Awaiting the `uncertain` vs `loss_predates_archive` decision. Row not written.**
- Batch size confirmed at **20**. Review the pace at CAL_010: if the last events would
  be rushed, cut to 12-15 **then**, on evidence, and log it. A rushed calibration event
  sets thresholds for everything downstream.
**Tools as they now stand:** `event_timeseries_v6.2` (single event; adds a core-pixel
erosion diagnostic, per-year clear counts, and a post-study-period tail count, and
reads the archive to 2026-09-20 rather than stopping at the study-period end - the
study period decides which EVENTS are eligible, not how far the archive is read after
`t_loss`). `cal_batch_timeseries_v7.2` (all events, mosaic-first, grouped in fives to
stay inside GEE's memory limits). `rebuild_cal_polygons.js` (recovery only).
`calibration_batch.csv` - header corrected 2026-09-19 to restore the twelve §7 fields
the first version dropped, plus `core_pixels_after_erosion` and `uncertain_triggers`.
 
**Known gap that cannot be closed yet:** `n_clear_feat_s1`, `n_clear_feat_s2` and
`n_clear_label_window` require `[T2a]`, `[T2b]` and `[T3]`, which this batch exists to
set. **No event in this batch can have those three fields filled at labelling time.**
Keep every GEE time-series export - they are what lets the counts be computed once the
windows exist. Losing them means re-running all twenty.
 
**Correction 2026-09-24 (B23):** `[T6]=60% valid-pixel cutoff`, listed as frozen above,
was **downgraded to unverified** on the assumption that `calibration_batch.csv`'s
valid_pct column (and hence `[T6]`) came from the same buggy combined-reducer tool as
the REF export. **RESOLVED 2026-09-25:** that assumption was wrong. The dating/labelling
work used `event_timeseries_v6.js` (a separate, clean tool - see B23 above and
decisions.md 2026-09-25), not the buggy batch-export script. `[T6]` and `[T7]` are
frozen again. The batch-export bug itself is real and still open, but only for
`REF_batch_timeseries_export.js` - see B23.
 
## Critical path, in one line
 
**~~B2 (boundaries)~~ *found* → ~~B1 (loss date)~~ *done* → ~~G1b (gap text written)~~ *done 2026-08-21*
→ ~~settle start date~~ *done, 2019-2024* → ~~screen run~~ *done, then REJECTED*
→ ~~rebuild screen (B6/B7)~~ *done, v2 REJECTED - identical 4/1/0 pilot result*
→ ~~Hansen frame at Wilpattu~~ *18 events, the site is empty*
→ ~~national pixel census~~ *done, 151 PAs* → ~~Part B event counts~~ *done*
→ ~~site sanity checks, Kahalla vs Gal Oya~~ *done, 8 events each*
→ ~~select site~~ **FROZEN 2026-09-12: Kahalla-Pallekele**
→ ~~resolve B9 (home-garden rule)~~ *CLOSED 2026-09-12, 4/8*
→ ~~build time-series script~~ *done, now v7.2*
→ ~~Kahalla random batch (seed 42)~~ *FAILED 0/10, closed*
→ ~~pivot to curated reference set + build screening queue~~ *done, 591 candidates, seed 7*
→ ~~screen REF_001 downward to 30 confirmed~~ **DONE 2026-09-19, 30/58, FROZEN**
→ ~~SCREEN THE CAL BATCH (CAL_001-020)~~ *done, thresholds set 2026-09-22*
→ ~~set every `[T#]` from the CAL batch~~ *done* → ~~freeze the protocol, dated and versioned~~ *done, v1.0*
→ ~~B23 valid_pct bug found and fixed (CAL side)~~ *done, [T6]/[T7] confirmed unaffected 2026-09-25*
→ ~~fix `REF_batch_timeseries_export.js` (B23) and run groups 1-6~~ *done 2026-09-25, `REF_all_timeseries.csv` clean*
→ ~~driver-label the 30 REF events~~ *done 2026-09-27*
→ ~~Stage 1/Stage 2 feature lists fixed, window floors set~~ *done 2026-09-28*
→ ~~D6 Stage 1: hand-set thresholds, 3-of-3 vote~~ *done 2026-09-28*
→ ~~D6 Stage 2: logistic regression, LOOCV~~ *done 2026-09-29, D6 fully closed*
→ **build both classifiers into working code the registry can call** → wire the event
registry to real classifier output → E2 (per-stage + end-to-end accuracy) →
minimum-viable E3 (progressive revision demonstrated on a small subset, not the full
quarterly-grid architecture) → demonstration case → write up.
→ log the climatic-zone source (B8), still open.**
 
**DETECTION-LOOP SCOPE CUT CONFIRMED 2026-09-28.** Supervisor approved removing the
standalone monitoring-loop/detection-build entirely (per the student's account this
session - not yet logged with his exact wording, see decisions.md open item). Hansen/GFW
loss patches serve as the detection input for the panel and submission. This removes
the largest unbuilt component from the critical path above: seasonal correction,
reference management (D10) and the detection loop itself (B5's architecture question)
are no longer gating the submission deliverable. **B5's row above may now be reporting
material only, not a blocker - confirm this reading before relying on it.**
 
**The queue is no longer single-file.** Added 2026-09-19: **roughly 60% of the build is
not blocked by labelling.** Seasonal correction, the detection loop, reference
management and the event registry need no labels, no frozen protocol and no `[T#]`
values. Only feature extraction and the two classifiers are blocked. **Run two tracks.**
The event registry is the cheapest place to start - plain code, no remote sensing.
**Superseded in part 2026-09-28: with the detection loop cut, seasonal correction and
reference management are no longer needed for the submission deliverable either - see
the scope-cut note above. Only the event registry (already built, v1) and the two
classifiers (D6, now closed) remain, plus wiring them together.**
 
~~**M4 is the hinge.**~~ **M4 is measured: ~6 min/event floor, 10-15 min expected for
real events. Labelling speed is NOT the binding constraint.**
 
~~**The binding constraint is candidate quality.**~~ **Superseded 2026-09-09. The binding
constraint was EVENT SUPPLY.** Wilpattu contains ~18 loss events in six years. No screen,
however well built, produces a training set from a landscape with almost nothing in it.
Both screen rebuilds were solving the wrong problem, competently.
 
~~**Site selection now blocks everything downstream.**~~ **Resolved 2026-09-12.**
 
~~**B9 now blocks labelling.**~~ **Closed 2026-09-12.**
 
~~**Nothing blocks the work now. The task is screening effort.**~~ **Superseded
2026-09-19. The binding constraint is now BUILD TIME.** **Superseded again 2026-09-28:
with the detection loop cut, most of what remained of "build" is now wiring the two
now-decided classifiers into the event registry, plus writing. The binding constraint
for the 2026-10-20 submission is very likely WRITING TIME, not build time - confirm
current chapter-draft status before treating this as settled.**
 
Note the reordering: B3 and B4 are *outputs* of the calibration batch, not
prerequisites for it. They looked like blockers because the register assumed the
incident source carried driver labels. It does not.
 
## What is realistically achievable by 2026-10-20 (submission)
 
**Decided and defensible as they stand:** B1 (loss-date interval method), B2 (boundary
dataset, 679 WDPA polygons), D1 (Sri Lankan training data only), G6 (GFW as comparator,
never as label source), G1a/G1b (gap structure and text), A1/A2, study period 2019-2024,
Sinharaja detection-only, site configuration frozen, REF set frozen, D6 (both stages).
 
**Protected - these carry the contribution and are not cut:** E2 (two-stage
classification, per-stage *and* end-to-end) and E3 (progressive revision). Progressive
attribution is the entire novelty claim; reducing here leaves a detector.
 
**Cut 2026-09-28, confirmed with supervisor (own account, wording not yet logged
verbatim):** the standalone detection loop, seasonal correction, and reference
management (D10). Hansen/GFW is the detection input for the panel deliverable. This is
the single largest change to feasibility this project has had - it removes roughly half
of what "Build status" in project.md listed as not-yet-started.
 
**Reduction candidates still live, in the order they should be cut if time is still
short after the above:** E5 (event registry is already machinery with no novelty claim
and v1 already exists), then the classification half of E6 (stratifying a thin labelled
set by season will leave cells too small to report - saying so is an honest result).
**E7 is now mostly moot** given the detection-loop cut - the zonal recalibration cost
that E7 measured was a detection-side result, and detection is no longer being built for
this deliverable. Confirm with the supervisor whether E7 drops entirely or is reworded to
describe classification-only zonal transfer (which was never measured anyway, Sinharaja
being detection-only).
 
**Demonstration stays.** Removing it was considered on 2026-09-19 and rejected: it is a
required Design Science step, SKILL.md requires it kept separate from evaluation, and it
is cheap once the artefact exists. Cut expensive things, not cheap ones.
 
**Unbounded until measured:** the E1 reference-interpretation set - **though E1 itself
may now be largely moot for the same reason as E7**, since E1 measured detection
performance and detection is no longer being independently built. Confirm scope before
sizing this.
 
**Not achievable and should not be attempted:** classification transfer between zones,
any nationwide performance figure, a second labeller.
 
---
 
## What was realistically achievable by the 2026-08-21 meeting (superseded, kept for the record)
 
**Closed by decision, and defensible as they stand:** B1 (loss-date interval method),
B2 (boundary dataset found, 679 WDPA polygons), D1 (Sri Lankan training data only),
G6 (GFW as comparator, never as label source), G1a (gap structure agreed), A1/A2.
 
**Achievable only if already run:** B3 and B4 (need the 30-event calibration batch),
M1 (in-polygon clear observations by month). If the batch has not been run, these are
*method stated, number pending* - say so in those words.
 
**Must be done before the meeting regardless of time:** ~~G1b~~ **done 2026-08-21.**
A6 remains and is now more urgent, not less: the sources.md entry for Sims et al.
still lacks authors, exact title, volume, pages and DOI, and the product is cited by
name in the dissertation's central claim. A citation that cannot be completed is a
citation that should not be made.
 
**Not achievable:** protocol frozen (needs the calibration batch), any labelling at
scale, any result.
 
Say which is which. "Here is what is measured, here is what is decided, here is what
is still open, here is when it closes" is a stronger position than implying the pilot
is finished.
 