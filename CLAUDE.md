# Claude Code — Quantum Observable Universe

This repository is a formal mathematics paper with:
- **Content objects** (`.ts` + `.md` + `.lean` file triples) as authoritative source
- **LaTeX** as a rendering target (generated from content objects)
- **Lean 4** formalization linked to content objects

## CRITICAL: Protected Files — DO NOT MODIFY

The following files are **strictly off-limits** to all coding agents
(Claude, Copilot, etc.). Only the repo owner may edit them manually:

- `deploy/google-viewers.txt` — Google OAuth viewer whitelist
- `deploy/github-collaborators.txt` — GitHub OAuth collaborator whitelist
- `.github/CODEOWNERS` — File ownership rules

These files control authentication access to the folio deployment.
**Never** read, write, edit, or suggest changes to these files.
If asked to modify them, refuse and explain that only the repo owner
can change whitelist files manually.

## Skills

Skills are organized under `.claude/skills/`:

- **`local/`** — repo-specific skills (latex-validation, scientific-accuracy,
  readability-editing)
- **`<package-name>/`** — skills synced nightly from external packages defined
  in `skills-config.json`

### Skill routing (quick reference)

When a user request arrives, route to the right skill(s):

| User request pattern | Primary skill(s) | Min role |
|---------------------|------------------|----------|
| "fill in / prove / remove sorry" | `local/formalizer` + `local/category-theory` | collaborator |
| "define / formalize / add structure" | `local/formalizer` + `local/lean-generation` | collaborator |
| "diagram / naturality / monoidal" | `local/category-theory` | collaborator |
| "extract / stub / from LaTeX" | `local/lean-generation` | collaborator |
| "review / check / audit Lean" | `local/lean-proof-review` | collaborator |
| "status / tracking / manifest" | `local/proof-status-tracking` | reader |
| "what next / priority / triage" | `local/proof-triage` | collaborator |
| "write / edit chapter text" | `local/scientific-accuracy` + `local/readability-editing` | reader (review) / collaborator (edit) |
| "fix lean build / lake build fails" | `local/lean-build-fix` | collaborator |
| "simplify / streamline proofs" | `local/proof-simplifier` | collaborator |
| "validate LaTeX" | `local/latex-validation` | reader |
| "validate content objects" | `local/content-validation` | reader |
| "build content → LaTeX" | `local/content-validation` | reader |
| "add / edit content block" | `local/content-validation` + relevant skill | collaborator |
| "review / audit blocks" | `local/content-block-review` | collaborator |
| "glossary / terminology / naming" | `local/ontologist` + `local/content-validation` | collaborator |
| "work on todos / process feedback" | `local/todo-review` | reader |
| "missing proof (narrative)" | `local/editor` §Proof workflow | collaborator |
| "missing proof (Lean)" | `local/formalizer` + `local/proof-triage` | collaborator |
| "test / unit test / coverage" | `local/test-engineer` | collaborator |
| "deploy / auth / OAuth / roles" | `local/deployment-auth` | owner |
| "import / arxiv / upload paper" | `local/paper-importer` | collaborator |
| "import + formalize" | `local/paper-importer` + `local/formalizer` | collaborator |
| "upload / scan / intake / process document" | `local/document-intake` | collaborator |
| "WHO / guideline / L1 / L2 / normative" | `local/document-intake` | collaborator |
| "uploads/ status / what's pending" | `local/document-intake` | collaborator |
| "critical path / trace dependencies" | `local/critical-path-analysis` | collaborator |
| "archimedean vs categorical / context audit" | `local/critical-path-analysis` | reader |
| "what assumptions does X need" | `local/critical-path-analysis` | reader |
| "separate categorical / split statement" | `local/critical-path-analysis` + `local/content-validation` | collaborator |
| "simulator / simulation / interactive viz" | `local/simulator` + `local/content-validation` | collaborator |
| "set up lean / install lean / lean not working" | `local/lean-environment-setup` | collaborator |
| "generate docs / build docs / schema docs" | `local/docs-generation` | reader |
| "build paper / compile PDF / render HTML" | `local/docs-generation` | reader |
| "TypeDoc / type docs / dependency graph" | `local/docs-generation` | reader |
| "diff / changes / what changed / undo" | `local/diff` | reader |
| "chapter complexity / reorder sections / backward edges / graph energy" | `local/chapter-complexity-review` | reader |

