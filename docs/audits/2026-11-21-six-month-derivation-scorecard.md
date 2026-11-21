# QOU scorecard: masses and Standard Model structure, May → November 2026

Date 2026-11-21. Issue #8956. Repo `litlfred/qou` at `main` `507688841`. Read-only assessment: no content block, Lean file or producer is changed.

**Sources.** The live L2 dashboard witness `computations/per-observable-100x-status.witness.json` (computed 2026-11-21 04:22Z), `docs/coordination/owner-rulings.md`, `docs/canonical-derivation-cheat-sheet.md`, and the dated audits under `docs/audits/` (each row cites one). Commit history 2026-05-01 → 2026-11-21 (35,740 commits on `main`). Measured data (CODATA, PDG, AME) appear only in the comparison columns, never as proof inputs.

## Legend

| tag | meaning |
|---|---|
| **D** | derived from the axioms, no fitted or selected input |
| **D\|cal** | derived given a named calibration only (CAL-1 = m_e unit, CAL-2 = q₀ pin) |
| **D\|sel** | derived algebra, but at least one joint was **selected** (a chosen word, integer, normalisation or functional among alternatives) |
| **F** | fitted: selected against the target, or a parameter tuned to data |
| **C** | conjectural: stated, not proved, no fit |
| **O** | open: no construction yet |
| **N** | proved negative (Lean or exact algebra): a route is excluded |

"Free inputs" counts calibrations plus selected discrete choices, since the repo's own rule (AGENTS.md, 2026-09-05) treats selection against the target as fitting.

---

## 1. Bottom line

1. **Two numbers really are close.** The fine-structure constant (form B) sits **−0.37 ppb (2.4σ)** from CODATA with no fitted coefficient, and it independently picks out the *same* q₀ as the proton to 0.05 ppb. Separately, the muon–proton consistency has stayed close for six months. With q₀ pinned from m_p/m_e, the figure-eight formula m_μ/m_e = Vol(4₁)/ℏ_q² lands **211 ppb** from CODATA (2.1 × 10⁻⁷). First seen 2026-05-25 at 0.24 ppm, it has not degraded through three re-pins and two convention changes. Together these are the strongest quantitative results in the corpus.
2. **But both carry joints that are not yet derived.** For α_em it is one: the Schwinger factor c = 1 is structurally motivated, not fitted, but its exact check failed (it needs c ≈ 0.73), and whether form B or the Chern–Simons tower is canonical is an open decision. For the muon–proton check there are more. The proton side, m_p = 2(m_μ·F_Bor − 6m_e), uses the Borromean braid (conjecture), a /q³ normalisation (asserted, a 37 % lever), and the integers 2 and 12 (read off after the fact). On 2026-11-21 the −12 was shown **not derivable** as a correction to the Borromean tower (`ProtonTwelveOrigin.lean`). Without the −12 the proton misses by about 0.65 %. So it is **D|sel**, not D.
3. **The rest of the mass spectrum is far.** Q_β is 58 % low, m_n − m_p 35 % low, ⁴He binding 3.3× low. A Lean bound proved today shows the scored Q_β cell can **never** exceed 0.383 MeV at any q (target 0.782). The error sits in the q = 1 base, not in a missing small correction.
4. **Standard Model structure is mostly not derived.** The gauge group, three generations, anomaly cancellation and CKM are open or conjectural. The eightfold way has one derived entry (I₃ on the nucleon doublet, with the coupling c = ½ derived) and a growing set of proved structural facts and negatives.
5. **The trend is real, but it runs in a different direction from "closer numbers".** May had many sub-1 % matches; most were later reclassified as fits. Since August the corpus has gained hard structure: convention D forced, exact closed forms, Lean bounds and exclusions. The numbers got worse because they became honest. That is progress toward a derivation, but not yet progress toward the spectrum.

**On "not proved today says nothing about tomorrow":** agreed. Nothing here is a structural exclusion of the program. The Lean negatives exclude *specific classes* (e.g. "no operator commuting with U_q(sl₂) splits p from n beyond the pivot q²"). They also say exactly what new object would be needed, which is useful.

---

## 2. Masses

Errors use the live dashboard (one-term proton pin, q₀ = 1.10997858275…).

