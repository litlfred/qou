# Plan: Lean Formalization Backlog Resolution

## Objective
Audit, clean up, and resolve the Lean formalization backlog in `content/quantum-observable-universe/`.
1. Ensure all `.lean` files compile successfully under Lean 4/Mathlib (R1).
2. Audit and correct vacuous/trivial proof anti-patterns (R2).
3. Discharge non-conjectural sorries from the queue and annotate remaining sorries (R3).
4. Coordinated execution with <=8 concurrent active subagents in specialized subteams (R4).

## Architecture & Subteams
To prevent token burning and build conflicts:
- **Compilation Team (comp_team)**: Focuses on compiling all `.lean` files and resolving syntax/import/structure errors. (Up to 2 agents)
- **Vacuity Audit Team (vacuity_team)**: Audits proofs for vacuous/trivial patterns and replaces them with genuine proofs. (Up to 2 agents)
- **Sorry Discharge Team (sorry_team)**: Resolves outstanding items in `todos/lean-discharge-queue.json` and adds proper bibliographic references to any legitimate conjectural sorries. (Up to 3 agents)

## Verification
- `lake build` / `./scripts/lean-build-all.sh` succeeds with 0 errors across the package.
- All `.lean` files are reachable via imports from the root module.
- `bun run content/pipeline/lean-vacuity-axiom-audit.ts` reports 0 high-confidence vacuous proof findings.
- Sibling stubs are removed.
- All remaining `sorry` occurrences carry valid bibliographic citations `-- Ref: [key]`.
- Open items in `todos/lean-discharge-queue.json` (such as `lean-catalan-G-numerical-bound`) are resolved.
- Forensic Auditor (teamwork_preview_auditor) verifies work is clean and free of cheating/facades.

## Phased Execution Plan

### Phase 1: Environment Diagnostics & Status Audit
- [ ] Task 1.1: Run initial `lake build` or diagnostic check to locate compilation errors.
- [ ] Task 1.2: Run `bun run content/pipeline/lean-vacuity-axiom-audit.ts` to locate vacuous proofs.
- [ ] Task 1.3: Survey `todos/lean-discharge-queue.json` and verify which items are open and their target files.

### Phase 2: Compilation and Import Clean-Up (R1)
- [ ] Task 2.1: Fix compilation issues file-by-file in `content/quantum-observable-universe/`.
- [ ] Task 2.2: Ensure all files are reachable via imports from the root module.

### Phase 3: Proof Vacuity and Trivial-True Correction (R2)
- [ ] Task 3.1: Resolve high-confidence vacuous proof findings identified by audit script.
- [ ] Task 3.2: Delete sibling-resolution stubs shadowing real proofs, formalize placeholders or demote to conjectures.

### Phase 4: Sorry Discharge (R3)
- [ ] Task 4.1: Resolve and close the open items in `todos/lean-discharge-queue.json` (e.g. `lean-catalan-G-numerical-bound`).
- [ ] Task 4.2: Audit all remaining `sorry` tokens in the workspace and ensure they have a `-- Ref: [key]` annotation.

### Phase 5: Verification & Integrity Audit (R4 verification)
- [ ] Task 5.1: Run final full compile checks.
- [ ] Task 5.2: Run final vacuity checks.
- [ ] Task 5.3: Run Forensic Auditor to certify integrity.
