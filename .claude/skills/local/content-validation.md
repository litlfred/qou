---
name: content-validation
roles: [reader, collaborator, owner]
---

# Content Validation Skill

## Role

Validate content objects (`.ts` manifests + `.md` content + `.lean` files)
for structural integrity, constraint compliance, and LaTeX AST correctness.

## Content-object infrastructure

| Path | Purpose |
|------|---------|
| `content/schema/types.ts` | TypeScript types for all block kinds |
| `content/schema/constraints.ts` | Zod schemas + constraint rules |
| `content/schema/builders.ts` | Builder functions (`definition()`, `theorem()`, etc.) |
| `content/pipeline/validate.ts` | Validation pipeline (schema + constraints + AST) |
| `content/pipeline/render-latex.ts` | Block → LaTeX rendering + AST validation |
| `content/pipeline/build.ts` | Full document build (all chapters) |

## Directory convention

```
content/
  <paper-name>/
    <paper-name>.ts                    — Paper manifest (ChapterRef[])
    <chapter-dir>/
      <chapter-dir>.ts                 — Chapter manifest (sections, block refs)
      <block-name>.ts                  — Block manifest (kind, label, lean, constraints)
      <block-name>.md                  — Narrative content (markdown + TeX snippets)
      <block-name>.lean                — Lean formalization (when required by kind)
```

## Validation levels

### Level 1: Zod schema validation
- Block kind matches discriminated union
- Label prefix matches kind (def: for definitions, thm: for theorems, etc.)
- Required fields present (e.g. definitions MUST have `lean`)
- Status enum values are valid

### Level 2: Constraint rules
- **md-exists**: Every block has a sibling `.md` file
- **lean-file-exists**: Definitions have a sibling `.lean` or `lean.file` reference
- **no-orphan-lean**: Every `.lean` file MUST have a `.ts` manifest sibling — `.lean` files are NEVER standalone, always part of a content triple (`.ts` + `.md` + `.lean`)
- **uses-resolve**: All labels in `uses[]` exist in the document
  (or are qualified cross-paper refs in `"paper-dir:label"` format,
  which are skipped — resolved at folio level)
- **provable-lean-warning**: Theorems/lemmas without Lean get warnings

### Level 5: Witnessed-value directive validation

Five rules check `:val[name]` directive usage in every block kind
(definitions, propositions, theorems, lemmas, conjectures, proofs,
examples, remarks, prose, equations):

| Rule                       | Level | What it checks |
|---------------------------|-------|----------------|
| `val-registered`          | error | name appears in `WITNESSED_VALUES` |
| `val-resolves`            | error | witness file exists, dotted path resolves |
| `val-precision-bounded`   | error | requested precision ≤ source precision |
| `val-units-consistent`    | warn  | `units=plain` only when entry has units |
| `val-pending`             | warn  | `needsReview: true` entry was cited |
| `val-block-computation`   | warn  | block cites `:val[…]` but `computation:` is absent or refers to a different witness file |

When you spot a hard-coded substrate-derived literal in **any** block
kind (a numeric bound in a proposition, a constant in a conjecture, a
calibration value in a definition, a quoted intermediate in a proof,
etc.), flag it as drift risk and migrate it to `:val[name]`.  The
`content/pipeline/codemod-val.ts` codemod handles bulk migration.
See [`witnessed-values.md`](./witnessed-values.md) for full details.

### Level 3: LaTeX AST validation
- Rendered LaTeX parses through unified-latex without errors
- Environment balance (\begin matches \end)
- No malformed macro syntax
- No unbalanced braces

### Level 4: TeX snippet validation (in .md files)

The `.md` files are parsed using **remark + remark-gfm + remark-math**
(formal markdown grammar with GFM table support and math extension).
GFM pipe tables are converted to `\begin{tabular}` with `booktabs`
rules; inline code (backticks) renders as `\texttt{}` with LaTeX
escaping. Each extracted TeX snippet is validated via **unified-latex**
AST parsing. This catches:

