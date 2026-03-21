---
name: ontologist
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

## Lean MCP Tools (lean-lsp-mcp)

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
The `key` must match an entry in `references.bib` exactly.
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
4. **BibTeX references**: Every `-- Ref: [key]` in Glossary.lean must match
   a `references.bib` entry; when adding new glossary terms, identify the
   foundational paper and add it to `references.bib` if absent

## Checklist

- [ ] Every definition in `chapters/*.tex` has a glossary entry
- [ ] No unresolved ambiguities in `glossary.json`
- [ ] `Glossary.lean` compiles without errors (sorry warnings OK)
- [ ] `mapping.json` covers all `\lean{}` macros in LaTeX
- [ ] Category-theoretic types have correct universe annotations
- [ ] Docstrings in `Glossary.lean` match narrative definitions
- [ ] Every `sorry` in `Glossary.lean` has a `-- Ref: [key] url` comment
- [ ] All `-- Ref:` keys exist in `references.bib`
- [ ] `blueprint/src/content.tex` has entries for all glossary definitions
- [ ] `\uses{}` edges in blueprint are bidirectionally valid
