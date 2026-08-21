---
# qou-2u26
title: 'Formalisation backlog: 57 blocks whose lean.ref names a declaration that exists nowhere'
status: todo
type: task
priority: normal
created_at: 2026-08-15T23:25:59Z
updated_at: 2026-08-15T23:26:33Z
---

Owner directive 2026-08-15: **keep these refs, bean them** — do not delete.

These 57 content blocks carry a `lean.ref` naming a declaration that exists **nowhere** in the Lean tree, verified by normalised (case/underscore-insensitive) matching against a decl index built from the whole tree, plus the canonical resolver. They are genuinely **unformalised**, not mis-referenced — distinct from the 6 in `qou-cu0a` that were casing mismatches and have been repointed.

## Why the refs stay

- After the upstream resolver fix (folio-assistant `#121`) these report an honest `n/a` instead of the false `pass` they used to get from the root import aggregator. The misleading part is already fixed.
- The ref still records the **intended formalisation target**, which is the useful half — it tells whoever writes the Lean what the block expects to be called.
- Omitting `lean:` is well-precedented (2345 of 3567 blocks have none), so deletion remains available later; it just throws the intent away.

## Definition of done

Per block: either a real Lean declaration at the named path, or an author decision to drop the ref. **Not** a mass edit — each is a separate formalisation.

## The 57

- `braids-and-knots/q-casimir-classical-limit.ts` → `qou:QOU.QCasimirEigenvalue_classical_limit`
- `brings-surface/color-sector-coords.ts` → `qou:QOU.ColorSectorCoords`
- `brings-surface/orbital-space-normal-bundle.ts` → `qou:QOU.orbital_space_normal_bundle`
- `knots-particles-confinement/localized-hadron.ts` → `qou:QOU.LocalizedHadron`
- `knots-particles-confinement/hadron-fibre-embedding.ts` → `qou:QOU.HadronFibreEmbedding`
- `fluid-dynamics/observable-mtc.ts` → `qou:QOU.ObservableMTC`
- `information-theory/computational-spacetime-observer.ts` → `qou:QOU.computationalDistance`
- `information-theory/q-heat-kernel-peter-weyl.ts` → `qou:QOU.qHeatKernelPeterWeyl`
- `information-theory/q-gaussian-solves-q-heat.ts` → `qou:QOU.qGaussianSolvesQHeat`
- `information-theory/q-exponential-taylor.ts` → `qou:QOU.qExponentialTaylor`
- `information-theory/aeon-boundary.ts` → `qou:QOU.aeonBoundary`
- `information-theory/aeon-adjacency.ts` → `qou:QOU.aeonAdjacent`
- `information-theory/information-theoretic-time.ts` → `qou:QOU.informationTheoreticTime`
- `information-theory/planck-time.ts` → `qou:QOU.planckTime`
- `quantum-observable-universes/q-exponential.ts` → `qou:QOU.QExponential`
- `quantum-observable-universes/q-logarithm.ts` → `qou:QOU.QLogarithm`
- `quantum-observable-universes/categorical-reeb-exists.ts` → `qou:QOU.categorical_reeb_exists`
- `quantum-observable-universes/categorical-point.ts` → `qou:QOU.CategoricalPoint`
- `quantum-observable-universes/spin-labels.ts` → `qou:QOU.SpinDecomposition`
- `quantum-observable-universes/spectral-chart-correspondence.ts` → `qou:QOU.spectral_chart_correspondence`
- `quantum-observable-universes/braiding-eigenvalue-extraction.ts` → `qou:QOU.braiding_eigenvalue_extraction`
- `quantum-observable-universes/braiding-induced-ordering.ts` → `qou:QOU.braiding_induced_ordering`
- `quantum-observable-universes/categorical-q-lie-bracket.ts` → `qou:QOU.CategoricalQLieBracket`
- `quantum-observable-universes/contact-affine-chart.ts` → `qou:QOU.ContactAffineChart`
- `quantum-observable-universes/su2-emergence.ts` → `qou:QOU.RankOneGaugeData`
- `quantum-observable-universes/categorical-reeb.ts` → `qou:QOU.CategoricalReeb`
- `quantum-observable-universes/commutative-qou.ts` → `qou:QOU.CommutativeQOU`
- `quantum-observable-universes/weight-decomposition.ts` → `qou:QOU.WeightDecomposition`
- `quantum-observable-universes/tannaka-krein-reconstruction.ts` → `qou:QOU.tannaka_krein_reconstruction`
- `quantum-observable-universes/maximal-torus.ts` → `qou:QOU.MaximalTorus`
- `glossary/glossary-quantum-flatness.ts` → `qou:QOU.QuantumFlatness`
- `glossary/glossary-categorical-q-torsion-leaf.ts` → `qou:QOU.CategoricalQTorsionLeaf`
- `glossary/glossary-reeb-gauge-group.ts` → `qou:QOU.ReebGaugeGroup`
- `glossary/glossary-descent.ts` → `qou:QOU.DescentData`
- `glossary/glossary-s3-group.ts` → `qou:QOU.S3Group`
- `measurement-observation/bundle-initial-conditions.ts` → `qou:QOU.BundleInitialConditions`
- `measurement-observation/torsion-knot-flow.ts` → `qou:QOU.ParticleState`
- `measurement-observation/bundle-isotopy-equivalence.ts` → `qou:QOU.BundleIsotopyEquiv`
- `quantum-universes/frobenius-pairing.ts` → `qou:QOU.FrobeniusPairing`
- `quantum-universes/poisson-object.ts` → `qou:QOU.PoissonObject`
- `quantum-universes/snake-identity.ts` → `qou:QOU.snake_identity_left`
- `quantum-universes/rigid-monoidal-category.ts` → `qou:QOU.RigidMonoidalCategory`
- `quantum-universes/fundamental-object.ts` → `qou:QOU.FundamentalObject`
- `quantum-universes/tannaka-dual.ts` → `qou:QOU.TannakaDual`
- `lifting-and-descent/descent-lemma.ts` → `qou:QOU.DescentLemma`
- `lifting-and-descent/localized-knot.ts` → `qou:QOU.LocalizedKnot`
- `lifting-and-descent/categorical-q-reeb-flow.ts` → `qou:QOU.CategoricalQReebFlow`
- `mass-theory/vertex-operator.ts` → `qou:QOU.VertexOperator`
- `mass-theory/reeb-bundle.ts` → `qou:QOU.ReebBundle`
- `mass-theory/quantum-bloch-group.ts` → `qou:QOU.QuantumBlochGroup`
- `mass-theory/vertex-is-exceptional-divisor.ts` → `qou:QOU.vertex_is_exceptional_divisor`
- `mass-theory/transfer-matrix-level-independence.ts` → `qou:QOU.transfer_matrix_level_independence`
- `models-of-qous/categorical-archimedean-bridge.ts` → `qou:QOU.categorical_archimedean_bridge`
- `models-of-qous/spatial-realization-functor.ts` → `qou:QOU.SpatialRealizationFunctor`
- `models-of-qous/symmetric-point-channel-collapse.ts` → `qou:QOU.symmetric_point_channel_collapse`
- `models-of-qous/physical-units-gap-linear.ts` → `qou:QOU.physical_units_gap_linear`
- `models-of-qous/witt-vector-lift.ts` → `qou:QOU.WittVectorLift`

