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
