---
# qou-3ufj
title: Add reference for 9608020v2.pdf at docs/audits/2026-07-24-covariance-kernel-literature-assessment.md
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:37:28Z
updated_at: 2026-08-21T17:03:16Z
---

Named in a live attack plan and in a literature-assessment audit with no ref() entry.

**From the source**
- Binomial formula (Sec. 1-2) — An explicit binomial expansion of Jack polynomials in terms of shifted Jack polynomials evaluated at the contents of the partition.
  Use here: The content-evaluation machinery the Delta_lambda covariance-kernel attack plan (bean qou-v8t7) uses; the 2026-07-24 assessment records it as supporting but blocked by the same dim-threshold obstruction, so it is cited as method, not as a closure.

Source: `library/arxiv-q-alg-9608020v2/9608020v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-q-alg-9608020v2/  ->  [arxiv-q-alg-9608020v2]
  Shifted Jack polynomials, binomial formula, and applications

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
