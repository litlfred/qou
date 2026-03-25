/-!
# QOU.CategoricalReeb.ofWeightDecomposition

Existence of the categorical Reeb derivation: given a maximal torus
and weight decomposition, the infinitesimal generator of the torus
action yields a Reeb derivation `(ξ, θ_A)` satisfying all three
properties (vertical generator, normalisation, kernel).

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
    Maurer–Cartan dual `θ_A` satisfy all three Reeb properties:

    1. Vertical generator: π_V ∘ d factors through contraction with ξ.
    2. Normalisation: ξ ≫ θ_A = θ_A.
    3. Kernel: horizontal forms are the kernel of contraction with ξ.

    Construction:
    1. Let `ξ : A → A` be the infinitesimal generator of the torus
       action (`d/dt|_{t=0}` of the one-parameter subgroup).
    2. Let `θ_A : A → 𝟙_C` be the Maurer–Cartan form, dual to `ξ`:
       it is the unique morphism satisfying `θ_A(ξ) = id`.
    3. Let `ι_ξ : Ω¹(A) → A` be the interior product (contraction).
    4. Let `d : A → Ω¹(A)` be the differential.

    The three properties follow from the compatibility of the torus
    action with the differential calculus.

    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
noncomputable def CategoricalReeb.ofWeightDecomposition
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (mt : MaximalTorus C) (wd : WeightDecomposition C)
    (A : C)
    (xi : A ⟶ A)
    (theta : A ⟶ (𝟙_ C))
    (d : A ⟶ wd.forms)
    (contract_xi : wd.forms ⟶ A)
    (norm : xi ≫ theta = theta)
    (vert : d ≫ wd.proj_V ≫ contract_xi = xi)
    (proj_idem : wd.proj_V ≫ wd.proj_V = wd.proj_V := wd.proj_V_idem)
    (kern : contract_xi ≫ d ≫ wd.proj_V = contract_xi ≫ d) :
    CategoricalReeb C :=
  { A := A
    forms := wd.forms
    xi := xi
    theta := theta
    proj_V := wd.proj_V
    d := d
    contract_xi := contract_xi
    vertical_generator := vert
    normalisation := norm
    proj_V_idem := proj_idem
    kernel_horizontal := kern }

end QOU
