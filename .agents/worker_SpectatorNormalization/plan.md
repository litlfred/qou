# Plan — Spectator Normalization Proof

This plan details the steps to solve the task.

## Steps

1. **Investigate the Math Description**:
   - Read `content/quantum-observable-universe/particle-interactions/spectator-normalization.md` using `view_file` to understand context.
2. **Investigate the Lean implementation**:
   - Read `content/quantum-observable-universe/lean/QOU/ParticleInteractions/SpectatorNormalization.lean` using `view_file` to understand the code structure.
3. **Edit the Lean implementation**:
   - Add `import Mathlib` at the top of the file.
   - Replace `sorry` in `SpectatorNormalization` with `⟨ctx.h_converting, ctx.h_spectator_p, ctx.h_spectator_n⟩`.
4. **Verify correctness**:
   - Run `./scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/ParticleInteractions/SpectatorNormalization.lean`.
5. **Report & Handoff**:
   - Update `progress.md`.
   - Write `handoff.md` with observations, logic chain, caveats, conclusion, and verification command output.
   - Send completion message to parent conversation ID: `be00c364-ad77-4bc3-a81c-a94b2c5de0d9`.
