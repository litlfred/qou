---
name: content-graph
roles: [reader, collaborator, owner]
description: >
  Editorial & Lean Knowledge-Graph organisation skill — analyses (1) the
  prose/content block graph (`uses[]`, `interprets`, `proofs`, `examples`),
  (2) the chapter/section reading-order graph (`H1..H7`), and (3) the Lean 4
  module & Two-Tier Reservoir `lean_lib` import DAG (`L1..L6` via
  `scripts/lean-kg-detangler.py` and `scripts/lean-best-practices-lint.py`).
  Produces actionable reorganisation suggestions and implements approved moves.
allowed-tools: Read Edit Write Bash Grep Glob Agent
---

# Content & Lean Subgraph Graph — Editorial & KG Organisation Skill

## Overview

This skill analyses the **full knowledge graph** of the monograph at three coupled levels:

1. **Block graph** — Every content block under `folio/quantum-observable-universe/` is a node. Edges represent
   relationships: `uses[]` (dependency), `interprets` (remark → statement),
   `proofs[]` (proof → statement), `examples[]` (example → statement).
   The block graph captures the logical argument structure.

2. **Chapter/section graph** — Chapters and sections in [`quantum-observable-universe.ts`](../../folio/quantum-observable-universe/quantum-observable-universe.ts) are nodes. A
   directed edge from section S₁ to section S₂ exists whenever a block in
   S₁ uses a block in S₂. The section graph captures the pedagogical
   reading order (`H1..H7`).

3. **Lean 4 module & Reservoir `lean_lib` subgraph DAG** — Every `.lean` module in `folio/quantum-observable-universe/lean/` and chapter `.lean` sibling is a node (`L1..L6`, audited by [`scripts/lean-kg-detangler.py`](../../scripts/lean-kg-detangler.py) and [`scripts/lean-best-practices-lint.py`](../../scripts/lean-best-practices-lint.py)), stratified strictly from `Mathlib4` → Tier-A `MathlibExt` → Tier-B 6 Lean Reservoir community `lean_lib` packages → 12 canonical chapter-aligned `QOU.<Subgraph>` modules → chapter `.lean` siblings.

## When to Use This Skill

- "content graph" / "content organisation"
- "cross-chapter arrows" / "cross-section dependencies"
- "forward references" / "minimise forward refs"
- "sections too small" / "sections too large" / "section balance"
- "disentangle content" / "reorganise chapters"
- "analyse content connections"
- "show me the block graph" / "show me the chapter graph"
- "what blocks should move?" / "suggest reorganisation"

## Prerequisites

- Python 3 and `graphviz` (installed automatically if missing)
- Content block `.ts` files in `folio/quantum-observable-universe/`
- Chapter manifests with `sections → blocks` structure

## Heuristics

The skill applies the following heuristics, each producing a severity-
ranked finding:

### H1 — Forward references (severity: HIGH)

A **forward reference** occurs when block A `uses` block B, but B appears
*later* in the document than A.  These cause readers to encounter concepts
before they are defined.

A block's position is its (chapter_number, section_index, block_index)
tuple in document order.

```
forward_ref: A (pos P_A) uses B (pos P_B) where P_B > P_A
```

**Ideal:** 0 forward references.
**Acceptable:** ≤ 5 (architectural cycles across categorical/archimedean wall).
**Flag for action:** > 5.

### H2 — Cross-chapter coupling (severity: MEDIUM)

A **cross-chapter edge** occurs when block A in chapter C₁ uses block B in
chapter C₂ (C₁ ≠ C₂).

Count cross-chapter edges per chapter pair (C₁ → C₂):
- Edges going *forward* (C₁.number < C₂.number): normal; blocks in early
  chapters depend on later chapters' content → **may be a problem** (forward
  reference by chapter).
- Edges going *backward* (C₁.number > C₂.number): normal; later chapters
  build on earlier ones → fine.

**Flag**: chapters with more than 10 cross-chapter forward edges.

