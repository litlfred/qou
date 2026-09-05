import QOU.BraidKnot.PartitionLex
import QOU.Mathlib.YoungLatticeCornerCount

/-!
# The lex order on partitions of `n` is well-founded — 3.14's outer induction measure

Mathas' Lemma 3.14 is a **double** induction: lexicographic across shapes (case (i),
`ν >ₗ λ`) and dominance within a fixed shape (case (ii), `ν = λ` with `u ⊵ s`).  Neither
half can even be *stated* as an induction until its measure is known to be well-founded.

This file supplies the outer one.

## Why it is short, and where each piece came from

Both halves were already in the corpus and neither was built for this:

* `PartitionLex.partitionLexGt_irrefl` and `partitionLexGt_trans` — the lex order is a
  strict order (proved when the order was introduced, to settle that Mathas' 3.12 step is
  lex and not dominance);
* `QOU.Mathlib.fintypeSizedDiagram` — diagrams of a fixed size are a `Fintype`,
  transported from `Nat.Partition n`, built for the Young-lattice corner count.

A strict order on a finite type is well-founded, so the two compose in one line.  The
point of the file is not the proof but that the composition **exists**: without a
`Fintype` on shapes of fixed size, the outer induction of 3.14 would need a numeric
measure and a monotonicity argument, and that is a real piece of work this corpus does not
have to do.

## What is NOT here

The **inner** measure — dominance on tableaux of a fixed shape — is a separate
well-foundedness obligation and is not addressed.  `SpechtDominanceCore.domRel` exists;
whether it is proved to be a strict order, and whether tableaux of a fixed shape carry a
`Fintype`, has not been checked here.  Do not read this file as "3.14's induction is
justified" — it justifies one of its two axes.
-/

namespace QOU.BraidKnot.PartitionLexWellFounded

open QOU.BraidKnot.PartitionLex

/-- Partitions of `n`, as diagrams of that size. -/
abbrev PartOf (n : ℕ) := {μ : YoungDiagram // μ.cells.card = n}

/-- The lexicographic order restricted to shapes of one size — the order 3.14's case (i)
inducts along. -/
def lexGtOn (n : ℕ) (a b : PartOf n) : Prop := partitionLexGt a.1 b.1

instance instIsIrreflLexGtOn (n : ℕ) : IsIrrefl (PartOf n) (lexGtOn n) :=
  ⟨fun a => partitionLexGt_irrefl a.1⟩

instance instIsTransLexGtOn (n : ℕ) : IsTrans (PartOf n) (lexGtOn n) :=
  ⟨fun _ _ _ hab hbc => partitionLexGt_trans hab hbc⟩

/-- **The outer induction of Mathas 3.14 is well-founded.**  A strict order on a finite
type is well-founded, and shapes of a fixed size are finite. -/
theorem lexGtOn_wellFounded (n : ℕ) : WellFounded (lexGtOn n) :=
  Finite.wellFounded_of_trans_of_irrefl _

instance instIsWellFoundedLexGtOn (n : ℕ) : IsWellFounded (PartOf n) (lexGtOn n) :=
  ⟨lexGtOn_wellFounded n⟩

/-- Recursion along the lex order, in the form an induction on shapes actually uses:
to prove `C μ` for every shape of size `n`, it suffices to prove it for `μ` given it for
every **lex-greater** shape of the same size. -/
theorem lexGtOn_induction {n : ℕ} {C : PartOf n → Prop}
    (ih : ∀ a : PartOf n, (∀ b : PartOf n, lexGtOn n b a → C b) → C a) (a : PartOf n) :
    C a := by
  refine (lexGtOn_wellFounded n).induction (C := fun x => C x) a ?_
  intro x hx
  exact ih x fun b hb => hx b hb

end QOU.BraidKnot.PartitionLexWellFounded
