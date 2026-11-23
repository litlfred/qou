import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Data.Complex.Basic
import Mathlib.Data.ZMod.Basic

/-!
# `QOU.HyperellipticQuintic.bring_weight_match` — `ℤ₅`-weight identification (`prop:x5-bring-weight-identification`)

Formalises `prop:x5-bring-weight-identification`: under the cyclic `ℤ₅ ⊂ S₅` generator `σ`,
both the hyperelliptic-quintic coordinate `x` on `𝒳₅ : y² = x⁵ - 1` (acting by contragredient
pullback `(σ · f)(x, y) = f(ζ₅⁻¹ x, y)`) and Bring's first 5-point DFT Lagrange resolvent
`w₁(c) = ∑_{j ∈ ℤ/5ℤ} ζ₅^j c_j` (under cyclic root shift `(σ c)_j = c_{j+1}`) transform in
the **weight-`(-1)` character** with common eigenvalue `ζ₅⁻¹ = ζ₅⁴`, while their fifth powers
`x⁵` and `w₁⁵` are `ℤ₅`-invariant.

LaTeX label: `prop:x5-bring-weight-identification`

## References

- [bolza1887] https://doi.org/10.2307/2369402
- [edge1978] https://doi.org/10.1112/jlms/s2-18.3.539
-/

open scoped BigOperators

namespace QOU.HyperellipticQuintic

/-- Primitive fifth root of unity `ζ₅ = exp(2πi / 5)`. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
noncomputable def zeta5 : ℂ :=
  Complex.exp (2 * Real.pi * Complex.I / 5)

/-- `ζ₅ ≠ 0` since the complex exponential never vanishes. -/
theorem zeta5_ne_zero : zeta5 ≠ 0 := by
  unfold zeta5
  exact Complex.exp_ne_zero _

/-- `ζ₅⁵ = 1`. -/
-- Ref: [bolza1887] https://doi.org/10.2307/2369402
theorem zeta5_pow_five : zeta5 ^ 5 = 1 := by
  unfold zeta5
  rw [← Complex.exp_nat_mul]
  have h5 : (5 : ℕ) * (2 * (Real.pi : ℂ) * Complex.I / 5) =
      2 * (Real.pi : ℂ) * Complex.I := by
    push_cast
    ring
  rw [h5]
  exact Complex.exp_two_pi_mul_I

/-- Reduction of exponents modulo `5`: `ζ₅^(n % 5) = ζ₅^n`. -/
theorem zeta5_pow_mod (n : ℕ) : zeta5 ^ (n % 5) = zeta5 ^ n := by
  conv_rhs => rw [← Nat.div_add_mod n 5]
  rw [pow_add, pow_mul, zeta5_pow_five, one_pow, one_mul]

/-- Character homomorphism identity `ζ₅^((a + b).val) = ζ₅^(a.val) · ζ₅^(b.val)` on `ZMod 5`. -/
theorem zeta5_zmod_add (a b : ZMod 5) :
    zeta5 ^ (a + b).val = zeta5 ^ a.val * zeta5 ^ b.val := by
  rw [ZMod.val_add, zeta5_pow_mod, pow_add]

/-- **Bring / `𝒳₅` eigenvalue identity (`prop:x5-bring-weight-identification`)**: `ζ₅⁴ = ζ₅⁻¹`. -/
-- Ref: [edge1978] https://doi.org/10.1112/jlms/s2-18.3.539
theorem bring_weight_match : zeta5 ^ (4 : ℕ) = zeta5⁻¹ := by
  have hz_ne : zeta5 ≠ 0 := zeta5_ne_zero
  have h4 : zeta5 ^ 4 * zeta5 = 1 := by
    rw [← pow_succ]
    exact zeta5_pow_five
  field_simp
  linear_combination h4

/-! ### Coordinate-ring contragredient `ℤ₅`-action on `𝒳₅` -/

/-- Left contragredient pullback `(σ · f)(x, y) = f(ζ₅⁻¹ x, y)` induced by
    `φ₅(x, y) = (ζ₅ x, y)` on functions `ℂ × ℂ → ℂ`. -/
noncomputable def x5CoordPullback (f : ℂ × ℂ → ℂ) : ℂ × ℂ → ℂ :=
  fun p => f (zeta5⁻¹ * p.1, p.2)

/-- `m`-th coordinate monomial `x^m` on `ℂ × ℂ`. -/
def x5Monomial (m : ℕ) : ℂ × ℂ → ℂ :=
  fun p => p.1 ^ m

/-- `x^m` is a `ℤ₅`-eigenvector of `x5CoordPullback` with eigenvalue `(ζ₅⁻¹)^m`; in
    particular `x` (`m = 1`) has eigenvalue `ζ₅⁻¹` and `x⁵` (`m = 5`) is invariant. -/
