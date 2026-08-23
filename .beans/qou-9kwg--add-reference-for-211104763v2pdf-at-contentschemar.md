---
# qou-9kwg
title: Add reference for 2111.04763v2.pdf at content/schema/references.ts
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:34:48Z
updated_at: 2026-08-21T17:03:25Z
---

This four-author sequel has no ref() entry and is currently mis-joined to the three-author paper. Register it from its own front matter.

Source: `library/arxiv-2111.04763v2/2111.04763v2.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/arxiv-2111.04763v2/  ->  [garoufalidis2021a]
  RESURGENCE OF CHERN–SIMONS THEORY AT THE TRIVIAL FLAT CONNECTION

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
