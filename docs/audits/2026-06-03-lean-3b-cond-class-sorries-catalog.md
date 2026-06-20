# §3b-cond conditional-class sorries — catalog (2026-06-03)

> Discharge-queue artefact for the lean-discharge queue item
> `lean-3b-cond-class-sorries-catalog` (priority: high, status: open).
> Enumerates all Lean `class` declarations that contain a `sorry` in
> their body — the §3b-cond conjectural inputs per AGENTS.md.

## What §3b-cond is (and why these sorries are PERMANENT)

AGENTS.md §3b-cond (the conditional-class exception) lets a
`theorem` / `proposition` / `lemma` / `corollary` block whose
`uses[]` cone transitively touches a `conj:C` keep its provable
block kind **iff**:

1. **Class axiomatisation.** `conj:C` has a Lean `class C`
   declaration with class fields encoding the conjecture's content.
   **The class instance is the only `sorry` in the entire downstream
   chain.**
2. **Explicit hypothesis on Lean side.** The downstream block's
   Lean declaration has the class as an explicit `[Instance]`
   hypothesis.
3. **Explicit conditional banner on narrative side.** The `.md`
   block opens with: **Theorem (conditional on
   [`conj:C`](path/to/C.md)).**
4. **`uses[]` includes the conjecture explicitly.**

When all four hold, the downstream theorem is a *rigorous
conditional result* — fully verified by Lean modulo a single,
named, class-axiomatised conjectural input.

The `sorry` inside the `class C` body **IS the conjectural input**.
It is **permanent by design**. Removing it would mean proving the
conjecture — which is a different (research-grade) endeavour. The
catalog below is **NOT a discharge target list**; it is a
**reference list** so future sessions don't waste cycles
investigating a §3b-cond class sorry as if it were a missing proof.

Discharge guidance:

- ❌ **Do not** attempt to discharge any `sorry` in a `class` body
  unless you are explicitly proving a conjecture.
- ✓ Do verify any class-body sorry against the §3b-cond
  4-condition test. Most should pass trivially (they're the
  whole reason the class exists).
- ✓ Sorries in `theorem` / `lemma` / `proposition` / `def` /
  `instance` bodies are **separate** from this catalog and ARE
  potentially dischargeable (subject to the cache-host 403
  blocker — see `infra-lean-cache-host-bypass`).

## Headline

| Stat | Value |
|---|---|
| `.lean` files in `content/quantum-observable-universe/lean/QOU/` with `sorry` | **241** |
| Raw `sorry` text matches (includes comments / docstrings) | 653 (uncorrected) — **491** with the `(?!-)` correction |
| **Lean classes with `sorry` in body (§3b-cond catalog)** | **194** |
| **Total class-body sorries** | **219** |
| Approximate non-class sorries (potentially dischargeable) | **~272** |

## By area rollup

| Area | Classes | Class-body sorries |
|---|---:|---:|
| `BraidKnot` | 37 | 43 |
| `AppendixSurreals` | 16 | 30 |
| `ParticleInteractions` | 18 | 18 |
| `Archimedean` | 15 | 17 |
| `FluidDynamics` | 17 | 17 |
| `BraidsAndKnots` | 9 | 9 |
| `Observations` | 8 | 9 |
| `QuantumObservableUniverse` | 7 | 7 |
| `Braiding` | 6 | 6 |
| `Molecular` | 6 | 6 |
| `Torsion` | 5 | 6 |
| `Information` | 4 | 5 |
| `Interactions` | 5 | 5 |
| `LiftingDescent` | 5 | 5 |
| `ArchimedeanUniverse` | 4 | 4 |
| `BraidsKnots` | 4 | 4 |
| `QGeometricLanglands` | 4 | 4 |
| `WedderburnMass` | 4 | 4 |
| `AlgebraicSubstrate` | 3 | 3 |
| `HadronicMass` | 3 | 3 |
| `TopologicalMass` | 3 | 3 |
| `Brings` | 2 | 2 |
| `Experimental` | 2 | 2 |
| `BaryonWeight` | 1 | 1 |
| `CategoricalReeb` | 1 | 1 |
| `CommutativeQOU` | 1 | 1 |
| `Descent` | 1 | 1 |
| `Encounter` | 1 | 1 |
| `FeynmanPathIntegrals` | 1 | 1 |
| `FrobeniusHopfData` | 1 | 1 |
| `HyperellipticQuintic` | 1 | 1 |
| `Kashaev` | 1 | 1 |
| `PhiQJSJ` | 1 | 1 |
| `QuantumBloch` | 1 | 1 |
| `StaircaseCornerHook` | 1 | 1 |
| `orbital_fourier_decomposition` | 1 | 1 |
| `q_gl_obstruction_calc` | 1 | 1 |
| `qou_canonical_action` | 1 | 1 |
| **TOTAL** | **202** | **227** |

## Full enumeration

### [`AlgebraicSubstrate/collatz_contact_boundary.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/collatz_contact_boundary.lean)

- `class CollatzContactBoundaryContext` (line 17) — **1** sorry

### [`AlgebraicSubstrate/collatz_no_cycles.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/collatz_no_cycles.lean)

- `class CollatzNoCyclesContext` (line 17) — **1** sorry

### [`AlgebraicSubstrate/qou_obstruction_reduction.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AlgebraicSubstrate/qou_obstruction_reduction.lean)

- `class QouObstructionReductionContext` (line 18) — **1** sorry

### [`AppendixSurreals/ArchimedeanStpart.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/ArchimedeanStpart.lean)

- `class ArchimedeanStpart` (line 25) — **2** sorryes

