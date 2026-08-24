---
# qou-b83i
title: Add reference for Invariant_eigendistributions_2.pdf at alg:delta-lambda-closure
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:36:39Z
updated_at: 2026-08-21T17:03:26Z
---

No ref() entry, and no Springer-theory citation exists anywhere in the corpus despite the Delta_lambda value being described as a signed Springer dimension.

**From the source**
- sec. 2 and sec. 4 — Weyl-group representations are constructed on the (Borel-Moore) homology of the conormal variety via an integral formula for invariant eigendistributions, yielding the Springer representations.
  Use here: The geometric backdrop for the phrase 'signed Springer dimension' that alg:delta-lambda-closure uses without a source.
- sec. 12 (Appendix) — The homotopy action constructed here agrees with the Kazhdan-Lusztig construction of the Weyl-group action on the conormal variety.
  Use here: Relevant to the PROBE-4 prune's framing, which contrasts the mixed-sign Delta_lambda target against the non-negativity of Kazhdan-Lusztig multiplicities; the comparison shows the two constructions of the same W-action are not independent sources of a sign.

Source: `library/invariant-eigendistributions-2/Invariant_eigendistributions_2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/invariant-eigendistributions-2/  ->  [rossmann-invariant-eigendistributions-2]
  Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
