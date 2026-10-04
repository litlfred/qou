---
# qou-cds5
title: 'S5 (SCIENCE): verify the r* D-frame band BEFORE re-scoring the six Delta_lambda ansaetze'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-10-04T15:15:06Z
parent: qou-v2om
---

Parent: `qou-cdx1`. **This bean exists to stop a re-scoring that has not earned
its target yet.**

## The claim, as relayed — NOT independently confirmed

Relayed into the ruling session: `r* ≈ 1.585` is a **convention-C** number, and
**PR #4766** measured **2.04–2.16 under D**; the **six Δ_λ closure ansätze** were
all tested against the C value.

**I could not locate the #4766 D-frame band in the tree** while writing
[`2026-08-15-owner-ruling-convention-d-proton-color.md`](../docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md).
It is recorded there as relayed, explicitly not as a corpus measurement. **Step 1
of this bean is to confirm or refute it.**

## What IS in-corpus

`r*` as the needed ratio in the A3-magnitude work:

- `docs/audits/2026-07-26-deltalambda-a3-magnitude-source-three-walls.md:32,39,48`
  — `r = κ_W/κ_y`; route closes iff derived `r = μ₃/v_y ≈ 1.585`. Derived
  `r = 52.6` vs needed `1.585` — overshoots by the wrong *order*.
- `docs/audits/2026-07-27-deltalambda-s5so3-geometric-wlambda.md:35,74,86,91`
  — `r_geom = 47.369`; `r_both = r_geom·Σy_λ = 47.37·0.03175 = 1.504`, recorded
  as *"a tantalizing 5.1 % short of r* ≈ 1.585"*.

## Why this matters, if the relay holds

`r_both = 1.504` is **5.1 % short of a C-frame target**. Under D the target
moves, and a "tantalizing near-miss" either becomes a hit, a miss, or a
different miss. The six ansätze were scored against the same moving target.

**Do not re-run the ansätze against a number nobody has re-measured.** That is
how a fit gets laundered into a derivation — score against an unverified target,
find the one ansatz that lands, and call it closure.

## Standing constraints that do not move

- The Δ_λ **value** is PROVED (`Δ_λ = (−1)^{n(λ)}·dim V_λ`,
  `dtEuler_eq_deltaLambda_unconditional`, sorry-free, general-n). What is open is
  the many-body binding **MAGNITUDE**.
- **No seventh fit-based ansatz for the magnitude.**
- PROBE-4 (Kashiwara-crystal / KL-weight) stays **pruned** — KL positivity vs a
  mixed-sign target, Lean-proved (`PartitionOf5.deltaSign_mixed`). That is a
  proved exclusion, not a scope gate.
- The gate is **open for all** (2026-07-13) for *derivation* routes; the
  anti-fit discipline is orthogonal and unchanged.
