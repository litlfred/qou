---
# qou-b6ti
title: 'Library: DeTurck-Gluck (0406276v1) sectionised to 4510 chars of 40 pages — the paper defining the EM-linking kernel is ungreppable'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-07T08:20:08Z
updated_at: 2026-10-04T15:21:15Z
parent: qou-mub3
---

Found 2026-09-07 by a six-path corpus-grep on the EM-linking front
(`qou-17mq`). Verified directly, not inferred.

`library/0406276v1/` is **DeTurck & Gluck, _The Gauss Linking Integral on the
3-Sphere and in Hyperbolic 3-Space_** — the paper this whole front reads its
kernel off. Thm 1(3) is where `phi_0(alpha) = -coth(alpha)/4pi` comes from;
it is cited at `content/schema/references.ts:10125`.

Measured on the committed tree:

    structure.json: pages 40, chars_total 4510, sections 1, toc_entries 1
                    pages_without_text 0, likely_scanned FALSE
    sections/:      sec-000-references.md (4888 B) + sec-000.jsonld only
    grep -rl coth library/0406276v1/  ->  NO HIT

~113 characters per page extracted, and the one section file is the
**bibliography** (pages 38-40 of 40). So corpus-grep **path 5 cannot be cited
as evidence about this kernel's literature at all** — a `sections/` grep for
`coth`, `linking integral`, or `hyperbolic Green` misses the defining source
and returns a clean bill.

## Why this is a NEW sub-class

Not the `thurston1978` held-but-partial class (a scanning failure). Here
`pages_without_text = 0` and `likely_scanned = false` — **the text extracts
fine; the SECTIONISER produced one section and kept only the references.**
The `ocr/` fourth tier does not help either: there is no `ocr/` directory,
because nothing thought this document needed one.

Detection shape worth generalising: `chars_total / pages` far below the
corpus norm while `likely_scanned` is false is a sectionisation failure that
no existing guard looks for. A tier-4 `ocr/` sweep will not catch it.

## Fix

Re-ingest this one PDF (`scripts/pdf-structure.py`). Highest-leverage single
library action on the EM-linking front: it is the only held primary source
for the kernel, and `qou-17mq` / `qou-zp6a` / `qou-o6ml` all reason from
Thm 1(3) without being able to grep it.

## Also observed, separately

`library/` INDEX.md is behind again: 655 directories, 609 rows, 23
duplicate-marked, leaving **23 real documents with no index row**. Tier 1 is
not a clean bill until `python3 scripts/summarize-library.py --apply` runs.
Recorded here rather than beaned separately — this is the recurring class
AGENTS.md already documents.


## 🛑 RETRACTED, same day: the cause is SECTIONING, not extraction. And the 8.9x was my measurement error.

The text above says `pypdf.extract_text()` fails on this PDF and that
`pdfminer.six` recovers 12.1x more, generalising to a class of 9 documents
"recoverable 8.9x by an extractor swap". **Both halves are wrong.**

**What I did wrong.** I compared pdfminer's RAW output against pypdf's
POST-SECTIONING output — `diagnostics.chars_total` is
`sum(s.n_chars for s in sections)`, not the page text. Measured raw-to-raw:

    doc                         sectioned   pypdf RAW  pdfminer RAW  ratio  sec  toc
    0406276v1                        4510       53937         54418  1.01x    1    1
    1-s20-0040938387900097-main      2079       27714         32996  1.19x    1    1
    67-6-1860                        1647        1632          3536  2.17x    1    0
    90-1-219                         4506       43222         48559  1.12x    3    3
    arxiv-nucl-th-0409040v2          2213       20713         20774  1.00x    1    2
    neumann-zagier-1985 (x2)         5437       55012         63793  1.16x    2    2
    procrsoclondona92                1597        1580          1716  1.09x    1    0
    the-period-matrix-of-brings      8674       28861         30543  1.06x    2    6

**pypdf reads these documents fine** — 1.00x to 1.19x of pdfminer on seven of
nine. The DeTurck-Gluck text it returns is clean and includes the defining
line verbatim. What is lost is lost afterwards: 53937 -> 4510 is **92%
discarded by `split_sections`**, and the same is true at 90%, 90%, 93%, 89%,
70% for the others.

