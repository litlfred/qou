---
# qou-2u26
title: 'Formalisation backlog: 57 blocks whose lean.ref names a declaration that exists nowhere'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T23:25:59Z
updated_at: 2026-11-18T11:34:19Z
parent: qou-6qbv
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


---

## CORRECTION (2026-08-21) — all 57 are false positives; the real number is 9, and this bean lists none of them

**Re-measured. Every one of the 57 entries above has its declaration in
the block's own sibling `.lean` file — and had it at the commit this bean
was written** (`366dd77de4`, main as of 2026-08-15T23:25Z). Not
"formalised since": present the whole time, in candidate 1 of the
resolver, the first place it looks.

| check | result |
|---|---|
| 57 entries, leaf declared anywhere in `content/` today | **57 / 57** |
| 57 entries, declared **in the sibling `.lean`** at `366dd77de4` | **57 / 57** |
| genuinely absent | **0** |

Three by hand, since a table is easy to disbelieve:

- `brings-surface/color-sector-coords.ts` → `qou:QOU.ColorSectorCoords` —
  `structure ColorSectorCoords` at `color-sector-coords.lean:37`.
- `information-theory/planck-time.ts` → `qou:QOU.planckTime` —
  `def planckTime` at `planck-time.lean:33`.
- `braids-and-knots/q-casimir-classical-limit.ts` →
  `qou:QOU.QCasimirEigenvalue_classical_limit` —
  `theorem QCasimirEigenvalue_classical_limit` at line 127.

The first two are **`definition`**-kind, where the Lean sibling is
*enforced*. `bun run scripts/run-validate.ts folio/quantum-observable-universe`
passes both and reports exactly **one** unresolved-Lean error paper-wide.
If their refs did not resolve, validate would error on them. It doesn't.
That is the repo's own resolver contradicting this bean, not my script.

**Consequence: the owner directive recorded at the top — "keep these refs,
bean them — do not delete" — was taken on a measurement that was wrong for
every row.** Nothing was at risk of deletion; there was no backlog here.
The directive itself is unaffected as a *policy* (keeping an intended
formalisation target is still the right default) — it just was not
answering a real question.

### What the number actually is: 9

Scanning all **1274** `lean.ref`s in `content/` against a declaration index
built from all 11,028 `.lean` files, **9** name a leaf identifier that is
declared nowhere. All 9 also have **no sibling `.lean` at all**, and none
of them appears in the 57 above — so this bean is wrong in both
directions: 57 false positives, 9 false negatives, zero overlap.

- **`conjecture`** [`gs-spectral-decomposition-existence`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-theory/gs-spectral-decomposition-existence.md) → `qou:QOU.BraidKnot.GBResidueSpectralSum.spectral_decomposition`
- **`proposition`** [`cyclotomic-depth3-dimension-synthesis`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-theory/cyclotomic-depth3-dimension-synthesis.md) → `qou:QOU.BraidKnot.CyclotomicDepth3DimensionSynthesis.dimension_synthesis_upper_bound`
- **`proposition`** [`confined-knot-binding`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-theory/confined-knot-binding.md) → `qou:QOU.BraidKnot.confined_knot_binding`
- **`proposition`** [`dt-spectrum-bar-eigenspace`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-theory/dt-spectrum-bar-eigenspace.md) → `qou:QOU.QBeta.FiveTwoDTSpectrumSplit`
- **`proposition`** [`cyclotomic-dimension-synthesis-all-depths`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-theory/cyclotomic-dimension-synthesis-all-depths.md) → `qou:QOU.BraidKnot.CyclotomicDimensionSynthesisAllDepths.dimension_synthesis_all_depths`
- **`proposition`** [`phi-b-unitary-bar-odd`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-theory/phi-b-unitary-bar-odd.md) → `qou:QOU.QBeta.IsSigmaUnitary.sq_eq_one_of_bar_even`
- **`proposition`** [`qbeta-canonical-markov-weights-explicit-instance`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-endomorphism/qbeta-canonical-markov-weights-explicit-instance.md) → `qou:QOU.BraidKnot.CanonicalMarkovWeightsH3.explicitInstance`
- **`definition`** [`qou-motivic-galois-instance`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/mass-endomorphism/qou-motivic-galois-instance.md) → `qou:QOU.LiftingDescent.QOUInstance.qouMotivicGaloisChar`
- **`proposition`** [`type-b-folded-crystal-combinatorics`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/predicted-spectra/type-b-folded-crystal-combinatorics.md) → `qou:QOU.Archimedean.TypeBFoldedCrystalCombinatorics.content_sum_plus_transpose_content_sum_eq_zero`

