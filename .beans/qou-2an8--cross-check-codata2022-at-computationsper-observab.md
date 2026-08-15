---
# qou-2an8
title: Cross-check [codata2022] at computations/per-observable-100x-status.witness.json
status: in-progress
type: task
priority: normal
created_at: 2026-08-08T23:34:20Z
updated_at: 2026-08-09T10:58:16Z
---

Six of seven mass literals labelled CODATA 2022 in the Lean are CODATA 2018, off by ~1.3-1.5 ppb. Re-run the L2 dashboard against the real 2022 values and report the deltas. Flagged for attention, not asserted: the documented de-fitted m_p round-trip miss is +1.35 ppb and the CODATA 2018->2022 proton shift is also +1.35 ppb; whether these are the same number is a check to run, not a conclusion.

Source: `library/codata-2022-constants.txt` (`codata2022`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## RESULT (2026-08-09, PR #4860) — CHECK RUN: yes, they ARE the same number

The bean asked whether the m_p +1.35 ppb round-trip miss and the CODATA
2018->2022 proton shift are the same number. Ran it: **they are.**

Probe computations/codata_registry_triangulation_probe.py (audit-only,
3/3 assertions pass). Audit
docs/audits/2026-08-09-codata-registry-vintage-straddle.md.

- The over-determined triple (m_e, m_p/m_e, m_p) — all labelled CODATA 2022 —
  is inconsistent: m_e*(m_p/m_e) - m_p = +1.3507 ppb = **127x m_p's last
  printed digit**. (Against measurement sigma it is only 3.14 sigma; that is
  recorded but is NOT the test — same-edition CODATA values are one
  correlated fit output, so the bar is printed granularity.)
- q_0 is pinned so m_p_pred == m_e*MASS_RATIO_P_E identically, so the scored
  row reproduces that residual to 3e-4 ppb (limited by the dashboard's own
  4-sig-fig err_ppb). **The m_p row measures registry inconsistency, nothing
  else.**
- Independent neutron leg: m_p+m_e+Q_beta vs the stored CODATA DIRECT
  neutron — ratio-derived proton 0.32 sigma, stored proton 2.96 sigma. The
  stored m_p is the stale member. (codata_2022_source holds a genuine 2022
  m_e and 2022 direct neutron but a 2018 proton.)
- Muon leg is NON-DISCRIMINATING (sigma is 23x the effect); supports nothing.

**m_p does NOT become MET.** Under the proton pin m_p is the anchor, so a
corrected round-trip is a calibration tautology (AGENTS.md q_0-anchor rule 1,
as already applied to m_mu). Honest disposition: stop scoring the row. Count
does NOT rise to 3/7.

L2 projection (audit-only, dashboard unmodified): m_n 420.1x -> 176.7x,
Delta_pn 163.3x -> 151.3x. Both still genuine FAILs (Q_beta-driven).

Follow-ups left open: (1) fix codata_2022_source.M_P_MEV + re-score
dashboard (touches committed witnesses, own branch); (2) re-classify the m_p
row as an anchor diagnostic; (3) MASS_RATIO_P_E_ERR is still the 2018 sigma.


## Companion finding (same PR #4860): the 5 L2 failures are 2 independent ones

Probe computations/l2_row_independence_probe.py (1/1 assertion).
Delta_pn == Q_beta + m_e and m_n == m_p + Q_beta + m_e hold on BOTH the
prediction and the TARGET side (M_N_MEV_AME_DERIVED is CONSTRUCTED as
M_P + M_E + Q_BETA, not independently measured). So:

  m_p artifact | m_n redundant | Delta_pn redundant | Q_beta INDEP | m_mu INDEP

L2 has TWO levers (Habiro/Q_beta = bean kehn; mu-p tension), not five fronts.

Also: leg 4 checked whether the vintage artifact reaches m_mu. It does NOT —
correcting the ratio to 2022 moves m_mu 963.6x -> 970.2x, i.e. WORSE.
Recorded as measured.

Blast radius for the M_P_MEV fix: 234 referencing files, 175 emitting
witnesses => own owner-gated branch (bean qou-if87), not an idle drain.
