---
# qou-82w7
title: 'GAP: c3 carrier S=c3+Vol(4_1) — z(q0) argument map is transcendental, not combinatorial'
status: todo
type: task
created_at: 2026-08-01T01:23:31Z
updated_at: 2026-08-01T01:23:31Z
---


## Status (2026-08-01)

The tetraplectic → combinatorics **structural** reduction of the c₃ Faddeev
integral is DONE and sorry-free (`QOU/QBeta/EkParitySplit.lean`; probe
`computations/qbeta/qbeta_c3_barodd_tetraplectic_reduction_probe.py`). The exact
coefficient closed form is now also pinned: `e_k(q,q³,…) = q^{k²}/(q²;q²)_k`
(Lean backbone `QOU/QBeta/TetraplecticProductRecurrence.lean`; witness
`computations/qbeta/qbeta_ek_qpochhammer_closed_form.witness.json`, k≤6).

**What remains OPEN is NOT combinatorial.** Reproducing the c₃ carrier
`S = c₃ + Vol(4₁)` (muon S=+0.00968, proton S=−0.03946, sign flip, ratio ≈ −4.08)
requires the **argument map z(q₀)** = meridian holonomy m(q₀) that feeds the
combinatorial e_k. Audit `docs/audits/2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`
proved this link is **near-singular** (`dc₃/dq ≈ 4.7×10⁶`) and a **smooth
deformation is excluded** (predicts ratio ≈ 1.0 vs measured −4.08) — it is a
transcendental root-of-unity accumulation (PR #3458's z→c_k evaluation map), not a
combinatorial/algebraic object. Do NOT attempt to close S via the reduction; the
reduction supplies the *coefficients*, not the *argument*.

## Update (2026-08-01, PRs #4452 + #4457 merged)

The candidate space for the argument map is further narrowed **by proof**:

- **Real-seed class excluded, scope-(b)** (`QOU/QBeta/NewtonRealityInvariance.lean`,
  sorry-free): real Newton seeds of EITHER sign have all-real iterates and can
  never converge to the cusp `e^{iπ/3}`. Covers the literal Φ_q-pole seed and
  its negative.
- **Pole-sign principal-branch family excluded, scope-(a)**
  (`computations/qbeta/qbeta_c3_pole_sign_complexification_probe.py`, 4/4):
  `u_k = iπ − (2k+1)log q₀` is anchor-blind for every k (sign boundary
  `(2k+1) = π/log q₀ ≈ 30.109` crossed by no odd integer between anchors).
  Near-k=15 magnitude dip is a flagged numerological trap — do not chase it.
- **Surviving constraint composition** (audit
  `docs/audits/2026-08-01-qbeta-c3-pole-sign-reality-exclusion.md`): the phase
  is strictly interior, `0 < |arg m²| < π`, and must cross the diagonal
  `|Re u| = |Im u|` at the root-found q* with the anchor inversion targets
  `(Re²u−Im²u) = +0.0224` (muon) / `−0.0911` (proton). Geometric backbone:
  `docs/scope/2026-08-01-reeb-tetraplectic-cs-threeform-identification.md`
  (Reeb ⌟ tetraplectic → CS face).
