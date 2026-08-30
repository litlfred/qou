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

## RESOLVED 2026-08-30 — neither of the two options this bean offered

The bean asked whether the producer regressed or the tolerance was always too
tight. It is **neither**. The witness went stale because its three upstream
inputs were regenerated and it was never re-run.

**Proven by exact reproduction, not inference.** Restore all three inputs to
the commit the witness names in `commitSha` (`ce39b659e64`) and the *current*
producer reproduces the committed number bit-for-bit:

```
L2 with all three inputs at generating state : 6.845644678724866e-14
committed witness                            : 6.845644678724866e-14
```

The three inputs, all read by `main()`:

| input | line | changed since generation |
|---|---|---|
| `y-lambda-cyclotomic-factor.witness.json` | 153 | yes — 54 ins / 58 del |
| `q-pinning-50-digit.witness.json` | 211 | yes — 76 ins |
| `qbeta-decay-sdp-knot-operator.witness.json` | 235 | yes — all 6 coefficients |

`y-lambda-cyclotomic-factor` is the dominant term: restoring it alone (with the
other two current) moves the residual from `0.0245` to `1.9e-12`.

The upstream coefficients moved substantially — `γ` from `0.09698419128158346`
to `0.07445029684383929`, **23 %** — across four commits including
`ce43a990db2 migrate(q0) batch 3` and `41019097908 q0: label 229 witnesses`.
This is a q₀ migration propagating, not drift.

## What was ruled out, each by test rather than argument

* **Producer code.** The complete diff from the generating commit to HEAD is
  one drain of `shapes-differ-per-channel` (`qou-26f2`), which touches nothing
  on the L2 path.
* **mpmath.** The committed witness records `1.3.0`; this container has
  `1.4.1`. Installing `1.3.0` into an isolated target dir and shadowing via
  `PYTHONPATH` gives `3.478181380183418e-09` — **bit-identical** to the 1.4.1
  run. Not the cause.
* **scipy.** Absent when the earlier guess was made; installing it moved the
  residual `3.455e-09 -> 3.478e-09`, under 1 % and in the wrong direction.

### Correcting this bean's own earlier reasoning

The bean claimed "not an environment precision gap" on the strength of the
scipy test plus a `main`-worktree reproduction. That worktree ran in **this**
container, so it isolated the *code* and never the environment — the
conclusion happened to be right, but the evidence given for it did not support
it. The mpmath test above is what actually establishes it.

## The real open question, now sharp

With migrated inputs the residual is `3.478e-09` against a `1e-9` tolerance —
**3.5x over**. So: after the q₀ migration, is the L2 constraint still expected
to hold at `1e-9`, or does the tolerance belong at the migrated scale? That is
a question about the Q_β norm work, not about this witness, and it wants the
person who set `1e-9` in the first place.

Regenerating the witness is correct either way — it currently reports a number
no state of this repository produces — but it will land `L2-constraint-at-q0`
as a **recorded failure** until that tolerance question is answered. That is
why it is still not regenerated here.

## One provenance note worth keeping

`commitSha: ce39b659e64` is on **no branch**. It survives only as a dangling
commit still fetchable from the remote (`git fetch origin <sha>` works;
`git branch -r --contains` returns nothing). This whole diagnosis depended on
that object still existing. A witness whose provenance pointer is unreachable
cannot be audited at all — worth knowing before anyone prunes.
