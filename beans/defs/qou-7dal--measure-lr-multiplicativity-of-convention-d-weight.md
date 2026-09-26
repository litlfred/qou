---
# qou-7dal
title: 'Measure: LR-multiplicativity of convention-D weights at H_6; block measure + entangled support for D/T/3He/4He from committed witnesses'
status: completed
type: task
priority: normal
created_at: 2026-09-16T01:38:59Z
updated_at: 2026-09-16T01:53:38Z
parent: qou-qt8b
---

## 2026-09-16 — measured, 7/7, committed data only

computations/probes/branching_pushforward_entangled_support_probe.py. (H2) LR weight identity Σ_λ y_λ c^λ_{μν} = y_μ y_ν for all 9 pairs μ,ν ⊢ 3 at (3,3)→6, worst |dev| 5.1e-51 (convention D, proton pin). (H1) branching rule on the committed deuteron free characters vs the LR pushforward of chi-proton/neutron-h3: worst 7.2e-50. tr_M(p) = 0.6293284022, tr_M(n) = 0.4751335172. Per nucleus: Σ y f = 1 at n = 6, 9, 12; y-weighted entangled support = the two-row support (4 / 5 / 5 / 7 blocks for D / T / 3He / 4He); tr(free) = tr(p)^Z tr(n)^N to 1e-40 for all four; weighted deviation Δ = tr(atom) − tr(free): D −0.1470 ((5,1) −0.1109 dominant), T −0.1129, 3He −0.1296 (both led by (8,1), (7,2), (6,3), (5,4) — same support and order, different magnitudes), 4He −0.0782 ((11,1), (8,4), (9,3), (10,2)). LR table self-checked by f^μ f^ν C(6,3) = Σ c f^λ. LR coefficients at A ≥ 3 are NOT tabulated here (would need S_9 ⊃ S_3^3); the A=3/4 factorisation checks use the traces only.


## 2026-09-16 — extended to 10/10: bond product corroborated; reading 3 FAILS on every production bound nucleus

(BF) tr(atom)/tr(free) = ∏_{interfaces}(z_D + d_kind) to ≤ 9e-51 for D (pn), T (pn, nn), 3He (pp, pn), 4He (pp, pn, nn) with z_D = 0.61268803715, d_pn = −0.10445824777 (bring_color_weighted), d_nn = −h — corroborates the_intra_ordering_moves_absolute_traces_not_the_bond_model_probe's ~1e-60 finding; so the y-weighted deviation total Σ y δ = tr(free)(∏(z+d) − 1) is fixed by the interface letters. (R3) owner-ruled whole-word reading 3 (χ_λ ≥ 0 on y>0 blocks): the FREE products pass on all four; the BOUND production words fail — D on (5,1) [χ = −0.682], T and 3He on (8,1) and (5,4), 4He on (11,1) and (8,4). Same shape as the nuc11_interleaved rejection on (2,1) (qou-99qc), one confinement level up. Committed data only (atom-chi-rust-*, y-lambda-at-q0, chi-proton/neutron-h3).
