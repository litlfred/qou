/-
# The A=4 (⁴He) ≥4-body magnitude via the interface operator is a ONE-SCALAR gate:
# the derived `−ln det(I + G)` form (exchange spectrum `{±√5, ±1}`, #3924) is
# SURJECTIVE onto `(0, ∞)` in its single free scalar `m` — so every positive AME
# target is reachable (NOT a scope-(b) exclusion) yet none is fixed by a categorical
# driver (NOT a closure): **WALL(scope-(a))**, sharpened from the #4526 reweight bracket.
# Separately, the derived ceiling `m < 1/√5` **structurally excludes** the naive uniform
# per-pair magnitude `z ≈ 0.499` (scope-(b), cited invariant = the exchange spectrum).

Option-E PROBE 2 (the A=4 interface operator + `conj:s5-so3-fiber-action`), forward, 0-fit.
This file consolidates two previously-separate A=4 magnitude framings and proves they
collapse to the SAME single under-determined categorical scalar.

## The two framings that meet here

1. **s5-so3 normalized reweight (#4526, `GeometricWLambdaA4Helium.lean`).** A normalized
   color-tube measure `W` (`Σ W = 1`, `W ≥ 0`) reweighting per-block characters gives a
   weighted average bounded by `max|χ|`.  The production weight `y_λ` UNDERSHOOTS
   (`0.243 MeV`), the geometric weight `d_q²/D²` OVERSHOOTS (`60.33 MeV`); the two 0-fit
   endpoints BRACKET the target but neither lands, and the bound `E₀·max|χ| = 266 MeV`
   lies above the target ⇒ NOT scope-(b) excluded — WALL(scope-(a)).

2. **Interface-operator `−ln det(I + G)` form (#3924, merged; probe
   `b4-slater-antisymmetrizer-exchange-sign`).** The ⁴He `[1⁴]` complete-graph exchange
   matrix `G` has the EXACT spectrum `{±√5, ±1}` (derived, not fitted), so with a single
   per-pair bond magnitude `m` its eigenvalues are `{±m√5, ±m}` and

     `det(I + G) = (1 + m√5)(1 − m√5)(1 + m)(1 − m) = (1 − 5m²)(1 − m²)`,

   giving the connected 4-body cumulant `b₄ = −ln det(I + G)` (the attractive branch).
   The physicality `det(I + G) > 0 ⇔ m < 1/√5` reproduces the derived writhe cap.  The
   ONE open scalar is `m` — precisely the standing Δ_λ magnitude gate.

## What THIS file adds (the push forward from #4526's WALL)

The #4526 bracket showed the target sits *between* two normalized measures.  Here the
sharper `−ln det` form shows the obstruction was never the bracket width: with the derived
spectrum fixed, the magnitude functional `b₄(m)` is **strictly monotone** and **surjects
onto all of `(0, ∞)`** as `m` ranges over `(0, 1/√5)`.  Hence:

* **`magnitude_form_surjective`** — for EVERY positive target `t` there is an
  `m ∈ (0, 1/√5)` with `b₄(m) = t`, via the CLOSED FORM
  `m*(t) = √((6 − √(16 + 20·e^{−t}))/10)`.  This is proved algebraically (no IVT):
  `det(I + G)(m*) = e^{−t}` exactly, so `b₄(m*) = t`.  Because `m*` is a function of the
  TARGET, choosing it is an **anchor-inversion = FIT**; it is *never* wired.  The
  existence proof establishes reachability (⇒ NOT scope-(b) excluded), NOT a derivation.
* **`b4_strictMono_on`** — `b₄` is strictly increasing on `(0, 1/√5)`, so the required
  `m*` is unique; the gate is exactly one scalar.
* **`naive_z_unphysical`** — the naive uniform per-pair magnitude `z ≈ 0.499` has
  `5z² > 1`, so `det(I + G)(z) < 0`: the attractive `−ln det` branch does not exist there.
  This is a **scope-(b) structural exclusion** of the naive-uniform-`z` mechanism, citing
  a proved invariant (the exchange spectrum `{±√5,±1}` ⇒ most-negative eigenvalue `−m√5`
  ⇒ `det = (1−5m²)(1−m²)`).  It is the direct analog of the #4526 geometric OVERSHOOT:
  both canonical categorical objects run PAST the physical value, so the surviving
  mechanism is a categorical principle fixing `m` strictly BELOW the naive `z` (equiv. a
  normalized `W` strictly BELOW the geometric `d_q²/D²`).

## Honest verdict

The A=4 ≥4-body magnitude is **open at scope-(a)**.  The surviving mechanism is now
pinned to a SINGLE scalar `m ∈ (0, 1/√5)` (equivalently, one intermediate normalized
weight): the form reaches every positive value, so matching the AME target is a FIT unless
an independent categorical driver fixes `m`.  No identified driver does.  No inversion is
wired; `free_parameters = 0` in production.

Base ring (§7c): `ℝ` throughout — the whole content is archimedean (ordering `0 < m`,
`Real.sqrt`, `Real.log`, `Real.exp`).

-- Ref: [leitner2026] computations/probes/b4-slater-antisymmetrizer-exchange-sign.witness.json
   (the derived spectrum `{±√5,±1}`, `det=(1−5m²)(1−m²)`, ceiling `1/√5`, `b₄` target; 0-fit).
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors", Invent. Math. 92 (1988) 349-383.
-/
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Deriv

namespace QOU.MassTheory.A4InterfaceMagnitude

open Real

/-! ### The derived magnitude form `det(I + G) = (1 − 5m²)(1 − m²)` -/

/-- The determinant `det(I + G)` for the ⁴He `[1⁴]` complete-graph exchange matrix `G`
whose EXACT spectrum is `{±√5, ±1}` (derived in #3924, probe
`b4-slater-antisymmetrizer-exchange-sign`): with per-pair bond magnitude `m`, the
eigenvalues of `G` are `{±m√5, ±m}` and

  `det(I + G) = (1 + m√5)(1 − m√5)(1 + m)(1 − m) = (1 − 5m²)(1 − m²)`. -/
noncomputable def detG (m : ℝ) : ℝ := (1 - 5 * m ^ 2) * (1 - m ^ 2)

/-- `det(I + G)` is exactly the product over the four spectral eigenvalues `{±m√5, ±m}`.
This is the derivation of `detG` from the exchange spectrum (not an assertion of a value):
`∏ (1 + λᵢ)` with `λ ∈ {m√5, −m√5, m, −m}` telescopes to `(1 − 5m²)(1 − m²)`. -/
theorem detG_eq_spectral_product (m : ℝ) :
    detG m = (1 + m * Real.sqrt 5) * (1 - m * Real.sqrt 5) * ((1 + m) * (1 - m)) := by
  have h5 : Real.sqrt 5 ^ 2 = 5 := Real.sq_sqrt (by norm_num)
  unfold detG
  linear_combination (m ^ 2 * (1 - m ^ 2)) * h5

/-- Polynomial normal form `det(I + G) = 1 − 6m² + 5m⁴`. -/
theorem detG_expand (m : ℝ) : detG m = 1 - 6 * m ^ 2 + 5 * m ^ 4 := by
  unfold detG; ring

/-! ### Positivity region and the derived ceiling `m < 1/√5` -/

/-- **Physical region.**  For `0 < m` with `5m² < 1` (i.e. `m < 1/√5`), the determinant is
strictly between `0` and `1`.  `0 < det` is physicality; `det < 1` makes `b₄ = −ln det`
strictly positive (an attractive/binding contribution). -/
theorem detG_mem_Ioo (m : ℝ) (hm : 0 < m) (hceil : 5 * m ^ 2 < 1) :
    0 < detG m ∧ detG m < 1 := by
  have hm2 : 0 < m ^ 2 := by positivity
  have h1 : 0 < 1 - 5 * m ^ 2 := by linarith
  have hlt1 : m ^ 2 < 1 := by nlinarith
  have h2 : 0 < 1 - m ^ 2 := by linarith
  refine ⟨by unfold detG; positivity, ?_⟩
  unfold detG
  nlinarith [hm2, h1, h2, mul_pos h1 h2]

/-- **The derived ceiling structurally excludes `m ≥ 1/√5` (within the framing `m < 1`).**
If `1/5 < m²` and `m² < 1`, then `det(I + G) < 0`: the first factor `1 − 5m²` is negative
while `1 − m²` is positive.  Cited invariant: the exchange spectrum `{±√5, ±1}` fixes the
most-negative scaled eigenvalue at `−m√5`, giving `det = (1 − 5m²)(1 − m²)`.  This is a
**scope-(b)** exclusion of any per-pair magnitude at or above the writhe cap `1/√5`. -/
theorem detG_neg_of_above_ceiling (m : ℝ) (hlo : 1 / 5 < m ^ 2) (hhi : m ^ 2 < 1) :
    detG m < 0 := by
  have h1 : 1 - 5 * m ^ 2 < 0 := by linarith
  have h2 : 0 < 1 - m ^ 2 := by linarith
  unfold detG
  exact mul_neg_of_neg_of_pos h1 h2

/-- **The naive uniform per-pair magnitude `z ≈ 0.499` is UNPHYSICAL (scope-(b)).**  The
framework's naive bond factor `z = 0.499320334` (probe
`b4-1four-complete-graph-writhe-signs`, constant `z_bond_factor`) satisfies `5z² > 1`
(`z` exceeds the writhe cap `1/√5 ≈ 0.447` by ~12%), so `det(I + G)(z) < 0` and the
attractive `−ln det` branch does not exist there.  Direct analog of the #4526 geometric
OVERSHOOT: the naive categorical value runs PAST the physical window. -/
theorem naive_z_unphysical : detG (4993 / 10000) < 0 := by
  apply detG_neg_of_above_ceiling <;> norm_num

