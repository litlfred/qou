---
name: lean-generation
description: >
  Extract theorem-like objects from LaTeX source and generate corresponding
  Lean 4 stub files with `sorry` placeholders.  Maintains the proof-objects.json
  manifest linking LaTeX labels to Lean declarations by doc-gen4 URL.
allowed-tools: Read Write Edit Bash Grep Glob
---

# Lean File Generation

## Overview

This skill covers the pipeline from LaTeX mathematical content to Lean 4
formalization stubs.  It bridges the gap between human-readable proofs in
the manuscript and machine-checkable formal proofs.

## When to Use This Skill

- When new theorem/definition/lemma environments are added to chapter files
- When running the proof object extraction pipeline
- When generating or updating Lean stub files
- When adding `\lean{}`, `\leanok`, or `\uses{}` macros to LaTeX

## Workflow

### 1. Extract proof objects from LaTeX

```bash
python .github/scripts/extract_proof_objects.py
```

This parses all `chapters/*.tex` files for `\begin{theorem}`, `\begin{definition}`,
etc. and outputs `proof-objects.json`.

### 2. Generate Lean stubs

```bash
python .github/scripts/generate_lean_stubs.py
```

Reads `proof-objects.json` and appends `sorry`-based stubs to the appropriate
`lean/QOU/*.lean` files.

### 3. Add LeanBlueprint macros to LaTeX

After generating stubs, annotate the LaTeX source with:

```latex
\begin{theorem}\label{thm:my-result}
  \lean{QOU.Chapter.my_result}
  \uses{def:prerequisite}
  Statement here.
\end{theorem}
```

Add `\leanok` once the Lean proof is complete (no `sorry`).

### 4. Update proof status after Lean build

```bash
cd lean && lake build 2>&1 | python ../.github/scripts/update_proof_status.py
```

## Naming Conventions

| LaTeX label | Lean declaration |
|-------------|-----------------|
| `thm:lifting-exists` | `QOU.Torsion.lifting_exists` |
| `def:quantum-connection` | `QOU.QuantumObservableUniverse.quantum_connection` |
| `lem:torsion-skew` | `QOU.Torsion.torsion_skew` |

Rules:
- Hyphens become underscores
- The Lean namespace matches the chapter module
- Fully qualified name = `QOU.<Chapter>.<snake_case_name>`

## Lean Project Structure

```
lean/
├── lakefile.lean        ← Lake build configuration (depends on mathlib4)
├── lean-toolchain       ← Lean version pin
├── QOU.lean             ← Root import file
└── QOU/
    ├── Basic.lean       ← Shared foundations
    ├── QuantumObservableUniverse.lean  ← Chapter 1
    ├── Elaboration.lean               ← Chapter 2
    └── ...              ← One per chapter
```

## Linking to mathlib4

When a Lean declaration corresponds to an existing mathlib result:
1. Add it to the `mathlib_links` array in `proof-objects.json`
2. In the Lean file, import the relevant mathlib module
3. Use `mathlib_links` in the `lean` field of the proof object:

```json
{
  "lean": {
    "decl": "QOU.Torsion.lifting_exists",
    "url": "https://litlfred.github.io/qou/lean/QOU/Torsion.html#QOU.Torsion.lifting_exists",
    "mathlib_links": ["Mathlib.Topology.FiberBundle.Basic"]
  }
}
```

## Output Format

The `proof-objects.json` manifest follows the schema at
`schemas/proof-objects.schema.json`.  Lean declarations are referenced by
their doc-gen4 URL — the Lean data model is **not** duplicated in JSON.

## Checklist

- [ ] All labeled theorem-like environments are in `proof-objects.json`
- [ ] Every object with `formalization_status != "not_started"` has a `lean.decl`
- [ ] Lean files compile without errors (sorry warnings are expected)
- [ ] `\lean{}` macros in LaTeX match the Lean declaration names exactly
- [ ] `\uses{}` macros capture all mathematical dependencies