### H3 — Cross-section coupling (severity: MEDIUM)

Same as H2 but at section granularity within a single chapter.  Report
any section pair where ≥ 3 blocks reference each other across section
boundaries.

**Ratio metric**: cross_section_edges / total_edges_in_chapter.
- Ratio < 0.20: well-structured
- 0.20–0.40: moderate coupling
- > 0.40: high coupling — restructuring likely needed

### H4 — Section too sparse (severity: LOW)

Sections with fewer than 3 content blocks (excluding intro prose) risk
fragmenting the narrative.  They are candidates for merging with an
adjacent section.

**Threshold:** < 3 non-prose blocks.
**Exception:** Intro/overview sections (first block is `prose`).

### H5 — Section too dense (severity: LOW)

Sections with more than 18 content blocks are hard to navigate.

**Threshold:** > 18 blocks.
**Suggestion:** Split along natural dependency boundaries within the
section.

### H6 — Isolated blocks (severity: LOW)

A block with no `uses[]` edges (other than prose/intro) and no block in
`uses[]` of other blocks is **isolated**.  It may belong to a different
section or chapter, or may be dead content.

### H7 — Remark / example ratio (severity: INFO)

Sections where `remark + example` blocks outnumber provable blocks
(`definition + theorem + lemma + proposition + corollary + conjecture`)
by more than 2:1 may have too much interpretation and too little formal
content — or vice versa.

## Lean 4 Subgraph Heuristics (`L1..L6` — `Process_GraphDetanglement`)

In addition to prose heuristics `H1..H7`, [`scripts/lean-kg-detangler.py`](../../scripts/lean-kg-detangler.py) and [`scripts/lean-best-practices-lint.py`](../../scripts/lean-best-practices-lint.py) enforce six Lean subgraph invariants derived from `Process_GraphDetanglement`:

### L1 — Unassigned-first completeness (severity: CRITICAL)
Every library `.lean` module and every resolved `import` edge must be classified (`unassigned_library_modules == 0`, `unassigned_resolved_edges == 0`) BEFORE evaluating cross-edge or cut-edge counts. Zero cross-edges over an unjudged subset is never read as clean.

### L2 — Strict zero-`QOU.*` boundary on Tier-A & Tier-B Reservoir libraries (severity: CRITICAL, `BP008`)
Pure-mathematics modules in Tier-A (`MathlibExt`) and the 6 Tier-B Lean Reservoir community `lean_lib` packages (`HeckeTemperleyLieb`, `TwistedFrobeniusHopf`, `ToricConicOpt`, `CompactQuantumMetrics`, `QCalculus`, `BraidKnotOctonion`) MUST have **zero** upward `import QOU.<Model>` edges into QOU physics/framework modules. Resolve any `community_to_qou_cut_edges` via the four detanglement moves: **prune** an unused import, **merge** mutually-defining helpers, **factor** the pure base definition downward, or **reclassify** a misbucketed target.

### L3 — Subgraph condensation acyclicity (severity: HIGH)
Both the module-level `import` graph and the inter-`lean_lib` condensation graph must be strictly acyclic (`0` Tarjan SCCs of size > 1; imports point monotonically toward lower architectural layers `L0 Mathlib → L1 MathlibExt/UGB → L2 QCalculus → L3 TwistedFrobeniusHopf → L4 ToricConicOpt → L5 CompactQuantumMetrics → L6 HeckeTemperleyLieb → L7 BraidKnotOctonion → L8..L15 QOU.<Chapter>`).

