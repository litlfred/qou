## 2026-06-24T04:11:15Z

You are a teamwork_preview_worker named worker_m10.
Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_m10/`.
Task:
1. Read the target file `content/quantum-observable-universe/lean/QOU/ParticleInteractions/demand_stability.lean`.
2. Ensure `import Mathlib` is placed at the very top of the file, before any other content (including doc comments).
3. Replace `sorry` with the valid Lean proof:
   `by refine ⟨ctx.claim_i_beta_stable, ctx.claim_ii_shell_closed, ctx.claim_iii_doubly_magic⟩`
4. Verify using `scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/ParticleInteractions/demand_stability.lean`.
5. Write your `handoff.md` detailing the changes and verification output, and report back.

MANDATORY INTEGRITY WARNING:
> DO NOT CHEAT. All implementations must be genuine. DO NOT
> hardcode test results, create dummy/facade implementations, or
> circumvent the intended task. A Forensic Auditor will independently
> verify your work. Integrity violations WILL be detected and your
> work WILL be rejected.
