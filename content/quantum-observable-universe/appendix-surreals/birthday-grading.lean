/-
  Birthday grading on a surreal-coefficient category.

  Axiomatisation of the ordinal-valued grading b : K → Ord on a
  real-closed field K extending ℝ (target: K = Conway's surreals
  No).  Induces a filtration on each K-linear hom-space.

  ## References
  - [conway1976] Conway, *On Numbers and Games*, Academic Press.
  - [gonshor1986] Gonshor, *An Introduction to the Theory of
    Surreal Numbers*, Cambridge University Press.
    https://doi.org/10.1017/CBO9780511629143
-/

import Mathlib.SetTheory.Ordinal.Basic
import Mathlib.Order.Filter.Basic

namespace QOU.AppendixSurreals

universe u

/-- A **surreal-coefficient field** `K` is a linearly ordered field
    extending `ℝ` equipped with a birthday function `K → Ordinal`
    satisfying Conway's recursive construction axioms.

    We axiomatise `K` rather than construct it, since mathlib's
    surreal-number development (`SetTheory.Game.Surreal`) does not
    yet expose a real-closed-field witness. -/
class SurrealField (K : Type u) extends LinearOrderedField K where
  /-- Conway's birthday function. -/
  birthday : K → Ordinal
  /-- Zero has birthday zero. -/
  birthday_zero : birthday 0 = 0
  /-- One has birthday one. -/
  birthday_one : birthday 1 = 1
  /-- Sum birthday bounded by natural sum
      (`Ordinal.natAdd`, denoted `α ⊕ β`). -/
  birthday_add_le : ∀ x y, birthday (x + y) ≤ birthday x ⊕ birthday y
  /-- Product birthday bounded by natural product. -/
  birthday_mul_le : ∀ x y, birthday (x * y) ≤ birthday x ⊗ birthday y

/-- The **birthday grading** on a `K`-linear category `C` is an
    ordinal-indexed filtration of each hom-space.

    We axiomatise the filtration rather than derive it: in practice
    a birthday grading on `C = Rep(SU_q(2))` at `q = 1 + ε` is
    built by hand from the Hoefsmit matrix-entry birthdays. -/
structure BirthdayGrading
    (K : Type u) [SurrealField K]
    (Hom : Type u) [AddCommGroup Hom] [Module K Hom] where
  /-- The birthday-`≤ α` subgroup of each hom-space. -/
  filter : Ordinal → Submodule K Hom
  /-- The filtration is monotone in `α`. -/
  mono : ∀ {α β : Ordinal}, α ≤ β → filter α ≤ filter β
  /-- The filtration exhausts the hom-space. -/
  exhaustive : ⨆ α, (filter α : Set Hom) = Set.univ
  /-- The archimedean sub-hom is birthday `≤ ω`. -/
  archimedeanPart : Submodule K Hom := filter Ordinal.omega

/-- A **morphism of birthday-graded hom-spaces** preserves filter stage
    up to ordinal natural-sum. -/
-- Ref: [conway1976], [gonshor1986]
structure BirthdayGradedMorphism
    (K : Type u) [SurrealField K]
    {H₁ H₂ : Type u}
    [AddCommGroup H₁] [Module K H₁] (G₁ : BirthdayGrading K H₁)
    [AddCommGroup H₂] [Module K H₂] (G₂ : BirthdayGrading K H₂) where
  /-- Underlying `K`-linear map. -/
  toLinear : H₁ →ₗ[K] H₂
  /-- The ordinal shift induced by composition. -/
  shift : Ordinal
  /-- Preservation of filter stage up to `shift`. -/
  filter_le :
    ∀ α : Ordinal,
      (G₁.filter α).map toLinear ≤ G₂.filter (α ⊕ shift)

-- The existence of a birthday grading on
-- `Rep_{𝐍𝐨}(SU_q(2))` at `q = 1 + ε` is conjectural pending
-- mathlib's surreal-analysis development.
-- Ref: [gonshor1986]
theorem birthday_grading_exists_conjecture
    (K : Type u) [SurrealField K]
    (Hom : Type u) [AddCommGroup Hom] [Module K Hom] :
    Nonempty (BirthdayGrading K Hom) := by
  -- Ref: [gonshor1986] — construction via sign-sequence length.
  sorry

end QOU.AppendixSurreals
