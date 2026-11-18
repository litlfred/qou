import Mathlib.Tactic

/-!
# Untwisted geometric monodromy cannot be the substrate monodromy

Bean `qou-d0qq`, step 1 of the framework-side plan
(`docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md` follow-up, agent `fw-conn`).

The Gauss–Manin local system of an algebraic family has **quasi-unipotent** local
monodromy: every eigenvalue `λ` of a lasso monodromy satisfies `(λ^k − 1)^m = 0` for some
`k, m ≥ 1`; for the colour cubic's root map the fibre is three points and the monodromy is a
permutation, so `λ^k = 1` outright. The framework's Step-2 monodromy generators have the
Hecke eigenvalues `q₀` and `−q₀⁻¹` with the real substrate parameter `q₀ > 1`. These are
incompatible over any linearly ordered field, so **no untwisted geometric monodromy of a
framework family can be the substrate connection**: the deformation `1 ↦ q₀` must enter as
a twist (a rank-one local system with non-unitary exponent), which is exactly what the
Knizhnik–Zamolodchikov side supplies through the level (`KZLevelFromHeckeNormalisation`).

Scope-(b): the invariant is finiteness/quasi-unipotence of geometric monodromy, and the
statement below is the only arithmetic it needs. It says nothing about *twisted*
Gauss–Manin systems, which are the surviving candidate (C3′ of the plan).

Base ring: a linearly ordered field; the reals are one instance. No archimedean analysis.
-/

namespace QOU.Mass.UntwistedMonodromyPrune

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- A finite-order eigenvalue is never a real number greater than one. -/
theorem finite_order_eigen_ne_gt_one {l : K} (hl : 1 < l) {k : ℕ} (hk : 1 ≤ k) :
    l ^ k ≠ 1 := by
  intro h
  have : 1 < l ^ k := one_lt_pow₀ hl (by omega)
  rw [h] at this
  exact lt_irrefl _ this

/-- Quasi-unipotence `(λ^k − 1)^m = 0` (with `m ≥ 1`) already forces `λ^k = 1` in a field,
so a quasi-unipotent eigenvalue is never `> 1` either. -/
theorem quasi_unipotent_eigen_ne_gt_one {l : K} (hl : 1 < l) {k m : ℕ} (hk : 1 ≤ k)
    (hm : 1 ≤ m) : (l ^ k - 1) ^ m ≠ 0 := by
  intro h
  have h0 : l ^ k - 1 = 0 := pow_eq_zero_iff (by omega) |>.mp h
  exact finite_order_eigen_ne_gt_one hl hk (sub_eq_zero.mp h0)

/-- The negative Hecke eigenvalue `−q⁻¹` is not of finite order either (for `q > 1`):
its `k`-th power has absolute value `q^{−k} < 1`. -/
theorem neg_inv_eigen_ne_one {q : K} (hq : 1 < q) {k : ℕ} (hk : 1 ≤ k) :
    (-q⁻¹) ^ k ≠ 1 := by
  intro h
  have hq0 : 0 < q := lt_trans zero_lt_one hq
  have habs : |(-q⁻¹) ^ k| = (q⁻¹) ^ k := by
    rw [abs_pow, abs_neg, abs_inv, abs_of_pos hq0]
  have hlt : (q⁻¹) ^ k < 1 := by
    have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
    have h0 : 0 < q⁻¹ := inv_pos.mpr hq0
    exact pow_lt_one₀ h0.le this (by omega)
  rw [h, abs_one] at habs
  rw [← habs] at hlt
  exact lt_irrefl _ hlt

/-- Subtracting one from a positive power of a strictly-greater-than-one element yields a nonzero difference (`qou-ddo8`). -/
theorem finite_order_eigen_sub_one_ne_zero {l : K} (hl : 1 < l) {k : ℕ} (hk : 1 ≤ k) :
    l ^ k - 1 ≠ 0 :=
  sub_ne_zero.mpr (finite_order_eigen_ne_gt_one hl hk)

end QOU.Mass.UntwistedMonodromyPrune
