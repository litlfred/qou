---
# qou-q0gw
title: 'α-decay Q_α: split inherited binding-slope error from α-specific (B_α, preformation)'
status: in-progress
type: task
priority: high
tags:
    - compute-accuracy
    - alpha-decay
created_at: 2026-11-27T19:46:04Z
updated_at: 2026-11-27T20:36:29Z
parent: qou-myts
---

Accuracy-scorecard vector 5 (α-decay): derived Q_α is 585 % off (median 320 %) on 1,051 emitters; WKB half-lives at Q_exp are 0.35 dex. Goal: derive, no fitting; separate what Q_α inherits from the binding term (qou-brng / C2) from what is α-specific.

## Finding 1 (2026-11-27, probe computations/probes/alpha_qalpha_inheritance/)
Q_α = B_α − ΔB, ΔB = B(Z,N) − B(Z−2,N−2) (Lean QOU.Nuclear.AlphaQInheritance, sorry-free, generic CommRing).
- Production mass table (mass-table-comprehensive, Q-CLT −8G m_e Σ ln|V|) has ONE alpha-line slope on all 1,051 pairs: ΔB_pred = 9.5366 MeV (2.384 MeV/nucleon). So Q_pred is a single number for every emitter and carries no information about which nuclei α-decay.
- Error split at medians: total +15.08 MeV = α-cluster +1.03 (M3a B_α 29.33 vs 28.30) + inherited +14.05 (ΔB 9.54 vs 23.59). Median row-wise inherited share 93 %.
- Model mixing: the scorecard pairs the M3a K4 ⁴He with the Q-CLT chain parent/daughter. The chain's own ⁴He (B(8Be) − ΔB = 6.84 MeV) gives Q_α = −2.70 MeV for every nucleus (no α emitters at all). Neither pairing is self-consistent; the 585 % number measures the mixture.
- Target for the binding term (comparison only, not an input): with the derived Coulomb slope ΔE_C (Form-B α_q, CAL-3 r0_FCC; median 34.82 MeV), the nuclear α-line slope must be ≈ 57.86 MeV = 14.47 MeV/nucleon (median). This is a sharp number for qou-brng / C2 in place of "A ≥ 5 underbound ~69 %".

## α-specific remainder
- B_α: M3a 29.33, 64 m_e G 29.96, AME 28.30 (+3.6 % / +5.9 %).
- WKB: open-shell 0.14–0.89 dex at Q_exp, ²¹⁰Po closed by Mayer–Jensen S_α = 1/20 (+0.044 dex). Open-shell S_α = 1 is an assumption, not derived.

## Next
1. Report the split to C2 / B1 threads; Q_α accuracy waits on the binding slope (inherited, not α work).
2. Scorecard: show Q_α with a self-consistent B_α (same model for parent, daughter, α), label the current row as mixed.
3. Derive open-shell preformation (seniority overlap for 2g9/2, 1i11/2...) with the same Mayer–Jensen rule as ²¹⁰Po; record if it worsens the fit.


## 2026-11-27 update
- Scorecard relabel: PR #9672. The mixed rows are labelled, and a chain-only row gives Q_alpha = -2.70 MeV for every nucleus (0/1051 exothermic).
- Preformation bound (Lean AlphaPreformationBound, sorry-free): since 0<S<=1, T = T_WKB/S >= T_WKB. Of the 7 bare-WKB emitters, 4 cannot be closed by any preformation (8Be, 222Rn, 226Ra, 238U, S_req 7.7/1.39/1.55/2.54). Their miss is on the barrier side: Q, radius or deformation. 3 can be closed (212Po S_req 0.447, 214Po 0.726, 210Po 0.0553, the last already matched by MJ 1/20).
- Scope (a) negative: reading the 210Po Mayer-Jensen rule literally for 212Po/214Po gives S=0.01 and dex +1.65/+1.86. That is worse than bare WKB. Open-shell pair coherence is missing from the counting rule.
- Still open: a derived open-shell (coherent-pair) preformation for 212Po/214Po, and the barrier-side miss for the deformed actinides.
