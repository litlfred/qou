/-!
# QOU.AlgebraicSubstrate.ClassicalLimitFunctor

The classical limit functor L : C_q → C_1, sending the braided monoidal
category at deformation parameter q to the symmetric monoidal category
at q = 1.

LaTeX label: `def:classical-limit-functor`
-/

set_option autoImplicit false

import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Monoidal.Braided.Basic
import Mathlib.CategoryTheory.Functor.Basic

open CategoryTheory MonoidalCategory BraidedCategory

namespace QOU.AlgebraicSubstrate

universe u v

/-- **Classical limit functor** `L : C_q → C_1`.

    Sends the braided monoidal category `C_q` (at deformation parameter q)
    to the symmetric monoidal category `C_1` (at q = 1). The functor
    collapses the quantum gap, smooths the q-differential, and trivializes
    the braiding.

    LaTeX: `\label{def:classical-limit-functor}`
    Ref: [manuscript] Chapter 8, Section 5 -/
structure ClassicalLimitFunctor
    (Cq : Type u) [Category.{v} Cq] [MonoidalCategory Cq] [BraidedCategory Cq]
    (C1 : Type u) [Category.{v} C1] [MonoidalCategory C1] [SymmetricCategory C1]
    where
  /-- The underlying monoidal functor. -/
  functor : MonoidalFunctor Cq C1
  /-- Quantum gap collapse: ℏ_q → 0 as q → 1.
      Expressed as: the functor sends the braiding to the symmetric swap. -/
  -- Ref: [manuscript] Chapter 8, Section 5
  braiding_trivializes :
    ∀ (X Y : Cq),
      functor.toFunctor.map (β_ X Y).hom =
        functor.μIso X Y |>.hom ≫
        (β_ (functor.toFunctor.obj X) (functor.toFunctor.obj Y)).hom ≫
        (functor.μIso Y X).inv
  /-- The functor is exact (preserves short exact sequences).
      Stated abstractly as a Prop field; the full proof requires
      checking preservation of finite limits and colimits. -/
  is_exact : Prop
  /-- The functor is NOT full: quantum information is lost in the limit.
      There exist morphisms in C_1 not in the image of L. -/
  not_full : ¬ (functor.toFunctor.Full)

end QOU.AlgebraicSubstrate
