---
# qou-2364
title: 'STALE: qbeta-markov-trace-norm witness records L2 6.85e-14 but HEAD''s script gives 3.48e-09 — 50000x, and scriptHash differs'
status: todo
type: task
priority: normal
created_at: 2026-08-30T07:13:03Z
updated_at: 2026-08-30T07:13:20Z
---


## The measurement

`computations/qbeta/qbeta-markov-trace-norm-probe.witness.json` is committed
with `allPassed: true`. Re-running its producer — on **`main`'s own copy**,
from a `main` worktree — fails:

| | committed | HEAD re-run |
|---|---|---|
| `L2-constraint-at-q0` | `6.845644678724866e-14` ✓ | `3.478181380183418e-09` ✗ (tol `1e-9`) |
| `shapes-differ-per-channel` | `0.0899095006045937` | `0.13917393188609142` |
| `scriptHash` | `b416f84925e0` | `e67039d1be38` |
| `computedAt` | 2026-07-05 | 2026-08-30 |

The L2 residual is **~50,000x larger** than the committed value, against a
tolerance of `1e-9`. `shapes-differ-per-channel` moved too. And the
`scriptHash` differs, so the witness was minted against a version of the
producer that no longer exists — it has been stale for nearly two months.

## What it is not

**Not caused by any branch.** `main`'s own copy of the probe, run from a
`main` worktree, reproduces `3.478181380183418e-09` bit-for-bit.

**Not an environment precision gap**, which was the standing hypothesis. The
committed witness was made under `mpmath 1.3.0` and the re-run uses `1.4.1`,
which is a real difference — but it was tested directly and does not explain
this. Installing `scipy` (absent when the guess was made) moved the residual
`3.455e-09 -> 3.478e-09`: under 1%, and in the wrong direction. Nothing about
a five-order-of-magnitude gap is a precision effect.

So the producer's behaviour changed between `a13f0066fec` and HEAD, and the
witness was never regenerated to match.

## Why nothing caught it

Same two reasons as `qou-7fvo`:

* the failed-assertion ratchet in `precision-gates.sh` is **advisory, not
  blocking** (`qou-a31p`), so a witness can carry a failure and every blocking
  gate still reports green;
* nothing re-runs producers to compare against their committed witnesses, so a
  `scriptHash` mismatch this old goes unnoticed.

## Not fixed here

The regenerated witness is **reverted**, not committed. Committing it would
flip `L2-constraint-at-q0` PASS->FAIL and land an unrelated red in a PR about
the tautology drain. Which way this should resolve — the producer regressed
and should be fixed, or the tolerance was always too tight and the committed
`6.85e-14` was the anomaly — is a question for whoever owns the Q_β norm work,
and it needs the `a13f0066fec` -> HEAD diff of the producer read.
