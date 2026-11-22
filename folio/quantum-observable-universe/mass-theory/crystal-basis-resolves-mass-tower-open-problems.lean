/-!
# `prop:crystal-basis-resolves-mass-tower-open-problems` — three reductions, stated as reductions

The block claims that the Brundan–Kleshchev isomorphism and the Lecouvey
bijection **reduce** three of the four open mass-tower problems to finite
crystal-graph combinatorics.  Per the context remark, the three are:

* **chirality factor** ⟸ an integer multiplicity sum on a Type-B folded
  crystal (the folded Demazure components);
* **Term 7 shell correction** ⟸ enumerating crystal vertices at depth 6;
* **Habiro convergence divergence** ⟸ the Kazhdan–Lusztig classical-limit
  functor, mapping the divergent Hecke trace to a finite integer sum over the
  symmetric group.

The fourth — the Bloch-group decomposition of the EM coupling — is stated in
the same remark to be **transverse** to this machinery.

## 2026-08-31 — the whole file was one `Prop` field and its own proof

This file read, in its entirety:

```lean
class CrystalBasisCorrespondence where
  reduction_holds : Prop
  reduction_holds_proof : reduction_holds

theorem crystal_basis_reduction [ctx : CrystalBasisCorrespondence] :
    ctx.reduction_holds := by exact ctx.reduction_holds_proof
```

`reduction_holds := True`, `reduction_holds_proof := trivial` inhabits the
class, so the binder assumed nothing and the theorem asserted nothing — the
purest form of the self-assuming projection (AGENTS.md §3b-cond item 5; bean
`qou-z9ws`).  It also stated **nothing** about crystals, chirality, Term 7,
the `z`-Habiro divergence, or the fourth problem: no part of the block's
content appeared in the Lean at all.

The re-encoding takes the block at its word.  A *reduction* is an
implication, `ReducesTo problem computation := computation → problem`, and
the proposition is three such implications over caller-supplied problems and
computations.  Those three are the conjecture and are carried by
`CrystalBasisCorrespondence` as fields — but over **parameters**, so a
`[CrystalBasisCorrespondence …]` binder is a hypothesis about the caller's
propositions rather than about ones the instance chose.
`crystal_basis_reduction` then **derives** what a reduction is for: carrying
out the three finite computations settles the three problems.

## What is NOT claimed here, stated rather than implied

- **The three reductions are not proved.**  They are conditional on the
  upstream Brundan–Kleshchev and Lecouvey results, exactly as the block's
  author note says (*"Each reduction is sorry-free conditional on the
  upstream Brundan-Kleshchev / Lecouvey conjectures"*).  No instance of the
  class is supplied.
- **The three computations are not carried out.**  They are the residual
  open content the author note names, and they enter below as hypotheses.
- **The fourth problem is untouched.**  Nothing here reduces the Bloch-group
  decomposition, and nothing here proves that it *cannot* be reduced — the
  remark's "transverse" is a scope-limited statement, not an exclusion.
- **The crystal combinatorics themselves are absent.**  Type-B folding,
  Demazure sub-crystals and depth-6 vertex enumeration appear in this file
  only as the *names* of the computations, carried as opaque propositions.

## References
- [leitner2026] prop:crystal-basis-resolves-mass-tower-open-problems
- [brundankleshchev2009], [lecouvey2007], [kashiwara1991], [khovanovlauda2009]
-/

namespace QOU.Archimedean

/-- **`problem` reduces to `computation`**: carrying out the computation
settles the problem.

A reduction is an implication in this direction and not the other; stating it
the other way round would say that the problem being open bounds the
computation, which is not what a reduction claims. -/
-- Ref: [leitner2026] prop:crystal-basis-resolves-mass-tower-open-problems
def ReducesTo (problem computation : Prop) : Prop := computation → problem

/-- The crystal-basis correspondence, as a class over the four problems and
the three finite computations it concerns.

`chirality`, `term7`, `zHabiro` and `blochGroup` are the four open mass-tower
problems; `chiralityCount`, `term7DepthSix` and `zHabiroKLLimit` are the
three finite crystal-graph computations the block names.  All seven are
**parameters**, so the class is a hypothesis about the caller's propositions.

The three fields are the conjecture, conditional on Brundan–Kleshchev and
Lecouvey.  No instance is supplied.  `blochGroup` is carried so the fourth
problem is visible in the type and its absence from the fields is legible:
the class makes no claim about it. -/
-- Ref: [brundankleshchev2009] Brundan–Kleshchev, graded decomposition numbers
-- Ref: [lecouvey2007] Lecouvey, crystal bases and combinatorics
-- Ref: [leitner2026] prop:crystal-basis-resolves-mass-tower-open-problems
class CrystalBasisCorrespondence
    (chirality term7 zHabiro blochGroup : Prop)
    (chiralityCount term7DepthSix zHabiroKLLimit : Prop) : Prop where
  /-- The chirality factor average reduces to an integer multiplicity sum on
      a Type-B folded crystal. -/
  chirality_reduces : ReducesTo chirality chiralityCount
  /-- The Term 7 shell correction reduces to enumerating crystal vertices at
      depth 6. -/
  term7_reduces : ReducesTo term7 term7DepthSix
  /-- The Habiro convergence divergence reduces to the Kazhdan–Lusztig
      classical-limit functor. -/
  zHabiro_reduces : ReducesTo zHabiro zHabiroKLLimit

/-- **Crystal-basis correspondence**
([`prop:crystal-basis-resolves-mass-tower-open-problems`]).

Given the three reductions, discharging the three finite crystal-graph
computations settles three of the four open mass-tower problems.

Derived: the conclusion is none of the class's fields, and the proof is the
three implications applied to the three computations.  This is what a
reduction claim is *for*, and it is the part the previous encoding — a bare
`Prop` field handed back — did not state.

The fourth problem does not appear in the conclusion, because nothing here
reduces it. -/
-- Ref: [leitner2026] prop:crystal-basis-resolves-mass-tower-open-problems
theorem crystal_basis_reduction
    {chirality term7 zHabiro blochGroup : Prop}
    {chiralityCount term7DepthSix zHabiroKLLimit : Prop}
    [inst : CrystalBasisCorrespondence chirality term7 zHabiro blochGroup
      chiralityCount term7DepthSix zHabiroKLLimit]
    (hCount : chiralityCount) (hDepth : term7DepthSix)
    (hLimit : zHabiroKLLimit) :
    chirality ∧ term7 ∧ zHabiro :=
  ⟨inst.chirality_reduces hCount, inst.term7_reduces hDepth,
    inst.zHabiro_reduces hLimit⟩

end QOU.Archimedean