/-! ### Convention-D naive magnitude is unphysical across the whole physical q-window -/

/-- The **canonical convention-D** naive per-pair (Markov) bond magnitude
`z_D(q) = q³/(q²+1)` (owner ruling 2026-08-15 R1: convention D is canonical, C
excised).  The `naive_z_unphysical` theorem above used the *excised* convention-C
value `z_C(q₀) ≈ 0.499` as a bare rational; this is its canonical-convention
replacement, stated symbolically in `q` and proved on the whole window rather
than at a point. -/
noncomputable def zD (q : ℝ) : ℝ := q ^ 3 / (q ^ 2 + 1)

/-- `z_D(q)² = q⁶/(q²+1)²`. -/
theorem zD_sq (q : ℝ) : zD q ^ 2 = q ^ 6 / (q ^ 2 + 1) ^ 2 := by
  unfold zD; rw [div_pow]; ring_nf

/-- On the physical window `1 ≤ q ≤ 7/5` the convention-D naive magnitude sits
strictly **above** the writhe ceiling and **below** `1`: `1/5 < z_D² < 1`.  Both
bounds are polynomial (`q⁴ + 2q² + 1 ≤ 4q⁶ < 5q⁶` for the lower; `q⁶ < q⁴+2q²+1`
on the window for the upper).  The window comfortably contains the substrate
`q₀ ≈ 1.110`. -/
theorem zD_sq_mem (q : ℝ) (hlo : 1 ≤ q) (hhi : q ≤ 7 / 5) :
    1 / 5 < zD q ^ 2 ∧ zD q ^ 2 < 1 := by
  have hq1 : 1 ≤ q ^ 2 := by nlinarith
  have hqm1 : (0 : ℝ) ≤ q ^ 2 - 1 := by linarith
  have hq2 : (0 : ℝ) ≤ q ^ 2 := by positivity
  have hq4 : (0 : ℝ) ≤ q ^ 4 := by positivity
  have hq6_ge_q4 : q ^ 4 ≤ q ^ 6 := by nlinarith [mul_nonneg hq4 hqm1]
  have hq6_ge_q2 : q ^ 2 ≤ q ^ 6 := by nlinarith [mul_nonneg hq2 hqm1, mul_nonneg hq4 hqm1]
  have hq6_ge_1 : (1 : ℝ) ≤ q ^ 6 := by nlinarith [hq1, mul_nonneg hq2 hqm1, mul_nonneg hq4 hqm1]
  have hd2 : (0 : ℝ) < (q ^ 2 + 1) ^ 2 := by positivity
  rw [zD_sq]
  constructor
  · rw [lt_div_iff₀ hd2]
    nlinarith [hq6_ge_q4, hq6_ge_q2, hq6_ge_1]
  · rw [div_lt_one hd2]
    have hq2u : q ^ 2 ≤ 49 / 25 := by nlinarith [hhi, hlo]
    nlinarith [hq1, hq2u,
      mul_nonneg (by linarith : (0 : ℝ) ≤ 49 / 25 - q ^ 2) hq4,
      mul_nonneg (by linarith : (0 : ℝ) ≤ 49 / 25 - q ^ 2) hq2]

