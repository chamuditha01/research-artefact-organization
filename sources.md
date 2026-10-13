# sources.md - Verified Claims & References
 
<!-- Every claim, definition, statistic or method the model gives me
     goes here until I've checked it against a PRIMARY source.
     Unverified = flagged, and NOT used in the dissertation. -->
 
_Last updated: 2026-09-27_
 
The entries below are seeded from the research blueprint and the field guide.
Nothing here is verified yet. Work down the list; anything still marked
`Verified: no` must not appear as a claim in the dissertation.
 
---
 
## Design Science Research methodology - the six-step process model
- From: research blueprint / field guide, 2026-08-16
- Verified: **no**
- Source: Peffers et al. - Design Science Research Methodology (get exact authors, year, journal, volume, pages)
- Notes: Need the primary paper, not a secondary description. One citation in the methodology chapter; the six steps are already used as the project's spine.
## FEDS - Framework for Evaluation in Design Science (artificial/naturalistic, ex ante/ex post)
- From: field guide, 2026-08-16
- Verified: **no**
- Source: Venable, Pries-Heje & Baskerville (get exact year, title, journal, pages)
- Notes: Used to justify the evaluation strategy line in methodology.md. Check that my artificial/naturalistic split is described the way the original defines it, not the way I remember it.
## Sentinel-2 revisit interval and spatial resolution (per band)
- From: primary document, read 2026-09-05
- Verified: **yes** (for the claims listed below only)
- Source: European Space Agency. (2015). *Sentinel-2 user handbook* (Issue 1,
  Rev. 2). https://sentinels.copernicus.eu/documents/247904/685211/Sentinel-2_User_Handbook
  (Issue 1 Rev 2, dated 24 July 2015, 64 pp., ESA Standard Document, no DOI)
- Checked and confirmed:
  - Single satellite: 10-day revisit. Two-satellite constellation: 5 days at the
    equator, narrowing to 2-3 days at mid-latitudes (pp. 8, 51)
  - The 5-day figure is stated as applying at the equator, with the full
    two-satellite configuration, in cloud-free conditions (Table 1 footnote, p. 35)
  - 13 bands: four at 10 m, six at 20 m, three at 60 m (p. 52)
- Notes: **Sri Lanka is equatorial, so 5 days is the applicable figure - not the
  2-3 day mid-latitude one.** ESA's own cloud-free qualifier is useful: it makes M1
  a correction the mission documentation anticipates rather than a contradiction of
  it. The handbook is a 2015 document written before the second satellite launched;
  S2C replaced S2A in operation in January 2025, which does not affect a study
  period ending 2024. Cited in Chapter 1.
## Sentinel-1 archive coverage over Sri Lanka for the study period
- From: [to check directly], 2026-08-16
- Verified: **no**
- Source: query the archive myself during the feasibility pilot; cite the query and date
- Notes: Do not assume coverage. Acquisition plans have changed over the mission's life; this is a pilot output, not a literature claim.
## Forest cover / deforestation rate figures for Sri Lanka
- From: [any figure I am tempted to use in the introduction]
- Verified: **no**
- Source: FAO Forest Resources Assessment, Sri Lanka Forest Department, or a peer-reviewed study - primary only
- Notes: **High risk of a confidently wrong number.** Different sources use different forest definitions and different baselines, so the figures disagree legitimately. Quote the definition alongside the number, or don't quote the number.
## Protected-area designation and legal status (A9) - Reserved Forest / Conservation Forest vs Other State Forest
- From: secondary sources, checked 2026-09-27
- Verified: **partial** (statute-level claims from a law-database copy of the
  Ordinance text, not the Gazette itself; administrative-history claims from two
  conflicting secondary articles, not confirmed)
- Source:
  - Forest Conservation Ordinance (as amended), text via srilankalaw.lk,
    https://www.srilankalaw.lk/f/404-forest-conservation-ordinance.html
    (a law-database copy, not the Gazette PDF - get the Gazette or the official
    consolidated statute before citing section numbers in the dissertation)
  - Raheem, D. (2020, 23 November). *Other State Forests and the conservation of
    Sri Lanka's rainforest biota*. Groundviews.
    https://groundviews.org/2020/11/23/other-state-forests-and-the-conservation-of-sri-lankas-rainforest-biota/
  - *Sri Lanka activists decry downgrade of non-protected "other" forests by
    government*. (2020, December). Mongabay.
    https://news.mongabay.com/2020/12/sri-lanka-activists-decry-downgrade-of-non-protected-other-forests-by-government/
