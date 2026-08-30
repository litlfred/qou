---
# qou-1u1i
title: Add reference for 0411647v2.pdf at content/schema/references.ts, id sniady2006asymptotics (id alr…
status: completed
type: task
priority: normal
created_at: 2026-08-08T16:12:48Z
updated_at: 2026-08-21T17:03:14Z
---

Closes an unregistered -- Ref: key used by 7 producers. This is a corpus-hygiene defect, not a nice-to-have; do this first. Verify the DOI 10.1007/s00440-005-0479-7 and the PTRF 136 (2006) 263-297 volume/pages before committing (the corpus asserts them; they were not independently confirmed in-sandbox).

Source: `library/arxiv-math-0411647v2/0411647v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-math-0411647v2/  ->  [sniady2006asymptotics]
  Asymptotics of characters of symmetric groups, genus expansion and free probability

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
