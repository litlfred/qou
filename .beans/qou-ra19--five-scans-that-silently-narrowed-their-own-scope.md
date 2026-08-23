---
# qou-ra19
title: Five scans that silently narrowed their own scope, and the rule that would have caught all five
status: todo
type: task
created_at: 2026-08-23T22:37:32Z
updated_at: 2026-08-23T22:37:32Z
---

Five separate instances in one branch's recent history, all the same shape: **a
scan whose scope silently narrowed, whose output got smaller, and whose smaller
output read as success.**

| # | site | narrowed to | found |
|---|---|---|---|
| 1 | `hecke_character_symbolic._load_chi_witness` | own dir after Phase-6 moved the module into `hecke/` | 93e24e23d — cache never hit, removed |
| 2 | `qou_substrate.witness` `check-all` | the installed package dir | 93e24e23d — reported **0** witnesses, now scans 2717 |
| 3 | `sync-qou-mass-vendor.py:217` | `[a-z0-9]` class matched a TRUNCATED fragment after a capital | 93e24e23d — a witness was never vendored |
| 4 | `content_block_label_audit.py:133` | own dir after Phase-6 moved it into `audits/` | 1ca6fe52b — **43 of 2717 = 1.6%**, `missing_label` 43 → 1 read as a drain; true backlog is **90** |
| 5 | `witness_provenance_audit` | reports only over witnesses that CARRY a `scriptFile` | 5ee66d05a — stripping provenance made the gate GREENER (2426 → 2428 as it was RESTORED) |

Add the near-miss: the drift tool's upstream resolver tried only a sibling dir
and the flat `computations/` root, so **357 of 688 drift records were false**
(qou-jvav) — same cause (Phase-6), opposite sign, and it was loud rather than
quiet only by luck.

## The rule already exists and is not enforced

`witness_shape_guard`'s own preamble states it:

> A CHECK WHOSE SUCCESS CONDITION IS SATISFIED BY THE EMPTY STATE IS NOT A
> CHECK.

Every one of the five satisfies its success condition on the empty state. None
of them said so. Four were found by accident — by regenerating something and
diffing, or by chasing an unrelated count.

## Two contributing causes, both structural

**(a) `Path(__file__).parent`-relative scope survives a file move syntactically
but not semantically.** The Phase-6 refactor (2026-06-02) moved modules into
cluster subdirectories while the artifacts they read stayed flat. Nothing
breaks at import; the scope just shrinks to a directory that happens to be
nearly empty. `qou-rug0` fixed 67 files of `__file__`-rooted PATH resolution
and repo-wide outside-repo resolutions went 81 → 0 — but SCOPE (what a glob
covers) was not part of that sweep, only RESOLUTION (whether a path exists).

**(b) An audit's denominator is chosen by the thing it audits.** #5 is the
purest form: the gate reports over rows that opt in by carrying a field, so
destroying the field removes the row. Any audit whose corpus is "things with
property P" is blind to a regression that removes P.

## What would actually catch this class

Ideas, none implemented, roughly in order of cost:

1. **A scanned-count floor per audit.** Every corpus-wide audit records how
   many artifacts it examined, and a drop of more than X% against its own
   previous witness is red. This is `witness_shape_guard` applied to audit
   COVERAGE rather than witness payload, and it would have caught #1, #2 and
   #4 on the first run after each move. Cheap: the count is already in most of
   these witnesses.
2. **A grep gate on `HERE.glob(` / `Path(__file__).parent.glob(`** in anything
   under `computations/audits/` or named `*_audit.py`, requiring a located
   root and `rglob`. Mechanical, catches the cause rather than the symptom.
3. **For (b): audits report their EXCLUDED count too.** #5 was invisible
   because the gate printed only the size of its own denominator. It now
   prints the 421 outside the audit alongside the 2296 inside, and that single
   line is what makes a shrinking denominator visible.

Ideas 1 and 3 are cheap and mostly mechanical. 2 is a lint. None requires a
domain decision.

## Immediate follow-on

The repointed `content_block_label_audit` is red at **90 missing_label** —
registered advisory in `staleness-gates.sh` with a flip-to-blocking condition
at 0. That backlog is real work nobody has seen since June and is NOT tracked
elsewhere.