### [`AppendixSurreals/BigbangHeatdeath.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/BigbangHeatdeath.lean)

- `class BigbangHeatdeath` (line 25) — **2** sorryes

### [`AppendixSurreals/ClassicalLimitStpart.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/ClassicalLimitStpart.lean)

- `class ClassicalLimitStpart` (line 44) — **1** sorry

### [`AppendixSurreals/DiophantineBirthday.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/DiophantineBirthday.lean)

- `class DiophantineBirthday` (line 25) — **2** sorryes

### [`AppendixSurreals/HahnSubstrate.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/HahnSubstrate.lean)

- `class HahnSubstrate` (line 25) — **2** sorryes

### [`AppendixSurreals/InfinitesimalFrobenius.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/InfinitesimalFrobenius.lean)

- `class InfinitesimalFrobenius` (line 25) — **2** sorryes

### [`AppendixSurreals/InfinitesimalObservability.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/InfinitesimalObservability.lean)

- `class InfinitesimalObservability` (line 25) — **2** sorryes

### [`AppendixSurreals/JonesBirthday.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/JonesBirthday.lean)

- `class JonesBirthday` (line 25) — **2** sorryes

### [`AppendixSurreals/KashaevSurreal.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/KashaevSurreal.lean)

- `class KashaevSurreal` (line 25) — **2** sorryes

### [`AppendixSurreals/LocalInfinitesimalField.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/LocalInfinitesimalField.lean)

- `class LocalInfinitesimalField` (line 25) — **2** sorryes

### [`AppendixSurreals/OnPModularHecke.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/OnPModularHecke.lean)

- `class OnPModularHecke` (line 25) — **2** sorryes

### [`AppendixSurreals/QBirchSwinnertonDyer.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/QBirchSwinnertonDyer.lean)

- `class QBirchSwinnertonDyer` (line 25) — **2** sorryes

### [`AppendixSurreals/QCollatz.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/QCollatz.lean)

- `class QCollatz` (line 25) — **1** sorry

### [`AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/QouInfraDischargesGoncharovZeta5.lean)

- `class QouInfraDischargesGoncharovZeta5` (line 25) — **2** sorryes

### [`AppendixSurreals/SpectralNormalForm.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/SpectralNormalForm.lean)

- `class SpectralNormalForm` (line 25) — **2** sorryes

### [`AppendixSurreals/VacuumEpsilon.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/AppendixSurreals/VacuumEpsilon.lean)

- `class VacuumEpsilon` (line 25) — **2** sorryes

### [`Archimedean/BorelZagierQouVolumes.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/BorelZagierQouVolumes.lean)

- `class BorelZagierQouVolumes` (line 25) — **2** sorryes

### [`Archimedean/HyperbolicVolumeIndependence.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/HyperbolicVolumeIndependence.lean)

- `class HyperbolicVolumeIndependence` (line 25) — **1** sorry

### [`Archimedean/MassTowerOpenProblemsClasses.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/MassTowerOpenProblemsClasses.lean)

- `class Term7ShellCorrectionClass` (line 62) — **1** sorry
- `class ChiralityFactorClass` (line 123) — **1** sorry
- `class ZHabiroConvergenceClass` (line 155) — **1** sorry
- `class AlphaOver4PiClass` (line 183) — **1** sorry

### [`Archimedean/PauliWitness/witness_12C.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/PauliWitness/witness_12C.lean)

- `class Witness12CContext` (line 17) — **1** sorry

### [`Archimedean/PauliWitness/witness_4He.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/PauliWitness/witness_4He.lean)

- `class Witness4HeContext` (line 17) — **1** sorry

### [`Archimedean/PauliWitness/witness_8Be.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/PauliWitness/witness_8Be.lean)

- `class Witness8BeContext` (line 17) — **1** sorry

### [`Archimedean/SingleVolumeIrrationality.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/SingleVolumeIrrationality.lean)

- `class SingleVolumeIrrationality` (line 25) — **2** sorryes

### [`Archimedean/ThreeSubstantiveMathlibFillers.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/ThreeSubstantiveMathlibFillers.lean)

- `class Cl_2_PentagonHolds` (line 100) — **1** sorry
- `class FaddeevKashaevQuasiClassicalLimit` (line 137) — **1** sorry
- `class HasAllSubstantiveFillers` (line 162) — **1** sorry

### [`Archimedean/archimedean_hartree_derivation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/archimedean_hartree_derivation.lean)

- `class ArchimedeanHartreeDerivationContext` (line 19) — **1** sorry

### [`Archimedean/knot_operator_selection.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Archimedean/knot_operator_selection.lean)

- `class KnotOperatorSelectionContext` (line 22) — **1** sorry

### [`ArchimedeanUniverse/brings_euler_characteristic.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ArchimedeanUniverse/brings_euler_characteristic.lean)

- `class BringsEulerCharacteristicContext` (line 19) — **1** sorry

### [`ArchimedeanUniverse/brings_riemann_hurwitz.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ArchimedeanUniverse/brings_riemann_hurwitz.lean)

- `class BringsRiemannHurwitzContext` (line 18) — **1** sorry

### [`ArchimedeanUniverse/heisenberg_commutator.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ArchimedeanUniverse/heisenberg_commutator.lean)

- `class HeisenbergCommutatorContext` (line 17) — **1** sorry

### [`ArchimedeanUniverse/mi_sw_cartan_reduction.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ArchimedeanUniverse/mi_sw_cartan_reduction.lean)

- `class MiSwCartanReductionContext` (line 18) — **1** sorry

### [`BaryonWeight/beta4_hook.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BaryonWeight/beta4_hook.lean)

