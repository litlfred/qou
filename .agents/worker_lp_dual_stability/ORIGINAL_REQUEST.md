## 2026-06-24T04:27:38Z
You are a teamwork_preview_worker.
Your task is to replace the `sorry` statement in `content/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean` with a valid Lean proof.

Working Directory:
Please write all your metadata files (progress.md, handoff.md, plan.md) in your own working directory: `/Users/litlfred/space_cats/qou/.agents/worker_lp_dual_stability/`. Do not write metadata files outside this folder.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

Instructions:
1. View the math description in the corresponding `.md` content file: `content/quantum-observable-universe/particle-interactions/lp-dual-stability.md`.
2. Edit `content/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean`:
   - Replace `import Mathlib.Algebra.BigOperators.Group.Finset.Basic` at the top with `import Mathlib`.
   - Replace the `sorry` in `theorem lp_dual_stability` with the proof:
     `⟨ctx.claim_i_primal_stable, ctx.claim_ii_dual_bounded, ctx.claim_iii_sub_braid_unstable, ctx.claim_iv_strong_duality⟩`
3. Run the validation tool to verify correctness: `./scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/ParticleInteractions/lp_dual_stability.lean`.
4. Create `progress.md` and `handoff.md` (which must include the output of the verify command showing it compiles successfully and is sorry-free) in your working directory.
5. Send a completion message to the parent (conversation ID: be00c364-ad77-4bc3-a81c-a94b2c5de0d9).
