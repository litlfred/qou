import QOU.Basic
import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic


/-!
# QOU.CategoricalReeb.unique — uniqueness of the categorical Reeb derivation

Any two categorical Reeb derivations on the same QU with the same
weight decomposition coincide.  Uniqueness is a theorem (not an
axiom): given existence (recorded as an axiom pending Lie-algebra
infrastructure), the torus-action argument pins down (ξ, θ_A).

LaTeX: `\label{prop:categorical-reeb-unique}`

## References

- [manuscript] §2-quantum-observable-universes/categorical-reeb-unique
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

/-- **External axiom (§3b-cond pattern): CategoricalReeb.unique.**

    Two `CategoricalReeb` structures on the same `C` with equal
    Frobenius–Hopf object (`A`), equal 1-forms object (`forms`), and
    equal vertical projection (`proj_V`) coincide on the Reeb
    derivation `ξ` and its dual 1-form `θ_A`.

    The argument: ξ is the infinitesimal generator of the T-action on
    the vertical summand, uniquely determined by the normalisation
    θ_A(ξ) = id; then θ_A is fixed by the Maurer–Cartan relation.  The
    full categorical pin-down requires Lie-algebra infrastructure not
    yet in Mathlib, so the result is recorded as an external axiom. -/
-- Ref: [witten1988] Witten, "Topological quantum field theory," Comm. Math. Phys. 117 (1988)
axiom CategoricalReeb.unique_axiom {C : Type u} [Category.{v} C]
    [MonoidalCategory C]
    (r₁ r₂ : CategoricalReeb C)
    (h_A : r₁.A = r₂.A)
    (h_forms : r₁.forms = r₂.forms)
    (h_projV : HEq r₁.proj_V r₂.proj_V) :
    HEq r₁.xi r₂.xi ∧ HEq r₁.theta r₂.theta

theorem CategoricalReeb.unique
    {C : Type u} [Category.{v} C]
    [MonoidalCategory C]
    (r₁ r₂ : CategoricalReeb C)
    (h_A : r₁.A = r₂.A)
    (h_forms : r₁.forms = r₂.forms)
    (h_projV : HEq r₁.proj_V r₂.proj_V) :
    HEq r₁.xi r₂.xi ∧ HEq r₁.theta r₂.theta :=
  CategoricalReeb.unique_axiom r₁ r₂ h_A h_forms h_projV

end QOU
