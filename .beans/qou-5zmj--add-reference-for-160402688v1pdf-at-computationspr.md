---
# qou-5zmj
title: Add reference for 1604.02688v1.pdf at computations/probes/deltalambda_normal_surface_classes_prob…
status: todo
type: task
created_at: 2026-08-08T23:37:22Z
updated_at: 2026-08-08T23:37:22Z
---

A paper cited by six audit docs and consumed by two production probes has no ref() entry; every citation is a bare arXiv id, so nothing in the bibliography pipeline sees it.

**From the source**
- Prop. A.3 — For a generalized angle structure alpha, the Euler characteristic of a normal surface S satisfies chi(S) = -sum_q alpha(q) x_q / pi + rho_alpha(dS) / 2pi, pairing the angle polytope against the normal-surface cone.
  Use here: This is the identity the Delta_lambda collective-term probe uses to compute chi and the alpha-independence check on the 52 Borromean vertex spun-normal classes; it is cited there by paper section only.

Source: `library/arxiv-1604.02688v1/1604.02688v1.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
