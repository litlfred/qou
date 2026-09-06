---
# qou-b9c3
title: 22 PDFs sit in library/ never sectioned — a third un-ingested population, invisible to every path-5 tier
status: todo
type: task
priority: normal
created_at: 2026-09-06T09:42:46Z
updated_at: 2026-09-06T14:33:09Z
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
