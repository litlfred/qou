## 2026-06-24T04:06:56Z
You are worker_batch6_integration. Your working directory is `/Users/litlfred/space_cats/qou/.agents/worker_batch6_integration/`.
Your task is to finalize all Lean proofs for Batch 6 on the branch `claude/prove-stubs-batch6-2026-06-23`.

Here is the exact state:
- The branch `claude/prove-stubs-batch6-2026-06-23` is already checked out in the shared workspace.
- `content/quantum-observable-universe/lean/QOU/Interactions/BorromeanUnique.lean` has already been modified in the worktree and is ready to be committed.
- The following 5 files still contain `sorry` statements and need their proofs implemented:

1. `content/quantum-observable-universe/lean/QOU/q_gl_obstruction_calc.lean`
Insert `import Mathlib` at the very top of the file (before the docstring).
Replace the `sorry` in `q_gl_obstruction_calc` with:
  ⟨ctx.claim_i_intrinsic_curvature_zero, ctx.claim_ii_q_flat_iff_curvature_zero, ctx.claim_iii_kummer_level_obstruction, ctx.claim_iv_non_vanish_density⟩

2. `content/quantum-observable-universe/lean/QOU/orbital_fourier_decomposition.lean`
Insert `import Mathlib` at the very top of the file (before the docstring).
Replace the `sorry` in `orbital_fourier_decomposition` with:
  ctx.claim_orbital_fourier_decomposition

3. `content/quantum-observable-universe/lean/QOU/qou_canonical_action.lean`
Insert `import Mathlib` at the very top of the file (before the docstring).
Replace the `sorry` in `qou_canonical_action` with:
  ctx.claim_qou_canonical_action

4. `content/quantum-observable-universe/lean/QOU/Archimedean/skein_finiteness_bound.lean`
Replace the `sorry` in `skein_finiteness_bound` with:
  ⟨ctx.claim_i_skein_factorisation, ctx.claim_ii_per_generator_positivity, ctx.claim_iii_stable_configurations_finite⟩

5. `content/quantum-observable-universe/lean/QOU/Archimedean/shell_structure_eigenvalues.lean`
Replace the `sorry` in `shell_structure_eigenvalues` with:
  ⟨ctx.claim_i_char_poly_product, ctx.claim_ii_eigenvalue_sum, ctx.claim_iii_chebyshev_second_kind, ctx.claim_iv_traced_volume⟩

Tasks:
1. Apply the proof modifications to the 5 files listed above.
2. Run the verification script to verify all Batch 6 files compile successfully:
   `scripts/lean-verify.sh \
     content/quantum-observable-universe/lean/QOU/variational_equations.lean \
     content/quantum-observable-universe/lean/QOU/q_gl_obstruction_calc.lean \
     content/quantum-observable-universe/lean/QOU/orbital_fourier_decomposition.lean \
     content/quantum-observable-universe/lean/QOU/qou_canonical_action.lean \
     content/quantum-observable-universe/lean/QOU/MassEndomorphism/PhiQConvergence.lean \
     content/quantum-observable-universe/lean/QOU/Interactions/BorromeanUnique.lean \
     content/quantum-observable-universe/lean/QOU/Interactions/QIntegerMassFormula.lean \
     content/quantum-observable-universe/lean/QOU/Archimedean/skein_finiteness_bound.lean \
     content/quantum-observable-universe/lean/QOU/Archimedean/torus_knot_shell_binding.lean \
     content/quantum-observable-universe/lean/QOU/Archimedean/shell_structure_eigenvalues.lean`
3. Stage all modified Lean files (`git add ...`) and commit them.
4. Push the branch to origin: `git push origin claude/prove-stubs-batch6-2026-06-23`.
5. Write a handoff report in your working directory and notify the parent (conversation ID: 837fa052-e939-4f89-aa75-7a97078c29a4).

DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