- `class Beta4HookContext` (line 19) — **1** sorry

### [`BraidKnot/BringFigureEightDepth2Witness.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/BringFigureEightDepth2Witness.lean)

- `class BringFigureEightDepth2Witness` (line 25) — **1** sorry

### [`BraidKnot/BringTrilogDepth3Witness.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/BringTrilogDepth3Witness.lean)

- `class BringTrilogDepth3Witness` (line 25) — **1** sorry

### [`BraidKnot/CemeteryGroupEmergence.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/CemeteryGroupEmergence.lean)

- `class CemeteryGroupEmergence` (line 34) — **1** sorry

### [`BraidKnot/Cl3Zeta5GeometricRealization.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/Cl3Zeta5GeometricRealization.lean)

- `class Cl3Zeta5GeometricRealization` (line 25) — **2** sorryes

### [`BraidKnot/ClassicalRiemannHypothesis.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/ClassicalRiemannHypothesis.lean)

- `class ClassicalRiemannHypothesis` (line 25) — **2** sorryes

### [`BraidKnot/ConfinementGradingCorrespondence.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/ConfinementGradingCorrespondence.lean)

- `class ConfinementGradingCorrespondence` (line 34) — **1** sorry

### [`BraidKnot/ConfinementNfStructureForcing.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/ConfinementNfStructureForcing.lean)

- `class ConfinementNfStructureForcing` (line 25) — **2** sorryes

### [`BraidKnot/CrystalGraphRealization.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/CrystalGraphRealization.lean)

- `class CrystalGraphRealization` (line 45) — **1** sorry

### [`BraidKnot/CrystalRMatrixSubLemma.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/CrystalRMatrixSubLemma.lean)

- `class CrystalRMatrixSubLemma` (line 74) — **1** sorry

### [`BraidKnot/GBResidueSpectralSum/residue.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum/residue.lean)

- `class residue` (line 25) — **1** sorry

### [`BraidKnot/GBResidueSpectralSum/spectral_decomposition.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/GBResidueSpectralSum/spectral_decomposition.lean)

- `class spectral_decomposition` (line 25) — **1** sorry

### [`BraidKnot/GradedBaerStarHq.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/GradedBaerStarHq.lean)

- `class GradedBaerStarHq` (line 25) — **1** sorry

### [`BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/HabiroResidueSumEquivalence/archimedean_agreement.lean)

- `class archimedean_agreement` (line 25) — **1** sorry

### [`BraidKnot/HabiroResidueSumEquivalence/protonExample/archimedean_agreement.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/HabiroResidueSumEquivalence/protonExample/archimedean_agreement.lean)

- `class archimedean_agreement` (line 25) — **1** sorry

### [`BraidKnot/HeckeAnyonicSubstrate.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/HeckeAnyonicSubstrate.lean)

- `class HeckeAnyonicSubstrate` (line 54) — **1** sorry

### [`BraidKnot/JointGaloisBraidAction.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/JointGaloisBraidAction.lean)

- `class JointGaloisBraidAction` (line 25) — **2** sorryes

### [`BraidKnot/KazhdanLusztigClassicalLimit.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/KazhdanLusztigClassicalLimit.lean)

- `class KazhdanLusztigClassicalLimit` (line 43) — **1** sorry

### [`BraidKnot/KnotFactorFrobeniusPairing.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/KnotFactorFrobeniusPairing.lean)

- `class KnotFactorFrobeniusPairing` (line 47) — **1** sorry

### [`BraidKnot/NSymSymmetricChannelNormalization.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/NSymSymmetricChannelNormalization.lean)

- `class NSymSymmetricChannelNormalization` (line 25) — **2** sorryes

### [`BraidKnot/RootOfUnityMTCTruncation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/RootOfUnityMTCTruncation.lean)

- `class RootOfUnityMTCTruncation` (line 45) — **1** sorry

### [`BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/SixTermPerDerivationWeights/binding_assembly.lean)

- `class BindingAssemblyContext` (line 22) — **1** sorry

### [`BraidKnot/SubstrateEWHypotheses.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean)

- `class SubstrateEWDerivations` (line 96) — **1** sorry

### [`BraidKnot/SymmetricCrystalPairProduction.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/SymmetricCrystalPairProduction.lean)

- `class SymmetricCrystalPairProduction` (line 39) — **1** sorry

### [`BraidKnot/Term6BindingDensity.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/Term6BindingDensity.lean)

- `class Term6BindingDensity` (line 67) — **1** sorry

### [`BraidKnot/TwoFiltrationBridge.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/TwoFiltrationBridge.lean)

- `class TwoFiltrationBridge` (line 25) — **2** sorryes

### [`BraidKnot/ZeqNRhoCorrection.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/ZeqNRhoCorrection.lean)

- `class ZeqNRhoCorrection` (line 76) — **1** sorry

### [`BraidKnot/algebraic_quantum_volume_specialization.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/algebraic_quantum_volume_specialization.lean)

- `class AlgebraicQuantumVolumeSpecializationContext` (line 22) — **1** sorry

### [`BraidKnot/chirality_frobenius_self_pairing.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/chirality_frobenius_self_pairing.lean)

- `class ChiralityFrobeniusSelfPairingContext` (line 19) — **1** sorry

### [`BraidKnot/confined_knot_binding.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/confined_knot_binding.lean)

- `class ConfinedKnotBindingContext` (line 20) — **1** sorry

### [`BraidKnot/e_infinity_identifications.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/e_infinity_identifications.lean)

- `class EInfinityIdentificationsContext` (line 22) — **1** sorry

