import QOU.IwahoriHecke.Quotient

/-!
# `QOU.IwahoriHecke.Tw` — word products over the quadratic-only quotient

## 🛑 RETRACTION (2026-09-05, bean `qou-k4oq`)

This file used to declare a class `HeckeAnyonicSubstrate` and a theorem

```
theorem hecke_anyonic_substrate_structural :
    Nonempty (HeckeAnyonicSubstrate R q S) := ⟨inferInstance⟩
```

under the docstring *"**Discharge of `conj:hecke-anyonic-substrate`** … The conjecture's
claim … is now sorry-free at the algebra-existence level."* **That discharge was empty and
has been removed.** Four separate defects, each sufficient on its own:

1. **The class asserted almost nothing.** Its only fields were a function
   `Tw_gen : W → IwahoriHeckeQuot R q S` and `Tw_gen 1 = 1`. No Matsumoto
   well-definedness, no linear independence, no spanning — none of the content the
   docstring described. This is the `proof-claims-unencoded` pattern of AGENTS.md §3b-tax:
   a docstring enumerating properties the `Prop` fields do not carry.
2. **A stub instance was supplied to inhabit it.** `Tw_gen := fun w => if w = 1 then 1
   else 0` — the zero map away from the identity — with its own comment calling it a
   placeholder. §3b-tax: *"do not fabricate a trivial instance to close"* an open
   conjecture.
3. **It contradicted the canonical carrier.**
   `QOU.BraidKnot.HeckeAnyonicSubstrate` — the class the content block
   `conj:hecke-anyonic-substrate` actually points at — is content-bearing and carries **no
   instance**, stating in its own docstring that *"`conj:hecke-anyonic-substrate` is
   open"*. Two files in one tree, one declaring the conjecture open and the other
   declaring it discharged. They also **shared the class name**, so bare
   `HeckeAnyonicSubstrate` resolved to different objects depending on the open namespace —
   the same overload hazard AGENTS.md records for `markovZ`.
4. **The underlying algebra cannot support the claim anyway.** See the scope note below.

## 🛑 Scope: `IwahoriHeckeQuot` has NO braid relations

[`Quotient.lean`](Quotient.lean) is explicit that it imposes the Hecke **quadratic**
relation only — *"Imposing the quadratic relation alone yields a strictly larger algebra in
which the braid relations simply do not hold, so nothing downstream may assume them"*. The
braid step is tracked as bean `qou-phir`.

Matsumoto's theorem is exactly a statement about braid moves, so **no** part of the `T_w`
story can be told over this object: a braid move changes the product here. That is why the
`wordProduct` below is kept as what it honestly is — the product of a list of generators in
a quadratic-only quotient — and nothing is claimed about well-definedness on `W`.

## Where the real content lives

The word product **over the algebra that does impose both relations** is
[`QOU.IwahoriHecke.BraidWordInvariance`](BraidWordInvariance.lean), built on
`QOU.MathlibExt.IwahoriHecke.HeckeAlgebra`. It proves:

* `heckeWord_append` — concatenation of words is multiplication;
* `heckeWord_eq_of_braidMove` / `heckeWord_eq_of_braidEquiv` — **the algebra half of
  Matsumoto**: braid-equivalent words have equal products;
* `exists_Tw_of_braidEquiv` — the conditional theorem making the remaining gap exact: given
  the *group-theoretic* half (words with the same image in `W` are braid-equivalent),
  a well-defined `T_w` follows.