/-- **(SCOPE-(b), convention-D, whole q-window) The canonical convention-D naive
per-pair magnitude `z_D = q³/(q²+1)` is unphysical for EVERY `q ∈ [1, 7/5]`.**
`det(I + G)(z_D) < 0`, because `5·z_D² > 1` (above the writhe ceiling `1/√5`)
while `z_D² < 1`.  This is the convention-D analog of `naive_z_unphysical` (which
cited the *excised* convention-C value `0.499`): under the CANONICAL Markov
convention the overshoot is *larger* — `z_D(q₀) ≈ 0.613 > z_C(q₀) ≈ 0.499` — so
the exclusion is strengthened, and it now holds across the entire `|q| > 1`
physical window, not just at the substrate point.  Cited invariant: the exchange
spectrum `{±√5, ±1}` fixing `det = (1 − 5m²)(1 − m²)` (`detG_eq_spectral_product`).
The surviving mechanism must therefore fix `m` strictly BELOW the naive braiding
overlap under **either** Markov convention. -/
theorem zD_unphysical (q : ℝ) (hlo : 1 ≤ q) (hhi : q ≤ 7 / 5) : detG (zD q) < 0 := by
  obtain ⟨h1, h2⟩ := zD_sq_mem q hlo hhi
  exact detG_neg_of_above_ceiling (zD q) h1 h2