### [`BraidKnot/geom_yekutieli_alignment.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/geom_yekutieli_alignment.lean)

- `class GeomYekutieliAlignmentContext` (line 19) — **1** sorry

### [`BraidKnot/jet_convergence_classical_limit.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/jet_convergence_classical_limit.lean)

- `class jet_convergence_classical_limit` (line 25) — **1** sorry

### [`BraidKnot/jet_filtered_knot_factor.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/jet_filtered_knot_factor.lean)

- `class jet_filtered_knot_factor` (line 25) — **1** sorry

### [`BraidKnot/jet_prefix_gb_filtration.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/jet_prefix_gb_filtration.lean)

- `class JetPrefixGbFiltrationContext` (line 20) — **1** sorry

### [`BraidKnot/spectral_sequence_h3_explicit.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/spectral_sequence_h3_explicit.lean)

- `class SpectralSequenceH3ExplicitContext` (line 20) — **1** sorry

### [`BraidKnot/spectral_sum_finite.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/spectral_sum_finite.lean)

- `class spectral_sum_finite` (line 25) — **1** sorry

### [`BraidKnot/terms_2_6_higher_operations.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidKnot/terms_2_6_higher_operations.lean)

- `class Terms26HigherOperationsContext` (line 21) — **1** sorry

### [`Braiding/beta_stability.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Braiding/beta_stability.lean)

- `class BetaStabilityContext` (line 18) — **1** sorry

### [`Braiding/fermion_boson_knot_link.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Braiding/fermion_boson_knot_link.lean)

- `class FermionBosonKnotLinkContext` (line 18) — **1** sorry

### [`Braiding/hecke_mass_trace.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Braiding/hecke_mass_trace.lean)

- `class HeckeMassTraceContext` (line 37) — **1** sorry

### [`Braiding/mobius_energy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Braiding/mobius_energy.lean)

- `class MobiusEnergyContext` (line 21) — **1** sorry

### [`Braiding/reidemeister_mass_invariance.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Braiding/reidemeister_mass_invariance.lean)

- `class ReidemeisterMassInvarianceContext` (line 18) — **1** sorry

### [`Braiding/skein_crossing_asymmetry.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Braiding/skein_crossing_asymmetry.lean)

- `class SkeinCrossingAsymmetryContext` (line 23) — **1** sorry

### [`BraidsAndKnots/QSchurYLambdaClosedForm.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/QSchurYLambdaClosedForm.lean)

- `class QSchurYLambdaClosedFormClaim` (line 149) — **1** sorry

### [`BraidsAndKnots/S4S3HalfSymmetricProjection.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S4S3HalfSymmetricProjection.lean)

- `class BorromeanCommonScale` (line 121) — **1** sorry

### [`BraidsAndKnots/demazure_fiber_markov_trace.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/demazure_fiber_markov_trace.lean)

- `class DemazureFiberMarkovTraceContext` (line 26) — **1** sorry

### [`BraidsAndKnots/ew_interface_knot.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ew_interface_knot.lean)

- `class EwInterfaceKnotContext` (line 21) — **1** sorry

### [`BraidsAndKnots/explicit_alpha_k_h4.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/explicit_alpha_k_h4.lean)

- `class ExplicitAlphaKH4Context` (line 24) — **1** sorry

### [`BraidsAndKnots/qmn_recursive_memoized.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/qmn_recursive_memoized.lean)

- `class QmnRecursiveMemoizedContext` (line 24) — **1** sorry

### [`BraidsAndKnots/wedderburn_bratteli_recursion.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/wedderburn_bratteli_recursion.lean)

- `class WedderburnBratteliRecursionContext` (line 24) — **1** sorry

### [`BraidsAndKnots/wenzl_qmn_synergy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/wenzl_qmn_synergy.lean)

- `class WenzlQmnSynergyContext` (line 24) — **1** sorry

### [`BraidsAndKnots/y_lambda_recipe_from_partition.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsAndKnots/y_lambda_recipe_from_partition.lean)

- `class YLambdaRecipeFromPartitionContext` (line 24) — **1** sorry

### [`BraidsKnots/mobius_frobenius_kernel.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsKnots/mobius_frobenius_kernel.lean)

- `class MobiusFrobeniusKernelContext` (line 18) — **1** sorry

### [`BraidsKnots/nsi_q_deformed_kernel.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsKnots/nsi_q_deformed_kernel.lean)

- `class NsiQDeformedKernelContext` (line 18) — **1** sorry

### [`BraidsKnots/skein_mass_from_linking.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsKnots/skein_mass_from_linking.lean)

- `class SkeinMassFromLinkingContext` (line 20) — **1** sorry

### [`BraidsKnots/tmli_constituent_composite_agreement.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/BraidsKnots/tmli_constituent_composite_agreement.lean)

- `class TmliConstituentCompositeAgreementContext` (line 21) — **1** sorry

### [`Brings/brings_is_qou.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Brings/brings_is_qou.lean)

- `class BringsIsQouContext` (line 18) — **1** sorry

### [`Brings/coral_elliptic.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Brings/coral_elliptic.lean)

- `class CoralEllipticContext` (line 21) — **1** sorry

### [`CategoricalReeb/ofWeightDecomposition.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/CategoricalReeb/ofWeightDecomposition.lean)

- `class OfWeightDecompositionContext` (line 17) — **1** sorry

### [`CommutativeQOU/u1EquivariantReduction.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/CommutativeQOU/u1EquivariantReduction.lean)

- `class U1EquivariantReductionContext` (line 19) — **1** sorry

### [`Descent/descended_level_zero.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Descent/descended_level_zero.lean)