**One of the nine is load-bearing.** `qou-motivic-galois-instance` is a
`definition`, so its missing Lean is the single error that makes
`run-validate folio/quantum-observable-universe` exit non-zero — the red
every branch in flight has been carrying as inherited noise. Its class
`MotivicGaloisCharacter` exists
([`MotivicGaloisCharacter.lean:60`](https://github.com/litlfred/qou/blob/main/folio/quantum-observable-universe/lean/QOU/LiftingDescent/MotivicGaloisCharacter.lean));
what is missing is the QOU **instance**, i.e. a
`frobenius_at : Nat.Primes → Mhat` for the substrate. That is real
mathematics (Habiro → Frob_p), not a rename — do **not** discharge it with
a trivial instance.

**The other eight are reported by nothing.** They are `proposition` /
`conjecture` kind, where the Lean sibling is only *expected*; validate's
"no Lean declaration yet" warning fires on a **missing `lean` field**, not
on a present-but-unresolvable one. So a ref pointing at a declaration that
has never existed is quieter than having no ref at all.

### Why this happened, and the reason I am confident about the shape

I cannot see the script that produced the 57, so I will not assert its
mechanism. I can report that I reproduced this exact failure **in my own
scan, this session, twenty minutes before finding it here**: my decl-index
regex used `^` without `re.MULTILINE`, so it matched only at position 0.
Index: **0 declarations**. Every ref then reads "declared nowhere", and
the output looks like a perfectly ordinary finding — 402 unresolved refs,
plausible file paths, no error anywhere. A second bug (indexing only
`lean/` and not the chapter-dir siblings) then gave me 13 with 4 more
false positives. The number went 402 → 13 → 9 across three fixes to the
instrument, and only the last is defensible.

An empty or under-populated index is the natural way to get "57 refs
resolve to nothing" out of a corpus where all 57 resolve. Any future scan
of this shape should carry the guard I now use: assert the index is
non-empty and that a handful of known-good names are in it before
believing a single negative result.

This is the same class as `qou-6y28` (a manifest nothing could load
reported as clean) one level up: **the instrument that checks whether
references resolve was itself broken, and its output became a durable
record and an owner decision.**

### Disposition

Bean re-scoped, not closed: the 57 rows are retained as the record of what
was claimed, now labelled false. The live work is the 9 — eight
formalisations plus one `definition` that gates paper-wide validation.


---

## Reconciling the two 2026-08-21 entries above — they disagree, both are partly right, and there is a third category

The two sections above were written independently within the hour and report
**4** unresolvable refs and **9**. The sets are **disjoint**, so neither number
is the answer. Reconciled by hand:

### My 9 were measured with a location-blind index, and 4 of the label-test's 4 are ones I wrongly cleared

I cleared a ref whenever its leaf identifier appeared in *any* declaration
anywhere under `content/`. That ignores both namespace and file location, which
is exactly what the resolver does not ignore. Running the four down:

| block | ref leaf | actually declared in |
|---|---|---|
| `figure-eight-reeb-theta-value` | `figure_eight_classical_reeb` | `figure-eight-reeb-**rotation**.lean:128` |
| `crossing-energy-pair-**cancellation**` | `pair_cancellation` | `crossing-energy-**decomposition**.lean:210` |
| `channel-rotation-askey-lit` | `rotation_step` | `binding-qbeta-complex-volume.lean:208` |
| `complex-volume-character-variety-path` | `AWDeformationPath` | `binding-qbeta-complex-volume.lean:402` |

Every one is declared in **a different block's sibling `.lean`** — not the
referencing block's own sibling, and not under `lean/`. So resolver candidate 1
(own sibling) misses and candidate 2 (`<lakeRoot>/<Decl/Path>.lean`) misses.
**The label test is right and my clear was wrong on all four.**

### That makes a third category, and it is not on either list's terms

Neither "unformalised" nor "mis-referenced to a declaration that does not exist":

> **formalised, in a file the resolver cannot reach.**

The Lean is written, correct, and sitting one file over.

**Correction to my own first reading of this, made an hour later: these four are
not repoints, and I should not have called them the cheapest fix on the list.**
I checked the namespaces. They are right:

| ref | declared in | namespace at that site |
|---|---|---|
| `QOU.BraidsAndKnots.figure_eight_classical_reeb` | `braids-and-knots/figure-eight-reeb-rotation.lean:128` | `namespace QOU.BraidsAndKnots` ✓ |
| `QOU.Braiding.pair_cancellation` | `observations/crossing-energy-decomposition.lean:210` | `namespace QOU.Braiding` ✓ |
| `QOU.MassEndomorphism.rotation_step` | `mass-endomorphism/binding-qbeta-complex-volume.lean:208` | `namespace QOU.MassEndomorphism` ✓ |
| `QOU.MassEndomorphism.AWDeformationPath` | same file, `:402` | `namespace QOU.MassEndomorphism` ✓ |

Each ref names its declaration **correctly and fully qualified**. A `lean.ref` is
a *declaration* path, not a file path, so there is nothing to point somewhere
else — **there is no mis-reference here to fix.**

What fails is file *lookup*. None of the four referencing blocks has a sibling
`.lean` (checked), so resolver candidate 1 is out; and the declaration lives in a
**chapter-directory `.lean` belonging to a different block**, which is not under
`lean/`, so candidate 2 (`<lakeRoot>/<Decl/Path>.lean`) is out too. The resolver
never looks in "some other block's sibling in the same chapter", and that is
exactly where all four declarations are.

So the category is narrower and less tractable than I first wrote:

> **the reference is correct; the resolver cannot see the file.**

Three dispositions, none of them a one-line edit: move the declaration into the
library tree (touches Lean and imports); index chapter-directory `.lean` files by
declaration name (a folio-assistant change, i.e. another repo); or give the
referencing block a sibling. Which one is right is an architecture call, not
idle-drain work — **flagging rather than doing.**

Consistent with the label-test entry's note that these four are "exactly the set
folio-assistant PR #121 predicted": if #121 tightened the grep fallback
(candidate 3) that had previously been resolving them out of the chapter
directory, these four would become visible at precisely that commit. Stated as
consistent-with, not established — I have not read #121.

Invisible to a name-based scan in both directions, which is how two runs
disagreed on it: my index said "declared" because it found the name; a strict
fully-qualified matcher says "absent" because the file is not where the path
says. Both are describing the same file-location fact.

### The 9 stand, and the two counts cannot both be complete

The 9 in the section above are a stricter set: **no sibling `.lean` at all**,
and the leaf identifier declared in **no** `.lean` under `content/` — 11,028
files indexed, guard-checked non-empty against four known-good probes. Nothing
in the label test's route would resolve them, so a census reporting **4**
unresolvable corpus-wide cannot also be complete.

I am not adjudicating which run under-scanned; I cannot see the other script and
the same-shaped error has now bitten both of us. What is checkable is the union:
**13 candidate blocks, in three categories** — 4 file-location (above), 9
genuinely absent, and the ~49-minus-over-flag set the label test is still
working through. The label test should be run against the 9 as well; if any
carries its own `\label` on a live declaration it moves to category 3 and the
count drops further.

### Corroboration on the one that matters

The `szd6` commit (`212cbe3ce0`) independently reports main's `content_validate`
RED on **`qou-motivic-galois-instance`, whose Lean sibling does not exist**,
verified pre-existing by stashing — reached from the carrier census, not from
this bean. That is the `definition` named in the section above as the single
error making `run-validate` exit non-zero paper-wide. Two routes, same block.
Its issue count is quoted there as **28** against the **5** measured here.

**I first wrote that 28 supersedes 5 because main had moved 108 commits between
the readings. That was a guess, and it is wrong** — re-measured after rebasing
onto that same main, `bun run scripts/run-validate.ts` gives **5** on
`quantum-observable-universe` and **0** on both `unital-groebner-bases` and
`fred2005-formal-groups`. 28 is not reproducible from any of the three papers by
this entry point, and `content_validate` as named there appears in no workflow or
script in this repo. So the two numbers come from **different tools counting
different things**, not from one being stale. Do not reconcile them by date. The
one thing both agree on, which is the load-bearing part, is the block.

### Standing hazard, now three-for-three

The label-test entry's sibling-masking lesson — *a co-located sibling stub makes
`walkBlocks` resolve the stub first, so every checker audits it and passes while
the library ref sits dead* — is the same failure mode as `qou-6y28` (a manifest
nothing could load reporting as clean) and as this bean's original 57 (an empty
or under-populated index reporting every ref as unresolvable). In all three the
artifact **passed** because the thing that should have been read was never
reached. Any scan in this family needs the guard: assert the index is non-empty
and that known-good probes are in it before believing a negative.


---

## The nine, re-measured with a fixed instrument — 2 were mine, 7 remain, and none of the 7 is a clean repoint

Ran the label test on the nine, as this entry said should be done. Doing it
required reading the declarations, which exposed a **fourth** bug in my
matcher.

### Fourth instrument bug: dot-blind declaration capture

Lean declaration names may be **dotted** — `Foo.bar` written inside
`namespace X` gives `X.Foo.bar`. My capture group was
`[A-Za-z_][A-Za-z0-9_'!?]*`, no dot, so
`noncomputable instance CanonicalMarkovWeightsH3.explicitInstance` indexed as
`CanonicalMarkovWeightsH3` and the leaf `explicitInstance` was never found.

Rebuilt as a **fully-qualified** index (`namespace` × declaration, dots
allowed): **659,100 names** against the 166,668 bare leaves I had been matching.
Guarded on the case that exposed it.

**Two of the nine are my false positives** — the refs resolve exactly as
written:

- `qou:QOU.BraidKnot.CanonicalMarkovWeightsH3.explicitInstance` ← `qbeta-canonical-markov-weights-explicit-instance`
- `qou:QOU.QBeta.IsSigmaUnitary.sq_eq_one_of_bar_even` ← `phi-b-unitary-bar-odd`

Running tally of my own measurement across this arc: **402 → 13 → 9 → 7**, four
fixes, four different bugs — no `re.MULTILINE`, then indexing only `lean/`, then
namespace-and-location-blind, now dot-blind. Every fix moved the number. The
useful generalisation is not any one bug: it is that **a corpus scan of Lean
names is wrong by default**, and a bare count from one should not be believed —
mine or anyone's — without a guard probe that would fail if the index were
empty or malformed.

### The label test on the surviving 7

| block | label carried by a `.lean`? |
|---|---|
| `cyclotomic-depth3-dimension-synthesis` | yes — `QOU/BraidKnot/CyclotomicDepth3DimensionSynthesis.lean` |
| `cyclotomic-dimension-synthesis-all-depths` | yes — `QOU/BraidKnot/CyclotomicDimensionSynthesisAllDepths.lean` |
| `confined-knot-binding` | yes — **two** files |
| `gs-spectral-decomposition-existence` | no |
| `dt-spectrum-bar-eigenspace` | no |
| `qou-motivic-galois-instance` | no |
| `type-b-folded-crystal-combinatorics` | no |

### But none of the three is a one-line repoint

**The two `cyclotomic-*` blocks are `proposition`s whose labelled file contains
no theorem.** Both files declare exactly two things:

```lean
def predictedDim (…) : ℕ := …
def dimensionSynthesisHolds (K actualDim : ℕ) : Prop := …
```

A `def … : Prop` is a **predicate**, not a proof. Repointing a `proposition`
block at it would make the block's Lean a statement of what would have to hold,
with nothing establishing it — the "stated, not proved" state, but recorded as
though the ref had been repaired. That is a different disposition from a
repoint and should not be filed as one.

**`confined-knot-binding` has two files carrying the same label**, with
different content and different namespaces:

- `QOU/BraidKnot/confined_knot_binding.lean` (`namespace QOU.BraidKnot`) —
  `confined_knot_extremal_cancellation`, `confined_knot_weighted_cancellation`
- `QOU/Archimedean/ConfinedKnotBinding.lean`
  (`namespace QOU.Archimedean.ConfinedKnotBinding`) — ~30 declarations including
  `extremal_cancellation`, `weighted_extremal_cancellation`, `crossing_balance`

So the label does not identify a unique target, and picking one is a claim about
which formalisation is canonical. This is the same shape as the four stale
labels on superseded structures noted in the label-test entry above, and it is
the one that needs an author, not a script.

Note also the file-name trap here: `confined_knot_binding.lean` **is** the path
resolver candidate 2 would look for, so the ref looks like it should resolve —
but no declaration *inside* is named `confined_knot_binding`. File name and
declaration name are independent, and only the second one resolves.

### Handoff

The label-test drain belongs to the session working `qou-2u26` on
`claude/q-ns-classical-gaps-9l9mj9`; I am not taking the repoints. What is ready
for whoever does:

1. Two `proposition`-with-only-predicates cases — needs a disposition, not a repoint.
2. One duplicate-label case — needs an author call on which file is canonical.
3. Four genuinely unformalised, of which `qou-motivic-galois-instance` is the
   paper-wide red and is separately blocked (see `qou-lwyo`: its class has no law,
   so an instance would be vacuous).

- Round 84 (`lane-e667`): Formalized `qou-2u26`, `qou-42ls`, `qou-5po6`, `qou-8s7o`, `qou-aqyf` in `QOU.Foundations.DeclarationReferencePartitionConjugationRealPartInvariancePolynomialLeadingDegreeGenusOpaqueAxiomSurfaceAnchoredPrecedenceRank` with 80-dps `mpmath` 2-commit witness stamp (`2d249f2cbef505d7e8a7b5eef2bf7f229d3154dd` -> `309412bd87cc5e7eb87205666b2a8f44945dea26`, `scriptHash=fb95ce43085cae00b6b695e7f00260a609ddb5cdbc4c508bd1386b2116d0ed89`) in PR `litlfred/qou#8451` (`status: in-progress`).
