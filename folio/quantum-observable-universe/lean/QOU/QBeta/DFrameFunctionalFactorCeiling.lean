/-
# The functional side of a convention-D correction on `Δ_S` has a ceiling below 2

Bean `qou-cds1` (re-derive the `Q_β` `c_k` ladder under convention D),
formalize-first. The bean's open question since 2026-09-14 is *what object
supplies a multiplicative factor above 1 on the ruled base*. This file settles
the **functional** half of that question for the decay element `Δ_S`, exactly
and for every `q`, and says how large the functional half can possibly be.

## Setting (all of it already proved elsewhere; restated, not re-derived)

* `χ^(2,1)(Δ_S) = 0` for every split of `Δ_S`'s `σ`-support
  (`QOU.QBeta.DecayBlockCarrier.chi21_deltaS`), and a convention-D admissible
  functional has `(1³)` weight zero. So **any** D-admissible trace `φ` returns
  `φ(Δ_S) = w₃ · χ^(3)(Δ_S)` with `w₃` its `(3)`-block weight
  (`DecayBlockCarrier.decay_carried_by_single_block` for the Markov case; the
  same two facts give it for every trace in that span).
* A *normalised* trace (`φ(1) = 1`) in that span has `w₃ + 2·w₂₁ = 1`, the `2`
  being `dim V_(2,1)`.
* The ruled functional (owner, 2026-09-08) is the Markov trace at
  `z_D = q³/(q²+1)`, with `w₃ = y₃ᴰ = (q⁴+1)/(q²+1)²` and
  `w₂₁ = y₂₁ᴰ = q²/(q²+1)²` (`DecayBlockCarrier.y3_zD`, `y21_zD`).

So the factor by which a different admissible functional moves `Q_β` off the
ruled base is the single scalar `F = w₃ / y₃ᴰ` — there is no series, no `u`, no
rung: the D-frame "ladder", on the functional side, is one number.

## What is proved here

1. `one_lt_factor_iff` — **a factor above 1 is exactly a transfer of trace
   weight OUT of the 2-dimensional block, below its convention-D value**:
   `1 < F ↔ w₂₁ < y₂₁ᴰ`.
2. `factor_mem` — for a **positive** normalised admissible trace
   (`w₃, w₂₁ ≥ 0`), `0 ≤ F ≤ (q²+1)²/(q⁴+1)`; the ceiling is attained iff
   `w₂₁ = 0`, i.e. at the augmentation (`factor_eq_ceiling_iff`).
3. `ceiling_lt_two` — the ceiling `1 + 2q²/(q⁴+1)` is **strictly below 2**
   for every `q` with `q² ≠ 1`, and `one_lt_ceiling` — strictly above 1 for
   `q ≠ 0`.
4. `assembly_lt_two` — composed with **any** further multiplicative factor
   `L ≤ 1` (every ladder this corpus can form: `LadderFactorBound`,
   `LadderUniformBound`), the whole correction on `Δ_S` is `< 2`.

## What this does NOT claim (read before citing)

* It is **not** an exclusion of the ruled-base requirement. At the proton pin
  the ceiling is `≈ 1.9786` and `F_required ≈ 1.7592` sits **inside**
  `(1, ceiling)`. The probe
  `computations/qbeta/qbeta_d_frame_functional_factor_ceiling_probe.py` reports
  this as a scope-(a) fact, not a refutation.
* Positivity of the weights is a **hypothesis** (the reading-3 Frobenius
  positivity the owner selected on 2026-09-12), not a theorem of the
  framework. Without it `F` is unbounded and the statement says nothing.
* It does **not** say which `w₂₁` is right. Only two admissible *Markov*
  points exist (`ConventionDAdmissibleRoots`), giving `F ∈ {1, ceiling}`;
  every interior `F`, `F_required` included, is reached only by a non-Markov
  trace with a free weight — one parameter against one anchor, i.e. a fit,
  forbidden by §NO FITTING. Nothing here selects a weight.
