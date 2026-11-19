---
# qou-10v9
title: 'PROGRAM: L2 at 1 ppQ (mass and binding accuracy)'
status: in-progress
type: milestone
priority: critical
tags:
    - reorg-2026-10-04
created_at: 2026-10-04T15:09:54Z
updated_at: 2026-11-19T16:48:43Z
---

Programme root for the L2 / 1 ppQ target. Anchor document: `docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md`.

- L1 (compute precision, cross-method agreement <= 1 ppQ) is met.
- L2 (per-observable accuracy sigma_th <= sigma_exp/100) is 1 of 6 scoreable, 0 of 6 unconditional (2026-09-07 dashboard).
- Four un-derived objects: the Q_beta functional under convention D, the extensive binding term, the m_mu / proton-pin tension, the alpha_em conditional classes.

Predecessor articulations (cite, do not restate): 1qug, vibo, m2ay, ggdk/65jh, qou-37j2, qou-tonv.
Physical-identification conjectures (owner ruling 2026-10-04, decision 1) live here or under P4, never under the formal-conjecture umbrella.

2026-10-10: ofri named this OWNER GOAL #2 (goal #1 is qou-ywyq, trace = multiplicative integral).



## Progress Update (2026-11-19)
Updated 2026-11-19 L1/L2 status: L1 core gate GREEN (`1.82e-49` Markov cross-check, `1.32e-50` clarabel-mpfr duality gap); `m_mu` improved 26x to `8.058 ppb` (`+0.37 sigma_exp`), `v_EW` at `29.37 ppb` (`0.11 sigma_exp`), `m_K/m_pi` at `51.43 ppb` (`5.1x` inside L2), `Delta_pn` within `111 eV` (`86.2 ppm`). Added child tasks for anchor round-trip polish, `q_2t - q_mu` 2-loop dressing, 2-loop `v_EW`, and Dirac-Coulomb-Breit atomic electron binding.
