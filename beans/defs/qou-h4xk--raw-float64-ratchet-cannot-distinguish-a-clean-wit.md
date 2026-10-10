---
# qou-h4xk
title: raw-float64 ratchet cannot distinguish a clean witness from an empty one
status: completed
type: task
priority: normal
created_at: 2026-08-15T10:32:31Z
updated_at: 2026-08-19T21:04:09Z
---


> **Note.** This bean was originally filed as `qou-0vn0` on the branch behind
> PR #5070. That PR was closed as superseded and the branch reset, taking the
> bean file with it. Re-filed here under a new ID; `qou-0vn0` does not exist
> and references to it (in #5089's body and on #5078) point at nothing.

## The defect

`computations/witness_raw_float64_audit.py` scores a witness by **counting raw
float64 leaves**. It has no notion of how much content a witness is *supposed*
to have. So:

    an EMPTY or TRUNCATED witness scores exactly the same as a fully DRAINED one — zero.

"Fewer raw floats" is treated as unambiguous progress, and destroying the file
is the most effective way to achieve it.

## Observed twice, on the same file, in one session (2026-08-15)

`rho_k_co_casimir_extended.py` writes its witness **after each atom**, so the
file on disk is incomplete for most of a multi-hour run. Measuring it mid-run:

| | committed | mid-run |
|---|---|---|
| raw float64 | 4 | **0** |
| `durationMs` | 2,552,837 | **519** |
| diff | — | 2,272 deletions |

The ratchet reported `REGRESSED: 0` — a **green** reading on a gutted file.
Committing it would have been a false green *and* would have destroyed the
witness. Caught both times only by manually checking `durationMs`, which the
ratchet does not look at.

## Same defect class as `qou-lb0f`

`qou-lb0f` records the lake-cache `restore` no-oping on a cache gutted from
7268 oleans to 459, because its presence check asks "are there *any* oleans"
rather than "are there the *expected* oleans". Identical shape:

> **a check whose success condition is satisfied by the empty state is not a check.**

Worth fixing as a pair, and worth stating as a general rule for this repo's
gates, alongside the existing "a gate that cannot be shown to FAIL on a
violation is indistinguishable from a no-op" (already in the audit's own
`self_test` docstring).

## Fix sketch

A count alone cannot detect this — the guard needs a **reference** to compare
against. The cheap reference already in the repo is the committed copy:

1. For each `*.witness.json` modified relative to `HEAD`, compare leaf-scalar
   count, assertion count, and data-key count against `git show HEAD:<path>`.
2. Flag any witness whose content **collapsed** (large drop), regardless of
   what happened to its float count.
3. Ship a self-test that reproduces the rho-k gutting above and asserts the
   guard FAILS on it — otherwise the guard has the same unfalsifiable
   character as the hole it closes.

This is a **pre-commit** guard, which is the right place: the damage is done
when a gutted witness is committed, and CI here is dispatch-only
(2026-06-30 Actions-billing directive), so CI cannot be the backstop.

## CLOSED — the guard is a BLOCKING gate on main (verified 2026-08-19)

`computations/witness_shape_guard.py` is registered in
`scripts/precision-gates.sh` as blocking, and its self-test passes on current
main. The gate list carries the reasoning inline: the ratchet counts raw
floats, so a gutted witness scores zero and reads as a perfect drain; this one
asks the orthogonal question by diffing shape against HEAD. Neither subsumes
the other.

Worth recording: the guard fired for real during its own arc, on a mid-write
`rho-k-co-casimir-extended` — the ratchet reported 0 raw floats ("clean") on
the same file the guard reported COLLAPSED (1,863 -> 899 leaves, durationMs
2,552,837 -> 12,262). That is the exact false-green the bean was filed for.
