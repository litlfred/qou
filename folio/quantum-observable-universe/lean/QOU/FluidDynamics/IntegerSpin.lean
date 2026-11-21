import Mathlib.Algebra.Ring.Parity
import Mathlib.Tactic.Ring

/-!
# QOU.FluidDynamics.IntegerSpin — velocity fields on `ℝ³` carry integer spin only

Lemma L1 of the 2026-11-21 restatement of `conj:regularity-breakdown` and
`def:leray-profile` (issue #8864); the other four are in
`QOU.FluidDynamics.DSSObstructions`.

On the spin-`j` summand of an `SU(2)`-representation the central element `-1`
acts by `(-1)^{2j}`. On velocity fields on `ℝ³` the rotation action factors
through `SO(3)`, so `-1` acts as the identity. Hence `(-1)^{2j} = 1`, and over
any commutative ring with `2 ≠ 0` this forces `2j` even. The two
representation-theoretic facts are standard and are the hypotheses of the
lemma; they are not re-proved here.

## Base ring (§7c)
Generic `{R : Type*} [CommRing R]`, no `ℝ`.

## References
- [leitner2026] fluid-dynamics/leray-profile-construction, leray-profile-exclusions
-/

namespace QOU.FluidDynamics.IntegerSpin

/-- **L1 (integer spin only).** If the central element `-1` acts on the
    spin-`j` summand by `(-1)^{2j}` (write `twoJ = 2j`) and also acts trivially
    (as on any field on `ℝ³`, since `SU(2) → SO(3)` kills `-1`), then `twoJ` is
    even, i.e. `j` is an integer. Holds over any commutative ring with `2 ≠ 0`. -/
theorem even_of_neg_one_pow_eq_one {R : Type*} [CommRing R] (h2 : (2 : R) ≠ 0)
    {twoJ : ℕ} (h : (-1 : R) ^ twoJ = 1) : Even twoJ := by
  rcases Nat.even_or_odd twoJ with he | ho
  · exact he
  · exfalso
    rw [ho.neg_one_pow] at h
    apply h2
    calc (2 : R) = 1 - (-1) := by ring
      _ = 0 := by rw [h]; ring

/-- **L1, contrapositive form.** A half-integer spin (`twoJ` odd) cannot occur
    in a representation where `-1` acts trivially. -/
theorem neg_one_pow_ne_one_of_odd {R : Type*} [CommRing R] (h2 : (2 : R) ≠ 0)
    {twoJ : ℕ} (hodd : Odd twoJ) : (-1 : R) ^ twoJ ≠ 1 := by
  intro h
  exact (Nat.not_even_iff_odd.mpr hodd) (even_of_neg_one_pow_eq_one h2 h)

end QOU.FluidDynamics.IntegerSpin
