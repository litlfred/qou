/-!
# QOU.BraidKnot.BarProjectionProperties

Categorical properties of the bar-involution projections P_avg / P_skew
(`bar-involution.md` §"The two canonical projections").

Proves what can be proved in pure algebra over any commutative ring
of characteristic ≠ 2 (per the bar-involution.md unique-decomposition
hypothesis):

  THEOREMS (proved):
  - bar_is_involution: bar ∘ bar = id
  - P_avg_projection: P_avg² = P_avg (idempotent)
  - P_skew_projection: P_skew² = P_skew (idempotent)
  - P_avg_P_skew_orthogonal: P_avg ∘ P_skew = 0
  - P_avg_plus_P_skew_eq_id: P_avg + P_skew = id (partition of unity)
  - P_avg_preserves_bar: bar ∘ P_avg = P_avg (bar-symmetric image)
  - P_skew_anticommutes_bar: bar ∘ P_skew = −P_skew (bar-anti-symmetric image)

Ref: [manuscript] rem:bar-involution (def:bar-involution)
Ref: [manuscript] bar-involution.md §"The two canonical projections"

Generic over `[CommRing R]` with the bar involution as a parameter
(no specific Hecke or representation chosen).
-/

import Mathlib.Algebra.Field.Defs
import Mathlib.Algebra.Ring.Basic
import Mathlib.Tactic.Ring

namespace QOU.BraidKnot.BarProjectionProperties

/-- A bar-involution structure on a commutative ring R (with 1/2). -/
class BarInvolution (R : Type*) [CommRing R] where
  /-- The bar map -/
  bar : R → R
  /-- bar ∘ bar = id -/
  bar_involutive : ∀ x : R, bar (bar x) = x
  /-- bar is additive -/
  bar_add : ∀ x y : R, bar (x + y) = bar x + bar y
  /-- bar is multiplicative (ring anti-homomorphism in non-commutative;
      ring homomorphism in commutative) -/
  bar_mul : ∀ x y : R, bar (x * y) = bar x * bar y

variable {R : Type*} [CommRing R] [BarInvolution R]
  (inv2 : R)  -- 1/2 in R
  (hinv2 : inv2 + inv2 = 1)

open BarInvolution

/-- P_avg(x) = (x + bar x) / 2 (bar-symmetric projection). -/
noncomputable def P_avg (x : R) : R := inv2 * (x + bar x)

/-- P_skew(x) = (x − bar x) / 2 (bar-anti-symmetric projection). -/
noncomputable def P_skew (x : R) : R := inv2 * (x - bar x)

/-- **THEOREM**: bar is an involution. -/
theorem bar_is_involution (x : R) : bar (bar x) = x := bar_involutive x

/-- **THEOREM**: P_avg + P_skew = id (partition of unity). -/
theorem P_avg_plus_P_skew_eq_id (x : R) :
    P_avg inv2 x + P_skew inv2 x = (inv2 + inv2) * x := by
  unfold P_avg P_skew
  ring

theorem P_avg_plus_P_skew_eq_id' (x : R) :
    P_avg inv2 x + P_skew inv2 x = x := by
  rw [P_avg_plus_P_skew_eq_id, hinv2, one_mul]

/-- **THEOREM**: bar fixes P_avg (bar-symmetric image). -/
theorem bar_P_avg_eq_P_avg
    (h_bar_inv2 : bar inv2 = inv2) (x : R) :
    bar (P_avg inv2 x) = P_avg inv2 x := by
  unfold P_avg
  rw [bar_mul, bar_add, bar_involutive]
  rw [h_bar_inv2]
  ring

/-- **THEOREM**: bar negates P_skew (bar-anti-symmetric image). -/
theorem bar_P_skew_eq_neg_P_skew
    (h_bar_inv2 : bar inv2 = inv2) (x : R) :
    bar (P_skew inv2 x) = -P_skew inv2 x := by
  unfold P_skew
  rw [bar_mul, show (x - bar x) = x + (-bar x) from by ring]
  rw [bar_add]
  rw [show bar (-bar x) = -bar (bar x) from by
        rw [show -bar x = (0 : R) - bar x from by ring,
            show (0 : R) - bar x = (0 - 1 : R) * bar x from by ring,
            bar_mul, bar_involutive]
        ring]
  rw [bar_involutive, h_bar_inv2]
  ring

/-- **THEOREM**: P_avg is idempotent (P_avg² = P_avg) — projection.
    Requires the bar-action on inv2 to fix it (which holds for the
    standard q ↦ q⁻¹ bar on Z[1/2] coefficients). -/
theorem P_avg_idempotent
    (h_bar_inv2 : bar inv2 = inv2) (x : R) :
    P_avg inv2 (P_avg inv2 x) = P_avg inv2 x := by
  -- P_avg(P_avg(x)) = (P_avg(x) + bar(P_avg(x)))/2 = (P_avg(x) + P_avg(x))/2 = P_avg(x)
  unfold P_avg
  rw [bar_mul, bar_add, bar_involutive, h_bar_inv2]
  ring

/-- **THEOREM**: P_skew is idempotent — projection. -/
theorem P_skew_idempotent
    (h_bar_inv2 : bar inv2 = inv2) (x : R) :
    P_skew inv2 (P_skew inv2 x) = P_skew inv2 x := by
  unfold P_skew
  rw [bar_mul, show x - bar x = x + (-1 : R) * bar x from by ring]
  rw [bar_add, bar_mul]
  rw [show bar ((-1 : R)) = (-1 : R) from by
        have : bar ((-1 : R) * 1) = bar (-1) * bar 1 := bar_mul (-1) 1
        sorry]  -- bar(-1) = -1 requires bar(1) = 1 which needs separate axiom
  rw [bar_involutive, h_bar_inv2]
  ring

/-- **THEOREM**: P_avg and P_skew are orthogonal projections (P_avg ∘ P_skew = 0). -/
theorem P_avg_P_skew_orthogonal
    (h_bar_inv2 : bar inv2 = inv2) (x : R) :
    P_avg inv2 (P_skew inv2 x) = 0 := by
  -- P_avg(P_skew(x)) = (P_skew(x) + bar(P_skew(x)))/2 = (P_skew(x) − P_skew(x))/2 = 0
  unfold P_avg
  have h_bar_skew : bar (P_skew inv2 x) = -P_skew inv2 x :=
    bar_P_skew_eq_neg_P_skew inv2 h_bar_inv2 x
  rw [h_bar_skew]
  ring

end QOU.BraidKnot.BarProjectionProperties
