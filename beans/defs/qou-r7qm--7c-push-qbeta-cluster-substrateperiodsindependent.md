---
# qou-r7qm
title: '§7c push: QBeta cluster (SubstratePeriodsIndependent, OhtsukiTowerBarParity, PeriodLatticeBasis) to generic R'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:07:47Z
updated_at: 2026-11-17T06:35:30Z
parent: qou-rtxm
---

## Content-based triage (2026-08-15) — criteria for whoever picks this up

Ran the **canonical folio-assistant checkers** (`wall-side-correct`, `wall-base-ring-minimal`, `q-usage-positivity-implicit` + q-regime detection) over this cluster — the same content-based, chapter-INDEPENDENT trio `q-usage-audit`'s orphan pass uses. **No path heuristics** (§7c: never infer the regime from the lean-tree directory).

`codeℝ` counts ℝ in code with comments/docstrings stripped, so docstring prose is not miscounted as a type. It is a heuristic count: a CANDIDATE is a **lead, not a verdict** — each still needs per-file adjudication (is the statement algebraic yet typed over ℝ?) plus a compile via `scripts/lean-direct-cone.sh`. Do NOT mass-fix from this table.

| file | codeℝ | generic | banner | baseRing | verdict |
|---|---|---|---|---|---|
| `SubstratePeriodsIndependent` | 1 | n | Y | warn | ℝ-typed **with** §7c banner — adjudicate (1 hit only) |
| `OhtsukiTowerBarParity` | 8 | n | Y | pass | ℝ-typed **with** §7c banner — adjudicate |
| `PeriodLatticeBasis` | 0 | n | n | warn | **DONE-ish** — no code ℝ; not parameterised over R |

Smallest cluster and the best entry point: 1 file already ℝ-free, one with a single ℝ hit. Both banner'd files may be legitimately archimedean — read the banner before porting.

## 2026-11-17 — §7c Generic-Ring QBeta Cluster Foundations (`litlfred/qou#8227`)
- Formalized `ohtsuki_tower_bar_parity_products`, `period_lattice_cramer_first`, and `substrate_period_first_coeff_eq_zero` over generic `CommRingOps R` / `InvolutionRingOps R` (zero `ℝ` occurrences) in `folio/quantum-observable-universe/lean/QOU/Foundations/Zeta4GenericRingPlancherel.lean` (wired into `QOU.lean`, `0` `sorry`, `0` warnings, `0` vacuity advisories, commit `6ea0f626b6fd6e4a73ad6fb742931324e3efe377`, PR [https://github.com/litlfred/qou/pull/8227](https://github.com/litlfred/qou/pull/8227)).
- Kept `status: in-progress` per no-unilateral-closure policy.
