## 2026-06-24T00:31:07Z
You are a Lean Proof Worker. Your task is to implement the Lean proof for `FluidDynamics/helicity_conservation.lean`.
Working directory: `/Users/litlfred/space_cats/qou/.agents/worker_helicity_conservation/`

File path: `/Users/litlfred/space_cats/qou/content/quantum-observable-universe/lean/QOU/FluidDynamics/helicity_conservation.lean`

Instructions:
1. Prepend `import Mathlib` at the very top of the file (before any docstring or module header).
2. Replace the `sorry` in `theorem helicity_conservation` with:
   `  ⟨ctx.impl_conservation ctx.conservation_active,
   ctx.impl_CWF_decomposition ctx.conservation_active,
   ctx.impl_jones_refinement ctx.conservation_active,
   ctx.impl_classical_limit ctx.conservation_active⟩`
3. Run verification: `lake build` or `scripts/lean-verify.sh` from the repository root.
4. Send a message to parent ("6d37ee5b-d998-4962-b4ad-e8849799d11e") with your status and verify that build passes for this file.
