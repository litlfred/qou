import CompactQuantumMetrics.OqSU2BudgetHaar
import CompactQuantumMetrics.OqSU2HaarPositivity

/-!
# The sign of the budget integrand

Bean `qou-q3dc` (q-NS Part A, `conj:regularity-breakdown`).

`OqSU2BudgetHaar` writes each budget integrand as minus a Haar square,
`h(X a · X' a) = -h(w* w)`. `OqSU2HaarPositivity` proves `h(x* x) ≥ 0` for `q > 0`,
`q ≠ 1`, over any linearly ordered field. Together they fix the sign.

## Results (sorry-free)

* `haarState_cartan_nonpos`: `h(X a · X a) ≤ 0` for the Cartan field and self-adjoint `a`.
* `haarState_field_pair_nonpos`: `h(X_{s0,sp,sm} a · X_{s0,sm,sp} a) ≤ 0` when `s² = q⁻¹`;
  in particular `h(X₊ a · X₋ a) ≤ 0` (`haarState_plusMinus_nonpos`).

## Not established here

* That these integrands, with these normalisations, are the budget of the q-NS
  transport equation. That identification is part of Part A (bean `qou-pa7n`), which
  stays open.
* Any statement about the limit `q → 1`. Positivity needs `q ≠ 1`, and nothing here
  controls the size of the integrand as `q → 1`.

Ref: [woronowicz1987-twisted-su2] S. L. Woronowicz, Twisted SU(2) group. An example of a
non-commutative differential calculus, Publ. RIMS 23 (1987), 117–181, §4.
-/

namespace QOU.AlgebraicSubstrate.OqSU2

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K] (q : Kˣ)

theorem haarState_cartan_nonpos (hq0 : 0 < (q : K)) (hq1 : (q : K) ≠ 1) (s : Kˣ) (cinv : K)
    (a : OqSU2 K q) (ha : compactStar q a = a) :
    haarState q
        (leftInvOp q (cinv • ((counit q).toLinearMap - (diagCharAlgHom q (s ^ 2)).toLinearMap)) a *
          leftInvOp q (cinv • ((counit q).toLinearMap -
            (diagCharAlgHom q (s ^ 2)).toLinearMap)) a) ≤ 0 := by
  rw [haarState_cartan_eq_neg_square q s cinv a ha]
  exact neg_nonpos.2 (haarState_star_mul_self_nonneg q hq0 hq1 _)

theorem haarState_field_pair_nonpos (hq0 : 0 < (q : K)) (hq1 : (q : K) ≠ 1) (s0 sp sm : K)
    (s : Kˣ) (hs : s ^ 2 = q⁻¹) (a : OqSU2 K q) (ha : compactStar q a = a) :
    haarState q (field q s0 sp sm a * field q s0 sm sp a) ≤ 0 := by
  rw [haarState_field_pair_eq_neg_square q s0 sp sm s hs a ha]
  exact neg_nonpos.2 (haarState_star_mul_self_nonneg q hq0 hq1 _)

theorem haarState_plusMinus_nonpos (hq0 : 0 < (q : K)) (hq1 : (q : K) ≠ 1) (s : Kˣ)
    (hs : s ^ 2 = q⁻¹) (a : OqSU2 K q) (ha : compactStar q a = a) :
    haarState q (fieldPlus q a * fieldMinus q a) ≤ 0 :=
  haarState_field_pair_nonpos q hq0 hq1 0 1 0 s hs a ha

end QOU.AlgebraicSubstrate.OqSU2
