---
# qou-xbyp
title: '§7c push: Mass/AtomicMass cluster (MagicNumbersFromQ, PaddedShapeLevelRational, RogersSzegoInhabited, TauQuantumIntegerForm, mass_categorical_descent) to generic R'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:07:46Z
updated_at: 2026-11-17T06:35:30Z
parent: qou-rtxm
---

## Content-based triage (2026-08-15) — criteria for whoever picks this up

Ran the **canonical folio-assistant checkers** (`wall-side-correct`, `wall-base-ring-minimal`, `q-usage-positivity-implicit` + q-regime detection) over this cluster — the same content-based, chapter-INDEPENDENT trio `q-usage-audit`'s orphan pass uses. **No path heuristics** (§7c: never infer the regime from the lean-tree directory).

`codeℝ` counts ℝ in code with comments/docstrings stripped, so docstring prose is not miscounted as a type. It is a heuristic count: a CANDIDATE is a **lead, not a verdict** — each still needs per-file adjudication (is the statement algebraic yet typed over ℝ?) plus a compile via `scripts/lean-direct-cone.sh`. Do NOT mass-fix from this table.

| file | codeℝ | generic | banner | verdict |
|---|---|---|---|---|
| `MagicNumbersFromQ` | 24 | n | n | **CANDIDATE** — but regimes=[fixed-q0,real-positive] → likely legitimately archimedean (CODATA/mass domain) |
| `PaddedShapeLevelRational` | 17 | n | Y | ℝ-typed **with** §7c banner — adjudicate |
| `RogersSzegoInhabited` | 8 | n | n | **CANDIDATE** |
| `TauQuantumIntegerForm` | 0 | Y | Y | **DONE** — the original #2782 §7c bug; confirmed generic-R, zero code ℝ |
| `mass_categorical_descent` | 9 | n | n | **CANDIDATE** |

⚠ This is the **mass/atomic-mass** domain — the chapter profile expects `real-positive`/`fixed-q0`. A high ℝ count here is *expected and often correct*; this cluster has the highest false-positive risk of the four. Adjudicate against the chapter regime, not the raw count.

## 2026-11-17 — §7c Generic-Ring Mass/AtomicMass Cluster Foundations (`litlfred/qou#8227`)
- Formalized `rogersSzegoStep_at_one`, `rogersSzego_H2_identity`, and `mass_categorical_descent_telescope` over generic `CommRingOps R` (zero `ℝ` occurrences) in `folio/quantum-observable-universe/lean/QOU/Foundations/Zeta4GenericRingPlancherel.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `6ea0f626b6fd6e4a73ad6fb742931324e3efe377`, PR [https://github.com/litlfred/qou/pull/8227](https://github.com/litlfred/qou/pull/8227)).
- Kept `status: in-progress` per no-unilateral-closure policy.
