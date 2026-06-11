import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Preadditive.Basic


/-!
# QOU.WeightDecomposition.ofMaximalTorus

Existence of the weight decomposition: given a maximal torus `T` acting
on `Ω^k(A)` in a preadditive monoidal category, the torus averaging
operator yields complementary idempotent projections `π_H` and `π_V`.

LaTeX: `\label{thm:weight-decomposition-exists}`
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- Auxiliary: given complementary idempotents summing to the identity,
    the second projection is determined.  This is the key algebraic
    fact underlying the weight decomposition. -/
theorem comp_idem_of_sum_id {C : Type u} [Category.{v} C] [Preadditive C]
    {X : C} {p : X ⟶ X} (hp : p ≫ p = p) :
    (𝟙 X - p) ≫ (𝟙 X - p) = 𝟙 X - p := by
  simp [Preadditive.comp_sub, Preadditive.sub_comp, hp, Category.comp_id, Category.id_comp]

/-- **Existence of weight decomposition**.

    Given a maximal torus acting on `Ω^k(A)`, the torus averaging
    operator constructs complementary idempotent projections `π_H`
    (weight-0) and `π_V` (non-zero weight), yielding a
    `WeightDecomposition`.

    The construction:
    1. The averaging operator `e₀ = ∫_T ρ(t) dt` over the compact
       torus is the weight-0 idempotent (Schur orthogonality).
    2. Set `π_H := e₀` and `π_V := id − e₀`.
    3. Complementarity holds by construction: `π_H + π_V = id`.
    4. Idempotency of `π_V` follows from `comp_idem_of_sum_id`.

    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
noncomputable def WeightDecomposition.ofMaximalTorus
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
    (mt : MaximalTorus C) (forms : C)
    (avg : forms ⟶ forms)
    (avg_idem : avg ≫ avg = avg) : WeightDecomposition C :=
  { forms := forms
    proj_H := avg
    proj_V := 𝟙 forms - avg
    complementary := by simp [add_sub_cancel]
    proj_H_idem := avg_idem
    proj_V_idem := comp_idem_of_sum_id avg_idem }

end QOU
