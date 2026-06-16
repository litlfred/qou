# Plan: q Constant Interpretation Purge and QOU Realignment

This plan details the steps required to purge references to $q$ as an abstract global constant and align the codebase and literature with $q$ as the local fundamental mass ratio.

## Scope of Work
- **R1: Markdown Lit Realignment**: Update files in `content/quantum-observable-universe/` (in the folders specified in the audit manifest) to satisfy criteria:
  - `C1_Q_IDENTITY`: Purge descriptions of $q$ as rigid global constant/invisible ether; declare it mathematically synonymous with the mass ratio.
  - `C2_3_CALIBRATION_POINTS`: Frame around 3 calibration points ($m_e$, $m_\mu$, $Q_\beta$) as local physical fields derived from topological trace evaluated at local $q(p)$.
  - `C3_CAL2_VACUUM_LOCK`: Verify $m_\mu/m_e$ locks flat-space vacuum expectation value $q_0 \approx 1.1097$.
- **R2: Codebase Refactoring**: Scan `computations/` and `simulations/` for Python/Rust scripts using `q` as an abstract constant (e.g., `q_constant`) without mass-ratio context, and refactor them.
- **R3: Execution Verification**: Run representative sample of modified scripts to ensure logic is unbroken.

## Milestones

### Milestone 1: Scoping and Analysis (Investigation)
- **Objective**: Identify all markdown files and code files requiring modifications.
- **Task**: Spawn a `teamwork_preview_explorer` to scan the specified scope directories for violations of C1, C2, C3, and find code files that treat `q` as an abstract constant.
- **Verification**: Explorer produces a comprehensive handoff report detailing files to edit and proposed changes.

### Milestone 2: Expository Literature Update (Markdown Audit)
- **Objective**: Mechanically rewrite markdown files in scope.
- **Task**: Spawn a `teamwork_preview_worker` to apply the edits.
- **Verification**: Reviewers check files to ensure no violating phrases remain, and the 3 calibration points are correctly framed.

### Milestone 3: Computational Codebase Refactoring (Python/Rust)
- **Objective**: Refactor Python/Rust code to rename variables and rewrite comments/prints from abstract constant to mass ratio context.
- **Task**: Spawn a `teamwork_preview_worker` to perform the search and refactor.
- **Verification**: Reviewer checks that `q_constant` and similar names are removed or put into context.

### Milestone 4: Execution Validation
- **Objective**: Run representative scripts and verify they do not crash or produce unexpected results.
- **Task**: Spawn a `teamwork_preview_worker` to execute the scripts (e.g. `computations/build_q0_anchor_chain.py`, `simulations/q_double_slit.py`).
- **Verification**: Challenger/Reviewer confirms scripts execute with 0 exit code and expected outputs.

### Milestone 5: Forensic Integrity Audit & Final Verification
- **Objective**: Run the Forensic Auditor to confirm no integrity violations or cheating occurred.
- **Task**: Spawn a `teamwork_preview_auditor` to audit the changes.
- **Verification**: CLEAN audit verdict.
