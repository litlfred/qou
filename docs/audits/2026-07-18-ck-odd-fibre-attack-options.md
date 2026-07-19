# c_k^odd from the categorical fibre — corpus + literature attack map (2026-07-18)

Scoping synthesis (corpus grep + external literature) for the "derive a
c_k^odd from the fibre without routing through S = Q_β/E₀" program. Three
independent research legs (route-3 substrate-q₀ scoping, route-2 corpus
scoping, external literature search). No wiring; no fit; this is a map.

## The two structural facts everything else hangs on

**1. The swing's *value* is proved measurement-limited.** Sorry-free
`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing` (scope-(b)): no
anchor-invariant fibre datum equals the c₃ carrier `S` (2.44 % proton/muon
swing, sensitivity ~3.84e6). Same-day direct measurements close the residual
openings: the 4₁ deformed Stokes amplitude is **real to the rung floor**
(odd-phase NULL, scope-(a), commit `f95c8f6730`), and the 5₂ anchor-dependent
quantum volume has `max |d𝔙/dq| = 1.47` — **O(1) vs the 3.84e6 required**
(`qbeta-5two-quantum-volume.witness.json`). A fibre derivation can supply the
**shape** of the bar-odd numerator `N_odd` (simple zero at q\*, slope
A′(q\*) ≈ +2.37, per the Im 𝔙_q→N_odd capstone scope doc); it cannot supply
the **value** below the experimental-Q_β floor (`dq*/dQ_β ≈ −0.54`). The gate
arithmetic is now Lean-recorded
([`MeasurementLimitedFloor.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MeasurementLimitedFloor.lean)).

**2. 4₁ is amphichiral ⇒ its bar-odd channel vanishes identically.** The bar
involution on quantum knot invariants acts as mirror image
(`J_K(q⁻¹) = J_{K*}(q)`); 4₁ ≅ 4₁\* forces every fibre-level 4₁ invariant —
colored Jones, Kashaev, Ohtsuki series, Stokes data — to be **bar-even**.
This is the structural *reason* behind the odd-phase NULL: the session
measured a symmetry-forced zero. **The odd datum must come from a chiral
knot; 5₂ is canonical** (smallest chiral hyperbolic knot; the second worked
example in the entire relevant literature: GGM Stokes tables
[arXiv:2007.10190](https://arxiv.org/abs/2007.10190),
[2111.04763](https://arxiv.org/abs/2111.04763), Garoufalidis–Kashaev state-
integral factorization [1304.2705](https://arxiv.org/abs/1304.2705),
Garoufalidis–Zagier cocycles [2111.06645](https://arxiv.org/abs/2111.06645),
GSWZ Habiro-ring-of-a-number-field running example
[2412.04241](https://arxiv.org/abs/2412.04241)).

## Literature facts (external)

- **GGM Stokes matrices are pairs of integer-coefficient q-series**, one
  entry = the DGG 3D index; tabulated for 4₁ **and 5₂**. The raw Stokes
  constants are integers (BPS counts); the anchor-independent *real*
  constant must be an **evaluation of the Stokes q-series at q₀**, not a raw
  integer.
- **The Habiro ring has no archimedean evaluation off roots of unity**
  (generic elements converge nowhere off roots of unity). Real-q₀ access
  goes through (a) Borel–Laplace median resummation of the q→1 series
  (Costin–Garoufalidis resurgence proved for torus-knot families,
  [2304.07001](https://arxiv.org/abs/2304.07001)) or (b) the two-variable
  holomorphic-block / descendant q-series lifts, which converge for |q|≠1.
- **The bar-odd projection of the block/Stokes data is unstudied** — the
  literature works the symmetric pairings (state integral, index); the
  antisymmetric (chirality-odd) pairing is definable from published 5₂ data
  but has no named treatment. Genuine opening.
- **GZ quantum-modularity cocycle entries at the real-q ray are computable,
  calibration-free constants** (state-integral built, hundreds of digits for
  4₁/5₂/(−2,3,7)) — a third cross-check route.

## Ranked attack options

| # | attack | object / computation | feasibility |
|---|---|---|---|
| **A1** | **Chirality-difference state integral for 5₂** | `Z_{5₂}(ℏ₀) − Z_{5₂*}(ℏ₀)` (Andersen–Kashaev Φ_b product, 1-dim integral, explicit in 1304.2705) evaluated by mpmath quadrature at real `ℏ₀ = ln q₀` | **session-computable** — the cleanest genuinely fibre-level bar-odd real number at q₀ |
| **A2** | **Bar-odd projection of the 5₂ GGM Stokes / index q-series** | antisymmetric combination of the tabulated integer q-series pair under the q↔q⁻¹ swap; evaluate at `q₀⁻¹ ≈ 0.9009` (geometric convergence) | **session-computable** — published integer coefficients |
| **A3** | **Capstone-carrier falsification on 5₂** | extend `qbeta_5two_quantum_volume_probe.py`: does any `u³·(smooth)` normalization carry `Im 𝔙_q(5₂)` (O(1), no zero at q\*) to `N_odd` (O(1e-8), simple zero at q\*, slope +2.37)? expected **fail** → narrows the capstone carrier to the categorical H₅(q) Markov trace, not the analytic NZ saddle | **session-computable** falsification |
| **A4** | **Median Borel–Laplace of the 5₂ bar-odd perturbative series** | mirror-difference Ohtsuki series, Borel–Padé + median resummation on the real ray; cross-check vs A1 via resurgence | needs-serious-work |
| **A5** | **5₂ H₅(q) categorical Markov-trace 𝔙_q** | build the fibre-level (pre-archimedean) 5₂ datum to feed the quantum-modularity two-route rigidity | needs-serious-work (the flagged G3 obstacle) |
| **A6** | **GSWZ Habiro-ring-of-number-field element for 5₂** | Frobenius + Bloch-group formulation; no archimedean evaluation exists in the literature | open-problem; nothing to run today |

**Pruned (do not re-attack):** any 4₁ odd datum (symmetry-forced zero); any
anchor-invariant datum as the swing *value* (scope-(b) Lean); the winding
lattice, branch-point tuning, ratio/W_λ routes (prior scope-(b)); route 3's
substrate-q₀ is not session-closable (missing categorical level-N selection
principle — the open problem itself).

## Session results (updated as attacks land)

- **A1 LANDED (derived chirality state-integral datum, 5/5).**
  [`qbeta_5two_chirality_state_integral_probe.py`](../../computations/probes/qbeta_5two_chirality_state_integral_probe.py)
  + witness: `Z_{5₂} = ∫Φ_b(v)³e^{−2πiv²}dv` on the substrate ray `τ = iβ`
  (`b = √β·e^{iπ/4}`, `q = 1/q₀`, `q̃ ≈ 1e-165`) computed **two independent
  ways** — strip-aware bent-contour quadrature with the corpus Φ_b evaluator,
  and the GGM/Peacock H-series factorization — agreeing at **3.4e-14**, gated
  by the exact 4₁ `b=1` closed form at **1.1e-19**. The frame-reduced split
  `Ẑ = e^{−iπ/4}Z` separates cleanly: `Re Ẑ = R^{1/8}H⁺₁H⁻₁` (the bar-even
  index channel) and `Im Ẑ = −(R^{1/8}/2)[βH⁺₂H⁻₀ − (1/β)H⁺₀H⁻₂]` — the
  **derived chirality-odd state-integral datum** at the substrate, the
  state-integral face of A2's odd-Stokes matrix datum. Honest: anchor-smooth
  (`|d ln(odd)/dq| = 3.6e2`) — odd ingredient, not the swing. Numerics
  lesson: the corpus `log_phi_b` integral rep is valid only in
  `|Im v| < Im c_b`; a contour leaving the strip produces silent garbage
  (first run cost 1033s) — the probe now sizes the bend angle to the strip.
- **A4.1 LANDED — the τ² misprint is ARBITRATED (4/4): GGM's eq 20 τ² is the
  misprint; Peacock eq 76 (at ξ) is correct.**
  [`qbeta_5two_phi_series_tau2_arbitration_probe.py`](../../computations/probes/qbeta_5two_phi_series_tau2_arbitration_probe.py)
  + witness: independent extraction of φ_σ1's Taylor coefficients from the
  radial asymptotics of the A1/A2-validated H-series on the tilted ray
  `τ = t·e^{iπ/6}` (σ1-dominant; model-guided phase unwrap; two-stage
  V-then-polynomial fit). Gates: dominant-saddle **V = Vol(5₂) − 1.379i with
  Re to 2e-8**; fit residual 1.3e-9; the AGREED τ¹ coefficient identifies
  the convention uniquely at **3.8e-4** (confirming the generator identity
  `GGM@z = Peacock@ξ`). Verdict: extracted τ² matches **Peacock at 1.9% vs
  GGM at 98% — 50.8× separation**. Bonus finding: the dominant saddle on
  this ray carries the **conjugate CS sign** (V = Vol − i·1.379). τ³ is
  reported as an ill-conditioned diagnostic (0.3 rel, convention twins tie).
  Three numerics lessons recorded in-file (principal-branch phase hops;
  \>π phase steps need model-guided unwrap; 1/τ-vs-polynomial collinearity
  needs the two-stage fit).
- **A4.2 LANDED — the coefficient engine (all gates at full precision).**
  [`qbeta_5two_phi_series_engine_probe.py`](../../computations/probes/qbeta_5two_phi_series_engine_probe.py)
  + witness: φ_σ1 generated to **order 24** from first principles (τ-channel
  steepest descent; `V₀ = 3Li₂(−e^y)+y²` reproducing GGM eq-19 exactly;
  vertices rational in the saddle via the `Li_{−k}` tower; Wick engine at
  dps 60). Three convention faults found + fixed empirically against
  validated references: the balanced Φ_b expansion uses **Bernoulli
  polynomials at ½** (`B_{2n}(1/2) = (2^{1−2n}−1)B_{2n}`; the naive form
  overshoots O(ħ) by exactly 3×; corrected form converges to 9e-25 by n=6
  against the corpus `log_phi_b`); the `P_k = phi_h[2k]` unit map; and the
  exact `e^{−ħ/8}` alignment for the Thm-3 `(q/q̃)^{1/8}` prefactor (found
  as a +1/8 shift in P₁). **Result: P₁ = printed at 9e-62; P₂ = the
  arbitrated Peacock@ξ value at 2e-60 — a third independent confirmation of
  the τ² misprint verdict; P₃ = printed at 5e-59** (the A4.1 τ³ diagnostic
  settled exactly). Borel diagnostics: nearest singularity 5.798 vs the
  predicted Stokes distance `|V(σ1)−V(σ2)| = 5.656` (2.5%, in the
  `x = 2πiτ` Borel plane — resurgence structure confirmed). **The A4 median
  Borel–Laplace program is unblocked with a full-precision 24-order basis.**
- **A4.3 LANDED — the resummation + bar-odd split (bean `qou-ea86` COMPLETED,
  2026-07-18).** [`qbeta_5two_median_borel_resummation_probe.py`](../../computations/probes/qbeta_5two_median_borel_resummation_probe.py)
  + witness (committed, 4/4): Borel–Padé [11/12] pole map locating `ζ₁₂ =
  i(V₁−V₂)` to 2.2 %; directional Laplace along the substrate ray (`arg x = 180°`
  never meets a Stokes ray, so the median prescription is not needed for the
  physical evaluation); exact-object cross-check `F = h₁·e^{−V/2πτ}` beating raw
  truncation at `|x| = 1,2,3`; and the bar-odd datum `[φ(x)−φ(−x)]/2`,
  truncation↔resummation-consistent to ~1e-19 at the substrate. Two-anchor
  follow-up (proton `q_at` / muon `q_muon_at`): the bar-odd datum is
  **anchor-smooth** (`d ln|odd|/dq ≈ 8.6`, O(10¹)) — the odd **ingredient**, not
  the swing, a **third** independent anchor-smoothness confirmation after A1
  (3.6e2) and A2 (8.2e2), consistent with the proved measurement-limited scope-(b)
  (`no_anchor_invariant_realizes_swing`). **A4 is closed.** The open odd-ingredient
  frontier is now A5 (categorical H₃(q) quantum `𝔙_q(5₂)`, bean `qou-3yxn`).
- **A5.1 ATTEMPTED — blocked by a certified literature/transcription
  discrepancy (5/5 on the discrepancy itself).**
  [`qbeta_5two_colored_tower_barodd_qstar_probe.py`](../../computations/probes/qbeta_5two_colored_tower_barodd_qstar_probe.py)
  + witness. The Masbaum math/0306345 Thm-5.1 twist-knot tower at p=2
  (K₂ = 5₂) **fails external validation at N ≥ 3** despite: N=2 = corpus TL₃
  Jones at 1e-41; p=±1 = the printed Rmk-5.2 values; amphichiral 4₁ bar-odd
  null at 1e-30; the p=−1 tower reproducing the **proven** 4₁ VC growth
  (2.0299); and the §5-Example `c'_{n,2}` ≡ the independent §4 skein
  composition to 1e-31. The arbiter — **GZ 2111.06645 eq (7.9)**, whose
  growth tracks the proven Vol(5₂) (2.71→2.76→2.80 after the 3π·logN/N
  subtraction) — disagrees with the tower already at N=3 (16.09 vs 20.95),
  ratio diverging to 3.6e4 at N=80; the tower's growth constant ≈ 2.03.
  Mirror variants eliminated. **Either a subtle transcription fault upstream
  of both my routes, or a genuine fault in the printed Thm-5.1 p≥2
  assembly** — the session's third caught literature-level fault (GGM τ²
  misprint; Peacock towers-vs-entries; now this). Arbitration path: an
  independent N=3 colored Jones of 5₂ via TL 2-cabling. **The B_N q*-scan
  (no zero found, anchor-smooth, N=3..32) is recorded as an UNCERTIFIED
  diagnostic — no capstone falsification is claimed on the categorical
  colored face.** Bean `qou-3yxn` stays open, blocked here. A discarded
  O(N⁸) R-matrix attempt failed its own braid-relation gate pre-commit —
  the gates-first discipline caught every fault in this tranche.
- **A5.2 ARBITRATION LANDED (6/6) — GZ (7.9) correct, Masbaum Thm-5.1 p=2
  REFUTED; the N=3 categorical q\*-test is now CERTIFIED.**
  [`qbeta_5two_n3_cable_arbitration_probe.py`](../../computations/probes/qbeta_5two_n3_cable_arbitration_probe.py)
  + witness: a generic TL_n transfer engine computes the **definitional**
  `J'₃ = ⟨K(e₂)⟩/⟨e₂⟩` via 2-cabled braid closures. Gates: corpus TL₃ Jones
  at 1e-31; the 4₁ 2-cable = the trusted p=−1 tower at **1e-30** (key:
  `q_Masbaum = q_cable²` — "recall a = A²"); trefoil calibrates the framing
  factor to exactly `q⁴` = the standard ribbon twist `q_M²` on V₃.
  **Verdict:** at the radial root limit (`⟨e₂⟩ = [3]` vanishes at the N=3
  root — genuine 0/0, handled by limit) the cable gives
  `|J'₃(5₂)| = 20.95232671` = **GZ eq (7.9)** to the ε-residual — not the
  Masbaum tower's 16.09; at real q the tower deviates measurably (8.5e-6 at
  q=1.037, growing with |q−1|). **The printed Thm-5.1 p≥2 assembly is not
  the 5₂ colored Jones** — resolved, not just flagged. **Certified [C]:**
  the bar-odd datum `B₃(5₂;q*) = 0.394` via the validated cable has **no
  zero** on q\*±2e-8 and is anchor-smooth (8.4e1; 4₁ null control 6.8e-31)
  — capstone constraint (2) fails on the certified N=3 categorical face
  (scope-(a)), superseding the earlier uncertified tower diagnostic. Higher
  N needs e_{N−1} cables (Catalan growth) — open but now on a validated
  foundation.