### L4 — Synonym-directory anti-sprawl & Open-PR Fixup (severity: CRITICAL, `BP009`)
`folio/quantum-observable-universe/lean/` is isolated under **Q3 Option 1** (`7` top-level community `[[lean_lib]]` roots + `12` canonical `QOU/<Chapter>/` subgraphs; `0` loose `QOU/*.lean` files). Never create ad-hoc synonym directories under `QOU/` or `lean/`. New pure math goes directly to `MathlibExt/` or one of the 6 Tier-B roots (see [`lean-mathlibext-curator.md`](lean-mathlibext-curator.md)); new QOU model Lean goes to `QOU/<Chapter>/`. When rebasing a pre-migration branch or open PR, run `nice -n 15 python3 scripts/apply-lean-reservoir-migration.py --fixup-branch` to relocate legacy `QOU/<OldDir>/` modules and rewrite imports/`lean.ref`s deterministically.

### L5 — §7c Base-ring & empirical wall alignment (severity: HIGH, `BP005` / `BP006`)
Tier-A/Tier-B community libraries and pre-wall chapters stay over generic `{R : Type*} [CommRing R]` / `[Field R]` / `[LinearOrderedField R]` with zero decimal literals, `Float`, `CODATA`, or `substrate_q`. Concrete `(R := ℝ)` evaluations live exclusively post-wall.

### L6 — Root & `lean.ref` reachability (severity: MEDIUM)
Every `.lean` module should be reachable either from its `lean_lib` root aggregator (`QOU.lean` / Tier-B root) or from a live `.ts` `lean.ref` / chapter sibling import (`scripts/lean-root-coverage-audit.py` + `scripts/dead-lean-pointer-audit.py`).

## Placement Principles for New/Changed Content

The heuristics above detect problems **post-hoc**. The placement
principles below are **proactive**: agents must follow them when
creating new blocks or `.lean` modules, or significantly changing existing ones.

### PR1 — Topical home chapter & canonical Lean subgraph

Every prose block belongs in the chapter whose topic it primarily addresses (matching [`quantum-observable-universe.ts`](../../folio/quantum-observable-universe/quantum-observable-universe.ts)), and every new `.lean` library module belongs either in Tier-A/Tier-B (if pure math with 0 QOU coupling) or in the paired canonical `QOU.<Subgraph>`:

