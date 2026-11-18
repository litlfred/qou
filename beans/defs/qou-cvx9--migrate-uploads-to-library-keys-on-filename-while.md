---
# qou-cvx9
title: migrate-uploads-to-library keys on filename while pdf-structure keys on the arXiv stamp — divergence silently creates orphan doc dirs
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-09-06T13:48:45Z
updated_at: 2026-10-04T15:14:58Z
parent: qou-5vkl
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

## Update 2026-09-07: Part A LANDED in #6978; Part B still gated

**Part A (the guard) is written, calibrated and pushed** — PR #6978, issue #6976.
`scripts/migrate-uploads-to-library.py` now refuses to create a `library/<doc-id>/`
with no `structure.json`, at **both** entry points (a flat PDF, and a directory
under `uploads/`), with a non-zero exit and a printed remedy.

Three changes, and the split matters because they catch different things:

1. the arXiv-id fallback checks **both** roots, not `uploads/` only;
2. an unresolvable flat PDF is REFUSED, not moved;
3. same refusal for an un-ingested directory under `uploads/`.

**Calibration, because a guard never seen to fail is not evidence.** Each change
was reverted ALONE and `--selftest` re-run: three distinct failure signatures,
PASS only with all three. The selftest carries six cases including two negative
controls (`0406242v4.pdf`, the bean's own old-style-id document that landed
correctly, and an ordinary fresh ingest) — over-matching would block working
cases.

### CORRECTION to this bean: which half of the fix carries the measured case

This bean's framing — `pdf-structure.py` skips an ALREADY-HELD document — needs
one qualifier that changes the answer. In the measured incident the sectioned
copy was on the **other branch**, not in the working tree `migrate` ran against;
that is why `git merge-tree` reported `rename/rename` rather than a duplicate.
So the both-roots fallback could **not** have recovered `1808.02836v2` or
`2108.09349v2`: `library/arxiv-1808.02836v2/` was not there to be found.

**The REFUSAL carries the measured case.** The fallback carries a different and
larger class — where the held copy *is* local. Measured on `main`: `source.file`
is the ingest-time basename, and **226 of 633** `structure.json` carry a `doc_id`
that is neither the stem nor `arxiv-<stem>`, so `build_mapping`'s `source.file`
loop misses a third of the corpus and the fallback is what runs. Both cases are
in the selftest so the two are never conflated.

My first selftest failed to make this distinction and PASSED against the
un-fixed fallback — the held `structure.json` I wrote had a `source.file`
matching the upload, so the first loop claimed it and the fallback was never
reached. A selftest that passes on the broken code is worth nothing; it was only
found by reverting the fix deliberately.

### A self-inflicted defect, caught by the script's own `--verify`

The first draft wrote `"uploads/1808.02836v2.pdf"` as a literal in the selftest.
`rewrite_refs` scans every tracked `.py` **including this one**, so `--verify`
reported it as a stale reference and `--apply` would have REWRITTEN the script's
own source, silently breaking the test that guards the rewriter. Fixture names
are now assembled. Found by running `--verify` on the real tree, not by reading
the diff.

### `--verify` now reports the class

`library/ dirs with no structure.json: 22` — **reported, not counted**,
following this file's own convention for pre-existing conditions. Counting them
would make `--verify` permanently red, and a permanently-red gate gets ignored:
the same end state as the unfalsifiable check this file's ledger comment already
records the cost of.

### Part B remains OPEN and gated

#6962 and #6964 are both still open and both write `library/INDEX.md`. Verified
`main` `805f11d62d` independently of any script: **22** orphan dirs, names
matching this bean exactly. Intent posted on both siblings.

### ~~`qou-b9c3` does not exist~~ — RETRACTED, see the section below

This bean originally carried that claim and it was posted on #6964. It is
**wrong**; `qou-b9c3` is real. Retracted there and corrected below.

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


## 2026-09-07 — the guard is SOUND and was BYPASSED; my prediction was wrong

I predicted this bean's guard would miss the canonically-named orphan shape (arxiv-0705.2975v1,
a dir already named canonically, holding only its PDF). **Tested; the prediction is refuted.**

**The guard works.** Reproduced the exact shape in a synthetic repo — 2 ingested artefact dirs plus
one bare skipped PDF, the same mix as the real commit:

    REFUSED 1 move(s) — target has no structure.json:
        uploads/0705.2975v1.pdf
            target library/0705.2975v1/ has no structure.json

It is prefix-agnostic: has_structure() keys on structure.json PRESENCE, not on the arxiv- prefix.
My stated reason for expecting a miss was wrong about what the guard keys on. (Note also that with
no ingested artefacts at all the script bails before any move — an even stronger refusal.)

**So the orphan came in by another route.** 588ed02d5fc created it at 11:38 as a
plain rename — "R100 uploads/0705.2975v1.pdf -> library/arxiv-0705.2975v1/0705.2975v1.pdf"
— with no structure.json in the commit, two hours AFTER the guard landed at 09:21
(08d1fa9d4fd, verified an ancestor via git merge-base --is-ancestor). A hand git mv,
or a tool that is not this script.

That is the row-33 class in the detector-blindness taxonomy: **a guard installed on one of an API's
several write paths** (bean qou-3ral). The repair is not a second entry-point guard.

