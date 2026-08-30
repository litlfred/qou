---
# qou-ju3e
title: 'DEFECT: GBResidueSpectralSum is a second zero-Prop-field carrier, in mass-theory'
status: todo
type: task
priority: normal
created_at: 2026-08-30T03:27:51Z
updated_at: 2026-08-30T03:28:53Z
---

`content/quantum-observable-universe/mass-theory/gb-residue-spectral-sum.lean:87`

Found while fixing the same defect in `QOU/IwahoriHecke/MarkovTrace.lean`
(`GradedMarkovTraceExistence`, PR #6055). This is a **second instance of the same
class**, in a different chapter, and it was not swept into that PR because it is
mass-theory content rather than the Hecke cluster.

```lean
class GBResidueSpectralSum (R : Type*) [CommRing R] [LinearOrder R] where
  descended   : R
  levelBound  : ℕ
  q           : R
  roots       : Fin levelBound → RootOfUnity R
  gradedTrace : Fin levelBound → R
  ...
```

**Measured: zero `Prop` fields.** Every field is data — a ring element, a natural, a
function into `R`. So the class asserts nothing, and any tuple of the right shape
inhabits it. That is `proof-no-empty-prop-carrier` under AGENTS.md §3b-tax.

Its docstrings promise properties the fields do not encode — `gradedTrace` is
described as *"the value of `tr_M` descended to `J^ℓ / J^{ℓ+1}`"*, but nothing in the
class relates it to `tr_M`, to the filtration, or to `descended`. That is
`proof-claims-unencoded`.

**Not yet measured, and the first thing to do:** whether anything downstream takes
`[GBResidueSpectralSum]` as a hypothesis and concludes something. If so, those
conclusions are conditional on a class that constrains nothing, and the conditional
buys nothing — the shape of the `MarkovTrace` defect. The two greps run so far found
only docstring mentions in `QOU/BraidKnot/GBResidueSpectralSum.lean`; a real consumer
scan has **not** been run, so do not read that as "no consumers".

**The fix that worked on the sibling defect**, for reference: give the class `Prop`
fields carrying the properties its docstrings name (there: additivity, cyclicity, and
agreement with the trace at level 0); delete any instance that trivially inhabits it;
and prove one lemma showing the class now *buys* something, so the rebuild is not
itself decorative. Expect the honest outcome to be a content-bearing class with **no
instance** — which is what §3b-tax says an unproved primary should look like.

Do NOT fabricate content to make an instance exist.