- `class DescendedLevelZeroContext` (line 18) — **1** sorry

### [`Encounter/MostowRigidity.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Encounter/MostowRigidity.lean)

- `class MostowRigidity` (line 122) — **1** sorry

### [`Experimental/local_substrate_q.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Experimental/local_substrate_q.lean)

- `class LocalSubstrateQContext` (line 19) — **1** sorry

### [`Experimental/terminal_resolution.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Experimental/terminal_resolution.lean)

- `class TerminalResolutionContext` (line 18) — **1** sorry

### [`FeynmanPathIntegrals/markov_identification.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FeynmanPathIntegrals/markov_identification.lean)

- `class MarkovIdentificationContext` (line 21) — **1** sorry

### [`FluidDynamics/acoustic_horizon_conditions.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/acoustic_horizon_conditions.lean)

- `class AcousticHorizonConditionsContext` (line 20) — **1** sorry

### [`FluidDynamics/core_levi_form.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/core_levi_form.lean)

- `class CoreLeviFormContext` (line 21) — **1** sorry

### [`FluidDynamics/discrete_vortex_spectrum.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/discrete_vortex_spectrum.lean)

- `class DiscreteVortexSpectrumContext` (line 21) — **1** sorry

### [`FluidDynamics/helicity_conservation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/helicity_conservation.lean)

- `class HelicityConservationContext` (line 21) — **1** sorry

### [`FluidDynamics/kelvin_dispersion_derivation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/kelvin_dispersion_derivation.lean)

- `class KelvinDispersionDerivationContext` (line 20) — **1** sorry

### [`FluidDynamics/leray_profile.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/leray_profile.lean)

- `class LerayProfileContext` (line 22) — **1** sorry

### [`FluidDynamics/ns_kummer_specialisation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/ns_kummer_specialisation.lean)

- `class NsKummerSpecialisationContext` (line 20) — **1** sorry

### [`FluidDynamics/ns_obstruction_computation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/ns_obstruction_computation.lean)

- `class NsObstructionComputationContext` (line 20) — **1** sorry

### [`FluidDynamics/ns_obstruction_tower.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/ns_obstruction_tower.lean)

- `class NsObstructionTowerContext` (line 20) — **1** sorry

### [`FluidDynamics/ns_singularity_descartes.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/ns_singularity_descartes.lean)

- `class NsSingularityDescartesContext` (line 20) — **1** sorry

### [`FluidDynamics/p1_nonlinear_uniqueness.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/p1_nonlinear_uniqueness.lean)

- `class P1NonlinearUniquenessContext` (line 21) — **1** sorry

### [`FluidDynamics/p1_spectral_sobolev.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/p1_spectral_sobolev.lean)

- `class P1SpectralSobolevContext` (line 19) — **1** sorry

### [`FluidDynamics/p4_universality.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/p4_universality.lean)

- `class P4UniversalityContext` (line 19) — **1** sorry

### [`FluidDynamics/q_ns_wellposedness.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/q_ns_wellposedness.lean)

- `class QNsWellposednessContext` (line 22) — **1** sorry

### [`FluidDynamics/q_turbulence_spectrum.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/q_turbulence_spectrum.lean)

- `class QTurbulenceSpectrumContext` (line 23) — **1** sorry

### [`FluidDynamics/root_of_unity_truncation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/root_of_unity_truncation.lean)

- `class RootOfUnityTruncationContext` (line 19) — **1** sorry

### [`FluidDynamics/vorticity_lower_bound.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FluidDynamics/vorticity_lower_bound.lean)

- `class VorticityLowerBoundContext` (line 20) — **1** sorry

### [`FrobeniusHopfData/frobeniusForm.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/FrobeniusHopfData/frobeniusForm.lean)

- `class FrobeniusFormContext` (line 17) — **1** sorry

### [`HadronicMass/deuteron_binding_energy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/HadronicMass/deuteron_binding_energy.lean)

- `class DeuteronBindingEnergyContext` (line 21) — **1** sorry

### [`HadronicMass/nucleon_borromean_topology.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/HadronicMass/nucleon_borromean_topology.lean)

- `class NucleonBorromeanTopologyContext` (line 18) — **1** sorry

### [`HadronicMass/pair_skein_mass_formula.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/HadronicMass/pair_skein_mass_formula.lean)

- `class PairSkeinMassFormulaContext` (line 21) — **1** sorry

### [`HyperellipticQuintic/minimal_z5_classification.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/HyperellipticQuintic/minimal_z5_classification.lean)

- `class MinimalZ5ClassificationContext` (line 17) — **1** sorry

### [`Information/QouPNeqNp.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Information/QouPNeqNp.lean)

- `class QouPNeqNp` (line 25) — **2** sorryes

### [`Information/photon_threading_mass.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Information/photon_threading_mass.lean)

- `class PhotonThreadingMassContext` (line 21) — **1** sorry

### [`Information/reeb_operations_per_planck.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Information/reeb_operations_per_planck.lean)

- `class ReebOperationsPerPlanckContext` (line 21) — **1** sorry

### [`Information/toffoli_transfer_matrix.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Information/toffoli_transfer_matrix.lean)

- `class ToffoliTransferMatrixContext` (line 23) — **1** sorry

### [`Interactions/DoubleMagicDeltaI/DeltaIBoundConjecture.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Interactions/DoubleMagicDeltaI/DeltaIBoundConjecture.lean)

- `class DeltaIBoundConjecture` (line 25) — **1** sorry

### [`Interactions/UniversalILP.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Interactions/UniversalILP.lean)

- `class UniversalILPContext` (line 19) — **1** sorry

