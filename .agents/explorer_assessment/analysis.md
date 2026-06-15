# QA Agent Backlog and Queue Investigation Report

## 1. Structure of `todos/qa-agent-drain-queue.json`

The file `todos/qa-agent-drain-queue.json` represents a trackable work queue of **agent-only** QA criteria lacking fresh agent/human entries. 

### Structure
The JSON schema contains the following top-level metadata:
- `generated_at`: The date the queue was generated (e.g. `"2026-06-15"`).
- `total_gaps`: Total number of pending criteria across all blocks (sum of all needs).
- `total_blocks`: Total number of unique content blocks containing at least one gap.
- `total_batches`: Number of batches created to divide the workload (grouped by chapter, default max 25 blocks per batch).
- `batches`: An array of Batch objects.

Each **Batch** object consists of:
- `batch_id`: A 1-indexed sequential integer identifying the batch.
- `chapter`: The chapter folder slug (e.g. `"appendix-knot-periodic-table"`).
- `status`: Set to `"pending"` initially.
- `blocks`: An array of block-specific rows.

Each **Row** (block entry) contains:
- `block`: The base path to the content block relative to the repository root, without extension (e.g., `"content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas"`).
- `chapter`: The chapter slug.
- `kind`: The block's kind manifest property (e.g., `"proposition"`, `"theorem"`, `"lemma"`, `"remark"`).
- `need`: An array of criterion ID strings (e.g., `["proof-no-self-assuming-projection", "proof-no-trivial-true"]`) representing the specific audits currently lacking a fresh review entry.

---

## 2. Pipeline Scripts: Drain Queue and Write Entry

There are two primary pipeline scripts that manage the agent-drain queue workflow:

### A. Queue Generator (`content/pipeline/qa-agent-drain-queue.ts`)
*Note: A duplicate file also exists at `folio-assistant/src/qa-agent-drain-queue.ts`.*
- **Invocation**:
  ```bash
  bun run content/pipeline/qa-agent-drain-queue.ts [root-dir] [--batch-size <size>] [--out <out-path>]
  ```
  - `root-dir`: Default is `content/quantum-observable-universe`.
  - `--batch-size`: Number of blocks per batch (defaults to 25).
  - `--out`: Target output file path (defaults to `todos/qa-agent-drain-queue.json`).
- **Logic & Validations**:
  1. Changes working directory to the repo root (`process.chdir`) to ensure correct relative path processing.
  2. Iterates over all content blocks using `walkBlocks(root)`.
  3. Filters for agent-only criteria (where `automated === false` in `QA_CRITERIA_REGISTRY`).
  4. Skips criteria that do not apply to the block's `kind` (checks `c.applies_to`).
  5. Determines if a block has a **fresh** review entry:
     - Reads the block's `.qa.json` file.
     - A criterion entry is fresh if it was reviewed by an `agent` or `human` and the recorded `field_hash.md` matches the current SHA-256 hash of the block's `.md` file.
  6. Collects all blocks needing at least one agent-only criterion, groups them by chapter, splits them into batches, and outputs the JSON queue file.

### B. QA-Entry Writer (`folio-assistant/src/qa-agent-write.ts`)
*Note: The script is located in `folio-assistant/src/qa-agent-write.ts`, although code comments refer to it at `content/pipeline/qa-agent-write.ts`.*
- **Invocation**:
  ```bash
  bun run folio-assistant/src/qa-agent-write.ts \
    --block <base-path-without-extension> \
    --criterion <criterion-id> \
    --result pass|fail|warn|n/a \
    [--severity critical|major|minor] \
    [--score <score>] [--score-max <max>] [--score-rubric '<json>'] \
    [--evidence "<verbatim quote>"] \
    [--notes "<notes>"] \
    [--model <model>] [--skill <skill>]
  ```
