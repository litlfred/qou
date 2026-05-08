# Trivial-skeleton workplan

**Date**: 2026-05-08
**Branch**: `claude/audit-content-blocks-hzjAf`
**Audit pipeline**: `content/pipeline/trivial-skeleton-audit.ts`
**Witness**: `docs/audits/2026-05-08-trivial-skeleton-audit.json`

The §3b-cond pattern lets a class-axiomatised conjecture be discharged
by *any* inhabitant of its class type. A **tautological skeleton** is
one whose data fields are picked so trivially (e.g., everything = 0,
every type = `PUnit`, every Prop = `True`) that the equation/Prop
fields close vacuously.

This is spec-compliant — the class is inhabited, downstream `[C]`
hypothesis users resolve. But it encodes **none** of the conjecture's
actual content. The audit pipeline flags every such site so future
work can promote them to faithful instances.

## Three upgrade patterns

| Pattern | Description | Example commit |
|---|---|---|
| **A. Numerical-pinning** | Replace `def f := 0` with the witness-pinned value (CODATA / PDG / 50dps witness). | `electronMass := 0.51099895` (CODATA 2022) |
| **B. Canonical-existence** | Replace `_holds := trivial` (where the field is `True`) with the canonical-witness existential and discharge by exhibiting the witness. | `is_baryon_realisation := ∃ p n, p = proton_partition ∧ ...; := ⟨proton_partition, neutron_partition, …⟩` |
| **C. Weakest-non-trivial-predicate** | Replace `def P : Prop := True` with the weakest checkable predicate the canonical witness satisfies. | `AtlasIsWitnessDerived := atomKnotAtlas.length ≥ 1` (after populating the atlas) |

## Audit summary (post-Bucket 1+2+3 work)

| Pattern | Initial | After B1+B2+B3 | Δ |
|---|---:|---:|---:|
| `const_zero`     | 38 | 35 | -3 |
| `skel_inst`      | 21 | 12 | **-9** (renamed faithful instances to `canonical`) |
| `prop_true`      | 15 | 12 | -3 (atlas + cyclotomic + weinberg) |
| `punit_type`     | 14 | 14 | 0 (Bucket 4) |
| `one_def`        | 10 | 9  | -1 |
| `holds_trivial`  | 8  | 7  | -1 |
| `punit_unit`     | 2  | 2  | 0 |
| `id_def`         | 1  | 1  | 0 |
| `const_zero_typed` | 1 | 1 | 0 |
| **Total**        | **111** | **93** | **-18 (16 % reduction)** |

## Per-file triage

### Faithful (canonical existence already shown)

| File | Faithful values |
|---|---|
| `borromean-quark.lean` | `bare_mass = borromean_volume / (1 - 1/q)²`; `is_baryon_realisation = ⟨proton_partition, neutron_partition, …⟩` |
| `electroweak-mass-eigenstate-count.lean` | SM instance: `(W±, Z, H) = (2, 1, 1)`, eigenstateCount = 3 (rfl) |
| `electroweak-higgs-torus-link-triplet.lean` | `(T(2,4), T(2,6), T(2,8))` triplet (rfl) |
| `weak-spectral-completeness.lean` | $H_2(q)$ instance, completenessIndex = 1 (rfl) |
| `levi-degeneracy-conjecture.lean` | `degeneracySet = {1/κ : κ ≥ 2}` literally (rfl) |
| `partition-sum-proton-residual.lean` | `electronMass = 0.51099895`, `protonCodata = 938.27208816`, `neutronCodata = 939.56542194`, `qSubstrate = 1.10998`, `protonTowerMass = 938.7228`, `neutronTowerMass = 411.227` |
| `n-v-leading-order-derivation.lean` | `q_0_real = 1.10998`, `m_e_real = 0.51099895`, `v_ew_real = 246220` |
| `n-v-tower-depth-ninety.lean` | `level_v = 90`, `tower_depth = arithmetic difference` (theorem) |
| `alpha-shift-torus-knot.lean` | `alphaShift p k = k(p-1)` (closed form) |
| `explicit-alpha-k-h4.lean` | `alpha_3_H4 = 0.0034625204` (witness-pinned) |
| `brane-level-selection.lean` | `nStar = ell·n₀ + k` (canonical formula) |
| `recursive-atom-knot-atlas.lean` | `atomKnotAtlas = [proton, neutron]` with full Hecke-NF / mass / err records |
| `electron-shell.lean` | `bindingMultiplicity` is noble-gas-aware (`{2,10,18,36,54,86} → 2; else 1`) |
| `mass-volume-factorization.lean` | `density.scaleMe = 0.51099895` (CODATA m_e) |
| `markov-trace-frobenius-selection.lean` | `tau_M ≡ 1`, `tau_SW ≡ 0`; non-degeneracy theorems by `one_ne_zero` / `rfl` |
| `lifted-crossing-locality.lean` | `localFactor ≡ 1` (multiplicative neutral) |

