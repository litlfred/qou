import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Functor
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Functor.Basic

/-!
# QOU.AlgebraicSubstrate.ClassicalLimitFunctor

The classical limit functor L : C_q → C_1, sending the braided monoidal
category at deformation parameter q to the symmetric monoidal category
at q = 1.

LaTeX label: `def:classical-limit-functor`
-/

set_option autoImplicit false


open CategoryTheory MonoidalCategory BraidedCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **Classical limit functor** `L : C_q → C_1`.

    Sends the braided monoidal category `C_q` (at deformation parameter q)
    to the symmetric monoidal category `C_1` (at q = 1). The functor
    collapses the quantum gap, smooths the q-differential, and trivializes
    the braiding.

    LaTeX: `\label{def:classical-limit-functor}`
    Ref: [leitner2026] Chapter 8, Section 5

    **`is_exact : Prop` removed 2026-09-07 — universe-`Prop` typed, neither read
    nor constructed. Exactness of the functor needs additive structure on `Cq`
    and `C1`, which this structure does not require.** -/
structure ClassicalLimitFunctor
    (Cq : Type u) [Category.{v} Cq] [MonoidalCategory Cq] [BraidedCategory Cq]
    (C1 : Type u) [Category.{v} C1] [MonoidalCategory C1] [SymmetricCategory C1]
    where
  /-- The underlying functor, together with its monoidal structure.

      Mathlib replaced the bundled `MonoidalFunctor Cq C1` with a plain
      functor carrying a `Functor.Monoidal` **typeclass**, so the bundle is
      split in two here. `functor.toFunctor` and `functor.μIso X Y` become
      `functor` and `Functor.Monoidal.μIso functor X Y` accordingly. -/
  functor : Cq ⥤ C1
  /-- The monoidal structure on `functor`. -/
  [functorMonoidal : functor.Monoidal]
  /-- Quantum gap collapse: ℏ_q → 0 as q → 1.
      Expressed as: the functor sends the braiding to the symmetric swap. -/
  -- Ref: [leitner2026] Chapter 8, Section 5
  braiding_trivializes :
    ∀ (X Y : Cq),
      functor.map (β_ X Y).hom =
        (Functor.Monoidal.μIso functor X Y).inv ≫
        (β_ (functor.obj X) (functor.obj Y)).hom ≫
        (Functor.Monoidal.μIso functor Y X).hom
  /-- The functor is NOT full: quantum information is lost in the limit.
      There exist morphisms in C_1 not in the image of L. -/
  not_full : ¬ (functor.Full)

end QOU.AlgebraicSubstrate
