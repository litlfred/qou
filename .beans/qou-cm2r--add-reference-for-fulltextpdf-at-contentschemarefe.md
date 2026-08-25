---
# qou-cm2r
title: Add reference for fulltext.pdf at content/schema/references.ts
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:35:20Z
updated_at: 2026-08-21T17:03:29Z
---

Useful classical background on Bloch-Wigner and ideal-tetrahedron volumes with no ref() entry. Create one; the ledger row keeps id null until then so the false join to the dilogarithm-identities key is not propagated.

Source: `library/zagier-the-dilogarithm-function/zagier-the-dilogarithm-function.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/zagier-the-dilogarithm-function/  ->  [zagier-dilogarithm]
  The dilogarithm function

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
