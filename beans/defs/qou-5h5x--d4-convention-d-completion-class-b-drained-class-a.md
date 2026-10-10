---
# qou-5h5x
title: 'D4: convention-D completion — class B drained, class A (gram.py) documented blocked'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-14T16:21:57Z
updated_at: 2026-10-10T07:47:05Z
parent: qou-cdx1
---

## The question this settles

A prior session stalled asking what "convention D is complete" means, given
that it **cannot literally complete** while `gram.py` is frozen on convention C
(`qou-w8zz`, D1). Owner directive 2026-08-14: **prepmerge PR #4928 as quickly
as possible, bean the rest.** So completion for the PR is:

> **class B drained** (everything reachable by re-running a producer),
> **class A documented and beaned** (the singular-Gram family, which needs a
> design decision, not a sweep).

The PR does **not** wait on class A.

## The measurement that justifies merging

The PR body's stop-line was *"merging now lands `main` half-migrated — some
witnesses D, some C — which is worse than either convention held
consistently."* That premise was **measured and is false**: `main` is *already*
half-migrated on its own, and the branch strictly reduces the split.

Scanned every `computations/**/*.json` (excluding `_deprecated/`) at both refs
with the same detector — fingerprints + `scan_doc` + `scan_doc_symbolic`:

| ref | convention-C witnesses | files scanned |
|---|---|---|
| `origin/main` | **72** | 4173 |
| PR #4928 (post-merge, pre-cascade) | **39** | 4198 |

37 fixed, 4 apparently regressed — and all four (`markov-stab-trace-axis-probe`,
`option-b-h3-h4-bratteli-probe`, `qbeta-c3-per-block-categorical-probe`,
`y-lambda-mpfr-proton`) were cleared by the pass-3 cascade in the same session.

So the honest framing is: **the branch does not create a split, it halves an
existing one.** Holding it makes `main` worse, not better.

## Class A — what is deliberately NOT done, and why

The `ℓ(λ) ≥ 3` blocks are the radical under convention D, so **any object built
over the full block set inherits a null direction**. Three instances, one shape:

1. **`pyhecke/gram.py`** — `G_INV = np.linalg.inv(G)` runs at import; under D
   `det G = 0`. numpy raises nothing and returns garbage
   (`||G G_INV − I|| = 1.64`). Frozen on C **on purpose**, with a 90-line
   banner. `qou-w8zz`.
2. **`tools/hecke-engine/src/gram.rs`** — already D, survives only via the
   pre-2026-05-19 `TR_M[5] = z^3` bug. Coupled to (1). `qou-m7py`.
3. **`aK_via_lp_dual_full`** — LP collapses to the trivial point, `y0* = -0.0`
   on all six atoms. `qou-fu8c`.

In each the live content is the two-row block and the right object is on the
quotient. That is a design decision for the owner, not a mechanical sweep —
which is exactly why it is class A and not part of this PR.

## Residual honesty — the count is a LOWER BOUND

Only **10 of 64** changed witnesses declare a `markov_convention` field. The
detector keys on `y_λ` tables; a convention-dependent quantity that is not a
`y_λ` table (`tr_M`, `z`, and everything derived) is invisible to it, because a
bare trace value looks identical under either convention. Nothing syntactic
fixes that — only producer provenance can. `qou-ng7j`.

So "39" and "72" are both lower bounds of unknown slack. The *comparison*
between them is still sound (same detector, same corpus), which is what the
merge decision rests on.

## Definition of done for this bean

- [ ] `markov_convention` provenance on every witness a producer writes
      (turns the lower bound into a total) — `qou-ng7j`
- [ ] class A resolved: `qou-w8zz` + `qou-m7py` + `qou-fu8c` share one quotient
      construction
- [ ] the 6 remaining orphans (`chi-*-matrix-m`) — need the `hecke-engine` CLI,
      not a Python producer


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

Premise has MOVED but the bean is not closed. Its 'class A (gram.py)
documented blocked' no longer holds -- `pyhecke.gram` is convention D and the
registry's `intra_module_split_waivers` is EMPTY with a note saying the split
is closed. What survives is its definition of 'complete', which is now
answerable. Live, and cheap: re-read it against the registry.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.
