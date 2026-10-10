---
# qou-fc7k
title: Add reference for 0006156v1.pdf at prop:faddeev-phib-uniqueness
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:35:59Z
updated_at: 2026-08-21T17:03:34Z
---

No ref() entry exists; the paper's Sect. 6 is the appropriate source for three separate Phi_b facts the corpus uses.

**From the source**
- Sect. 6.2, eq. (21) — e_b(z) equals a ratio of two q-exponentials with q = e^{i pi b^2} and qbar = e^{-i pi b^{-2}}, defining a meromorphic function on all of C with an explicit zero/pole lattice.
  Use here: Primary source for the modular-double product that prop:faddeev-phib-uniqueness writes verbatim as its Phi_b, and for the meromorphy + isolated-zeros facts that block currently establishes by hand.
- Sect. 6.2, eq. (22) — Four-sector asymptotic behaviour of e_b(z) as |z| -> infinity, with Gaussian, theta-function and constant regimes selected by arg(z) relative to arg(b).
  Use here: The sector-wise growth input behind prop:faddeev-phib-uniqueness's 'strip growth' hypothesis; applicable on that block's branch Im b^2 > 0 (arg b = pi/4), so it can replace the block's elementary product-norm bound with a literature statement.

Source: `library/arxiv-hep-th-0006156v1/0006156v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-hep-th-0006156v1/  ->  [faddeev-kashaev-volkov2000]
  Strongly coupled quantum discrete Liouville theory I: algebraic approach and duality

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
