#!/usr/bin/env bash
# generate-readme.sh — Regenerates README.md from the current project state.
#
# Usage: ./scripts/generate-readme.sh [--check]
#   --check   Print diff and exit non-zero if README.md would change (for CI)
#
# This script assembles README.md from static prose and dynamic sections
# derived from the actual file tree (chapters, Lean modules, simulators,
# papers, workflows).  Run it whenever project structure changes.

set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

OUT="$(mktemp)"
trap 'rm -f "$OUT"' EXIT

# ── Helpers ──────────────────────────────────────────────────────────────────

section() { printf '\n## %s\n\n' "$1" >> "$OUT"; }
subsection() { printf '\n### %s\n\n' "$1" >> "$OUT"; }
line() { printf '%s\n' "$1" >> "$OUT"; }
blank() { printf '\n' >> "$OUT"; }

# ── Header ───────────────────────────────────────────────────────────────────

cat >> "$OUT" << 'HEADER'
# Quantum Observable Universe

[![Lean CI](https://github.com/litlfred/qou/actions/workflows/lean_ci.yml/badge.svg)](https://github.com/litlfred/qou/actions/workflows/lean_ci.yml)
[![Build & Publish](https://github.com/litlfred/qou/actions/workflows/publish.yml/badge.svg)](https://github.com/litlfred/qou/actions/workflows/publish.yml)
[![Blueprint](https://github.com/litlfred/qou/actions/workflows/blueprint.yml/badge.svg)](https://github.com/litlfred/qou/actions/workflows/blueprint.yml)

A formal mathematics paper exploring the Quantum Observable Universe (QOU)
with machine-checked **Lean 4** formalization, **content-object architecture**
(TypeScript + Markdown + Lean triples), and an interactive **Folio Assistant**
platform for browsing, reviewing, and exploring the work.
HEADER

# ── Content-Object Architecture ──────────────────────────────────────────────

section "Content-Object Architecture"

cat >> "$OUT" << 'ARCH'
Content is organized as **atomic knowledge units** — each definition,
theorem, remark, or proof is a self-contained file triple:

```
content/<paper>/<chapter>/
  <block>.ts    ← Typed manifest (kind, label, dependencies, metadata)
  <block>.md    ← Narrative content (Markdown + TeX snippets)
  <block>.lean  ← Lean 4 formalization (when required by block kind)
```

The pipeline validates content objects against Zod schemas, checks
cross-references, renders LaTeX, and runs AST validation before
producing `chapters/*.tex` output. LaTeX is a **rendering target**,
not the source of truth.
ARCH

# ── Papers ───────────────────────────────────────────────────────────────────

section "Papers"

cat >> "$OUT" << 'PAPERS'
The repository hosts multiple papers as a **folio**:

| Paper | Directory | Description |
|-------|-----------|-------------|
PAPERS

# Detect papers from content/ directories that have a .ts manifest
for dir in content/*/; do
  name="$(basename "$dir")"
  # Skip non-paper directories
  [[ "$name" == "schema" || "$name" == "pipeline" || "$name" == "node_modules" ]] && continue
  manifest="$dir${name}.ts"
  if [[ -f "$manifest" ]]; then
    # Extract title from the manifest if possible
    title=$(grep -oP "title:\s*['\"]\\K[^'\"]*" "$manifest" 2>/dev/null | head -1 || echo "$name")
    [[ -z "$title" ]] && title="$name"
    line "| ${title} | \`content/${name}/\` | $(basename "$dir") |"
  fi
done

# ── Chapters (main paper) ───────────────────────────────────────────────────

section "Chapters (Quantum Observable Universe)"

line "| Chapter | Directory |"
line "|---------|-----------|"

for dir in $(ls -d content/quantum-observable-universe/ch*/ | sort -t'-' -k1 -V); do
  [[ -d "$dir" ]] || continue
  chapter_dir="$(basename "$dir")"
  # Parse chapter number and name from directory
  chapter_num="${chapter_dir%%-*}"
  chapter_name="${chapter_dir#*-}"
  chapter_name="${chapter_name//-/ }"
  # Capitalize first letter of each word
  chapter_name="$(echo "$chapter_name" | sed 's/\b\(.\)/\u\1/g')"
  line "| ${chapter_num} | \`${chapter_dir}/\` — ${chapter_name} |"
done

# Appendices
for dir in content/quantum-observable-universe/appendix-*/; do
  [[ -d "$dir" ]] || continue
  app_dir="$(basename "$dir")"
  app_name="${app_dir#appendix-}"
  app_name="${app_name//-/ }"
  app_name="$(echo "$app_name" | sed 's/\b\(.\)/\u\1/g')"
  line "| Appendix | \`${app_dir}/\` — ${app_name} |"
done

# ── Lean 4 Formalization ────────────────────────────────────────────────────

section "Lean 4 Formalization"

cat >> "$OUT" << 'LEAN_INTRO'
The Lean 4 formalization lives in `content/quantum-observable-universe/lean/`
and covers the key mathematical structures, mass-parameter derivations,
knot theory, and categorical constructions from the manuscript.
LEAN_INTRO

subsection "Modules"

line "| Module | Source |"
line "|--------|--------|"

# List top-level .lean files under QOU/
lean_dir="content/quantum-observable-universe/lean/QOU"
if [[ -d "$lean_dir" ]]; then
  for f in "$lean_dir"/*.lean; do
    [[ -f "$f" ]] || continue
    mod="QOU.$(basename "$f" .lean)"
    line "| \`${mod}\` | \`$(basename "$f")\` |"
  done
  # List subdirectory modules
  for sub in "$lean_dir"/*/; do
    [[ -d "$sub" ]] || continue
    subname="$(basename "$sub")"
    count=$(find "$sub" -name '*.lean' | wc -l)
    line "| \`QOU.${subname}.*\` | ${count} files |"
  done
fi

subsection "Knot Registry"

cat >> "$OUT" << 'KNOTS'
Every knot in the formalization carries an Alexander-Briggs index, a QOU
physical identity, a SnapPy-verified hyperbolic volume, and a persistent
link to [The Knot Atlas](http://katlas.org/).

| A-B Index | QOU Identity | Hyperbolic Volume | Knot Atlas |
|-----------|-------------|-------------------|------------|
| 0₁ | Neutrino (SU(2) vacuum) | 0 | [0_1](http://katlas.org/wiki/0_1) |
| 3₁ | Electron (Gen 1, B₃ monodromy) | 0 (torus knot) | [3_1](http://katlas.org/wiki/3_1) |
| 4₁ | Muon (Gen 2, mass residue) | 2.0298832128 | [4_1](http://katlas.org/wiki/4_1) |
| 0₁ | Photon (exceptional divisor) | 0 | [0_1](http://katlas.org/wiki/0_1) |

Every `sorry` in the Lean source is preceded by a `-- Ref: [key] url` comment
linking to the foundational reference that would resolve the gap.
KNOTS

# ── Folio Assistant ──────────────────────────────────────────────────────────

section "Folio Assistant"

cat >> "$OUT" << 'FOLIO'
The **Folio Assistant** (`folio-assistant/`) is the platform layer providing:

- **MCP Server** — Model Context Protocol server for AI-assisted editing
- **Viewer** — Web-based paper viewer with paper/visualizer toggle
- **Chat UI** — Assistant interface with role-based access (reader/collaborator/owner)
- **Simulators** — Interactive WebGL/HTML visualizations
- **Feedback** — User feedback collection (committed to main)
- **Auth** — Dual OAuth (Google viewers + GitHub collaborators)
FOLIO

subsection "Interactive Simulators"

line "| Simulator | File |"
line "|-----------|------|"

if [[ -d "folio-assistant/simulators" ]]; then
  for f in folio-assistant/simulators/*.html; do
    [[ -f "$f" ]] || continue
    name="$(basename "$f" .html)"
    # Convert underscores to spaces and capitalize
    pretty="$(echo "$name" | tr '_' ' ' | sed 's/\b\(.\)/\u\1/g')"
    line "| ${pretty} | \`simulators/${name}.html\` |"
  done
fi

# ── Published Artefacts ──────────────────────────────────────────────────────

section "Published Artefacts (GitHub Pages)"

cat >> "$OUT" << 'ARTEFACTS'
> **Note:** If GitHub Pages is not publicly accessible, use the GitHub source
> links in the rightmost column to browse the repository directly.

| Artefact | GitHub Pages | GitHub Source |
|----------|-------------|--------------|
| Folio landing page | [index.html](https://litlfred.github.io/qou/) | [home_page/](https://github.com/litlfred/qou/tree/main/home_page) |
| Paper viewer | [papers/quantum-observable-universe/](https://litlfred.github.io/qou/papers/quantum-observable-universe/) | [folio-assistant/viewer/](https://github.com/litlfred/qou/tree/main/folio-assistant/viewer) |
| Paper (PDF) | [quantum-observable-universe.pdf](https://litlfred.github.io/qou/quantum-observable-universe.pdf) | [content/](https://github.com/litlfred/qou/tree/main/content) |
| Blueprint (interactive graph) | [blueprint/](https://litlfred.github.io/qou/blueprint/) | [blueprint/src/](https://github.com/litlfred/qou/tree/main/blueprint/src) |
| Lean interactive docs | [docs/](https://litlfred.github.io/qou/docs/) | [content/.../lean/](https://github.com/litlfred/qou/tree/main/content/quantum-observable-universe/lean) |
| Schema docs (TypeDoc) | [schema-docs/](https://litlfred.github.io/qou/schema-docs/) | [content/schema/](https://github.com/litlfred/qou/tree/main/content/schema) |
| Axiom / Gap Report | [axiom-report.txt](https://litlfred.github.io/qou/axiom-report.txt) | [.github/scripts/](https://github.com/litlfred/qou/tree/main/.github/scripts) |
| Dependency Graph | [dependency-graph.svg](https://litlfred.github.io/qou/dependency-graph.svg) | CI-generated |
| Proof Objects Manifest | [proof-objects.json](https://litlfred.github.io/qou/proof-objects.json) | CI-generated |
| Glossary | [glossary.json](https://litlfred.github.io/qou/glossary.json) | CI-generated |
| Feature branch drafts | [drafts/](https://litlfred.github.io/qou/drafts/) | CI-generated |
ARTEFACTS

# ── Project Structure ────────────────────────────────────────────────────────

section "Project Structure"

cat >> "$OUT" << 'STRUCTURE'
| Path | Description |
|------|-------------|
| `content/` | **Authoritative content objects** (`.ts` + `.md` + `.lean` triples) |
| `content/schema/` | Type system, Zod schemas, builder functions |
| `content/pipeline/` | Validation, rendering, build pipelines |
| `content/quantum-observable-universe/` | Main paper — chapters, appendices, Lean |
| `content/quantum-observable-universe/lean/` | Lean 4 formalization (`lakefile.toml`, `QOU/`) |
| `folio-assistant/` | Platform: MCP server, auth, viewer, chat UI, simulators |
| `folio-assistant/viewer/` | Paper viewer SPA + Pyodide cache |
| `folio-assistant/simulators/` | Interactive HTML/WebGL visualizations |
| `blueprint/src/` | LeanBlueprint source (dependency graph) |
| `deploy/` | Remote MCP deployment (Docker Compose, Caddy, auth) |
| `.github/workflows/` | CI/CD: Lean build, publish, blueprint, deploy |
| `.claude/skills/` | AI skill definitions (local + synced packages) |
| `scripts/` | Build, setup, and utility scripts |
| `main.tex` | LaTeX preamble (rendering target, not source of truth) |
| `chapters/*.tex` | Generated LaTeX chapters (from content pipeline) |
| `references.bib` | Auto-generated BibTeX (source: `content/schema/references.ts`) |
| `home_page/` | Jekyll landing page for GitHub Pages |
STRUCTURE

# ── CI/CD ────────────────────────────────────────────────────────────────────

section "CI/CD Workflows"

line "| Workflow | Purpose |"
line "|----------|---------|"

declare -A workflow_desc=(
  ["lean_ci.yml"]="Lean build, proof status, axiom report, doc generation"
  ["publish.yml"]="Full paper build — PDF, HTML, viewer, schema docs, deploy to gh-pages"
  ["blueprint.yml"]="Blueprint compilation, dependency graph, doc-gen4"
  ["lean-build.yml"]="Lean build and proof status updates"
  ["deploy-folio.yml"]="Deploy Folio Assistant to remote server"
  ["build-lean-mcp.yml"]="Build Lean MCP Docker image"
  ["build-latex-image.yml"]="Build LaTeX CI Docker image"
  ["docker-ci-image.yml"]="Build general CI Docker image"
  ["agent-review.yml"]="AI-assisted code review"
  ["release-folio-assistant.yml"]="Release Folio Assistant package"
  ["snappea_wasm.yml"]="SnapPea WASM build and test"
  ["sync-skills.yml"]="Sync external skill packages"
)

for wf in .github/workflows/*.yml; do
  [[ -f "$wf" ]] || continue
  name="$(basename "$wf")"
  desc="${workflow_desc[$name]:-}"
  if [[ -z "$desc" ]]; then
    # Try to extract name from the file
    desc=$(grep -m1 '^name:' "$wf" 2>/dev/null | sed 's/^name:\s*//' || echo "")
  fi
  line "| \`${name}\` | ${desc} |"
done

# ── Building ─────────────────────────────────────────────────────────────────

section "Building"

cat >> "$OUT" << 'BUILD'
### Content validation and LaTeX generation

```bash
bun install                          # Install dependencies (root + content/)
bun run validate                     # Validate content objects
bun run build:content                # Generate chapters/*.tex from content objects
```

### Paper compilation

```bash
latexmk -pdf main.tex               # Compile PDF from generated LaTeX
```

### Lean formalization

```bash
cd content/quantum-observable-universe/lean
lake build                           # Build all Lean modules
```

### Folio Assistant

```bash
cd folio-assistant && bun install
bun run start                        # Start MCP server
bun run start:http                   # Start in HTTP mode
```

### Schema documentation

```bash
bun run build:docs                   # Generate TypeDoc documentation
```
BUILD

# ── License ──────────────────────────────────────────────────────────────────

section "License"

cat >> "$OUT" << 'LICENSE'
[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

This work is licensed under a
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided
appropriate credit is given, a link to the license is provided, and any
changes made are indicated.
LICENSE

# ── Write or check ──────────────────────────────────────────────────────────

if [[ "${1:-}" == "--check" ]]; then
  if diff -q README.md "$OUT" > /dev/null 2>&1; then
    echo "README.md is up to date."
    exit 0
  else
    echo "README.md is out of date. Run: ./scripts/generate-readme.sh"
    diff --color=auto README.md "$OUT" || true
    exit 1
  fi
fi

cp "$OUT" README.md
echo "README.md updated."
