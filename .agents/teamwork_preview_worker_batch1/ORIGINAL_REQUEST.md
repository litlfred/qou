# Worker Batch 1 Request

## Mission
Prove the 10 target stubs in the first batch of the Lean sorry stubs migration project.

## Working Directory
`/Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_batch1`

## Target Stubs to Prove
1. **`equivalence`** in `content/quantum-observable-universe/lean/QOU/BraidKnot/IsotopeKnot/equivalence.lean`
   - Complete the proof of `equivalence` using the reflexivity, symmetry, and transitivity fields from the `EquivalenceContext` class: `⟨ctx.claim_reflexivity, ctx.claim_symmetry, ctx.claim_transitivity⟩`.
2. **`antiparticle_crossing_reversal`** in `content/quantum-observable-universe/lean/QOU/Torsion/antiparticle_crossing_reversal.lean`
   - Complete the proof using the context class fields and `ctx.reversal_active`.
3. **`quadratic_form_two_index_proof`** in `content/quantum-observable-universe/lean/QOU/MathlibExt/Scratch.lean`
   - Prove the algebraic expansion of the 2x2 matrix quadratic form using `simp` and `ring`.
4-10. **The 7 lemmas** in `content/quantum-observable-universe/lean/QOU/HyperellipticQuintic/zeta5_residue_monodromy.lean`:
   - `zeta5_pow_five`
   - `zeta5_reductions`
   - `gauss_sum_5_reduced`
   - `zeta5_add_inv`
   - `cos_two_pi_fifths`
   - `gauss_sum_5_eval`
   - `gauss_sum_5_abs`

## Instructions
1. Replace each `sorry` statement in the targeted files with a valid Lean proof.
2. Follow all repository rules in `AGENTS.md` and `CLAUDE.md`, including:
   - **MANDATORY INTEGRITY WARNING**: DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
   - Every file modified must compile successfully. Verify using targeted `lean` checks or `lake build`.
3. Once all 10 stubs compile cleanly, write your handoff report to `/Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_batch1/handoff.md`.

## 2026-06-22T14:50:35Z
Prove the 10 target stubs in the first batch of the Lean sorry stubs migration project. Read /Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_batch1/ORIGINAL_REQUEST.md for full instructions. Write your handoff to /Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_batch1/handoff.md and send a completion message with your findings.