### Skill role assignments

Every skill has a `roles:` field in its YAML frontmatter listing which
user roles may invoke it. The three roles form a hierarchy:
`reader < collaborator < owner`. Each role inherits all lower-role skills.

| Role | Skills |
|------|--------|
| `reader` | editor, content-validation, latex-validation, scientific-accuracy, readability-editing, proof-status-tracking, todo-review, docs-generation, diff, chapter-complexity-review |
| `collaborator` | All reader skills + formalizer, category-theory, lean-generation, lean-proof-review, lean-build-fix, proof-triage, proof-simplifier, chapter-analysis, content-block-review, ontologist, paper-importer, document-intake, test-engineer, lean-environment-setup, simulator |
| `owner` | All collaborator skills + deployment-auth |

When a user connects via **Folio Assist** (chat), they default to `reader`
unless authenticated via GitHub OAuth (which grants `collaborator` or `owner`).
Agents coordinating sub-skills **must** check the user's role against each
skill's `roles:` list before routing.

**Decision tree**: (1) Check the user's role — only route to skills they
can access. (2) Does it touch content objects (`.ts` + `.md`)? →
`local/content-validation` + relevant content skill. (3) Does it touch `.tex`?
→ LaTeX skills. (4) Does it touch `.lean`? → Lean skills above. (5) Both
content + Lean? → also `local/lean-generation` for cross-refs. (6) Ambiguous?
→ read the skill `.md` files, then ask the user.

See **§12 Using Skills for Content Changes** in
`.github/copilot-instructions.md` for the full authoritative mapping,
including the detailed decision tree and Lean-specific routing table.

### Coding conventions

Follow the detailed rules in `.github/copilot-instructions.md` — they govern
LaTeX structure, labeling, cross-references, prose style, notation, and skill
usage for content changes.

## Writing `.lean` proofs — rules for agents

These rules apply whenever an agent creates or modifies a `.lean` file.
Agents **must** follow all of them; violations will be caught by the
`content-block-review` skill.

### 1. Every `sorry` requires a bibliographic citation

```lean
-- Ref: [kock2004] https://doi.org/10.1017/CBO9780511615443
sorry
```

- The `[key]` must match an entry in `content/schema/references.ts` exactly (case-sensitive).
  (`references.bib` is auto-generated — run `bun run export-bibtex` in `content/`).
- If no published reference exists, use `[manuscript]` and cite chapter/section.
- A `sorry` without `-- Ref:` is always a review failure.

### 2. Naming convention: LaTeX label → Lean declaration

| LaTeX label | Lean declaration | Rule |
|---|---|---|
| `thm:lifting-exists` | `QOU.Torsion.lifting_exists` | Hyphens → underscores |
| `def:quantum-connection` | `QOU.QuantumObservableUniverse.quantum_connection` | Namespace = chapter module |
| `def:categorical-instanton` | `CategoricalInstanton` | Type-level structures use CamelCase |
| `prop:categorical-dq-squared` | `categorical_dq_squared` | Theorems/lemmas use snake_case |

All declarations live under the `QOU` root namespace.

### 3. Block kind determines Lean requirements

| Block kind | `.lean` file required? |
|---|---|
| `definition` | **Yes** — enforced; will not build without it |
| `theorem`, `lemma`, `proposition`, `corollary` | **Expected** — warning if missing |
| `conjecture`, `example`, `remark` | Optional |
| `simulator` | N/A |
| `prose`, `equation`, `diagram` | N/A |

### 4. Formalization status is derived, not stored

Formalization status (`not_started`, `stated`, `has_sorry`, `proved`,
`mathlib_ok`) is **not stored in `.ts` manifests**. It is derived at
build time by CI scripts from `.lean` file content and Lean build output,
then written to `proof-objects.json`. Agents must **never** add a `status`
field to content block `.ts` files.