| Part | Chapter directory (`folio/quantum-observable-universe/<dir>/`) | Canonical `QOU.<Subgraph>` | Primary topic scope |
|---|---|---|---|
| Front | `introduction`, `authors-note` | *(no new Lean)* | Framing motivation & contribution/open-problems note (preview chapter) |
| **I: Foundations** | `quantum-universes` | `QOU.Core` | Abstract QU axioms, fibre functors, rigid braided monoidal dagger categories |
| I | `quantum-observable-universes` | `QOU.Core` | QOU axioms, state/jet bundles, $q$-codifferentials, categorical Reeb |
| I | `models-of-qous` | `QOU.Core` / `QOU.MassTheory` | 5-step arc framing gallery, Archimedean wall (`sec:archimedean-models`), non-Archimedean models |
| I | `lifting-and-descent` | `QOU.LiftingDescent` *(pure Hopf/Sweedler → `TwistedFrobeniusHopf`)* | Yekutieli torsion lifting, descent, brane tower, Gröbner–Shirshov filtration |
| **II: Structural Mechanics** | `braids-and-knots` | `QOU.BraidsAndKnots` *(pure → `HeckeTemperleyLieb` / `BraidKnotOctonion`)* | Braid groups, Iwahori–Hecke $H_n(q)$, Temperley–Lieb, Jones–Markov trace |
| II | `brings-surface` | `QOU.BringsSurface` *(pure → `BraidKnotOctonion`)* | Bring's surface $\Sigma_4$ ($\chi = -6$), $S_5/A_5$ action, cohomological defect |
| II | `knots-particles-confinement` | `QOU.Confinement` | Knot–particle dictionary, hadron algebra, Borromean nucleons, confinement hierarchy |
| II | `eightfold-way` | `QOU.EightfoldWay` *(pure octonion/$\mathfrak{g}_2$ → `BraidKnotOctonion`)* | $A_2$ from 3-strand braiding, $\mathrm{SU}(3)$ flavour multiplets, octonionic colour |
| II | `mass-endomorphism` | `QOU.MassTheory` | Categorical mass identity, topological mass decomposition, complex volume, $\chi$-characters |
| II | `climax-volume-mass` | `QOU.MassTheory` | $q$-hyperbolic geometry, Möbius/crossing energy, Lagrange resolvents, spectral filter |
| II | `mass-theory` | `QOU.MassTheory` | Geometric & Archimedean mass pipeline across elementary particles, gauge bosons, and nuclei |
| II | `nuclear-interactions` | `QOU.Nuclear` *(pure LP/Graver → `ToricConicOpt`; pure $q$-calc → `QCalculus`)* | Many-body Gröbner–Shirshov reduction, LP/SDP operator selection, $\beta$-decay, $Q$-values |
| II | `gravity-spacetime` | `QOU.MassTheory` / `QOU.FluidDynamics` | Contact-geometric gravity emergence, geodesic Madelung bridge |
| **III: Physical Realization** | `predicted-spectra` | `QOU.StandardModel` / `QOU.MassTheory` | Fundamental fermion, meson/nucleon, atomic shell, and $\alpha_{\mathrm{EM}}$ spectra |
| III | `observations` | `QOU.Observations` | CODATA comparisons, experimental falsifiers, astrophysical/laboratory tests |
| III | `molecular-construction` | `QOU.Observations` | Molecular braids ($\mathrm{H}_2$ through benzene), stoichiometry |
| III | `organic-chemistry` | `QOU.Observations` | Covalent / Hopf-ring organic chemistry |
| **IV: Dynamics & Information** | `fluid-dynamics` | `QOU.FluidDynamics` | $q$-Navier–Stokes brane fluid dynamics, vorticity, Kelvin waves |
| IV | `stochastic-mechanics` | `QOU.FluidDynamics` | Markov-trace stochastic mechanics, Nelson/Itô diffusion |
| IV | `information-theory` | `QOU.InformationTheory` *(pure Rieffel/KR → `CompactQuantumMetrics`)* | Complexity barriers, Bekenstein/Planck horizons, CMB |
| IV | `measurement-observation` | `QOU.InformationTheory` | Internalised quantum measurement via fibre-functor behaviour |
| IV | `q-geometric-langlands` | `QOU.InformationTheory` | $q$-Geometric Langlands, Tannaka–Krein, Hasse–Weil |
| Back | `glossary`, `appendix-*`, `index-of-definitions`, `notation` | `QOU.Observations` / `QOU.Core` | Ch 8 Mathlib glossary, knot/NF/Q-value/SM/surreal/Lean-library appendices, symbol register |

If a block spans two chapters' topics, split it (see PR5).

### PR2 — Forward-reference & upward-leak avoidance

A new prose block must appear **after** all blocks it `uses[]`, and a new `.lean` module must import only same-or-lower architectural layers (`BP008`). Run `computations/forward_ref_classifier.py` (prose) and `nice -n 15 python3 scripts/lean-best-practices-lint.py --diff` + `scripts/lean-kg-detangler.py --summary-only` (Lean) after placement.

### PR3 — Section density bounds

When adding blocks to a section, check the count stays within
**3–18 blocks**.  If adding would exceed 18, split the section first
(H5).  If a removal would drop a section below 3, consider merging
(H4).

### PR4 — Cross-chapter dependency direction

New blocks should depend **backward** (on earlier chapters), not
forward.  If a new block in Ch 3 needs to use something from Ch 7,
either:
- Move the dependency to Ch 3 first, or
- Place the new block in Ch 7 instead.

### PR5 — Topic-coherent blocks

Before accepting a new block, verify it addresses a **single topic**.
If the `.md` content contains material belonging to multiple chapters,
split it into separate blocks placed in their respective chapters.
Defer to `block-density` R1 for the full audit.

### PR6 — Table extraction on creation

