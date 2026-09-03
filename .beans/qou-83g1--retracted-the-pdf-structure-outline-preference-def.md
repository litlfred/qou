---
# qou-83g1
title: 'RETRACTED: the pdf-structure outline-preference defect is environment-dependent, not a file defect'
status: todo
type: task
priority: normal
created_at: 2026-08-25T21:55:50Z
updated_at: 2026-08-25T21:56:39Z
---

In commit `02105d0517` and in the PR #5799 body I wrote that
`folio-assistant/scripts/pdf-structure.py` has a defect: it prefers the embedded
PDF outline whenever one exists (line 726, `"toc_source": "outline" if outline
else ...`), and `arxiv-2106.01332v4`'s outline titles do not occur literally in
the extracted text, so only 1 of 9 sections was produced (4.7kc of 66kc). I
worked around it by re-sectioning from an outline-stripped copy and recorded a
`toc_note` in structure.json explaining the bypass.

**A sibling ingested the same PDF onto main in parallel and got a clean result
with no intervention.** Their `structure.json`, from an add/add merge conflict
resolved 2026-08-25:

    toc_source : inferred
    sha256     : 44c19a99624997bfbc59...   <- the ORIGINAL pdf, not a stripped copy
    toc_note   : absent
    sections   : 9
    diagnostics: toc_entries 9, sections 9, chars_total 63650

Same file (sha matches the original in `uploads/`), same script, **no outline
detected at all** — while my run reported `toc=16 (out)`.

**So what I claimed is not established.** The line-726 preference is real and an
outline WAS detected in my environment; but whether the outline is visible is
environment-dependent (pypdf/pikepdf version in the container, most likely), not
a property of this PDF. "pdf-structure.py is defective on this file" does not
follow from one environment's run, and the suggestion that folio-assistant needs
a `--prefer-inferred-toc` flag rests on it.

**What actually stands:** on MY run the outline path produced a 1-section, 93%-
unreachable ingest, and that failure mode — a doc that looks ingested while its
text is not greppable — is real and worth a guard regardless of what triggers
it. A cheap one that needs no flag: warn when `chars_total` per section, or
sections-vs-toc_entries, falls off a cliff.

**Resolution in-tree:** the merge took main's version for all 19 conflicted
library artifacts, so the outline-stripped route and its `toc_note` are gone from
the tree. Nothing depends on them. The 21 ingests survive; INDEX is 402 and a
regeneration is a no-op.

**Lesson for the ingest path specifically:** two agents ingesting the same PDF in
parallel produce add/add conflicts on every generated artifact. Worth checking
`origin/main` for the doc-id before ingesting, which I did not do.