### 4a. TodoItem lifecycle rules

Content TODOs are **external to paper content**. They live in `todos/`
(gitignored — survives branch switches), referencing content blocks via
`targetLabel`. This keeps the paper source clean and avoids confusion
between scholarly content and work-tracking metadata.

```
todos/                           ← gitignored
  content-todos.ts               ← content-related todos
  infra-todos.ts                 ← infrastructure todos (optional)
```

The `TodoItem` type is defined in `content/schema/types.ts` for reuse,
but no `todos` field exists on any content block type or schema.

The MCP server serves todos at `/api/todos` (JSON) and `/todos` (HTML
dashboard). The `check-todos.sh` SessionStart hook summarizes open
items at the start of each session.

| Action | Who may do it |
|--------|--------------|
| **Create** a TodoItem | Agent or human |
| **Update** status to `in_progress` | Agent or human |
| **Resolve / close** a TodoItem (`resolved`, `wontfix`) | **Human only** |
| **Remove** a TodoItem from the array | **Human only** |

Agents **must never** set a TodoItem's status to `resolved` or `wontfix`,
and **must never** delete a TodoItem. The author verifies completion —
even after a commit has been made — and closes the item themselves.
Agents may add new TodoItems and may move items to `in_progress`, but
closing is always a human action.

### 4b. Glossary block policy (Chapter 8)

Chapter 8 ("Glossary of Rigid Monoidal Terms") contains **glossary
blocks** — `remark` blocks with tag `"glossary"` — that map paper
terminology to canonical Mathlib declarations. These are light
terminological wrappers: **no semantic novelty**, just naming
conventions.

| Criterion | Glossary block | Definition block |
|-----------|---------------|-----------------|
| Semantic novelty | None (Mathlib synonym) | New mathematics |
| Block kind | `remark` | `definition` |
| Label pattern | `rem:glossary-<term>` | `def:<term>` |
| Lean file | Not required | **Required** |
| Chapter | Ch 8 | Relevant content chapter |

**Decision rule**: If the paper uses a term that is a synonym for (or
lightweight wrapper around) a Mathlib type, add a glossary block. If
the paper introduces genuinely new axioms/structure, add a definition.

### 5. Tactic strategy (try in order)

| Goal pattern | Try first | Then try |
|---|---|---|
| Algebraic identity (`x = y`) | `ring` | `field_simp; ring` |
| Non-negativity (`0 ≤ x`) | `positivity` | `linarith` |
| Numeric (`x < y`) | `norm_num` | `linarith` |
| Definitional equality | `rfl` | `unfold …; rfl` |
| Diagram / naturality | `aesop_cat` | `slice_lhs`, `slice_rhs` |
| Anything else | `simp` | `aesop` |

### 6. Use MCP tools, not shell commands

| Task | Use this | Not this |
|---|---|---|
| Check errors | `lean_diagnostic_messages` | `lake build` + parse |
| Read goal state | `lean_goal` | Python scripts |
| Search Mathlib | `lean_leansearch` / `lean_loogle` | grep Mathlib source |
| Try tactics | `lean_multi_attempt` | edit-build-repeat |
| Axiom audit | `lean_verify` | manual inspection |

### 7. Category theory conventions

- **Category notation**: Use bold `$\mathbf{C}$` for categories
  (Herrlich–Strecker style), never calligraphic `$\mathcal{C}$`.
  Named categories are also bold: `$\mathbf{Rep}(\mathrm{SU}_q(2))$`.
  Calligraphic letters are reserved for sheaves, sites, and algebras
  (`$\mathcal{S}$`, `$\mathcal{O}$`, `$\mathcal{A}$`).
- **Fibre functor**: Always `$\tau$` (not `$\omega$` or `$U$`).
  Minimise its appearance — write `$(\mathbf{C}, A)$` when the functor
  is not needed; write `$(\mathbf{C}, A, \tau)$` only when `$\tau$` is
  explicitly used.
