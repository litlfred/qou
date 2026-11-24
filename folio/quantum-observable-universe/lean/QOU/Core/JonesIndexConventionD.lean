/-
Copyright (c) 2026 litlfred. All rights reserved.
Released under Apache 2.0 license.
-/
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Algebra.Field.Basic
import Mathlib.Algebra.Order.Ring.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Linarith

/-!
# Convention D is the Jones / Temperley–Lieb Markov trace, with index `[2]_q²`

Let `σ` be a Hecke generator with eigenvalues `q` and `-q⁻¹`, and let
`e = (q + q⁻¹)⁻¹ (q - σ)` be the projection onto the `-q⁻¹` eigenspace. A Markov
trace `tr (x σ) = z tr x` then gives `tr (x e) = τ_J tr x` with
`τ_J = (q - z)/(q + q⁻¹)` (`trace_mul_proj`). This holds over any field.

At convention D, `z = q³/(q² + 1)`:

* `jonesParam_convD`: `τ_J = q² / (q² + 1)²`;
* `jonesIndex_convD`: `1/τ_J = (q + q⁻¹)²`, i.e. the index is `[2]_q²`;
* `four_le_jonesIndex`: over any linearly ordered field, for `q ≠ 0` (in particular `q > 0`),
  the index is at least `4`. Over `ℝ` this is Jones' range in which the Markov trace on the
  Temperley–Lieb tower is positive.

The positivity theorem itself (Jones 1983) is cited, not formalised here.
Base ring (§7c): generic `[Field K]`, with `[LinearOrder K] [IsStrictOrderedRing K]` for the
order bound; no `ℝ` import.

No `sorry`.

## References
- [jones1983] Jones, *Index for subfactors*, Invent. Math. 72 (1983), 1–25.
- [leitner2026] §1 Categorical foundations.
-/
-- Ref: [jones1983] Jones, Index for subfactors, Invent. Math. 72 (1983) 1–25
-- Ref: [leitner2026] §1 Categorical foundations

namespace QOU.QuantumObservableUniverse.JonesIndex

section Generic

variable {K : Type*} [Field K] {B : Type*} [Ring B] [Algebra K B]

/-- A Markov trace evaluated against the projection `e = (q + q⁻¹)⁻¹ (q - σ)`. -/
theorem trace_mul_proj (tr : B →ₗ[K] K) (σ x : B) (q z : K)
    (hM : tr (x * σ) = z * tr x) :
    tr (x * ((q + q⁻¹)⁻¹ • (q • (1 : B) - σ))) = (q - z) / (q + q⁻¹) * tr x := by
  rw [Algebra.mul_smul_comm, mul_sub, Algebra.mul_smul_comm, mul_one, map_smul, map_sub,
    map_smul, hM, smul_eq_mul, smul_eq_mul]
  ring

/-- At convention D the Jones parameter is `q² / (q² + 1)²`. -/
theorem jonesParam_convD (q : K) (hq : q ≠ 0) (h : q ^ 2 + 1 ≠ 0) :
    (q - q ^ 3 / (q ^ 2 + 1)) / (q + q⁻¹) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have h' : q + q⁻¹ ≠ 0 := by
    intro h0
    apply h
    have := congrArg (· * q) h0
    simp only [add_mul, inv_mul_cancel₀ hq, zero_mul] at this
    rw [sq]; exact this
  field_simp
  ring

/-- The index `1/τ_J` at convention D is `[2]_q² = (q + q⁻¹)²`. -/
theorem jonesIndex_convD (q : K) (hq : q ≠ 0) (h : q ^ 2 + 1 ≠ 0) :
    ((q ^ 2 + 1) ^ 2 / q ^ 2) = (q + q⁻¹) ^ 2 := by
  field_simp

end Generic

/-- Over any linearly ordered field, for nonzero `q` (in particular `0 < q`),
the convention-D index `(q + q⁻¹)²` is at least `4`. -/
theorem four_le_jonesIndex {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
    (q : K) (hq : q ≠ 0) : 4 ≤ (q + q⁻¹) ^ 2 := by
  have h1 : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
  nlinarith [sq_nonneg (q - q⁻¹)]

end QOU.QuantumObservableUniverse.JonesIndex
