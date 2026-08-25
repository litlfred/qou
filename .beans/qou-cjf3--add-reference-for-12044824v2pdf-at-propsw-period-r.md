---
# qou-cjf3
title: Add reference for 1204.4824v2.pdf at prop:sw-period-residue-sum
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:35:50Z
updated_at: 2026-08-21T17:03:28Z
---

A ref() stanza for this document was drafted in the D2a thimble audit with a written rationale and never landed in references.ts; the SW/thimble blocks it was drafted for are still uncited.

**From the source**
- Abstract; §5.1-5.2 — Spectral networks are networks of trajectories on a Riemann surface obeying local rules; they give a map between flat GL(K,C) connections on a surface and flat abelian connections on a branched cover, with walls as the loci where trajectories degenerate.
  Use here: The abelianisation statement is the published form of what prop:mi-sw-abelianisation asserts for the colour spectral curve; citing it gives that proposition an external template rather than leaving the abelianisation unsourced.

Source: `library/arxiv-1204.4824v2/1204.4824v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-1204.4824v2/  ->  [arxiv-1204.4824v2]
  Spectral networks

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