| quantity | status | model vs data | free inputs | source |
|---|---|---|---|---|
| m_e | CAL-1 | defines the MeV unit | 1 (calibration) | dashboard |
| m_p / m_e | CAL-2 anchor | 0.003 ppb (round trip: q₀ is solved from it) | 1 (calibration) | `2026-08-22-mp-fbor-massformula-redteam.md` §1 |
| **m_μ / m_e** (cross-check against m_p) | **D\|sel** | **+211 ppb** (9.5σ) | q₀ + Borromean word + /q³ + integers 2, 12 | dashboard; `2026-11-21-proton-minus-twelve-origin.md` |
| m_μ with two-term QED proton term | F (comparison only) | +8 ppb | adds a selected pair-omission | `2026-11-20-two-term-proton-q0-repin.md` (reverted; costs α_em 495σ) |
| m_n | D\|sel | −486 ppm (939.109 vs 939.565 MeV) | as m_p, plus Q_β | dashboard |
| Q_β (n → p e ν̄) | D\|sel | 0.3254 vs 0.7823 MeV, **−58 %**; Lean: ≤ 0.383 MeV for every q ≥ 1 | 2 cal + scored word V³ + cell identification | `2026-11-21-qbeta-np-error-budget.md` |
| m_n − m_p | D\|sel | 0.836 vs 1.293 MeV, **−35 %** | same cell as Q_β (one error seen three ways) | same |
| n–p cell 2E₀·ln q | D\|cal, unassigned | 0.8735 MeV; owner ruled it is not yet assigned to Q_β or Δm | 2 cal | owner-rulings 2026-11-21 |
| per-quark split (m_d − m_u) | **N** for the derived class; ansatz is F | the ansatz h²ℏ_q/√q matched CODATA by construction | — | `2026-11-21-per-quark-flavor-split-not-derived.md` (`PivotSplitOrder.lean`) |
| quark masses (u, d, s, c…) | O / N | charm-tower and Frobenius-block routes negative | — | `2026-08-02-charm-mass-*` |
| ²H binding (B_can⁰) | D\|cal (word conjectural) | 2.33 vs 2.22 MeV, about +5 % | 2 cal | `2026-08-29-mass-provenance-breakdown-and-gap-map.md` §3 |
| ²H…⁴He binding (production B_sym) | **posited** form | ratio B_AME/B: 0.79, 1.38, 1.44, **3.26** | 2 cal + posited α ln(·) map | same |
| ⁴He binding, magic-A 2m_e·A·8G | F (census selection) | +5.87 % | knot chosen to match | cheat sheet §9.3 |
| fusion Q-values (D+T) | consequence | wrong sign (−0.3 vs +17.6 MeV) until ⁴He closes | — | provenance map §4 |
| m_K / m_π | **F** | +51 ppb | (3,4) pair scan-selected; EM factor form selected | `2026-11-20-mk-mpi-derivation-status.md` |
| g_A | **F** | +0.1 % | best of three colour averages | `2026-11-15-standard-model-eightfold-way-corpus-map.md` §7 |
| W, Z, H masses (T(2,4), T(2,6), T(2,8)) | C | ratios within 1–3 % (May) | knot assignment conjectural | cheat sheet §5 |
| EW vev fixed point | C, four slots underived | none of tree prefactor, loop sign, loop coupling, zero-mode rule derived | — | `2026-11-20-ew-vev-gaps.md` |

## 3. Couplings

| quantity | status | model vs data | free inputs | source |
|---|---|---|---|---|
| α_em⁻¹ bare q[9]_q[10]_q | **D\|cal** (the (9,10) pair is Diophantine-forced; one unverified linchpin) | 136.823, **−0.155 %** | 1 (q₀) | `2026-08-22-alpha-em-deriva*.md` |
| **α_em⁻¹ form B (Schwinger)** | **D\|cal + one underived factor** | **−0.37 ppb (2.4σ)**; best non-anchor row on the dashboard (238× from the 100× target, vs 970× for m_μ) | q₀ (from m_p) only; 8/(12π) = b₁/Area of Bring's surface is structural (proved template); Schwinger factor c = 1 not fitted but not derived (exact check gave c ≈ 0.73); canonical functional undecided (bean `qou-aemx`) | `alpha_em_schwinger_ladder_probe.py`; `2026-11-20-alpha-em-two-term-q0-pull.md` |
| α_em⁻¹ CS tower | C | −468 ppb | conditional on an open κ (Gram `sorry`) | same |
| α_em⁻¹ 45·[3]_q form | F, ruled out | 2.6 ppb | PSLQ single-point fit | `2026-06-10-alpha-em-legacy-empirical-forms.md` |
| sin²θ_W | F | 0.127 % | best of 74 enumerated candidates | corpus map §1 |
| g = π·h₀, v ratio = log 6 | F/C | ±0.5 % | empirical-match hypotheses (May) | cheat sheet §5 |
| strong coupling, Yukawas, CKM, PMNS | O | — | — | `sm-params-ckm.md` |

