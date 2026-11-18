import Mathlib.Algebra.Algebra.Hom
import Mathlib.Algebra.Algebra.Prod
import Mathlib.Logic.Function.Basic

/-!
# QOU.DescentLemma — Descent preserves the quantum observable universe

**Lemma** ([`lem:descent`](descent-lemma.md)).

The restriction morphism `rₙ : Aₙ → A_{n-1}` yields a Frobenius–Hopf object
such that `(C, A_{n-1}, τ)` is again a QOU. The induced descent homomorphism
`𝔡ₙ : End_C(Aₙ) → End_C(A_{n-1})` is a **surjective algebra homomorphism**,
and it **intertwines the `G_q`-actions** across levels `n` and `n − 1`.

## 2026-09-03 — the conclusion was a field, and the encoding was weaker in
## three separate ways

`structure DescentLemma` carried `endAlgN`, `endAlgPrev` and `descentMap` as
data plus `surjective : Function.Surjective descentMap` — the lemma's
conclusion verbatim — and `descent_surjective` returned that field. AGENTS.md
§3b-cond item 5: with the map chosen by whoever builds the structure, "the
descent map is surjective" reduces to "the surjective map I supplied is
surjective".

A bundled *definition* whose fields are its own axioms would be the accessor
idiom and not a defect. This is not that: the block is a **lemma**
(`label: "lem:descent"`), and its content is that the actual restriction
morphism *yields* such a datum. Nothing here constructs one, so the assertion
was empty rather than merely unproved.

**And the encoding said less than the `.md` in three ways**, none of them
noted in the file:

1. **`→ₗ[R]`, not an algebra map.** The `.md` says *surjective **algebra**
   homomorphism*; a `LinearMap` drops multiplicativity entirely. Corrected
   here to `→ₐ[R]`.
2. **The `G_q`-intertwining is absent.** The `.md`'s second sentence about
   `𝔡ₙ` has no counterpart at all.
3. **The QOU-preservation claim is absent.** That `(C, A_{n-1}, τ)` is again
   a quantum observable universe — the first thing the lemma asserts — is
   nowhere in the Lean.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`descent_surjective` is now a **`Prop`-valued definition over a
caller-supplied algebra homomorphism**. A caller with an actual `𝔡ₙ` takes it
as a hypothesis, and it constrains them because the map is theirs.

`descentSurjective_comp` **derives** the tower statement: descent through two
levels is surjective when each step is. That is what makes the lemma worth
having for a tower `{Aₙ}_{n ≥ 0}` rather than for one pair of levels, and it
is the one consequence available without constructing `End_C(Aₙ)`.

`not_descentSurjective_diagonal` refutes the claim at a concrete algebra map
— the diagonal `ℤ →ₐ[ℤ] ℤ × ℤ`, whose image misses `(1, 0)` — so an unproved
placeholder over it would read as "true, not yet proved" about something false.

## What is still unencoded

Everything the lemma is about: the brane tower `{Aₙ}`, the restriction
morphism `rₙ`, the Frobenius–Hopf structure, `End_C(Aₙ)`, the `G_q`-actions
and the intertwining, and the archimedean realisation as a surjective
`*`-homomorphism of section algebras. The two algebras and the map are
caller-supplied.

## References

- [leitner2026] §3 Lifting and Descent
-/

namespace QOU

/-- **Surjectivity of a descent homomorphism** ([`lem:descent`]), as a
proposition over a caller-supplied algebra map.

`𝔡ₙ : End_C(Aₙ) →ₐ[R] End_C(A_{n-1})` is surjective.

**Named, not asserted.** An algebra homomorphism rather than a linear one,
matching the `.md`; see the module docstring for the two claims of the lemma
that remain unencoded. -/
-- Ref: [leitner2026] §3 Lifting and Descent
def descent_surjective {R A B : Type*} [CommSemiring R] [Semiring A] [Semiring B]
    [Algebra R A] [Algebra R B] (descentMap : A →ₐ[R] B) : Prop :=
  Function.Surjective descentMap

/-- **Descent through the tower, derived.**

