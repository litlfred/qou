# Full-library red census after the #2094 repair thread (2026-06-11)

**Context.** PR #2094 repaired 31 red modules and deferred 2 diagnosed
roots; PR #2125 (this branch) repairs those 2 roots
(`Archimedean/HeckeH3`, `QGeometricLanglands`) — both verified green,
axiom-clean. The 2026-06-09 audit
([`2026-06-09-full-lib-lean-errors.md`](2026-06-09-full-lib-lean-errors.md))
predicted "likely more deeper in the closure"; this census quantifies
that remainder via a full `lake build QOU` on `main` + the two #2125
fixes (toolchain v4.24.0, restored olean cache).

**Headline: 51 ✖ build jobs, ~31 distinct first-error source files,
plus a 27-file stale-Mathlib-import inventory (overlapping). Zero
sandbox artifacts** — every failure was verified real: no
unknown-module/cache errors in the log, and each "missing Mathlib
module" was confirmed absent from the pinned Mathlib checkout (the
modules were renamed/split upstream). `QOU.Archimedean.HeckeH3` and
`QOU.QGeometricLanglands` are NOT in the list (green in the full pass).

## Class 1 — stale Mathlib module imports (mechanical rename sweep)

Five imported module names no longer exist in the pinned Mathlib;
every importer is red (directly or as an import casualty).

| stale import | importers |
|---|---|
| `Mathlib.Algebra.BigOperators.Basic` (split; `Finset.sum` core now in `Mathlib.Algebra.BigOperators.Group.Finset.*`) | 20 files: `FluidDynamics/leray_profile`, `WedderburnMass/confinement_categorical`, `WedderburnMass/chirality_residue_mass_term`, `Information/photon_threading_mass`, `TopologicalMass/cat_transient_localises_blowup`, `BraidsKnots/skein_mass_from_linking`, `FeynmanPathIntegrals/markov_identification`, `Archimedean/knot_operator_selection`, `ParticleInteractions/mass_categorical_descent`, `ParticleInteractions/lp_dual_stability`, `BraidKnot/e_infinity_identifications`, `BraidKnot/hoefsmit_scattering_pipeline`, `BraidKnot/PlancherelWeightBoundedness`, `BraidKnot/KnotFactorSpectralDerivation`, `Machinery/QDilogarithm`, `Machinery/QPochhammer`, `Observations/TraceLocalityMeetsGsNonLocality`, `BraidsAndKnots/demazure_fiber_markov_trace`, `LiftingDescent/tm_transient_localisation`, `Torsion/mass_decomposition_categorical` |
| `Mathlib.RingTheory.Subring.Basic` (→ `Mathlib.Algebra.Ring.Subring.Basic`) | `AppendixSurreals/StandardPart` |
| `Mathlib.Algebra.Polynomial.Induction` | `AppendixSurreals/PolynomialEval` |
| `Mathlib.CategoryTheory.Monoidal.Basic` (→ `…Monoidal.Category`) | `CategoricalDqSquared`, `LiftingDescent/JetProlongation`, `LiftingDescent/CosimplicialCrossedGroupoid` |
| `Mathlib.Algebra.Order.AbsoluteValue` (split under `…AbsoluteValue.Basic`) | `MassEndomorphism/DeltaMaxUniformBound`, `MassEndomorphism/PhiQConvergence` |

Fix shape: per-name rename sweep (verify the v4.24 target module per
name, then mechanical replace). One bulk commit per stale name is
appropriate (mechanical-sweep exception in CLAUDE.md).

## Class 2 — known v4.24 syntax/lint regressions (per-file, small)

| file | first error | known class (#2094 precedent) |
|---|---|---|
| `AlgebraicSubstrate/TwoFiltrationBridgeGeneral.lean:25` | `unexpected token 'λ'` | λ-token (LRFusion) |
| `AlgebraicSubstrate/TwoFiltrationBridgeSmallCases.lean:27` | `unexpected token 'λ'` | λ-token |
| `HeckeAlgebra/JonesMarkovWenzl.lean:118` | `unexpected token 'λ'` | λ-token |
| `Archimedean/AxialCoupling.lean:116` | `unexpected token '/--'; expected 'lemma'` | orphaned docstring |
| `AlgebraicSubstrate/SurrealSqueeze.lean:102` | `surreal_squeeze has already been declared` | duplicate decl (YekutieliTriple) |
| `LiftingDescent/DirectLimitAlgebra.lean:39` | `expected token` | syntax |
| `Observations/QCltNonCommutative.lean:57` | `invalid binder annotation` | binder syntax |

## Class 3 — `Unknown identifier ℕ/ℝ` (import-rot casualties / no-prelude)

`AppendixSurreals/B1HyperbolicRowsTheorem:19`,
`AppendixSurreals/B1SoftSharpnessTheorem:19`,
`FluidDynamics/q_bkm_criterion:32`,
`ParticleInteractions/atomic_lp_stability:25`,
`volume_from_rigidity:36` — ℕ/ℝ unknown means the Mathlib prelude never
loaded (broken/missing imports; same class as #2094's
`frobenius_antipode_unifies`).

## Class 4 — real proof/elaboration regressions (per-proof diagnosis needed)

| file | first error |
|---|---|
| `AppendixSurreals/KComplex.lean:103` | `No goals to be solved` |
| `Archimedean/MultiGeneratorSpectrum.lean:142` | `Unknown identifier altEigenvalue` |
| `Archimedean/OrderingIndependence.lean:143` | `Unknown identifier SkeinMultisetInvariant` |
| `Archimedean/PauliWitness/Witness12B.lean:13` | deterministic whnf timeout |
| `AtomicMass.lean` | maxErrors (100) reached — triage after upstream fixes |
| `BraidKnot/GramSeminormalBlock.lean:159` | failed to compile definition |
| `BraidKnot/NucleusEmptySDPUniqueness.lean:105` | failed to synthesize |
| `BraidKnot/WitnessR5Full.lean:67` | failed to generate projection `StrictComplementarityCert.min_block_eig` |
| `Braiding/HeckeGenPolyReduction.lean:81` | unsolved goals (NOTE: #2104 Phase 4 wants this re-verified) |
| `FeynmanPathIntegrals.lean:300` | application type mismatch |
| `FlavorDressing/FlavorMassSplittingBound.lean:100` | `Unknown identifier inv_lt_one_iff_of_pos` (renamed in Mathlib) |
| `Information/HeckeLogDecomposition.lean:37` | unsolved goals |
| `Interactions/BorromeanUnique.lean:104` | unsolved goals |
| `LightningPath.lean:100` | `Unknown identifier descartes_terminal` |
| `MassEndomorphism/MassEndomorphismConjecture.lean:72` | unsolved goals |
| `MathlibExt/RpowAlgebra.lean:51` | unsolved goals |
| `PhiQJSJ.lean:44` | unsolved goals |
| `su2_emergence_volume_determinant.lean:58` | `Unknown identifier SU2EmergenceContext` |

Several "Unknown identifier" rows are likely casualties of an upstream
red file in the same directory — re-triage after Classes 1–3 land.

## Recommended tranche order (follow-up branch, NOT #2125)

1. Class 1 rename sweep (5 bulk commits; unblocks the casualty chains)
2. Class 2 + Class 3 (mechanical, one commit per file)
3. Re-run full build; re-census Class 4 (expect shrinkage), then
   per-proof repairs in #2094 style (one commit each)

Census produced from `/tmp/build-full.log` (3,500+ jobs) on the #2125
branch; reproduce with `lake build QOU` after a cache restore per
`lean-environment-setup.md`.
