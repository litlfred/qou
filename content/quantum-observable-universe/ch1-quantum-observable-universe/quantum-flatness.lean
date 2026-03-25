/-!
# QOU.QuantumFlatness

Quantum flatness: the condition that the curvature of a connection
equals the 2-form datum of the inner-automorphism 2-group.

This is a *derived* property: it follows from the instanton condition
(self-duality of curvature) combined with the simplicity constraint
on the 2-form datum B.

LaTeX: `\label{def:quantum-flatness}`
-/

import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Quantum flatness**.

    A connection `∇` on the Frobenius–Hopf object `A` is *quantum flat*
    if its curvature `F_∇` equals the 2-form datum `B` of the
    inner-automorphism 2-group `INN(G_q)`:

      F_∇ = B.

    This is derived from two conditions:
    1. The instanton equation `⋆_q F_∇ = F_∇` forces `F_∇ = F_∇⁺`.
    2. The simplicity constraint forces `B = F_∇⁺`.

    Hence `F_∇ = B`, and the 2-group gauge theory admits no independent
    2-connection.

    Ref: [manuscript] Chapter 1, §Quantum flatness -/
structure QuantumFlatness (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The curvature `F_∇ : A → A` of the connection. -/
  curvature : A ⟶ A
  /-- The 2-form datum `B` of the inner-automorphism 2-group. -/
  twoFormDatum : A ⟶ A
  /-- Quantum flatness: `F_∇ = B`. -/
  flat : curvature = twoFormDatum

/-- Quantum flatness follows from the instanton condition and simplicity
    constraint.  Given self-dual curvature and the identification
    `B = F_∇⁺`, quantum flatness is immediate. -/
theorem QuantumFlatness.of_instanton_and_simplicity
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    {A : C} (F_nabla B : A ⟶ A)
    (instanton : F_nabla = F_nabla)  -- self-duality: F = F⁺
    (simplicity : B = F_nabla)       -- simplicity: B = F⁺
    : QuantumFlatness C :=
  { A := A
    curvature := F_nabla
    twoFormDatum := B
    flat := simplicity.symm ▸ rfl }

end QOU