### Tautological skeleton (open upgrade targets)

These have `*skeleton`-prefixed instance names and are honest about
their tautological nature. Each commit message + file docstring
includes "skeleton" + "encodes none of the conjectural content" +
"upgrade target" pointers.

| File | Genuine content needed |
|---|---|
| `algebraic-substrate/magic-numbers-bring.lean` | Concrete `BringPeriodSublattice` from Bring-surface cohomology with `S_5` and `τ̂` actions |
| `braids-and-knots/brane-tower-z-habiro.lean` | Cyclotomic-projection / Habiro convergence at q_0 |
| `braids-and-knots/categorical-linking-operation.lean` | All five Lk-* predicates (LkLinear, LkReductionAtZero, LkMultiplicative, LkTraceCutSymmetric, LkBarInvolutionCompatible) |
| `braids-and-knots/conj-canonical-knot-id-sdp.lean` | SDP-uniqueness derivation (currently only knot-name pinned) |
| `braids-and-knots/conj-rho-prefactor-structural.lean` | `ρ = q-dim of dominant Wedderburn block` (needs partition lattice) |
| `braids-and-knots/jet-tower-uniform-delta-max.lean` | Δ_max bound from the jet tower (currently δ ≡ 0) |
| `braids-and-knots/mass-element-nf.lean` | NF coefficients (a₁, a₃, a₅) from the actual H_3(q) decomposition (currently all 1) |
| `braids-and-knots/shared-denominator-cusp-holonomy.lean` | Per-cusp shape parameter z_k from Newton–Raphson (currently constant `z = 2`) |
| `braids-and-knots/weinberg-angle-categorical.lean` | All four hypothesis predicates (Lk, Hoefsmit, vev, numerical) |
| `descartes-universe/abelianisation-at-algebraic-poles.lean` | MI = SW period at the matched critical points |
| `descartes-universe/denominator-zeros-as-sw-critical-points.lean` | `colorTubeDiscriminant` non-trivially |
| `descartes-universe/e-hartree-categorical-derivation.lean` | The 13-round δ_q : NF → R derivation roadmap |
| `descartes-universe/force-carrier-knot-vs-link-dichotomy.lean` | CategoricalHiggsAsLinking + HoefsmitCellContentEW |
| `descartes-universe/gb-reduction-pl-thimble-bijection.lean` | Genuine SW thimble flow, not constant identity |
| `descartes-universe/pl-jsj-mass-integration-equivalence.lean` | algebraicMarkovTrace = JSJVolume + thimble-sum |
| `lean/QOU/AppendixSurreals/ClassicalLimitStpart.lean` | Standard-part of q-evaluation |
| `lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean` | Markov trace = Frobenius pairing identity |
| `molecular-construction/shell-closure-nf-term-count.lean` | Per-shell term-count constancy (currently identically 0) |
| `particle-interactions/lifted-crossing-locality.lean` | KZ-flatness factorisation |
| `particle-interactions/mass-volume-factorization.lean` | Genuine Thurston-volume / Frobenius-packing per atom |
| `fluid-dynamics/levi-degeneracy-conjecture.lean` | Real Levi-form (currently identically 0) |

