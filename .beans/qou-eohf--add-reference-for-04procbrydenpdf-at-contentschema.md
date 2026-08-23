---
# qou-eohf
title: Add reference for 04procbryden.pdf at content/schema/references.ts
status: completed
type: task
priority: normal
created_at: 2026-08-09T00:10:43Z
updated_at: 2026-08-21T17:03:34Z
---

Orphan with no ref() entry, and it is the only registered-or-unregistered source in the tree stating the Sigma(2,3,5) Ohtsuki series in closed form with an explicit normalisation. Per the skill, creating the ref() entry is the first action, not the last; metadata (title, authors, year, venue) goes in content/schema/references.ts, never here.

Source: `library/04procbryden/04procbryden.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/04procbryden/  ->  [jacoby-lawrence2004]
  Some computations of Ohtsuki series

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
