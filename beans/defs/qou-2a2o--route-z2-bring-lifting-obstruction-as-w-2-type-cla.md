---
# qou-2a2o
title: 'Route Z/2: Bring lifting obstruction as w_2-type class (centre of SU(2))'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:30:20Z
updated_at: 2026-11-16T18:35:00Z
parent: qou-vo9t
---

Route 1 of qou-lx8f (owner, 2026-10-12: pursue the Z/2 and Z readings in parallel, final band deferred).

**Reading.** The band is the centre Z/2 of SU(2), and the lift is SU(2) -> SO(3) (or Spin(2) -> SO(2) for a frame). The obstruction is a w_2-type bit in H^2(Sigma_4, Z/2) = Z/2.

**Next honest step.**
1. Identify WHICH principal bundle on Bring the tower lifts. Corpus candidates: the frame bundle, "SU_q(2) frame bundles" (archimedean-lifting-intro.md), and Z(Aut A_n) (brings-is-qou-proof.md).
2. For the tangent frame, w_2 = chi mod 2 = 0, so it lifts (Bring is spin; 2^8 theta characteristics, a unique S_5-invariant one per bean qou-9l0d).

**Lean.** T1 (QOU.CentralExtension) gives the group-level criterion. Instantiating it with Z/2 -> SU(2) -> SO(3) needs those groups as Mathlib GroupExtension values. Mathlib has no Stiefel-Whitney classes, so the sheaf-level statement waits on T2-T4.

**Consequence if adopted.** The `persistence` / perpetual-obstruction claims are false on Bring for the frame bundle.

## Progress (2026-11-16, PR `litlfred/qou#8150` — `status: in-progress`)
- **Lean 4 formalization (`0` `sorry`, `0` custom axioms):** Added `folio/quantum-observable-universe/lean/QOU/Brings/BringLiftingObstructionRoutes.lean` (wired into `QOU.lean`, verified with Lean v4.24.0 `-DautoImplicit=false`), proving:
  - `w2_tangent_vanishes_all_genera`: for every closed orientable genus-`g` surface `Σ_g`, `χ(Σ_g) = 2 - 2g` is even so `w₂(TΣ_g) = (2 - 2g) % 2 = 0` vanishes identically (in particular at Bring's curve `g = 4`, `χ(Σ₄) = -6` and `w₂(TΣ₄) = 0`, `bring_w2_tangent_zero`), whereas odd-degree circle bundles `d = 2k + 1` (such as the Hopf bundle `d = -1`) have `w₂(2k + 1) = 1 ≠ 0` (`w2_odd_degree_bundle_one`).
  - `theta_characteristic_partition` and `bring_theta_counts_and_s5_orbits`: proves `N₊(g) + N₋(g) = 2^(2g)` and `N₊(g) - N₋(g) = 2^g` for all `g ≥ 1`, and at `g = 4` certifies `256 = 136 + 120`, `136 - 120 = 16`, `136 % 5 = 1` (`136 = 1 + 15 + 60 + 60`, unique `S₅`-fixed even spin structure), and `120 = |S₅| = 60 + 60` (`qou-9l0d`).
- **50-dps / Exact Probe + Witness:** `computations/probes/bring_lifting_obstruction_routes_z2_vs_z_probe.py` and `.witness.json` (12/12 assertions passed).
