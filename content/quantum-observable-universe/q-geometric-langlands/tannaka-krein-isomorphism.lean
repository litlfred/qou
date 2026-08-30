import Mathlib.CategoryTheory.Equivalence
import Mathlib.CategoryTheory.Monoidal.Category

/-!
# QOU.AlgebraicSubstrate.tannaka_krein_isomorphism

Tannaka–Krein duality for the substrate, as a named hypothesis class.

## What this file used to be, and why it changed (2026-08-30)

Two `axiom`s and a theorem laundered through one of them:

```lean
axiom RepLoc : Type (u + 1)
axiom ComodH : Type (u + 1)
axiom tannaka_krein_isomorphism_axiom : Nonempty (RepLoc ≃ ComodH)
theorem tannaka_krein_isomorphism : Nonempty (RepLoc ≃ ComodH) :=
  tannaka_krein_isomorphism_axiom
```

Three separate defects, and the third is the one that matters most:

1. **The types were unconstrained.** `RepLoc` and `ComodH` were opaque `axiom`s
   with no structure whatsoever, so `Nonempty (RepLoc ≃ ComodH)` asserted a
   bijection between two arbitrary types. That is satisfiable by taking both to
   be `ULift Bool` and says nothing about representation categories. Already
   flagged `da-vacuous` in
   `docs/audits/2026-07-02-lean-proof-progress-qa-table.md` line 729.

2. **`≃` is `Equiv`, a bijection of TYPES.** The narrative claims
   `Rep_loc(A) ≃ Comod(H_ξ)` as an equivalence of *categories*, which is `≌`.
   Even had the types been the right ones, the statement would have been about
   their underlying object types, forgetting every morphism —
   `da-lean-narrative-divergence`.

3. **The theorem was its own axiom.** `tannaka_krein_isomorphism` proved nothing;
   it returned the axiom asserting it. This is the shape §"Axiomatization is NOT
   a Proof" names: sorry-free, `#print axioms`-dirty, and indistinguishable from
   a result unless you read the proof term.

## What it is now

`IsTannakaKreinDual` takes the two categories as **parameters** — nothing opaque
— and carries the claim the narrative actually makes:

* an equivalence of **categories** (`≌`, not `≃`), and
* **compatibility with the fibre functors**: that equivalence commutes with `τ`
  up to natural isomorphism.

The second field is the content of Tannaka–Krein rather than a decoration. The
reconstruction theorem's force is that `H_ξ` is determined *by the fibre functor
on the monoidal category*; an equivalence that did not lie over `τ` would not be
the duality being claimed. Stating only `Nonempty (RepLoc ≌ ComodH)` would be
weaker in a way that matters — many inequivalent Hopf algebras have equivalent
comodule categories, and it is exactly the fibre functor that separates them.

The two are one field, not two, because the compatibility must hold *of the same*
`e`: as separate fields they would permit an equivalence and an unrelated
natural isomorphism, which is not a statement about either.

**No instance is provided for the substrate's own categories.** That is the
conjecture, and it is why the sibling block is a `conjecture` rather than a
`theorem`. `isTannakaKreinDual_refl` witnesses that the class is inhabited, so it
is not an empty carrier — but see its docstring for what that does and does not
establish.
-/

set_option autoImplicit false

namespace QOU.AlgebraicSubstrate

open CategoryTheory

universe u v w

/-- **Tannaka–Krein duality, as a named hypothesis.**

    `RepLoc` and `ComodH` are the two categories; `τR` and `τC` are their fibre
    functors to a common target `E` (the fibre at the unit defect, in the
    narrative). The single field says: there is an equivalence of categories
    between them *lying over the fibre functors*.

    Parameters, not axioms — an instance must supply real categories and real
    functors, and then exhibit the equivalence. Nothing here is opaque. -/
-- Ref: [tannaka1939] Tannaka, Über den Dualitätssatz der nichtkommutativen topologischen Gruppen, Tôhoku Math. J. 45 (1939) 1-12 (Tannaka–Krein duality)
-- Ref: [deligne1990] Catégories tannakiennes, in The Grothendieck Festschrift II, 111-195 (reconstruction from a fibre functor)
class IsTannakaKreinDual
    (RepLoc : Type u) [Category.{v} RepLoc]
    (ComodH : Type u) [Category.{v} ComodH]
    {E : Type u} [Category.{w} E]
    (τR : RepLoc ⥤ E) (τC : ComodH ⥤ E) : Prop where
  /-- An equivalence of **categories** commuting with the fibre functors:
      `τ_C ∘ e ≅ τ_R`. One field rather than two, so that the compatibility is
      asserted of the same equivalence. -/
  equiv_over_fibre : ∃ e : RepLoc ≌ ComodH, Nonempty (e.functor ⋙ τC ≅ τR)

/-- The duality itself, as the conjecture's statement: given the hypothesis, an
    equivalence of categories over the fibre functors exists.

    A projection, and labelled as one. It exists so the conjecture has a name to
    be cited by, not to suggest anything was derived. -/
theorem tannaka_krein_isomorphism
    (RepLoc : Type u) [Category.{v} RepLoc]
    (ComodH : Type u) [Category.{v} ComodH]
    {E : Type u} [Category.{w} E]
    (τR : RepLoc ⥤ E) (τC : ComodH ⥤ E)
    [IsTannakaKreinDual RepLoc ComodH τR τC] :
    ∃ e : RepLoc ≌ ComodH, Nonempty (e.functor ⋙ τC ≅ τR) :=
  IsTannakaKreinDual.equiv_over_fibre

/-! ## Non-vacuity

The class is inhabited: a category is dual to itself over its own fibre functor,
via the identity equivalence.

**What this establishes and what it does not.** It rules out the failure mode the
old file had — a carrier no datum satisfies, or one any `⟨True⟩` discharges —
and it is not much more than that: the witness is the *identity*, so it exhibits
no interesting duality. What makes the conjecture a conjecture is that
`Rep_loc(A)` and `Comod(H_ξ)` are **different** categories, and nothing here
relates them. Satisfiability of the shape is a floor, not evidence. -/

/-- Any category is Tannaka–Krein dual to itself over its own fibre functor.

    **Deliberately a `theorem` and not an `instance`.** As an instance it would
    be *general* — quantified over every `C` and `τ` — so typeclass resolution
    would discharge any `[IsTannakaKreinDual A B τR τC]` whose two sides happen
    to unify, silently, in a downstream result whose author meant them to be
    different categories. The whole point of this class is that the hypothesis is
    hard; an instance that supplies it for free where the arguments coincide is a
    trapdoor.

    Contrast `instance : IsWeilZeta weilZetaExample` in
    `QOU.AlgebraicSubstrate.WeilZeta`, which is an instance on a **concrete**
    witness and therefore cannot fire spuriously. Generality is the difference,
    not the fact of being a witness. -/
theorem isTannakaKreinDual_refl
    (C : Type u) [Category.{v} C] {E : Type u} [Category.{w} E] (τ : C ⥤ E) :
    IsTannakaKreinDual C C τ τ :=
  ⟨⟨CategoryTheory.Equivalence.refl, ⟨Functor.leftUnitor τ⟩⟩⟩

end QOU.AlgebraicSubstrate