- **A5 disposition (narrowed + first bricks laid).** The A3 falsification +
  sibling #3954's σ3-shape constraint jointly kill the analytic-saddle
  carrier; the capstone carrier search narrows to the **categorical H₃(q)
  Markov-trace 𝔙_q(5₂)** (corrected braid `[1,1,1,2,-1,2]` is B₃ ⇒ H₃, not
  H₅). Classical H₃ bricks already exist (validated TL₃ Jones + bar-odd
  datum); the missing object is the *quantum* (colored/Kashaev-tower) trace
  datum at the substrate. Bean `qou-3yxn` stays open with this scope.

- **A2 LANDED (derived odd-Stokes datum).**
  [`qbeta_5two_stokes_barodd_index_probe.py`](../../computations/probes/qbeta_5two_stokes_barodd_index_probe.py)
  + witness, 8/8: both 5₂ Stokes automorphisms `S⁺(q)`, `S⁻(q)` (GGM
  2007.10190 eqs 29a/29b, 112–124, transcribed from the owner-supplied PDF)
  evaluated at the substrate point `q = 1/q₀`. Gates: all 18 printed
  H-series tables exact; `det W = 2`; assembled q→0 limits = the eq-100a/b
  Stokes-constant products; `(0,0)` entry = `Ind^rot` (eq 102); `det S± = 1`;
  **Conjecture 1(b) `S⁺ᵀ·S⁻ = 1` at 1.1e-37 with independently-assembled
  matrices**. The odd chirality datum `O = ½(S⁺−S⁻)` is live:
  **‖O‖_F = 2.107** — a derived, calibration-free fibre-level odd-Stokes
  datum of the chiral 5₂ (4₁'s vanishes by amphichirality). Honest:
  anchor-smooth (max slope 8.2e2 ≪ 3.84e6) — the odd *ingredient*, not the
  swing. Structural finding: `Ind^rot_{5₂}` is **bar-EVEN** (eq 124) despite
  5₂'s chirality — the naive "chiral index" intuition is wrong; the odd
  channel lives in `S⁺ vs S⁻`, not in the index. Lesson: the Peacock eq-99
  "towers" are per-ray radar factors, **not** entries of the assembled
  matrix.
- **Literature flag (for A4):** the printed 5₂ perturbative series carries a
  **τ² misprint** — GGM eq 20 and Peacock eq 76 agree at τ¹, τ³ under the
  generator map `z = ξ/(ξ−1)` but disagree irreconcilably at τ²
  (machine-checked). Any A4 Borel work must first arbitrate c₂ from an
  independent saddle expansion; do not blind-trust either printed value.

- **A3 LANDED (falsification confirmed, scope-(a)).**
  [`qbeta_5two_capstone_carrier_falsification_probe.py`](../../computations/probes/qbeta_5two_capstone_carrier_falsification_probe.py)
  + witness, 6/6: the 5₂ NZ-saddle bar-odd datum
  `B(q)=[𝔙(m=q)−𝔙(m=1/q)]/2` is smooth and **nonvanishing at q\***
  (`|B(q*)|=0.149`, 0 sign changes on a ±2e-8 grid straddling the anchor
  window); pushing the simple zero into the `u³` normalization's smooth
  factor would need log-slope ≈ 4×10⁸ (not smooth). Writhe data
  (capstone's writhe-2 **and** the corrected #3892 writhe-4 `½(q⁴−q⁻⁴)=0.43`)
  fail identically. **The capstone carrier is not the analytic NZ-saddle
  datum** — narrows to the categorical H₃(q) Markov-trace 𝔙_q (A5).
- **Braid landmine (respect in all 5₂ work):** the pre-#3892 corpus "5₂"
  braid `[1,1,1,-2,1,-2]` is actually **6₂** (det 11, writhe 2); canonical
  5₂ is `[1,1,1,2,-1,2]` (det 7, writhe 4). The capstone's
  `D_odd = ½(q²−q⁻²)` is the 6₂-era form; the corrected 5₂ datum is
  `½(q⁴−q⁻⁴) = sinh(2u_sub)`.
- **Classical bar-odd home already built:** `qbeta_5two_jones_barodd_probe.py`
  (validated TL₃ Kauffman bracket; `V(5₂)_odd ≠ 0`, O(1) at q₀,
  anchor-smooth — the bar-odd home, not the swing). A5's remaining core is
  the **categorical/quantum** 𝔙_q(5₂), which is H₃(q)-sized (B₃ braid), not
  H₅ as first beaned.

## Honest prize statement

Even a successful A1/A2 yields a **derived, anchor-independent bar-odd
fibre constant of 5₂** — which would make the *form* of the odd channel a
prediction and feed the Im 𝔙_q→N_odd capstone — but the Q_β *value*
remains experimental-Q_β-limited (the L2 100× target stays out of reach by
the measurement floor, per `MeasurementLimitedFloor.lean`). Comparison to
observed only; no ontological claims.
