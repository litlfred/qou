---
# qou-diu5
title: Add reference for 0105039v1.pdf at content/schema/references.ts
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:35:25Z
updated_at: 2026-08-21T17:03:31Z
---

The document is a distinct, corpus-relevant paper with no ref() entry; the ledger currently mis-joins it onto faddeev_kashaev1994. Register a new key (metadata from the title page: Hikami, math-ph/0105039) before any citation is added.

Source: `library/arxiv-math-ph-0105039v1/0105039v1.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-math-ph-0105039v1/  ->  [hikami2001]
  Hyperbolic Structure Arising from a Knot Invariant

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
