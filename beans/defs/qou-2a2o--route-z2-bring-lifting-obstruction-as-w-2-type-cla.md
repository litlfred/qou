---
# qou-2a2o
title: 'Route Z/2: Bring lifting obstruction as w_2-type class (centre of SU(2))'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T19:30:20Z
updated_at: 2026-11-24T03:25:23Z
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

## 2026-11-21 (bean-drain sibling bring-gerbe-ns, session_01Qmmkt6JCxoNkQcgaG1tFNF, issue #8808)

Superseded-premise check (owner, 2026-11-21: photon L±, virtual photons, old γγ letters, T(2,n_s), convention C, single-term trace, trefoil electron, c_2 = −1, χ₍₂,₁₎ = 2 − h⁴, fitted α/CODATA in proofs, project memory): none found in this bean; its subject is surface topology / gerbes / NS and touches none of them.
Open PR #8150 (Antigravity, 'ready' since 2026-11-16, mergeable clean) carries this bean's Lean. Re-verified here: BringLiftingObstructionRoutes.lean lean-direct exit 0, no sorry; probe re-run 12/12 assertions pass, no float literals or float() in it (precision-gates.sh could not resolve a merge base in a shallow clone, so the gate itself was not run). Caveat for review: the declarations are integer arithmetic named as cohomology (mod2StiefelWhitney e := e % 2, tangentW2 g := (2 − 2g) % 2). This is the lemma qou-lx8f (2026-10-12) deliberately declined to add, and PNeqNpEquivalence.chi_mod_vanishes_iff already covers the arithmetic. '136 % 5 = 1' does not prove a unique S₅-fixed even theta characteristic. The PR also bundles unrelated Hecke MTC (S,T) data. The bean's real next step, identifying WHICH principal bundle the tower lifts, is untouched. Merge decision raised to the coordinator.

## 2026-11-22 applicability review (wave-2 sibling bring-riemann-gerbes, session_01Qmmkt7Jw9nSDCzSdsd8hLX)

APPLIES. Premises checked against owner-rulings.md on origin/main (all rows to 2026-11-22: photon with fixed constant 1, γγ linking neutrality, derived quark charges, potential-energy sign, m_p = m_n at q = 1, gluon open, electron σ₀σ₁σ₀ with T(2,n) as backup, S₅ two-test rule, T(A) tangent algebra) and git log on the Lean/content paths since the last update. Unchanged since 2026-11-21. The real next step (which principal bundle the tower lifts) is still untouched; '136 % 5 = 1' still does not prove a unique S₅-fixed even theta characteristic.

BringThetaCharacteristicsSymplectic.lean (08dfe533aaa) + 80-dps witness (ef51559461b) prove exact Sp(8,F_2) spin uniqueness & true BDH orbits [1,5,5,5,10,10,10,30,30,30] / [20,20,20,60]; #8150 flagged DO-NOT-MERGE.
