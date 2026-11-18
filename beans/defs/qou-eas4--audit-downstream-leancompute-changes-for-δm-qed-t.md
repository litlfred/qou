---
# qou-eas4
title: Audit downstream Lean/compute changes for Δm_QED two-term tracking and test impact on the 211 ppb μ–p anchor tension & 1ppQ c_k/d_k ladders
status: in-progress
type: task
priority: high
tags:
    - compute
    - 1ppq
    - audit
created_at: 2026-11-18T19:52:24Z
updated_at: 2026-11-18T19:52:24Z
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