### [`Interactions/confinementUniversality.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Interactions/confinementUniversality.lean)

- `class ConfinementUniversalityContext` (line 19) — **1** sorry

### [`Interactions/inductiveGBReduction.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Interactions/inductiveGBReduction.lean)

- `class InductiveGBReductionContext` (line 19) — **1** sorry

### [`Interactions/nucleon_ordering_factorization.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Interactions/nucleon_ordering_factorization.lean)

- `class NucleonOrderingFactorizationContext` (line 19) — **1** sorry

### [`Kashaev.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Kashaev.lean)

- `class VolumeConjecture` (line 57) — **1** sorry

### [`LiftingDescent/jp_categorical_jet.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/LiftingDescent/jp_categorical_jet.lean)

- `class JpCategoricalJetContext` (line 18) — **1** sorry

### [`LiftingDescent/tm_descended_is_holonomy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/LiftingDescent/tm_descended_is_holonomy.lean)

- `class TmDescendedIsHolonomyContext` (line 19) — **1** sorry

### [`LiftingDescent/tm_dilogarithm_evaluation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/LiftingDescent/tm_dilogarithm_evaluation.lean)

- `class TmDilogarithmEvaluationContext` (line 18) — **1** sorry

### [`LiftingDescent/tm_eigenspace_decomp.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/LiftingDescent/tm_eigenspace_decomp.lean)

- `class TmEigenspaceDecompContext` (line 19) — **1** sorry

### [`LiftingDescent/tm_transient_localisation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/LiftingDescent/tm_transient_localisation.lean)

- `class TmTransientLocalisationContext` (line 20) — **1** sorry

### [`Molecular/benzene_threading_emergence.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Molecular/benzene_threading_emergence.lean)

- `class BenzeneThreadingEmergenceContext` (line 21) — **1** sorry

### [`Molecular/ch4_lp_dual_binding.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Molecular/ch4_lp_dual_binding.lean)

- `class Ch4LpDualBindingContext` (line 21) — **1** sorry

### [`Molecular/co2_lp_dual_binding.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Molecular/co2_lp_dual_binding.lean)

- `class Co2LpDualBindingContext` (line 21) — **1** sorry

### [`Molecular/co_lp_dual_binding.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Molecular/co_lp_dual_binding.lean)

- `class CoLpDualBindingContext` (line 21) — **1** sorry

### [`Molecular/h2_lp_dual_binding.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Molecular/h2_lp_dual_binding.lean)

- `class H2LpDualBindingContext` (line 23) — **1** sorry

### [`Molecular/shell_filling_rule.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Molecular/shell_filling_rule.lean)

- `class ShellFillingRuleContext` (line 19) — **1** sorry

### [`Observations/QCltNonCommutative/QCltNonCommutative.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/QCltNonCommutative/QCltNonCommutative.lean)

- `class QCltNonCommutative` (line 25) — **2** sorryes

### [`Observations/QPlancherelAsymptoticSkeleton.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/QPlancherelAsymptoticSkeleton.lean)

- `class QPlancherelAsymptoticSkeletonContext` (line 21) — **1** sorry

### [`Observations/SDPRegimeSwitch.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/SDPRegimeSwitch.lean)

- `class SDPRegimeSwitchContext` (line 19) — **1** sorry

### [`Observations/brane_tower_q_laplacian_decay.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/brane_tower_q_laplacian_decay.lean)

- `class BraneTowerQLaplacianDecayContext` (line 20) — **1** sorry

### [`Observations/centered_hecke_variance_positive.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/centered_hecke_variance_positive.lean)

- `class CenteredHeckeVariancePositiveContext` (line 19) — **1** sorry

### [`Observations/hecke_satisfies_blitvic_hypothesis.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/hecke_satisfies_blitvic_hypothesis.lean)

- `class HeckeSatisfiesBlitvicHypothesisContext` (line 21) — **1** sorry

### [`Observations/strangelet_crossing_energy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/strangelet_crossing_energy.lean)

- `class StrangeletCrossingEnergyContext` (line 20) — **1** sorry

### [`Observations/substrate_consistency_window.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Observations/substrate_consistency_window.lean)

- `class SubstrateConsistencyWindowContext` (line 18) — **1** sorry

### [`ParticleInteractions/PerNucleonChannelDecomposition.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/PerNucleonChannelDecomposition.lean)

- `class PerNucleonChannelDecompositionContext` (line 23) — **1** sorry

### [`ParticleInteractions/SpectatorNormalization.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/SpectatorNormalization.lean)

- `class SpectatorNormalizationContext` (line 19) — **1** sorry

### [`ParticleInteractions/atomic_nf_witness.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_nf_witness.lean)

- `class AtomicNfWitnessContext` (line 21) — **1** sorry

### [`ParticleInteractions/confinement_frobenius_reciprocity.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_frobenius_reciprocity.lean)

- `class ConfinementFrobeniusReciprocityContext` (line 20) — **1** sorry

### [`ParticleInteractions/confinement_operator_selection.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/confinement_operator_selection.lean)

- `class ConfinementOperatorSelectionContext` (line 21) — **1** sorry

### [`ParticleInteractions/demand_stability.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/demand_stability.lean)

- `class DemandStabilityContext` (line 20) — **1** sorry

### [`ParticleInteractions/deuterium_derived_binding.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/deuterium_derived_binding.lean)

- `class DeuteriumDerivedBindingContext` (line 21) — **1** sorry

### [`ParticleInteractions/four_term_pair_nucleon.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/four_term_pair_nucleon.lean)

- `class FourTermPairNucleonContext` (line 20) — **1** sorry

