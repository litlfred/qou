---
# qou-hs0c
title: 'A library document can be fully sectioned with no ocr/ dir and still be unsearchable: O''Hara 1991 is OCR-destroyed, and ''greppable: yes'' in PR #7315 was wrong'
status: todo
type: task
priority: normal
created_at: 2026-09-13T16:51:33Z
updated_at: 2026-09-13T16:52:42Z
---

Found by doing exactly what `qou-o6ml` instructs — *"re-run path 5 before the
next 'this is open' or 'no theorem exists' declaration on this arc"* — after the
knot-energy ingest landed.

## The corrected claim, and it is mine

PR #7315 (merged) reports `O'Hara's own paper greppable: yes`. **True only in
the sense that grep executes.** `library/1-s20-0040938391900102-main/` is
O'Hara, *Energy of a Knot*, Topology **30**(2) 1991 — a SCANNED pre-digital
paper — and a grep of its sections for the vocabulary the paper is built on
returns **zero on every term**:

    intrinsic distance | regulariz* | renormaliz* | geodesic distance
    | Mobius | arc length | shorter arc          ->  0 hits

Not because the concepts are absent. The OCR destroyed the mathematics. Its
proof section reads, where an integral belongs:

    I;,,$_~), ~;,(,)~(~l~"'~+~~~~'~z+'+~~~"'i~+~:'lli")r-'di
    b'((S - I). b'(l) 2 2((r + a)-' -2(S+a)-'--2(~+u+2r)~')

This matters beyond bookkeeping: O'Hara 1991 is the PRIMARY for the whole
`qou-pc85` / `qou-zfs6` / `qou-o6ml` route-2 arc, and path 5 cannot answer a
question about it.

## 🛑 A NEW blind-spot variant — the documented discriminator does not fire

AGENTS.md documents a tier-4 trap: *text lives in `ocr/`, `sections/` holds a
stub*, discriminator **does an `ocr/` directory exist**. This document has
**no `ocr/` directory at all** — the degraded OCR *is* the `sections/` content.
Page ranges cover the whole paper (1-4, 4-7), the byte count is unremarkable
(13,443 B / 2 sections). Every documented check passes. A reader following the
tier-4 advice finds no `ocr/`, concludes the sections are good, and greps rubble.

## TWO DISCRIMINATORS THAT DO NOT WORK — do not re-spend them

1. **Whole-document OCR-fidelity statistics.** Clean-token rate + maths-marker
   density put O'Hara at **69.5 % / 3.52 per kchar**, inside the healthy
   cluster's **69.4–77.7 % / 2.18–4.45**. `arxiv-1904.13129v1`, a healthy arXiv
   paper, scores LOWER on clean-token rate. It fails because the PROSE is
   largely intact — the front matter reads fine — and only the mathematics is
   destroyed, which a word-level statistic cannot see.
2. **Per-section token density.** Fires on **13 of 20** sections of a healthy
   paper; `tok/kchar < 90` just means "maths-dense", true of most of a maths
   paper.

Do not fish for a third threshold. Trying variants until one separates a sample
of one is selection against the target.

## WHAT DOES WORK — `scripts/library-ingest-fidelity-probe.py`

**Hypothesis, stated before it was run:** a healthy ingest reproduces most of
its own abstract's content words somewhere in its body; a maths-destroyed one
does not. `doc_brief` is extractive from the abstract, so the terms come from
the document itself rather than from a judgement about it.

Knot-energy cluster (14 docs): O'Hara **60.0 %** (3 of 5 terms); every other
**85–100 %**, twelve of thirteen at exactly **100 %**.

## 🟩 THE VALIDATION IS NOT FISHED — it recovers the DOCUMENTED class blind

Run corpus-wide over **704** scorable documents, the eight lowest scorers are
all **0.0 %**, and every one carries the documented tier-4 signature: exactly
**1 section**, `sections/` holding **1.5 %–6.4 %** of its text against a large
`ocr/`.

    1992evansberger    4.1%      bm-markov-j          2.2%
    67-6-1860          6.4%      centsim              1.5%
    mcmullen-braids-hodge-2013 2.5%   procrsoclondona92  4.8%
    yanagihara-1980-...  3.7%    yuasa-rims-...       5.0%

**`procrsoclondona92` and `1992evansberger` are the two AGENTS.md names by
hand** as the worked cases for that trap. The probe **reads only `sections/`**
— it never looks at `ocr/` — so recovering all eight is independent
corroboration, not circularity. Two distinct failure modes, one statistic, and
the second mode was previously undetectable.

## The triage queue, split honestly

    scored                      704
    carry an ocr/ dir            26
    flagged (< 75 %)             88
      with ocr/                  11   the documented class
      WITHOUT ocr/               77   invisible to the documented check

**11 of 26 `ocr/` docs flagged is correct behaviour, not a miss** — median
recall among `ocr/`-carrying docs is 84.6 %, so most have healthy sections
*and* an `ocr/`. Carrying `ocr/` is not itself a defect.

🛑 **88 is a TRIAGE QUEUE, not 88 broken documents.** A short or venue-heavy
`doc_brief` depresses recall benignly. The floor (75 %) describes known-bad
points; it is **not calibrated**, and the positive sample is small. A flag means
*open it and look*, never a verdict.

## NOT CLAIMED

That the O'Hara ingest can be repaired here (needs a better OCR pass over the
source scan); that any of the 77 no-`ocr/` flags beyond O'Hara is genuinely
degraded (none triaged); that the recall statistic survives a larger sample.

Cross-links: `qou-o6ml` (the arc whose path-5 instruction found this),
`qou-pc85` / `qou-zfs6` (route 2, for which O'Hara 1991 is the primary), #7315
(the merged PR carrying the corrected claim), #7322.
