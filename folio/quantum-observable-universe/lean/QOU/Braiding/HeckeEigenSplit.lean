import Mathlib.LinearAlgebra.Matrix.Charpoly.Eigs
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.Algebra.Polynomial.Splits
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp

/-!
# A Hecke generator's determinant and trace from its two eigenvalues

A matrix `A` with `A² = h·A + 1`, `h = q − q⁻¹`, has spectrum in `{q, −q⁻¹}`.
When its characteristic polynomial splits there are `d₊, d₋` with
`d₊ + d₋ = dim`, `det A = q^{d₊}(−q⁻¹)^{d₋}` and `tr A = d₊q − d₋q⁻¹`.
So the determinant exponent `c₁ = d₊ − d₋` is fixed by the trace:
`c₁·(q + q⁻¹) = 2·tr A − dim·(q − q⁻¹)`.

For an irreducible `V_λ` of `H_n(q)` this says `c₁(V_λ)` is read off the
character. At `q = 1` it is `χ^λ(transposition)`; that `c₁` does not move with
`q` is the Tits deformation argument (cited, not formalized here). Bean qou-078y.
-/

namespace QOU.Braiding.HeckeEigenSplit

open Matrix Polynomial

variable {n K : Type*} [Fintype n] [DecidableEq n] [Field K]

/-- Every eigenvalue `r` of a Hecke generator satisfies `r² = h·r + 1`. -/
theorem eigen_quadratic (A : Matrix n n K) (h : K) (hA : A * A = h • A + 1)
    {r : K} (hr : r ∈ spectrum K A) : r * r = h * r + 1 := by
  rw [Matrix.mem_spectrum_iff_isRoot_charpoly, IsRoot, Matrix.eval_charpoly] at hr
  obtain ⟨v, hv0, hv⟩ := Matrix.exists_mulVec_eq_zero_iff.mpr hr
  have hAv : A *ᵥ v = r • v := by
    have e : (scalar n r - A) *ᵥ v = r • v - A *ᵥ v := by
      rw [Matrix.sub_mulVec]; congr 1; ext i; simp [Matrix.mulVec_diagonal]
    rw [e, sub_eq_zero] at hv
    exact hv.symm
  have h2 : (A * A) *ᵥ v = (r * r) • v := by
    rw [← Matrix.mulVec_mulVec, hAv, Matrix.mulVec_smul, hAv, smul_smul]
  rw [hA, Matrix.add_mulVec, Matrix.smul_mulVec, hAv, Matrix.one_mulVec, smul_smul] at h2
  have h3 : (h * r + 1 - r * r) • v = 0 := by
    rw [sub_smul, add_smul, one_smul, h2, sub_self]
  rcases smul_eq_zero.mp h3 with h4 | h4
  · linear_combination -h4
  · exact absurd h4 hv0

/-- **Determinant and trace from the two eigenvalues.** -/
theorem det_trace_split (A : Matrix n n K) (q : K) (hq : q ≠ 0) (hsep : q ≠ -q⁻¹)
    (hA : A * A = (q - q⁻¹) • A + 1) (hs : A.charpoly.Splits (RingHom.id K)) :
    ∃ dp dm : ℕ, dp + dm = Fintype.card n ∧ A.det = q ^ dp * (-q⁻¹) ^ dm ∧
      A.trace = dp * q - dm * q⁻¹ := by
  classical
  set R := A.charpoly.roots with hR
  have hmem : ∀ r ∈ R, r = q ∨ r = -q⁻¹ := by
    intro r hr
    have hroot : IsRoot A.charpoly r := (mem_roots (A.charpoly_monic.ne_zero)).mp hr
    have := eigen_quadratic A _ hA ((Matrix.mem_spectrum_iff_isRoot_charpoly).mpr hroot)
    have hfac : (r - q) * (r + q⁻¹) = 0 := by
      field_simp at this ⊢; linear_combination this
    rcases mul_eq_zero.mp hfac with h | h
    · exact Or.inl (sub_eq_zero.mp h)
    · exact Or.inr (eq_neg_of_add_eq_zero_left h)
  have hsplitR : R = Multiset.replicate (R.count q) q
      + Multiset.replicate (R.count (-q⁻¹)) (-q⁻¹) := by
    rw [← Multiset.filter_eq', ← Multiset.filter_eq']
    conv_lhs => rw [← Multiset.filter_add_not (· = q) R]
    congr 1
    refine Multiset.filter_congr fun r hr => ?_
    rcases hmem r hr with h | h
    · subst h; simp [hsep]
    · subst h; simp [Ne.symm hsep]
  have hcard : R.card = Fintype.card n := by
    rw [hR, splits_iff_card_roots.mp hs, Matrix.charpoly_natDegree_eq_dim]
  obtain ⟨a, b, hab⟩ : ∃ a b : ℕ,
      R = Multiset.replicate a q + Multiset.replicate b (-q⁻¹) := ⟨_, _, hsplitR⟩
  refine ⟨a, b, ?_, ?_, ?_⟩
  · rw [← hcard, hab]; simp
  · rw [det_eq_prod_roots_charpoly_of_splits hs, ← hR, hab]; simp
  · rw [trace_eq_sum_roots_charpoly_of_splits hs, ← hR, hab]
    simp [sub_eq_add_neg, nsmul_eq_mul]

/-- **`c₁` is fixed by the character:** `(d₊ − d₋)(q + q⁻¹) = 2·tr A − dim·(q − q⁻¹)`. -/
theorem c1_from_trace (q t : K) (dp dm N : ℕ) (hN : dp + dm = N)
    (ht : t = dp * q - dm * q⁻¹) :
    ((dp : K) - dm) * (q + q⁻¹) = 2 * t - N * (q - q⁻¹) := by
  subst ht hN; push_cast; ring

end QOU.Braiding.HeckeEigenSplit