The group half is Matsumoto's theorem proper. **Mathlib** does not have it: `GroupTheory/
Coxeter/` supplies `IsReduced`, the length function, descents and inversion sequences, but
no exchange property and no Matsumoto.

🛑 **This corpus, however, DOES have the exchange property** — corrected 2026-09-06, the
earlier wording here ("and neither does this corpus") was wrong and was mine.
`QOU.Machinery.CoxeterReflectionCocycle.rightExchange` proves `RightExchangeProp cs` for
**every** Coxeter system, sorry-free, off `strong_exchange` (Björner–Brenti Thm 1.4.3). So
the chain from here is **deletion → Matsumoto**, not exchange → deletion → Matsumoto: the
first and hardest input is in hand.

✅ **And the rest of that chain landed on 2026-09-06.** `QOU.Machinery.CoxeterDeletion` has
deletion; `QOU.IwahoriHecke.Matsumoto` has Matsumoto, **hypothesis-free for every Coxeter
system** — so `Matsumoto.exists_Tw` gives the `T_w` map with nothing assumed, and
`exists_Tw_An` is its type-`A` specialisation. `DihedralExact` (that `σᵢσⱼ` has order exactly
`M i j`) was the corpus's own named open item, recorded as such in
`CoxeterGeometricRepresentationFull`'s HONESTY note; it is now proved in
`QOU.Machinery.CoxeterDihedralOrder.dihedralExact_full`. The named-hypothesis form below is
kept because it names its input rather than assuming it.

Refs:
- [matsumoto1964] DOI 10.1090/S0002-9904-1964-11211-9
- [humphreys1990] §7.4 (Iwahori-Hecke basis)
- [bourbaki1968] Ch IV §1 (braid + Hecke relations)
- [leitner2026] docs/workplans/2026-05-30-iwahori-hecke-mathlib-infra-plan.md; bean qou-k4oq
-/

namespace QOU.IwahoriHecke.Tw

open QOU.IwahoriHecke.Quotient

universe u v

variable {W : Type u} (R : Type v) [CommRing R] (q : R) (S : Set W) [DecidableEq W] [Group W]

/-- **Word product** in `IwahoriHeckeQuot R q S` for an explicit finite list of simple
reflections: `T_{s_{i_1}} · T_{s_{i_2}} · … · T_{s_{i_k}}`.

This is honest as stated and nothing more: it is a product of generators in the
quadratic-only quotient. It is **not** `T_w` — see the scope note in the module docstring,
and `QOU.IwahoriHecke.BraidWordInvariance` for the word product over the algebra that
actually imposes the braid relations. -/
noncomputable def wordProduct : List S → IwahoriHeckeQuot R q S
  | [] => 1
  | s :: rest => QOU.IwahoriHecke.Quotient.T R q S s * wordProduct rest

omit [DecidableEq W] [Group W] in
/-- **Empty word maps to 1** definitionally. -/
theorem wordProduct_nil : wordProduct R q S [] = 1 := rfl

omit [DecidableEq W] [Group W] in
/-- **Cons step**: the word-product on `s :: rest` factors as `T_s · wordProduct rest`. -/
theorem wordProduct_cons (s : S) (rest : List S) :
    wordProduct R q S (s :: rest) =
      QOU.IwahoriHecke.Quotient.T R q S s * wordProduct R q S rest := rfl

omit [DecidableEq W] [Group W] in
/-- **Singleton word**: the word product of `[s]` is `T_s`. -/
theorem wordProduct_singleton (s : S) :
    wordProduct R q S [s] = QOU.IwahoriHecke.Quotient.T R q S s := by
  rw [wordProduct_cons, wordProduct_nil, mul_one]

omit [DecidableEq W] [Group W] in
/-- **Concatenation is multiplication.** The one structural fact about `wordProduct` that
holds over the quadratic-only quotient, since it uses no relation at all — only
associativity. Everything beyond this needs the braid relations, which this quotient does
not impose. -/
theorem wordProduct_append (l₁ l₂ : List S) :
    wordProduct R q S (l₁ ++ l₂) = wordProduct R q S l₁ * wordProduct R q S l₂ := by
  induction l₁ with
  | nil => rw [List.nil_append, wordProduct_nil, one_mul]
  | cons s l ih =>
    rw [List.cons_append, wordProduct_cons, ih, wordProduct_cons, mul_assoc]

end QOU.IwahoriHecke.Tw
