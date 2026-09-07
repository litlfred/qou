---
# qou-b9c3
title: 22 PDFs sit in library/ never sectioned — a third un-ingested population, invisible to every path-5 tier
status: in-progress
type: task
priority: normal
created_at: 2026-09-06T09:42:46Z
updated_at: 2026-09-07T08:58:30Z
---

## What was found

`library/` holds **639 directories**. `library/INDEX.md` holds **593 rows**
after regeneration this session (589 before). The gap is **46**, and it is
**not** all duplicates:

| population | count | shape on disk |
|---|---|---|
| duplicate copies (`duplicate_of` in section front-matter) | 23 | full ingest, deliberately no row |
| bound-journal container (`ant-v14-n7-s`) | 1 | `container_note`; all 10 `container_children` indexed |
| **never ingested** | **22** | one file — the PDF — and nothing else |
| total | 46 | |

The 22 hold **exactly one entry each**: the PDF. No `sections/`, no `ocr/`,
no `structure.json`, no `candidates.json`, no index row.

```
0008027v1  0110009v3  0308152v1  0410111v2  0603444v2  0605242v1
0803.1227v1  0806.2317v1  1.9781611972443.fm  1012.4941v2  1408.3518v3
1905.02045v3  1907.00949v2  2023unat1343  2108.03616v2  2203.06568v4
2404.02087v1  2603.12136v1  amc_2730  fulltext  m4-24
exploring-the-geometric-buchberger-algorithm-in-integer-prog
```

## Why it matters

**These are invisible to every tier of corpus-grep path 5**, while sitting in
`library/` — the directory AGENTS.md says *is* the searchable one. Tier 1
(`INDEX.md`) has no row; tier 2 (`summary.json`) does not exist; tier 3
(`sections/`) does not exist; tier 4 (`ocr/`, the tier added 2026-08-30
precisely because `sections/` misses things) does not exist either. So a clean
path-5 result is not evidence the corpus lacks a source — the same conclusion
the `ocr/` note reached, one population further out.

They are a **third distinct population**, not a re-description of a known one:
they are not in `uploads/`, and none of them appears in `qou-k1hs`'s list of 19.

## Mechanism

`qou-k1hs`'s own working recipe is four steps ending in
`git mv uploads/<f>.pdf library/<doc-id>/`. Running that `git mv` **without**
the preceding `scripts/pdf-structure.py` produces exactly this shape: a
directory named for the doc-id, holding only the PDF. The fix per file is to
run the ingest steps that were skipped; `scripts/migrate-uploads-to-library.py`
is the supported path for one that is still in `uploads/`.

## Correction to AGENTS.md — the prescribed check is wrong as stated

AGENTS.md §"Before declaring open" path 5 says:

> check the arithmetic before trusting tier 1: `directories − index rows`
> should equal the duplicate count, and when it does not the index is behind.

Here that gives **46 vs 23** and reads as *"the index is behind"*. The index
**was** behind — regenerating recovered 4 rows — but that accounts for 4 of the
46, and running the producer to convergence still leaves 23 of the gap
unexplained by duplicates. The correct decomposition is

```
directories − index rows = duplicates + containers + never-ingested
```

and only the middle term is discretionary. A residual after regeneration is
**not** an index-staleness signal; it is an ingest-backlog signal, and the two
have opposite remedies (`summarize-library.py --apply` fixes the first and
cannot touch the second). Recording it here rather than editing AGENTS.md in
this bean's PR so the wording change can be reviewed on its own.

## Next step

Ingest the 22 (`pdf-structure.py` then `extract-candidates.py` per
`qou-k1hs`), then `summarize-library.py --apply` once, and re-run the
three-way arithmetic above as the check.


## 2026-09-06 (later) — a sibling landed the library work, and we found TWO DIFFERENT populations both called "orphans"

`main` moved under this bean while it was being written. `2c567cca9c` drained
the uploads backlog (17 PDFs ingested, INDEX 589 → 606), `14a7bb5a2d` regenerated
the index (606 → **609**), and `805f11d62d` filed **`qou-cvx9`**, which reports
*"the orphan class is 22 documents and pre-dates this session"*.

**The index half of this bean is fully superseded.** My regeneration
(589 → 593) is subsumed; re-running `summarize-library.py --apply` on merged
`main` produces a **byte-identical** `library/` tree, so main is already at the
generator's fixed point. Nothing of mine survives there and nothing should.

**The arithmetic correction stands, and now closes exactly** on the larger tree:

    dirs 655 − rows 609 = 46 = 23 duplicates + 1 container + 22 never-ingested

### 🛑 But `qou-cvx9`'s MECHANISM explains ZERO of the 22 — measured

`qou-cvx9` diagnoses a real defect: `migrate-uploads-to-library.py` keys the
doc-id on the **filename** while `pdf-structure.py` keys it on the **page-1
arXiv stamp**, so a PDF named `1808.02836v2.pdf` lands at `library/1808.02836v2/`
(one file) *beside* the fully-ingested `library/arxiv-1808.02836v2/`. Their two
measured instances are `1808.02836v2` and `2108.09349v2`.

That produces an orphan **with a twin**. Checked every one of the 22 on merged
`main` for an `arxiv-<id>` sibling directory:

    orphans with an arxiv- twin :  0
    orphans without            : 22

and the two they named are **not on `main` at all** — no orphan dir survives for
either; only their `arxiv-` twins do. So their defect was caught and did not
land, which is the good outcome, and it is a **different population** from the 22.