### [`ParticleInteractions/frobenius_positivity_filter.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/frobenius_positivity_filter.lean)

- `class FrobeniusPositivityFilterContext` (line 19) — **1** sorry

### [`ParticleInteractions/ground_state_ordering.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/ground_state_ordering.lean)

- `class GroundStateOrderingContext` (line 20) — **1** sorry

### [`ParticleInteractions/lp_dual_stability.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean)

- `class LpDualStabilityContext` (line 22) — **1** sorry

### [`ParticleInteractions/mass_categorical_descent.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/mass_categorical_descent.lean)

- `class MassCategoricalDescentContext` (line 22) — **1** sorry

### [`ParticleInteractions/neutron_qvalue_symbolic.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/neutron_qvalue_symbolic.lean)

- `class NeutronQvalueSymbolicContext` (line 19) — **1** sorry

### [`ParticleInteractions/operator_selection_lp.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/operator_selection_lp.lean)

- `class OperatorSelectionLpContext` (line 23) — **1** sorry

### [`ParticleInteractions/parity_regime_selection.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/parity_regime_selection.lean)

- `class ParityRegimeSelectionContext` (line 20) — **1** sorry

### [`ParticleInteractions/positron_correction.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/positron_correction.lean)

- `class PositronCorrectionContext` (line 19) — **1** sorry

### [`ParticleInteractions/transfer_matrix_identities.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/transfer_matrix_identities.lean)

- `class TransferMatrixIdentitiesContext` (line 20) — **1** sorry

### [`ParticleInteractions/tritium_qvalue_symbolic.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/ParticleInteractions/tritium_qvalue_symbolic.lean)

- `class TritiumQvalueSymbolicContext` (line 19) — **1** sorry

### [`PhiQJSJ.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/PhiQJSJ.lean)

- `class PerPieceBridge` (line 73) — **1** sorry

### [`QGeometricLanglands/q_gl_classical_limit.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_gl_classical_limit.lean)

- `class q_gl_classical_limit` (line 25) — **1** sorry

### [`QGeometricLanglands/q_gl_fiber_functor.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_gl_fiber_functor.lean)

- `class q_gl_fiber_functor` (line 25) — **1** sorry

### [`QGeometricLanglands/q_gl_kummer_filtration.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_gl_kummer_filtration.lean)

- `class q_gl_kummer_filtration` (line 25) — **1** sorry

### [`QGeometricLanglands/q_oper_hecke.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QGeometricLanglands/q_oper_hecke.lean)

- `class q_oper_hecke` (line 25) — **1** sorry

### [`QuantumBloch/pentagon_uv_commutation.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumBloch/pentagon_uv_commutation.lean)

- `class PentagonUvCommutationContext` (line 20) — **1** sorry

### [`QuantumObservableUniverse/exists_axiom_1_frobenius.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/exists_axiom_1_frobenius.lean)

- `class ExistsAxiom1FrobeniusContext` (line 18) — **1** sorry

### [`QuantumObservableUniverse/exists_axiom_2_observability.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/exists_axiom_2_observability.lean)

- `class ExistsAxiom2ObservabilityContext` (line 18) — **1** sorry

### [`QuantumObservableUniverse/exists_axiom_3_chern.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/exists_axiom_3_chern.lean)

- `class ExistsAxiom3ChernContext` (line 18) — **1** sorry

### [`QuantumObservableUniverse/exists_axiom_4_volume.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/exists_axiom_4_volume.lean)

- `class ExistsAxiom4VolumeContext` (line 18) — **1** sorry

### [`QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean)

- `class FaiProjectorCoadjointOrbitContext` (line 18) — **1** sorry

### [`QuantumObservableUniverse/fibre_functor_atlas.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/fibre_functor_atlas.lean)

- `class FibreFunctorAtlasContext` (line 20) — **1** sorry

### [`QuantumObservableUniverse/observation_energy.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/observation_energy.lean)

- `class ObservationEnergyContext` (line 18) — **1** sorry

### [`StaircaseCornerHook/StaircaseEWResidual.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/StaircaseCornerHook/StaircaseEWResidual.lean)

- `class StaircaseEWResidual` (line 25) — **1** sorry

### [`TopologicalMass/cat_descended_is_base_mass.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/TopologicalMass/cat_descended_is_base_mass.lean)

- `class CatDescendedIsBaseMassContext` (line 19) — **1** sorry

### [`TopologicalMass/cat_eigenspace_decomposition.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/TopologicalMass/cat_eigenspace_decomposition.lean)

- `class CatEigenspaceDecompositionContext` (line 19) — **1** sorry

### [`TopologicalMass/cat_transient_localises_blowup.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/TopologicalMass/cat_transient_localises_blowup.lean)

- `class CatTransientLocalisesBlowupContext` (line 20) — **1** sorry

### [`Torsion/KnotParticleGeneration.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Torsion/KnotParticleGeneration.lean)

- `class KnotParticleGenerationContext` (line 18) — **1** sorry

### [`Torsion/YangMillsMassGap.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Torsion/YangMillsMassGap.lean)

- `class YangMillsMassGap` (line 25) — **2** sorryes

### [`Torsion/antiparticle_crossing_reversal.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Torsion/antiparticle_crossing_reversal.lean)

- `class AntiparticleCrossingReversalContext` (line 20) — **1** sorry

### [`Torsion/mass_decomposition_categorical.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Torsion/mass_decomposition_categorical.lean)

- `class MassDecompositionCategoricalContext` (line 21) — **1** sorry

### [`Torsion/weak_equiv_invariance.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/Torsion/weak_equiv_invariance.lean)