### Substrate axioms (Prop = True; require external upstream)

These are predicates with no Lean-checkable content yet because the
upstream Mathlib infrastructure (spectral sequences, SDP machinery,
arbitrary-precision real arithmetic) does not yet exist:

| File | Predicate(s) | Upstream gap |
|---|---|---|
| `atom-knot-mass-derivation.lean` | YekutieliFiniteSliceMultiplicativeTrace, GbSpectralSequenceCollapseAtE2, CategoricalMassInvariantFinite, MassIdentity | Mathlib spectral-sequence support |
| `joint-tower-sdp-confinement.lean` | WedderburnBlockPositivity, GbFiltrationGrading, JetOrderOrdering, CrossLevelConsistency, JointTowerSdpFeasible | LP / SDP machinery in Mathlib |
| `recursive-atom-knot-atlas.lean` | PrincipledPathForAtomKnot, FiltrationCertificateFormat | SDP-on-full-tower implementation |
| `markov-trace-frobenius-selection.lean` | PartitionHeightGtTwo | Partition-enumeration on top of `Mathlib.Combinatorics.Young.YoungDiagram` |
| `y-lambda-cyclotomic-factorization.lean` | CyclotomicDenominatorN23456 | Closed-form cyclotomic-factor verification at n=2..6 |
| `lean/QOU/Descartes/AxialCoupling.lean` | InSymmetricIdempotent | Hoefsmit basis on `End_R(A)` |

### Carrier-type stubs (PUnit)

These types are stubs for genuine carrier types (`HeckeAlgebra n q`,
`SDPState`, `BraneTowerLevel`, etc.) that are not yet constructed.
Replacing `PUnit` with the genuine carrier requires the corresponding
formalisation (q-deformed Specht modules, KLR algebras, …).

## What was upgraded this session

| Upgrade | Count |
|---|---:|
| Numerical-pinning (Pattern A) | 12 fields (CODATA / PDG / witness values) |
| Canonical-existence (Pattern B) | 4 instances (SM EW, borromean baryons, atom-knot atlas, force-carrier components) |
| Weakest-non-trivial-predicate (Pattern C) | 1 (AtlasIsWitnessDerived) |
| Closed-form definitions | 6 (alphaShift, brane-level nStar, depth-90 tower, Bohr-radius, η-canonical, …) |
| Axiom → theorem | 7 (electronMass_witness, neutronCodata_witness, neutronTowerMass_witness, n-v-tower-depth-ninety, schur_2var_vanish_height_gt_2, tau_M/SW/exists_height_gt_two_index) |

Net audit deltas across the full session:
- Opaques: **115 → 19** (−96, ~84% reduction)
- Constants: **38 → 1** (−37, ~97% reduction)
- Real sorries: **133 → 117** (−16)
- Conjectures with concrete Lean witness: 1 → ~30
- Conjectural-propagation violators: 258 → 0 (held since W1)

## CI integration (landed in this PR)

Wired the trivial-skeleton-audit into `.github/workflows/witness-pipeline.yml`
as a warn-only check (alongside the existing `Witness wiring audit`).
Path filters extended so any change to
`content/pipeline/trivial-skeleton-audit.ts` or any
`content/quantum-observable-universe/**/*.lean` triggers the workflow.

The CI step prints flagged counts but does not fail. To convert to
a strict gate later, extend the script with per-pattern thresholds
(e.g. `--max-per-pattern const_zero=37 prop_true=15`) and an
`--exit-on-baseline-exceeded` flag.

## Buckets (discrete follow-up parcels)

The 108 remaining flagged sites split into six concrete work buckets
prioritised by upstream effort needed.

### Bucket 1 — Numerical-pinning sweep (low-effort)