Nine of the 22 are not even arXiv-shaped — `amc_2730`, `fulltext`, `m4-24`,
`2023unat1343`, `1.9781611972443.fm`,
`exploring-the-geometric-buchberger-algorithm-in-integer-prog` — so there is no
arXiv stamp for a filename to diverge from. The mechanism cannot apply to them
even in principle.

**The two populations differ in the way that matters for path 5:**

| | `qou-cvx9`'s orphans | the 22 here |
|---|---|---|
| twin doc dir | **yes**, fully ingested | **no** |
| corpus holds the document | twice, findable once | **once, findable never** |
| on `main` today | 0 | 22 |
| mechanism | filename vs arXiv stamp | **still unidentified** |

So *"the corpus holds the document twice and a check finds it once at best"* is
true of theirs and **not** of these: for the 22 there is no second copy to find.

**My own earlier guess is retracted too.** This bean said the mechanism was
running `qou-k1hs`'s final `git mv` without the preceding `pdf-structure.py`.
That is consistent with the shape but I never measured it, and `qou-cvx9`
finding a *different* real mechanism for a *different* population is a reminder
that a plausible story for a shape is not a diagnosis. **The mechanism for these
22 is open**, and the honest next step is to date them (`git log --diff-filter=A`
on each PDF) rather than to reason from the shape again.

Nothing in this contradicts `qou-cvx9`; it narrows what that bean's fix will
close. Their guard belongs in `migrate-uploads-to-library.py` regardless.


## 🛑 2026-09-06 (later still) — the decomposition was NOT mine; a sibling posted it first

Read the #6962 thread properly, which I should have done before commenting on
it. Comment `5559854490`, **2026-09-06T14:23:14Z** — eleven minutes before mine
(`5559920028`, 14:34:21Z) — already carries:

> `main` now carries **22 orphan doc dirs** — a bare PDF with no
> `structure.json`, invisible at *every* tier of corpus-grep path 5. … `INDEX.md`
> is at **609** rows on `main` and the arithmetic closes with no residual:
> `655 dirs − 609 rows = 46 = 23 duplicates + 22 orphans + 1 container`
> (`ant-v14-n7-s` is a bound journal issue; `summarize-library.py:98` skips
> containers by design).

That is the same count, the same three-way split, and the same container. **This
bean should not be read as the origin of any of it.** Their citation is also the
better one: `summarize-library.py:98` skips `container` **and** `duplicate_of`
in one branch with the rationale written above it (*"the point of the scan tier
is one line per work"*), where this bean reached the container by reading its
`container_note` by hand.

**What survives as this bean's own contribution, measured and not in theirs:**

1. **`qou-cvx9`'s mechanism explains ZERO of the 22** — 0 of 22 have an
   `arxiv-<id>` twin, and nine are not arXiv-shaped at all, so the
   filename-vs-stamp divergence cannot reach them even in principle. Their
   comment says the 22 "pre-date this session"; it does not say the mechanism
   fails to account for them, and the two claims are different.
2. **"held twice, found once" vs "held once, found never"** as the distinction
   that matters for path 5.
3. **AGENTS.md path 5's stated arithmetic is wrong as written** — it says
   `directories − rows` should equal the *duplicate count*, which reads as index
   staleness when the residual is an ingest backlog. Neither sibling comment
   says this; both simply use the correct form.

**The lesson, and it is the one this session keeps re-learning in new places:**
the corpus-grep discipline applies to a **PR thread**, not only to `content/`,
`docs/`, `computations/`, `library/` and `.beans/`. I checked five corpora and
not the two comments already sitting on the PR I was about to comment on.
Posted the correction as `5562781339`.


## 2026-09-07 — DRAINED. 23, not 22 — and the defect IS still producing

Claimed and drained on branch claude/library-ingest-invisible-23-2026-09-07.

**The count was 23, not the 22 this bean lists.** The extra is arxiv-0705.2975v1, which arrived
TODAY in 588ed02d5fc (11:38, 'ingest: five q-difference Stokes / difference-Galois uploads') —
after the stability measurement recorded in qou-cvx9, which concluded 'the defect is NOT actively
producing'. That conclusion is now falsified: a 23rd orphan appeared after it was written. Note
this one has the CANONICAL dir name already (arxiv-0705.2975v1 holding 0705.2975v1.pdf), so it is
a different shape from the 22 filename-keyed ones and would not be caught by a guard keyed on the
arxiv- prefix divergence alone.

**Result: 23 ingested, 0 failed.** 18 PDFs moved into their canonical doc dirs, 18 orphan dirs
removed; 5 were already canonically named. INDEX.md 614 -> 637 rows.

**The index arithmetic now closes exactly, residual 0:**

    661 dirs - 637 rows = 24 = 23 duplicates + 1 container (ant-v14-n7-s) + 0 orphans

(was 46 = 23 + 22 orphans + 1 container).

**🛑 ONE of the 23 is NOT actually searchable, and is now WORSE than absent.**
exploring-the-geometric-buchberger-algorithm-in-integer-prog is a SCANNED pdf with no text layer:
pdf-structure reports '0kc SCANNED?' and its single section file is 295 bytes of FRONT-MATTER with
ZERO body text. Measured: grep -c Buchberger on that file = 1, and on the body with front-matter
stripped = 0. So the ingest gave it a sections/ dir that produces a grep HIT ON ITS OWN FILENAME
while containing nothing — a false positive, which is a worse failure than being invisible. It
needs OCR (the ocr/ tier), not sectioning. Tracked as the remaining work.

The other 22 carry real body text (24kB to 390kB each; m4-24 alone is 111 sections / 390kB).