- `class WeakEquivInvarianceContext` (line 19) — **1** sorry

### [`WedderburnMass/chirality_residue_mass_term.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/WedderburnMass/chirality_residue_mass_term.lean)

- `class ChiralityResidueMassTermContext` (line 20) — **1** sorry

### [`WedderburnMass/confinement_categorical.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/WedderburnMass/confinement_categorical.lean)

- `class ConfinementCategoricalContext` (line 22) — **1** sorry

### [`WedderburnMass/curvature_rank_gb_stratification.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/WedderburnMass/curvature_rank_gb_stratification.lean)

- `class CurvatureRankGbStratificationContext` (line 20) — **1** sorry

### [`WedderburnMass/exterior_square_borromean.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/WedderburnMass/exterior_square_borromean.lean)

- `class ExteriorSquareBorromeanContext` (line 20) — **1** sorry

### [`orbital_fourier_decomposition.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/orbital_fourier_decomposition.lean)

- `class OrbitalFourierDecompositionContext` (line 17) — **1** sorry

### [`q_gl_obstruction_calc.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/q_gl_obstruction_calc.lean)

- `class QGlObstructionCalcContext` (line 18) — **1** sorry

### [`qou_canonical_action.lean`](https://github.com/litlfred/qou/blob/main/content/quantum-observable-universe/lean/QOU/qou_canonical_action.lean)

- `class QouCanonicalActionContext` (line 17) — **1** sorry

## Verification convention (for future sessions)

When you encounter a `sorry` in a `.lean` file:

1. **Check if it's inside a `class` body.** Scroll up from the
   `sorry` line until you hit either `class <Name>` (this is a
   §3b-cond conditional-class sorry — catalogued above; **leave
   alone**) or `theorem | lemma | def | instance` (this is a
   regular sorry — potentially dischargeable).
2. **For class-body sorries**, search this catalog for the class
   name. If listed, it's expected; move on.
3. **If a class-body sorry is NOT in this catalog**, it was added
   after 2026-06-03. Regenerate the catalog (see methodology
   below).
4. **For non-class sorries**, check the lean-discharge queue
   (`.beans/lean-discharge-queue.json`) for an existing item; if
   none, the sorry may be a candidate for triage once the
   cache-host blocker is resolved.

## Methodology

Generated by Python regex against `content/quantum-observable-universe/lean/QOU/**/*.lean`:

```python
for f in glob.glob('content/quantum-observable-universe/lean/QOU/**/*.lean', recursive=True):
    content = open(f).read()
    for m in re.finditer(r'^(class\s+(\w+)[^\n]*?)$', content, re.MULTILINE):
        start = m.end()
        rest = content[start:]
        # Find next top-level declaration
        next_decl = re.search(
            r'^(class\s|theorem\s|lemma\s|def\s|noncomputable\s|axiom\s|'
            r'instance\s|namespace\s|end\s|@\[)', rest, re.MULTILINE
        )
        body = rest[:next_decl.start()] if next_decl else rest
        sorries = len(re.findall(r'\bsorry\b', body))
        # ...
```

**Known imprecisions:**

- The class-body scan stops at the next top-level declaration
  pattern. If a class has a nested `def` inside `where ... :=`,
  the scan may stop early. Spot-checking the high-density classes
  did not surface mis-attribution, but the catalog should be
  treated as ~5% imprecise rather than exact.
- The `sorry` regex must use the negative lookahead
  `\bsorry\b(?!-)` to skip the `sorry-free` docstring phrase. The
  pre-correction regex `\bsorry\b` over-counts by **162** matches
  (~25 %), almost all in
  `BraidKnot/PeriodicTableUniqueness.lean` (119 `sorry-free`
  abbrevs for the 119-element periodic-table coverage). The
  headline numbers above are post-correction; the legacy 255-file
  / 653-sorry / 202-class / 227-class-body / ~426-non-class
  figures cited in earlier audit drafts and skill docs are
  inflated artefacts of the old regex.
- "Class with `sorry`" includes classes whose fields use
  `extend` patterns or `decide` placeholders; the catalog should
  be the START of analysis, not the END.

## Cross-refs

- [`.beans/lean-discharge-queue.json`](../../.beans/lean-discharge-queue.json) — work queue (10 items, all blocked on `infra-lean-cache-host-bypass`)
- [`docs/audits/2026-06-03-lean-axiom-tractability-triage.md`](2026-06-03-lean-axiom-tractability-triage.md) — companion: which **axioms** are tractable (77 total, 6 tractable)
- [`docs/audits/2026-06-03-proof-objects-json-extractor-broken.md`](2026-06-03-proof-objects-json-extractor-broken.md) — why the gh-pages manifest has been stale 45 days
- [AGENTS.md §3b-cond](../../AGENTS.md) — the formal definition of the conditional-class exception

## Follow-ups (out of scope for this PR)

- **Sorry-distribution triage for the ~426 non-class sorries**.
  Cannot be done in this container until the cache-host fix lands
  (needs `lean_diagnostic_messages` against a built project to
  distinguish TRACTABLE / PROBLEMATIC / RESEARCH-GRADE per the
  queue item `lean-discharge-triage-pass`).
- **§3b-cond compliance audit**. Spot-check 5-10 classes in this
  catalog against the 4-condition test and confirm they all pass.
  If any fail, flag as either (a) needs banner / `uses[]` fix
  (mechanical), or (b) shouldn't be §3b-cond at all (escalate).
- **`proof-objects.json` rewrite** so the gh-pages manifest can
  carry this catalog as a public artefact (currently broken — see
  the companion audit).