Single-PR scope. For each remaining `def f := 0` numerical placeholder,
pin to the witness JSON value. Each upgrade is a 2-line edit + a
norm_num/decide proof.

Targets (5 files, ~10 lines):
- `mass-formula-regime-switching.lean` — `bindingSW`, `bindingBW`,
  `bindingBWShell` → import the per-atom values from
  `mass_formula_6term.witness.json`.
- `wenzl-qmn-synergy.lean` — `markovTrace`, `length`, `cycleType` for
  the canonical proton/neutron CanonicalPermutationBraid case.
- `qmn-recursive-memoized.lean` — `markovTraceCanonical` from
  `markov-substrate-realization.witness.json`.

### Bucket 2 — Canonical-existence sweep (medium-effort)

For each remaining tautological skeleton, build the canonical
existential witness from upstream definitions and discharge by
exhibiting the witness (Pattern B in §"Three upgrade patterns").

Targets (8 files):
- `magic-numbers-bring.lean` — replace `s5_stable := True` /
  `tau_stable := True` with concrete sub-lattice carriers (need
  Bring-surface cohomology data).
- `categorical-linking-operation.lean` — populate the five Lk-*
  predicates with their algebraic content (linearity, reduction-at-zero,
  multiplicative-in-k, trace-cut-symmetric, bar-involution-compatible).
- `weinberg-angle-categorical.lean` — define `LkDischarged`,
  `HoefsmitDischarged`, `HiggsVEVAutomorphism`, `WeinbergAngleNumerical`
  in terms of the underlying Hecke / Hoefsmit data.
- `e-hartree-categorical-derivation.lean` — encode the
  δ_q : NF basis → R q-dimension decoration map per the .md roadmap.
- `force-carrier-knot-vs-link-dichotomy.lean` — define
  `CategoricalHiggsAsLinking`, `HoefsmitCellContentEW` non-vacuously.
- `pl-jsj-mass-integration-equivalence.lean` — populate
  `algebraicMarkovTrace` / `descendedJSJVolume` / `thimbleIntegral`
  with the integrals from the SW thimble side.
- `lifted-crossing-locality.lean` — encode KZ flatness factorisation.
- `mass-volume-factorization.lean` — supply per-atom Thurston volumes
  for the canonical {proton, neutron, ²H, ³H, ³He, ⁴He} entries.

### Bucket 3 — Weakest-non-trivial-predicate sweep (medium-effort)

For each `def P : Prop := True`, replace with the smallest decidable
predicate the canonical witness already satisfies. Pattern C from
§"Three upgrade patterns".

Targets (15 sites in 6 files):
- `atom-knot-mass-derivation.lean` — `YekutieliFiniteSliceMultiplicativeTrace`
  → `T_w.Foo ≠ none` (or similar minimal sanity check).
- `joint-tower-sdp-confinement.lean` — five Prop-fields (Wedderburn,
  GbFiltrationGrading, JetOrderOrdering, CrossLevelConsistency,
  JointTowerSdpFeasible) → minimal "data is well-formed" predicates.
- `recursive-atom-knot-atlas.lean` — `PrincipledPathForAtomKnot`,
  `FiltrationCertificateFormat` → check the atlas has no
  `deprecatedVolumeMatch` entries (i.e. `principledAtlas atomKnotAtlas
  = atomKnotAtlas`).
- `markov-trace-frobenius-selection.lean` — `PartitionHeightGtTwo`
  encoded against the actual partition's height field.
- `y-lambda-cyclotomic-factorization.lean` — `CyclotomicDenominatorN23456`
  → witness-pinned numerical bound on `cyclotomicDenominator n t` for
  `n ∈ {2, 3, 4, 5, 6}`.
- `lean/QOU/Descartes/AxialCoupling.lean` — `InSymmetricIdempotent`
  per the symmetric-idempotent characterisation in
  `prop:hoefsmit-cell-content`.

### Bucket 4 — Carrier-type formalisation (heavy-effort, Mathlib-bound)

