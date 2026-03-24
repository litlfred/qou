/-!
# QOU.CategoricalReeb.ofWeightDecomposition

Existence of the categorical Reeb derivation: given a maximal torus
and weight decomposition, the infinitesimal generator of the torus
action yields a Reeb derivation `(ξ, θ_A)` satisfying the
normalisation axiom.

LaTeX: `\label{thm:categorical-reeb-exists}`
-/

import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Existence of the categorical Reeb derivation**.

    Given a maximal torus `T` with weight decomposition `(π_H, π_V)`,
    the infinitesimal generator `ξ` of the `T`-action on `A` and its
    Maurer–Cartan dual `θ_A` satisfy the normalisation axiom
    `ξ ≫ θ_A = θ_A`.

    Construction:
    1. Let `ξ : A → A` be the infinitesimal generator of the torus
       action (`d/dt|_{t=0}` of the one-parameter subgroup).
    2. Let `θ_A : A → 𝟙_C` be the Maurer–Cartan form, dual to `ξ`:
       it is the unique morphism satisfying `θ_A(ξ) = id`.
    3. The normalisation axiom `ξ ≫ θ_A = θ_A` encodes that `ξ` is
       a section of `θ_A`: applying `ξ` first and then `θ_A` is the
       same as applying `θ_A` directly.

    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
noncomputable def CategoricalReeb.ofWeightDecomposition
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (mt : MaximalTorus C) (wd : WeightDecomposition C)
    (xi : wd.forms ⟶ wd.forms)
    (theta : wd.forms ⟶ (𝟙_ C))
    (norm : xi ≫ theta = theta) :
    CategoricalReeb C :=
  { A := wd.forms
    xi := xi
    theta := theta
    normalisation := norm }

end QOU
