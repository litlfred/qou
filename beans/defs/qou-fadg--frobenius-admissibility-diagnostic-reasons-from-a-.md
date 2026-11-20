---
# qou-fadg
title: frobenius_admissibility_diagnostic reasons from a rank-6 Gram that is rank 5
status: todo
pr: 8284
type: task
priority: medium
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T00:00:00Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

Found while stamping the convolution onto the generative-isotope SDP path
(`qou-mgq3`). Not fixed here: the defect is in a reasoning chain, and
rewriting someone's analysis speculatively is worse than flagging it.

`computations/probes/frobenius_admissibility_diagnostic.py` is the recorded
explanation of the `0/3558` Frobenius-infeasible result in
`all-nuclides-sdp-admissibility.witness.json`. Its argument rests on a premise
that convention D falsified.

## The premise is false

Its docstring: *"Since G (the H_3 NF Gram) is invertible (rank 6, though
indefinite: 1 neg-norm block), `G x = nf` already fixes x = G^-1 nf uniquely"*.

Measured on the live Gram:

| | |
|---|---|
| `det(G)` in float64 | `3.9984e-17` (looks nonzero) |
| `det(G)` at 60 dps | `2.9556e-60` — tracks precision, i.e. **0** |
| singular values | `4.230, 0.7527 x4, 5.701e-17` |
| numerical rank | **5 of 6** |
| `gram.gram_inverse()` | **raises NotImplementedError** |

`gram.py` says so explicitly under convention D ("the H_3(q) trace form is
SINGULAR (rank 5 of 6); the radical is the q-antisymmetriser, exported as
RADICAL"), and `RADICAL` checks out: `||G @ RADICAL|| = 5.2e-17`.

## Two consequences for the diagnostic's conclusion

1. **`G x = nf` does not fix `x` uniquely.** With G rank 5 the system is either
   inconsistent, or has a **1-parameter solution family** — and then the net
   row can select a member, so it is not over-determined at all.
2. **The constraint count is wrong.** "7 equality constraints on 6 unknowns,
   over-determined by one" counts 6 Frobenius rows; only **5** are
   independent. 5 + 1 net = 6 on 6 unknowns — square, not over-determined.

## And its light/heavy statement is backwards

Its text: *"For light nuclei nf in range(G) (residual ~1e-15)"*. Measured in
mpmath at 60 dps via the exact null projection `|<nf, RADICAL>| / ||nf||`:

| nuclide | off-range fraction |
|---|---|
| He-4 | **0.21431** (21 %!) |
| O-16 | **0.0027264** |
| Ca-40 | 3.635e-17 |
| Fe-56 | 3.403e-17 |
| Pb-208 | 3.392e-17 |

It is the **light** nuclei that are clearly OFF range and the **heavy** ones
that sit at the floor — the reverse of what the docstring says. (The heavy
figures are at the precision floor set by RADICAL's own accuracy, ~5e-17, so
"in range" there is *consistent with* but not *proved by* this measurement.)

## A hypothesis of mine, TESTED AND REFUTED — do not repeat it

I expected the cause to be a float64 conditioning artifact: `cond(G) = 4.94e16`
in float64, so I predicted `np.linalg.solve` would return a tiny residual while
the true off-range component was O(0.1), the ill-conditioning absorbing it into
a huge `x`. **Measured, that is wrong.** The f64 residuals are `He-4 0.734`,
`O-16 5.97e-3`, `Ca-40 1.45e-16` — they track the exact null projections rather
than hiding them. `||x||` is indeed ~1e15-1e16, but the large `||x||` does not
buy a false small residual. So the diagnostic's "~1e-15" figure is not explained
by conditioning, and where it came from is **undetermined** — that is the open
question, not a settled artifact story.

## Why it matters

The `0/3558` is cited as a structural result — I cited it myself in `qou-mgq3`
("the Frobenius equality is degenerate -> 0 feasible"). If the over-determination
argument is wrong, the *reason* for 0/3558 is unestablished, even though the
count itself may well be right. A correct diagnosis has to start from rank 5.

## Not doing here, and why

Rewriting the analysis is not a mechanical fix and would widen the active PR.
The measurements above are the input a correct rewrite needs.

## Progress Update (PR #8284 — `status: in-progress`)

- [x] Formalized pure Lean 4.24.0 module(s) (`QOU/MassTheory/PhiQTowerConvexityAndGramRankFive.lean`, `QOU/MassTheory/ChainOrderingSpreadAndOneRowUrsellIdentity.lean`, `QOU/MassTheory/CoordinationChannelAritySeparation.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` probe `computations/probes/phi_q_convexity_gram_rank_chain_ursell_arity_probe.py` and 2-commit stamped witness `computations/probes/phi-q-convexity-gram-rank-chain-ursell-arity-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8284](https://github.com/litlfred/qou/pull/8284) (`ready: d9d87101718b841adc62a2d83ad74df6ff4798e4`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8284, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
