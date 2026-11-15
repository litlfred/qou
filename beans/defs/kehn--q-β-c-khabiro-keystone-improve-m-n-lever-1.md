---
# kehn
title: Q_β c_k/Habiro keystone — improve m_n (lever 1)
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-06-24T03:18:40Z
updated_at: 2026-11-15T17:33:12Z
parent: qou-avtq
blocked_by:
    - qou-cds1
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



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-09 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 — evidence re-check (verification sweep of `qou-avtq`)

**Verdict: EVIDENCE-UNRELIABLE.** The 1.04 ppb / 139–164× figures belong to the retired z=1 base and convention C. They say nothing about m_n under the 2026-09-08 ruling (dashboard: 1.389e5 ppb). The lever has to be re-sized on the ruled base before any gain is quoted. Work overlaps qou-iagg.

Evidence: Numbers in the bean: m_n +1.04 ppb, Q_β +1.25 ppm (Kashiwara b² Q_N2), lever-2 139–164×. All are C-frame on the retired z=1 base (Q_A·cos·(1−u²)). The live dashboard `computations/per-observable-100x-status.witness.json` (2026-09-14) scores m_n err_ppb 1.389e+5 and Q_β 1.668e+8 with `ck_rungs_applied: 0` and `ladder_on_admissible_base_exists: false`.

Status: `todo` → `todo` (unchanged: edited today by another session, or held in-progress).
Checked against qou `main` at `77695711d2`. Probes were re-run only where cheap and decisive. A numeric result counts as evidence only where it reproduces and its precision exceeds the gap it decides; convention-C numbers are not evidence about convention-D claims.


## 2026-10-10 — a witness this bean cites is red (cross-cluster check, verification sweep of `qou-avtq`)

The headline `m_n: −1759 → +1.04 ppb` (via `m_p_substrate_identity_50dps.py`, PR #2723) no longer holds on main: `computations/m-p-substrate-identity-50dps.witness.json` (2026-08-29, proton q0) fails `m_n_matches_codata_within_10ppb` at **501.43 ppb** (tolerance 10). `qou-khue` records the 501 ppb move. Cite `qou-khue`, not the 1.04 ppb figure.

## 2026-10-10 — follow-up review (re-check of the `qou-avtq` sweep flags)

The 1.04 ppb and 139–164× figures are from the **retired z = 1 base, convention C**. The `m-p-substrate-identity-50dps` witness fails at 501 ppb, and the dashboard gives m_n at 1.389e5 ppb with no ladder on the ruled base. These figures should be read as superseded (see `qou-khue`). Whether to rescope this bean or fold it into `qou-iagg`/`qou-cds1` is the owner's call.

Checked read-only against qou `main` at `aa914b606a`, mpmath 1.3.0. Full write-up: `qou-review/avtq-reopened-beans-2026-10-10.md` (project files). Status unchanged.
