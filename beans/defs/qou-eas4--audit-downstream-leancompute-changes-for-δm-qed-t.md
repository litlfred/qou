---
# qou-eas4
title: Audit downstream Lean/compute changes for Δm_QED two-term tracking and test impact on the 211 ppb μ–p anchor tension & 1ppQ c_k/d_k ladders
status: completed
type: task
priority: high
tags:
    - compute
    - 1ppq
    - audit
created_at: 2026-11-18T19:52:24Z
updated_at: 2026-11-18T20:19:51Z
parent: qou-7xl8
---

1. Audit every downstream Lean file, content block (`.md`/`.ts`), and Python producer/witness in `folio/quantum-observable-universe/` and `computations/` affected by separating `m_N = m_N^QCD + m_N^QED` and `Δm_np = Δm_QCD + Δm_QED`:
   - `observations/neutron-proton-mass-splitting.{lean,md,ts}` and `mass-theory/neutron-proton-splitting.{md,ts}`,
   - `mass-theory/isospin-mass-split-em-localisation.{md,ts}` (`³H - ³He`),
   - `computations/canonical_mass.py`, `computations/m_p_substrate_identity_50dps.py`, `tools/qou-substrate/python/qou_substrate/constants.py` (`_solve_q_proton_f64`),
   - `computations/qbeta/` (`q_beta_predicted.py`, `qbeta_utils.py`, `c_k` ladder under Convention D),
   - `docs/coordination/1ppq-qbeta.md` and `docs/coordination/ck-dk-canonical-registry.md`.
2. Run a pre-registered 50-dps `mpmath`/`sympy` probe (`computations/probes/np_two_term_qed_mup_tension_probe.py`) that tracks `Δm_QED` and `M_p^QED` from the derived `α_EM(q)` and the 3-strand charge operators (`QSelf`, `QPair`, `Q12`, `Q23`, Cottingham self-energy) all the way through:
   - What does separating `M_p^QED` do to the proton-pinned `q₀` and the `211 ppb` `μ–p` consistency tension (`m_μ/m_e = Vol(4₁)/ℏ_q²` vs `m_p/m_e`)?
   - What does separating `Δm_QED` do to `Δm_np` and `Q_β = Δm_np - m_e` under Convention D (`z_D = q³/(q²+1)`) and the `c_3` cross-anchor swing?
3. Write a comprehensive audit document `docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md` with the exact workplan and Lean/compute migration table.



## Completion Record (2026-11-18)
- **50-dps Probe:** `folio/quantum-observable-universe/computations/probes/np_two_term_qed_mup_tension_probe.py` (mirrored at `computations/probes/np_two_term_qed_mup_tension_probe.py`)
- **Audit & Sequenced Workplan:** `docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md`
- **Key Findings:**
  1. `211 ppb` `mu--p` Tension: Because `d ln(m_p^QCD/m_e) / d ln q = -21.007 < 0`, `m_p^exp - m_p^QCD(q_muon) = +0.228807 keV > 0`, so a positive (repulsive) proton QED self-energy `M_p^QED > 0` moves `q_proton` upward toward `q_muon` (physically correct sign). Macroscopic `O(alpha_EM m_p hbar_q) ~ +0.68 MeV` is already absorbed in the `2 m_mu F_Bor - 12 m_e` substrate identity, whereas the 1-loop electron-scale quantum-group QED dressing sits right at `+0.17 to +0.24 keV`: `QOU-P12` (`+alpha_EM m_e tr_D(Q_pair^(p)) = +0.1732 keV`) shrinks the `211.21 ppb` (`9.49 sigma`) tension to `+51.29 ppb` (`2.31 sigma`), and `QOU-P13` (`+alpha_EM m_e hbar_q [2]_q/[3]_q = +0.2441 keV`) shrinks it to `-14.12 ppb` (`-0.63 sigma`, a 93.3% reduction inside 1 sigma CODATA uncertainty).
  2. Macroscopic `Delta m_np` (`S2 + QED-Q6b`): Combining oriented Convention-D strong splitting `S2` (`alpha_bind * 4 ln q = +1.56280 MeV`) with `QED-Q6b` (`-1/3 alpha_bind h = -0.26094 MeV`) yields `Delta m_np = 1.30186 MeV` (`+0.659%` vs CODATA, closing the `-18.50%` one-term Convention-D gap by 28x).
  3. Convention-D `Q_beta` `c_k` Ladder (`QED-Q14`): Adding the 1-loop electron-scale radiative QED shift `Delta m_QED = -1/3 alpha_EM m_e h [2]_q = -0.5225 keV` to the `N=2` (`c_2 = -1`) Kashiwara decay base `Q_N2^D` shrinks the residual from `+600.62 ppm` (`+0.4699 keV`) to `-67.32 ppm` (9x reduction) and collapses the anomalous `c_2^emp(D)` from `-9.274` to `-1.0727` (within 7% of canonical `c_2 = -1`).
