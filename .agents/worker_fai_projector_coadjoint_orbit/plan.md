# Plan - worker_fai_projector_coadjoint_orbit

1. **Investigate Codebase**:
   - Confirm target file location: `content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean`.
   - Confirm target file contents (we just did).
2. **Apply Changes**:
   - Add `import Mathlib` at the top of the Lean file.
   - Replace `sorry` with `ctx.twice_sigma_eq_id_of_projector ctx.ρ_proj` in `theorem fai_projector_coadjoint_orbit`.
3. **Verify Changes**:
   - Execute verification script: `./scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/fai_projector_coadjoint_orbit.lean`.
   - Verify that the output has no errors, compiles successfully, and contains no `sorry` statements.
4. **Handoff and Completion**:
   - Update `progress.md`.
   - Write `handoff.md` with verification command output.
   - Send message to parent.
