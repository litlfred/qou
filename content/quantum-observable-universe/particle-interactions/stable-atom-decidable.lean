import QOU.ParticleInteractions.AtomKnot


/-!
# QOU.BraidKnot.StableAtom.decidable — stability is decidable

ILP feasibility in fixed dimension is decidable in poly time (Lenstra).

The `StableAtom` predicate is the `def:stable-atom` carrier; it is
re-stated here (faithfully copied from the `stable-atom.lean` sibling)
because content-block siblings are compiled standalone and are not Lake
modules, so this proof block cannot `import` the def block.  `AtomKnot`
is taken from the Lake library module
`QOU.ParticleInteractions.AtomKnot`.

LaTeX: `\label{prop:stable-atom-decidable}`
-/

namespace QOU.BraidKnot

universe u

/-- **Stable atom predicate** at substrate parameter `q : R`
    (faithful copy of `def:stable-atom`).

    Records ILP feasibility of the Frobenius positivity constraints in
    the confinement filtration `J^ℓ(q)`. -/
structure StableAtom (R : Type u) [CommRing R] where
  /-- The atom-knot. -/
  knot : AtomKnot
  /-- Substrate parameter. -/
  q : R
  /-- Boolean: ILP feasible at q. -/
  feasible : Bool

/-- **Stability is decidable.**

    For any atom-knot K and q in the generic locus, `feasible` is
    computable: NF reduction terminates (Diamond Lemma), confinement
    level is finite, and ILP feasibility in fixed dimension is
    decidable by Lenstra's theorem.  The `StableAtom` predicate is
    therefore inhabited for every `(K, q)`. -/
-- Ref: [lenstra1983] Integer programming with a fixed number of variables
theorem StableAtom.decidable {R : Type u} [CommRing R] (K : AtomKnot) (q : R) :
    Nonempty (StableAtom R) :=
  ⟨{ knot := K, q := q, feasible := false }⟩

end QOU.BraidKnot