If a new block's `.md` contains a table with **> 5 data rows**, extract
it immediately to a `table` block (`kind: "table"`, label:
`tbl:<name>-data`).  Reference it from the parent block via `uses[]`.
Do not wait for a later audit.  See `block-density` R3 for details.

### PR7 — Reorganisation map update

After any block move, section split/merge, or directory rename, update
`docs/reorganization-map.md` with the change.  This is mandatory — it
is the downstream debugging reference for tracing broken labels and
imports.

## Placement Checklist (for agents)

When adding a new block or significantly changing an existing block:

1. □ Identify the primary topic → select home chapter (PR1)
2. □ Check `uses[]` deps appear earlier in document order (PR2)
3. □ Check target section has 3–18 blocks after insertion (PR3)
4. □ Verify no new forward cross-chapter edges (PR4)
5. □ Verify block is single-topic; split if not (PR5)
6. □ Extract tables > 5 rows to `table` blocks (PR6)
7. □ Update `docs/reorganization-map.md` if anything moved (PR7)
8. □ Run `python3 pipeline/content-graph-analysis.py` to confirm

## Workflow

### Step 1 — Parse the content tree

Read the paper manifest `quantum-observable-universe.ts` to enumerate
chapters.  For each chapter, read its manifest to enumerate sections and
their block lists.  Assign each block a document position
`(chapter_number, section_index, block_index)`.

For each block `.ts` file, extract:
- `label`, `kind`, `uses[]`, `interprets`, `proofs[]`, `examples[]`

### Step 2 — Build the block graph

Build an adjacency map:
```python
edges[(from_label, to_label)] = edge_type  # "uses"|"interprets"|"proof"|"example"
```

Index every block's document position:
```python
position[label] = (chapter_no, section_idx, block_idx)
```

### Step 3 — Build the chapter/section graph

For each chapter pair (C₁, C₂) count directed edges from blocks in C₁
to blocks in C₂:
```python
chapter_edges[(c1_num, c2_num)] += 1
```

For each section pair within the same chapter, count cross-section edges:
```python
section_edges[(s1_label, s2_label)] += 1
```

### Step 4 — Apply heuristics

Run each heuristic (H1–H7) and collect findings.  Each finding has:
- `severity`: HIGH / MEDIUM / LOW / INFO
- `heuristic`: H1–H7
- `description`: human-readable explanation
- `blocks`: list of involved block labels
- `suggestion`: proposed action

### Step 5 — Generate visualisations

Two DOT/SVG outputs (via Graphviz):

**5a. Chapter/section graph** (`/tmp/content_chapter_graph.svg`)
- Nodes: chapters (large boxes) containing sections (small boxes)
- Edges: weighted directed arrows between sections
- Color: red = forward cross-chapter edges, orange = high cross-section
  coupling, gray = normal backward dependencies

**5b. Block graph heat-map** (`/tmp/content_block_heatmap.svg`)
- Nodes: blocks (grouped by chapter/section in clusters)
- Edges: forward references only (red), cross-chapter edges (orange)
- Isolated blocks highlighted in yellow

### Step 6 — Report findings

Print a ranked report (HIGH → LOW → INFO):

```
## Content Graph Analysis: quantum-observable-universe

### Summary
- Total blocks: N  |  Chapters: N  |  Sections: N
- Total block edges: N (uses/interprets/proof/example)
- Cross-chapter edges: N  |  Cross-section edges: N
- Forward references: N

### HIGH — Forward References (H1)
- block A (ch1/sec2) uses block B (ch3/sec5) ← B defined later
  Suggestion: move B earlier, or add stub to ch1

### MEDIUM — Cross-Chapter Coupling (H2)
- Ch4 → Ch1: 14 forward edges  ← Ch4 blocks depend on Ch1
  Top offending blocks: ...

### LOW — Sparse Sections (H4)
- sec:my-section (Ch3): 2 non-prose blocks
  Suggestion: merge with adjacent sec:other-section

### LOW — Dense Sections (H5)
- sec:hadrons-knot-composites (Ch4): 20 blocks
  Suggestion: split into "Hadron operations" + "Quark structure"
```

