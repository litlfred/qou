## 2026-06-24T04:20:57Z
You are worker_atomic_nf_witness.
Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_atomic_nf_witness/`.
Your objective is to:
1. Read the file `content/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_nf_witness.lean`.
2. Add `import Mathlib` at the very top of the file.
3. Replace the `sorry` statement in the `atomic_nf_witness` theorem with a valid proof. Since the theorem statement is a conjunction of the fields of `AtomicNfWitnessContext`, the proof is:
`⟨ctx.claim_i_global_min_ordering, ctx.claim_ii_greedy_electron_placement, ctx.claim_iii_gb_convergence, ctx.claim_iv_NF_accumulation, ctx.claim_v_certificate_definition⟩`
4. Run `scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_nf_witness.lean` to verify the correctness of the proof. Ensure it type-checks and is sorry-free.
5. Create a handoff report in your directory explaining what you did, the commands run, and the verification results.
6. Send a message to parent (id: `77eb5e76-6c62-4186-abd7-faa7c0d38dae`) when complete with details.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
