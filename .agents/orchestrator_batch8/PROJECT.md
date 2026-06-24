# Project: Lean Sorry Stub Proof Migration - Batch 8

## Architecture
- Target files are located under `content/quantum-observable-universe/lean/QOU/`.
- Verifications are done using `lake build` or `scripts/lean-verify.sh`.
- The project implements mathematical proofs for various topological, algebraic, and analytical observations in QOU.

## Target Files (Batch 8)
1. `ParticleInteractions/atomic_nf_witness.lean`
2. `ParticleInteractions/parity_regime_selection.lean`
3. `ParticleInteractions/four_term_pair_nucleon.lean`
4. `ParticleInteractions/confinement_frobenius_reciprocity.lean`
5. `ParticleInteractions/operator_selection_lp.lean`
6. `ParticleInteractions/ground_state_ordering.lean`
7. `ParticleInteractions/mass_categorical_descent.lean`
8. `ParticleInteractions/transfer_matrix_identities.lean`
9. `ParticleInteractions/deuterium_derived_binding.lean`
10. `ParticleInteractions/frobenius_positivity_filter.lean`

## Active Goal
Select the 10 files listed above. Spawn 10 worker subagents (up to 10 concurrently) to:
- Read corresponding `.md` content files.
- Understand the math.
- Write valid Lean proofs to replace the `sorry` statements.
- Insert `import Mathlib` at the top of files using ℝ, ℕ, or | | to prevent synthesis issues.
- Verify proofs compile via `scripts/lean-verify.sh` or `lake build`.
Once all 10 are completed and verified, commit all changes to branch `claude/prove-stubs-batch8-2026-06-23`, push to origin, and report victory.
