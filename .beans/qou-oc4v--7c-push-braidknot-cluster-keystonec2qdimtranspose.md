---
# qou-oc4v
title: '§7c push: BraidKnot cluster (KeystoneC2QDimTranspose, DepthStratifiedFrobeniusReciprocity, knot_mass_unified, hoefsmit_*, KnotFactor*, QBetaWenzlDecomposition, six_term_mass_formula) to generic R'
status: todo
type: task
priority: normal
created_at: 2026-08-01T23:07:46Z
updated_at: 2026-08-15T14:51:23Z
---

## Content-based triage (2026-08-15) — criteria for whoever picks this up

Ran the **canonical folio-assistant checkers** (`wall-side-correct`, `wall-base-ring-minimal`, `q-usage-positivity-implicit` + q-regime detection) over this cluster — the same content-based, chapter-INDEPENDENT trio `q-usage-audit`'s orphan pass uses. **No path heuristics** (§7c: never infer the regime from the lean-tree directory).

`codeℝ` counts ℝ in code with comments/docstrings stripped, so docstring prose is not miscounted as a type. It is a heuristic count: a CANDIDATE is a **lead, not a verdict** — each still needs per-file adjudication (is the statement algebraic yet typed over ℝ?) plus a compile via `scripts/lean-direct-cone.sh`. Do NOT mass-fix from this table.

| file | codeℝ | generic | banner | wall | verdict |
|---|---|---|---|---|---|
| `KeystoneC2QDimTranspose` | 6 | n | n | pass | **CANDIDATE** |
| `DepthStratifiedFrobeniusReciprocity` | 5 | Y | Y | **fail** | **MIXED** — generic + archimedean in one file; review split per §7c |
| `knot_mass_unified` | 0 | Y | Y | pass | **DONE** — `(R : Type*) [AddCommGroup R]`, no code ℝ |
| `QBetaWenzlDecomposition` | 9 | n | n | pass | **CANDIDATE** |

`hoefsmit_*` / `KnotFactor*` / `six_term_mass_formula` from the title were not resolved to single files — enumerate before starting. 1 of the named files is already done.