## 2026-08-21 — the "not mis-referenced" claim is not established, and one is now fixed

This bean states the 57 are *"genuinely **unformalised**, not mis-referenced —
verified by normalised (case/underscore-insensitive) matching against a decl
index built from the whole tree, plus the canonical resolver."*

**That verification cannot detect the mis-reference mode that has already
produced two confirmed hits.** Both `thm:su2-emergence` (→ `QOU.RankOneGaugeData`,
repointed in PR #5222) and `def:mass-identity` (→ `QOU.categoricalMass`,
repointed under `qou-qc6s`) named declarations that exist nowhere — so they pass
this bean's name test as "unformalised" — while the correct declaration existed
all along, identified by the block's **`\label`**. A name-based index cannot see
a label match. The test has to be run on the label, not the name.

### Ran the label test

| measure | count |
|---|---:|
| blocks carrying a `qou:` ref | 1238 |
| refs the **canonical resolver** cannot resolve at all | **4** |
| refs naming no declaration by normalised fully-qualified match | **49** |
| of those 49, a Lean decl carries the block's **own label** | **16** |

The 4 fully-unresolvable ones are exactly the set folio-assistant PR #121
predicted — `figure-eight-reeb-theta-value`, `crossing-energy-pair-cancellation`,
`channel-rotation-askey-lit`, `complex-volume-character-variety-path`.
Independent confirmation of that number by a different route.

**Do not read the 16 as 16 defects.** Resolving them individually, **10 of 12
checked resolve correctly** — my fully-qualified matcher over-flags
module-path-style refs (e.g. `def:yekutieli-triple`, `thm:qu-to-qou`, both of
which I repaired myself in #5113 and which are fine). Recorded because the
over-flagging is the same class of error this entry is about, and it caught me
too.

### One confirmed mis-reference, fixed

`def:ns-regular-qou` (`fluid-dynamics/ns-regular-qou.ts`):

- ref was `qou:QOU.FluidDynamics.NSRegularQOU` → **UNRESOLVED**; that namespace
  and that declaration exist nowhere.
- `QOU.GaugeFieldFluidDynamics.BoundaryObservability`
  (`lean/QOU/GaugeFieldFluidDynamics.lean:477`) carries
  `\label{def:ns-regular-qou}` — the block's own label.
- Repointed; verified through the canonical resolver.

**Why nothing caught it, and this is the reusable lesson.** The block has a
co-located sibling `ns-regular-qou.lean`, and `walkBlocks` resolves the
**sibling first**. So every checker audited the stub and passed, while the
library ref sat dead and the real declaration went unchecked. **A sibling stub
masks a broken library ref**, and it masks it from the diff-scoped gates too.
Neither this bean's method nor #121's fix surfaces that combination — #121 made
*aggregator* fallbacks honest, not sibling-shadowed ones.

### What the remaining work actually is

Not "57 separate formalisations". It is:

1. **Run the label test per block on the ~49**, which is cheap and mechanical:
   does any Lean declaration carry this block's `\label`? If yes → repoint (a
   ref edit). If no → genuinely unformalised (a formalisation).
2. **Audit the sibling-masking population separately.** Any block with both a
   co-located `.lean` and a library `lean.ref` can have a dead ref that no gate
   reports. That set is not enumerated anywhere yet and is the more dangerous
   half, because it is invisible rather than merely unresolved.

The owner directive to **keep the refs and bean them** is unaffected — repointing
preserves intent, and nothing here deletes a ref.
