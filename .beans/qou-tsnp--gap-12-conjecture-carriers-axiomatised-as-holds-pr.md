---
# qou-tsnp
title: 'GAP: 12 conjecture carriers axiomatised as `holds : Prop` assert nothing'
status: todo
type: task
created_at: 2026-08-09T00:12:10Z
updated_at: 2026-08-09T00:12:10Z
---


## The defect

Twelve conjecture sibling carriers are axiomatised as

```lean
class C where
  holds : Prop
```

A field of type `Prop` names *some* proposition; it does not assert it.
`instance : C := ⟨True⟩` discharges the class, so the carrier asserts
nothing. This is the AGENTS.md §3b-tax failure ("the carrier must assert
something"), in a shape neither `proof-no-empty-prop-carrier` (fires on
*zero* fields) nor `proof-claims-unencoded`'s `true-class-field` pattern
(fires on a field typed literally `: True`) currently catches.

**Known, not new.** Named vacuous for one instance in
[`2026-06-07-klr-gs-order-formalization-plan.md` §Layer 1](../docs/audits/2026-06-07-klr-gs-order-formalization-plan.md)
("the current stub `class CrystalGraphRealization where holds : Prop` is
vacuous"), and as `reduction_holds : Prop` in
[`2026-06-24-devils-advocate-wave10.md`](../docs/audits/2026-06-24-devils-advocate-wave10.md).
This bean is the **corpus-wide census** and the drain queue.

## Scope — the 12 (verified: no library decl exists under the ref leaf)

| block | class |
|---|---|
| `mass-theory/borromean-bloch-group-element` | `BorromeanBlochGroupElement` |
| `mass-theory/dim-master-pentagon` | `DimMasterPentagon` |
| `mass-theory/isospin-from-canonical-bowtie` | `IsospinFromCanonicalBowtie` |
| `mass-theory/kashaev-density-equals-sdp-multiplicity` | `KashaevDensityEqualsSdpMultiplicity` |
| `mass-theory/p-from-braid-mirror` | `PFromBraidMirror` |
| `mass-theory/poincare-lefschetz-borromean` | `PoincareLefschetzBorromean` |
| `nuclear-interactions/spin-from-so3-fiber` | `SpinFromSo3Fiber` |
| `nuclear-interactions/t-from-trace-cyclicity` | `TFromTraceCyclicity` |
| `nuclear-interactions/type-b-folding-cpt` | `TypeBFoldingCpt` |
| `nuclear-interactions/wigner-su4-from-spin-isospin` | `WignerSu4FromSpinIsospin` |
| `q-geometric-langlands/mirror-3d-3d-correspondence` | `Mirror3d3dCorrespondence` |
| `stochastic-mechanics/lusztig-canonical-basis-q-eq-1` | `LusztigCanonicalBasisQEq1` |

**Count correction.** An earlier pass put this at 18, then 16. Both were
too high: 4 of the 16 (`brunnian-property-of-borromean`,
`gs-graded-markov-trace-existence`, `hyperbolic-volume-transcendence`,
`q-gl-conjecture`) do have substantive library formalisations, declared
under the **ref's leaf name in a differently-named file**, which a
class-name match misses. Those 4 were shadows and are now deleted. 12 is
the verified figure.

## Repair shape

Per §3b-tax and the klr plan: replace `holds : Prop` with fields that
encode the conjecture's **content** — parameter-quantified statements in
the shape of the claim, so that an instance is a real commitment and
downstream `[C]`-conditional theorems are conditional on something.

The exemplars now reachable after the shadow deletions show the target
shape, e.g. `QOU.Archimedean.HyperbolicVolumeIndependence.no_relation`
(a full algebraic-independence statement) and
`QOU.QGeometricLanglands.QGeometricLanglandsConjecture` (functor +
`hecke_compatible` + `recovers_eigenvalue`).

**Not mechanical.** Each requires reading the block's `.md` and stating
its actual claim in Lean. Do not batch-rewrite. Do not substitute a
`sorry`-carrying restatement for an honest one — a carrier with no
instance is the correct representation of an open conjecture.

## Guard

This is the *ideal* end state, not a licence to fabricate content. If a
conjecture's claim cannot yet be stated against existing types (the
`categorical-proton` failure mode — the type has no field for the
asserted property), the honest outcome is to say so and leave the
carrier, noting what type must grow first.
