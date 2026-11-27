import CompactQuantumMetrics.OqSU2BudgetAllDirections
import CompactQuantumMetrics.OqSU2HaarState

/-!
# The budget identities for zero-weight functionals and the Haar state

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`).

`OqSU2BudgetSquare` and `OqSU2BudgetAllDirections` prove that each budget integrand is
minus a twisted square, `φ(X a · X' a) = -φ(w* w)`, for any functional `φ` invariant under
one torus scaling. `OqSU2HaarState` proves that every zero-weight functional, the Haar
state among them, is invariant under every torus scaling. This file combines the two, so
the identities hold for those functionals with no invariance hypothesis left.

## Results (sorry-free)

* `zeroWeight_cartan_eq_neg_square`: the Cartan direction, any moments `lam`, any `R`.
* `zeroWeight_field_pair_eq_neg_square`: the off-diagonal pairs, for `s² = q⁻¹`.
* `haarState_cartan_eq_neg_square`, `haarState_field_pair_eq_neg_square`: the Haar case
  over a field `K`.

## Not established here

* Positivity `h(w* w) ≥ 0` of the Haar state. Only with it do these identities give a
  sign, `h(X a · X' a) ≤ 0`; it is open in the Haar thread.
* Which pairing is the budget in the q-NS transport equation; Part A (`qou-pa7n`).

Ref: [woronowicz1987-twisted-su2] S. L. Woronowicz, Twisted SU(2) group. An example of a
non-commutative differential calculus, Publ. RIMS 23 (1987), 117–181, §4 (Haar measure).
-/

namespace QOU.AlgebraicSubstrate.OqSU2

section Generic

variable {R : Type*} [CommRing R] (q : Rˣ)

theorem zeroWeight_cartan_eq_neg_square (lam : ℕ → R) (s : Rˣ) (cinv : R)
    (a : OqSU2 R q) (ha : compactStar q a = a) :
    zeroWeightFunctional q lam
        (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q (s ^ 2)).toLinearMap)) a *
          leftInvOp q (cinv • ((counit q).toLinearMap -
            (diagCharAlgHom q (s ^ 2)).toLinearMap)) a) =
      -zeroWeightFunctional q lam
        (compactStar q (torusScaleAlgHom q s⁻¹ s (leftInvOp q (cinv • ((counit q).toLinearMap -
            (diagCharAlgHom q (s ^ 2)).toLinearMap)) a)) *
          torusScaleAlgHom q s⁻¹ s (leftInvOp q (cinv • ((counit q).toLinearMap -
            (diagCharAlgHom q (s ^ 2)).toLinearMap)) a)) :=
  cartanField_sq_eq_neg_square q s cinv a ha _ (zeroWeightFunctional_torus q lam s⁻¹ s)

theorem zeroWeight_field_pair_eq_neg_square (lam : ℕ → R) (s0 sp sm : R) (s : Rˣ)
    (hs : s ^ 2 = q⁻¹) (a : OqSU2 R q) (ha : compactStar q a = a) :
    zeroWeightFunctional q lam (field q s0 sp sm a * field q s0 sm sp a) =
      -zeroWeightFunctional q lam
        (compactStar q (torusScaleAlgHom q s⁻¹ s (field q s0 sm sp a)) *
          torusScaleAlgHom q s⁻¹ s (field q s0 sm sp a)) :=
  field_pair_eq_neg_square q s0 sp sm s hs a ha _ (zeroWeightFunctional_torus q lam s⁻¹ s)

end Generic

section Haar

variable {K : Type*} [Field K] (q : Kˣ)

theorem haarState_cartan_eq_neg_square (s : Kˣ) (cinv : K)
    (a : OqSU2 K q) (ha : compactStar q a = a) :
    haarState q
        (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q (s ^ 2)).toLinearMap)) a *
          leftInvOp q (cinv • ((counit q).toLinearMap -
            (diagCharAlgHom q (s ^ 2)).toLinearMap)) a) =
      -haarState q
        (compactStar q (torusScaleAlgHom q s⁻¹ s (leftInvOp q (cinv • ((counit q).toLinearMap -
            (diagCharAlgHom q (s ^ 2)).toLinearMap)) a)) *
          torusScaleAlgHom q s⁻¹ s (leftInvOp q (cinv • ((counit q).toLinearMap -
            (diagCharAlgHom q (s ^ 2)).toLinearMap)) a)) :=
  zeroWeight_cartan_eq_neg_square q _ s cinv a ha

theorem haarState_field_pair_eq_neg_square (s0 sp sm : K) (s : Kˣ) (hs : s ^ 2 = q⁻¹)
    (a : OqSU2 K q) (ha : compactStar q a = a) :
    haarState q (field q s0 sp sm a * field q s0 sm sp a) =
      -haarState q (compactStar q (torusScaleAlgHom q s⁻¹ s (field q s0 sm sp a)) *
          torusScaleAlgHom q s⁻¹ s (field q s0 sm sp a)) :=
  zeroWeight_field_pair_eq_neg_square q _ s0 sp sm s hs a ha

end Haar

end QOU.AlgebraicSubstrate.OqSU2
