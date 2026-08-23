---
# qou-y7ss
title: Add reference for 2302.08363v2.pdf at def:ecalle-borel-resummation
status: completed
type: task
priority: normal
created_at: 2026-08-09T00:10:47Z
updated_at: 2026-08-21T17:04:03Z
---

Orphan on all three checks and carries the trans-series-convergence layer the resummation blocks depend on. The ref() entry is the prerequisite for the cite-in-block and new-remark actions below.

**From the source**
- Sec 2, eqs (2.5)-(2.8) — The Borel-resummed trans-series s_pm(Phi) = sum_l y^l s_pm(phi_l)(g) is itself an infinite sum over non-perturbative sectors and is a potential new source of divergence; reorganising by fixed power n of the coupling gives the partial series G_n(y) = sum_l a_{n,l} y^l, and convergence of the G_n with a common radius R (eq 2.8) is the property that makes the resummed trans-series a well-defined function.
  Use here: Supplies the second-stage premise that def:ecalle-borel-resummation does not define and rem:st-is-median-resummation silently uses. That remark identifies st(f~|_eps) with L^med(f~) for a transseries f~, citing Watson/Nevanlinna-Sokal uniqueness -- which is a one-series statement. The sum over sectors is a separate convergence question, and this gives the vocabulary (partial series, common radius R) to state it.

Source: `library/arxiv-2302.08363v2/2302.08363v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-2302.08363v2/  ->  [arxiv-2302.08363v2]
  On the structure of trans-series in quantum field theory

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