/-! ### The magnitude functional `b₄(m) = −ln det(I + G)` -/

/-- The connected 4-body cumulant magnitude in the derived form: `b₄(m) = −ln det(I + G)`,
the attractive branch (positive on the physical region). -/
noncomputable def b4 (m : ℝ) : ℝ := - Real.log (detG m)

/-- **`b₄` is strictly positive on the physical region** `(0, 1/√5)`: `det ∈ (0,1)` there,
so `log det < 0`, hence `b₄ = −log det > 0`. -/
theorem b4_pos (m : ℝ) (hm : 0 < m) (hceil : 5 * m ^ 2 < 1) : 0 < b4 m := by
  obtain ⟨hpos, hlt1⟩ := detG_mem_Ioo m hm hceil
  have : Real.log (detG m) < 0 := Real.log_neg hpos hlt1
  unfold b4; linarith

/-- **`det(I + G)` is strictly DECREASING on the physical region.**  For
`0 < m₁ < m₂` with `5m₂² < 1`, `det(m₁) > det(m₂) > 0`.  Purely algebraic:
`det(m₁) − det(m₂) = (m₂² − m₁²)·(6 − 5(m₁² + m₂²))`, and both factors are positive since
`m₁² + m₂² < 2/5 < 6/5`. -/
theorem detG_strictAnti (m₁ m₂ : ℝ) (h1 : 0 < m₁) (h12 : m₁ < m₂)
    (hceil : 5 * m₂ ^ 2 < 1) : detG m₂ < detG m₁ ∧ 0 < detG m₂ := by
  have hm2pos : 0 < m₂ := lt_trans h1 h12
  have hsq : m₁ ^ 2 < m₂ ^ 2 := by nlinarith
  have hsum : 5 * (m₁ ^ 2 + m₂ ^ 2) < 6 := by nlinarith
  have hpos2 : 0 < detG m₂ := (detG_mem_Ioo m₂ hm2pos hceil).1
  refine ⟨?_, hpos2⟩
  rw [detG_expand, detG_expand]
  nlinarith [hsq, hsum, sq_nonneg (m₂ ^ 2 - m₁ ^ 2)]

/-- **`b₄` is strictly INCREASING on the physical region** (the gate is exactly one
scalar; the required `m` is unique). -/
theorem b4_strictMono_on (m₁ m₂ : ℝ) (h1 : 0 < m₁) (h12 : m₁ < m₂)
    (hceil : 5 * m₂ ^ 2 < 1) : b4 m₁ < b4 m₂ := by
  obtain ⟨hdec, hpos2⟩ := detG_strictAnti m₁ m₂ h1 h12 hceil
  have hpos1 : 0 < detG m₁ := lt_trans hpos2 hdec
  have hlog : Real.log (detG m₂) < Real.log (detG m₁) := Real.log_lt_log hpos2 hdec
  unfold b4; linarith

/-! ### Surjectivity: the derived form reaches EVERY positive magnitude (⇒ not scope-(b)) -/

