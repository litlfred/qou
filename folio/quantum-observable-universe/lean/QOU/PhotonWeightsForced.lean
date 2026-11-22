import Mathlib.LinearAlgebra.LinearIndependent.Defs
import Mathlib.Algebra.Algebra.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Data.Fin.VecNotation
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Ring

namespace QOU.PhotonWeightsForced

variable {K A : Type*} [Field K] [Ring A] [Algebra K A]

/-- Two V-only photons with identity coefficients `c, d` and `V` coefficients `e, f`
multiply to `cd + (cf + ed) V + ef V²`. -/
theorem vOnly_mul (V : A) (c d e f : K) :
    (c • (1 : A) + e • V) * (d • (1 : A) + f • V) =
      (c * d) • (1 : A) + (c * f + e * d) • V + (e * f) • (V * V) := by
  simp only [add_mul, mul_add, smul_mul_smul_comm, one_mul, mul_one, add_smul, mul_smul]
  abel

/-- **Coefficient matching.** If `1, V, V²` are linearly independent and the product of two
V-only photons equals `1 + s V + p V²`, then `cd = 1`, `cf + ed = s` and `ef = p`. -/
theorem coeffs_of_eq (V : A) (hind : LinearIndependent K ![(1 : A), V, V * V])
    (s p c d e f : K)
    (h : (c • (1 : A) + e • V) * (d • (1 : A) + f • V) = (1 : A) + s • V + p • (V * V)) :
    c * d = 1 ∧ c * f + e * d = s ∧ e * f = p := by
  rw [vOnly_mul] at h
  have h0 : ∑ i, ![c * d - 1, c * f + e * d - s, e * f - p] i • ![(1 : A), V, V * V] i = 0 := by
    simp only [Fin.sum_univ_three, Matrix.cons_val_zero, Matrix.cons_val_one,
      Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, sub_smul, one_smul]
    rw [← sub_eq_zero] at h
    rw [← h]; abel
  have := (Fintype.linearIndependent_iff.mp hind) _ h0
  refine ⟨?_, ?_, ?_⟩
  · have := this 0; simpa [sub_eq_zero] using this
  · have := this 1; simpa [sub_eq_zero] using this
  · have := this 2; simpa [sub_eq_zero] using this

/-- **The weights are the roots of `x² − h²x − h²`.** With `h = q − q⁻¹`, if `e + f = h²` and
`e f = −h²` then `{e, f} = {q h, −q⁻¹ h}`. -/
theorem weights_of_sum_prod (q e f : K) (hq : q ≠ 0)
    (hs : e + f = (q - q⁻¹) ^ 2) (hp : e * f = -(q - q⁻¹) ^ 2) :
    (e = q * (q - q⁻¹) ∧ f = -q⁻¹ * (q - q⁻¹)) ∨
      (e = -q⁻¹ * (q - q⁻¹) ∧ f = q * (q - q⁻¹)) := by
  have hfac : (e - q * (q - q⁻¹)) * (e + q⁻¹ * (q - q⁻¹)) = 0 := by
    have hf : f = (q - q⁻¹) ^ 2 - e := by linear_combination hs
    subst hf
    have hqi : q * q⁻¹ = 1 := mul_inv_cancel₀ hq
    linear_combination (-1 : K) * hp - (q - q⁻¹) ^ 2 * hqi
  rcases mul_eq_zero.mp hfac with h1 | h1
  · left
    have he : e = q * (q - q⁻¹) := by linear_combination h1
    refine ⟨he, ?_⟩
    linear_combination hs - he
  · right
    have he : e = -q⁻¹ * (q - q⁻¹) := by linear_combination h1
    refine ⟨he, ?_⟩
    linear_combination hs - he

/-- **The V-only factorisation of `V³` is forced.** Suppose `1, V, V²` are linearly independent
and `V³ = 1 + h²V − h²V²` (the cubic `vertex_cube` / `borromeanV3A_eq_one_add_h_sq_V_sub_V_sq`).
If `V³` is a product of two V-only photons `(c + eV)(d + fV)`, then `cd = 1`; and for photons of
norm `1` (`c = d = 1`) the weights are `{q h, −q⁻¹ h}` up to order. -/
theorem vOnly_factorisation_forced (V : A) (q : K) (hq : q ≠ 0)
    (hind : LinearIndependent K ![(1 : A), V, V * V])
    (hcube : V * V * V = (1 : A) + (q - q⁻¹) ^ 2 • V + (-(q - q⁻¹) ^ 2) • (V * V))
    (c d e f : K) (hprod : (c • (1 : A) + e • V) * (d • (1 : A) + f • V) = V * V * V) :
    c * d = 1 ∧
      (c = 1 → d = 1 →
        ((e = q * (q - q⁻¹) ∧ f = -q⁻¹ * (q - q⁻¹)) ∨
          (e = -q⁻¹ * (q - q⁻¹) ∧ f = q * (q - q⁻¹)))) := by
  rw [hcube] at hprod
  obtain ⟨h0, h1, h2⟩ := coeffs_of_eq V hind _ _ c d e f hprod
  refine ⟨h0, fun hc hd => ?_⟩
  subst hc; subst hd
  exact weights_of_sum_prod q e f hq (by simpa [add_comm] using h1) (by simpa using h2)

end QOU.PhotonWeightsForced