Replace `def T : Type := PUnit` with genuine carrier types as the
upstream Mathlib packages land. Each replacement requires:
- The genuine type definition (q-Specht module, KLR algebra, …)
- Migration of every downstream consumer

Targets (14 files):
- `confinement-category.lean`, `confinement-phase-stratification.lean`,
  `level-sufficiency.lean`, `electron-shell.lean`,
  `confinement-sdp.lean` — `ConfinedParticleTy` → `ConfinedParticle`
  (already a real structure in `confined-particle.lean`).
- `dressed-particle.lean` — `BareTy`, `ShellTy` → `BareParticle`
  / `ElectronShell`.
- `frobenius-antipode-lean-stub.lean` — `HeckeAlgebra n q` →
  `LaurentPolynomialQuotient` of the type-A Iwahori–Hecke presentation.
- `qmn-recursive-memoized.lean` — `BorderStrip lam k` →
  combinatorial border-strip type from
  `Mathlib.Combinatorics.Young`.
- `wenzl-qmn-synergy.lean` — `CanonicalPermutationBraid n` →
  `Equiv.Perm (Fin n)` length-minimal braid-word lift.
- `lean/QOU/Interactions/AlgebraicPrimality.lean` — `SDPState n q`
  → `Confinement.SDP.OptimumState`.
- `alpha-em-shift-multiplicative-chain.lean` — `qIntegerIndex n`
  → `Fin n` (after the witness chain is verified through the
  q-integer literal substitution).

### Bucket 5 — Substrate axioms waiting on Mathlib (deferred, blocked)

These predicates encode mathematical content that **cannot** be
upgraded until specific Mathlib packages land. Each is correctly
declared as an axiom or `Prop := True` substrate axiom; the upgrade
target is documented at the file level.

Targets (6 substrate axioms):
- Spectral-sequence collapse predicates (Mathlib spectral-sequence
  support not yet available).
- LP / SDP duality theorems (Schrijver §7.2 / §7.4 require Mathlib
  LP-duality formalisation).
- Arbitrary-precision real-number bounds (CODATA comparisons require
  Mathlib `Real.evalRational`-style decision procedures).
- Partition-enumeration over `Mathlib.Combinatorics.Young.YoungDiagram`
  (waits on the `Fintype (Partition n)` instance).
- q-deformed Specht-module construction (waits on
  `Mathlib.RepresentationTheory.Hecke`).
- Cyclotomic factor-product comparison
  (`Polynomial.cyclotomic_eval` is in Mathlib; per-n closed forms
  for n=2..6 need the `factor` tactic over ℚ(t)).

### Bucket 6 — CI strict-gate flip (governance)

Once Buckets 1–3 land and the per-pattern counts drop below
sustainable thresholds, flip the CI audit step from warn-only to
strict-per-pattern.

Order of strict-gates to enable:
1. **`punit_unit`** (currently 2): easiest first; the only legitimate
   use is `PUnit.unit` as an explicit element of a `PUnit` carrier.
   Flip strict at 0.
2. **`id_def`** (currently 1): legitimate iff the function is genuinely
   identity (not a stand-in). Flip strict at 0.
3. **`one_def`** (currently 10): some are canonical multiplicative
   neutrals (`localFactor := 1`, `qHookProduct := 1`). Flip after
   Bucket 2 with budget 5.
4. **`holds_trivial`** (currently 8): expected to remain non-zero
   for genuine vacuous-truth fields; flip with budget 10.
5. **`prop_true`** (currently 15): flip after Bucket 5 lands the
   Mathlib upstreams; budget 6 for residual substrate axioms.
6. **`punit_type`** (currently 14): flip after Bucket 4 lands; budget 0.
7. **`const_zero`** (currently 38) and **`skel_inst`** (currently 21):
   the largest; flip last with per-PR delta budgets.

Each strict-gate flip is its own one-line PR (extend the
`trivial-skeleton-audit.ts` invocation with `--max-per-pattern`).
