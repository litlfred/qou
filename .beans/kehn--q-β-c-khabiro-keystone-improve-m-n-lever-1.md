---
# kehn
title: Q_β c_k/Habiro keystone — improve m_n (lever 1)
status: in-progress
type: milestone
priority: normal
created_at: 2026-06-24T03:18:40Z
updated_at: 2026-08-09T18:24:25Z
---

## 2026-06-24 — PR #2723: Kashiwara b² Q_β wired into production neutron

Wired the parameter-free Kashiwara b² truncation `Q_N2`
(`derived_masses.q_beta_kashiwara_n2_mev`) into the canonical neutron
(`m_n = m_p + Q_β + m_e`) via `canonical_mass.py` +
`m_p_substrate_identity_50dps.py`.

- **m_n: −1759 → +1.04 ppb; Q_β: −2112 ppm → +1.25 ppm** (both ~1690× better).
- De-circularized the old Q_AME "Path C"; flavor-split demoted to a secondary diagnostic.
- Gemini review (3 comments) addressed; L1/L2 dashboards reported (no regression);
  `mba-step11` appendix + `appendix-qvalues` content synced.
- TIER: **near-match**. Exact closure still open — gated on the s5-so3 / Habiro
  keystone (bean `s5bb`; siblings #2409, #2524). This is lever 1's near-match
  milestone, not the exact-derivation close.

PR: https://github.com/litlfred/qou/pull/2723

## Lever-2 sharpening (2026-08-09, PR #4860) — target contamination found; miss is GENUINE

Ran the 'is the residual what it claims to be?' check on Q_beta (the same one
that dissolved the m_p row). Probe computations/codata_registry_triangulation_probe.py
leg 5; audit docs/audits/2026-08-09-codata-registry-vintage-straddle.md.

**Q_beta's miss is REAL — this does NOT close or shrink the lever.** But its
comparison target was contaminated:

- The corpus holds TWO experimental Q_beta determinations: Q_BETA_MEV_AME and
  m_n(direct) - m_p - m_e. The second is built on M_P_MEV, a mislabelled
  CODATA-2018 proton.
- They disagreed by 1814 ppb (2.33 sigma). With a consistent proton: 194 ppb
  (0.249 sigma). The stale proton explains 89.3%; the two then AGREE.
- Prediction vs each: AME 163.98x | consistent 139.06x | STALE 68.69x.

**Trap removed:** anyone scoring Q_beta against the stale-derived target sees
68.7x and could conclude Q_beta is within ~1.4 sigma of passing. It is not —
139x-164x against every legitimate target.

So lever 2's true size is 139x-164x, and the honest experimental spread on
Q_beta is now ~194 ppb rather than 1814 ppb (which matters if anyone was
treating the determination spread as headroom).
