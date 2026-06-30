import QOU.QuantumObservableUniverse.Structures
import Mathlib.CategoryTheory.Preadditive.Basic


/-!
# QOU.PositiveDefiniteStructure

The positive-definite dagger structure on an involutive monoidal
category, and the proposition that such a structure exists.

`PositiveDefiniteStructure` and its base `InvolutiveStructure` are
defined in `QOU.QuantumObservableUniverse.Structures`; this block
records the existence proposition `prop:positive-definite-dagger`.
-/

open scoped CategoryTheory CategoryTheory.MonoidalCategory

namespace QOU

universe u v

/-- Theorem stating the existence of the positive-definite dagger
    structure on an involutive monoidal category. -/
-- Ref: [manuscript] §1-quantum-universes/positive-definite-dagger
theorem positive_definite_dagger_exists (C : Type u)
    [CategoryTheory.Category.{v} C]
    [CategoryTheory.MonoidalCategory C]
    [CategoryTheory.Preadditive C] :
    Nonempty (PositiveDefiniteStructure C) := by
  -- Ref: [manuscript] §1 — the concrete witness (the canonical dagger on
  -- the ℂ-realisation Rep(SU_q(2))) requires the rigid-monoidal /
  -- inner-product infrastructure not yet available standalone.
  -- Ref: [manuscript]
  sorry

end QOU
