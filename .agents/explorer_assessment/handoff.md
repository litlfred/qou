# Teamwork Handoff Report

## 1. Observation

- **Queue File Location and Content**: Directly observed `todos/qa-agent-drain-queue.json` containing top-level properties:
  - Line 2: `"generated_at": "2026-06-15"`
  - Line 3: `"total_gaps": 3452`
  - Line 4: `"total_blocks": 683`
  - Line 5: `"total_batches": 43`
  - Batches are groups of blocks grouped by chapter, each containing `batch_id`, `chapter`, `status`, and `blocks`.

- **Pipeline Scripts**:
  - Located `content/pipeline/qa-agent-drain-queue.ts` (and duplicate at `folio-assistant/src/qa-agent-drain-queue.ts`) defining the queue generator.
  - Located `folio-assistant/src/qa-agent-write.ts` (referred to as `content/pipeline/qa-agent-write.ts` in code comments/requests) defining the QA sidecar writer.
  - In `folio-assistant/src/qa-agent-write.ts`, observed parameters:
    - Lines 60-62: `blockArg = arg("block"); criterion = arg("criterion"); result = arg("result")`
    - Lines 73-77: `--severity` check (`critical|major|minor`)
    - Lines 85-128: `--score`, `--score-max`, `--score-rubric` checks and structures
    - Lines 133-140: Rubric band consistency rule:
      ```typescript
      const frac = score.value / score.max;
      const band = frac >= 0.66 ? "pass" : frac >= 0.33 ? "warn" : "fail";
      if (result !== band) {
        fail(
          `--result "${result}" contradicts --score ${score.value}/${score.max} ` +
            `(band "${band}"); use --result ${band} or adjust the score`,
        );
      }
      ```
    - Lines 216-224: Idempotency filter replacing prior entries with the same reviewer ID:
      ```typescript
      const kept = existing.filter(
        (e) => !(e.reviewer.kind === "agent" && e.reviewer.id === skill),
      );
      report.criteria[criterion] = [...kept, entry];
      ```

- **Example Content Block**:
  - Located `recursive-atom-knot-atlas.ts` (manifest), `recursive-atom-knot-atlas.md` (narrative), `recursive-atom-knot-atlas.lean` (Lean formalization), and `recursive-atom-knot-atlas.qa.json` (QA report).
  - In `recursive-atom-knot-atlas.lean`, observed:
    - Line 58: `inductive Methodology` defining categories of particle-knot derivation.
    - Lines 96-121: `atomKnotAtlas` array containing the seed values for proton and neutron.
    - Lines 157-163: `theorem atlas_witness_derived` proved by `decide`.
  - In `recursive-atom-knot-atlas.qa.json`, observed:
    - Lines 755-790: The entry for `proof-narrative-lean-equiv` currently has `"result": "fail"`, referencing that the Lean signature is a placeholder True stub.

- **Heuristics & Rules adopted**:
  - Observed Adoption Design in `docs/audits/2026-06-07-google-paper-qa-rubrics-and-tooling.md`:
    - Lines 25-29: Optional `score` structure mapped to pass/warn/fail bands (`value >= 0.66` $\implies$ pass, `0.33 <= value < 0.66` $\implies$ warn, `value < 0.33` $\implies$ fail).
    - Line 22: `proof-rater-goal-plausibility` scores remaining sorries/gaps based on criticality: `routine` $\implies$ ~0.9 (pass), `core` $\implies$ ~0.3 (warn), `restates-target` $\implies$ 0.0 (fail).
  - Observed `proof-statement-integrity` logic in registry:
    - Lines 720-723: Checks for statement-weakening and unexpected axioms (e.g. `sorryAx`) on declarations claimed proved.

---

## 2. Logic Chain

1. **Queue Structure & Generation**:
   - The queue generator (`qa-agent-drain-queue.ts`) reads block properties from their `.ts` manifests and compiles a list of blocks needing agent audits.
   - A block "needs" a criterion if the criterion is agent-only (`automated === false`), applies to the block's `kind`, and lacks a fresh agent or human entry whose `field_hash.md` matches the current `.md` file's hash.
   - The output queue file organizes blocks into batches of at most 25 blocks grouped by chapter, enabling parallel subagent processing.

2. **Writing Sidecar Reports**:
   - When a subagent evaluates a block's criterion, it calls `qa-agent-write.ts` with `--block`, `--criterion`, `--result`, and optional score details.
   - The script enforces Zod schema constraints, resolves missing local siblings to canonical library files via `resolveCanonicalLean`, and ensures that score ratios are consistent with the assigned `pass|warn|fail` band.
   - The script is idempotent per agent identity: it filters out and overwrites any existing entry written by the same `skill` ID, preserving other script or human verdicts.

3. **Proof Stub Identification & Rating Heuristics**:
   - Proof stubs are Lean declarations that contain `sorry` or compiles with `sorryAx` (or consist of trivial constructs like `True := by trivial` shadowing real claims).
   - Under `proof-rater-goal-plausibility`, we score:
     - **Sorry-free (verified) proofs**: Score `1.0` (band `pass`).
     - **Routine gaps** (standard algebra, library lookup): Score `~0.9` (band `pass`).
     - **Core gaps / proof stubs** (requires key ideas, contains sorry/sorryAx, but has proper math structure/hypotheses): Score `0.34` (band `warn`).
     - **Trivial-skeleton / restates-target / shadow stubs** (empty proof, sorry immediately following target signature): Score `0.0` (band `fail`).
   - Under `proof-statement-integrity`, any proof claimed proved that compiles with `sorryAx` or unexpected axioms is marked as `fail`.
   - Under `proof-no-bare-sorries`, any `sorry` that lacks a `-- Ref: [key]` citation lookback is marked as `fail`.

---

## 3. Caveats

- **Script Paths**: The write script is located at `folio-assistant/src/qa-agent-write.ts`, whereas the codebase comments suggest `content/pipeline/qa-agent-write.ts`. If running from content pipeline folder, subagents must resolve it correctly.
- **Mathlib compilation**: Building and compiling Lean files in the workspace environment requires Mathlib. The environment might not have prebuilt Mathlib oleans, meaning executing full compiler checks locally could trigger a long Mathlib recompilation unless lightweight warm sets are built using `lake build`.

---

## 4. Conclusion

The investigation successfully mapped:
1. The queue JSON structure, blocks list, and requirements.
2. The parameters, validations, and update mechanisms of the drain queue and write scripts.
3. The relationship between manifests, markdown, and Lean files (using `recursive-atom-knot-atlas` as an exemplar).
4. The exact rules/heuristics for pass/warn/fail conditions on proof stubs and rater criteria.

All findings have been synthesized and documented in the target location `/home/litlfred/space_cats/qou/.agents/explorer_assessment/analysis.md`.

---

## 5. Verification Method

To independently verify the pipeline scripts, mappings, and schemas:
1. Validate the repository content schema using the project validation script:
   ```bash
   bun run validate
   ```
2. Verify that the agent queue is generated correctly:
   ```bash
   bun run content/pipeline/qa-agent-drain-queue.ts
   ```
   Check that `todos/qa-agent-drain-queue.json` is successfully outputted.
3. Inspect `analysis.md` for completeness.
