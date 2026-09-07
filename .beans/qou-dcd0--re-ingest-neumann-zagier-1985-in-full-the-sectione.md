---
# qou-dcd0
title: 'Re-ingest Neumann-Zagier 1985 in full: the sectioner kept only pp. 328-332 of a complete 26-page text layer'
status: completed
type: task
priority: normal
created_at: 2026-09-06T13:36:37Z
updated_at: 2026-09-06T13:40:04Z
---

## Resolved 2026-09-06 (branch claude/ingest-uploads-2026-09-06, PR #6964)

**The premise was wrong, and the measurement is what corrected it.** The bean
the coordinator named (`qou-ss6z`) does not exist, and the paper was described
as "held three times as a 4-page tail". It is not a tail: the PDF at
`library/1-s20-0040938385900047-main/1-s2.0-0040938385900047-main.pdf` is the
complete *Topology* 24 (1985) 307-332 article, 26 pages, every page with an
embedded text layer (pypdf: 400-4031 chars per page, 0 empty; `pdf-ocr.py
--check`: tesseract and pdftoppm are absent here, and were not needed).

**What was actually broken: the sectioning.** `pdf-structure.py`'s heading
inference matched one pseudo-heading on p. 328 (`4. A2 35A I`) and its
splitter starts at the first mark, so pp. 307-327 were dropped:
`chars_total 5437`, sections covering PDF pp. 22-26 only. The printed
headings are typeset `§ 1. INTRODUCTION` and extract as `5 1. INTRODUCTION`,
`52. COMBINATORICS ...`, `$3. VOLUME COMPUTATIONS`, which the numbered-heading
regex cannot see. This is a platform (folio-assistant) limitation; not fixed
there.

**Fix applied.** The seven printed headings, read from the page text, were
handed to `pdf-structure.py`'s own `split_sections` / `write_sections`
(driver in the session scratchpad, not committed); `structure.json` carries a
`toc_note` saying so and keeps `duplicate_copies`; doc-id unchanged.

    before  2 sections  pp. 22-26  chars_total  5437
    after   7 sections  pp.  1-26  chars_total 54579

Greppable now (verified): `Theorem 1A` (sec-000:43), `THEOREM 2` (sec-000:101),
gluing condition (sec-001:61), symplectic form / Theorem 2.2 (sec-001:136-146),
volume computations (sec-004).

**Left as is, stated plainly.**
- The two `duplicate_of` copies keep their 2-section extraction; the
  `duplicate_of` marker redirects readers to this directory.
- `extract-candidates.py` finds 0 candidates: the 1985 typesetting prints
  `THEOREM 2.2.` in capitals, which its regex does not match.
- The 2026-09-03 JSON-LD nodes (`sections/sec-00{0,1}.jsonld`, `blocks/`,
  `manifest.jsonld`) still describe the OLD two sections. The generator is not
  in the pinned platform (428ca5c) and its `main` version fails against the
  pin (`DAK_BLOCK_KINDS` missing), so they were left rather than hand-edited.
  Regenerating them is a platform-pin bump away.