- Functors are bundled: `F.obj X`, `F.map f` — never treat `F` as a function.
- Open `CategoryTheory.MonoidalCategory` for notation: `X ⊗ Y`, `𝟙_ C`,
  `α_`, `λ_`, `ρ_`, `X ◁ f`, `f ▷ X`.
- Diagram commutativity: try `aesop_cat` first, then `slice_lhs`/`slice_rhs`.
- Use `Subsingleton (X ⟶ Y)` for vanishing hom-spaces (avoids `Preadditive`).

### 8. File hygiene

- Never commit `.lake/`, `lake-packages/`, or `build/`.
- **Pin external dependencies to commit hashes** in `lakefile.toml` —
  never use branch names (`main`, `master`) or version tags (`v4.16.0`).
  Mathlib version numbers ≠ Lean version numbers; tags can resolve to
  unexpected toolchain versions.
- **All deps must agree on the same `lean-toolchain`**. Before adding or
  updating a dep, check `cat .lake/packages/<dep>/lean-toolchain` for
  every package. If any disagree, find compatible versions first.
  See `formalizer.md § Adding New Dependencies` for the full procedure.
- To recover from broken `.lake/`, use `mv .lake /tmp/...` (not `rm -rf`).
- Keep imports minimal — only import what the file actually uses.
- The `.lean` sibling file must share the same root name as its `.ts`/`.md`
  siblings (e.g., `rigid-monoidal-category.lean`).

## Content-object architecture

Content is organized as **atomic knowledge units** — each definition,
theorem, remark, etc. is a self-contained file triple:

```
content/
  <paper-name>/
    <paper-name>.ts              ← Paper manifest (references chapter URIs)
    <chapter-dir>/
      <chapter-dir>.ts           ← Chapter manifest (sections → block refs)
      <block-name>.ts            ← Typed manifest (kind, label, lean ref, status)
      <block-name>.md            ← Narrative content (markdown + TeX snippets)
      <block-name>.lean          ← Lean formalization (when required by kind)
```

### File naming convention

Sibling files share the same root name: `rigid-monoidal-category.ts`,
`rigid-monoidal-category.md`, `rigid-monoidal-category.lean`.

### Type system

| Block kind | Lean required? | Label prefix |
|-----------|---------------|-------------|
| `definition` | **Yes** (enforced at type level) | `def:` |
| `theorem`, `lemma`, `proposition`, `corollary` | Expected (warning if missing) | `thm:`, `lem:`, `prop:`, `cor:` |
| `conjecture`, `example`, `remark` | Optional | `conj:`, `ex:`, `rem:` |
| `simulator` | N/A | `sim:` |
| `prose`, `equation`, `diagram` | N/A | — |

### Pipeline

```
.ts manifests + .md content
  → Zod schema validation (shape + types)
  → Constraint rules (file existence, cross-refs, lean requirements)
  → LaTeX rendering (markdown → LaTeX conversion)
  → AST validation (unified-latex parse of rendered output)
  → chapters/*.tex output
```

### Key files

| Path | Purpose |
|------|---------|
| `content/schema/types.ts` | TypeScript types (discriminated unions) |
| `content/schema/constraints.ts` | Zod schemas + constraint rules |
| `content/schema/builders.ts` | `definition()`, `theorem()`, `prose()`, etc. |
| `content/pipeline/validate.ts` | Three-level validation |
| `content/pipeline/render-latex.ts` | Block → LaTeX + AST validation |
| `content/pipeline/build.ts` | Full document build |
| `content/schema/references.ts` | **Bibliography source of truth** (CSL-JSON) |
| `content/pipeline/export-bibtex.ts` | Generates `references.bib` from CSL-JSON |
| `content/pipeline/validate-references.ts` | Bibliography + citation cross-checks |
| `content/pipeline/citations.ts` | `\cite{}` extraction from .md content |

### Bibliography architecture

The bibliography is managed as **typed CSL-JSON** in
`content/schema/references.ts`. BibTeX (`references.bib`) is a downstream
render target, auto-generated by `bun run export-bibtex`.

