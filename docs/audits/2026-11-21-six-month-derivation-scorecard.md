# QOU scorecard: masses and Standard Model structure, May → November 2026

Date 2026-11-21. Issue #8956. Repo `litlfred/qou` at `main` `507688841`. Read-only assessment: no content block, Lean file or producer is changed.

**Revision 2 (same day), after QA on PR #8957.** Version 1 overstated α_em form B (called it derived up to one factor and an independent confirmation of the proton q₀). Corrected in §1, §3, §5 and §6. Revision 3 (same day, second QA pass) relabels Coleman–Glashow, fixes the legend, reconciles the electroweak figures and the sources of two counts. Revision 5 (23:10Z) records the three-strand Coleman–Glashow Lean. Revision 4 (22:45Z) folds in results from the sibling work streams on α_em, the −12, the Borromean word and the /q³ (see §8). Also: m_p/m_e relabelled as the experimental pin, not CAL-2; the −12 result scoped (a); bare α_em and Coleman–Glashow relabelled; binding rows flagged as on a superseded word; m_n given in ppm only.

**Sources.** The live L2 dashboard witness `computations/per-observable-100x-status.witness.json` (computed 2026-11-21 04:22Z), `docs/coordination/owner-rulings.md`, `docs/canonical-derivation-cheat-sheet.md`, and the dated audits under `docs/audits/` (each row cites one). Commit history 2026-05-01 → 2026-11-21 (35,740 commits on `main`). Measured data (CODATA, PDG, AME) appear only in the comparison columns, never as proof inputs.

## Legend

| tag | meaning |
|---|---|
| **D** | derived from the axioms, no fitted or selected input |
| **D\|cal** | derived given a named calibration or pin only (CAL-1 = m_e unit; q₀ evaluated at the experimental proton pin m_p/m_e, a precision substitution for CAL-2 = 𝔇_β, whose proxy is m_μ/m_e) |
| **D\|sel** | derived algebra, but at least one joint was **selected** (a chosen word, integer, normalisation or functional among alternatives) |
| **F** | fitted: selected against the target, or a parameter tuned to data |
| **C** | conjectural: stated, not proved, no fit |
| **O** | open: no construction yet |
| **N** | proved negative (Lean or exact algebra): a route is excluded |

"Free inputs" counts calibrations plus selected discrete choices, since the repo's own rule (AGENTS.md, 2026-09-05) treats selection against the target as fitting.

---

## 1. Bottom line