If each one-step descent is surjective then so is their composite, so
surjectivity propagates from level `n` down to any lower level of the brane
tower `{Aₙ}_{n ≥ 0}`.

This is why the lemma is stated for a tower rather than a single pair, and it
is the one consequence obtainable without constructing `End_C(Aₙ)`. -/
-- Ref: [leitner2026] §3 Lifting and Descent
theorem descentSurjective_comp {R A B C : Type*} [CommSemiring R]
    [Semiring A] [Semiring B] [Semiring C]
    [Algebra R A] [Algebra R B] [Algebra R C]
    {f : A →ₐ[R] B} {g : B →ₐ[R] C}
    (hf : descent_surjective f) (hg : descent_surjective g) :
    descent_surjective (g.comp f) :=
  hg.comp hf

/-- **The claim is refutable at a concrete algebra map**, which is why it is
named rather than carried as an unproved placeholder.

The diagonal `ℤ →ₐ[ℤ] ℤ × ℤ` is an algebra homomorphism whose image misses
`(1, 0)`: a preimage would have to equal `1` in the first coordinate and `0`
in the second. -/
theorem not_descentSurjective_diagonal :
    ¬ descent_surjective (Algebra.ofId ℤ (ℤ × ℤ)) := by
  intro h
  obtain ⟨r, hr⟩ := h (1, 0)
  have h1 : r = 1 := congrArg Prod.fst hr
  have h2 : r = 0 := congrArg Prod.snd hr
  omega

/-- **`G_q`-intertwining of a descent homomorphism** ([`lem:descent`]):
    the algebra map `descentMap : A →ₐ[R] B` intertwines caller-supplied
    actions `actA : G → A → A` and `actB : G → B → B` across adjacent levels. -/
def descent_intertwines {R A B G : Type*} [CommSemiring R] [Semiring A] [Semiring B]
    [Algebra R A] [Algebra R B] (descentMap : A →ₐ[R] B)
    (actA : G → A → A) (actB : G → B → B) : Prop :=
  ∀ (g : G) (x : A), descentMap (actA g x) = actB g (descentMap x)

/-- **`G_q`-intertwining composes across the brane tower.**
    If `f : A →ₐ[R] B` intertwines `actA` with `actB` and `g : B →ₐ[R] C`
    intertwines `actB` with `actC`, then `g.comp f` intertwines `actA` with `actC`. -/
theorem descentIntertwines_comp {R A B C G : Type*} [CommSemiring R]
    [Semiring A] [Semiring B] [Semiring C]
    [Algebra R A] [Algebra R B] [Algebra R C]
    {f : A →ₐ[R] B} {g : B →ₐ[R] C}
    {actA : G → A → A} {actB : G → B → B} {actC : G → C → C}
    (hf : descent_intertwines f actA actB)
    (hg : descent_intertwines g actB actC) :
    descent_intertwines (g.comp f) actA actC := by
  intro γ x
  change g (f (actA γ x)) = actC γ (g (f x))
  rw [hf γ x, hg γ (f x)]

/-- **Concrete model of a surjective descent homomorphism:** the first-factor
    projection `AlgHom.fst R A B : A × B →ₐ[R] A` is surjective whenever `B` is
    inhabited (for instance by `0 : B`). -/
theorem descentSurjective_fst (R A B : Type*) [CommSemiring R]
    [Semiring A] [Semiring B] [Algebra R A] [Algebra R B] :
    descent_surjective (AlgHom.fst R A B) := by
  intro a
  refine ⟨(a, 0), ?_⟩
  rfl

/-- The first-factor projection `AlgHom.fst R A B` intertwines any diagonal
    product action `(a, b) ↦ (actA g a, actB g b)` with `actA`. -/
theorem descentIntertwines_fst (R A B G : Type*) [CommSemiring R]
    [Semiring A] [Semiring B] [Algebra R A] [Algebra R B]
    (actA : G → A → A) (actB : G → B → B) :
    descent_intertwines (AlgHom.fst R A B)
      (fun g p => (actA g p.1, actB g p.2)) actA := by
  intro g p
  change (actA g p.1, actB g p.2).1 = actA g p.1
  rfl

end QOU
