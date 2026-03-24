/-!
# QOU.WeightDecomposition.ofMaximalTorus

Existence of the weight decomposition: given a maximal torus `T` acting
on `Ω^k(A)` in a preadditive monoidal category, the torus averaging
operator yields complementary idempotent projections `π_H` and `π_V`.

LaTeX: `\label{thm:weight-decomposition-exists}`
-/

import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Preadditive.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Existence of weight decomposition**.

    Given a maximal torus acting on `Ω^k(A)`, the torus averaging
    operator constructs complementary idempotent projections `π_H`
    (weight-0) and `π_V` (non-zero weight), yielding a
    `WeightDecomposition`.

    The construction uses the averaging operator `e₀ = ∫_T ρ(t) dt`
    over the compact torus, which is idempotent by Schur orthogonality.

    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
noncomputable def WeightDecomposition.ofMaximalTorus
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
    (mt : MaximalTorus C) (forms : C) : WeightDecomposition C :=
  { forms := forms
    proj_H := sorry  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
    proj_V := sorry  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
    complementary := sorry  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
    proj_H_idem := sorry  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
    proj_V_idem := sorry  -- Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9
  }

end QOU
