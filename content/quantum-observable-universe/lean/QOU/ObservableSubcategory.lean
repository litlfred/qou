import Mathlib.Tactic

/-!
# QOU.ObservableSubcategory

**Canonical declaration** for content block at
[`quantum-observable-universe/information-theory/observable-subcategory.ts`](quantum-observable-universe/information-theory/observable-subcategory.ts).

Formalises the manuscript **definition** of the observable subcategory
`Bun°(ℙ(V)) = { 𝒮 ∈ Bun(ℙ(V)) : Γ(𝒮, A₀) ≠ 0 }` — the full subcategory of
objects whose degree-0 algebra is non-trivial (the regime where the
Frobenius pairing is non-degenerate and degree-0 measurements are defined).
-/

namespace QOU

/-- Data for the observable subcategory `Bun°(ℙ(V))`.

    A `definition` carrier: `Obj` are the objects of the ambient bundle
    category, `A0section 𝒮` is the degree-0 section `Γ(𝒮, A₀)` (its
    non-vanishing is the observability criterion), and `isObservable` is the
    membership predicate, pinned to `A0section 𝒮 ≠ 0`. -/
structure ObservableSubcategory where
  /-- Objects of the ambient bundle category `Bun(ℙ(V))`. -/
  Obj : Type
  /-- The degree-0 section `Γ(𝒮, A₀)` (scalar proxy; observability turns on
      its non-vanishing). -/
  A0section : Obj → ℝ
  /-- Membership in the observable subcategory `Bun°`. -/
  isObservable : Obj → Prop
  /-- Defining identity: `𝒮 ∈ Bun°` iff its degree-0 section is non-zero. -/
  observable_iff : ∀ S, isObservable S ↔ A0section S ≠ 0

-- Ref: [manuscript] quantum-observable-universe/information-theory/observable-subcategory.ts

/-- The complement `Bun ∖ Bun°` is exactly the `A₀ = 0` locus (jet horizons
    and big-bang states) — manuscript "Complement". -/
theorem ObservableSubcategory.not_observable_iff
    (C : ObservableSubcategory) (S : C.Obj) :
    ¬ C.isObservable S ↔ C.A0section S = 0 := by
  rw [C.observable_iff, not_ne_iff]

end QOU