- **Script Parameters**:
  - `--block`: (Required) Path to block without extension (e.g. `content/quantum-observable-universe/appendix-knot-periodic-table/recursive-atom-knot-atlas`).
  - `--criterion`: (Required) The ID of the criterion being adjudicated.
  - `--result`: (Required) One of `pass`, `fail`, `warn`, or `n/a`.
  - `--severity`: (Optional) One of `critical`, `major`, `minor`.
  - `--score`: (Optional) The numeric score.
  - `--score-max`: (Optional) Maximum score (defaults to 1). Required if score is present.
  - `--score-rubric`: (Optional) A JSON string mapping keys to numeric scores (e.g., `'{"clarity":0.8}'`).
  - `--evidence`: (Optional) A string containing evidence (such as line number and quote).
  - `--notes`: (Optional) Text comments from the evaluator.
  - `--model`: (Optional) Defaults to `"claude-opus-4-8"`.
  - `--skill`: (Optional) Defaults to `"local/qa-agent-drain"`.
- **Validations & Constraints**:
  1. Validates values for `--result` and `--severity`.
  2. Ensures that `--score-max` and `--score-rubric` are only provided when `--score` is present.
  3. Ensures `--score` is in `[0, score-max]` and `--score-rubric` is a valid JSON object of numbers.
  4. **Rubric Band Consistency**: If a score is present, computes `frac = score.value / score.max`. It checks that `--result` matches the fraction:
     - `frac >= 0.66` $\implies$ `result` must be `"pass"`
     - `0.33 <= frac < 0.66` $\implies$ `result` must be `"warn"`
     - `frac < 0.33` $\implies$ `result` must be `"fail"`
     If there is a mismatch, the script exits with an error.
  5. Resolves paths and verifies that the block's `.ts` manifest exists. If a sibling `.lean` file is absent, it parses the `lean.ref` from the `.ts` manifest and resolves the canonical `.lean` library file using `resolveCanonicalLean`.
- **File Update Logic**:
  1. Computes the current hashes for the block's `ts`, `md`, and `lean` files.
  2. Retrieves the current Git HEAD SHA and the current ISO timestamp.
  3. Loads the existing sidecar file `${block}.qa.json` (or creates a new one if it does not exist).
  4. Prepares a `QaCriterionEntry` object and inserts it into the `criteria[criterion]` array.
  5. **Idempotency**: Replaces any existing entry under the same criterion that has the same reviewer ID (`reviewer.id === skill`, which defaults to `"local/qa-agent-drain"`), while preserving entries from scripts, humans, or other agents.
  6. Writes the updated object back to disk in the sidecar.

---

## 3. Relationships & Example Block Structure

### Relationship Triads
Each content block consists of several tightly coupled files:
1. **Manifest (`.ts`)**: Defines metadata (Zod validated). Contains `label` (defining the LaTeX anchor), `title`, `lean` configuration (with `ref` containing package-qualified Lean declaration paths), `uses` dependencies, `cites` references, and optional `computation` pointers (script/witness/status) and `authorNotes`.
2. **Narrative (`.md`)**: The LaTeX-markdown narrative statement and proof.
3. **Formalization (`.lean`)**: The formal proof. A content block can have:
   - A sibling `.lean` file located in the same directory (used for direct local proofs).
   - An *absent* sibling, in which case the compiler locates the canonical declaration via the `lean.ref` inside the package Lake tree (e.g. resolving `qou:QOU.BraidsAndKnots.recursive_atom_knot_atlas` to `content/quantum-observable-universe/lean/QOU/BraidsAndKnots/recursive_atom_knot_atlas.lean`).
4. **QA Report (`.qa.json`)**: A sidecar tracking audit results. Top-level `source_hashes` must match the actual files' hashes to avoid staleness.

### Example Block: `recursive-atom-knot-atlas`
- **Location**: `content/quantum-observable-universe/appendix-knot-periodic-table/`
- **Manifest (`recursive-atom-knot-atlas.ts`)**:
  - Label: `"prop:recursive-atom-knot-atlas"`
  - Lean ref: `"qou:QOU.BraidsAndKnots.recursive_atom_knot_atlas"`
  - Computation: mpmath script `q_pinning_50_digit.py` producing `q-pinning-50-digit.witness.json`.
