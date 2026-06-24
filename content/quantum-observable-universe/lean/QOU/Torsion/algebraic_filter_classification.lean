import Mathlib.Tactic

/-!
# QOU.Torsion.algebraic_filter_classification — fermion / boson via `[F_A, α]`

**Proposition** ([`prop:algebraic-filter-classification`](../../../quantum-observable-universe/lifting-and-descent/algebraic-filter-classification.md)).

*Let `F_A` be the substrate curvature and `α` be a harmonic 1-form
in the `q`-harmonic basis on branes.  The commutator `[F_A, α]`
classifies `α` into exactly one of two types:*

*(i) **Fermionic (matter)**: `[F_A, α] ≠ 0`.*

*(ii) **Bosonic (radiation)**: `[F_A, α] = 0`.*

The Lean encoding records the dichotomy as a `∀ α, fermionic α ∨
bosonic α` statement against an abstract context.

-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/algebraic-filter-classification.md
-/

namespace QOU.Torsion

/-- Abstract context for the algebraic-filter classification. -/
class AlgebraicFilterContext where
  /-- The substrate curvature `F_A`. -/
  F_A : Type
  /-- The `q`-harmonic 1-form space. -/
  OneForm : Type
  /-- The commutator `[F_A, α] : OneForm`. -/
  commutator : F_A → OneForm → OneForm
  /-- The "is fermionic / matter" predicate: `[F_A, α] ≠ 0`. -/
  IsFermionic : F_A → OneForm → Prop
  /-- The "is bosonic / radiation" predicate: `[F_A, α] = 0`. -/
  IsBosonic : F_A → OneForm → Prop
  /-- Zero 1-form (for the bosonic case). -/
  zero : OneForm
  /-- The two predicates' definitions: fermionic ⟺ commutator ≠ 0;
      bosonic ⟺ commutator = 0. -/
  fermionic_iff : ∀ F α, IsFermionic F α ↔ commutator F α ≠ zero
  bosonic_iff   : ∀ F α, IsBosonic F α ↔ commutator F α = zero

/-- **Algebraic-filter dichotomy** ([`prop:algebraic-filter-classification`]).

    Every harmonic 1-form `α` is exactly one of fermionic or bosonic. -/
-- Ref: [manuscript] quantum-observable-universe/lifting-and-descent/algebraic-filter-classification.md
theorem algebraic_filter_classification
    [ctx : AlgebraicFilterContext] (F : ctx.F_A) (α : ctx.OneForm) :
    ctx.IsFermionic F α ∨ ctx.IsBosonic F α := by
  -- The commutator either equals `zero` or it doesn't (LEM at the
  -- `OneForm` level — manuscript content is just this disjunction
  -- packaged with the two predicate definitions).
  by_cases h : ctx.commutator F α = ctx.zero
  · right
    exact (ctx.bosonic_iff F α).mpr h
  · left
    exact (ctx.fermionic_iff F α).mpr h

end QOU.Torsion
