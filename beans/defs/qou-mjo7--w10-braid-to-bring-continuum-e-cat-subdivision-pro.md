---
# qou-mjo7
title: W10 Braid-to-Bring Continuum E_cat Subdivision, Proton (k=-3,2,12) & Intra-Nucleon m_d-m_u
status: completed
type: task
priority: high
created_at: 2026-11-23T20:54:28Z
updated_at: 2026-11-23T22:14:15Z
parent: qou-qzvs
blocked_by:
    - qou-pzsi
    - qou-37y0
    - qou-17mq
---

L2 `1-ppQ` Workstream Package `Q-Gap-6` under `qou-qzvs` (also cross-linked with `qou-sm8w`).

- **Linked Beans:** `qou-pzsi`, `qou-37y0`, `qou-17mq`
- **Scope:** Construct the braid-to-Bring curve map and continuum `E_cat` subdivision, derive the structural integers `(k = -3, 2, 12)` in the proton identity, and evaluate intra-nucleon `ΔE_EM(p - n)` via even `μ̄₁₂₃² = 1` and neutralized `H³` Green's function to extract `m_d - m_u` (`0` fits, ≥80 dps `mpmath`).

Claimed by claude/w10-continuum-ecat-intranuc-em-20261123 (Worker 18, 2026-11-23)

Lean formalization QOU/QBeta/ContinuumECatIntraNucleonEM.lean compiled sorry-free and custom-axiom-free (24 theorems, 0 vacuity advisories) in 406133dcc7c.

EOS 2026-11-23 (PR #9219, issue #9218, HEAD 23ab7c141ec): Completed W10 / Q-Gap-6 + L_cal Route-1 package. (1) Lean QOU/QBeta/ContinuumECatIntraNucleonEM.lean (24 theorems, 0 sorry, 0 custom axioms, 0 vacuity advisories, §7c generic, zero empirical literals). (2) Pre-registered 80-dps probe & witness (11/11 assertions, probe-float64-guard clean): verified N=16..256 E_cat subdivision Richardson/Shanks convergence < 10^-12 (1.43e-17 box, 1.83e-55 S^1), non-circular q_mu grid selection of (k1,k2,k3)=(-3,2,12) at -243.86 ppb, and all 11 pre-registered L_cal Route-1 (no m_pi) Borromean/3-strand shape factors f (f_R1_1a=1/9 -> Delta_EM=0.76077 MeV, m_d-m_u=2.0541 MeV; f_R1_1c=1/6 -> Delta_EM=1.14116 MeV, m_d-m_u=2.4345 MeV; f_R1_3a..c Compton-HO -> 0.386-0.580 MeV; O(hbar_q^4) Hecke trace f_R1_3d -> 0.00295 MeV).
