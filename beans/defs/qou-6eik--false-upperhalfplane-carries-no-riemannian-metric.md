---
# qou-6eik
title: 'FALSE: "UpperHalfPlane carries no Riemannian metric" — Mathlib Metric.lean gives ℍ the hyperbolic metric + isometries (2 sites: HyperbolicVolumeMeasure.lean:12 and bean qou-5gai)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-09-04T09:08:24Z
updated_at: 2026-10-04T15:14:50Z
parent: qou-n4nr
---

**FALSE CLAIM — two sites, one sentence, one edit pass.**

**Site A — `QOU/Archimedean/HyperbolicVolumeMeasure.lean:12-13`:**

> "that one hit is the **2-dimensional modular-forms** upper half plane — a complex
> domain with an `SL₂` action, carrying **no Riemannian metric, no volume form, no
> geodesics**."

**Site B — bean `qou-5gai`** (the epic governing the whole H1-H5 hyperbolic tier plan),
same sentence verbatim, followed by *"So the gap is total, not partial."*

**One of the three is false.** Measured 2026-09-04 against the pinned mathlib
`f897ebcf72cd16f89ab4577d0c826cd14afaafc7`:
`Mathlib/Analysis/Complex/UpperHalfPlane/Metric.lean` is **341 lines** and gives ℍ

* `instance : Dist ℍ` with
  `dist_eq : dist z w = 2 * arsinh (dist (z:ℂ) w / (2 * √(z.im * w.im)))` — the Poincaré
  distance, i.e. the hyperbolic metric;
* `metricSpaceAux : MetricSpace ℍ`, `cosh_dist`, `sinh_half_dist`, `tanh_half_dist`;
* hyperbolic `center z r` and ball comparisons;
* the isometries `isometry_real_vadd`, `isometry_pos_mul`, `isometry_vertical_line`, and
  **`ModularGroup.S` acting by isometries** (`Metric.lean:324`).

Alongside: `Manifold.lean` gives `ChartedSpace ℂ ℍ` + `IsManifold 𝓘(ℂ) ω ℍ`;
`MoebiusAction.lean` (389 lines) the `GL(2,ℝ)⁺` / `SL(2,R)` actions.

"No volume form" and "no geodesics" **hold** (no measure on ℍ;
`grep -rln 'geodesic' Mathlib/` returns two unrelated combinatorics files).

**The irony is sharp and worth keeping in the fix.** `ModularGroup.S` is *inversion* —
the very generator `HyperbolicVolumeMeasure.lean` names, twenty lines further down
(55-60), as the one missing from its own `H³` isometry work.

**The corpus already knows.** Sibling bean `qou-b84o` (2026-08-31) says:
*"`Mathlib/Analysis/Complex/UpperHalfPlane/` is the 2-dimensional hyperbolic plane, built
for modular forms — **`Metric.lean` gives it the hyperbolic metric**, and nothing extends
to `ℍ³`."* Two beans, opposite claims, the correct one newer and quieter.

**Corrected form (both sites):**

> "…carrying the hyperbolic **metric** (`Metric.lean`: `Dist ℍ`, `dist_eq`,
> `isometry_real_vadd` / `isometry_pos_mul` / `ModularGroup.S`) and a
> `ChartedSpace ℂ` / `IsManifold` structure, but **no volume measure and no geodesics** —
> and in dimension **two**, which is what makes it not a route to `H³`."

**The verdict does not change.** The dimension argument is the real one and survives
intact; `qou-5gai`'s tier plan H1-H5 stands. What must go is "no Riemannian metric" and
the "total, not partial" gloss, which overstate a correct conclusion with a wrong reason.

Also worth deleting: the `Analysis/Complex only` line at
`HyperbolicVolumeMeasure.lean:9` presents a *directory location* as if it were evidence
about content. It is not.

Source: `docs/audits/2026-09-04-mathlib-infrastructure-inventory.md` §F1, §F2, §H1.

## Progress Update (PR litlfred/qou#8231)
- **Status**: `in-progress` (awaiting PR merge)
- **PR**: https://github.com/litlfred/qou/pull/8231 (`513987e80ae041a6d8bc835ffbdda5371ccac289`, scriptCommitSha `9bd895c1b028c3d1abf67e3de52aeade9e9e5ccc`)
- **Summary**: Added `integral_Ioi_hemisphere_diff` and `integral_Ioi_hemisphere_strict_mono` in `QOU/Archimedean/HyperbolicVolumeMeasure.lean`, verified by 80-dps mpmath probe `hyperbolic_planck_oneloop_qint_dilog_probe.py` (`scriptHash: 83d59661279d`).