**The actual bug**, at `scripts/pdf-structure.py:589` in `folio-assistant`:

    marks.sort(...)
    if not marks:
        whole = "\n".join(pages).strip()
        return [Section("sec-000-document", ..., whole)]     # keeps EVERYTHING
    for i, (pi, li, e) in enumerate(marks):                  # starts at marks[0]
        ...

Sections are emitted starting at the FIRST heading mark. **Text before
`marks[0]` is never emitted.** `0406276v1`'s heading inference finds exactly
one heading — "References", on page 38 of 40 — so pages 1-37 are silently
discarded.

The shape is perverse and is why this went unnoticed: a document with **zero**
headings hits the `if not marks` branch and keeps all its text, while a
document with **one late** heading loses everything before it. Correct when it
finds nothing; broken when it finds one thing.

**This also re-splits the class.** The two documents with `toc = 0` —
`procrsoclondona92` (1597 kept of 1580 raw) and `67-6-1860` (1647 of 1632) —
are NOT sectioning losses at all. They keep ~100% of what pypdf finds and are
genuinely low-text (scans); `procrsoclondona92` already has its `ocr/` tier,
exactly as AGENTS.md describes. So the sectioning-loss class is **7**, not 9,
and the extractor is not implicated in any of them.

**The fix I wrote first was the wrong fix and is reverted.** A pdfminer
fallback in `page_texts` would not have fired here anyway: its trigger reads
the RAW yield, which is healthy at 1348 chars/page.

**What the fix is:** emit a leading section for the text before `marks[0]`.
Whether that should apply corpus-wide is being measured — nearly every paper
has a title and abstract before its first heading, so this may mean the whole
library is losing its front matter, not just these seven. That measurement is
running; do not act on the "7" until it lands.

Detection shape, corrected: NOT chars/page (which measures the extractor).
The signal is **`chars_total` divided by the raw page-text total** — a
sectioning-retention ratio. Nothing in the corpus computes it today.


## MEASURED, and FIXED upstream: not corpus-wide, but 18 documents keep under 50%

The retraction above left one thing open — whether the `split_sections`
prefix-drop is 7 documents or the whole library. Measured across **623
documents**, as the fraction of raw pypdf page text surviving sectioning:

    median 0.977, mean 0.945
      <50%:  18 docs
    50-90%:  26 docs
    90-99%: 499 docs
     >=99%:  80 docs

**Not systemic** — most documents keep essentially everything. But the tail is
severe and lands on primary sources: Kauffman's *State models and the Jones
polynomial* (7.5% kept), DeTurck-Gluck (8.4%), Neumann-Zagier x2 (9.9%),
`90-1-219` (10.4%), `arxiv-1304.4737v1` (28.9%).

**My chars/page detector was the wrong detector and I said so before measuring
— now confirmed.** It found 9 documents and MISSED five that lose 70-85%:
`arxiv-1508.01458v1` (15.5%), `arxiv-1304.4737v1` (28.9%),
`arxiv-1909.06744v1` (29.2%), `arxiv-alg-geom-9408004v1` (29.6%), `kirbycal`
(32.5%). They keep enough text to clear 400 chars/page while losing most of
the document. The retention ratio is the right signal.

**`arxiv-1304.4737v1` is the clearest case and shows the failure compounding.**
Its TOC is inferred CORRECTLY — six headings, "I Introduction" p2 through
"References" p15 — but only one is located by the title match, and that one is
"Acknowledgements" on page 14 of 18. So `sections` is exactly
`[Acknowledgements 14-18]` and the entire paper is dropped. Marks failing to
locate (the +/-2-page window, the 44-char prefix match) is a SEPARATE
weakness; the prefix-drop is what turns it into data loss.

## Fixed upstream

litlfred/folio-assistant#167 (issue #166), commit `f933f87` — emit a leading
section for everything before `marks[0]`. Id is **`sec-front-matter`,
deliberately non-numeric**: numbering it `sec-000` would shift every following
section id, and section ids are cited from `docs/audits/*` in THIS repo.

