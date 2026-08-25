---
# qou-tn6j
title: Add reference for ki52.pdf at content/schema/references.ts
status: completed
type: task
priority: normal
created_at: 2026-08-08T23:35:36Z
updated_at: 2026-08-21T17:03:57Z
---

The corpus's 5_2 programme depends on one source for its 5_2 numbers; this in-repo paper is the independent asymptotic source and has no ref() entry. Register it from the title page (note [ohtsuki-takata2015] is a DIFFERENT, already-registered paper sharing this document's first author - do not reuse that key).

Source: `library/ki52/ki52.pdf` — no `references.ts` entry yet
Relevance: **core** — agent assessment, not yet adjudicated.

Raised by `local/paper-relevance-triage`; the ledger row is in `content/bib-qa-verifications.json`.

RESOLVED 2026-08-21 (bean qou-kqbk, PR #5384). This bean's task was to add the reference; it exists.

  library/ki52/  ->  [ohtsuki2016]
  On the asymptotic expansion of the Kashaev invariant of the 5_2 knot

The library registration backlog is drained to zero — every library document now has a references.ts entry, and 351 entries name the copy they point at. The 'no `references.ts` entry yet' line in the body above is stale and was true when paper-relevance-triage raised this.

Closing only because adding the reference WAS the whole task. Sibling beans titled 'Cite X at Y' (81), 'Remark interpreting X' (70) and 'Cross-check' (33) carry that same stale line and are NOT closed: the entry existing is necessary for them and not sufficient — the citation site, the remark, or the check is still to be written.