- **Narrative (`recursive-atom-knot-atlas.md`)**:
  - Describes the methodology classification tags (`principled-derivation`, `manual-historical-volume-match`, `magic-A-formula`, `recursive-on-⁴He`, and the provisional `deprecated-volume-match`).
  - Contains tables indexing particle-knot predictions for the Electron ($3_1$, trefoil), Proton/Neutron ($\mathcal{B}_3$, Borromean), Deuterium ($6_2$), Tritium ($8_{11}$), Helium-3 ($L_{6a4}$), and Helium-4 ($A \cdot 8G$).
  - Contains the exact symbolic $|\mathrm{tr}_M(q_0)|$ values.
- **Lean File (`recursive-atom-knot-atlas.lean`)**:
  - Defines the `Methodology` inductive type and the `AtlasEntry` structure.
  - Seeds the `atomKnotAtlas` with concrete representations of the proton and neutron principled derivations.
  - Proves `theorem atlas_witness_derived` and `theorem principled_path_for_atom_knot` by `decide` / `rfl`.
  - Notes the provisional status of `li7_provisional_volume_match`.
- **QA Sidecar (`recursive-atom-knot-atlas.qa.json`)**:
  - Contains historical and script-based entries for `voice-status-leak`, `voice-emoji-content`, etc.
  - Contains a `fail` entry under `proof-narrative-lean-equiv` because the local Lean signature is partially a placeholder stub relative to the full `.md` claim.

---

## 4. Evaluation Rules & Proof Stub Heuristics

### General Assessment Verdicts
- **PASS**: The content strictly satisfies the criteria. For scored rubrics, score $\ge 0.66$.
- **WARN**: The content has minor issues, notational mismatches, or acceptable caveats. For scored rubrics, $0.33 \le \text{score} < 0.66$.
- **FAIL**: The content violates constraints, introduces errors, or is structurally/mathematically deficient. For scored rubrics, score $< 0.33$.

### Specific Rules for Scored & Proof Integrity Criteria

1. **`proof-rater-goal-plausibility`** (Plausibility of closing remaining proof gaps):
   - **Score 1.0 (Pass)**: The proof compiles without any `sorry` or `sorryAx` (fully verified).
   - **Score ~0.9 (Pass)**: Proof contains `sorry` but the gap is classified as `routine` (standard algebraic reduction, simple identities, basic library searches).
   - **Score ~0.34 (Warn)**: Proof is a **proof stub** where a non-trivial theorem is stubbed out with `sorry` or `sorryAx`, but contains structure, definitions, or intermediate claims representing `core` gaps that are plausible to resolve but require key math ideas.
   - **Score 0.0 (Fail)**: The proof is a **trivial/vacuous skeleton** that restates the target (the gap IS the goal, e.g., the theorem is immediately followed by `:= sorry` or is a vacuous placeholder like `True := by trivial`).

2. **`proof-statement-integrity`** (SafeVerify):
   - **Pass**: The declaration matches the prior commit signature and compiling it yields **no** `sorryAx` or unexpected axioms.
   - **Fail**: The compiler output reveals `sorryAx` (indicating it depends on a `sorry` under the hood) or introduces unapproved axioms on a declaration that is claimed proved.

3. **`proof-no-bare-sorries`**:
   - **Pass**: Every single `sorry` in the Lean file is accompanied by a `-- Ref: [key] <url>` bibliographic citation within the same line, inside the enclosing declaration scope, or in the preceding 5 lines.
   - **Fail**: Any `sorry` token lacks a referenced citation (classified as an orphan sorry).

4. **`proof-narrative-lean-equiv`**:
   - **Pass**: Narrative statement quantifiers, hypotheses, and conclusions structurally align with the Lean signature.
   - **Warn**: Slight notational differences (different variable names, binder implicitness) that are easily reconciled.
   - **Fail**: Theorem-changing divergence (quantifier mismatches, missing assumptions on either side) or the Lean file uses a `sorry` stub or `True` placeholder while the narrative claims a real, completed proof.

5. **`proof-no-self-assuming-projection`**:
   - **Pass**: The proof derives the claim by composing fields or applying lemmas.
   - **Fail**: The proof is a verbatim projection of a structure field whose type is the declaration's own conclusion (tautological projection `P ⊢ P`, e.g., `:= d.claim`).
