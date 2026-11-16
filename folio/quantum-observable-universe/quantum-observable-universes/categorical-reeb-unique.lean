import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Monoidal.Types.Basic


/-!
# QOU.CategoricalReeb.unique — uniqueness of the categorical Reeb derivation

Any two categorical Reeb derivations on the same QU with the same
weight decomposition coincide.  Uniqueness is a theorem (not an
axiom): given existence (recorded as an axiom pending Lie-algebra
infrastructure), the torus-action argument pins down (ξ, θ_A).

LaTeX: `\label{prop:categorical-reeb-unique}`

## References

- [leitner2026] §2-quantum-observable-universes/categorical-reeb-unique
- [witten1988] Topological Quantum Field Theory,
  https://doi.org/10.1007/BF01223371
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Reeb derivation** (inlined for standalone compilation;
    canonical definition lives in `categorical-reeb.lean`).

    The endomorphism `ξ : A → A` generating the `T`-action on the
    Frobenius–Hopf object `A`, equipped with a canonical 1-form `θ_A`
    satisfying the vertical-generator, normalisation, and kernel axioms. -/
structure CategoricalReeb (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The object of 1-forms `Ω¹(A)` in `C`. -/
  forms : C
  /-- The Reeb derivation `ξ : A → A`. -/
  xi : A ⟶ A
  /-- The canonical 1-form `θ_A`, abstractly a morphism `A → 𝟙`. -/
  theta : A ⟶ (𝟙_ C)
  /-- The vertical projection `π_V : Ω¹(A) → Ω¹(A)`. -/
  proj_V : forms ⟶ forms
  /-- The differential `d : A → Ω¹(A)`. -/
  d : A ⟶ forms
  /-- The interior product (contraction) `ι_ξ : Ω¹(A) → A`. -/
  contract_xi : forms ⟶ A
  /-- **Vertical generator**: `d ≫ π_V ≫ ι_ξ = ξ`. -/
  vertical_generator : d ≫ proj_V ≫ contract_xi = xi
  /-- **Normalisation**: `ξ ≫ θ_A = θ_A`. -/
  normalisation : xi ≫ theta = theta
  /-- **Kernel**: `π_V` idempotent. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V
  /-- **Kernel (horizontal)**: `ι_ξ ≫ d ≫ π_V = ι_ξ ≫ d`. -/
  kernel_horizontal : contract_xi ≫ d ≫ proj_V = contract_xi ≫ d

/-! **The former axiom `CategoricalReeb.unique_axiom` was false** (removed
    2026-11-15, with its wrapper `CategoricalReeb.unique`).

    The fields above do not determine `ξ` from `A`, `forms` and `π_V`:
    `d` and `ι_ξ` are free. In `Type` take `A = forms = Bool`,
    `π_V = d = id` and `ι_ξ = ξ`; every field holds for *any*
    `ξ : Bool → Bool` (`θ` lands in `PUnit`, so normalisation is
    automatic). With `ξ = id` and `ξ = not` the conclusion fails.
    `not_unique_unconstrained` below proves this.

    The manuscript argument pins `ξ` through the torus action, which these
    fields do not record. The repaired statement is open in Lean
    (bean `qou-n2un`). -/

/-- A Reeb structure on `Bool` in `Type` with any endomorphism as `ξ`. -/
def CategoricalReeb.boolReeb (f : Bool → Bool) : CategoricalReeb (Type) where
  A := Bool
  forms := Bool
  xi := f
  theta := fun _ => PUnit.unit
  proj_V := id
  d := id
  contract_xi := f
  vertical_generator := rfl
  normalisation := rfl
  proj_V_idem := rfl
  kernel_horizontal := rfl

/-- **The former axiom is false.** -/
theorem CategoricalReeb.not_unique_unconstrained :
    ¬ ∀ (r₁ r₂ : CategoricalReeb (Type)) (_h_A : r₁.A = r₂.A)
        (_h_forms : r₁.forms = r₂.forms) (_h_projV : HEq r₁.proj_V r₂.proj_V),
        HEq r₁.xi r₂.xi ∧ HEq r₁.theta r₂.theta := by
  intro h
  have h1 := (h (CategoricalReeb.boolReeb id) (CategoricalReeb.boolReeb not)
    rfl rfl HEq.rfl).1
  have h2 : (id : Bool → Bool) = not := eq_of_heq h1
  exact absurd (congrFun h2 true) (by decide)

end QOU