**Added: scripts/library-orphan-audit.py** — checks the INVARIANT over library/ itself, which no
write path can bypass: (1) no dir lacks both sections/ and ocr/; (2) dirs - INDEX rows ==
duplicates + containers + orphans with residual 0.

Live on main: 661 dirs, 637 rows, gap 24 = 23 dup + 1 container + 0 orphans, residual 0 — OK.
Replayed against history via git ls-tree: 23 orphans at 588ed02d5fc, 0 on main now. It would have
caught all 23, including the one the write-path guard could not.

--selftest is calibrated by REVERTING the condition (plant orphan -> must be DETECTED and report()
must return non-zero; remove it -> must be clean), not by observing a pass.


---

## 2026-09-13 — three fresh instances of the known blanket-rewrite cost, one of which FALSIFIES a record

Hit while ingesting `library/arxiv-astro-ph-0203462v1/0203462v1.pdf` (owner upload `7ac8aacd5f`, Hill
et al. 2002 on CS 31082-001). **Not a new defect class** — this script's own
header already documents it at lines 28-39 and 271-272: the rewrite is total
*by design*, including beans, to avoid ~485 dangling references, and
*"blanket rewrite cannot tell a citation from a sentence"*. Recording three
live instances, because two of them are worse than a dangling link.

`--apply` rewrote three files that were narrating history, not linking:

1. **`.beans/qou-4lbh`** — *"a correct path update, `uploads/roth_lemma.pdf`
   -> `library/roth-lemma/roth_lemma.pdf`"* became
   *"`library/roth-lemma/roth_lemma.pdf` -> `library/roth-lemma/roth_lemma.pdf`"*.
   An arrow from a thing to itself. Nonsense, but visibly so.

2. **`.beans/qou-cvx9` (this bean)** — *"The first draft wrote
   `uploads/1808.02836v2.pdf` as a literal in the selftest"* became *"wrote
   `library/arxiv-1808.02836v2/1808.02836v2.pdf` as a literal"*. **This one
   falsifies a historical claim**: the first draft did not write that. The
   sentence is now confidently false rather than obviously broken, which is
   the more expensive failure.

3. **`scripts/library-orphan-audit.py`** — a docstring quoting git's own
   output, *"`R100 uploads/0705.2975v1.pdf -> library/arxiv-0705.2975v1/...`"*,
   became `R100 library/... -> library/...`. A rename record with identical
   source and target is not a rename; verbatim quoted evidence, now wrong.

All three **reverted** rather than committed. They will be rewritten again on
the next `--apply`, so this is a recurrence, not a repair.

**The pattern worth naming:** the files hit are the ones *describing the
migration itself*, because those are exactly the files that legitimately
contain `uploads/` paths as historical text. So the script's blast radius is
biased toward its own documentation — and toward the beans a future agent
would read to understand it.

**NOT FIXED, and deliberately not.** The obvious fix (skip `.beans/`, or skip
lines containing an arrow, or require the path to resolve) is a change to
somebody else's script, is neither a precision increase nor corpus-derived,
and therefore needs the owner per AGENTS.md 2026-09-07. Put here for that
decision rather than made.

---

## Update 2026-09-06: the pipeline is being run CONCURRENTLY by three agents, which raises the guard's value

Measured on `origin` while coordinating #6942's merge — **three open PRs are draining
`uploads/` at once**, and their document sets nest:

| PR | doc dirs touched | writes `INDEX.md` |
|---|---|---|
| #6955 | **20** | yes |
| #6962 | **12** | yes |
| #6964 | **15** | yes |

All 12 of #6962's dirs are in both others: **12 ⊂ 15 ⊂ 20**.

The *content* is the same, not merely the scope. `git rev-parse <branch>:library/<doc>`:

```
arxiv-0902.0350v1   : 6962 tree == 6955 tree ;  6964 +1 file (the PDF)
arxiv-2601.07906v2  : 6962 tree == 6955 tree ;  6964 +1 file (the PDF)
```

So #6962 and #6955 produce **byte-identical trees** for the shared documents, and
#6964 is #6962's ingest plus the migrate step.

### Why this belongs on this bean

The orphan defect above is a silent failure on the **skip** path. A skip is common
precisely when *another agent has already ingested the document* — which is the
normal state when three PRs run the pipeline concurrently. So the concurrency does
not merely duplicate effort; it **drives traffic through the exact path that
produces invisible orphans**. The guard (refuse to move a PDF into a dir with no
`structure.json`) is what turns that into a loud skip.

### The other cost, which is not this bean's to fix

All three regenerate `INDEX.md`, so two of the three conflict on it, and a
hand-resolved index conflict is how rows go missing. The index already carries
that damage: **642 dirs against 589 rows**; subtracting the 23 duplicates whose
row is correctly omitted leaves **8 sectioned documents with no row**, invisible to
tier 1 of corpus-grep path 5 while their sections sit on disk.

Coordination comments posted on #6962 and #6964 with the measurements and a stated
recommendation (land the superset, let the others reduce to no-ops) marked as
judgement. Neither PR was touched.

### Standing hazard, not a one-off

`uploads/` is a **live incoming queue**, not a one-time backlog (AGENTS.md corrects
this explicitly). So "N agents ingest the same drop" recurs every time the owner
drops PDFs, and nothing in the pipeline claims ownership of a drain. Worth a
claim mechanism — a bean claimed before draining, or a marker file — but that is a
process proposal, not written here.

In-progress in Round 102 PR litlfred/qou#8453.