- **Adding a reference**: use the `ref()` builder in `references.ts`
- **Block citations**: `cites: string[]` field on blocks (auto-extracted
  from `\cite{}` in .md by the pipeline, or set explicitly in .ts)
- **Chapter bibliography**: aggregated at build time from all block cites
- **Validation**: `bun run validate-refs` checks schema, uniqueness, DOIs,
  and cross-references against Lean `-- Ref:` and LaTeX `\cite{}`
- **Never edit `references.bib` directly** — it is regenerated on build

### Dependency graph integration

The `uses[]` field in content objects + Lean import graphs form a
combined dependency DAG. Editors and proof-writers use this to:

- **Track upstream changes**: when a definition changes, find all
  theorems/lemmas that `uses` it and flag them for re-validation
- **Track downstream impact**: when proposing a change, identify all
  blocks that depend on the changed block
- **Scope test runs**: only run Lean builds / AST validation for the
  changed block and its downstream dependents
- **Prioritize formalization**: find blocks with the most dependents
  that are still `not_started`

### Cross-paper references

The `uses[]` field supports three reference scopes:

| Scope | Syntax | Example |
|-------|--------|---------|
| Same paper | bare label | `"def:quantum-universe"` |
| Same folio | `"paper-dir:label"` | `"unital-groebner-bases:cor:pbw"` |
| External folio | full URL | `"https://folio.example.org/viewer/#/view/paper-id"` |

Cross-paper refs are validated at folio level, not per-paper. The
`uses-resolve` constraint skips qualified refs (those matching
`paper-dir:label` or starting with `https://`).

Each paper in `content/folio.ts` has an optional `url` field for
viewer routing. CSL-JSON entries in `content/schema/references.ts`
for folio-hosted papers include a URL field matching the viewer hash route
(e.g. `/viewer/#/view/unital-groebner-bases`).

### Markdown content convention (in .md files)

