---
# qou-4n9o
title: 'library: INDEX.md misses 4 fully-sectioned documents and 23 directories were never sectioned'
status: completed
type: task
priority: normal
created_at: 2026-09-07T07:17:06Z
updated_at: 2026-09-07T17:20:18Z
---

Measured 2026-09-07 while ingesting the owner's 8 q-difference uploads (a23d06ce2c).

AGENTS.md prescribes the invariant `directories − index rows = duplicate count` and says a failure means INDEX.md is behind. It is behind, and in TWO different ways that need different fixes.

    dirs = 661   INDEX.md rows = 615   gap = 46
      19  marked `duplicate_of`      — correct, these get no row by design
      23  ZERO sections              — PDF present, NEVER sectioned; not an index
                                       bug at all, an ingestion backlog
       4  fully sectioned, NO row    — the real index defect

**The 4 that are sectioned and invisible to tier 1** — this is the tier every agent is told to read FIRST, so these are documents corpus-grep path 5 cannot find by its documented route:

    ant-v14-n7-s                            170 sections
    s40687-023-00400-3                       13 sections
    gt-v10-n3-p07-p                          12 sections
    neumann-zagier-1985-...(two dirs)         2 sections each

`ant-v14-n7-s` at 170 sections is a whole document. The two `neumann-zagier` dirs are probably the known NZ triplicate AGENTS.md mentions and may be legitimately duplicate-adjacent — check before adding rows.

**The 23 with zero sections** are a separate problem: they hold a PDF and no `sections/`, so they are invisible to a text grep entirely. Several have opaque names (`1.9781611972443.fm`, `fulltext`, `amc_2730`, `m4-24`) which is presumably why they were skipped. Fix is to run folio-assistant `scripts/pdf-structure.py` over them, and route any with no text layer to the OCR tier (AGENTS.md records 25 directories already in that state).

**Note for whoever does this — the platform version matters.** Regenerating sections with the PINNED platform (`428ca5c`) is a REGRESSION on documents whose sections were produced later: it drops `doc_brief` from section front-matter (the field path 5 relies on to make a hit interpretable) and appends the author line to `doc_title`. Measured on `arxiv-0903.0853v3` + `arxiv-1404.2541v1`: 237 files, −786 lines. Reverted rather than committed. Run `scripts/summarize-library.py --apply` afterwards, which restores `doc_brief`, or bump the pin deliberately.

Not fixed here — out of scope for the branch that found it.


---
**RESOLVED 2026-09-07 — and TWO of my three claims in this bean were wrong. Re-measured on current main before acting.**

    when I opened it (~09:00)   dirs 661, rows 615, gap 46 = 19 dup + 23 zero-section + 4 real
    now                          dirs 661, rows 640, gap 21 = 20 dup + 1 container + 0 real

**Claim 1, "23 directories were never sectioned" — GONE, and not by me.** Zero remain. Someone sectioned them between my measurement and this one. Half this bean closed itself.

**Claim 2, "`ant-v14-n7-s` carries 170 sections and is invisible to the tier every agent is told to read first" — WRONG, and it was the flagship complaint.** It is *Algebra & Number Theory* Volume 14 No. 7 — a **journal issue**, carrying `container: true` in its `structure.json`. `build()` excludes containers deliberately: *"A container holds other documents; a duplicate is another copy of one already in the index. Neither should occupy its own index line — the point of the scan tier is one line per **work**."* And its ten constituent papers **do** have directories and index rows (`ant-v14-n7-s-p01` … `-p10`, all 10 present). Nothing is invisible. I measured the symptom (no row) and asserted a cause (indexer defect) without reading the design.

**Claim 3 — the only real one: 3 documents genuinely had no row.** `neumann-zagier-1985-volumes-of-hyperbolic-three-manifolds`, its `-co` sibling, and `the-period-matrix-of-bring-s-curve-1hik02mwva` (on this corpus's own subject). All three passed `build()` and *would* emit a row — so INDEX.md was simply **stale**, not broken. `python3 scripts/summarize-library.py --apply` added them. Real gap now **0**.

**The durable fix, which is worth more than the three rows.** AGENTS.md stated the invariant as `directories − index rows == duplicate count`. That is **short by the containers**, so it fails (24 ≠ 20 as I measured it) on a healthy tree and invites exactly the wrong conclusion — the one I drew. Corrected in AGENTS.md to

    directories − index rows  ==  duplicates + containers

with the measurement (661 − 640 = 21 = 20 + 1, exact) and the reason the distinction is easy to miss: **`build()` returns `None` for a container and for a duplicate with no diagnostic either way**, so a genuinely un-indexed document is indistinguishable from a designed exclusion without opening its `structure.json`. The classification recipe and the `--apply` fix are recorded there.

Completing: the real gap is closed, the stale index is regenerated, and the misleading invariant that caused my own misdiagnosis is fixed at the source. No open conjecture here, so §13a does not apply.