1. **Two numbers are close, and both are conditional.** With q₀ pinned from the experimental proton ratio m_p/m_e, the figure-eight formula m_μ/m_e = Vol(4₁)/ℏ_q² lands **211 ppb** from CODATA (9.49σ on the ratio). First seen 2026-05-25 at 0.24 ppm, it has not degraded through three re-pins and two convention changes. The fine-structure constant in form B sits **−0.37 ppb (2.4σ)** at the same pin (+79 ppb at the muon pin). Form B rests on four assumed steps: the postulate that b₁/Area is added to 1/α (the decisive gap), the [10]_q in the tree term, the normalisation of H, and the Schwinger factor c = 1 (the exact check gives c ≈ 0.73). These are the closest numbers in the corpus, but closeness is not evidence of correctness under the repo's own rules.
2. **The two cannot both be good at once.** The one-term proton pin gives α_em 2.4σ and m_μ 9.5σ. The two-term pin gives m_μ 0.36σ but α_em 495σ, and the owner reverted it on 2026-11-20 (citing the α cost and that covariant insertions give zero proton self-energy, PR #8565). So α_em and the muon are not two independent confirmations of one q₀; the pin choice trades one for the other.
3. **The L2 dashboard says 1/6 scoreable predictions meet the 100× target (m_K/m_π); the AGENTS.md red-team (2026-08-22) counts 0/6 unconditional parameter-free.** m_K/m_π is the one win and it is fitted.
4. **Both close numbers carry selected joints.** For α_em: the four assumed steps above, and forms A, B and the Chern–Simons tower are all live. A new sorry-free Lean result (sibling branch, not yet merged) shows B and the CS tower differ at q = 1 for every c and κ, so the choice reduces to one axiom question: does the correction survive the classical limit? The owner left it open on 2026-11-21 (bean `qou-aemx`). For the muon–proton check, the proton side m_p = 2(m_μ·F_Bor − 6m_e) uses the Borromean braid (conjecture), a /q³ normalisation (asserted, a 37 % lever), and the integers 2 and 12. On 2026-11-21 the −12 was shown not to arise as a tower correction in the tested class (scope (a); one sub-case C1 is excluded structurally by a pole-order invariant, `ProtonTwelveOrigin.lean`). Writing −12 = −k²·3, the 3 is now derived as the dimension of the proton weight space (PR #8968, merged), but k = 2 is not: neither Reeb realisation in the corpus gives it (KZ ≈ 0.05, Bring triad k = 1), so the 12 is still a fit (scope (a): those two realisations). Without the −12 the proton misses by about 0.65 %. Both are selected, not D: the muon–proton check is **D|sel**, α_em form B is **C / D|sel**.
5. **The rest of the mass spectrum is far.** Q_β is 58 % low, m_n − m_p 35 % low, ⁴He binding 3.3× low. A Lean bound proved today shows the scored Q_β cell can **never** exceed 0.383 MeV at any q (target 0.782). The error sits in the q = 1 base, not in a missing small correction.
6. **Standard Model structure is mostly not derived.** The gauge group, three generations, anomaly cancellation and CKM are open or conjectural. The eightfold way has one derived entry (I₃ on the nucleon doublet, with the coupling c = ½ derived) and a growing set of proved structural facts and negatives.
7. **The trend is real, but it runs in a different direction from "closer numbers".** May had many sub-1 % matches; most were later reclassified as fits. Since August the corpus has gained hard structure: convention D forced, exact closed forms, Lean bounds and exclusions. The numbers got worse because they became honest. That is progress toward a derivation, but not yet progress toward the spectrum.

**On "not proved today says nothing about tomorrow":** agreed. Nothing here is a structural exclusion of the program. The Lean negatives exclude *specific classes* (e.g. "no operator commuting with U_q(sl₂) splits p from n beyond the pivot q²"). They also say exactly what new object would be needed, which is useful.

---

## 2. Masses

Errors use the live dashboard (one-term proton pin, q₀ = 1.10997858275…).

| quantity | status | model vs data | free inputs | source |
|---|---|---|---|---|
| m_e | CAL-1 | defines the MeV unit | 1 (calibration) | dashboard |
| m_p / m_e | experimental proton pin (Physical-Observations layer; not CAL-2, whose proxy is m_μ/m_e) | 0.003 ppb (round trip: q₀ is solved from it) | 1 (pin) | `2026-08-22-mp-fbor-massformula-redteam.md` §1 |
| **m_μ / m_e** (cross-check against m_p) | **D\|sel** | **+211 ppb** (9.49σ on the ratio, σ 22.25 ppb; 9.70σ on the mass) | q₀ + Borromean word + /q³ + integers 2, 12 | dashboard; `2026-11-21-proton-minus-twelve-origin.md` |
| m_μ with two-term QED proton term | F (comparison only) | +8 ppb | adds a selected pair-omission | `2026-11-20-two-term-proton-q0-repin.md` (reverted; costs α_em 495σ) |
| m_n | D\|sel | −486 ppm (absolute mass is excised as a claim, 2026-08-11) | as m_p, plus Q_β | dashboard |
| Q_β (n → p e ν̄) | D\|sel | 0.3254 vs 0.7823 MeV, **−58 %**; Lean: ≤ 0.383 MeV for every q ≥ 1 | 2 cal + scored word V³ + cell identification | `2026-11-21-qbeta-np-error-budget.md` |
| m_n − m_p | D\|sel | 0.836 vs 1.293 MeV, **−35 %** | same cell as Q_β (one error seen three ways) | same |
| n–p cell 2E₀·ln q | D\|cal, unassigned | 0.8735 MeV; owner ruled it is not yet assigned to Q_β or Δm | 2 cal | owner-rulings 2026-11-21 |
| per-quark split (m_d − m_u) | **N** for the derived class; ansatz is F | the ansatz h²ℏ_q/√q matched CODATA by construction | — | `2026-11-21-per-quark-flavor-split-not-derived.md` (`PivotSplitOrder.lean`) |
| quark masses (u, d, s, c…) | O / N | charm-tower and Frobenius-block routes negative | — | `2026-08-02-charm-mass-*` |
| ²H binding (B_can⁰) | D\|cal on a **superseded word** (γγ re-scope 2026-11-15) | 2.33 vs 2.22 MeV, about +5 % | 2 cal | `2026-08-29-mass-provenance-breakdown-and-gap-map.md` §3 |
| ²H…⁴He binding (production B_sym) | **posited** form, superseded word | ratio B_AME/B: 0.79, 1.38, 1.44, **3.26** | 2 cal + posited α ln(·) map | same |
| ⁴He binding, magic-A 2m_e·A·8G | F (census selection) | +5.87 % | knot chosen to match | cheat sheet §9.3 |
| fusion Q-values (D+T) | consequence | wrong sign (−0.3 vs +17.6 MeV) until ⁴He closes | — | provenance map §4 |
| m_K / m_π | **F** | +51 ppb | (3,4) pair scan-selected; EM factor form selected | `2026-11-20-mk-mpi-derivation-status.md` |
| g_A | **F** | +0.1 % | best of three colour averages | `2026-11-15-standard-model-eightfold-way-corpus-map.md` §7 |
| W, Z, H masses (T(2,4), T(2,6), T(2,8)) | C | W/Z = cosh 5η₀/cosh 7η₀, +1.07 % (gap unexplained); Z²/H² = 6/8, ≈ 3 % (both May) | knot assignment conjectural | cheat sheet §5 |
| EW vev fixed point | C, four slots underived | none of tree prefactor, loop sign, loop coupling, zero-mode rule derived | — | `2026-11-20-ew-vev-gaps.md` |

## 3. Couplings

| quantity | status | model vs data | free inputs | source |
|---|---|---|---|---|
| α_em⁻¹ bare q[9]_q[10]_q | **C** (the [10]_q factor is asserted, bean `qou-15sj`) | 136.823, **−0.155 %** | 1 (q₀) | `2026-08-22-alpha-em-deriva*.md` |
| **α_em⁻¹ form B (Schwinger)** | **C / D\|sel** | **−0.37 ppb (2.4σ)** at the proton pin, +79 ppb at the muon pin, +76 ppb at the two-term pin; 238× from the 100× target | q₀ + four assumed steps (b₁/Area added to 1/α; [10]_q; H normalisation; c = 1, exact check gives ≈ 0.73). The value 8/(12π) = b₁/Area is proved. Of the three classes named in rev 2, `ArchimedeanLimit` is proved on [0,1), `BlochSuslinUniqueness` is vacuous (D = 0 only), and `BringZeroModeBlochClass` is expected false with nothing depending on it. One of three live forms; canonical open (`qou-aemx`) | `alpha_em_schwinger_ladder_probe.py`; `2026-11-20-alpha-em-two-term-q0-pull.md` |
| α_em⁻¹ form A | C | +0.99 ppb | live alternative; canonical undecided | same |
| α_em⁻¹ CS tower | C | −468 ppb | κ not derived; live alternative | same |
| α_em⁻¹ 45·[3]_q form | F, ruled out | 2.6 ppb | PSLQ single-point fit | `2026-06-10-alpha-em-legacy-empirical-forms.md` |
| sin²θ_W | F | 0.127 % | best of 74 enumerated candidates | corpus map §1 |
| g = π·h₀, v ratio = log 6 | F/C | ±0.5 % | empirical-match hypotheses (May) | cheat sheet §5 |
| strong coupling, Yukawas, CKM, PMNS | O | — | — | `sm-params-ckm.md` |

Note on α_em (corrected after QA, 2026-11-21): an earlier version of this note called α_em and m_p "two independent observables, one parameter", agreeing on q₀ to 0.053 ppb. That was wrong. The proton pin shares the selected inputs of the proton formula (Borromean word, /q³, the integers 2 and 12), and form B rests on four assumed steps including an underived c = 1, so the agreement is between two conditional constructions, not two independent derivations. The pins also trade off: one-term gives α 2.4σ and m_μ 9.5σ, two-term gives m_μ 0.36σ and α 495σ. The bare backbone is 0.155 % off with an asserted [10]_q. Forms A, B and the CS tower are all live; which is canonical is an open owner decision. The sign of the form-B residual also flipped between CODATA 2018 and 2022.

## 4. Standard Model structure

| item | status | what is actually established | source |
|---|---|---|---|
| gauge group SU(3)×SU(2)×U(1) | **C/O** | quaternionic electroweak facts are textbook; `StandardModelTruncation` is inhabited by the SM group itself (vacuous) | corpus map §1 |
| hypercharge Y | C / N | writhe → Y falsified; GMN closes only with Y = 1/3 put in by hand; the derived-Y class has no instance | corpus map §2 |
| weak isospin T₃ | D (finite toy) | T₃ = sign(κ)/2 grading, 26 Lean theorems; "SU(2) acts on L only" is absent | corpus map §3 |
| N = 2 Schur–Weyl (Jimbo) | **D (Lean)** | kernel = trace radical, H/rad ≅ TL, Jimbo trace = convention D, proved | corpus map §8 |
| convention D (z = q³/(q²+1)) | **D (Lean)** | forced by the N = 2 fibre; a genuine success | `2026-08-08-mass-fibre-dimension-forces-convention-d.md` |
| three generations | **O** | four countings give 4, 3, 2, 3; the "completeness" theorem is vacuous | `2026-10-10-generation-count-two-independent-countings.md` |
| anomaly cancellation | O | absent | corpus map §5 |
| colour channel (1³) | C (conditional) | forced given four S₃ factors + Fermi statistics + Δ⁺⁺ | corpus map §11 |
| N_c = 3 | O / N | seven routes excluded; owner decision pending (`qou-j3w6`) | corpus map §6 |
| confinement | O | the word mostly names the SDP; no colour-singlet theorem | corpus map §10 |

### Eightfold way (asked for separately)

| item | status | detail |
|---|---|---|
| I₃ on the nucleon doublet, Q = w/2 | **D** (two-point match) | coupling c = ½ structurally fixed by `def:coulomb-charge`; the one derived ledger entry |
| A₂ Cartan matrix, roots, weight lattice | standard | true by construction of three strands |
| 3 ⊗ 3̄ = 8 ⊕ 1, decuplet row cap | proved (arithmetic) | representation content carried by names, not by Lean |
| Gell-Mann–Okubo | **N / O** | first order withdrawn; second order under-determined (2 equations, 3 unknowns) |
| Coleman–Glashow Σ = N + Ξ | **proved identity, non-discriminating (Lean, three strands, 2026-11-21)** | `IsospinMurphyOctetThreeStrand.lean` (sorry-free): for the weighted Murphy sum, Σ − N − Ξ = 0 for **every** weight and every flavour order of the Jimbo braiding, because each flavour pair has a one-sided braiding coefficient. So exact CG is evidence for nothing (matches `cg_cannot_discriminate`). Same file: the hypercharge sum gives zero nucleon splitting always, but zero Σ and Ξ splittings only when s is on one side of u and d; with s between them the Σ split is h²(q²+2)(w_s − w_u) |
| sign of the octet isospin coefficient α₂/α₁ | N for this operator (scope a) | +0.056 at q₀ vs lattice −0.141: right structure, wrong sign, 0.4× size |
| strange strand and n − p | **N (Lean)** | an s strand cannot change the n–p direction result |
| octet mass degeneracy m_Λ = m_Σ⁰ | N | weight-only mass forces the degeneracy |
| nonet mixing angle | proved unconstrained | — |

Ledger count (eightfold chapter, 2026-08-08): 1 derived, 3 proved, 8 standard, 2 refuted, 9 open of 23 rows. SM appendix: of 26 SM parameters, 1 input, 1 proxy, 1 partial, 2 conjectural, 21 open. The 2026-11-15 map and today's Murphy-octet work add structure (Coleman–Glashow proved to be a weight-independent identity, several Lean negatives) but no new derived SM parameter.

---

## 5. Trend over six months

### Activity (commit subjects on `main` mentioning each topic)

| topic | May | Jun | Jul | Aug | Sep | Oct | Nov (to 21st) |
|---|--:|--:|--:|--:|--:|--:|--:|
| Q_β | 84 | 324 | 418 | 110 | 70 | 5 | 92 |
| binding / ²H / ⁴He | 173 | 348 | 186 | 288 | 108 | 13 | 44 |
| proton | 98 | 54 | 33 | 146 | 48 | 12 | 59 |
| quark / flavour | 32 | 42 | 16 | 24 | 17 | 11 | 73 |
| eightfold / octet / GMO | 4 | 3 | 0 | 71 | 19 | 3 | 17 |
| gauge / hypercharge / θ_W | 4 | 16 | 17 | 30 | 14 | 1 | 18 |
| generation | 1 | 16 | 8 | 37 | 23 | 2 | 9 |
| all commits | 3,694 | 6,461 | 5,373 | 11,828 | 5,034 | 1,009 | 2,341 |

### What each headline looked like, then and now

| headline | May–June claim | now | why it moved |
|---|---|---|---|
| m_p ↔ m_μ identity | 0.24 ppm (2026-05-25) | 211 ppb m_μ, stable | **held up**; −12 and /q³ now flagged as selected |
| Q_β | +0.17 % "non-calibrated" (2026-05-10) | −58 %, Lean bound ≤ 0.383 MeV | old form needed z = 1, inadmissible under convention D (2026-09-08) |
| m_n − m_p | ~0.14 % (Bring colour-tube scheme 4) | −35 % | colour weighting relaxed to a conjecture (2026-11-21); Bridge B shows only the pivot q² splits p from n |
| m_p absolute | +2.9 % (λ_A volume form) | excised as an absolute claim (2026-08-11) | λ_A was a CODATA-implied fit |
| deuteron | +0.19 % (m_e·Vol·Δtr) | about +5 % (B_can⁰); production form posited | trace convention and word fixed |
| ⁴He | +5.87 % (magic-A) | 3.26× low on production | magic-A was a census selection |
| α_em | 2.6 ppb (PSLQ fit) | −0.37 ppb form B, resting on four assumed steps incl. c = 1; 0.155 % bare | PSLQ form ruled out (2026-06-10); form B built Jul–Nov; canonical form undecided |
| EW ratios | W/Z +1.07 %, Z²/H² ≈ 3 % (g, v hypotheses ±0.5 %) | still conjectural; knot assignment not derived | never derived |
| generations | "3" | 4 / 3 / 2 / 3 unresolved | counting criteria disagree |

### Reading the trend fairly

- **Precise results:** in May each later turned out to carry a fit. Now there are two ppb-level numbers with no tuned continuous coefficient (μ–p at 211 ppb, α_em form B at −0.37 ppb), but both are conditional or selected, and the pin choice trades one against the other. The L2 count of unconditional parameter-free predictions is still 0/6.
- **Proved structure:** grew sharply from August. Convention D is forced, the Borromean trace has an exact Lean closed form, N = 2 Schur–Weyl is proved, and Q_β is now one rational function of q times m_e. These are permanent results that any future mass formula has to respect.
- **Proved negatives:** about a dozen this month alone. They localise the gaps sharply. For n − p, the corpus now knows that a symmetry-breaking object beyond U_q(sl₂)-commuting operators is required, and that Q_β's missing factor (about 2.04 of the 2.40) must come from a link that survives at q = 1.
- **Discipline:** the 2026-09-05 no-fit rule, the 2026-08-11 excision and today's "derive, not assert" ruling mean every remaining number is honestly labelled. That is why the scorecard looks worse than in May. It is also why a future match will count.

---

## 6. The test that would change this assessment

A single trace-to-energy map, fixed once and pre-registered, that predicts a **second** observable it was not tuned on. The best candidates, in order of leverage:

1. **Derive the −12** (or the /q³) from the two-term Lagrangian or the electron word. That would turn the 211 ppb μ–p cross-check from D|sel into D|cal, which would be a strong result.
2. **Find the q = 1 factor in Q_β** (about 2.04). The Lean bound says no q-correction can supply it, so it must come from the counting 3/8, the factor 2, or the identification of the cell with Q_β (the β-decay GB reduction now in progress, PR #8904).
3. **Derive the b₁/Area addition and c = 1**, then settle whether the correction survives q → 1 (that decides between form B and the CS tower). Only then is α_em a test of the framework rather than of a selected form.

---

## 7. Next steps (pick by number)

1. ~~Turn this scorecard into a repo doc~~ Done: this file, issue #8956 (owner chose 1 and 4).
2. The −12, Borromean word and /q³ have their own work streams; see §8 for where they stand.
3. Pre-register a "one map, two observables" test: fix the trace-to-energy map on Q_β's GB reduction, then predict Δm or ²H with no new choice.
4. ~~Bring the α_em canonical-functional decision (bean `qou-aemx`) to you~~ Posted as a decision card 2026-11-21.
5. Add a dated "status" column to `sm-params-intro.md` so the 26-parameter count is tracked over time automatically.

---

## 8. Sibling work-stream status (as of 2026-11-21 22:45Z)

| joint | result so far | effect on the rows above |
|---|---|---|
| −12 = −k²·3 | 3 = dim of the proton weight space, Lean, PR #8968 **merged**. k = 2 not found: KZ Reeb gives ≈ 0.05, Bring-triad Reeb gives k = 1, and in that realisation parity forbids k = 2 on three strands | m_μ cross-check stays D\|sel; the 12 is still a fit (scope (a)) |
| Borromean word | PR #8966 (draft): no other word with the same trace at lengths 1–8 under convention-D weights; length-16 search running | still a conjecture, now with a uniqueness check up to length 8 |
| Borromean weight | that stream reports F_Bor divides by the corpus weight y₃ ≈ 0.223, while convention D gives y₃ ≈ 0.505. **Not checked here**; passed to the /q³ stream | if confirmed, the proton formula's inputs change and the 211 ppb must be recomputed |
| /q³ | in progress: proving in Lean that the units of ℤ[q, q⁻¹] are ±q^m | none yet |
| α_em canonical form | Lean (unmerged branch): B ≠ CS tower at q = 1 for all c, κ; owner chose "leave open, draft PR, rewrite the block's framing" | α rows relabelled in rev 4 |
| ⁴He binding | nucleon order is a conjugation, so it cannot change a trace (argument only, not yet proved); next is a γγ formation word | none yet |
