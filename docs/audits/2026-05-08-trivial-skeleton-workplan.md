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

## Audit summary (post-upgrades)

| Pattern | Count |
|---|---:|
| `const_zero`     | 38  (some converted to canonical numbers; rest awaiting upstream values) |
| `skel_inst`      | 21  (intentional `*skeleton`-named instances per CLAUDE.md §3b-cond) |
| `prop_true`      | 15  (substrate axioms; most need Mathlib spectral-sequence / SDP machinery) |
| `punit_type`     | 14  (carrier-type stubs; require genuine Hecke / atom data structures) |
| `one_def`        | 10  (multiplicative-neutral defaults; `localFactor := 1` is canonical for trivial links) |
| `holds_trivial`  | 8   (vacuous proofs of `True` / `0=0` / `rfl`; some are intentional) |
| `punit_unit`     | 2   |
| `id_def`         | 1   |
| `const_zero_typed` | 1 |

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

## Next steps (deferred)

- **Run the trivial-skeleton-audit in CI** as a warn-only check; flip
  to a strict gate per-pattern as upgrades land. Suggested PR: add a
  `bun run pipeline/trivial-skeleton-audit.ts --max-flagged N` mode.
- **Faithful Hecke / Mathlib bridge**: the carrier-type stubs and
  Prop=True predicates that wait on Mathlib's q-Specht modules,
  spectral sequences, and SDP machinery should be revisited as those
  packages land.
- **Upstream the canonical instances**: every faithful witness should
  appear in the corresponding `.witness.json` so the Python compute
  pipeline and the Lean defs share a single source of truth.