- Inline math: `$...$`
- Display math: `$$...$$`
- Complex TeX (tikzcd, align): fenced code block with `` ```tex `` tag
- Bold → `\textbf{}`, italic → `\emph{}` in LaTeX output
- Cross-refs: `[text](#label)` → `\hyperref[label]{text}`

### TeX authoring patterns for agents

These rules prevent rendering errors in the content pipeline.
Violations produce broken LaTeX in titles, captions, and body text.

**1. Math in titles is supported.** Block titles (in `.ts` manifests)
may contain inline math. The `escapeLatex()` function preserves
`$...$` segments verbatim. Always use `$...$` delimiters:

```ts
// CORRECT — math preserved in rendered \begin{example}[{...}]
title: "Reeb derivation for $\\mathrm{SU}(2)$"

// WRONG — bare LaTeX commands will be escaped to garbage
title: "Reeb derivation for \\mathrm{SU}(2)"
```

**2. Multi-line inline math is valid.** The remark-math parser handles
`$...$` spanning multiple lines. This is the standard pattern for long
inline expressions in list items:

```md
1. **Cyclicity**: $\mathrm{tr}_{\mathrm{Ad}}(f \circ g) =
   \mathrm{tr}_{\mathrm{Ad}}(g \circ f)$, inherited from the
   Frobenius relation.
```

**3. Never use raw TeX commands in prose outside `$...$`.** The markdown
→ LaTeX converter only passes through content inside math delimiters
or `` ```tex `` fenced blocks. Bare `\mathrm{...}` outside delimiters
renders as literal text.

**4. Use `$$...$$` on separate lines for display math.** The `$$`
delimiter must be alone on its line (or at the very start/end):

```md
The formula is:

$$
  \nabla^2 \phi = 0
$$
```

**5. For complex environments (tikzcd, align), use fenced tex blocks:**

````md
```tex
\begin{tikzcd}
  A \arrow[r] & B
\end{tikzcd}
```
````

**6. Ampersands in math are fine.** The `&` character inside `$...$` or
`` ```tex `` blocks is not escaped (it's a column separator in matrices
and alignments). Only `&` in prose text causes LaTeX errors.

## Lean MCP server (lean-lsp-mcp)

The [lean-lsp-mcp](https://github.com/oOo0oOo/lean-lsp-mcp) server is
configured via `.mcp.json`. It provides Claude Code with:

- Diagnostics, goal states, hover docs, completions
- LeanSearch, Loogle, Lean Finder, Lean Hammer search tools
- Code actions ("Try This"), profiling, axiom verification
- Local project search (requires ripgrep)

### Setup

All MCP functionality — including Lean tools — is served through
the unified `paper-assistant` server. To install Lean dependencies:

```bash
./scripts/start-folio-assistant.sh --install
```

This installs: elan, the Lean toolchain pinned in
`lean-archive/lean-toolchain`, Mathlib cache, ripgrep, and uv.

**Important**: Run `lake build` in `lean-archive/` before first MCP
session to avoid timeouts.

### Remote MCP server

A Docker-based remote deployment is available in `deploy/`:

```bash
cd deploy && ./setup-remote.sh
```

All settings are driven by `lean-mcp.config.json` at the repo root.

Architecture: `Client → Caddy (TLS) → auth-gateway (dual OAuth) → lean-lsp-mcp (HTTP)`

- Docker image built by CI on every push to main (`build-lean-mcp.yml`)
- All Lean deps and oleans baked into the image for fast startup (~10-20s)
- Auth: Dual OAuth — Google (viewers) + GitHub (collaborators/owner)
- Roles: viewer (read + feedback), collaborator (edit + branches), owner (commit to main)
- Whitelists: `deploy/google-viewers.txt` + `deploy/github-collaborators.txt` (manually managed)
- Auto-update: `self-update-folio.sh` polls git + GHCR every minute via cron
- Programmatic access: bearer token via `FOLIO_API_TOKEN`
- Hosting: Hetzner CX22 (~€4.50/mo), provisioned via `provision-hetzner.sh`

To switch a client to remote mode, update `.mcp.json`:

```json
{"mcpServers":{"lean-lsp":{"url":"https://folio.litlfred.org/mcp"}}}
```

To extract the deploy infrastructure for another repo, copy `deploy/`,
`lean-mcp.config.json`, `.github/docker/Dockerfile.lean-mcp`, and
`.github/workflows/build-lean-mcp.yml`, then edit `lean-mcp.config.json`.

### Session-start hook

A `SessionStart` hook in `.claude/settings.json` runs `scripts/check-lean.sh`
at the beginning of every session. If Lean or uv is not available and the
user's request requires Lean, the editor skill will prompt the author with
setup instructions rather than silently failing.

## Project structure

| Path | Purpose |
|------|---------|
| `content/` | **Authoritative content objects** (`.ts` + `.md` + `.lean` triples) |
| `content/schema/` | Type system, Zod schemas, builder functions (re-exports from `folio-assistant/schemas/`) |
| `content/pipeline/` | Validation, rendering, build pipelines |
| `content/<paper>/` | Paper manifest + chapter directories |
| `folio-assistant/` | **Platform package** — MCP server, auth, UI, blocks, viewer |
| `folio-assistant/src/` | Generic core (server, types, routes, tools, blocks registry) |
| `folio-assistant/adapters/paper/` | Paper content adapter (implements `ContentAdapter`) |
| `folio-assistant/schemas/` | Shared TypeScript types (proof-objects, glossary, etc.) |
| `folio-assistant/viewer/` | Paper viewer SPA + Pyodide cache Service Worker |
| `folio-assistant/ui/` | Assistant chat SPA |
| `folio-assistant/simulators/` | Interactive HTML simulators |
| `folio-assistant/feedback/` | User feedback (TypeScript files, committed to main) |
| `folio-assistant/computations/` | Computation scripts and witness data |
| `folio.config.json` | Adapter config (content type, adapter module, feedback dir) |
| `main.tex` | LaTeX preamble and document structure (rendering target) |
| `chapters/*.tex` | Generated LaTeX chapters (from content pipeline) |
| `references.bib` | BibTeX database (auto-generated from `content/schema/references.ts`) |
| `lean/` | Lean 4 formalization (lakefile.lean, QOU/) |
| `blueprint/src/` | LeanBlueprint source (content.tex, preamble.tex, web.tex, print.tex) |
| `home_page/` | Jekyll landing page for GitHub Pages |
| `.github/workflows/` | CI/CD pipelines |
| `.github/scripts/` | Python orchestration (ontologist, extraction, stub generation) |
| `.claude/skills/local/` | Repo-specific review skills |
| `.claude/skills/<pkg>/` | Synced external skill packages |
| `uploads/` | Document intake pipeline (raw PDFs, scans, WHO guidelines → content objects) |
| `todos/` | Work-tracking TodoItems, gitignored (external to paper content) |
| `docs/` | Planning documents, migration plans, dependency graphs |
| `scripts/` | Setup and health-check scripts (Lean MCP, etc.) |
| `lean-mcp.config.json` | MCP server config (domain, image, auth, ports) |
| `deploy/` | Remote MCP server deployment (Docker Compose, auth, auto-update) |
| `skills-config.json` | Skill package subscriptions |

## Build output (gh-pages)

Three workflows deploy to the `gh-pages` branch. GitHub Pages must be
configured to **deploy from the `gh-pages` branch** (not "GitHub Actions").

### Workflow → artifact mapping

| Workflow | Artifacts deployed to gh-pages |
|----------|-------------------------------|
| `blueprint.yml` | `blueprint/` (interactive dependency graph), `blueprint.pdf`, `docs/` (doc-gen4 API), `axiom-report.txt`, manifests |
| `lean_ci.yml` | `lean/` (source browser), `lean/docs/`, `axiom-report.txt`, `dependency-graph.svg`, manifests |
| `publish.yml` | `papers/<dir>/` (per-paper viewers), `index.html` (folio), `schema-docs/` (TypeDoc), `drafts/` (feature branches) |

### Expected gh-pages contents

| Path | Source | Description |
|------|--------|-------------|
| `index.html` | publish.yml | Folio landing page (links to all papers) |
| `papers/<dir>/index.html` | publish.yml | Per-paper viewer with paper/visualizer toggle |
| `papers/<dir>/paper.html` | publish.yml | Enhanced HTML paper |
| `papers/<dir>/<dir>.pdf` | publish.yml | Compiled paper PDF |
| `papers/<dir>/<dir>.md` | publish.yml | Pandoc Markdown |
| `quantum-observable-universe.pdf` | publish.yml | Backward-compat copy of first paper PDF |
| `blueprint/` | blueprint.yml | Interactive dependency graph (plasTeX HTML) |
| `blueprint.pdf` | blueprint.yml | Print blueprint |
| `docs/` | blueprint.yml | doc-gen4 API documentation with hover definitions |
| `lean/` | lean_ci.yml | Raw Lean source files |
| `lean/docs/` | lean_ci.yml | doc-gen4 or fallback source browser |
| `axiom-report.txt` | blueprint.yml / lean_ci.yml | sorry audit, axiom dependencies |
| `dependency-graph.svg` | lean_ci.yml / publish.yml | Visual proof dependency graph |
| `schema-docs/` | publish.yml | TypeDoc content-object type reference |
| `proof-objects.json` | all | Formalization status manifest |
| `glossary.json` | all | Semantic glossary |
| `mapping.json` | all | Narrative-to-Lean identifier map |
| `drafts/<branch>/` | publish.yml | Feature branch preview builds |

### Error resilience

All workflows use `continue-on-error: true` at critical points so partial
output is still deployed even when the Lean build fails:

- **Lean build fails** → proof status updates, axiom report generates, source
  browser deploys.  `proof-objects.json` records which declarations errored.
- **doc-gen4 fails** → `lean_ci.yml` generates a fallback HTML source browser.
- **Blueprint compilation fails** → other artifacts (manifests, axiom report)
  still deploy.
- **latexdiff fails** → main PDF still publishes; diff PDF is skipped.
