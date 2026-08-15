---
# qou-e4ri
title: '§7c push: HeckeAlgebra/Torsion/AlgebraicSubstrate cluster (JonesMarkovWenzl, YekutieliTriple, quantum_dilogarithm, QVonMangoldtFunction, QChebyshevFunction, WedderburnBlockDecomposition) to generic R'
status: todo
type: task
priority: normal
created_at: 2026-08-01T23:07:47Z
updated_at: 2026-08-15T14:51:23Z
---

## Content-based triage (2026-08-15) — criteria for whoever picks this up

Ran the **canonical folio-assistant checkers** (`wall-side-correct`, `wall-base-ring-minimal`, `q-usage-positivity-implicit` + q-regime detection) over this cluster — the same content-based, chapter-INDEPENDENT trio `q-usage-audit`'s orphan pass uses. **No path heuristics** (§7c: never infer the regime from the lean-tree directory).

`codeℝ` counts ℝ in code with comments/docstrings stripped, so docstring prose is not miscounted as a type. It is a heuristic count: a CANDIDATE is a **lead, not a verdict** — each still needs per-file adjudication (is the statement algebraic yet typed over ℝ?) plus a compile via `scripts/lean-direct-cone.sh`. Do NOT mass-fix from this table.

| file | codeℝ | generic | banner | baseRing | verdict |
|---|---|---|---|---|---|
| `JonesMarkovWenzl` | 26 | n | n | warn | **CANDIDATE** — largest in cluster |
| `YekutieliTriple` | 11 | n | n | warn | **CANDIDATE** |
| `quantum_dilogarithm` | 10 | n | n | pass | **CANDIDATE** — dilog is classically archimedean; adjudicate carefully |
| `QVonMangoldtFunction` | 3 | n | Y | pass | ℝ-typed **with** §7c banner — adjudicate |
| `QChebyshevFunction` | 5 | n | n | pass | **CANDIDATE** |
| `WedderburnBlockDecomposition` | 0 | Y | Y | warn | **DONE** — `(R : Type*) [Field R]`; the ~15-extender restructure `z1lz` deferred has since landed |

1 of 6 already done. Note the dilog files were flagged in the 2026-06-25 audit as *legitimately* archimedean — do not assume CANDIDATE means bug.
