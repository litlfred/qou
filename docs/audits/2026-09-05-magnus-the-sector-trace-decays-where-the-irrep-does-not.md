# The sector trace decays where the irrep column does not — and the irrep failure diverges

**Date:** 2026-09-05 · **Bean:** `qou-o6ov` (rescoped) · **Scope:** (a) scope-limited — A = 2…5 at
one q₀, complete ≤2-row column. Nothing wired, no witness, no fit. **One negative sharpened into a
divergence, and the arc's first constructive direction.**

## Part 1 — the irrep failure is a divergence, not a near miss

The ≤2-row column's monotonicity breaks are not scattered across `k`. Read across sizes, the **same
step `k=3→4`** fails at A=3, 4 and 5; A=2's column is simply too short to contain it. That is a
**fixed-`k`** feature, invisible to a per-A verdict, so it is worth measuring as one thing.

y-weighted monotonicity at a step is exactly `|tr_{k+1}|/|tr_k| < y_k/y_{k+1} =
[n−2k+1]_q/[n−2k−1]_q` (`|c_λ| = y_λ·|tr_λ|` carries no `dim`, so the raw trace ratio is the right
quantity — using `|tr|/dim` here cost a correction in #6822). At `k=3→4`:

| A | n | `\|tr₄\|/\|tr₃\|` | ceiling | margin | verdict |
|---|---|---|---|---|---|
| 3 | 9 | 1.23869 | 2.04371 | 1.6499 | falls ✓ |
| 4 | 12 | 5.36793 | 1.46067 | 0.27211 | **rises ✗** |
| 5 | 15 | **26.4306** | 1.32961 | **0.050306** | **rises ✗** |

**Trace-ratio growth per A step: ×4.334, then ×4.924** — near-constant, ~×4.6.

The two sides move apart from both ends. The ceiling is capped at `[3]_q ≈ 3.0437` at *any* `k`, and
at **fixed** `k` it is forced downward toward `q² = 1.23205` as `n` grows — protection that cannot be
raised and additionally erodes. Against that, a trace ratio growing ~4.6× per step. The margin
collapses **1.65 → 0.272 → 0.0503**.

So the y-weighting route does not fail by a margin a sharper analysis might recover. It fails at a
rate.

## Part 2 — but the irrep traces are DIFFERENCES, and the sector decays

The corpus already named the obstruction; the bean records:

> *"a decay BOUND for two-rows must respect the difference structure — a per-sector triangle
> inequality does not decay in k."*

By `U_q(sl₂)` Schur–Weyl, `W_k = ⊕_{j≤k} S^{(n−j,j)}`, so

```
tr_{W_k} = Σ_{j≤k} tr_{(n−j,j)}        and        tr_{(n−k,k)} = tr_{W_k} − tr_{W_{k−1}}
```

A difference of two decaying sequences need not decay. So the question was asked from the other
side: **does the sector trace itself decay, per sector dimension `C(n,k)`?**

| A | irrep column, ρ_true | **sector `\|tr_{W_k}\|/C(n,k)`, ρ_true** | sector, ρ_bare |
|---|---|---|---|
| 2 | 1 rise ✗ | **1 rise ✗** (k=2, ×1.231) | decays ✓ |
| 3 | 1 rise ✗ | **decays ✓** | decays ✓ |
| 4 | **2 rises ✗** | **decays ✓** | decays ✓ |

**At A=3 and A=4 the sector decays where the irrep column does not** — and A=4 is the decisive case,
since that is where the irrep column fails twice and where the y-weighted mass fails too. The A=4
sector column, ρ_true:

```
k:              1         2         3         4         5         6
|tr_W|/C:   2.5826    0.3197    0.1176    0.1040   0.06225   0.04539
```

Signs are load-bearing here and nowhere else in this arc: the partial sum needs the **signed**
`tr_{(n−j,j)}`, which alternate for the true element (A=4: `− + − − + +`) while the bare element's are
essentially one sign. The reframing cannot be tested from `|tr|` data.

## What this changes

**The arc's non-monotonicity looks like a difference artifact, not a failure of decay.** The natural
object carrying the decay is the **sector** trace; the irrep trace is its first difference, and
first differences of decaying sequences are not required to decay. That is a constructive direction —
the first in this arc after a run of negatives — and it is not a new mechanism I invented: it is the
one the corpus had already flagged, tested from the other end.

## What is NOT established, and one caution I registered before running

- **A=2 fails**, so the honest statement is *"decays for A ≥ 3"*. **A property that only starts
  holding at the third size is the shape of a small-size artifact**, and I wrote that into the
  probe's docstring *before* running it rather than after seeing the result. Two things weigh
  against dismissing it that way: A=2 is the smallest size, its column has only three entries, and
  its single rise is mild (×1.231) against A=4's irrep rises of ×3.0 and ×7.6. But that is an
  argument, not evidence.
- **A=5 is running** and is not in this document. It is the size that would make the sector claim
  3-of-4 rather than 2-of-3.
- **Nothing is bounded.** A monotone sequence is not a bound, and no tail estimate is attempted.
- **Why the sector decays is unexplained.** I have no argument for it — only the measurement.
- **The divergence in Part 1 is three sizes.** A rate read off three points is a rate to test, not a
  limit; this session has already been caught treating two agreeing sizes as a mechanism.
- **Part 1 and Part 2 are consistent, not redundant.** Part 1 says the *irrep* route diverges; Part 2
  says the irrep was the wrong object. If Part 2 holds up, Part 1 stops being the interesting fact
  about the column and becomes a statement about differencing.