Verified before -> after `chars_total`: 2079 -> 27711 (13.3x), 4510 -> 53954
(12.0x), 5437 -> 54993 (10.1x), 4506 -> 43175 (9.6x), 8170 -> 28231 (3.5x).
On three healthy controls every pre-existing section id is preserved and only
`sec-front-matter` is added.

**Even healthy documents were losing their abstracts.** The controls recover
858-6278 chars each — the title/author/abstract block. That is the ~2% the
0.977 median represents, and it is the part a reader searches for.

End-to-end, the thing this bean was opened for: `grep coth` on the
DeTurck-Gluck sections now returns the defining line verbatim,

    ϕ0(α)  =  (—1/(4π)) coth α

i.e. Thm 1(3), the kernel the whole EM-linking front reads off. Corpus-grep
path 5 works on it.

## Still open (do not close)

1. **Re-sectioning the affected library documents in THIS repo.** The upstream
   fix changes the producer; the committed `library/*/sections/` trees are
   still the old ones. Mechanical, but it is a real tranche — and it should
   wait until #167 lands and `.folio-assistant-pin` advances, since this repo
   validates against the pinned SHA (currently `428ca5c`), not upstream main.
2. **Marks failing to locate** — 1 of 6 correct headings found on
   `arxiv-1304.4737v1`. Not addressed by #167 and not measured here.


## Both open items closed — pin advanced, 18 documents re-sectioned (#7071)

**Pin `428ca5c` -> `df28d02`.** Measured as the pin file's header demands, both
platforms against the SAME corpus (today's main, not the `9d6fa7f2c8` the old
note quotes — a before/after at different corpus commits is not a comparison,
bean `vbase`):

    428ca5c  ->  6 issue lines printed, "9 issue(s)" reported
    df28d02  ->  3 issue lines printed, "3 issue(s)" reported

The three that clear are the `Unknown field` warnings — `computation` on
`knot-periodic-table`, `authorNotes` on `tm-interaction-completeness` and
`millennium-bounds-via-surreals-intro`. Those were being SILENTLY DROPPED at
the old pin, i.e. this bump RESTORES author-facing content already on disk.
It also confirms AGENTS.md §4d's live-state claim from the qou side: against
the pinned platform the fields really were still dropped.

Incidental: the old platform's printed list and its own count disagreed by 3
(6 shown, 9 claimed); the new one's agree.

**Re-sectioned the 18: 162,280 -> 669,287 chars (+507,007, 4.1x)**, range
2.2x-13.3x. The goal was greppability and it holds: `grep -rl coth
library/0406276v1/` now hits `sections/sec-front-matter.md` — Thm 1(3),
`phi_0(alpha) = -coth(alpha)/4pi`, the kernel the EM-linking front reads off
and which path 5 previously reported as absent.

Scope was checked BEFORE running: `pdf-structure` derives `doc_id` from the
arXiv stamp while the directory is named from the filename, so a mismatch
writes a new tree and orphans the old one (the `qou-cvx9` trap). All 18
matched; exactly 18 dirs touched, no orphan.

**Attribution is NOT all #167, and I checked rather than assumed.** The pin
also carried 172 commits, some touching heading inference. 16 of 18 gained
exactly `sec-front-matter` and nothing else (that is #167 alone). Two
exceptions: `bujack` 2->2 sections yet 2.5x text — both old sections started
at p7, so the entire paper (34,032 chars) was dropped; #167 added it AND the
newer platform rejected a bogus figure-caption mark. `arxiv-hep-th-0006111v2`
5->7, where the extra is a further MIS-INFERRED heading.

## Still open (do not close)

1. **Heading inference mis-locating.** #167 stops the prefix-drop becoming
   data loss; it does not fix the inference. `arxiv-1304.4737v1` is the type
   case — TOC inferred CORRECTLY (six headings, "I Introduction" p2 through
   "References" p15) and only one located, the second-to-last.
   `arxiv-hep-th-0006111v2`'s section titles are formula fragments
   (`(zeta, {mu}) = zeta`). Not addressed here or upstream.
2. **The other ~605 documents.** Median retention 0.977, but that residual
   ~2 % is the title/author/abstract block, which the same fix recovers
   (858-6,278 chars measured on three healthy controls). A 600-document diff
   and its own reviewable decision.