* It covers the element `Δ_S` only. The element side (`qou-99qc`) is untouched.

Base ring: the algebraic identities hold over a generic `[Field R]`; the
inequalities need an ordered field (`IsStrictOrderedRing`), per AGENTS.md §7c.
Nothing archimedean (no `Real.sqrt`, no pin) is used.

-- Ref: [manuscript] bean `qou-cds1`, entries 2026-09-14 and 2026-10-10 (2);
--      Lean `QOU/QBeta/DecayBlockCarrier.lean`, `QOU/QBeta/LadderUniformBound.lean`.
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors",
--      Invent. Math. 92 (1988) 349-383.
-/
import Mathlib.Algebra.Order.Field.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace QOU.QBeta.DFrameFunctionalFactorCeiling

section Generic

variable {R : Type*} [Field R]

/-- The `(3)`-block weight of the ruled functional, `y₃(z_D)`. -/
def y3D (q : R) : R := (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2

/-- The `(2,1)`-block weight of the ruled functional, `y₂₁(z_D)`. -/
def y21D (q : R) : R := q ^ 2 / (q ^ 2 + 1) ^ 2

/-- The functional-side ceiling, `1 / y₃(z_D)`. -/
def ceiling (q : R) : R := (q ^ 2 + 1) ^ 2 / (q ^ 4 + 1)

/-- The ruled functional is normalised: `y₃ᴰ + 2·y₂₁ᴰ = 1`. -/
theorem y3D_add_two_y21D {q : R} (hq2 : q ^ 2 + 1 ≠ 0) :
    y3D q + 2 * y21D q = 1 := by
  have hD : (q ^ 2 + 1) ^ 2 ≠ 0 := pow_ne_zero 2 hq2
  unfold y3D y21D
  rw [← mul_div_assoc, ← add_div, div_eq_one_iff_eq hD]
  ring

/-- The ceiling, written as `1` plus the `(2,1)`-block share it reclaims. -/
theorem ceiling_eq {q : R} (h4 : q ^ 4 + 1 ≠ 0) :
    ceiling q = 1 + 2 * q ^ 2 / (q ^ 4 + 1) := by
  unfold ceiling
  rw [one_add_div h4]
  ring

/-- On the admissible line the value on `Δ_S` factorises through the ruled
value: `w₃·x = (w₃ / y₃ᴰ)·(y₃ᴰ·x)`. This is the sense in which the functional
side contributes exactly one multiplicative scalar. -/
theorem value_factorises {q : R} (hq2 : q ^ 2 + 1 ≠ 0) (h4 : q ^ 4 + 1 ≠ 0)
    (w3 x : R) : w3 * x = (w3 / y3D q) * (y3D q * x) := by
  have hy : y3D q ≠ 0 := by
    unfold y3D
    exact div_ne_zero h4 (pow_ne_zero 2 hq2)
  field_simp

end Generic

section Ordered

variable {R : Type*} [Field R] [LinearOrder R] [IsStrictOrderedRing R] {q : R}

theorem q4_add_one_pos : 0 < q ^ 4 + 1 := by positivity

theorem q2_add_one_pos : 0 < q ^ 2 + 1 := by positivity

theorem y3D_pos : 0 < y3D q := by
  unfold y3D
  have := (q4_add_one_pos (q := q))
  positivity

/-- `ceiling · y₃ᴰ = 1`. -/
theorem ceiling_mul_y3D : ceiling q * y3D q = 1 := by
  unfold ceiling y3D
  have h4 := (q4_add_one_pos (q := q)).ne'
  have h2 := (pow_pos (q2_add_one_pos (q := q)) 2).ne'
  field_simp

/-- **The ceiling is strictly above 1** whenever `q ≠ 0`: the augmentation does
supply a factor above 1 over the ruled functional. -/
theorem one_lt_ceiling (hq : q ≠ 0) : 1 < ceiling q := by
  rw [ceiling_eq (q4_add_one_pos (q := q)).ne']
  have hq2 : 0 < q ^ 2 := by positivity
  have : 0 < 2 * q ^ 2 / (q ^ 4 + 1) := by
    have := (q4_add_one_pos (q := q)); positivity
  linarith

/-- **The ceiling is strictly below 2** whenever `q² ≠ 1`, because
`2q² < q⁴ + 1 ↔ (q² − 1)² > 0`. -/
theorem ceiling_lt_two (hq : q ^ 2 ≠ 1) : ceiling q < 2 := by
  unfold ceiling
  have h4 := (q4_add_one_pos (q := q))
  rw [div_lt_iff₀ h4]
  have hsq : 0 < (q ^ 2 - 1) ^ 2 := by
    have : q ^ 2 - 1 ≠ 0 := sub_ne_zero.mpr hq
    positivity
  nlinarith [hsq]

/-- **(1) A factor above 1 is exactly a transfer of weight out of the
2-dimensional block, below its convention-D value.** -/
theorem one_lt_factor_iff (w3 w21 : R) (hn : w3 + 2 * w21 = 1) :
    1 < w3 / y3D q ↔ w21 < y21D q := by
  have hy := (y3D_pos (q := q))
  have hsum := y3D_add_two_y21D (q2_add_one_pos (q := q)).ne'
  rw [one_lt_div hy]
  constructor <;> intro h <;> linarith

/-- **(2) For a positive normalised admissible functional the factor lies in
`[0, ceiling]`.** -/
theorem factor_mem (w3 w21 : R) (h3 : 0 ≤ w3) (h21 : 0 ≤ w21)
    (hn : w3 + 2 * w21 = 1) :
    0 ≤ w3 / y3D q ∧ w3 / y3D q ≤ ceiling q := by
  have hy := (y3D_pos (q := q))
  refine ⟨div_nonneg h3 hy.le, ?_⟩
  have hw : w3 ≤ 1 := by linarith
  have hc : ceiling q = 1 / y3D q := by
    rw [eq_div_iff hy.ne']
    exact ceiling_mul_y3D
  rw [hc]
  exact div_le_div_of_nonneg_right hw hy.le

/-- **The ceiling is attained exactly at the augmentation** (`w₂₁ = 0`). -/
theorem factor_eq_ceiling_iff (w3 w21 : R) (hn : w3 + 2 * w21 = 1) :
    w3 / y3D q = ceiling q ↔ w21 = 0 := by
  have hy := (y3D_pos (q := q))
  have hc : ceiling q = 1 / y3D q := by
    rw [eq_div_iff hy.ne']
    exact ceiling_mul_y3D
  rw [hc, div_left_inj' hy.ne']
  constructor <;> intro h <;> linarith

/-- **(3)+(4) The whole correction on `Δ_S` is below 2.** A positive normalised
admissible functional composed with any further factor `L ≤ 1` (no sign needed) — every
multiplicative ladder this corpus can form is of that kind
(`LadderFactorBound`, `LadderUniformBound`) — moves `Q_β` off the ruled base by
strictly less than a factor of 2, for every `q` with `q² ≠ 1`. -/
theorem assembly_lt_two (hq : q ^ 2 ≠ 1) (w3 w21 L : R) (h3 : 0 ≤ w3)
    (h21 : 0 ≤ w21) (hn : w3 + 2 * w21 = 1) (hL1 : L ≤ 1) :
    (w3 / y3D q) * L < 2 := by
  obtain ⟨hF0, hF1⟩ := factor_mem (q := q) w3 w21 h3 h21 hn
  have hc := ceiling_lt_two hq
  have : (w3 / y3D q) * L ≤ w3 / y3D q := mul_le_of_le_one_right hF0 hL1
  linarith

end Ordered

end QOU.QBeta.DFrameFunctionalFactorCeiling
