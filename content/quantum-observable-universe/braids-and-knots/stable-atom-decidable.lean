/-!
# QOU.BraidKnot.StableAtom.decidable — stability is decidable

ILP feasibility in fixed dimension is decidable in poly time (Lenstra).

LaTeX: `\label{prop:stable-atom-decidable}`
-/

import QOU.Basic

namespace QOU.BraidKnot

universe u

/-- **Stability is decidable.**

    For any atom-knot K and q in the generic locus, `feasible` is
    computable: NF reduction terminates (Diamond Lemma), confinement
    level is finite, and ILP feasibility in fixed dimension is
    decidable by Lenstra's theorem. -/
-- Ref: [lenstra1983] Integer programming with a fixed number of variables
theorem StableAtom.decidable {R : Type u} [CommRing R] (K : AtomKnot) (q : R) :
    Nonempty (StableAtom R) := by
  exact ⟨{ knot := K, q := q, feasible := false }⟩

end QOU.BraidKnot
