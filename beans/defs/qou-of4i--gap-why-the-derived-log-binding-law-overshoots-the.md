---
# qou-of4i
title: 'GAP: why the derived log binding law overshoots the deuteron by +27.4% under convention D (E_0 scale vs p-n letter weight)'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T11:23:57Z
updated_at: 2026-11-25T16:24:42Z
parent: qou-s028
---

Owner ruling 2026-11-25 ('3y sibling'), relayed by parent session. Derivation only; choosing d_pn or E_0 to hit AME is a fit and is forbidden. Two candidate loci per docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md §10b: (a) E_0 as the nucleon-nucleon interface scale; (b) the p-n interface weight (1/2 - delta/4). Context bean qou-xj4p, PR #9421. Child session of the qou-xj4p session.

## 2026-11-25 findings (PR #9424, branch claude/deuteron-overshoot-loci-2026-11-25)
- The +27.4% is on the single-crossing letter that the 2026-11-15 gg ruling supersedes. On the ruled gg chain word the deuteron is UNBOUND (mu_pn = 1.000611191 > 1; LightNucleiGGChainSign.lean, sorry-free; audit 2026-11-22-light-nuclei-a2-a3-gg-chain). The live question is binding at all (qou-brng).
- (a) Live producer uses order-zero E0 4.18598, not the ruled tower form 4.22748 (+28.62% with it). Lean UniversalScaleMinimax: one universal scale cannot do better than (r2-r1)/(r1+r2); floors 23.93% (2H-3H), 61.17% (2H-4He). E0 as the NN scale is NOT derived (qou-91w7, qou-y3bm).
- (b) (1/2 - delta/4) is asserted. Derived alternatives overshoot more: 1/[2]_q +31.45%, T=0 mu- = 1/[2]_q^2 +162.9%. Only bare sigma undershoots (-7.82%).
Stays open: the loci are scope-(a) negatives on the old letter; the deuteron on the ruled word is open (qou-brng). Owner decision pending: align binding_log_free_energy.py to qbeta_e0.canonical()?

## 2026-11-25 locus (a) closed on the corpus premises; Lean verified
BondScaleUniversality.lean: trace-only energy forces one scale (a·log x + b·log y = G(xy) => a=b). With route T (spectator audit §8-9) the common scale is k_BT = E0 (order zero). So on those premises an NN-specific scale is excluded; the locus is mu (the bond word). UniversalScaleMinimax.lean: minimax floor (r2-r1)/(r1+r2). Both lean-direct exit 0, standard axioms. Precision gates green. PR #9424.
Still open (do not close; the deuteron on the ruled gg word is open in qou-brng): owner decision on order-zero vs tower E0 in binding_log_free_energy.py.

## 2026-11-25 owner ruling 'A ruled tower' applied (commit f1c5d61db, PR #9424)
binding_log_free_energy.py + probe_d_dressing_is_proton_net.py + probe_d_dressing_cross_a.py now use qbeta_e0.tower_summed_scaled (new). E0 4.185981 -> 4.227483 MeV (+0.9915%). Log-law binding: 2H 2.83316->2.86125 (+28.62%), 3H 6.6309->6.6967, 3He 4.8839->4.9323, 4He 8.6817->8.7677. Probe-d E0*h*net(p) ansatz 0.78365->0.79142 MeV (vs Kashiwara Q_beta 0.107%->1.10%); probe-d binding negative -75.22%->-74.98%. Baselined on_scale assertion unchanged (already false). Precision gates --changed: NEW 0. NOT switched (outside named scope): forced_link_normalisation_bond_counting, cyclic_triple_under_log_law, normalised_law_residual_shape, surface_exponent_is_dimension probes (own order-zero E0).
