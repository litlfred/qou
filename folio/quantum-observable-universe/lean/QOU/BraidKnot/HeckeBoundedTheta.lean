import QOU.BraidKnot.HeckeBoundedSeminormalWeight
import QOU.BraidKnot.HeckeSeminormalWeight

/-!
# The twist scalar `θ_λ²` on the bounded presentation

The last piece of the Jucys–Murphy chain begun in `HeckeBoundedJucysMurphy.lean`: from the
per-element content eigenvalues to the full twist acting by `θ_λ² = q^{2c(λ)}`.

## Nothing about `prod_jmEigen` needed porting

`HeckeSeminormalWeight.prod_jmEigen` — that the content eigenvalues multiply to `θ_λ²` — mentions
no `HeckeGenerators` at all.  It is a statement about the eigenvalue *function* and the combinatorics
of `cells`, so the bounded versions below reuse it unchanged.  Only the two theorems that actually
touch a presentation had to move.

## The payoff, and an independent check

For `λ = (2,1)` the content sum is `0 + 1 + (−1) = 0`, so `θ_λ² = q⁰ = 1`: the full twist of `B₃`
acts **trivially** on the seminormal vector.  That is a falsifiable prediction, and
`stdTwo_fullTwist_eq_one` confirms it by a completely different route — a direct matrix computation
that `(σ₀σ₁)³ = 1`, with no Jucys–Murphy input.

This mirrors the falsifiability check `HeckeSeminormalWeight` runs for the one-row block against
`theta_single_row_sq`, but on a 2-dimensional module — which the unbounded presentation cannot host
at all (`stdTwo_no_stable_extension`).
-/

namespace QOU.BraidKnot.Hecke

open Finset Matrix QOU.MathlibExt.QPartitionCombinatorics QOU.BraidKnot.Keystone

variable {R : Type*} [Field R] {A : Type*} [Ring A] [Algebra R A] {q : R} {n : ℕ}
variable {V : Type*} [AddCommGroup V] [Module A V] [Module R V] [IsScalarTower R A V]

/-! ## §1  The general statements -/

/-- **The full twist acts by `θ_λ²`** on a bounded presentation.  `prod_jmEigen` is reused verbatim
— it never mentioned a presentation. -/
theorem fullTwistB_smul_eq_theta_sq (H : HeckeGeneratorsBelow R A q n) (hq : q ≠ 0)
    {l : Partition} {m : ℕ} (hm : m < n) (e : Fin (m + 1) ≃ {c // c ∈ cells l}) (v : V)
    (hw : IsJMWeightB H v (jmEigen q e) (m + 1)) :
    (deltaB H m ^ (m + 1)) • v = ((theta q l) ^ 2) • v := by
  rw [fullTwistB_smul_of_weight H v _ m hm hw, prod_jmEigen q hq e]

/-- **The twist scalar is pinned, not merely permitted**, on a bounded presentation. -/
theorem twistB_scalar_eq_theta_sq [NoZeroSMulDivisors R V] (H : HeckeGeneratorsBelow R A q n)
    (hq : q ≠ 0) {l : Partition} {m : ℕ} (hm : m < n)
    (e : Fin (m + 1) ≃ {c // c ∈ cells l}) (v : V) (hv : v ≠ 0) (s : R)
    (hw : IsJMWeightB H v (jmEigen q e) (m + 1))
    (hs : (deltaB H m ^ (m + 1)) • v = s • v) :
    s = (theta q l) ^ 2 := by
  have h := (fullTwistB_smul_eq_theta_sq H hq hm e v hw).symm.trans hs
  have hz : (s - (theta q l) ^ 2) • v = 0 := by rw [sub_smul, h, sub_self]
  rcases smul_eq_zero.mp hz with hc | hcv
  · linear_combination (norm := ring_nf) hc
  · exact absurd hcv hv

/-! ## §2  The `(2,1)` block: `θ_λ² = 1` -/

/-- `c((2,1)) = 0 + 1 + (−1) = 0`. -/
theorem contentSum_two_one : contentSum [2, 1] = 0 := by decide

/-- Hence `θ_{(2,1)}² = 1`: the full twist of `B₃` is predicted to act **trivially** on the
seminormal vector of the 2-dimensional block. -/
theorem theta_two_one_sq (q : R) : (theta q [2, 1]) ^ 2 = 1 := by
  unfold theta
  rw [contentSum_two_one, zpow_zero, one_pow]

/-! ## §3  The independent check -/

section StdThree

variable {K : Type*} [Field K]

/-- **The falsifiability check.**  `(σ₀σ₁)³ = 1` for the explicit `2×2` seminormal pair, by direct
matrix computation — no Jucys–Murphy input whatsoever.

This is the same number `θ_{(2,1)}² = 1` predicts, reached by a completely different route, so §1's
conclusion is constrained by an independently-proved case rather than free. -/
theorem stdTwo_fullTwist_eq_one (q : K) (hq : q ≠ 0) :
    (stdTwo0 q * stdTwo1 q) ^ 3 = 1 := by
  have e : (stdTwo0 q * stdTwo1 q) ^ 3
      = stdTwo0 q * stdTwo1 q * (stdTwo0 q * stdTwo1 q) * (stdTwo0 q * stdTwo1 q) := by
    rw [pow_succ, pow_succ, pow_one]
  rw [e]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [stdTwo0, stdTwo1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- **The two routes agree.**  The Jucys–Murphy product of the eigenvalues on `e₀` is
`1 · q² · q⁻² = 1`, and the full twist really is the identity.  Both sides are `θ_{(2,1)}²`. -/
theorem stdTwoBelow3_twist_trivial (q : K) (hq : q ≠ 0) :
    jmProdB (stdTwoBelow3 q hq) 3 = 1 := by
  rw [stdTwoBelow3_jmProd_eq_fullTwist]
  exact stdTwo_fullTwist_eq_one q hq

/-- **The agreement, stated as one equation.**  The Jucys–Murphy product of the content eigenvalues
on `e₀` equals `θ_{(2,1)}²`, on a 2-dimensional module.

Left side computed from the JM spectrum; right side from the content sum of the partition. They are
the same, and `stdTwo_fullTwist_eq_one` reaches it a third way from the matrices alone. -/
theorem stdTwoBelow3_twist_eq_theta_sq (q : K) (hq : q ≠ 0) :
    jmProdB (stdTwoBelow3 q hq) 3
      = algebraMap K (Matrix (Fin 2) (Fin 2) K) ((theta q [2, 1]) ^ 2) := by
  rw [stdTwoBelow3_twist_trivial q hq, theta_two_one_sq, map_one]

/-- Subtracting the identity matrix from the three-strand Jucys-Murphy product on the two-dimensional module yields zero (`qou-lsib`). -/
theorem stdTwoBelow3_twist_sub_one_eq_zero (q : K) (hq : q ≠ 0) :
    jmProdB (stdTwoBelow3 q hq) 3 - 1 = 0 := by
  rw [stdTwoBelow3_twist_trivial q hq, sub_self]

end StdThree

end QOU.BraidKnot.Hecke
