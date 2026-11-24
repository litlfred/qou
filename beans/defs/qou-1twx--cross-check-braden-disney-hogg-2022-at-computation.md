---
# qou-1twx
title: Cross-check [braden-disney-hogg-2022] at computations/alpha_em_b2_bring_period_matrix_probe.py
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T23:35:32Z
updated_at: 2026-11-24T16:29:02Z
parent: qou-mub3
---

The corpus recovers tau_0 to 50 dps by an exact SL_2(Z) word and reports a 6-digit match to this paper's 6 d.p. value. Recording that comparison against the printed j(tau_0) = -29^3 x 5/2^5 (rather than only against the derived -121945/32) closes the loop on the published input.

**From the source**
- section on the period matrix (j-invariant conditions) — tau_0 = -0.5 + 0.186676i to 6 d.p., characterised by j(tau_0) = -29^3 x 5/2^5 and j(5 tau_0) = -25/2; Riera-Rodriguez swapped the two values.
  Use here: The published tau_Bring / j(E) input used by BringEllipticFactor.lean and the alpha_em period-matrix probes; also the authority for the swap correction the corpus records.

Source: `library/arxiv-2208.13692v1/2208.13692v1.pdf` (`braden-disney-hogg-2022`)
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8475, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-24 — Resolved in PR #9371 (issue #9370)

- Upgraded `computations/alpha_em_b2_bring_period_matrix_probe.py` to `mp.mp.dps = 80` (zero `float64`, dynamic sibling read via `record_upstream` from `alpha-em-b2-scalar-c.witness.json`) and added the explicit 80-dps cross-check against `[braden-disney-hogg-2022]` (`library/arxiv-2208.13692v1/2208.13692v1.pdf`).
- Verified exact rational identity `-29^3 * 5 / 2^5 == -121945/32`, `|j(tau_0) - (-29^3 * 5 / 2^5)| = 1.30e-77`, and `|j(5*tau_0) - (-25/2)| = 1.35e-79` at `tau_0 = (tau_E - 3)/5 = -1/2 + 0.186676462462809923...i`, matching the printed 6 d.p. `-0.5 + 0.186676i` within `4.62e-7 < 5e-7` and resolving the earlier reflowed-PDF glyph misread (`allPassed: true`, `7/7` assertions pass).
