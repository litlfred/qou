# Three independent measurements, one hook split

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` · **Scope:** (a) scope-limited — n=9 complete census, n=12 for one leg. Nothing wired, no witness, no fit.

## The claim

Across this arc, **three measurements sharing no method** have each isolated the same structural
split: the hook family `(n−b, 1^b)` behaves *oppositely* to every other shape, and it is the family
that already carries a derived closed form. Individually each looked like a local curiosity;
together they are one fact about the corpus's `b`-decay, and they make "treat hooks separately"
something arrived at rather than assumed.

| # | measurement | what hooks do | PR |
|---|---|---|---|
| 1 | per-dimension majorant `tr_λ(X*X)/dim_λ`, rank within level | **level-max → level-min**, crossing at `b=4` | #6748 |
| 2 | pointwise monotonicity violations | **6 of 6** have a hook on the low side; 0 on the high side | #6729 |
| 3 | cancellation factor `κ = \|Σ eig\| / Σ\|eig\|` | **level-min → level-max** | #6779 |

They are independent in the strong sense: (1) is a norm, (2) is an ordering over pairs, (3) needs
eigenvalues — and (3) points the *opposite* way to (1), which is what one should expect if a single
mechanism drives both, since `|tr| = κ · Σ|eig|`.

## The mechanism, from the numbers rather than inferred

The hook column at n=9, measured end to end (#6779):

```
b:            1        2        3        4        5        6        7
κ         0.9362   0.5365   0.1042   0.0981   0.0661   0.2507   0.6852
|tr|/dim  33.648   13.258    1.320    0.536    0.142    0.176    0.115
Σ|eig|/dim 35.94   24.710   12.665    5.460    2.153    0.701    0.169
```

Across `b=1…7` the hook's `Σ|eig|/dim` collapses **213.3×** and its `|tr|/dim` falls **291.4×**.
Both fall faster than any other family, which is measurement (1). κ is their *ratio*, so it dips to
a minimum at `b=5` and then rebounds once the magnitude falls faster than the trace — which is
measurement (3), and the U-shape corrects an earlier claim of mine that hook κ simply rises.

So one fact — **the hook column decays faster than everything else** — produces a level-max→min
crossing in the majorant, all six pointwise violations, and a level-min→max crossing in κ. The
apparent tension between (1) and (3) is arithmetic, not a conflict.

## Why the split is actionable rather than descriptive

The hook column is exactly the family with a **derived closed form** — the reduced Burau expression
for `tr_hook(X*X)` (#6556), verified against the direct seminormal trace on all 9 hooks at 1.38e-64
(#6729). So a bound can:

- handle hooks **exactly**, through the closed form; and
- make a **uniform** statement about everything else, where pointwise monotonicity holds (#6729,
  0 violations off-hooks) and κ is better behaved.

That is materially different from the alternative the arc had been pursuing — one statistic valid
across all shapes — which #6669 showed no candidate achieves (17 tested) and #6677 showed would
have to reproduce a hook/two-row relation that *changes sign* at an interior `b` not tracking `n`.

## What is NOT established

- **n=9 for legs (2) and (3)**; leg (1) additionally at n=12. Nothing is proved for general `n`.
- **The κ level comparisons use partial levels.** At `b=6`, three of seven shapes are measured
  (`(3,3,3)` 0.073, `(3,2,2,2)` 0.154, the hook 0.251); the remaining four are in a census run still
  in flight, and any one could exceed the `b=7` value 0.685 and change the envelope picture.
- **Nothing here bounds anything.** These are measurements of a decomposition, not a derivation.
- **"Handle hooks separately" is a strategy, not a theorem.** The split is a strong empirical
  regularity at one size; it is not shown that the off-hook family admits a uniform bound, only that
  the obstruction to one is confined to hooks in every measurement so far.

## Method notes this arc paid for

- **A dim-capped sample is not a random subset of a level**, and it misled three separate times: it
  can only understate a level maximum (#6729), it omitted whole levels from the κ preliminary
  (#6764), and at `b=6` it retained exactly one shape — the hook, the least representative one.
- **Measure one family when one family answers the question.** A complete κ census is ~1h45m
  (`mp.eig` is ~dim³); the hook column, with all dims ≤ 70, is under two minutes.
- **`mp.mp.dps` is global mutable state.** Every probe here sets it at module scope, so dps must be
  set *after* all imports; the `_assert_dps` guard (#6710) caught a live instance and refused to
  compute rather than return numbers at an unrequested precision.
