## 2026-06-24T04:27:39Z

You are a teamwork_preview_worker.
Your task is to replace the `sorry` statement in `content/quantum-observable-universe/lean/QOU/ParticleInteractions/SpectatorNormalization.lean` with a valid Lean proof.

Working Directory:
Please write all your metadata files (progress.md, handoff.md, plan.md) in your own working directory: `/Users/litlfred/space_cats/qou/.agents/worker_SpectatorNormalization/`. Do not write metadata files outside this folder.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Instructions:
1. View the math description in the corresponding `.md` content file: `content/quantum-observable-universe/particle-interactions/spectator-normalization.md`.
2. Edit `content/quantum-observable-universe/lean/QOU/ParticleInteractions/SpectatorNormalization.lean`:
   - Add `import Mathlib` at the top of the file.
   - Replace the `sorry` in `theorem SpectatorNormalization` with the proof:
     `⟨ctx.h_converting, ctx.h_spectator_p, ctx.h_spectator_n⟩`
3. Run the validation tool to verify correctness: `./scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/ParticleInteractions/SpectatorNormalization.lean`.
4. Create `progress.md` and `handoff.md` (which must include the output of the verify command showing it compiles successfully and is sorry-free) in your working directory.
5. Send a completion message to the parent (conversation ID: be00c364-ad77-4bc3-a81c-a94b2c5de0d9).
