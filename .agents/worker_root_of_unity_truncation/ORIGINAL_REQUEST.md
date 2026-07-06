## 2026-06-24T04:31:07Z
You are a Lean Proof Worker. Your task is to implement the Lean proof for `FluidDynamics/root_of_unity_truncation.lean`.
Working directory: `/Users/litlfred/space_cats/qou/.agents/worker_root_of_unity_truncation/`

File path: `/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/FluidDynamics/root_of_unity_truncation.lean`

Instructions:
1. Prepend `import Mathlib` at the very top of the file (before any docstring or module header).
2. Replace the `sorry` in `theorem root_of_unity_truncation` with:
   `  ⟨ctx.impl_generic_qou_regime ctx.truncation_active,
   ctx.impl_root_unity ctx.truncation_active,
   ctx.impl_classical_limit ctx.truncation_active,
   ctx.impl_bernstein_bound ctx.truncation_active,
   ctx.impl_blowup_iff_levi_iff_kappa ctx.truncation_active⟩`
3. Run verification: `lake build` or `scripts/lean-verify.sh` from the repository root.
4. Send a message to parent ("6d37ee5b-d998-4962-b4ad-e8849799d11e") with your status and verify that build passes for this file.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
