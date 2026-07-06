# Work Plan - Lean Sorry Stub Proof Migration - Batch 9

## Milestone 1: Initialization & Branch Setup
- [x] Verify or checkout git branch `claude/prove-stubs-batch9-2026-06-23`
- [x] Restore/seed the Lean cache so workers have warm oleans (~2919 oleans) to compile against

## Milestone 2: Proving & Verification (Direct Iteration)
Spawn concurrent workers (up to 10) to:
- [x] File 1: `ParticleInteractions/lp_dual_stability.lean`
- [x] File 2: `ParticleInteractions/PerNucleonChannelDecomposition.lean`
- [x] File 3: `ParticleInteractions/positron_correction.lean`
- [x] File 4: `ParticleInteractions/SpectatorNormalization.lean`
- [x] File 5: `QuantumObservableUniverse/fibre_functor_atlas.lean`
- [x] File 6: `QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean`
- [x] File 7: `Substrate/ProtonMassSubstrateIdentity.lean`
- [x] File 8: `FluidDynamics/quantum_peter_weyl.lean`
- [x] File 9: `FluidDynamics/core_levi_form.lean`
- [x] File 10: `FluidDynamics/q_turbulence_spectrum.lean`

For each file, the worker must:
1. Locate the Lean file under `content/quantum-observable-universe/lean/QOU/`.
2. Locate the corresponding `.md` content file under `content/quantum-observable-universe/` or relevant sibling directory to understand the math.
3. Replace the `sorry` stub(s) with valid Lean proofs.
4. Ensure `import Mathlib` is at the top if using Real/Nat/Abs.
5. Verify using the `lean`-direct verification command or `lake build`.

## Milestone 3: Commit and Push
- [x] Verify all 10 files are compiled successfully.
- [x] Commit all changes.
- [x] Push branch to origin.
- [x] Report victory to the user.
