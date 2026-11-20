---
# qou-cds5
title: 'S5 (SCIENCE): verify the r* D-frame band BEFORE re-scoring the six Delta_lambda ansaetze'
status: todo
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-11-20T16:06:50Z
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


---

## Round 48 Execution Update — Step 1 Resolved (2026-11-16, PR #8181)

- **PR:** https://github.com/litlfred/qou/pull/8181 (`e3a0c2e1773d8a4bc1635ead95154cb8d9babb4d`)
- **Lean 4 Formalisation (`0` `sorry`, `0` `axiom`, wired into `QOU.lean`):**
  - `folio/quantum-observable-universe/lean/QOU/MassTheory/DeltaLambdaRStarConventionD.lean`
    - `rStarCabled_cross_decreases_while_door_increases`
    - `pr4766_door_scaled_band_provenance`
    - `rStar_convention_D_outside_pr4766_band`
    - `rBoth_convention_D_overshoots_all_targets`
- **Probe & 50-dps Witness:**
  - `computations/probes/spin_orbit_magic_rstar_mirror_probe.py`
  - `computations/probes/spin-orbit-magic-rstar-mirror-probe.witness.json`
- **Step 1 Resolution Summary:**
  1. **Provenance of `[2.04, 2.16]`:** PR #4766 (`docs/audits/2026-08-08-binding-channel-convention-exposure.md`, opened 2026-08-08 and merged 2026-08-25, ten days after the 2026-08-15 ruling doc) measured the **uncabled pairwise supermodularity door** `c₃^door = -E₀(χ_ab - χ_a - χ_b + χ_∅)` (`-1.768775 MeV` for `³H`, `-1.405424 MeV` for `³He` under C; `-1.372331 MeV` for `³H`, `-1.033836 MeV` for `³He` under D), giving C-to-D door ratios `1.288883` (`³H`) and `1.359427` (`³He`). Multiplying the cabled-Borromean C-frame ratio `r*_C = 1.585412` by those uncabled door ratios produced `[2.043411, 2.155251] ≈ [2.04, 2.16]`.
  2. **Direct 50-dps Convention-D measurement of the `#4364` cabled-Borromean cluster `c₃^cabled(y_λ) = E₀(g₀ - g_B)`:**
     - On the `#4364` `grouped` word: `c₃^cabled` increases from `0.296958 MeV` (C) to `0.303867 MeV` (D), so `r*_D(grouped) = 0.4708 / 0.303867 = 1.549361` (per-isotope `[1.414661, 1.712412]`), moving **down** by `-2.27%` (strictly below `[2.04, 2.16]`).
     - On the canonical `borromean` word (`qou-hu1f`): `c₃^cabled(D) = 0.191529 MeV`, giving `r*_D(borromean) = 2.458116` (per-isotope `[2.213893, 2.762901]`, strictly above `[2.04, 2.16]`).
  3. **Fate of `r_both` and the six `Δ_λ` ansaetze:** Under Convention D, `∑_λ y_λ^D = 0.062025` is `1.953×` larger than `∑_λ y_λ^C = 0.031752`, so `r_both^D = r_geom^D · ∑_λ y_λ^D = 2.871237` overshoots `r*_D(grouped) = 1.549361` by `+85.32%` (refuting the C-frame `1.504 vs 1.585` near-miss as a normalization artifact). None of the six pruned `Δ_λ` ansaetze is rescued.
- **Status:** Kept at `in-progress` pending owner review and PR merge.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8181, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
