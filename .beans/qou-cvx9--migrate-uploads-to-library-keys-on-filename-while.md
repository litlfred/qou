---
# qou-cvx9
title: migrate-uploads-to-library keys on filename while pdf-structure keys on the arXiv stamp — divergence silently creates orphan doc dirs
status: in-progress
type: task
priority: high
created_at: 2026-09-06T13:48:45Z
updated_at: 2026-09-07T04:56:58Z
---

Found pre-merge on #6955 while probing its merge ordering against #6942. **A defect
in the branch, not a merge artifact** — it lands orphan documents on `main` whether
or not #6942 exists.

## The two scripts disagree on what a document's identity is

| script | derives doc-id from |
|---|---|
| `scripts/pdf-structure.py` | the **page-1 arXiv stamp** — `arxiv-1808.02836v2` |
| `scripts/migrate-uploads-to-library.py` | the **filename** — `1808.02836v2` |

For every PDF whose filename lacks the `arxiv-` prefix these disagree. `migrate`
does not detect that: it creates `library/<basename>/` and moves the PDF in,
producing a directory holding **one file** — no `structure.json`, no `sections/`,
no `INDEX.md` row.

## Measured

`git ls-tree -r --name-only` on `origin/claude/uploads-library-ingest-2026-09-06`:

| orphan created | files | the real doc dir | files | sections |
|---|---|---|---|---|
| `library/1808.02836v2/` | **1** | `library/arxiv-1808.02836v2/` | 24 | 22 |
| `library/2108.09349v2/` | **1** | `library/arxiv-2108.09349v2/` | 22 | 20 |

`git merge-tree` surfaces them as `CONFLICT (rename/rename)`, which is how they
were caught — a merge probe, not a check anything runs on purpose.

A third skipped doc, `0406242v4`, does **not** trigger it: its old-style arXiv id
produces no `arxiv-` prefix, so both scripts agree on the path and the PDF lands
correctly beside the full ingest.

## Why it is worse than a cosmetic duplicate

The orphan is **invisible to corpus-grep path 5** at every tier — no `INDEX.md`
row (tier 1), no `summary.json` (tier 2), no `sections/` (tier 3), no `ocr/`
(tier 4). So the corpus holds the document twice and a `has the corpus got this?`
check finds it once at best. That is the precise failure mode the `uploads/` →
`library/` pipeline exists to close, reintroduced by the last step of the pipeline
itself.

## The trigger is the SKIP path, which is the part worth remembering

`pdf-structure.py` correctly **skips** an already-held doc and emits nothing.
`migrate` then moves that PDF anyway, and having no ingest output to consult,
falls back to the filename. So the orphan is produced exactly when the upstream
step did the right thing — a skip is indistinguishable from a fresh ingest at the
`migrate` boundary.

## Proposed guard (NOT written — flagged, per anti-speculation)

`migrate-uploads-to-library.py` should **refuse** to move a PDF into a target dir
that has no `structure.json`, and report it rather than inventing the dir. That
turns a silent orphan into a loud skip. It should probably also consult the
page-1 stamp itself, but the refusal alone closes the invisibility.

Not implemented here: the immediate case is fixed by deleting the two dirs on
#6955, and widening that PR to change an ingest script is the author's call.

## Blast radius

`scripts/migrate-uploads-to-library.py` is the only consumer. Nothing in
`content/`, no producer, no witness, no number. The cost of leaving it is future
orphans on every bulk ingest whose filenames lack the `arxiv-` prefix.

## Default if nothing is done

The two dirs are deleted on #6955 and the script is unchanged, so the next bulk
`uploads/` drain reproduces it. `migrate --verify` reports such dirs as
"pre-existing problems", which reads as pre-existing rather than as just-created.

## Related, separate

`library/` also holds **642 dirs against 589 `INDEX.md` rows**; 23 of the gap are
duplicates whose row is correctly omitted, leaving **8 sectioned documents with no
row** — five pre-existing (`ant-v14-n7-s`, `arxiv-1111.2828v2`, `arxiv-1307.6697v2`,
`arxiv-1401.5542v1`, `arxiv-2104.07437v4`) and three from #6942. Different defect
(staleness, not identity), fixed in-flight on #6955 by re-running
`summarize-library.py --apply`, so it carries no bean of its own.


---

## Update 2026-09-06 (later): the orphan class is 22 documents, and it PRE-DATES this session

