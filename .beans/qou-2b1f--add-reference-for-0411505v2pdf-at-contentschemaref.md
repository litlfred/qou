---
# qou-2b1f
title: Add reference for 0411505v2.pdf at content/schema/references.ts (new id, e.g. garoufalidis-loebl2…
status: completed
type: task
priority: normal
created_at: 2026-08-08T16:12:47Z
updated_at: 2026-08-21T17:03:14Z
---

No ref() entry; the folio already registers several Garoufalidis papers and this one carries the MacMahon <-> colored-Jones link the 13-driver menu leans on.

Source: `library/arxiv-math-0411505v2/0411505v2.pdf` — no `references.ts` entry yet
Relevance: **supporting** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-math-0411505v2/  ->  [garoufalidis-loebl2005]
  A non-commutative formula for the colored Jones function

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
