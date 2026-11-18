---
# qou-1twx
title: Cross-check [braden-disney-hogg-2022] at computations/alpha_em_b2_bring_period_matrix_probe.py
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:32Z
updated_at: 2026-10-04T15:18:23Z
parent: qou-mub3
---

The corpus recovers tau_0 to 50 dps by an exact SL_2(Z) word and reports a 6-digit match to this paper's 6 d.p. value. Recording that comparison against the printed j(tau_0) = -29^3 x 5/2^5 (rather than only against the derived -121945/32) closes the loop on the published input.

**From the source**
- section on the period matrix (j-invariant conditions) — tau_0 = -0.5 + 0.186676i to 6 d.p., characterised by j(tau_0) = -29^3 x 5/2^5 and j(5 tau_0) = -25/2; Riera-Rodriguez swapped the two values.
  Use here: The published tau_Bring / j(E) input used by BringEllipticFactor.lean and the alpha_em period-matrix probes; also the authority for the swap correction the corpus records.

Source: `library/arxiv-2208.13692v1/2208.13692v1.pdf` (`braden-disney-hogg-2022`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