Measured after merging `main` (with #6942) into #6955 and resolving. My two were
deleted; a whole-tree scan for `library/*/` with **no `structure.json`** then found
**22 more**, every one a bare PDF:

```
0008027v1 0110009v3 0308152v1 0410111v2 0603444v2 0605242v1 0803.1227v1 
0806.2317v1 1.9781611972443.fm 1012.4941v2 1408.3518v3 1905.02045v3 
1907.00949v2 2023unat1343 2108.03616v2 2203.06568v4 2404.02087v1 
2603.12136v1 amc_2730 
exploring-the-geometric-buchberger-algorithm-in-integer-prog fulltext m4-24 
```

All are present at the merge base, so **none were created by this session** — they
are a standing corpus condition, not fallout from the three concurrent drains.

### Why these are worse than the INDEX gap

A sectioned document missing an `INDEX.md` row is invisible at **tier 1** and
findable at tier 3 (`grep -rln <topic> library/*/sections/`). These 22 have no
`sections/` at all, so they are invisible at **every tier of corpus-grep path 5** —
tier 1 (INDEX), tier 2 (`summary.json`), tier 3 (`sections/`) and tier 4 (`ocr/`).
The corpus holds the PDF and cannot find a word of it. A "has the corpus got this?"
check returns clean while the paper sits on disk.

Several names suggest exactly the mechanism this bean is about — `fulltext`,
`m4-24`, `amc_2730`, `1.9781611972443.fm` are filename-derived doc-ids, i.e. what
`migrate` produces when it has no ingest output to consult.

### Not drained here, deliberately

22 ingests is not a small related fix, and **three sibling PRs are already
contending over `library/`** (#6955, #6962, #6964). Adding 22 documents to a
four-way race would make the `INDEX.md` conflict worse for everyone. Recorded for
the owner to schedule; the fix is mechanical (`pdf-structure.py` on each, then
`summarize-library.py --apply`) and needs one owner, not a fourth concurrent one.

### The index arithmetic now closes exactly, which is how the 22 were pinned down

After regenerating on #6955: **655 dirs − 609 rows = 46 = 23 duplicates + 22
orphans + 1 container.** No residual.

### CORRECTION to this bean's earlier figure

It said **8** sectioned documents were missing a row. It is **7**. `ant-v14-n7-s`
is a bound journal **issue** — `container: true`, ten `container_children` carrying
the content — and `summarize-library.py:98` skips containers and duplicates by
design. A correct omission was counted as a defect because my scan did not know
containers existed. The other 7 now have rows.


---

## 2026-09-07 — the ORPHAN half duplicates `qou-b9c3`, which was first. This bean keeps the GUARD.

A dispatched agent reported that `qou-b9c3` "does not exist" and posted that as a
correction on #6964. **That was wrong and is retracted on that PR.** Verified
against `origin/main`:

  .beans/qou-b9c3--22-pdfs-sit-in-library-never-sectioned-a-third-un.md
    title:  22 PDFs sit in library/ never sectioned — a third un-ingested
            population, invisible to every path-5 tier
    status: todo,  created 2026-09-06T09:42:46Z,  landed d00bb1ba45

The agent searched the stem `b9c3` and hit `.beans/b9c3--author-prove-
chi21-garside-zero-...`, an unrelated COMPLETED Lean bean from 2026-07-05,
rather than searching the full id `qou-b9c3`. Two beans whose ids differ only by
the `qou-` prefix. **A stem-only grep in `.beans/` is not an existence check** —
worth remembering, since the corpus-grep checklist's path 6 is exactly this
directory.

### Consequence: split the ownership

`qou-b9c3` found the same 22 orphans **about eleven minutes before** this bean's
finding (their own commit message records the priority). So:

  * **`qou-b9c3` owns the DRAIN** — ingesting the 22. It was first, and a
    mechanical job has one owner (AGENTS.md).
  * **`qou-cvx9` (this bean) owns the GUARD** — the identity divergence between
    `migrate-uploads-to-library.py` (keys on FILENAME) and `pdf-structure.py`
    (keys on the page-1 arXiv stamp), which is what CREATES orphans. A different
    defect: the drain clears the existing 22, the guard prevents the next ones.

Part A (the guard) landed in **#6978**. Part B (the drain) is **withdrawn from
this bean** rather than merely gated — it belongs to `qou-b9c3`.

### Measurements that stand, independent of the retraction

  * orphan count stable at **22** across `origin/main` at `805f11d62d` and
    `3036bf171a`; `comm` on the two sets shows no additions, no removals. The
    defect is NOT actively producing.
  * index arithmetic closes with no residual:
    **655 dirs − 609 rows = 46 = 23 duplicates + 22 orphans + 1 container**.
  * the guard's `--selftest` was calibrated by reverting each of its three
    changes ALONE and confirming three distinct failure signatures — not merely
    by observing it pass.

### Two further findings from that work, both live

  * **`pdf-structure.py` is NOT in this repo.** It is
    `folio-assistant/scripts/pdf-structure.py`, so any drain has a second
    prerequisite: a folio-assistant clone with `scripts/fix-python-pdf-deps.sh`
    run. Whoever takes `qou-b9c3` needs this.
  * **Which half carries the measured case.** In the incident that opened this
    bean the sectioned copy was on the OTHER branch, so the arXiv-id fallback
    could not have recovered those two — **the refusal is what carries it.** The
    fallback covers a larger latent class (226 of 633 `structure.json` have a
    `doc_id` that is neither the stem nor `arxiv-<stem>`), but it is not what
    fixed the observed failure.