- Checked and confirmed (statute text, moderate confidence - see caveat):
  - **Reserved Forest**: declared by the Minister, published in the Gazette
    (S.3(1)), limits specified, Management Plan required (S.3(2)). S.7(1)
    criminalises felling, timber transport, hunting, quarrying, fire-lighting,
    cultivation and boundary-mark damage inside one - up to 5 years imprisonment
    or a fine of not less than Rs. 10,000. S.8(1) exempts acts done under Minister's
    regulation or a forest officer's written permission.
  - **Conservation Forest** (S.3A): a stricter sub-category for areas with unique
    ecosystems or rare/endemic-species habitat; S.6 raises the maximum penalty to
    7 years.
  - **"Other State Forest" is not a category the Ordinance defines or gazettes at
    all.** It is unreserved state land carrying forest cover, with no statutory
    prohibition on clearing it under this Ordinance.
- **Not confirmed - conflicting secondary sources, do not cite either version yet:**
  the two articles disagree on the administrative history of who oversees OSF and
  when control moved (Groundviews: a November 2020 circular, "MWFC/1/2020," moved
  OSF administration away from the Forest Department to district/divisional
  secretariats, revoking an earlier circular referred to as "5/2001"; Mongabay's
  account of the same period does not match this and adds a claim about 2024 that
  the article's own dateline of December 2020 cannot support). **Do not use any
  specific circular number or date from either source until checked against a
  Forest Department or Gazette primary document.** The one thing both sources
  agree on: OSF administration is a matter of executive circular, not statute, and
  it has changed more than once - unlike Reserved Forest/Conservation Forest status,
  which is fixed by Gazette until degazetted the same way.
- Notes: **Live tension with D11 (issues.md).** D11 proposes monitoring the
  dissolved union of designations including both Reserved Forest and Other State
  Forest as one "protected area" set. The finding above means that union mixes a
  statutorily-protected category with a legally unprotected one - a clearing
  event's legal status differs by designation even inside the same monitored
  boundary set. Framing decision is still open (raised in chat 2026-09-27, not yet
  decided). Also unconfirmed: whether "Other State Forest" appears as a value in
  the actual WDPA extract used (`WCMC/WDPA/current/polygons`, 679 SL polygons) -
  D11 assumes it does; not checked against the `DESIG_ENG` field. Also ties to
  A13 and G2 (plantation harvest is likely concentrated in Forest Reserve/OSF, so
  a detection there may be lawful activity, not an attribution error).
## Existing operational forest-alert products used as comparison
- From: blueprint, 2026-08-16
- Verified: **no**
- Source: primary documentation for each product I actually compare against
- Notes: Only cite products I have genuinely inspected. For each, record its alert latency, minimum mapping unit and whether it attributes a driver - that comparison is where my contribution is argued.
## ~~Tamper-evident logging / Merkle-tree anchoring and timestamping~~
- **WITHDRAWN 2026-08-20** - accountability component removed from scope
  (decisions.md). Retained only for recovery if the removal is ever reversed.
  Nothing here needs verifying while the component is out of scope.
## Driver classes: cultivation / natural disturbance / permanent encroachment
- From: blueprint, 2026-08-16
- Verified: **no**
- Source: literature on forest-disturbance driver attribution + local context sources
- Notes: Check whether an established driver taxonomy exists that mine maps onto. If it does, mapping to it strengthens the classification chapter considerably; if I invent classes with no lineage, expect the question in the viva.
## GFW / Land & Carbon Lab drivers dataset - Sims et al. 2025
- From: primary paper, read 2026-08-20; further items checked 2026-09-27
- Verified: **partial**
- Source: Sims, M. J., Stanimirova, R., Raichuk, A., Neumann, M., Richter, J.,
  Follett, F., MacCarthy, J., Lister, K., Randle, C., Sloat, L., Esipova, E.,
  Jupiter, J., Stanton, C., Morris, D., Slay, C. M., Purves, D., & Harris, N.
  (2025). Global drivers of forest loss at 1 km resolution. *Environmental
  Research Letters*, *20*(7), Article 074027.
  https://doi.org/10.1088/1748-9326/add606
  (17 authors, all listed - APA 7 lists up to 20. Published 12 June 2025.
  Bibliographic details taken from the IOP article page, 2026-09-05.)
- Checked and confirmed:
  - Spatial unit: dominant driver assigned per **~1 km cell**, stated in the paper
    as 0.01 degree (approximately 1 km at the equator) resolution, globally.
  - Temporal: dominant driver per cell over a **multi-year mapping period**
    (2001-2022), NOT annual event-level attribution - "the direct driver that
    caused the majority of tree cover loss area" within each cell across that
    full period.
  - **Class probabilities: CONFIRMED YES (2026-09-27).** The product provides
    both the dominant-driver classification per cell AND separate maps of the
    probability of each class. The gap-statement sentence drafted 2026-08-21 and
    cut as unverified can now be restored - see project.md.
  - **No event-specific confidence or revision history (2026-09-27).** Confirms
    the core gap claim: this is a static map, one dominant label per cell for the
    whole 2001-2022 period, not a per-event attribution that updates as evidence
    accumulates.
  - **Validation and accuracy (2026-09-27):** stratified random sample of 3,574
    independent validation plots, stratified by region (7) and driver class (7),
    interpreted using the same protocol as training data. Global overall accuracy
    90.5+/-1.4%; regional range 82.8-94.1%; per-class producer's/user's accuracy
    60-97% depending on class and region.
  - **Logging definition (2026-09-27):** logging sits inside the "forest
    management" class, defined as "harvesting in wood-fiber plantations,
    clear-cut and selective logging, establishment of logging roads" and other
    forest management activities. Both clear-cut AND selective logging are
    pooled into one class by the source dataset too - my own G2 pooling of
    logging into `uncertain` is not out of step with how the reference dataset
    itself handles the same ambiguity.
  - Seven driver classes confirmed: permanent agriculture, hard commodities,
    shifting cultivation, forest management (logging), wildfire, settlements &
    infrastructure, other natural disturbances.
- **Source caveat (2026-09-27):** the IOPscience article page itself blocks
  automated fetching (robots.txt). The above was read from a WRI-hosted mirror
  PDF (https://www.forest-trends.org/wp-content/uploads/2025/08/WRI2024-GlobalDriversForestLoss1kmResolutionlowres.pdf),
  title and structure matching the published letter, via an AI fetch-and-summarise
  tool - not a full manual read of the primary text. **Still to do before this
  is safely citable: open the actual IOPscience article yourself and check the
  above against it directly**, especially the accuracy figures and the exact
  "dominant" tie-breaking rule, which the fetch did not fully resolve.
- Still to confirm (G3 remainder - blocks G4, not the gap statement, not G2 which
  is now closed):
  - What "dominant" means procedurally beyond "majority of tree-cover-loss area" -
    exact threshold, tie-breaking rule.
  - Training/reference data: source, sample count, how many fall in Sri Lanka (G5)
- Notes: The class list feeds G2 (closed 2026-09-24, REF-side count added
  2026-09-27). The validation method feeds G4 - a baseline comparison needs to
  know how their number was computed; now partially available above. Both
  narrowed but not fully closed. **Separately unverified (I7):** whether the
  underlying tree-cover-loss data is Landsat-derived and annual. That is a
  different claim from the driver label and is not settled by the above.
## Sri Lankan protected-area boundaries - WDPA
- From: own query, 2026-08-20
- Verified: **partial** (own measurement, query recorded)
- Source: `WCMC/WDPA/current/polygons` in GEE, filtered ISO3 = LKA
- Notes: 679 polygons; sum of `REP_AREA` = 22,362 km2, inflated by overlaps.
  `REP_AREA` is reported area and `GIS_AREA` is geometric - the two are not
  comparable, so the dissolved figure must be redone with `GIS_AREA` (M7). Query
  date recorded; AOI, collection and method recorded. **Outstanding:** designation
  semantics unverified (A9), marine extent not excluded (M9), 103 records carry
  `STATUS_YR = 0` (M8), and WDPA lags national gazette submissions (A8).
## Climatic-zone assignment for Wilpattu and Sinharaja
- From: [assumed, not checked], 2026-08-20
- Verified: **no**
- Source: Sri Lanka Department of Meteorology or a peer-reviewed climatic-zone
  classification - primary only
- Notes: Wilpattu is treated as dry zone and Sinharaja as wet zone throughout the
  sequencing decision, and the E7 recalibration argument depends on the contrast
  being real. Almost certainly correct, but it is currently a fact I know rather
  than a fact I cited.
---
 
## Template for new entries
 
## [the claim / definition / statistic, in a few words]
- From: model, [date]
- Verified: [ no / yes ]
- Source: [author, year, title, page] (primary source only)
- Notes: [what I checked; anything that didn't hold up]