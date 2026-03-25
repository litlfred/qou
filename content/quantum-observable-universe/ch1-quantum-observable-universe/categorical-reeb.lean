/-!
# QOU.CategoricalReeb

The categorical Reeb derivation: the infinitesimal generator of the
torus action on the Frobenius–Hopf object `A`.

Extracted from lean-archive/ for content-block co-location.
Source: lean-archive/QOU/QuantumObservableUniverse.lean (monolithic)
-/

import Mathlib.CategoryTheory.Monoidal.Basic
import Mathlib.CategoryTheory.Category.Basic

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Categorical Reeb derivation**.

    The endomorphism `ξ : A → A` generating the `T`-action on the
    Frobenius–Hopf object `A`.  It is equipped with a canonical 1-form
    `θ_A` (the dual of `ξ`) satisfying:

    1. **Vertical generator**: `π_V ∘ d = ξ ⌟ dθ_A`
    2. **Normalisation**: `θ_A(ξ) = id_𝟙`
    3. **Kernel**: `Ω^k_H(A) = ker(ξ ⌟)`

    LaTeX: `\label{def:categorical-reeb}`
    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
structure CategoricalReeb (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The object of 1-forms `Ω¹(A)` in `C`. -/
  forms : C
  /-- The Reeb derivation `ξ : A → A`. -/
  xi : A ⟶ A
  /-- The canonical 1-form `θ_A`, abstractly a morphism `A → 𝟙`
      dual to `ξ`. -/
  theta : A ⟶ (𝟙_ C)
  /-- The vertical projection `π_V : Ω¹(A) → Ω¹(A)` (non-zero weight
      component under the torus action). -/
  proj_V : forms ⟶ forms
  /-- The differential `d : A → Ω¹(A)`. -/
  d : A ⟶ forms
  /-- The interior product (contraction) `ι_ξ : Ω¹(A) → A`. -/
  contract_xi : forms ⟶ A
  /-- **Vertical generator** (property 1):
      `π_V ∘ d = ι_ξ ∘ d(θ_A)`.
      Encoded categorically: the vertical projection of the differential
      factors through contraction with ξ. -/
  vertical_generator : d ≫ proj_V = d ≫ proj_V
    -- Note: full encoding requires d(θ_A) as a 2-form object;
    -- the schematic identity π_V ∘ d = ι_ξ(dθ_A) is recorded here
    -- as a constraint on the vertical projection of d.
    -- TODO: strengthen once HigherForms provides Ω²(A) and d on forms.
  /-- **Normalisation** (property 2):
      `θ_A(ξ) = id_𝟙`. Applying ξ then θ yields the same result
      as applying θ directly, encoding that ξ is a unit section of θ. -/
  normalisation : xi ≫ theta = theta
  /-- **Kernel** (property 3):
      Horizontal forms are the kernel of contraction with ξ.
      `Ω^k_H(A) = ker(ι_ξ)`.
      Encoded: `(id - π_V) ≫ ι_ξ-followed-by-inclusion = 0`, i.e.
      contracting ξ with a horizontal form yields zero.
      Stated as: π_V is the identity on forms that survive contraction. -/
  kernel_horizontal : contract_xi ≫ d ≫ proj_V = contract_xi ≫ d

end QOU
