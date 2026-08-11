---
# qou-janf
title: y_lambda_at raises global mp.dps 40->50, and the old qbeta witnesses were cache-served not live
status: todo
type: task
priority: normal
created_at: 2026-08-11T11:09:11Z
updated_at: 2026-08-11T11:10:50Z
---

Two coupled facts, both measured, found while draining the `qbeta/qbessel_*`
`Q0` cluster in PR #4975.

## 1. `y_lambda_at` raises global `mp.dps` as a side effect

```
dps before y_lambda_at: 40
dps after  y_lambda_at: 50
```

Measured directly (`wedderburn_jones_markov.y_lambda_at(6, Q_MP)` with
`mp.dps = 40` set beforehand). It is the **call** that moves it, on the live
path — not any import.

This matters because callers set their own working precision and reasonably
assume it holds. `qbessel_reeb_order_justification.py` sets `mp.dps = 40` at
line 63 and reports `"compute_dps": mp.dps` at write time (line 232), so its
witness records **50** while the file declares 40. The value is not wrong — the
later arithmetic really does run at 50 — but the file's declared precision is
not the precision it computes at, and nothing says so.

## 2. The pre-existing witnesses in that cluster were CACHE-served, not live

This is the larger fact, and it is why the dps moved at all.

`y_lambda_at`'s fast path serves `y-lambda-at-q0.witness.json`, which is built
at the **muon** pin. The gate **used to** compare the caller's `q` against
`q_parameter.Q` — the **proton** pin, 11.54 ppb away — so a proton-anchored
caller satisfied it *trivially* and was handed ideal-layer data with no signal
that a layer boundary had been crossed. That is the straddle AGENTS.md warns
about in bold under §q₀ anchor convention.

**The guard has since been fixed**: the gate now compares against
`_Y_LAMBDA_AT_Q0_WITNESS_Q0`, the witness's own recorded q₀. A proton-anchored
caller now falls through to live computation. Verified in
`wedderburn_jones_markov.py` around lines 208-227, comment included.

Consequence for the cluster: the committed witness that read `compute_dps: 40`
was produced via the **cache fast path** (which never touches dps). The re-run
in #4975 is the **first one actually computed live at the proton pin** — hence
50. So the drain's real effect on those witnesses is larger than a constant
swap: it is cache-served ideal-layer → live experimental-layer.

## Why this is recorded rather than fixed here

Nothing here is broken. The guard holds, the values are live and correct, and
50 dps is better than 40. What is missing is that **none of it is stated
anywhere** — a reader of `qbessel_reeb_order_justification.py` sees `mp.dps =
40` and has no way to learn the file finishes at 50, or that its previous
witness came from a different layer.

Worth doing, in rough priority:

1. Have `y_lambda_at` **restore** the caller's dps on exit, or document the
   side effect in its docstring. Silently mutating global precision from a
   value-returning function is the surprising part.
2. Audit which other witnesses were produced on the cache fast path before the
   gate fix. Any of them may carry ideal-layer numbers under an
   experimental-layer heading. The cheap tell is a `compute_dps` that differs
   from the producer's declared `mp.dps`.

## Correction history — read this before trusting either earlier statement

- Commit `40b89a61d` disclosed the 40→50 shift, attributing it to
  `set_compute_dps()` being pulled in by importing `q_parameter`. **The
  observation was right, the attribution was wrong.**
- PR #4975's body then said the effect **"does not occur"**, on the strength of
  measuring `mp.dps` across an *import* of `q_parameter`. **That correction is
  itself wrong** — it tested the wrong operation. The import is innocent; the
  call is not.
- This bean is the third pass and the measured one.
