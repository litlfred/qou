# Handoff Report: mass-theory Directory Placeholders, TODOs, and Sorries

This report details the findings and remediation plans for placeholders, `TODO`s, `FIXME`s, and `sorry`s in the `content/quantum-observable-universe/mass-theory/` directory.

---

## 1. Observation

- **TODO / FIXME Scan:**
  - Search command: `grep_search` case-insensitively.
  - 0 occurrences of `FIXME` found.
  - `TODO` found in 4 files (`descent-rate-probe-sim.ts:13`, `multi-level-jet-sum-sim.ts:12`, `q-beta-radius-of-convergence-gate.md:30,31,96,97,100`, `reeb-bundle.lean:35`).
  - Example from `reeb-bundle.lean:35`:
    ```lean
    -- ExceptionalDivisor structure (Ch 6 §2); tracked as a TodoItem.
    ```
- **Sorry Scan:**
  - Search command: Alphabetical `grep_search` for `sorry` in `.lean` files.
  - Active `sorry`s found in 19 files. Every single `sorry` contains a bibliographic citation (e.g. `-- Ref: [manuscript]` or `-- Ref: [kashaev1997]`).
  - One `sorry` (`delta-q-decoration.lean:34`) is inside a block comment.
- **Vacuity Audit Cross-Reference:**
  - Source: `docs/audits/2026-06-17-lean-vacuity-axiom-audit.json`
  - Redundant shadow stubs: 22 files are flagged with `exempt_reason: "shadow-stub (real formalisation: content/quantum-observable-universe/lean/QOU/...)"` under category `proof-no-trivial-true`.
  - Non-exempt `proof-no-decide-masking` (`native_decide`):
    - `bring-residue-resolvent.lean` (Lines 198, 204, 210, 217)
    - `reidemeister-mass-invariance.lean` (Lines 113, 116)
  - Non-exempt `proof-no-false-premise` (`discharged-impossible-hyp`):
    - `magic-A-binding-formula.lean` (Lines 170, 179)
    - `q-pochhammer-partial-product.lean` (Line 67)
  - Non-exempt `proof-no-trivial-true` (`placeholder-true`):
    - `symbolic-character-table.lean:29` (which is actually a redundant shadow stub).
- **Git Branch Diff:**
  - Commits on `claude/placeholder-beans-2026-06-21` show changes to sidecar `.qa.json` files and the audit json. No changes to source `.lean` or `.md` files in `mass-theory/` are present on this branch yet.

---

## 2. Logic Chain

- **Step 1:** The `TODO`s are solely metadata tags or documentation notes. They do not represent functional placeholders or unfinished code that needs to be resolved.
- **Step 2:** The active `sorry`s are all cited with references (complying with AGENTS.md §1) and represent conjectural axioms (e.g. class instances for §3b-cond) or cited steps. Therefore, they should be preserved as honest citations and do not need to be resolved by writing new proofs.
- **Step 3:** The 22 exempt shadow stubs (and the 1 non-exempt one, `symbolic-character-table.lean`) duplicate declarations that are fully formalized in the library (`content/quantum-observable-universe/lean/QOU/...`). Under AGENTS.md §0a, keeping these stubs is a violation. Thus, the logical remediation is to delete all 23 stub files.
- **Step 4:** The `native_decide` calls evaluate simple, decidable equalities/inequalities on rational numbers or integers. They can be resolved without the `native_decide` axiom by using `rfl` or `decide`, satisfying `proof-no-decide-masking`.
- **Step 5:** The `proof-no-false-premise` flags are scanner false positives on standard induction base cases or rcases branch eliminations; no code changes are required for them.

---

## 3. Caveats

- **Compilation / Lake Build:** As a read-only explorer agent, we have not run `lake build` to verify the package compiles. The proposed remediation assumes the library files (`content/quantum-observable-universe/lean/QOU/...`) build successfully.

---

## 4. Conclusion

The remediation strategy is clear and structured:
1. **Delete 23 redundant shadow stubs** in `content/quantum-observable-universe/mass-theory/` (leaving the `.md` and `.ts` files intact; their `lean.ref` definitions correctly resolve to the library namespace).
2. **Replace `native_decide` with `rfl` or `decide`** in `bring-residue-resolvent.lean` and `reidemeister-mass-invariance.lean`.
3. **Preserve the cited `sorry`s and documentation `TODO`s** as they are compliant.

---

## 5. Verification Method

- **Inspection:** Inspect the `content/quantum-observable-universe/mass-theory/` files to verify findings.
- **Run Audit Script:** After deleting the shadow stubs and fixing `native_decide`, run:
  ```bash
  bun run content/pipeline/qa-agent-drain-queue.ts
  ```
  to verify that the sidecars are clean and the defects are resolved.
- **Lake Build:** Verify the `QOU` library compiles correctly:
  ```bash
  lake build QOU
  ```