### Step 7 — Interactive suggestions

After the report, offer the user a numbered menu of actions they can
approve:

```
What would you like to do?
[1] Move block X from sec:A to sec:B
[2] Split sec:large-section into two sections
[3] Add a new section "Preliminaries" in Ch3 to absorb forward refs
[4] Merge sec:sparse-1 and sec:sparse-2
[5] Show detailed block graph for chapter N
[6] Re-run analysis after changes
[0] Done
```

For each approved action, make the minimal changes to the `.ts` manifest
files.

### Step 8 — Implement approved moves

For a block move (action [1]):
1. Remove the block name from `blocks[]` in its current section.
2. Add the block name to `blocks[]` in the target section at the
   correct position (after its `uses[]` dependencies).
3. Re-run the analysis to confirm improvement.

For a section split (action [2]):
1. Ask the user to name the two new sections and choose a split point.
2. Rewrite the chapter manifest with two `section({...})` entries.
3. Move blocks to the correct new section.

For a section merge (action [4]):
1. Combine the two `blocks[]` arrays in document order.
2. Remove the merged-away section from the chapter manifest.

Always show a before/after energy comparison:
```
Before: energy=142, backward_edges=12, sparse_sections=3
After:  energy=87,  backward_edges=4,  sparse_sections=1
```

## Python CLI Tools (Prose + Lean KG)

1. **Lean 4 Module & Reservoir Subgraph Detangler (`L1..L6`):**
   - [`scripts/lean-kg-detangler.py`](../../scripts/lean-kg-detangler.py) (`< 15s` deterministic analyzer across all ~4,750 `.lean` files)
   - [`scripts/lean-best-practices-lint.py`](../../scripts/lean-best-practices-lint.py) (`--diff` and `--package` Mathlib4/Reservoir linter)
   ```bash
   export LEAN_NUM_THREADS=1 RAYON_NUM_THREADS=1 OMP_NUM_THREADS=1 \
          OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1

   # Concise DAG + Reservoir cut-edge summary:
   nice -n 15 python3 scripts/lean-kg-detangler.py --summary-only

   # Regenerate full JSON-LD + Markdown architecture options audit:
   nice -n 15 python3 scripts/lean-kg-detangler.py \
     --json-out docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-audit.json \
     --md-out docs/audits/2026-11-23-lean-kg-detangler-and-reservoir-options.md

   # Lint branch .lean changes for upward leaks (BP008) and synonym-dir sprawl (BP009):
   nice -n 15 python3 scripts/lean-best-practices-lint.py --diff
   ```

2. **Prose Forward-Reference Classifier & Manifest Validator:**
   - [`computations/forward_ref_classifier.py`](../../computations/forward_ref_classifier.py) (`logical` vs `storytelling` vs `structural` forward-ref discriminator)
   - [`scripts/run-validate.ts`](../../scripts/run-validate.ts) & [`folio/pipeline/block-manifest-audit.ts`](../../folio/pipeline/block-manifest-audit.ts)
   ```bash
   nice -n 15 python3 computations/forward_ref_classifier.py
   nice -n 15 bun run scripts/run-validate.ts
   ```

### Proposal kinds (--proposals output)

| Kind | Description | Trigger |
|------|-------------|---------|
| `split` | Split a dense section (> 18 blocks) along natural comment boundaries | H5 |
| `merge` | Merge two adjacent sparse sections (< 3 non-prose blocks each) | H4 |
| `move` | Move a block that is forward-referenced by ≥ 3 earlier blocks | H1 |
| `reverse` | Fix an `interprets`/`example` block that appears before its target | H1 |

Each proposal includes:
- A unique ID (`P1`, `P2`, …) for stable reference
- Exact chapter manifest path and section labels to edit
- Concrete `blocks[]` array changes to make
- Expected forward-reference reduction

### Implemented reorganisations (tracking)

