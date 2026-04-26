---
name: ontologist
roles: [collaborator, owner]
description: >
  Semantic Ontologist — scans narrative mathematical text for ambiguous terms,
  generates a formal Glossary.lean registry, and produces mapping.json linking
  narrative strings to Lean identifiers.  Acts as the "Gatekeeper" ensuring
  every term has a unique type assignment before formalization proceeds.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Semantic Ontologist (Ambiguity Detection & Glossary)

## Overview

This skill acts as the **Gatekeeper** for mathematical definitions.  Before
any narrative-to-Lean translation can proceed, every mathematical term must
have a unique type assignment in the Lean type system.  The Ontologist
detects ambiguities, maintains the formal glossary, and produces the
machine-readable mapping file.

## Lean MCP Tools (paper-assistant)

When the MCP server is available, **prefer MCP tools for type checking**:

| Old workflow | MCP tool | Why better |
|-------------|----------|-----------|
| `lake build` for type mismatches | `lean_diagnostic_messages` | Structured error messages per file |
| Manual type checking | `lean_hover_info` | Hover over any symbol to see its resolved type |
| Finding existing definitions | `lean_local_search` | Search project + stdlib for a term |
| Checking if a type exists in Mathlib | `lean_leansearch` / `lean_loogle` | "TopologicalGroup" → exact Mathlib location |
| Finding where a type is declared | `lean_declaration_file` | Jump to source of any symbol |
| Import path guessing | `lean_completions` | Auto-complete `import Mathlib.` paths |

### MCP-enhanced consistency loop

When `lean_diagnostic_messages` reports a type mismatch:

1. **`lean_hover_info`** on the mismatched symbol → see expected vs actual type
2. **`lean_leansearch`** for the intended type → find correct Mathlib import
3. **`lean_declaration_file`** → read the actual definition to understand the mismatch
4. Update `glossary.json` with the corrected type assignment
5. Regenerate `Glossary.lean` and re-check with `lean_diagnostic_messages`

## When to Use This Skill

- When new mathematical terms or definitions are added to chapter files
- When `lake build` fails due to type mismatches (consistency loop)
- When the Formalizer skill reports an unresolved term
- When reviewing LaTeX changes that introduce new notation
- Before running the Formalizer on any chapter

## Workflow

### 1. Scan narrative text for terms

```bash
PYTHONPATH=.github/scripts python .github/scripts/ontologist.py scan
```

Parses `chapters/*.tex` for definitions, symbols, and terms.  Outputs
candidates to `glossary.json`.

### 2. Detect ambiguities

The scanner flags terms that lack a unique type assignment:

**Trigger phrases** (require disambiguation):
- "The mapping" — without specifying domain/codomain types
- "The space" — without specifying `TopologicalSpace`, `SmoothManifold`, or `Scheme`
- "Smoothness" — without specifying the manifold/domain
- "The group" — without specifying `Group`, `TopologicalGroup`, or `LieGroup`
- Bare symbols like `M`, `X`, `G` without type annotation

**Action**: Interrupt the pipeline and request a **Type Assignment**.

### 3. Generate Glossary.lean

```bash
PYTHONPATH=.github/scripts python .github/scripts/ontologist.py generate-lean
```

Produces `lean/QOU/Glossary.lean` with:
- Each term as a `def`, `class`, or `constant`
- Lean docstrings (`/-- ... -/`) containing the original narrative definition
- Universe annotations for category-theoretic types

### 4. Generate mapping.json

```bash
PYTHONPATH=.github/scripts python .github/scripts/ontologist.py generate-mapping
```

Produces `mapping.json` linking narrative strings to Lean identifiers.

## Glossary Structure

Each entry in `Glossary.lean` follows this pattern:

```lean
/-- **Bring's Surface**: The maximally symmetric CR manifold of genus 4,
    with Euler characteristic χ = −6, defined by Σ x_j^k = 0 for k = 1,2,3.

    LaTeX: `chapters/brings-surface.tex:12` (`\label{def:brings-surface}`)
    Mathlib: `Mathlib.Geometry.Manifold.SmoothManifoldWithCorners` -/
-- Ref: [atiyah1988] https://doi.org/10.1007/BF02698547
def BringsSurface : Type* := sorry
```

### Bibliographic reference requirement

Every `sorry` in `Glossary.lean` **must** be preceded by a
`-- Ref: [key] url` comment linking to the foundational reference.
The `key` must match a citation key in `content/schema/references.ts` exactly.
(`references.bib` is auto-generated from this file — never edit `.bib` directly.)
This is enforced by the `axiom_report.py` Theoretical Gap Report.

## Category Theory Universe Requirements

The glossary must track universe levels for category-theoretic types:

