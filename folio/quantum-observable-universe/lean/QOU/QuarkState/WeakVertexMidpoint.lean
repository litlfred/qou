/-
# The weak vertex is a scalar multiple of the symmetric crossing `½(σ + σ⁻¹)`

Bean `qou-hlx7` (epic `qou-qs0e`), asked for by the n–p splitting thread. The corpus's
mixed u–d crossing in `HeckeRational.crossing` is set to the symmetric combination
`½(σ + σ⁻¹) = σ − h/2` (`h = q − q⁻¹`). This file proves that the one-sided weak vertex
of `OneSidedWeakVertex.lean` / `LeftLineDefinition.lean` is that same element up to a
scalar:

* `grading_eq_midpoint`: the chirality grading `J = P₊ − P₋` equals
  `(2/(q + q⁻¹)) · ½(s + s⁻¹)`. Pure algebra, no Hecke relation used.
* `oneSidedL_eq_midpoint`: the L-only flip is `(2/(q² + 1)) · ½(s + s⁻¹)`.
* `oneSidedR_eq_midpoint`: the R-only flip is `(2q²/(q² + 1)) · ½(s + s⁻¹)`.
* `weakVertex_eq_midpoint_of_one_lt`: for `1 < |q|` (the regime of the substrate
  `q₀ > 1`), `weakVertex q σ = (2/(q² + 1)) · ½(σ + σ⁻¹)`.

What this does and does not say. It is an identity between elements: the hand-set
crossing and the weak vertex span the same line, and differ by the scalar fixed by
`W² = q⁻²`. It does NOT derive the strong u–d crossing from the weak vertex; using one for
the other is an identification, and the weak vertex is itself conditional on D-H3
(bean `qou-hlx7`, open).

Base ring (§7c): generic `[Field K]`, `[Ring A] [Algebra K A]`; the last lemma needs the
order on `K` only because `weakVertex` chooses its line by `|q|`.

-- Ref: [kazhdan-lusztig1979] https://doi.org/10.1007/BF01390031
-/
import QOU.QuarkState.LeftLineDefinition

namespace QOU.QuarkState.WeakVertexMidpoint

open QOU.QuarkState.Helicity QOU.QuarkState.OneSidedWeakVertex

section Abstract

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]
variable {q : K} {s : A}

/-- The symmetric crossing `½(s + s⁻¹)`, with `s⁻¹ = flip q s = s − h`. -/
noncomputable def symCrossing (q : K) (s : A) : A := (2 : K)⁻¹ • (s + Helicity.flip q s)

/-- `½(s + s⁻¹) = s − h/2`. -/
theorem symCrossing_eq (h2 : (2 : K) ≠ 0) (q : K) (s : A) :
    symCrossing q s = s - ((q - q⁻¹) / 2) • (1 : A) := by
  unfold symCrossing Helicity.flip
  have : s + (s - (q - q⁻¹) • (1 : A)) = (2 : K) • s - (q - q⁻¹) • (1 : A) := by
    rw [two_smul]; abel
  rw [this, smul_sub, smul_smul, inv_mul_cancel₀ h2, one_smul, smul_smul, inv_mul_eq_div]

/-- **The grading is a multiple of the symmetric crossing:** `J = (2/[2]) · ½(s + s⁻¹)`. -/
theorem grading_eq_midpoint (h2 : (2 : K) ≠ 0) (q : K) (s : A) :
    grading q s = (2 * (q + q⁻¹)⁻¹) • symCrossing q s := by
  unfold grading Pp Pm symCrossing Helicity.flip
  rw [← smul_sub, smul_smul, mul_comm (2 : K), mul_assoc, mul_inv_cancel₀ h2, mul_one]
  congr 1
  rw [sub_smul]
  abel

/-- **The L-only flip is `(2/(q² + 1)) · ½(s + s⁻¹)`.** -/
theorem oneSidedL_eq_midpoint (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0)
    (hs : IsLetter q s) :
    oneSidedL q s = (2 / (q ^ 2 + 1)) • symCrossing q s := by
  rw [oneSidedL_eq hq hq2 hs, grading_eq_midpoint h2, smul_smul]
  congr 1
  have hq21 : q ^ 2 + 1 ≠ 0 := by
    intro h0; apply hq2
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this, h0, zero_div]
  field_simp

/-- **The R-only flip is `(2q²/(q² + 1)) · ½(s + s⁻¹)`.** -/
theorem oneSidedR_eq_midpoint (h2 : (2 : K) ≠ 0) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0)
    (hs : IsLetter q s) :
    oneSidedR q s = (2 * q ^ 2 / (q ^ 2 + 1)) • symCrossing q s := by
  rw [oneSidedR_eq hq hq2 hs, grading_eq_midpoint h2, smul_smul]
  congr 1
  have hq21 : q ^ 2 + 1 ≠ 0 := by
    intro h0; apply hq2
    have : q + q⁻¹ = (q ^ 2 + 1) / q := by field_simp
    rw [this, h0, zero_div]
  field_simp

end Abstract

section Regime

variable {K A : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  [Ring A] [Algebra K A]
variable {q : K} {σ : A}

/-- **For `1 < |q|`, the weak vertex is `(2/(q² + 1)) · ½(σ + σ⁻¹)`.** -/
theorem weakVertex_eq_midpoint_of_one_lt (h : 1 < |q|) (hq : q ≠ 0) (hq2 : q + q⁻¹ ≠ 0)
    (hs : IsLetter q σ) :
    LeftLine.weakVertex q σ = (2 / (q ^ 2 + 1)) • symCrossing q σ := by
  unfold LeftLine.weakVertex
  rw [if_pos h, oneSidedL_eq_midpoint two_ne_zero hq hq2 hs]

/-- For `|q| ≤ 1` the weak vertex is `(2q²/(q² + 1)) · ½(σ + σ⁻¹)`. -/
theorem weakVertex_eq_midpoint_of_not_one_lt (h : ¬ 1 < |q|) (hq : q ≠ 0)
    (hq2 : q + q⁻¹ ≠ 0) (hs : IsLetter q σ) :
    LeftLine.weakVertex q σ = (2 * q ^ 2 / (q ^ 2 + 1)) • symCrossing q σ := by
  unfold LeftLine.weakVertex
  rw [if_neg h, oneSidedR_eq_midpoint two_ne_zero hq hq2 hs]

end Regime

end QOU.QuarkState.WeakVertexMidpoint