/-- The closed-form inverse `u*(D) = (6 − √(16 + 20D))/10` — the smaller root of the
quadratic `5u² − 6u + (1 − D) = 0` in `u = m²`.  For `D ∈ (0,1)` it lies in `(0, 1/5)`. -/
noncomputable def uStar (D : ℝ) : ℝ := (6 - Real.sqrt (16 + 20 * D)) / 10

/-- `u*(D)` is a root: `5·u*² − 6·u* = D − 1`.  Algebraic, using `√(16+20D)² = 16+20D`. -/
theorem uStar_root (D : ℝ) (hD : 0 ≤ D) : 5 * uStar D ^ 2 - 6 * uStar D = D - 1 := by
  have h16 : (0:ℝ) ≤ 16 + 20 * D := by linarith
  have hs2 : Real.sqrt (16 + 20 * D) ^ 2 = 16 + 20 * D := Real.sq_sqrt h16
  unfold uStar
  have hs := hs2
  set s := Real.sqrt (16 + 20 * D) with hsdef
  field_simp
  nlinarith [hs]

/-- For `D ∈ (0,1)`, the root `u*(D)` lies strictly in `(0, 1/5)`. -/
theorem uStar_mem_Ioo (D : ℝ) (hD0 : 0 < D) (hD1 : D < 1) :
    0 < uStar D ∧ uStar D < 1 / 5 := by
  have h16 : (0:ℝ) ≤ 16 + 20 * D := by linarith
  -- s := √(16+20D) ∈ (4, 6)
  have hs_gt4 : (4:ℝ) < Real.sqrt (16 + 20 * D) := by
    have : (4:ℝ) = Real.sqrt 16 := by
      rw [show (16:ℝ) = 4 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
    rw [this]
    apply Real.sqrt_lt_sqrt (by norm_num); linarith
  have hs_lt6 : Real.sqrt (16 + 20 * D) < 6 := by
    have h6 : (6:ℝ) = Real.sqrt 36 := by
      rw [show (36:ℝ) = 6 ^ 2 by norm_num, Real.sqrt_sq (by norm_num)]
    rw [h6]
    apply Real.sqrt_lt_sqrt h16; linarith
  unfold uStar
  constructor
  · linarith
  · linarith

/-- **`det(I + G)(√(u*(D))) = D`** for `D ∈ (0,1)`: the closed-form `m = √u*` hits any
prescribed determinant value `D`.  Uses `(√u)² = u` and the root identity. -/
theorem detG_mStar (D : ℝ) (hD0 : 0 < D) (hD1 : D < 1) :
    detG (Real.sqrt (uStar D)) = D := by
  have hu0 : 0 < uStar D := (uStar_mem_Ioo D hD0 hD1).1
  have husq : Real.sqrt (uStar D) ^ 2 = uStar D := Real.sq_sqrt (le_of_lt hu0)
  have hroot : 5 * uStar D ^ 2 - 6 * uStar D = D - 1 := uStar_root D (le_of_lt hD0)
  rw [detG_expand]
  -- 1 - 6 m² + 5 m⁴ with m² = u*: = 1 - 6u* + 5u*² = 1 + (D - 1) = D
  have hm4 : Real.sqrt (uStar D) ^ 4 = uStar D ^ 2 := by
    rw [show (4:ℕ) = 2 * 2 by rfl, pow_mul, husq]
  rw [husq, hm4]
  linarith [hroot]

/-- **(MAIN) The derived magnitude form is SURJECTIVE onto `(0, ∞)` in its one free
scalar.**  For every positive target `t`, there exists a per-pair bond magnitude
`m ∈ (0, 1/√5)` (equivalently `5m² < 1`) with `b₄(m) = t`, given by the closed form
`m = √((6 − √(16 + 20·e^{−t}))/10)`.

Consequence for the A=4 program: because `b₄(m)` attains EVERY positive value, matching an
AME target (`b₄ ≈ 9.243 MeV`, or `|μ₄| ≈ 4.591`, or `B(⁴He) ≈ 28.30`) does not constrain
the framework at all UNLESS an independent categorical driver fixes `m`.  The witness `m`
here is a function of the target `t` — an anchor-inversion = **FIT** — so this is a
reachability (NOT scope-(b) excluded) statement, never a derivation and never wired. -/
theorem magnitude_form_surjective (t : ℝ) (ht : 0 < t) :
    ∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ b4 m = t := by
  set D : ℝ := Real.exp (-t) with hDdef
  have hD0 : 0 < D := Real.exp_pos _
  have hD1 : D < 1 := by rw [hDdef]; exact Real.exp_lt_one_iff.mpr (by linarith)
  refine ⟨Real.sqrt (uStar D), ?_, ?_, ?_⟩
  · -- 0 < √u* since 0 < u*
    exact Real.sqrt_pos.mpr (uStar_mem_Ioo D hD0 hD1).1
  · -- 5 m² < 1 since m² = u* < 1/5
    have husq : Real.sqrt (uStar D) ^ 2 = uStar D := Real.sq_sqrt (le_of_lt (uStar_mem_Ioo D hD0 hD1).1)
    have : uStar D < 1 / 5 := (uStar_mem_Ioo D hD0 hD1).2
    rw [husq]; linarith
  · -- b4 m = -log(detG m) = -log D = -(-t) = t
    have hdet : detG (Real.sqrt (uStar D)) = D := detG_mStar D hD0 hD1
    unfold b4
    rw [hdet, hDdef, Real.log_exp]
    ring

/-! ### Documented AME targets are all positive ⇒ all reachable (each match is a fit) -/

/-- Documented A=4 magnitude targets (probe constants; TARGETS, never inverted into
production): the `[1⁴]` connected cumulant `b₄ ≈ 9.243 MeV`, the 4-body simplex residual
`|μ₄| ≈ 4.591 MeV`, and the full binding `B(⁴He) ≈ 28.296 MeV`.  Each is positive, hence
each is reachable by `magnitude_form_surjective` via a target-dependent `m` (a fit). -/
theorem documented_targets_all_reachable :
    (∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ b4 m = 9.243) ∧
    (∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ b4 m = 4.591048) ∧
    (∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ b4 m = 28.29566) :=
  ⟨magnitude_form_surjective _ (by norm_num),
   magnitude_form_surjective _ (by norm_num),
   magnitude_form_surjective _ (by norm_num)⟩

/-! ### Capstone: WALL(scope-(a)) with the surviving mechanism pinned to one scalar -/

/-- **(CAPSTONE) The A=4 ≥4-body magnitude is a ONE-SCALAR gate — WALL(scope-(a)) — and
the naive uniform per-pair magnitude is scope-(b) EXCLUDED.**

With the derived exchange spectrum `{±√5, ±1}` fixed (`detG_eq_spectral_product`), the
magnitude functional `b₄ = −ln det(I + G)`:

1. **surjects onto `(0, ∞)`** (`magnitude_form_surjective`): every positive AME target is
   reachable ⇒ the magnitude is **NOT scope-(b) excluded**; but the reaching `m` is a
   function of the target (an anchor-inversion = FIT) ⇒ **NOT closed** — no identified
   categorical driver fixes `m`.  This SHARPENS the #4526 reweight bracket: the obstruction
   is not the bracket width but that the single scalar `m` is free.
2. **is strictly monotone** on `(0, 1/√5)` (`b4_strictMono_on`) ⇒ the gate is *exactly one*
   scalar and the required `m` is unique.
3. **excludes the naive uniform `z ≈ 0.499`** (`naive_z_unphysical`): `5z² > 1` ⇒
   `det < 0`, unphysical — a scope-(b) exclusion citing the proved spectrum.  Direct analog
   of the #4526 geometric OVERSHOOT ⇒ the surviving mechanism is a categorical principle
   fixing `m` strictly BELOW the naive `z` (equiv. a normalized `W` strictly below
   `d_q²/D²`).

Nothing is wired; `μ₄`/`B(⁴He)`/`b₄` are never inverted into production; `free_parameters
= 0`. -/
theorem a4_magnitude_one_scalar_gate :
    -- (1) reachable (not scope-(b)) yet target-parametrized (a fit, not closed):
    (∀ t : ℝ, 0 < t → ∃ m : ℝ, 0 < m ∧ 5 * m ^ 2 < 1 ∧ b4 m = t) ∧
    -- (2) exactly one scalar — strict monotonicity on the physical region:
    (∀ m₁ m₂ : ℝ, 0 < m₁ → m₁ < m₂ → 5 * m₂ ^ 2 < 1 → b4 m₁ < b4 m₂) ∧
    -- (3) scope-(b) exclusion of the naive uniform per-pair magnitude z ≈ 0.499:
    detG (4993 / 10000) < 0 :=
  ⟨magnitude_form_surjective, b4_strictMono_on, naive_z_unphysical⟩

end QOU.MassTheory.A4InterfaceMagnitude
