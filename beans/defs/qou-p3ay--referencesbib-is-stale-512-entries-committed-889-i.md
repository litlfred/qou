---
# qou-p3ay
title: 'references.bib is stale: 512 entries committed, 889 in references.ts'
status: todo
type: bug
priority: normal
tags:
    - reorg-2026-10-04
    - bibliography
created_at: 2026-09-29T21:12:39Z
updated_at: 2026-10-04T15:15:50Z
parent: qou-mub3
---

**Measured 2026-09-29 on main `32cb188c0`:** `references.bib` holds **512**
`@` entries; `folio/schema/references.ts` exports **889**. The header says
*"AUTO-GENERATED from folio/schema/references.ts — do not edit manually"*, so
377 entries are missing from what LaTeX sees, and some existing entries differ
too (e.g. `garoufalidis2004`'s note names an `uploads/` path that
`references.ts` now gives as `library/`).

**Why it was not fixed in passing.** PR #7487 changed one entry
(`leitner2026`) and patched only its 2 lines. A full regeneration would have
swept 377 unrelated entries into that PR.

**How to regenerate.** The platform's `export-bibtex.ts` needs qou's
reference registry configured first. Run bare, it throws *"Reference registry
not configured"*. A wrapper that does what `scripts/run-validate.ts` does
works:

    configureReferenceRegistry({ references, referenceMap, CSLEntrySchema })
    // then run folio-assistant/cat-harness/content/pipeline/export-bibtex.ts --out references.bib

No qou script does this today, which is probably why the file drifted. The
same thing happened once before: `qou-p8zx` recorded "references.bib was
stale" and fixed it by hand.

**Done when:**
- A committed qou command regenerates `references.bib`.
- The file is regenerated with it, and the diff is reviewed. It will be large
  and needs a look at LaTeX output for new or changed entries.
- Something (a gate, or a check in `run-validate`) fails when the `.bib`
  and `references.ts` disagree, so this cannot silently recur.
