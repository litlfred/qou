---
# kehn
title: Q_β c_k/Habiro keystone — improve m_n (lever 1)
status: in-progress
type: milestone
priority: normal
created_at: 2026-06-24T03:18:40Z
updated_at: 2026-06-24T16:50:00Z
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