- Non-math environments inside math mode (e.g. `\begin{itemize}` inside `$$`)
- Unbalanced braces or environments in inline/display math
- Malformed TeX in fenced ` ```tex ` blocks

The markdown AST node types used:

| Markdown syntax | remark AST node | Validated as |
|-----------------|-----------------|-------------|
| `$...$` | `inlineMath` | Math-mode TeX |
| `$$...$$` | `math` (display) | Display-mode TeX |
| ` ```tex ``` ` | `code` (lang=tex) | Raw LaTeX |

## Running validation

> **Currency (miga, 2026-06-23).** The content pipeline + schemas now live in the
> separate `litlfred/folio-assistant` repo. Run
> [`scripts/setup-folio-assistant.sh`](../../../scripts/setup-folio-assistant.sh)
> **once** (clones the platform as a sibling + symlinks `folio-assistant/`), then
> validate via the standalone entry `bun run scripts/run-validate.ts content/<paper>`.
> The `bun run <name>` package.json shortcuts below (`validate`, `validate-tex`,
> `build-glossary`, `migrate-lean-refs`) were dropped in the migration and the
> `pipeline/*.ts` paths moved under `folio-assistant/content/pipeline/`; only
> `run-validate.ts` has a standalone replacement so far (the rest await re-wiring —
> `miga` epic). Commands below are retained for their flags/semantics.

```bash
# Validate all objects in a paper (schema + constraints + LaTeX AST)
bun run scripts/run-validate.ts content/quantum-observable-universe   # after setup-folio-assistant.sh
# (legacy form, pre-miga: cd content && bun run pipeline/validate.ts quantum-observable-universe/)

# Full build with validation
cd content && bun run pipeline/build.ts quantum-observable-universe/quantum-observable-universe.ts

# Validate TeX snippets in .md files (AST-based, no compilation)
cd content && bun run pipeline/validate-tex.ts

# Validate specific file
cd content && bun run pipeline/validate-tex.ts --file path/to/block.md

# Validate with pdflatex compilation (slower, catches more)
cd content && bun run pipeline/validate-tex.ts --compile

# JSON output (for programmatic use by skills)
cd content && bun run pipeline/validate-tex.ts --json

# Strict mode: also fire `term-mention-coverage` on bare-text
# mentions of known glossary slugs. Run once a chapter has been
# backfilled with `:refterm[…]`.
cd content && bun run validate quantum-observable-universe --strict

# Build the glossary index (committed) + LaTeX chapter (gitignored)
cd content && bun run pipeline/build-glossary.ts quantum-observable-universe

# CI gate: non-zero exit on duplicates or out-of-date glossary.json
cd content && bun run pipeline/build-glossary.ts quantum-observable-universe --check
```

## Post-rebase / merge: run the lean-ref migration first

**Before** running validation after a rebase, merge, or cherry-pick
from upstream, **always run** the idempotent `lean.ref` migration:

```bash
cd content && bun run migrate-lean-refs
```

Coexisting forks may have authored content blocks against the legacy
`lean: { decl: "...", file? }` shape; the migration converts them to
the package-qualified URI form `lean: { ref: "<pkg>:<Decl>" }` that
the current Zod schema requires. Running validation first will fail
with `Lean ref must be "<package>:<Decl.Path>"` errors that are
trivially fixed by the migration. See AGENTS.md §0b.

When the schema's Zod error message names this script in its
output, **do not hand-edit the failing block** — run the script.

## When to validate

1. **Before commit**: Run validation on changed content objects
2. **After editing .md files**: Run `validate-tex.ts` on changed files —
   this uses the remark AST parser to extract and validate all TeX snippets
3. **After adding new blocks**: Check constraints (lean file exists, labels resolve)
4. **After modifying schema**: Run validation across all content
5. **After creating .md content**: Any skill that creates or edits `.md` files
6. **After Lean changes**: Run `bun run scripts/lean-audit.ts` for sorry/trivial/witness audit
7. **After computation changes**: Run `bun run scripts/witness-audit.ts` for staleness check
   MUST run `validate-tex.ts --file <path>` before considering the task complete
8. **After rebase / merge from upstream**: **first** run
   `bun run migrate-lean-refs` (see top of this section), then run
   `bun run validate` to confirm the schema is clean

## Adding custom constraints

Add rules to `CONSTRAINT_RULES` array in `content/schema/constraints.ts`:

```typescript
CONSTRAINT_RULES.push({
  id: "my-rule",
  description: "Custom constraint",
  appliesTo: ["definition", "theorem"],
  check: (block, ctx) => {
    // Return error message string or null
    return null;
  },
});
```

## Mandatory fallback participation

This skill is invoked automatically by the editor's **content-change fallback**
(see `editor.md § Content-change fallback`). Whenever any content is modified
during a session, the editor runs `content_validate` on affected chapters
before the task is considered complete.

## Block-kind classification rules

When auditing or creating blocks, use these criteria to assign the correct kind:

| Criterion | Kind | Example |
|-----------|------|---------|
| Introduces new structure/axioms | `definition` | quantum-universe, categorical-connection |
| Asserts a consequence of upstream defs | `proposition` / `theorem` | spin-labels (consequence of SU(2) emergence) |
| Proves something can be *constructed* from upstream | `theorem` (existence) | weight-decomposition-exists |
| Lightweight wrapper / synonym for Mathlib type | `remark` (glossary) | rigid-monoidal-category |

**Key test**: "Does this block introduce new mathematics, or does it assert
something that *follows* from existing definitions?" If the latter, it should
be a proposition/theorem, not a definition.

**Conditional definitions**: Some definitions are only meaningful given
upstream results (e.g. `def:maximal-torus` requires `thm:su2-emergence`).
These remain definitions but MUST list the immediate upstream theorem in
`uses[]` if it is a direct prerequisite.

## Proposition/theorem purity rule

**Propositions and theorems contain ONLY the mathematical statement.**
The `.md` file of a `proposition`, `theorem`, `lemma`, or `corollary`
block must contain only:

- Hypotheses (the "let" / "given" clauses)
- The conclusion (the "then" statement)
- Classical limit statements (if part of the formal result)

The following belong in **companion remark** blocks, not in the
statement block:

| Content type | Where it goes | Naming convention |
|---|---|---|
| Physical interpretation | `rem:<label>-physical` | `interprets: "prop:original"` |
| Proof sketch / strategy | `rem:<label>-proof-strategy` | `interprets: "thm:original"` |
| Testable predictions | `rem:<label>-prediction` | `interprets: "prop:original"` |
| Classical-limit discussion | `rem:<label>-classical-limit` | `interprets: "prop:original"` |
| Comparison tables | `rem:<label>-comparison` | `interprets: "prop:original"` |
| Connection to other topics | `rem:<label>-connection` | `interprets: "prop:original"` |

**Rationale**: Theorems are cited, cross-referenced, and formalised
in Lean.  Explication clutters the formal statement and makes it
harder to extract the precise mathematical content.  Companion
remarks provide the interpretive layer without contaminating the
statement.

**Remark length rule**: A remark block should cover **one topical
group**.  If a remark exceeds ~60 lines and covers multiple
distinct topics (each with its own header), split it into
separate remarks with focused titles.  Each sub-remark should
`interprets:` the same parent block.

## Dependency completeness checks

**Immediate neighbors only.** The `uses[]` array lists only direct
dependencies — not the full transitive chain. If A→B and B→C, then A
lists only B. Run `bun run pipeline/prune-transitive-deps.ts` to
enforce this after edits.

When auditing `uses[]` arrays:

1. **Narrative cross-refs**: Every `[text](#label)` in the `.md` file should
   have a corresponding entry in `uses[]` only if the referenced block is
   a **direct** dependency (not if it's already reachable transitively
   through another `uses[]` entry). Forward references and example/remark
   references do not need entries.
2. **Gauge group references**: Any block that references `G`, `SU(2)`,
   or the gauge group should depend on `thm:su2-emergence` — but only
   through the nearest intermediate block (e.g. `def:maximal-torus`),
   not by listing `thm:su2-emergence` directly when it's already reachable.
3. **Existence links**: Every definition that bundles fields should have a
   corresponding existence theorem (`thm:<name>-exists`) that proves the
   fields can be constructed from upstream structures.
4. **Lazy-loading caveat**: The viewer dep graph force-loads all sections
   before building edges. If edges appear missing in the UI, verify the
   data is correct before assuming the `uses[]` is wrong.

## Integration with test-engineer

The content-validation skill produces `ValidationResult` objects that the
test-engineer skill can consume in unit tests:

```typescript
import { validateObjects } from "../../content/pipeline/validate";

test("all content objects valid", async () => {
  const result = await validateObjects("content/quantum-observable-universe/quantum-universes/");
  expect(result.valid).toBe(true);
});
```
