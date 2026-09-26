# `fsh-guts/deprecated/root-scratch/`

**95 files that were tracked at the repository root and should not have been.**
Session leftovers from past work: one-off probe scripts, batch files, scratch
JSON, throwaway `.lean` files.

Moved 2026-09-26 on the owner directive *"the qou audit docs and such should be
moved under `docs/`"*, read together with *"put heavy client side stuff (pre
Skills/Tools) it in `fsh-guts/` under deprecated or so"* and *"we can pull out
later if we need."*

**Kept, not deleted.** AGENTS.md rule 9 and the owner's own "pull out later".

## The numbers

| | |
|---|---:|
| root tracked files before | **145** |
| root tracked files after | **28** |
| moved here | **95** |
| moved to `docs/_archive/orphan-top-level/` earlier the same day | 11 |
| held back deliberately | 11 |

Composition of the 95: 39 `.py`, 18 extensionless (`amalgamated_batch_a…q`),
12 `.json`, 11 `.txt`, 7 `.lean`, 6 `.sh`, 2 `.sing`.

## Why here and not `docs/_archive/orphan-top-level/`

That directory is **markdown only** — 43 files, zero of any other type — and its
own README states the purpose as orphaned *documents*. These are scripts and
data. Mixing them would make "an orphaned document" and "an abandoned script" one
category, and they are not: a stale document is still readable, whereas most of
these do not run.

## What was HELD BACK, and why

Eleven root files were candidates by shape and were kept at the root:

- **Generated manifests the `gh-pages` build publishes at the root** —
  `glossary.json`, `mapping.json`, `proof-objects.json`. AGENTS.md's
  "Expected gh-pages contents" table lists all three.
- **Referenced by live tooling** — `qou-all-tables.tex`
  (`scripts/make-all-tables.py`), `standalone-index-of-definitions.tex`.
- The remaining six are ordinary root files (`main.tex`, `references.bib`, …).

## Three of these files were quietly broken before the move

Worth recording, because it is the clearest evidence they are scratch:

- `parse_batches.py:3` opens
  `/Users/litlfred/space_cats/qou/.beans/qa-agent-drain-queue.json` — an absolute
  path to somebody's Mac.
- `find_blocks.py`, `find_blocks_fast.py`, `find_blocks_py.py` open
  `/Users/litlfred/space_cats/qou/lean-qa-report.md`, likewise.
- `append_ledger{,_batch2,_batch3}.py` append to `.beans/…`, a directory retired
  by the 2026-09-26 beans migration.

And a probe elsewhere in the tree already said so: the docstring of
`computations/qbeta/qbeta_c3_faddeev_rogers_probe.py` complains that a past
commit *"swept in `session.json` and `tmp.json`, i.e. an untargeted"* commit —
both of which are now in this directory.

## Before you move anything back

Nothing outside this directory reads any file in it. That was checked per file,
not assumed: of the 95, seven were referenced from outside, and every one of the
seven turned out to be **prose** — an audit narrating a filename, a skill
mentioning a witness, a docstring complaining about the scratch. Zero live reads.

If you need one of these back, move it back. Same rule as the docs archive: this
is for reducing noise, not gating access.
