import QOU.BraidKnot.SpechtDominanceCore

/-!
# Strict dominance on tabloids is well-founded — 3.14's inner induction measure

`PartitionLexWellFounded` supplies the **outer** axis of Mathas' Lemma 3.14: the lex order
across shapes.  This file supplies the **inner** one — dominance within a fixed shape, the
order 3.14's case (ii) inducts along (`ν = λ` with `u ⊵ s`, `v ⊵ t`).

Both ingredients were already here and, once again, neither was built for this:

* `SpechtDominanceCore.domRel_refl` / `_trans` / `_antisymm` — dominance is a genuine
  **partial** order on tabloids, proved sorry-free;
* `Specht.Tabloid.instFintype` — tabloids of a fixed shape are a `Fintype`.

The strict part of a partial order on a finite type is well-founded, so the two compose,
exactly as they did on the outer axis.

## Direction — and it matters

`domRel a b` reads "**`a` is dominated by `b`**".  3.14's case (ii) gives the induction
hypothesis for tableaux that **dominate** the one at hand, so the induction runs *up* the
order, and `domGtOn a b` below is "`a` strictly dominates `b`".  That mirrors
`lexGtOn`, where the hypothesis is available for lex-**greater** shapes.  Reversing either
would give a recursor whose hypothesis is the wrong way round — well-founded either way,
since the order is finite, and useless for the theorem.

## Scope

With this and `PartitionLexWellFounded.lexGtOn_wellFounded`, **both** of 3.14's axes have
a well-founded measure.  That does **not** make 3.14 proved, or even stated: the statement
also needs the two axes combined into a single measure (a lexicographic product), and then
the mathematics of the Garnir step itself.  What is settled is that neither axis can fail
to terminate.

Note also that dominance here is on **tabloids** — row-equivalence classes — which is the
standard object for the dominance order; a tableau's dominance is that of its class.

> **🛑 Read before writing an induction on this axis.**  The corpus holds an
> exact-arithmetic counterexample showing that a **Garnir step produces terms whose tabloids
> are dominance-INCOMPARABLE to the source's** — μ=(3,2), t=[[1,2,3],[5,4]] — and concludes
> *"no tabloid-level measure orders them"*.  It is in `SpechtStandardBasisCore.lean`
> §"Measure correction (2026-07-07)", which retired `domWeight` for exactly that reason and
> replaced it with the column-reading word `colWordNum`, on which the whole `q = 1`
> straightening argument then goes through sorry-free.
>
> **That does NOT refute this file**, and it is not being treated as if it did: the
> counterexample is about the `q = 1` *polytabloid* straightening, while Mathas 3.14's case
> (ii) is about *Murphy elements* and states `⊵` **non-strictly**, with case (i)'s lex drop
> doing the strict work.  The populations may be disjoint — `GarnirShapeCard.lexGtOn_garnirPartOf`
> shows a Garnir step drops the *shape*, so `murphyLex` descends on its outer axis there and
> never consults dominance.
>
> What it does establish is that this axis is **unvalidated for the descent it is meant to
> carry**, and that a validated alternative (`colWordNum`, with its monotonicity lemmas)
> already exists for the same job.  `murphyLex_wellFounded` proves the measure terminates;
> nothing yet proves 3.14's terms descend in it.  Settle that by measurement before building
> on it — [`docs/audits/2026-09-06-tabloid-dominance-vs-the-column-word-measure.md`](../../../../../docs/audits/2026-09-06-tabloid-dominance-vs-the-column-word-measure.md)
> names the probe.
-/

namespace QOU.BraidKnot.DominanceWellFounded

open QOU.BraidKnot.SpechtDominanceCore

variable {μ : YoungDiagram}

/-- **Strict dominance**: `domGtOn a b` says `a` strictly dominates `b`.  Note the
argument order matches `lexGtOn` — the first argument is the *greater* one. -/
def domGtOn (a b : Specht.Tabloid μ) : Prop := domRel b a ∧ b ≠ a

instance instIsIrreflDomGtOn : IsIrrefl (Specht.Tabloid μ) (domGtOn (μ := μ)) :=
  ⟨fun _ h => h.2 rfl⟩

instance instIsTransDomGtOn : IsTrans (Specht.Tabloid μ) (domGtOn (μ := μ)) := by
  refine ⟨fun a b c hab hbc => ⟨domRel_trans c b a hbc.1 hab.1, ?_⟩⟩
  -- if `c = a` then `a` and `b` dominate each other, contradicting `b ≠ a`
  rintro rfl
  exact hab.2 (domRel_antisymm _ _ hab.1 hbc.1)

/-- **The inner induction of Mathas 3.14 is well-founded.**  Strict dominance is the strict
part of a partial order, and tabloids of a fixed shape are finite. -/
theorem domGtOn_wellFounded (μ : YoungDiagram) :
    WellFounded (domGtOn (μ := μ)) :=
  Finite.wellFounded_of_trans_of_irrefl _

instance instIsWellFoundedDomGtOn : IsWellFounded (Specht.Tabloid μ) (domGtOn (μ := μ)) :=
  ⟨domGtOn_wellFounded μ⟩

/-- Recursion along strict dominance, in the shape an induction on tabloids uses: to prove
`C a`, it suffices to prove it given `C b` for every `b` that **strictly dominates** `a`. -/
theorem domGtOn_induction {μ : YoungDiagram} {C : Specht.Tabloid μ → Prop}
    (ih : ∀ a, (∀ b, domGtOn b a → C b) → C a) (a : Specht.Tabloid μ) : C a := by
  refine (domGtOn_wellFounded μ).induction (C := fun x => C x) a ?_
  intro x hx
  exact ih x fun b hb => hx b hb

end QOU.BraidKnot.DominanceWellFounded
