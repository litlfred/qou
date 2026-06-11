import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.CategoricalReeb.mk — Smart constructor for Reeb data

Packages the Reeb derivation components (ξ, θ_A, d, ι_ξ) together
with the three property proofs (vertical generator, normalisation,
kernel) into a `CategoricalReeb` structure.

This is a smart constructor, not an existence proof: it takes the
components and proofs as inputs and validates that they form a
consistent `CategoricalReeb`.  Constructing ξ from the torus action
requires the infinitesimal generator of a one-parameter subgroup,
which needs Lie algebra infrastructure not yet in Mathlib.

The existence theorem (that every QOU with a weight decomposition
admits such data) is recorded as an axiom below.

LaTeX: `\label{thm:categorical-reeb-exists}`
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Smart constructor** for `CategoricalReeb`.

    Packages Reeb derivation components from a weight decomposition
    into the `CategoricalReeb` structure, using `wd.proj_V` for the
    vertical projection.

    This is a constructor (`.mk`), not a derivation — the caller
    must supply `ξ`, `θ_A`, `d`, `ι_ξ`, and the three property proofs.
    See `categorical_reeb_exists` below for the existence axiom.

    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
noncomputable def CategoricalReeb.fromWeightDecomposition
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (_mt : MaximalTorus C) (wd : WeightDecomposition C)
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

/-- **Existence of the categorical Reeb derivation**.

    Every quantum observable universe with a maximal torus `T` and
    weight decomposition `(π_H, π_V)` admits a Reeb derivation
    `(ξ, θ_A)` satisfying all three properties.

    The construction is:
    1. `ξ` is the infinitesimal generator of the `T ≅ U(1)` action
       (`d/dt|_{t=0}` of the one-parameter subgroup).
    2. `θ_A` is the Maurer–Cartan form dual to `ξ`.
    3. `ι_ξ` is the interior product (contraction with ξ).
    4. `d` is the differential from the QOU's Kähler structure.

    Formalising this requires Lie algebra infrastructure (infinitesimal
    generators of compact group actions on categorical objects) which
    is not available in Mathlib as of 2026-03. -/
-- Ref: [witten1988] Witten, "Topological quantum field theory," Comm. Math. Phys. 117 (1988)
axiom categorical_reeb_exists
    {C : Type u} [Category.{v} C] [MonoidalCategory C]
    (mt : MaximalTorus C) (wd : WeightDecomposition C)
    (A : C) :
    ∃ (reeb : CategoricalReeb C),
      reeb.forms = wd.forms ∧ reeb.proj_V = wd.proj_V

end QOU
