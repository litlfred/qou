# Original User Request

## 2026-06-14T13:11:43Z

Evaluate the remaining 18 batches (220 blocks) in `todos/qa-agent-drain-queue.json` robustly and accurately. The agents must ensure all assigned criteria are evaluated and logged via `qa-agent-write.ts` without skipping files or hallucinating completion.

Working directory: /home/litlfred/space_cats/qou
Integrity mode: demo

## Requirements

### R1. Complete the QA Backlog
The teamwork agents must fully evaluate the 220 remaining blocks (or 806 gaps) listed in `todos/qa-agent-drain-queue.json`. 

### R2. Thorough File Review
For each block, the agents must thoroughly cross-reference the corresponding `.md` and `.lean` files to determine a pass, fail, or warn score for the required criteria.

### R3. Controlled Verdict Recording
The agents must record their verdicts explicitly using the provided pipeline script: `bun run content/pipeline/qa-agent-write.ts`. The team must verify that the script successfully executed and updated the corresponding `.qa.json` files for each block.

## Acceptance Criteria

### Verification
- [ ] Running `bun run content/pipeline/qa-agent-drain-queue.ts content/quantum-observable-universe` outputs exactly `0 batches, 0 blocks, 0 gaps`.
- [ ] The `git status` confirms that the corresponding `.qa.json` files were actually modified.
- [ ] No files are skipped or hallucinated as completed.

## 2026-06-15T13:10:27Z

The server restarted and your API quota has been completely reset. Please resume your task of evaluating the QA backlog.

## 2026-06-16T01:36:17Z

Mechanically audit and rewrite the QOU expository literature and computational codebase (Python/Rust) to purge the interpretation of `q` as a rigid global constant. Formally realign the framework around the "3 calibration points" ($m_e, m_\mu, Q_\beta$), asserting that $q$ is mathematically synonymous with the local mass ratio, and that the calibration inputs are locally evolving fields.

Working directory: /home/litlfred/space_cats/qou
Integrity mode: demo

## Requirements

### R1. Execute the QA Sidecar Audit
The team must process the `todos/qa-q-CAL-1-2-3-audit.json` manifest. All markdown files in the specified scope (including `introduction/`) must be mechanically rewritten to satisfy criteria `C1_Q_IDENTITY`, `C2_3_CALIBRATION_POINTS`, and `C3_CAL2_VACUUM_LOCK`.

### R2. Codebase Refactoring (Python/Rust)
The team must recursively scan the computational codebase (e.g., `computations/`, `simulations/`) to identify variables, comments, and print statements treating `q` as an abstract constant. These must be refactored to reflect `q` as the fundamental mass-ratio parameter.

### R3. Execution Validation
The team must execute the modified Python/Rust scripts to verify that the refactoring did not break existing computational logic.

## Acceptance Criteria

### Content Integrity (Agent-as-Judge Verification)
- [ ] An independent reviewing agent confirms that no `.md` file in the audit scope contains phrases describing $q$ as an "unobservable background parameter", "invisible ether", or "rigid global constant".
- [ ] An independent reviewing agent confirms that the introduction explicitly frames the framework using the "3 calibration points" and declares $q$ is the mass ratio.
- [ ] An independent reviewing agent confirms that no Python or Rust scripts in the active codebase define variables like `q_constant` without explicit mass-ratio context.

### Code Execution
- [ ] The team successfully executes a representative sample of the modified Python/Rust scripts without throwing runtime errors or assertion failures.