| Narrative Concept     | Lean Formalization        | Universe Requirement           |
|-----------------------|---------------------------|--------------------------------|
| Category C            | `Category.{v, u} C`      | Objects in `u`, Homs in `v`    |
| Small Category        | `SmallCategory C`         | Both in same universe          |
| Abelian Category      | `Abelian C`               | Requires `Preadditive`, `HasLimits` |
| Monoidal Category     | `MonoidalCategory C`      | Requires `Category` instance   |
| Rigid Monoidal        | `RigidCategory C`         | Requires `MonoidalCategory`    |

## Ambiguity Resolution Format

### Standing disambiguation rulings (v2, 2026-03-29)

The following terms have been resolved by the author.  Agents MUST
apply these rulings when scanning narrative text:

| Term | Ruling | Notes |
|------|--------|-------|
| **energy** (bare) | Replace with `κ` (Hecke cost) | Ban bare "energy"; always use κ(ξ), or qualify as binding/kinetic/crossing |
| **crossing** | OK unqualified | Both "braid crossing" and "nuclear crossing" are just "crossing" — the context is unambiguous in this paper |
| **shell** | Always "orbital shell" | Qualify by occupancy λ and degree [n], NOT by who occupies it. Use `𝔖_ℓ` for the formal object |
| **trace** | Two traces only: **categorical** and **Markov** | (1) **Categorical trace** (the Frobenius pairing ∫_A). The terms "descended trace," "transient trace," and "Frobenius trace" are just the categorical trace restricted to parts of the bundle — NOT separate traces. Use "categorical trace of the descended part" etc. (2) **Markov trace** tr_M (braid/knot invariant on H_n(q)). Bare "trace" OK when context is clear. |
| **dimension** | Always qualify | Quantum dimension d_λ(q), Hausdorff dimension d_H, categorical dim, topological dim — always say which |
| **volume** | Always qualify | Hyperbolic Vol(K), traced volume V̂, categorical volume, physical volume — always say which |
| **force** | Transfer matrix IS the force operator | Interactions are described by transfer matrices. No separate "force" concept. Newton's equations = transfer matrix composition |
| **numerical values** | Never `=` for observed values; always `≈` | Write `g_A ≈ 1.275` not `g_A = 1.275`. Exception: `=` is OK when accompanied by `O(ε)` or `± δ` error bounds. Algebraic identities (over ℤ[q,q⁻¹]) use `=`. Numerical evaluations at q₀ use `≈`. |
| **state** | OK unqualified | Not ambiguous in context |
| **particle** | Always "knot-particle" or use 𝒦 | A particle IS a knot equivalence class 𝒦_x; always make this explicit |
| **𝔈_{anything}** | BANNED | Use κ (Hecke cost) or specific qualified term. Fraktur E is banned in v2 notation |
| **T_{m,n}** for torus knot | BANNED | Use τ(r,s) for torus knot label; T is for transfer matrices only |
| **bar notation** on 𝒩 | BANNED | 𝒩_{Z,N} is assumed in Gröbner normal form; mark 𝒩^{unred} if unreduced |

### Ground ring ruling

All formal proofs over ℤ[q, q⁻¹].  Modules over ℝ or ℂ are the
archimedean realisation (Chapter 7 only) and NOT part of the formal
proof chain.  See `content/quantum-observable-universe/lean/QOU/GroundRingAnnotations.lean`.

When an ambiguity is detected, the Ontologist outputs:

```json
{
  "narrative_term": "The space M",
  "ambiguity": {
    "is_ambiguous": true,
    "message": "M is used as both a topological space and a smooth manifold",
    "candidates": ["TopologicalSpace M", "SmoothManifold M", "Scheme M"],
    "resolved_to": null
  }
}
```

The pipeline **halts** until `resolved_to` is filled.

## Consistency Loop

If `lake build` fails:
1. Parse the error log for type mismatch messages
2. Identify which glossary entries are involved
3. Flag those entries as ambiguous in `glossary.json`
4. Re-run the scan with the error context

## Output Files

| File | Purpose |
|------|---------|
| `glossary.json` | Machine-readable glossary with ambiguity flags |
| `lean/QOU/Glossary.lean` | Lean file with formal definitions |
| `mapping.json` | Narrative-to-Lean identifier mapping |

## Blueprint Integration

Every glossary entry that has a `\label{}` in a chapter file must also
appear in `blueprint/src/content.tex` with the matching `\lean{}`
macro.  The Ontologist is responsible for ensuring:

1. **Label consistency**: `\label{def:foo}` in chapters = `\label{def:foo}` in blueprint
2. **Declaration consistency**: `\lean{QOU.Glossary.Foo}` in blueprint = `def Foo` in `Glossary.lean`
3. **Dependency edges**: `\uses{}` in the blueprint must reference only labels
   that exist and whose glossary entries are resolved (not ambiguous)