The following reorganisations have been applied to the paper manifests:

| ID | Kind | Description | Status |
|----|------|-------------|--------|
| R1 | move | `sec:fivefold-symmetry` + `sec:orbital-space` from Ch2 → Ch9 (Descartes) | ✅ done |
| R2 | merge | 4 single-block sparse sections → `sec:non-archimedean-models` in Models | ✅ done |
| R3 | merge | `sec:jones-polynomials` (1 block) merged into `sec:finite-fields` in Models | ✅ done |
| R4 | split | `sec:descartes-particles` (84 blocks) → 5 sections of 17–25 blocks in Descartes | ✅ done |
| R5 | rename | Remove `ch#-` prefix from all chapter directory names | ✅ done |
| R6 | auto-number | Chapter numbers derived from manifest order, not stored in manifests | ✅ done |
| P1 | split | `sec:vertex-operators-markov` (19 blocks) → 4 sections in Braids and Knots | ✅ done |
| P2 | split | `sec:hadrons-knot-composites` (20 blocks) → 3 sections in Braids and Knots | ✅ done |
| P4 | split | `sec:brane-fluid` (19 blocks) → 3 sections in Fluid Dynamics | ✅ done |
| P5 | split | `sec:brings-geometry` (31 blocks) → 4 sections in Descartes Universe | ✅ done |
| P8 | split | `sec:small-scale` (21 blocks) → 3 sections in Observations | ✅ done |
| P9 | merge | `sec:orbital-space` + `sec:fivefold-symmetry` → `sec:orbital-symmetry-embedding` in Descartes | ✅ done |

### Chapter naming convention (R5/R6)

Directory names are **descriptive slugs** with NO chapter numbers:
- `introduction/`, `quantum-universes/`, `braids-and-knots/`, etc.
- The paper manifest `chapters[]` array defines the chapter order
- Chapter numbers are auto-derived: numbered chapters get sequential 1, 2, 3…
- Chapters with `tabLabel` set (e.g. `"I"`, `"G"`) are unnumbered (`\chapter*{}`)
- To reorder chapters: just reorder lines in the paper manifest — no renames needed

**Key functions:**
- `parse_paper(root)` → `{chapters, sections, blocks, positions}`
- `build_block_graph(blocks)` → `{nodes, edges}`
- `build_section_graph(blocks, positions)` → `{chapter_edges, section_edges}`
- `apply_heuristics(graph, positions)` → `[Finding]`
- `generate_proposals(...)` → `[Proposal]` (split/merge/move/reverse)
- `generate_dot_chapter(graph)` → SVG path
- `generate_dot_blocks(graph)` → SVG path
- `report(findings)` → formatted text

## Integration with other skills

| After this skill | Use next |
|-----------------|----------|
| Block moves approved | `content-validation` — verify schema integrity |
| Forward refs identified | `chapter-complexity-review` — block-level reorder within chapter |
| Cross-chapter coupling found | `critical-path-analysis` — trace logical dependency chain |
| Sparse sections found | `editor` — add missing content blocks |
| Dense sections found | `content-block-review` — audit individual blocks for splitting |
| Proposals generated | Approve with user, then implement via manifest edits + re-run |
| New content proposed | Run placement checklist (PR1–PR7) before accepting |
| Block too long / multi-topic | `block-density` — single-topic coherence audit |
| Large table found in block | `block-density` R3 — extract to `table` block |
| Feature branch ready to merge | `/prepare-merge` (slash command) — upstream check + placement + density + one-voice |

## Output artefacts

| File | Purpose |
|------|---------|
| `/tmp/content_chapter_graph.svg` | Section-level topology |
| `/tmp/content_block_heatmap.svg` | Block-level dependency heat-map |
| `/tmp/content-graph.json` | Machine-readable graph export |
| `/tmp/content-graph-report.md` | Full analysis report |
| `/tmp/content-graph-proposals.md` | Concrete reorganisation proposals |
