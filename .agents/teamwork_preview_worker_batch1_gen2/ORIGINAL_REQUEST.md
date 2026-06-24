## 2026-06-22T21:44:05Z
You are the worker agent 'teamwork_preview_worker_batch1_gen2'.
Your working directory is '/Users/litlfred/space_cats/qou/.agents/teamwork_preview_worker_batch1_gen2'.
Your parent is '505a533e-73e7-4484-b926-4abc8bd52d72'.

Your mission is to replace the 7 remaining `sorry` stubs in `content/quantum-observable-universe/lean/QOU/HyperellipticQuintic/zeta5_residue_monodromy.lean` with valid, compiling Lean 4 proofs.

The target lemmas to prove in `HyperellipticQuintic/zeta5_residue_monodromy.lean` are:
1. `zeta5_pow_five`
2. `zeta5_reductions`
3. `gauss_sum_5_reduced`
4. `zeta5_add_inv`
5. `cos_two_pi_fifths`
6. `gauss_sum_5_eval`
7. `gauss_sum_5_abs`

### Prerequisites and Rules
- Read and follow '.claude/skills/local/lean-environment-setup.md' and '.claude/skills/local/lean-build-fix.md'.
- To check or verify your files, restore the prebuilt oleans from the orphan branch `lake-cache/qou-v4-24-0` (refer to the instructions in 'lean-environment-setup.md').
- Use the direct `lean` compilation path or targeted lake command rather than rebuilding all of QOU from scratch if it's too slow.
- Do NOT modify the signatures of these lemmas.
- You must verify that the file builds cleanly with zero errors or sorry warnings.
- Keep 'progress.md' updated in your working directory as a heartbeat.
- Write a final handoff report 'handoff.md' in your working directory.
- Send a message to your parent upon completion or if you get blocked.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A Forensic Auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.