4. **Bibliography references**: Every `-- Ref: [key]` in Glossary.lean must match
   a citation key in `content/schema/references.ts`; when adding new glossary terms,
   identify the foundational paper and add a `ref()` entry in `content/schema/references.ts`
   (then run `bun run export-bibtex` to regenerate `references.bib`)

## Content Object Integration

Glossary terms should link to **content object labels**. Each `definition`
block in `content/` has a `.ts` manifest with a `label` (prefix `def:`)
and a `.md` file containing the narrative definition.

**Glossary–content object linkage.** When scanning for terms:
- Definitions in `.md` blocks should reference glossary entries by their
  `lean_name` and include cross-refs using `[term](#def:label)` format.
- New glossary entries should record the content object `label` they
  originate from, ensuring bidirectional traceability.
- The `lean.ref` URI in a definition's `.ts` manifest should match the
  corresponding `Glossary.lean` declaration name (parse via
  `parseLeanRef()` from `folio-assistant/schemas/lean-packages.ts`).

**Content object triples.** Each definition is a `.ts` + `.md` + `.lean`
triple. The `.ts` manifest is authoritative for the `kind`, `label`, and
`lean.ref`. When the Ontologist detects a new term in a `.md` file, it
should check whether a content object already exists before creating a
glossary entry, to avoid duplication.

## Glossary Block Policy (Chapter 8)

Chapter 8 ("Glossary of Rigid Monoidal Terms") contains **glossary blocks**
— `remark` blocks with tag `"glossary"` — that map paper terminology to
canonical Mathlib declarations. These are the content-object counterpart
of `glossary.json` entries.

### When to use a glossary block vs. a definition block

| Criterion | Glossary block (`remark`) | Definition block |
|-----------|--------------------------|------------------|
| Semantic novelty | **None** — the term is a synonym or light wrapper for a Mathlib type | The paper introduces genuinely new mathematics |
| Example | "$R$-linear category" → `CategoryTheory.Linear R` | "Quantum universe" (new structure with custom axioms) |
| Lean file | Not required | **Required** |
| Label prefix | `rem:glossary-<term>` | `def:<term>` |
| Chapter | Ch 8 (Glossary) | Relevant content chapter |

### Decision tree for new terms

1. **Does the term exist in Mathlib under a different name?**
   → Glossary block. Map paper name to Mathlib name.
2. **Is it a lightweight restriction/specialization of a Mathlib type?**
   → Glossary block with a note about the restriction.
3. **Does the paper add new axioms, fields, or structure?**
   → Definition block in the relevant chapter.
4. **Ambiguous?** → Ask the author.

### Glossary block structure

Each glossary block is a `.ts` + `.md` pair in `glossary/`:

```typescript
// glossary-<term>.ts
import { remark } from "../../schema/builders";
export default remark({
  label: "rem:glossary-<term>",
  title: "<Human-readable term>",
  tags: ["glossary", "category-theory", ...],
  uses: [],   // other glossary entries this depends on
});
```

```markdown
<!-- glossary-<term>.md -->
**<Term>.** <1–3 sentence definition as used in the paper.>

**Mathlib reference.**
`<Fully.Qualified.Mathlib.Name>` (<class|structure|def>).
Import: `<Mathlib.Import.Path>`.
<Optional: notation, key fields, relationship to paper's usage.>
```

### TeX snippet validation (mandatory after creating .md)

After creating any glossary `.md` file, validate its TeX snippets:

```bash
cd content && bun run pipeline/validate-tex.ts --file <path-to-new.md>
```

This uses **remark + remark-math** to parse the markdown and validate all
inline/display math and fenced TeX blocks via **unified-latex** AST parsing.
Fix any TeX errors before committing.

### Maintaining consistency

- When a new Mathlib-equivalent term appears in any chapter `.md`,
  check Ch 8 for an existing glossary entry before creating a definition.
- When `glossary.json` is regenerated, cross-check against Ch 8 entries.
- The `chapter-analysis` skill's glossary gap analysis should include
  Ch 8 glossary blocks in its coverage check.

## Checklist

- [ ] Every definition in `chapters/*.tex` has a glossary entry
- [ ] No unresolved ambiguities in `glossary.json`
- [ ] `Glossary.lean` compiles without errors (sorry warnings OK)
- [ ] `mapping.json` covers all `\lean{}` macros in LaTeX
- [ ] Category-theoretic types have correct universe annotations
- [ ] Docstrings in `Glossary.lean` match narrative definitions
- [ ] Every `sorry` in `Glossary.lean` has a `-- Ref: [key] url` comment
- [ ] All `-- Ref:` keys exist in `content/schema/references.ts`
- [ ] `blueprint/src/content.tex` has entries for all glossary definitions
- [ ] `\uses{}` edges in blueprint are bidirectionally valid