theorem x5CoordPullback_monomial :
    (∀ (m : ℕ) (p : ℂ × ℂ),
      x5CoordPullback (x5Monomial m) p = (zeta5⁻¹) ^ m * x5Monomial m p) ∧
    (∀ p : ℂ × ℂ, x5CoordPullback (x5Monomial 1) p = zeta5⁻¹ * x5Monomial 1 p) ∧
    (∀ p : ℂ × ℂ, x5CoordPullback (x5Monomial 5) p = x5Monomial 5 p) := by
  have hm : ∀ (m : ℕ) (p : ℂ × ℂ),
      x5CoordPullback (x5Monomial m) p = (zeta5⁻¹) ^ m * x5Monomial m p := by
    intro m p
    unfold x5CoordPullback x5Monomial
    ring
  refine ⟨hm, ?_, ?_⟩
  · intro p
    simpa using hm 1 p
  · intro p
    rw [hm 5 p, inv_pow, zeta5_pow_five, inv_one, one_mul]

/-! ### 5-point DFT Lagrange resolvents on Bring's root space `ZMod 5 → ℂ` -/

/-- Cyclic permutation `(σ c)_j = c_{j + 1}` of the 5 Bring roots `ZMod 5 → ℂ`. -/
def bringCyclicShift (c : ZMod 5 → ℂ) : ZMod 5 → ℂ :=
  fun j => c (j + 1)

/-- `k`-th Lagrange resolvent `w_k(c) = ∑_{j ∈ ZMod 5} ζ₅^((k * j).val) · c_j`. -/
noncomputable def lagrangeResolvent (k : ZMod 5) (c : ZMod 5 → ℂ) : ℂ :=
  ∑ j : ZMod 5, zeta5 ^ (k * j).val * c j

/-- **DFT eigenvector theorem for Bring's Lagrange resolvents**:
    under `bringCyclicShift`, `w_k(σ c) = ζ₅^((-k).val) · w_k(c)`; at `k = 1`,
    `w₁(σ c) = ζ₅⁻¹ · w₁(c)` (matching `x` on `𝒳₅`) and `w₁(σ c)⁵ = w₁(c)⁵`. -/
-- Ref: [edge1978] https://doi.org/10.1112/jlms/s2-18.3.539
theorem lagrangeResolvent_shift_eigenvalue (c : ZMod 5 → ℂ) :
    (∀ k : ZMod 5,
      lagrangeResolvent k (bringCyclicShift c) =
        zeta5 ^ (-k).val * lagrangeResolvent k c) ∧
    lagrangeResolvent 1 (bringCyclicShift c) = zeta5⁻¹ * lagrangeResolvent 1 c ∧
    (lagrangeResolvent 1 (bringCyclicShift c)) ^ 5 = (lagrangeResolvent 1 c) ^ 5 := by
  have hgen : ∀ k : ZMod 5,
      lagrangeResolvent k (bringCyclicShift c) =
        zeta5 ^ (-k).val * lagrangeResolvent k c := by
    intro k
    unfold lagrangeResolvent bringCyclicShift
    rw [← Equiv.sum_comp (Equiv.subRight (1 : ZMod 5))]
    rw [Finset.mul_sum]
    refine Finset.sum_congr rfl fun u _ => ?_
    simp only [Equiv.subRight_apply, sub_add_cancel]
    have hmul : k * (u - 1) = (-k) + k * u := by ring
    rw [hmul, zeta5_zmod_add]
    ring
  have hw1 : lagrangeResolvent 1 (bringCyclicShift c) = zeta5⁻¹ * lagrangeResolvent 1 c := by
    rw [hgen 1]
    have hval : (-1 : ZMod 5).val = 4 := rfl
    rw [hval, bring_weight_match]
  refine ⟨hgen, hw1, ?_⟩
  rw [hw1, mul_pow, inv_pow, zeta5_pow_five, inv_one, one_mul]

end QOU.HyperellipticQuintic

namespace QOU.X5BringWeight

/-- Backwards-compatible alias for `QOU.HyperellipticQuintic.zeta5`. -/
noncomputable abbrev zeta5 : ℂ := QOU.HyperellipticQuintic.zeta5

/-- Backwards-compatible alias for `QOU.HyperellipticQuintic.zeta5_pow_five`. -/
theorem zeta5_pow_five : zeta5 ^ 5 = 1 :=
  QOU.HyperellipticQuintic.zeta5_pow_five

/-- Backwards-compatible alias for `QOU.HyperellipticQuintic.bring_weight_match`. -/
theorem bring_weight_match : zeta5 ^ (4 : ℕ) = zeta5⁻¹ :=
  QOU.HyperellipticQuintic.bring_weight_match

end QOU.X5BringWeight
