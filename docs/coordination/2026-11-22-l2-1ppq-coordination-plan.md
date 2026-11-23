# L2 1-ppQ programme: optimistic overview, canonical-chain gap list, work plan

Date: 2026-11-22. Main at `46c74c318` (#9144 merged). Coordinating thread: "Coordinate the L2 1-ppQ derivation plan".
Epics: `qou-10v9` (programme root, L2 at 1 ppQ), `qou-8lxd` (eightfold way / SM), `qou-rgj8` (eightfold-way formalisation gaps).

Register. Everything upstream of a comparison is mathematics. The comparison lines (marked **cmp**) are where a model number meets a measured one; they stay out of Lean. No number below was fitted. Accuracy is a diagnostic, not a ranking.

---

## Part 1. Optimistic-case overview

"Optimistic" means: the open sibling PRs land as described (#9123 colour/p–n readout, #9126 photon-pair cells, #9130 skew Howe slice, #9105 precision reds, plus the Lean follow-ups the threads are on), and nothing they prove is later retracted. It does **not** assume any open derivation closes.

### 1.1 Proton–neutron mass difference

What is settled (proved, sorry-free unless marked):

| result | tier | where |
|---|---|---|
| m_p = m_n at q = 1 for every braid-built functional, all n | Lean | `FlipSymmetryAtOne`, `FlipSymmetryAtOneBridge`, `QOneFlipSymmetry` |
| closure mass 2^components at q = 1; Borromean amphichiral ⇒ closure mass gives no split at any q | Lean | `CategoricalMassAtOne` |
| no increasing map of the sector trace makes the neutron heavier (structural exclusion) | Lean | `NeutronHeavierSign` |
| pp = nn at generic q for within-nucleon braids (q-Casimir, KZ monodromy, and under the colour mirror b ↦ −b⁻¹) | Q(q) computer algebra at n = 6; Lean for the full-twist core in progress (#9123 thread) | audit `2026-11-22-coulomb-all-q-and-nucleon-writhe.md`; #9123 §30–31 |
| a U(1)_em phase on strands is obstructed (no U(1) grading of H₃(q)); charge lines sit on hadrons | Lean (`no_scaling_of_hecke`); #9123 | ruling 2026-11-21/22 |
| block-level charge lines give κ·Q_A·Q_B | Lean; t not tied to α_EM | #9123 thread |
| no pair term between two nucleon blocks is Coulomb; α + β = 1 identity in Q(q), and its strand-flip-plus-reversal symmetry | Lean (structural parts) + Q(q) at n = 6 | `PairTermSectorSymmetry`, `WeylSymmetricPairNotCoulomb`, `HeckeSeriesCollapse`, #9103/#9125 |
| neutral exchange = e²QQ′ + Z term; Coulomb needs sin²θ_W and a Z scale | Lean | `neutralExchange_split` |
| nucleon writhe is 0 for p and n; charge is not writhe | Lean | `charge_not_writhe_on_nucleons` |
| charge-squared terms make the neutron *lighter*; SM charges break the q = 1 equality (q_u² ≠ q_d²) | Lean | `delta_charge_quadratic`, `sm_charges_not_mirror` |
| Q = I₃ + c forces c = 1/6 from any one neutrality condition; slope and Y not derived | Lean | `QuarkChargeReduction` |
| colour (strand states, b = −qX) moves no production number | Lean | #9107 (merged) |
| cross-nucleon braids break pp = nn, but not in Coulomb shape; sign unsettled | probe (§35) | #9123 thread |

Where the p–n number stands (**cmp**, CODATA m_n − m_p = 1.29333 MeV):

- Strong/flavour sector is entirely O(h) (vanishes at q = 1): 𝒟² arm on the muon scale +0.171 MeV (13 %); vertex splits 0.09–0.20 MeV.
- EM/charge sector is the only part that survives at q = 1: bare α·S on the electron map −0.358 keV (= −m_e/720 at q = 1); α·S on the mass facade −2.30 MeV (2.3× the lattice EM part, and it breaks q = 1 equality through a decoration).
- The derived n–p cell 2E₀·ln q = 0.8735 MeV is not assigned to any observable (ruling 2026-11-21) and stays below 2m_e at every q > 1, so it cannot be m_n − m_p.
- For orientation, lattice QCD+QED splits the physical value as about +2.52 MeV (quark masses) and −1.00 MeV (EM).

**Optimistic reading.** The sibling work, if it lands, makes the *shape* of the split clean and proved: p and n are exactly degenerate on everything braid-built and within-nucleon, at every q; colour does not move it; charge lives on hadron lines, not strands; and the EM sector reduces to one Coulomb coupling κ·Q_A·Q_B whose normalisation t is tied (conditionally) to α_EM. That gives a sharp statement of what m_n − m_p *must* come from: (i) a cross-nucleon or flavour O(h) term with a sign that makes the neutron heavier, and (ii) one EM term proportional to α with a derived coefficient. Neither magnitude is in hand: today's best parts are +0.17 MeV and −2.30 MeV, each a factor of roughly 2 to 15 from what is needed. The headline result available now is structural, not numerical.

What the EM/charge sector carries: the only q = 1 survivor; the sign (neutron lighter from any charge-squared term); and, through Q_A Q_B on hadron lines, the Coulomb energy of nuclei. What it does not carry: any strand-level phase, any Coulomb pair term from Hecke insertions between blocks, or sin²θ_W / the Z scale (needed to separate Coulomb from the Z term).

### 1.2 Impact on the mass computation

- m_p/m_e = 2(Vol(4₁)/ℏ_q²)·F_Bor − 12 is an **anchor round trip**: q₀ is solved from m_p, and F_Bor's /q³ normaliser is asserted (k = 0 moves m_p by +37 %). The honest m_p test is the muon pin (−244 ppb).
- The p–n results above do not move m_p: every within-nucleon functional is isospin-blind, so m_n − m_p has to be an additive term outside the proton identity. Under the optimistic case this is a clean separation: m_N (isospin-blind, from F_Bor) plus Δ_pn (EM + cross-nucleon). It also means the convention-D proton identity cannot be "split" to give the neutron; that route is closed (PR #8804).
- Colour (#9107, #9130) changes no number on the baryon sector.
- The scale map 𝔈 → MeV (bean `qou-91w7`) moves every MeV figure in this document. It is the single largest lever on all comparisons.

### 1.3 Impact on β-decay

- Q_β (**cmp** 0.78233 MeV): ruled cell (T³ weight split from γγ) 0.32543 MeV, −58.4 %. Lean `QBetaErrorBudget`: Q_β = m_e·R(q) with R ≤ 3/4 for q ≥ 1, so this cell can never exceed 0.383 MeV; a factor 2.04 must come from a term that survives at q = 1, which the O(h) sector cannot supply (≤ 1.178). `BetaVertexBudget`: under placement B the vertex must supply ≥ 0.420 MeV.
- So the p–n finding and the Q_β finding are the same finding: the missing piece in both survives at q = 1, and the only q = 1 survivor found so far is the EM/charge sector. That is the strongest cross-front hint in the corpus right now, and it is a hint, not a derivation.
- Q_β = (m_n − m_p) − m_e kinematically; if the derived n–p cell is later assigned (GB reduction decides), both observables move together.
- Half-life: the two-term weak-vertex form factor 𝒲 = t₁ + c_em·t₂ is in Lean (`WeakVertexTwoTerm`), but there is **no numerical half-life** yet: c_em, the strand charges, the projection and the rate unit μ₀ are underived. Sensitivity ∂lnΓ/∂lnq ≈ 48. Optimistic case: with c_em (from the t ↔ α_EM link) and μ₀ from CAL-1/2/3 it becomes a parameter-free prediction; nothing tuned enters.
- ³H Q_β comes out ≈ 325 keV against 18.59 keV, and ≈ −523 keV with E_C added: the light-nucleus β sector inherits the nucleon miss.

### 1.4 Impact on binding (A = 2, 3, 4)

| nucleus | γγ chain B (keV) | all-pairs (keV) | **cmp** AME (keV) |
|---|---|---|---|
| ²H | −0.77 / −2.58 | — | +2224.6 |
| ³H | −0.73 to −1.00 | −1.1 to −1.7 | +8481.8 |
| ³He | −1.33 to −1.68 | −1.8 to −2.6 | +7718.0 |
| ⁴He | −0.862 | ≈ −1.6 | +28 296 |

- Proved: every γγ production chain unbinds for all A ≥ 2, every order, every q > 1 (`LightNucleiGGChainSign`). Bond tails at A = 2 start at h⁴ (into p) and h⁵ (into n) for any z.
- #9144 (merged): why h¹–h³ of a bond vanish; at A = 3 exact locality (48/48) and an exact product rule except two bonds into one nucleon, where the deviation starts at (1 − z²)h⁶. So log-binding is additive over bonds to that order. Lean for the h² cycle-count lemma is in progress; the A = 4 product run was skipped by the user's choice.
- EM impact: the hadron-line Coulomb κ·Q_AQ_B is the natural E_C carrier (³He–³H difference, ⁴He). With t tied to α_EM it becomes a derived Coulomb term; until then any E_C is imported.
- Optimistic reading: the structure (additive bonds, exact locality, Coulomb on hadron lines) becomes proved; the magnitude and sign do not. The trace alone is 10³–3·10⁴ too small and of the wrong sign; binding has to come from outside the single-γγ chain (many-body vertices, other blocks, or the energy map).

### 1.5 One-line scorecard (optimistic case)

| observable | today | after open PRs land | blocking derivation |
|---|---|---|---|
| m_p/m_e | round trip (proton pin); −244 ppb muon pin | unchanged | /q³, k = 2, muon carrier, 𝔈 → MeV |
| m_n − m_p | +0.17 / −2.30 MeV parts | structure proved; no number | Y and Q slope; c_em; cross-nucleon sign |
| Q_β | 0.325 MeV (−58 %) | unchanged; bound ≤ 0.383 proved | GB reduction of β; q = 1 survivor term |
| τ_n | no number | no number | c_em, μ₀ |
| B(A = 2–4) | keV-scale, unbound | structure proved (A = 3) | many-body / energy map |
| α_EM | two labelled arms (ppb) | conditional t ↔ α_EM | does the correction vanish at q → 1 |

---

## Part 2. Gap list for the canonical mass derivation

Paths are under `folio/quantum-observable-universe/lean/QOU/` unless stated. The cheat-sheet §0 and the 2026-09-08 audit §2 are out of date at steps 3–6; corrections are flagged ⚠.

### Step 1. Categorical Lagrangian → two-term trace
- **Proved:** `CategoricalLagrangian` structure; `CategoricalLagrangianTwoTermBridge` (`dirac_sq_three_term_expansion`, `lagrangian_five_term_expansion`, `trace_lagrangian_two_term_split`, pure algebra); `NormalisedLagrangian.matter_trace_eq_eigenvalue`; QED covariance negatives (`QEDHigherOrderCovariance`, `NucleonQEDCovariance`).
- **Conditional:** `Torsion/MassTraceIdentity` takes frobeniusForm = counit as a hypothesis; concrete trace results need `hReebP`, `hReebN`, `hMatReeb*`; `nablaEndo` has no instance.
- **Ruled, not derived:** two-term t₁ + c_em·t₂ on the scoreboard; normalised states (trial); degree-0 term is a potential; Coulomb enters as −α·S; α = q⁻¹/([9][10]) with [10]_q asserted (`qou-15sj`).
- **Left to prove:** instantiate ∇ from the substrate; discharge the Reeb hypotheses and ∫ = ε; derive c_em; land #8743 (lepton two-term from Lagrangian + Stokes; not on main) or a successor.

### Step 2. Non-abelian Stokes → braid monodromy → Hecke quadratic
- **Proved:** KZ side sorry-free (`Mass/KZHolonomy/*`, `kzBraidRep_sigma_isHeckeQuad`, `MultiStrandHeckeFactor`, `KohnoAssembly.kz_conj_jimbo_complex`, `KohnoWeighted.braidTrace_eq_kz`, `KohnoWeightedClass.massClass_kz`); descent to braid classes (`Torsion/MassTraceMarkovClass`); `HeckeMonodromy` consequences given an instance; q = 1 shadow from the colour cubic.
- **Cited:** Drinfeld–Kohno (Kohno 1987) at real q₀ via imaginary level; Riemann–Hilbert/Deligne; Yekutieli; Markov's theorem.
- **Conditional / carriers:** `HeckeMonodromy` has only the rank-one toy instance `laurentModel`; `KZPullbackGenerators` no instance; `NonAbelianStokes`, `LieValuedStokes`, `YekutieliFiniteSliceMultTrace` are class carriers; no continuous multiplicative integral in Lean (hence `conj:topological-mass-dilogarithm` demoted).
- ⚠ **Circularity:** `BridgeADeligneKZ.lagrangian_gauge_to_KZ` assumes `hL` (the Lagrangian monodromy *is* the Jimbo braiding), which is the step's conclusion. `LagrangianKZIdentification` postulates P1–P3.
- ⚠ **New:** with Hopf colour (#9107) the strand braid satisfies a cubic; the Hecke quadratic holds only on colour singlets (b = −qX). Bridge A must be restated for that.
- **Left to prove:** the n-body connection from 𝒟_∇ (P1–P3); its monodromy = Jimbo braiding without `hL`; `FundamentalSolution` + Deligne full faithfulness; a substrate instance of `HeckeMonodromy`; owner goal `qou-ywyq` (trace = multiplicative integral).

### Step 3. Markov trace, convention D
- ⚠ **Both cited axioms are gone**: `markov_trace_unique_axiom` was proved false (`markov_trace_unique_axiom_false`) and removed; `jones_markov_trace_exists` proved false on unconstrained data and removed.
- **Proved:** `markov_trace_unique` (given cross-level M3); `ocneanuMarkovTrace` instance at z_D for all n; `eq_wtrace_of_markov`; `tr_borromean` for any Markov family; convention D = Jimbo/sl₂ trace.
- **Legacy axioms still present** in parallel APIs: `HeckeAlgebra/MarkovTrace.MarkovTrace_markov_axiom`, `HeckeAlgebra/Formal.heckeFormalGenerator_T_relation`, and `axiom MarkovTrace` in `climax-volume-mass/vertex-algebra-relations.lean`. N = 2 fibre dimension is an input.
- **Left to prove:** unify the three Hecke models (`QOU.Hecke.IwahoriHecke`, `SchurWeyl.Hecke`, `Hecke/MarkovTrace`); delete the legacy axioms.

### Step 4. Partitions (Wedderburn, Jucys–Murphy, Reeb Laplacian)
- **Proved:** `heckeWedderburnF` (any characteristic, q not a root of unity); `seminormalRep_qJM`; JM projectors; content Casimir central; `HeckeReebHolonomyLaplacian` (relative full twist = Murphy element, eigenvalue Σ(q − q⁻¹)²[c][c+1]); `HeckePresentationBridge`; RSK Wedderburn.
- **Redundant axioms:** `Hoefsmit` (×2), `IwahoriHeckeAPI` (×3 central idempotents), convention-C `class WedderburnDecomp`.
- **Open:** "H_k is the Reeb-loop holonomy" needs Bridge A P1; the per-partition weight Δ_λ for binding is not derived.
- **Left to prove:** Bridge A (as step 2); derive Δ_λ; port consumers off the axiomatised APIs.

### Step 5. Frobenius pairings, Schur elements, T_β
- **Proved:** `KnotFactorFrobeniusPairing.ofHecke` (κ = Σ y_λ s_λ e_λ, any trace); [3]_q!/q³ is the sign Schur element, uniqueness of the three Schur elements; `markov_frobenius_min_norm_twisted` (+ uniqueness).
- **Conditional:** T_β collapse needs `TwistedPSDTrace` / `TwistedNonDegTrace`, no Hecke instance (positivity via the orthogonal seminormal form is prose only; `qou-baov`, #9032); `ofHecke` takes the Wedderburn equivalence as an argument and the Ocneanu trace is not yet a functional on `QOU.Hecke.IwahoriHecke`; binding half of `conj:knot-factor-frobenius-pairing` is a definition; `frobeniusForm_unique_axiom` remains.
- ⚠ The cheat sheet's "Ψ = S² = id ✅" is wrong for the q-deformed case: `antipode_sq_of_comm` is commutative-only.
- **Left to prove:** a `TwistedPSDTrace` instance for tr_M at z_D (y_λ ≥ 0 for q > 1, † anti-involution); Ocneanu trace into `ofHecke`; remove the Frobenius-form axiom.

### Step 6. The mass number
- **Proved:** `borromean_markov_trace_closed_form`; `BorromeanWordForcing` (`minimal_pure_zeroLinking`, `borromean_minimises_energy`); `ProtonWeightSpaceDim` (the 3 in 12 = k²·3); negatives in `ProtonTwelveOrigin`.
- **Ruled / chosen:** β_Bor by owner-sanctioned energy minimisation and linking neutrality (inputs "three strands", "pure zero-linking" chosen); /q³ asserted, k = −3 not selected by any route; k = 2 not found; the 2 and 12 are class fields of `ProtonBorromeanAssembly` (no instance; docstring cites the refuted "Ocneanu −1/12"); `conj:proton-mass-substrate-identity` fitted in the normaliser; muon carrier m_μ = m_e·Vol(4₁)/ℏ_q² asserted (`cal2_identity_pinned` circular; `qou-6gf9`); 𝔈 → MeV open (`qou-91w7`).
- ⚠ **False axiom on disk:** `knots-particles-confinement/categorical-proton.lean: axiom proton_mass_from_substrate_axiom : |proton_mass q₀ − 938.272| < 1` (left side evaluates to 746.40; also an empirical number in a formal statement). Outside the lake build. Delete or replace by a comparison remark.
- **Left to prove:** derive /q³ (or replace F_Bor by a derived observable), k = 2, the muon carrier, the energy scale; derive β_Bor without the owner rule.

### Highest-leverage proof obligations (ranked)
1. **Bridge A without `hL`** (steps 2, 4): connection from 𝒟_∇, monodromy = Jimbo braiding, FundamentalSolution, `HeckeMonodromy` substrate instance, reconciled with the colour cubic.
2. **Trace → energy scale** (step 6, every comparison): 𝔈 → MeV from CAL-1/2/3, the muon carrier.
3. **Proton normaliser** (step 6): derive k = −3 and k = 2, or replace F_Bor.
4. **Two-term trace from the Lagrangian** (step 1): ∇ instance, Reeb hypotheses, c_em; feeds τ_n and the EM sector of p–n.
5. **Hecke positivity and unification** (steps 3, 5): `TwistedPSDTrace` instance, one Hecke model, delete legacy and false axioms.

---

## Part 3. Cohesive work plan

Workstreams, each with an owner thread. "New" means I ask the project coordinator to start a thread.

| WS | goal | owner | next concrete step | depends on |
|---|---|---|---|---|
| W1 EM sector | tie the hadron-line coupling t to α_EM; settle cross-nucleon sign | thread "Settle the neutron-heavier sign" (#9123) | Lean full-twist pp = nn; conditional t ↔ α_EM; α_EM sorry | W6 |
| W2 Coulomb/hypercharge | derive Y and the slope of Q = I₃ + Y/2; sin²θ_W as a trace ratio; 7–8 strands for all q | thread "Tighten Coulomb and hypercharge corpus blocks" (#9125 merged) | Lean for the two n = 6 identities; more strands | — |
| W3 Colour | skew Howe beyond the singlet slice; Bridge A restated for the colour cubic | thread "Adopt strand colour states" (#9130) | land #9130; full skew Howe at n = 3 | — |
| W4 Binding A ≤ 4 | Lean h² lemma; A = 4 product rule later; many-body vertex search | thread "Compute A = 2 and A = 3 binding energies" | h² cycle-count lemma in Lean | W6 |
| W5 Photon pair / β GB reduction | finish the 6-strand pair cells (#9126); then the β-decay Gröbner–Shirshov reduction (unreduced vs reduced word) | thread "Photon norm 1" (#9126) | land #9126; then GB reduction, which also assigns the 2E₀ ln q cell | — |
| W6 Energy scale (new) | derive 𝔈 → MeV from CAL-1/2/3 and the muon carrier (`qou-91w7`, `qou-6gf9`) | **new thread** | formalize the scale map as a Lean class; state what CAL-1/2/3 can and cannot fix | — |
| W7 Bridge A (new) | non-circular Stokes → Hecke; substrate `HeckeMonodromy` instance | **new thread** (or the wave-2 Hecke/Schur–Weyl drain) | remove `hL`: state the 𝒟_∇ connection and prove its local monodromy | W3 |
| W8 Hecke hygiene (new, small) | one Hecke model; `TwistedPSDTrace` instance; delete legacy axioms and the false proton axiom | **new thread** or the wave-2 Hecke/Schur–Weyl drain | delete `proton_mass_from_substrate_axiom` (owner card first: changes a file) | — |
| W9 Precision | keep the gates green | thread "Fix red precision gates on main" (#9105) | land #9105 | — |
| W10 Proton normaliser | k = −3 and k = 2, or a derived replacement for F_Bor | parked (Round 4 negative); reopen only with a new idea | — | W6 |

Order of attack: W5 and W1 first (they decide what the derived n–p cell and the q = 1 survivor are); W6 next (moves every number); W7 and W8 in parallel as math infrastructure; W4 continues; W10 waits.

Coordination rules for every workstream: formalize first; no measured value inside Lean; no selection against the target; each result recorded in its audit and on its bean; this thread re-reads the sibling PRs daily and updates this plan and the epics.

---

## Part 4. Applicability review of the epics (2026-11-22)

Read openings and closings of every open child of `qou-10v9` (85) and of the `8f-mass`, `8f-ew`, `8f-colour`, `8f-flavour` children of `qou-8lxd` (44); the longest bodies were skimmed in the middle. Codes: L live, S superseded, D done elsewhere, SC stale claim, NO needs owner.

Three facts drive most verdicts:
1. About 30 in-progress beans are "in progress" only because of a "Round N" batch PR (#8139–8144, 8153, 8160, 8164, 8171, 8179, 8185, 8193, 8198, 8202, 8207, 8213, 8222, 8229, 8231, 8238, 8393, 8395, 8401) opened 11-16..18 and untouched since; several cited PRs are closed unmerged (#8145, 8187, 8244, 8322, 8342), and several claimed Lean files are not on main.
2. The 2026-11-15 γγ re-scope: every number on the single-crossing interface letters of `atom_braid_word_3A` describes a superseded word (deuteron offsets, μ_e, chain law, b₃ magnitudes). Lean for generic bond weights survives.
3. The 11-21/22 rulings: colour weighting R3 relaxed; strand colour with b = −qX; "nucleon energy = sum of crossing traces" dropped; Q_β from the γγ GB reduction, not a trace ladder.

**qou-10v9**
- L: e58e, 4waf, 4e5k, gpb5, 3e6w (maths only, low), 0pnj, 9bei, vvv4, 742w, dqgp, rz0g, xy5f, 9w1u, y7ek
- S: avtq, vtlj, cblw, fv0s, tqfm, dx1t, 4q9h, 19jc, 5d6k, vbyi, ughq, i4pz, 17mq, gcmn, dgpz, w5tg, ftas, jqhk (virtual loops), 4tqt
- D: 0gbx (→ qou-agc6), d5e8, 2pnv, 08xc, lq6k, pbwj, j1e5, cdh4
- SC (reset to todo; still live unless noted): efqx, itdn, vudb, 0c19, 7zob, 6he8, kok7, 768r, o6ov, eptr, 85wn, lzoh, t6hc, 8zjc, niah, 58r5, 59x9, 018h, 4qno, 7jok, k4f8, 1a69, ec5z, ckyw, xajh, adwi, o43i, 6nd0, 4cu3, 3l2l, 2002, 9nnz, l2vh, ijoi, wp3h, zrbv
- NO: 99qc (retitle/split as the Q_β γγ hub), wxhi (retire the c_k ladder or keep as maths), cdx1 (retitle or close: C excised, R3 relaxed), v2om and 8ffl (re-scope under γγ / derived order / ⊗_# reconcile), e5jf (deuteron frame), 5ruq (is atomic electron binding in scope without virtual exchange)

**qou-8lxd (8f-mass/ew/colour/flavour)**
- L: ni4b, 5iaz, 8pl1, uq5x, z03j, 20sx, d7h1, 8pl3, n6ls, wyy9, 10zv, 29s2, ak28, se9w, lyp3, ha6c, b1k4, pgzo, qydm, usft
- S: 17gn, 8p1x, 8p1e, 8p1c, 8p1h, ys29 (backup colour routes), htk4, lsp9, js8z, pvu4 (T(2,n) lepton tower is backup only)
- D: vhv6, hjs8, jogb
- SC: tqcp, swqq, 3oi0, 8pl2, 9l0d, 37y0, qneo
- NO: v5fp (gluon open by ruling), lxh5, ozyt (title asserts a false statement), yw3v (conflicts with up quark = unknot and derived charges)

Most relevant children per front:
- p–n: 99qc, itdn, 4waf, vudb, 0gbx→agc6; 8lxd: 37y0, ha6c
- β-decay: 99qc (hub), e58e, itdn, 7jok, zrbv (GB normal-form pipeline)
- binding: v2om, 8ffl, 85wn, 0c19, eptr, 7zob, e5jf, gpb5, lzoh
- canonical chain: gpb5, wp3h (Yekutieli multiplicative integral), o6ov, 018h, k4f8, 8zjc, 3e6w, t6hc, zrbv

## Part 5. What I changed and what waits on the owner

Done in this pass (beans only, no content or Lean): a dated status block appended to `qou-10v9`, `qou-8lxd`, `qou-rgj8`; the SC beans above reset from in-progress to todo with a note (standing stalled-claim policy; nothing judged). Not done without the owner: closing the D beans, scrapping the S beans, the NO decisions, deleting the false proton axiom.

Owner card 2026-11-22 21:56Z, option "PR plan + 3 new threads": this plan goes into `docs/coordination/` by PR, and threads for W6 (energy scale), W7 (non-circular Bridge A) and W8 (Hecke axioms and positivity) are requested from the project coordinator.

## Updates

- 2026-11-22 21:55Z — #9130 merged (61847e5f3). Gives the algebraic half of the singlet hook for Bridge A: on colour singlets X = −q⁻¹·b, so b = −qX satisfies the Hecke quadratic (`prop:colour-singlet-flavour-generator`); `ColourFlavourMirror.singlet_exterior_iff`; `ColourRelabel.braid_commuting_fixes_singlet`. Not proved: KZ/Stokes monodromy restricted to singlets equals b (nearest: `conj:colour-tube-monodromy-braided`, bean `qou-et5f`, Drinfeld–Kohno cited). W7 should restate Bridge A with that step as an explicit assumption, targeting the Lean singlet lemmas.
- 2026-11-22 21:57Z — New threads started: W6 "Derive the energy scale to MeV" (cmsg_01H9cBvdoT3vcjHkS7QAyTqgDchk7WGqQtLjhtZMvn1r6y), W7 "Make Stokes-to-Hecke non-circular" (cmsg_01H9cBvdoT3vcjHkS7QAyTqgDdtKBnFpPd9Qj4AhXNYbkZ), W8 "Clean up Hecke axioms and positivity" (cmsg_01H9cBvdoT3vcjHkS7QAyTqg4UuN3gFiqjM7qE2B4zzWQh).
- 2026-11-22 21:57Z — #9126 merged (b7a8606ee9a): all 1408 photon-pair cells decided (19 factorise, 1389 do not); colour cubic ≅ 50a1 by a linear map. W5 thread takes the β-decay GB reduction next (it has HeckeSectorRep and the pair machinery).
- 2026-11-22 22:06Z — W6 result (branch claude/energy-scale-cal-map-2026-11-22, 5438997b7; Lean QOU/Observations/EnergyScaleMap.lean, sorry-free; audit 2026-11-22-energy-scale-cal-map.md; PR awaiting owner card). (1) The only 𝔈 → MeV map CAL-1/2/3 allow is Φ(𝔈) = m_e·𝔈/𝔈_e at q₀; c_q² cancels in it. (2) The calibrations cannot fix the unit/weight split; the one open input is the electron's categorical weight 𝔈_e, and the trace pipeline (σ₀σ₁σ₀, finite at q = 1) and the mass formula (ℏ_q², order 2) use different 𝔈_e, so every E₀-scaled row in Part 1 depends on which is derived. (3) The muon carrier is CAL-2 itself, not a derivation: no pair of framed braid-word traces carries Vol/ℏ_q² (pole at q = 1), E₀/m_e = 1/(q(q−1)) is not a trace ratio, and Vol(4₁) needs an analytic input. Consequence for the plan: obligation 2 narrows to "derive 𝔈_e"; next probe 𝔈_e(q₀)/ℏ_q₀². Beans qou-91w7, qou-6gf9 updated.
- **2026-11-22 22:07Z, W1:** #9123 merged (merge commit 8c45a78; §32–§35, six sorry-free Lean files). Next in W1: KZ full-twist pp = nn at generic q (new PR, owner card pending), then audit §36, which answers whether κ·Q_A·Q_B can supply a q = 1 term for the missing ×2.04 in Q_β.
- **2026-11-22 22:13Z, W8** (branch claude/hecke-axioms-positivity-2026-11-22, no PR yet; sorry-free, lean-direct exit 0, standard axioms only):
  - Positivity at z_D (bean qou-baov): `QOU/SchurWeyl/WtraceTwistedPositivity.lean` proves 0 ≤ wtrace(X·X†) and wtrace(X†) = wtrace(X) for q > 1 over any ordered field. `markov_frobenius_min_norm_zD` gives S² ≤ tr_M(X·X†) when tr_M(X) = S.
  - Caveats. The trace is degenerate at z_D for n+1 ≥ 3, because the three-row weights vanish. So only the inequality half of the T_β collapse holds at z_D. Also, `TraceTwist` as stated is satisfied by a degenerate twist; the proposal is to require † to be anti-multiplicative (owner call).
  - Hecke models: `QOU/Hecke/HeckeModelsBridge.lean` gives equivalences between the IwahoriHecke, SchurWeyl.Hecke and HeckeSectorRep models, and a map into #9126's all-strands H(q). This closes plan obligation 4 (one Hecke model).
  - Legacy axioms: 8 have no consumers. `proton_mass_from_substrate_axiom` is false (its left side is 746.40). The deletion is on an owner card.
- **2026-11-22 22:19Z, W7** (branch claude/bridge-a-stokes-nbody-2026-11-22, commit 44c3767db, `QOU/Mass/BridgeAStokesNBody.lean`; sorry-free, standard axioms only; no PR yet, owner card pending; bean qou-x09k):
  - Under P1–P3, the n-body form with residues α + βP_ab equals `KZHolonomy.kzForm`, with κ = β/2 and c = −α/β.
  - Its generator monodromy is `kzBraidRep`. For V = ℂ² this is conjugate to Jimbo after a scalar, and it satisfies the Hecke quadratic.
  - `lagrangian_gauge_to_KZ_of_stokes` replaces the circular hL with a named assumption, `StokesToBraiding`. hL itself was too strong: the derived relation is conjugacy, not equality with Ř.
  - On colour singlets, under `ColourTubeBraided` (qou-et5f), X satisfies (X+1)(X−q⁻²) = 0.
  - **Plan obligation 1 narrows:** the circularity is gone. What remains open:
    - `StokesToBraiding` (a continuous multiplicative integral);
    - P1–P3 for n ≥ 4 (triple collisions);
    - a substrate instance of HeckeMonodromy (passed to W8).
- **2026-11-22 22:20Z, W7 ↔ W8 hand-off:**
  - At fixed β, a substrate HeckeMonodromy instance is only vacuous. `subsingleton_of_isUnit_h` forces the shadow target to be 0 over ℂ.
  - Next step for W7: a β-family version of `nbody_monodromy_hecke`, over ℂ[[β]] or a Laurent ring. W8 then builds the instance on that family plus `ocneanuMarkovTrace`.
- **2026-11-22 22:22Z, W7** (commit 2b13465d3; sorry-free). Laurent-family bridge:
  - `specialise β` evaluates at q = e^{iπβ}.
  - `specialise_strandBraid` and `nbody_monodromy_specialises`: one W per generic β conjugates the Jimbo-normalised n-body monodromy to the specialised `strandBraid` family over ℤ[q, q⁻¹].
  - `lagrangian_monodromy_specialises`: the same under StokesToBraiding.
  - Next: W8 to decide whether its HeckeMonodromy instance sits on this Laurent family.
- **2026-11-22 22:24Z, W4** (draft #9160):
  - `towerTr_shift_commutator` (the h² lemma) is sorry-free over any commutative ring, for all z and h.
  - The A = 4 product run is done:
    - locality 192/192;
    - product rule 736/736;
    - first deviation m(1−z²)h⁶, where m counts same-receiver bond pairs. This extends the A = 3 result (#9144).
  - E_C's expected carrier is κ·Q_A·Q_B, conditional on t ↔ α_EM. No empirical E_C is imported.
- **2026-11-23 00:32Z, W7: draft PR #9163 opened** (issue #9162, bean qou-x09k), carrying `BridgeAStokesNBody.lean`.
  - Named assumptions still open: `StokesToBraiding`, `ColourTubeBraided` (qou-et5f), P1–P3 for n ≥ 4, and Deligne full faithfulness.
  - The substrate HeckeMonodromy instance stays with W8.
- **2026-11-23 00:40Z, W8 draft PR #9166:**
  - **Hecke models:** proved to be one algebra (plan obligation 4 closed, pending merge).
  - **Positivity:** 0 ≤ tr_M(X·X†) at z_D for q > 1, with the instance proved. The form is degenerate, since rows ≥ 3 have weight 0.
  - **TraceTwist:** now requires † to be anti-multiplicative.
  - **Legacy axioms:** the eight owner-approved axioms are deleted, including the false `proton_mass_from_substrate_axiom`, which is replaced by proved bounds.
  - **Next:** the HeckeMonodromy instance on the Laurent family. This is unblocked by W7's 2b13465d3, and W8 has been told.
- **2026-11-23 00:47Z, W6 draft PR #9165 (issue #9164): two electron units in the corpus.**
  - The trace pipeline uses τ_e = tr(σ₀σ₁σ₀, Hopf closure). The mass formula uses ℏ_q².
  - Their ratio is R = τ_e/ℏ_q² = 70.4037232641 at the proton pin (70.4037110138 at the muon pin). R is neither c_q² nor E₀/m_e.
  - **Cross-cutting hazard:** any workstream that converts a trace-pipeline weight to MeV with the mass-formula unit, or the other way round, is off by about 70×. This touches W1 (Q_β, E_C), W4 (binding) and W5.
  - Which unit is canonical is open. CAL-1/2/3 cannot decide it, so it is an owner question.
- **2026-11-23 00:50Z, W1 unit check (PR #9161):** §35–§37 contain no MeV figures. Every value is a dimensionless trace ratio, and κ = 2 log t is dimensionless too. §36 now carries a units note naming τ_e, ℏ_q² and R ≈ 70.40.
- **2026-11-23 00:52Z, W8: a non-vacuous HeckeMonodromy instance** (branch claude/laurent-hecke-monodromy-2026-11-23, commits 2c64d0c20 and 8c2fc7450, stacked on #9166; no PR yet; owner card pending).
  - Files: `QOU/SchurWeyl/MarkovTraceDescent.lean` and `QOU/Mass/LaurentHeckeMonodromy.lean`. Standard axioms only.
  - The base ring is R = ℤ[q, q⁻¹, (q²+1)⁻¹]. The convention-D Ocneanu trace is proved to take values in R.
  - The instance sits on the Hecke colimit, with shadow ε : H_∞ → ℤ[1/2] sending each generator to 1. The shadow ring is nonzero.
  - Scope: this models the Step-2 conjecture. It does **not** show that the substrate connection's monodromy is this tower; that is still W7's `StokesToBraiding`.
- **2026-11-23 00:53Z, W5: draft PR #9168, β-decay Gröbner–Shirshov reduction.** Audit `docs/audits/2026-11-23-qbeta-gg-pair-gb-reduction.md`. The predictions were committed before any computation, and all of them held.
  - **Unreduced and reduced words are the same braid.** V0V1V2V0V3 and σ0²σ1⁻¹σ4⁻¹ are related by free cancellation and far commutation only. They are therefore equal in every braid representation, including H_n(q) at every q (sorry-free). So choosing between them chooses nothing.
  - **The 2E0·ln q cell is unassigned.** It goes to neither Q_β nor m_n − m_p. These words have no nucleon strand. The word that couples the pair to a nucleon is an owner input.
  - **The missing ×2.04 in Q_β cannot come from the reduced/unreduced choice.** This is a scope-(b) exclusion; the invariant is the braid identity. The search for a q = 1 term stays with W1 (§36) and W2.
  - **The only q-independent leftover is the cancellation count.** The shortest word has 4 letters, and any reduction cancels exactly 3 pairs.
  - **No MeV figures**, so the electron-unit split (R ≈ 70) does not apply.
