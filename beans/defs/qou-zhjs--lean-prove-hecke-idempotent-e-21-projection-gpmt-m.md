---
# qou-zhjs
title: Lean-prove Hecke idempotent e_(2,1) projection & GPMT modified quantum dimension trace on H₃(q) nucleon weight spaces
status: in-progress
type: task
priority: high
tags:
    - lean
    - convention-d
created_at: 2026-11-18T19:52:23Z
updated_at: 2026-11-18T19:52:23Z
parent: qou-7xl8
---

In `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/NucleonIdempotentModifiedTrace.lean` (importing `QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder` and `QOU.Machinery.MarkovTraceOnHecke` over generic `[Field R]`):
1. Prove the orthogonal idempotent decomposition `1 = e_(3) + e_(2,1)` on the 3-dimensional weight spaces `(2,1)` and `(1,2)` using `FEp_sector` and `EFn_sector` (`e_(3) = [3]_q⁻¹ • FE`, `e_(2,1) = 1 - [3]_q⁻¹ • FE`), verifying `e_(3)² = e_(3)`, `e_(2,1)² = e_(2,1)`, `e_(3) * e_(2,1) = 0`, and that both commute with `A₁, A₂` / `B₁, B₂` (`[aiston-morton-1997]`, `[hadji-morton-2009]`).
2. Prove the Jucys-Murphy and full-twist content eigenvalues on the symmetric `e_(3)` (`I=3/2` Δ-decuplet) vs mixed-symmetry `e_(2,1)` (`I=1/2` nucleon) sectors.
3. Formalize the Convention-D Wedderburn trace decomposition `tr_D = w_(3)(z_D) χ_(3) + w_(2,1)(z_D) χ_(2,1) + 0 · χ_(1³)` and the Geer-Patureau-Mirand-Turaev (`[geer-patureau-mirand-turaev-2009]`, `[geer-patureau-mirand-turaev-2013]`) first-order modified trace `t_(1³) = d/dz|_{z=z_D} tr_z` on the killed `(1³)` ideal.
