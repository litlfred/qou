---
# qou-k1hs
title: Ingest the remaining 19 un-ingested PDFs in uploads/
status: completed
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T18:48:29Z
updated_at: 2026-11-17T23:20:00Z
parent: qou-mub3
---

19 of the 26 PDFs in uploads/ remain un-ingested, i.e. invisible to corpus-grep path 5. The 7 from commit 21ae4db28 were done 2026-08-25 (PR #5764). Remaining stems: 0105186v2, 1006.1099v3, 1103.4815v3, 1109.3255v2, 1211.1812v5, 1409.4073v1, 1901.08945v2, 2010.12445v1, 2111.12409v4, 2301.08311v4, 2311.14221v2, 2508.03145v1, 2601.07042v1, 2605.19310v1, 2607.10525v1, 978-3-98547-562-9-volume-4-chapter-5483, noniterativeroth2, roth_lemma.
RECIPE (works, do not re-derive): pip install --upgrade cffi (pypdf's import panics in cryptography's rust bindings without it), then
  python3 ~/folio-assistant/scripts/pdf-structure.py uploads/<f>.pdf -o library/
  python3 ~/folio-assistant/scripts/extract-candidates.py library/<doc-id>
  git mv uploads/<f>.pdf library/<doc-id>/
  python3 scripts/summarize-library.py --apply   # REQUIRED: without it there is no INDEX.md line, and INDEX.md is the FIRST tier of corpus-grep path 5
Check for shared doc_id before moving -- two of the 8 collided (same paper, two PDFs).

SCOPE CHANGE 2026-08-25: the owner uploaded a further batch (commit e505ecfa,
11 PDFs) and told me sibling PR #5770 is ingesting THAT batch. Mechanical work
has one owner -- #5770 owns e505ecfa, this bean does not. Coordination comment
posted there with the three traps (cffi, the summarize-library step, shared
doc_id). uploads/ is now 29 PDFs; this bean covers only the pre-existing
un-ingested backlog, not #5770's batch.


## COUNT IS STALE — it is 10, not 19 (measured 2026-10-10)

`ls uploads/*.pdf | wc -l` -> **10**; `ls -d library/*/ | wc -l` -> 662. The
title says "the remaining 19", so the queue has **drained by 9**, not grown.

Correcting it because the direction matters: an agent reading "19" budgets for
twice the work that is left. (An earlier pass of this cleanup read a checkout
1245 commits behind and recorded "23, the queue GREW by 4" — the opposite of the
truth. Re-measure on the live tree, not on a stale clone.)

**Why it is cited from the eightfold arc:** AGENTS.md corpus-grep path 5 searches
`library/` only, so anything still in `uploads/` is invisible to every
"has the corpus got this?" check — which is how a held source gets re-derived.
Several `CITE:`-class beans say "source X is not held"; some of those sources may
be sitting in `uploads/`. Run this before buying such a citation.

Mover: `scripts/migrate-uploads-to-library.py`.

## Completed 2026-11-17
Every stem listed above now has a `library/` entry on main (checked by name; `roth_lemma` is `library/roth-lemma`). The list holds 18 stems, not 19. `uploads/` holds no PDFs. The last leftover there, a section-only copy of `arxiv-astro-ph-0203462v1`, is removed by PR #8368.
