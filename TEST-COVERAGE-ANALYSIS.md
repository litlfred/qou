# Test Coverage Analysis

## Current Test Coverage

| Area | File | Framework |
|------|------|-----------|
| LaTeX↔Lean coverage | `scripts/tests/latex-lean-coverage.test.ts` | Bun |
| Lean project structure | `scripts/tests/lean-projects.test.ts` | Bun |
| Infrastructure/config | `scripts/tests/infrastructure.test.ts` | Bun |
| SnapPea WASM smoke | `snappea-wasm/test/unit/smoke.test.js` | Vitest |
| SnapPea WASM census | `snappea-wasm/test/unit/census.test.js` | Vitest |

## Coverage Gaps (by priority)

### 1. Content Schema — HIGH priority, ~330 lines untested

**Files:** `content/schema/builders.ts`, `content/schema/constraints.ts`

Zero tests for 11 block builders, 6 structure builders, label prefix validation,
and 4 constraint rules (md-exists, lean-file-exists, uses-resolve, provable-lean-warning).

**Proposed tests (`content/schema/builders.test.ts`):**
- `definition()` with valid input returns `{kind: "definition", ...}`
- `definition()` without required `lean` field throws ZodError
- `theorem()` with wrong label prefix (e.g. `"def:"` instead of `"thm:"`) throws
- `prose()` with no args returns `{kind: "prose"}`
- All builders reject invalid properties

**Proposed tests (`content/schema/constraints.test.ts`):**
- `CONSTRAINT_RULES` md-exists: passes when `.md` exists, fails when missing
- `CONSTRAINT_RULES` lean-file-exists: passes with `lean.file` or `.lean` file
- `CONSTRAINT_RULES` uses-resolve: passes when all labels exist, reports missing
- `CONSTRAINT_RULES` provable-lean-warning: warns for theorem without lean
- Label prefix validation for each kind (`def:`, `thm:`, `lem:`, `prop:`, etc.)

### 2. Render Pipeline — HIGH priority, ~380 lines untested

**File:** `content/pipeline/render-latex.ts`

`markdownToLatex` has regex-based bold/italic/cross-ref conversion, display math,
fenced code blocks, and list detection. `renderBlock` wraps content in LaTeX
environments. `validateLatexAst` parses rendered output. All untested.

**Proposed tests (`content/pipeline/render-latex.test.ts`):**
- `markdownToLatex`: `**bold**` → `\textbf{bold}`
- `markdownToLatex`: `*italic*` → `\emph{italic}`
- `markdownToLatex`: `$$...$$` → `\[...\]`
- `markdownToLatex`: `` ```tex `` block → raw LaTeX passthrough
- `markdownToLatex`: `` ```python `` block → `\begin{verbatim}`
- `markdownToLatex`: numbered list → `\begin{enumerate}`
- `markdownToLatex`: `[text](#label)` → `\hyperref[label]{text}`
- `renderBlock`: prose → plain LaTeX (no environment wrapper)
- `renderBlock`: theorem with label, lean, uses → correct environment
- `renderBlock`: theorem with `hasProof` + `---` separator → `\begin{proof}`
- `renderBlock`: equation with label → `\begin{equation}\label{...}`
- `renderBlock`: equation without label → `\[...\]`
- `validateLatexAst`: valid LaTeX → `{valid: true}`
- `validateLatexAst`: malformed LaTeX → errors populated

### 3. Validation Pipeline — HIGH priority, ~170 lines untested

**File:** `content/pipeline/validate.ts`

`validateObjects` orchestrates 3-phase validation (Zod → constraints → AST).
This is the critical integrity gate for the content system.

**Proposed tests (`content/pipeline/validate.test.ts`):**
- `validateObjects` on empty dir → warning, `valid: true`
- `validateObjects` with invalid block schema → error
- `validateObjects` with missing `.md` companion → error from md-exists rule
- `validateObjects` with unresolved `uses[]` → error from uses-resolve rule
- `validateObjects` renders blocks and validates AST

### 4. Build + Export Pipeline — MEDIUM priority, ~230 lines untested

**Files:** `content/pipeline/build.ts`, `content/pipeline/export-json.ts`

End-to-end document build and JSON export for SPA viewer.

**Proposed tests:**
- End-to-end build from fixture content objects
- JSON export structure validation (required fields, hash, timestamps)
- Asset copying and URL rewriting in export

### 5. Python CI Scripts — MEDIUM priority, ~2000+ lines untested

**Files:** 12 scripts in `.github/scripts/`

Key untested logic:
- `extract_proof_objects.py` — LaTeX regex parsing for theorem-like environments
- `ontologist.py` — term extraction and ambiguity detection
- `generate_dependency_graph.py` — Graphviz DOT generation
- `qou_lib/manifest.py` — JSON merging (field preservation across updates)

**Proposed:** Add a `pytest` suite in `.github/scripts/tests/`.

### 6. MCP Server Tools — LOW priority, ~500+ lines untested

**Files:** `scripts/mcp-server/` (6 modules)

**Proposed:** Unit tests for path resolution and preference storage/retrieval.

## Summary Table

| Area | Untested LOC | Priority | Effort |
|------|-------------|----------|--------|
| Content schema (builders + constraints) | ~330 | HIGH | Low (pure functions) |
| Render pipeline (markdown→LaTeX) | ~380 | HIGH | Low (pure functions) |
| Validation pipeline | ~170 | HIGH | Medium (needs fixtures) |
| Build + export pipeline | ~230 | MEDIUM | Medium (async, I/O) |
| Python CI scripts | ~2000+ | MEDIUM | Medium (pytest setup) |
| MCP server tools | ~500+ | LOW | High (MCP mocking) |

## Recommendation

Start with the **content schema** and **render pipeline** tests — they are pure
functions with clear inputs/outputs, critical to content integrity, and the
easiest to write. The validation pipeline tests come next, requiring a small
fixture directory of mock content objects.