Note on α_em (corrected after review): q₀ is pinned by m_p, so α_em is a genuine prediction, not a round trip. The bare backbone is 0.155 % off with no knob at all. Adding the Bring zero-mode term b₁/Area and the Schwinger self-energy brings it to −0.37 ppb, with no coefficient fitted. Read as a determination of q₀, α_em lands **0.053 ppb** from the proton pin and 11.6 ppb from the muon pin. So α_em and m_p agree on q₀ to 2.4σ of α's error bar: **two independent observables, one parameter.** That is the most striking result in the scorecard. The caveats: c = 1 is not derived, the CS tower gives a different answer (−468 ppb) and the canonical choice is open, and the sign of the residual flipped between CODATA 2018 and 2022.

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
| Coleman–Glashow Σ = N + Ξ | **D (new, 2026-11-21)** | exact in q for the isospin/charge Murphy sum; hypercharge Murphy sum provably gives zero splitting |
| sign of the octet isospin coefficient α₂/α₁ | N for this operator (scope a) | +0.056 at q₀ vs lattice −0.141: right structure, wrong sign, 0.4× size |
| strange strand and n − p | **N (Lean)** | an s strand cannot change the n–p direction result |
| octet mass degeneracy m_Λ = m_Σ⁰ | N | weight-only mass forces the degeneracy |
| nonet mixing angle | proved unconstrained | — |

Ledger count (eightfold chapter, 2026-08-08): 1 derived, 3 proved, 8 standard, 2 refuted, 9 open of 23 rows. SM appendix: of 26 SM parameters, 1 input, 1 proxy, 1 partial, 2 conjectural, 21 open. The 2026-11-15 map and today's Murphy-octet work add structure (Coleman–Glashow exact, several Lean negatives) but no new derived SM parameter.

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
| α_em | 2.6 ppb (PSLQ fit) | **−0.37 ppb form B, no fitted coefficient**; 0.155 % bare | PSLQ form ruled out (2026-06-10); form B built from structural pieces (Jul–Nov) |
| EW ratios | 0.35–1 % (W/Z, g, v) | still conjectural | never derived |
| generations | "3" | 4 / 3 / 2 / 3 unresolved | counting criteria disagree |

### Reading the trend fairly

- **Precise results with no fitted coefficient:** essentially none in May (each later turned out to carry a fit). Now α_em form B at −0.37 ppb, with one underived factor (c = 1), and it agrees with the proton on q₀. This is the clearest real gain of the six months. The μ–p consistency is also precise but carries more selected joints.
- **Proved structure:** grew sharply from August. Convention D is forced, the Borromean trace has an exact Lean closed form, N = 2 Schur–Weyl is proved, Coleman–Glashow is exact, and Q_β is now one rational function of q times m_e. These are permanent results that any future mass formula has to respect.
- **Proved negatives:** about a dozen this month alone. They localise the gaps sharply. For n − p, the corpus now knows that a symmetry-breaking object beyond U_q(sl₂)-commuting operators is required, and that Q_β's missing factor (about 2.04 of the 2.40) must come from a link that survives at q = 1.
- **Discipline:** the 2026-09-05 no-fit rule, the 2026-08-11 excision and today's "derive, not assert" ruling mean every remaining number is honestly labelled. That is why the scorecard looks worse than in May. It is also why a future match will count.

---

## 6. The test that would change this assessment

A single trace-to-energy map, fixed once and pre-registered, that predicts a **second** observable it was not tuned on. The best candidates, in order of leverage:

1. **Derive the −12** (or the /q³) from the two-term Lagrangian or the electron word. That would turn the 211 ppb μ–p cross-check from D|sel into D|cal, which would be a strong result.
2. **Find the q = 1 factor in Q_β** (about 2.04). The Lean bound says no q-correction can supply it, so it must come from the counting 3/8, the factor 2, or the identification of the cell with Q_β (the β-decay GB reduction now in progress, PR #8904).
3. **Derive the Schwinger factor c = 1** and name form B canonical. α_em would then be a fully derived, ppb-level prediction that agrees with the proton on q₀, which is the clearest possible "second observable" test.

---

## 7. Next steps (pick by number)

1. ~~Turn this scorecard into a repo doc~~ Done: this file, issue #8956 (owner chose 1 and 4).
2. Open a thread on the −12: try the two-term Lagrangian and electron-word routes from `ProtonTwelveOrigin.lean` §C3–C4 to derive it, or prove it underivable.
3. Pre-register a "one map, two observables" test: fix the trace-to-energy map on Q_β's GB reduction, then predict Δm or ²H with no new choice.
4. ~~Bring the α_em canonical-functional decision (bean `qou-aemx`) to you~~ Posted as a decision card 2026-11-21.
5. Add a dated "status" column to `sm-params-intro.md` so the 26-parameter count is tracked over time automatically.
