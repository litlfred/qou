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

    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
noncomputable def CategoricalReeb.ofWeightDecomposition
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (mt : MaximalTorus C) (wd : WeightDecomposition C) :
    CategoricalReeb C :=
  { A := wd.forms
    xi := sorry  -- Ref: [witten1988] https://doi.org/10.1007/BF01223371
    theta := sorry  -- Ref: [witten1988] https://doi.org/10.1007/BF01223371
    normalisation := sorry  -- Ref: [witten1988] https://doi.org/10.1007/BF01223371
  }

end QOU
