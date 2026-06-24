## 2026-06-24T04:22:44Z
You are worker_deuterium_derived_binding.
Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_deuterium_derived_binding/`.
Your objective is to:
1. Read the file `content/quantum-observable-universe/lean/QOU/ParticleInteractions/deuterium_derived_binding.lean`.
2. Add `import Mathlib` at the very top of the file.
3. Replace the `sorry` in `deuterium_derived_binding` with:
`⟨ctx.claim_i_NF_existence, ctx.claim_ii_B3_factorisation, ctx.claim_iii_h6_factorisation, ctx.claim_iv_Tpn_symmetric, ctx.claim_v_binding_energy_formula, ctx.claim_vi_codata_match⟩`
4. Replace the `sorry` in `mass_binding_prefactor_deuteron` with:
```lean
  obtain ⟨h1, h2⟩ := mass_binding_share_prefactor (a := a)
  rw [h1, h2, h]
```
5. Run `scripts/lean-verify.sh content/quantum-observable-universe/lean/QOU/ParticleInteractions/deuterium_derived_binding.lean` to verify that it type-checks and is sorry-free.
6. Create a handoff report in your directory explaining what you did, the commands run, and the verification results.
7. Send a message to parent (id: `77eb5e76-6c62-4186-abd7-faa7c0d38dae`) when complete with details.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
