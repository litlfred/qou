## 2026-06-24T04:22:44Z
You are worker_ground_state_ordering.
Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_ground_state_ordering/`.
Your objective is to:
1. Read the file `content/quantum-observable-universe/lean/QOU/ParticleInteractions/ground_state_ordering.lean`.
2. Add `import Mathlib` at the very top of the file.
3. Replace the `sorry` statement in the `ground_state_ordering` theorem with the following proof term:
`⟨ctx.claim_i_interleaving, ctx.claim_iii_boundary_correction, ctx.claim_vieta_product⟩`
4. Run `scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/ParticleInteractions/ground_state_ordering.lean` to verify that it type-checks and is sorry-free.
5. Create a handoff report in your directory explaining what you did, the commands run, and the verification results.
6. Send a message to parent (id: `77eb5e76-6c62-4186-abd7-faa7c0d38dae`) when complete with details.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
