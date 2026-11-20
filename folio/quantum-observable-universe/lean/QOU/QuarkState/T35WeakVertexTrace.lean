/-
# The `T(3,5)` weak-vertex word under convention D

Bean `qou-99qc`, route R3 of 2026-11-20. `predicted-spectra/beta-decay-skein-properties`
claims that the weak vertex form factor `𝒲(q) = tr_Markov((σ₁σ₂)⁵)` lies in `ℤ[q^{±1/2}]`.
This file computes it under convention D, using the neutron weight space `W₋ = (3) ⊕ (2,1)`
of `IsospinRaisingRoundTrip` (on which `σᵢ` satisfy the `H₃(q)` relations, proved there).

* `trace_T35_Wm`: `tr_{W₋}((σ₁σ₂)⁵) = q¹⁰ − 1`. With `χ₍₃₎ = q¹⁰` this gives `χ₍₂,₁₎ = −1`.
* `zD_T35`: the convention-D trace `y₃χ₍₃₎ + y₂₁χ₍₂,₁₎` (`y₁₁₁ = 0`) is
  `q²(q¹² + q⁸ − 1)/(q² + 1)²`, whose denominator `(q²+1)²` is not a monomial: the claimed
  membership in `ℤ[q^{±1/2}]` fails under convention D (it was a convention-C statement).

Generic `[Field K]`, no `ℝ`, no `sorry`.

-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.QuarkState.IsospinRaisingRoundTrip

namespace QOU.QuarkState.T35WeakVertexTrace

open Matrix QOU.QuarkState.IsospinRaisingRoundTrip

variable {K : Type*} [Field K] {q : K}

theorem sm12_eq (hq : q ≠ 0) :
    sm1 q * sm2 q = !![0, 0, 1; q, 0, q - q⁻¹; 0, q, q ^ 2 - 1] := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [sm1, sm2, Matrix.mul_apply, Fin.sum_univ_three] <;> field_simp <;> ring

theorem trace_T35_Wm (hq : q ≠ 0) : trace ((sm1 q * sm2 q) ^ 5) = q ^ 10 - 1 := by
  rw [sm12_eq hq]
  simp [pow_succ, Matrix.mul_fin_three, Matrix.trace_fin_three]
  field_simp
  ring

/-- **Convention D on `(σ₁σ₂)⁵`.** `χ₍₂,₁₎ = tr_{W₋} − χ₍₃₎ = −1`. -/
theorem zD_T35 (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0) :
    (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 * q ^ 10 +
        q ^ 2 / (q ^ 2 + 1) ^ 2 * (trace ((sm1 q * sm2 q) ^ 5) - q ^ 10) =
      q ^ 2 * (q ^ 12 + q ^ 8 - 1) / (q ^ 2 + 1) ^ 2 := by
  rw [trace_T35_Wm hq]
  field_simp
  ring

end QOU.QuarkState.T35WeakVertexTrace

#print axioms QOU.QuarkState.T35WeakVertexTrace.trace_T35_Wm
#print axioms QOU.QuarkState.T35WeakVertexTrace.zD_T35
