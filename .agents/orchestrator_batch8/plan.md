# Batch 8 Lean Proof Migration Plan

## 1. Initial State Assessment
- Target files are located under `content/quantum-observable-universe/lean/QOU/ParticleInteractions/`.
- There are 10 target files.
- Each target file has corresponding `.md` content under `content/quantum-observable-universe/particle-interactions/`.

## 2. Target Files Breakdown
1. `ParticleInteractions/atomic_nf_witness.lean`
   - Maps to: `prop:atomic-nf-witness`
   - Content: Conjunction of fields in `AtomicNfWitnessContext`.
2. `ParticleInteractions/parity_regime_selection.lean`
   - Maps to: `prop:parity-regime-selection`
3. `ParticleInteractions/four_term_pair_nucleon.lean`
   - Maps to: `prop:four-term-pair-nucleon`
4. `ParticleInteractions/confinement_frobenius_reciprocity.lean`
   - Maps to: `prop:confinement-frobenius-reciprocity`
5. `ParticleInteractions/operator_selection_lp.lean`
   - Maps to: `prop:operator-selection-lp`
6. `ParticleInteractions/ground_state_ordering.lean`
   - Maps to: `prop:ground-state-ordering`
7. `ParticleInteractions/mass_categorical_descent.lean`
   - Maps to: `prop:mass-categorical-descent`
8. `ParticleInteractions/transfer_matrix_identities.lean`
   - Maps to: `prop:transfer-matrix-identities`
9. `ParticleInteractions/deuterium_derived_binding.lean`
   - Maps to: `prop:deuterium-derived-binding`
10. `ParticleInteractions/frobenius_positivity_filter.lean`
    - Maps to: `prop:frobenius-positivity-filter`

## 3. Workflows and Tools
- Use `teamwork_preview_worker` or `self` to replace `sorry` with valid proofs.
- Set up a queue of 10 workers, running concurrently (maximum 10).
- For files using ℝ, ℕ, or | |, ensure `import Mathlib` is added.
- Run `scripts/lean-verify.sh` or direct `lean` execution on each file to verify.

## 4. Verification and Integration
- Each worker will run verification locally and provide passing outputs.
- Once all are validated, check signatures are unchanged (using `git diff`).
- Perform the audit via `teamwork_preview_auditor` if needed, or directly check that there are no sorries left.
- Push to branch `claude/prove-stubs-batch8-2026-06-23`.
