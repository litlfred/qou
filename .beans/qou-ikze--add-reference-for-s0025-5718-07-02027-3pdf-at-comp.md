---
# qou-ikze
title: Add reference for S0025-5718-07-02027-3.pdf at computations/probes/gswz_coleman_li2_full_precisio…
status: todo
type: task
created_at: 2026-08-08T23:37:14Z
updated_at: 2026-08-08T23:37:14Z
---

Core and orphan; a live probe names this article as its algorithm source and there is no ref() entry.

**From the source**
- Prop. 4.3 — Li^{(p)}_n(z) = g_n(1/(1-z)) where the g_n are determined by an explicit differential recursion with g_n(0) = 0.
  Use here: The series the corpus probe evaluates to 120 terms to obtain full-precision Coleman Li_2 at Teichmueller points; currently implemented against an uncited source.
- Prop. 4.2 — For zeta a non-trivial (p^f - 1)-th root of unity, Li_n(zeta) is recovered from the Li^{(p)}_n(zeta^{p^r}) by a telescoped Frobenius sum with factor (p^{nf} - 1)^{-1}.
  Use here: The step that converts the computable truncated polylogarithm into the Coleman value at roots of unity, which is what the corpus's mod-5 dilogarithm cross-check needs.
- Prop. 6.1 — The coefficients of the g_n are p-integral with an explicit valuation lower bound, giving a computable precision/truncation estimate.
  Use here: The proved premise behind the probe's truncation choice (N = 120, tail valuation > 20); without it the probe's precision claim is an assertion.

Source: `library/s0025-5718-07-02027-3/S0025-5718-07-02027-3.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.
