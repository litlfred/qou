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
def BringsSurface : Type* := sorry
```

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

## Checklist

- [ ] Every definition in `chapters/*.tex` has a glossary entry
- [ ] No unresolved ambiguities in `glossary.json`
- [ ] `Glossary.lean` compiles without errors (sorry warnings OK)
- [ ] `mapping.json` covers all `\lean{}` macros in LaTeX
- [ ] Category-theoretic types have correct universe annotations
- [ ] Docstrings in `Glossary.lean` match narrative definitions
