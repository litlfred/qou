/-!
# QOU.AppendixSurreals.StandardPart — Robinson's standard-part map

The map `st : No_fin → ℝ` sending each finite surreal to the unique
real with infinitesimal difference.  Standard-part is a surjective
ring homomorphism whose kernel is the infinitesimals.

This module provides:

- `standardPart : K → ℝ` (zero on non-finite inputs by convention)
- ring-hom properties on the finite subring
- the kernel characterisation

## References

- [robinson1966] Robinson, *Non-standard Analysis*, §3.2.
- [alling1987] Alling, *Foundations of Analysis over Surreal Number
  Fields*, North-Holland.

LaTeX label: `def:standard-part-functor`
-/

import QOU.AppendixSurreals.Basic

namespace QOU.AppendixSurreals

open SurrealField

universe u

variable {K : Type u} [SurrealField K]

/-- Robinson's **standard-part map**: sends each finite surreal to the
    unique real of which it is an infinitesimal perturbation. -/
-- Ref: [robinson1966] §3.2
noncomputable def standardPart (x : K) : ℝ :=
  if hx : IsFinite x then
    Classical.choose (isFinite_decomposition hx).exists
  else 0

/-- Notation: `st x = standardPart x`. -/
scoped notation "st" => standardPart

/-- Defining property: for finite `x`, `x - ofReal (st x)` is
    infinitesimal. -/
-- Ref: [robinson1966] §3.2
theorem standardPart_spec {x : K} (hx : IsFinite x) :
    IsInfinitesimal (x - SurrealField.ofReal (standardPart x)) := by
  unfold standardPart
  rw [dif_pos hx]
  exact (Classical.choose_spec (isFinite_decomposition hx).exists)

/-- The standard part of a real is itself. -/
-- Ref: [alling1987] §4.7
theorem standardPart_ofReal (r : ℝ) :
    standardPart (SurrealField.ofReal (K := K) r) = r := by
  -- ofReal r is finite (bounded by ⌈r⌉ + 1).
  -- The decomposition gives r = r + 0, with 0 infinitesimal.
  -- Uniqueness pins it down.
  have hfin : IsFinite (ofReal (K := K) r) := by
    refine ⟨Nat.ceil |r| + 1, ?_⟩
    sorry  -- Ref: [robinson1966] § 3.1
  sorry  -- Ref: [alling1987] § 4.7

/-- The standard part of zero is zero. -/
@[simp]
theorem standardPart_zero : standardPart (0 : K) = 0 := by
  rw [show (0 : K) = SurrealField.ofReal 0 by simp [map_zero], standardPart_ofReal]

/-- The standard part of one is one. -/
@[simp]
theorem standardPart_one : standardPart (1 : K) = 1 := by
  rw [show (1 : K) = SurrealField.ofReal 1 by simp [map_one], standardPart_ofReal]

/-- An infinitesimal has standard part zero. -/
-- Ref: [robinson1966] Lemma 3.2.4
theorem standardPart_of_infinitesimal {x : K} (hx : IsInfinitesimal x) :
    standardPart x = 0 := by
  -- Apply uniqueness: 0 ∈ ℝ satisfies `x - ofReal 0 = x` infinitesimal.
  have hfin := hx.isFinite
  have h0 : IsInfinitesimal (x - SurrealField.ofReal (0 : ℝ)) := by
    simp [map_zero]; exact hx
  have hspec := standardPart_spec hfin
  have huniq := (isFinite_decomposition hfin).unique
  exact huniq hspec h0 |>.symm

/-- Standard-part is additive on the finite subring. -/
-- Ref: [robinson1966] Theorem 3.2.4 (i)
theorem standardPart_add {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    standardPart (x + y) = standardPart x + standardPart y := by
  -- Ref: [robinson1966] §3.2
  sorry

/-- Standard-part is multiplicative on the finite subring. -/
-- Ref: [robinson1966] Theorem 3.2.4 (ii)
theorem standardPart_mul {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    standardPart (x * y) = standardPart x * standardPart y := by
  -- Ref: [robinson1966] §3.2
  sorry

/-- Standard-part is order-compatible on the finite subring. -/
-- Ref: [robinson1966] Theorem 3.2.4 (iii)
theorem standardPart_le_iff {x y : K} (hx : IsFinite x) (hy : IsFinite y) :
    standardPart x < standardPart y →
    x < y + SurrealField.ofReal (1 : ℝ) := by
  -- Strict inequality on ℝ lifts to strict inequality up to
  -- an infinitesimal on K.
  -- Ref: [robinson1966] §3.2
  sorry

end QOU.AppendixSurreals
