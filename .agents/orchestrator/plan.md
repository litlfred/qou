# Plan - Mass-Theory Lean Formalization Repair Verification

We are verifying the 8 Lean formalization repairs for the mass-theory chapter.

## Steps

1. **Verify Workspace State**
   - Run `git status` and `git branch` to check the current branch.
   - Switch to `feature/options-2-and-4` if not already on it.
   - Ensure the workspace is clean.

2. **Verify Lean Compilation and Goal Closure**
   - Check compilation of the 8 `.lean` files in `content/quantum-observable-universe/mass-theory/`:
     - `alpha-shift-torus-knot.lean`
     - `gb-depth-period-correspondence.lean`
     - `knot-indexed-convolution-grid.lean`
     - `lr-coefficient-hecke.lean`
     - `pentagon-uv-commutation.lean`
     - `residue-at-root.lean`
     - `alpha-k-derivation-procedure.lean`
     - `atom-knot-mass-derivation.lean`
   - Use lean tools to verify all goals are closed and there are no warnings or compilation errors.

3. **Verify Proof Integrity (Forensic Audit)**
   - Run the Forensic Auditor to check for unexpected axioms, `sorryAx`, or hardcoded bypasses.
   - Ensure the audit verdict is `CLEAN`.

4. **Verify QA Pipeline Re-evaluation**
   - Run the QA sweep script: `bun run content/pipeline/qa-sweep.ts content/quantum-observable-universe/mass-theory`
   - Ensure the `.qa.json` files are properly updated with `pass` and score `1.0` for `proof-statement-integrity` and `proof-rater-goal-plausibility`.

5. **Document Results & Handoff**
   - Document final status in `.agents/orchestrator/progress.md`.
   - Write `.agents/orchestrator/handoff.md`.
   - Send completion message to parent.
