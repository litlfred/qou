# Integration Task

You are the Integration Worker (teamwork_preview_worker).
Your working directory is `/Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_integration_gen5`.

## Objective
1. Inspect the git status and diff to see what changes are current in the workspace.
2. If `import QOU.HyperellipticQuintic.zeta5_residue_monodromy` is not present in `content/quantum-observable-universe/lean/QOU.lean`, add it in the appropriate imports section.
3. Verify that the entire QOU package compiles successfully using `lake build` or target compilation as per local environment guidelines.
4. Git stage and commit the modified files (Batch 1 proofs: `equivalence.lean`, `Scratch.lean`, `antiparticle_crossing_reversal.lean`, `zeta5_residue_monodromy.lean`, plus `QOU.lean` itself) to the current branch `claude/prove-stubs-teamwork-2026-06-22`.
5. Report the build status and commit details (e.g. git log).

## Scope Boundaries
- Do not add or modify any other files.
- Do not change any theorem signatures.

## Input Context
- The Batch 1 proofs are located in:
  - `content/quantum-observable-universe/lean/QOU/BraidKnot/IsotopeKnot/equivalence.lean`
  - `content/quantum-observable-universe/lean/QOU/Torsion/antiparticle_crossing_reversal.lean`
  - `content/quantum-observable-universe/lean/QOU/MathlibExt/Scratch.lean`
  - `content/quantum-observable-universe/lean/QOU/HyperellipticQuintic/zeta5_residue_monodromy.lean`
- The top-level package file:
  - `content/quantum-observable-universe/lean/QOU.lean`

## Output Requirements
- Write your progress/activity to `progress.md` in your working directory.
- Write your handoff to `handoff.md` in your working directory.
- Send a completion message back to the parent (conversation ID: 1b3b0b37-aad0-49cc-a9d9-792a6a140430) using `send_message`.

## Completion Criteria
- QOU.lean updated and compiled.
- Commits staged and pushed (or at least committed locally).
- Zero compilation errors.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## 2026-06-23T11:23:49Z
Run the integration task described in /Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_integration_gen5/ORIGINAL_REQUEST.md. Verify git status, add the import to QOU.lean, run lake build to verify, commit the files, and write handoff.md and progress.md in /Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_integration_gen5/ before sending a completion report back to parent.
