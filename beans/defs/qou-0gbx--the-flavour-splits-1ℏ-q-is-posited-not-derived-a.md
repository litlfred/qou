---
# qou-0gbx
title: The flavour split's (1+ℏ_q³) is posited, not derived — and summing its whole tail buys 1/323 of the gap
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-05T07:50:02Z
updated_at: 2026-10-04T15:24:54Z
parent: qou-10v9
---


## The question this came from

*"Why only leading order? We should have ALL terms. Even if negligible within the
current error, mathematical accuracy is more important. Is there a closed form?"*

The corpus carries the flavour split `δ = Δm_pn/M_N` as

```
δ_leading   = (q-1)²(1-q⁻⁴)/3
δ_canonical = δ_leading · (1 + ℏ_q³)
```

and `(1 + ℏ_q³)` is the first two terms of `1/(1 - ℏ_q³)`. There is a closed form
for the resummation, and it does not help.

## 🛑 Most of this was already in the corpus — cite the predecessor, not me

`computations/probes/flavor_split_geometric_closure_probe.py` asked the same
question and got most of the answer: `(1+ℏ³)` and `1/(1−ℏ³)` differ only at
`O(ℏ⁶)`; neither reaches CODATA; `(1+ℏ³)` supplies **76.07 %** of the needed
correction; the exact demanded coefficient is `(C_true−1)/ℏ³ = 1.31459`, which is
the `c` at `k = 3` below to five figures; and its verdict was already *"NOT the
closure — a partial, posited factor, not merely unproven"*. **None of that is new
here.** What this bean adds is (i) the tail-vs-gap ratio `K = 323`, which turns
"does not close it" into a bound on what any resummation could ever be worth,
(ii) the sweep at `k = 1, 2, 4` and the required exponent `k = 2.8822`, and
(iii) the Lean statement. The open question below is the predecessor's, restated
with a formal bound attached.

## What was measured

`computations/qbeta/qbeta_flavour_split_series_probe.py` (all assertions pass,
float64-guard clean), with `x = ℏ_q³ = 9.7266e-4`:

| quantity | value |
|---|---:|
| whole tail past two terms, `(1-x)⁻¹ - (1+x) = x²/(1-x)` | `9.4707e-7` |
| gap between the two-term form and measured `Δm_pn/M_N` | `3.0598e-4` |
| **`K` = gap / tail** | **`323.07`** |

Summing every remaining term to infinity closes **one three-hundredth** of what
is missing. And resumming does not rescue it at any exponent or coefficient:

- solving `δ_leading/(1 - ℏ_q^k) = δ_CODATA` needs `k = 2.8822`, not `3`
  (4.09 % away);
- `1 + c·ℏ_q^k` needs `c = 0.012905, 0.130249, 1.314562, 13.26745` at
  `k = 1, 2, 3, 4` — none of them `1`, and none a simple rational.

**The missing 0.03 % is not in this tower at any order.**

## Formalised

`folio/quantum-observable-universe/lean/QOU/Hecke/GeometricTailBound.lean`,
5 declarations, sorry-free, registered in `QOU.lean`:

- `tail_eq` — `(1-x)⁻¹ - (1+x) = x²/(1-x)` for `x ≠ 1`;
- `tail_pos`, `tail_le` — the tail is positive and at most `2x²` on `[0, 1/2]`;
- `summing_cannot_close` — if the outstanding gap is `K > 1` tails wide, the FULL
  sum still undershoots the target;
- `gap_le_tail_of_summing_closes` — the contrapositive, which is how the
  measurement is used.

Pure ordered-field algebra with no substrate constant in it; the measurement
enters only as the hypothesis `K > 1`.

## What is actually open — the reason this bean exists

The numbers above justify the TRUNCATION. They do not justify the FACTOR.

`(1 + ℏ_q³)` is *labelled* a 3-loop substrate-Planck correction
(`docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md`,
Parts B and C) and **nothing derives it**. Reading two terms as the head of a
geometric series and summing them is the clean-formula move the anti-fit
discipline exists to catch — which is why this bean records the resummation as
refuted rather than adopting it.

**To close:** either derive `(1 + ℏ_q³)` from the substrate (a 3-loop count that
predicts the exponent 3 and the coefficient 1, not a form chosen to fit), or
demote it to a stated posit in every block that consumes it. The measured
`k = 2.8822` and `c = 1.3146` are the numbers a derivation must MISS or MATCH —
they are a target to check a future derivation against, never a criterion to
search on.

## Status 2026-09-05 — measurement half LANDED, derivation half OPEN

Landed on `claude/q407-self-assuming-projections-2026-08-21` (commit
"Coulomb and surface are one defect; the flavour-split tail is 323x too small"):
the probe, the Lean file, and the citation of the predecessor probe. Returned to
`todo` rather than left `in-progress` so a sibling is not blocked — nobody is
working the derivation.

- **Round 56 Progress (`2026-11-16T21:20:58Z`)**: Opened [`litlfred/qou#8207`](https://github.com/litlfred/qou/pull/8207) (`cfc03c4131df1ea758c17554768f2274e708f38b`, Commit 1 `0a9d3f269d6c23f614dc40aac55d5f0a7b2baafd`). Keeping bean at `status: in-progress` pending owner review.
