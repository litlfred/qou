import Mathlib.CategoryTheory.Monoidal.Category
import Mathlib.CategoryTheory.Category.Basic
import Mathlib.CategoryTheory.Preadditive.Basic


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

The upstream structures `MaximalTorus` (`def:maximal-torus`),
`WeightDecomposition` (`def:weight-decomposition`) and `CategoricalReeb`
(`def:categorical-reeb`) live in sibling content blocks; minimal copies
are inlined here so this block elaborates standalone without an
inter-sibling import.  Keep the inlined copies in sync with their
canonical sibling blocks.
-/

open CategoryTheory MonoidalCategory

namespace QOU

universe u v

/-- **Maximal torus** (inlined from `def:maximal-torus`): the subgroup
    of `Aut⊗(ω)` acting diagonally on each weight space of the
    fundamental object `V`.

    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
structure MaximalTorus (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A` in `C` (from the QOU). -/
  hopfObj : C
  /-- The fundamental object `V` of categorical dimension 2. -/
  V : C
  /-- The fibre functor `ω : C → Type*` (from the QOU). -/
  fibreFunctor : Functor C (Type*)
  /-- **Faithfulness** of the fibre functor. -/
  fibreFunctor_faithful : Functor.Faithful fibreFunctor
  /-- The number of weight spaces of `V` under the torus action. -/
  numWeights : ℕ
  /-- The diagonal automorphism type (abstracting `T ≅ U(1)^r`). -/
  torusType : Type*
  /-- The torus carries a group structure. -/
  [torusGroup : Group torusType]
  /-- The torus embeds into the gauge group. -/
  embed : torusType → (fibreFunctor ≅ fibreFunctor)
  /-- **Diagonal action**: the image of `embed` is abelian. -/
  diagonal_action : ∀ (t₁ t₂ : torusType),
    (embed t₁).hom ≫ (embed t₂).hom = (embed t₂).hom ≫ (embed t₁).hom
  /-- **Maximality**: rank of the torus. -/
  rank : ℕ

/-- **Weight decomposition** (inlined from `def:weight-decomposition`):
    the `T`-weight decomposition of differential forms into horizontal
    (weight-0) and vertical (non-zero weight) components.

    Ref: [lusztig1993] https://doi.org/10.1007/978-0-8176-4717-9 -/
structure WeightDecomposition (C : Type u) [Category.{v} C]
    [MonoidalCategory C] [Preadditive C] where
  /-- The object of `k`-forms `Ω^k(A)` in `C`. -/
  forms : C
  /-- The horizontal projection `π_H` (weight-0). -/
  proj_H : forms ⟶ forms
  /-- The vertical projection `π_V` (non-zero weight). -/
  proj_V : forms ⟶ forms
  /-- Complementarity: `π_H + π_V = id`. -/
  complementary : proj_H + proj_V = 𝟙 forms
  /-- Idempotency of horizontal projection. -/
  proj_H_idem : proj_H ≫ proj_H = proj_H
  /-- Idempotency of vertical projection. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V

/-- **Categorical Reeb derivation** (inlined from `def:categorical-reeb`):
    the endomorphism `ξ : A → A` generating the `T`-action on the
    Frobenius–Hopf object `A`, with canonical 1-form `θ_A`.

    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
structure CategoricalReeb (C : Type u) [Category.{v} C]
    [MonoidalCategory C] where
  /-- The Frobenius–Hopf object `A`. -/
  A : C
  /-- The object of 1-forms `Ω¹(A)`. -/
  forms : C
  /-- The Reeb derivation `ξ : A → A`. -/
  xi : A ⟶ A
  /-- The canonical 1-form `θ_A : A → 𝟙` dual to `ξ`. -/
  theta : A ⟶ (𝟙_ C)
  /-- The vertical projection `π_V : Ω¹(A) → Ω¹(A)`. -/
  proj_V : forms ⟶ forms
  /-- The differential `d : A → Ω¹(A)`. -/
  d : A ⟶ forms
  /-- The interior product (contraction) `ι_ξ : Ω¹(A) → A`. -/
  contract_xi : forms ⟶ A
  /-- **Vertical generator**: `d ≫ π_V ≫ ι_ξ = ξ`. -/
  vertical_generator : d ≫ proj_V ≫ contract_xi = xi
  /-- **Normalisation**: `ξ ≫ θ = θ`. -/
  normalisation : xi ≫ theta = theta
  /-- Idempotency of the vertical projection. -/
  proj_V_idem : proj_V ≫ proj_V = proj_V
  /-- **Kernel** (horizontal forms = ker ι_ξ). -/
  kernel_horizontal : contract_xi ≫ d ≫ proj_V = contract_xi ≫ d

/-- **Smart constructor** for `CategoricalReeb`.

    Packages Reeb derivation components from a weight decomposition
    into the `CategoricalReeb` structure, using `wd.proj_V` for the
    vertical projection.

    This is a constructor (`.mk`), not a derivation — the caller
    must supply `ξ`, `θ_A`, `d`, `ι_ξ`, and the three property proofs.
    See `categorical_reeb_exists` below for the existence axiom.

    Ref: [witten1988] https://doi.org/10.1007/BF01223371 -/
noncomputable def CategoricalReeb.fromWeightDecomposition
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
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
    is not available in Mathlib as of 2026-03.

    **Was an axiom; now proved (2026-11-15), but only because the
    statement is weak.** The fields do not exclude `ξ = θ = d = ι_ξ = 0`,
    so the zero Reeb structure on `wd.forms` witnesses it. The intended
    content (`ξ` is the torus generator) is not recorded by the structure
    and is open in Lean (bean `qou-n2un`). -/
-- Ref: [witten1988] Witten, "Topological quantum field theory," Comm. Math. Phys. 117 (1988)
theorem categorical_reeb_exists
    {C : Type u} [Category.{v} C] [MonoidalCategory C] [Preadditive C]
    (_mt : MaximalTorus C) (wd : WeightDecomposition C)
    (A : C) :
    ∃ (reeb : CategoricalReeb C),
      reeb.forms = wd.forms ∧ HEq reeb.proj_V wd.proj_V :=
  ⟨{ A := A
     forms := wd.forms
     xi := 0
     theta := 0
     proj_V := wd.proj_V
     d := 0
     contract_xi := 0
     vertical_generator := by simp
     normalisation := by simp
     proj_V_idem := wd.proj_V_idem
     kernel_horizontal := by simp }, rfl, HEq.rfl⟩

end QOU
