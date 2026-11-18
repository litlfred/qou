---
# qou-xc8t
title: 'Discharge JetOrderIndependence honestly: feed ofPivots per-order pivots from jet_order_pivots.py at higher truncation, or prove the column-extension linkage for jacobianRank_eq_three_of_base'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-09T22:04:32Z
updated_at: 2026-11-18T11:23:08Z
parent: 08a2
---


## 2026-09-14 — measured both routes. Route 1 is a no-op, and the Lean's "witnessed" constants are STALE against their own producer

Five weeks with no entry, so both halves of this bean's title were measured
rather than reasoned about. Two findings, and the second is the one to act on.

### 1. "Feed `ofPivots` per-order pivots at higher truncation" does not produce anything new

`jacobianRank N` is the rank of the order-`N` coefficient Jacobian — `3 × (N+1)`,
rows the three series, columns `h^0 … h^N`. Raising the truncation **adds
columns**; it cannot change the ones already there, because Taylor coefficients
do not depend on where the expansion is cut. Measured by calling
`jet_order_pivots.jet_coeffs` at order 2 and order 5 (`jet_coeffs` already takes
`order`, so this needed no code change, and `main()` was never called, so no
witness was written):

```
       4_1  order-2 ['1/4', '0', '11/4']     first 3 @ order-5 ['1/4', '0', '11/4']   IDENTICAL
       5_2  order-2 ['1/2', '1', '1/4']      first 3 @ order-5 ['1/2', '1', '1/4']    IDENTICAL
 Borromean  order-2 ['1', '0', '0']          first 3 @ order-5 ['1', '0', '0']        IDENTICAL

order-2 3x3 det = -11/4      LU pivots ['1/4', '1', '-11']
order-5 first-3-col minor    det = -11/4,  LU pivots ['1/4', '1', '-11']
PIVOTS IDENTICAL ACROSS TRUNCATION ORDER: True
rank of the full order-5 Jacobian (3 x 6) = 3
```

So feeding `ofPivots` from higher truncation hands it **the same triple at every
order** — i.e. a constant extension, which is precisely the defect `qou-1n7g`
records and PR #4884 removed. Route 1 as written re-commits it with extra steps.

**Stated precisely, because the literal statement is weaker than "impossible".**
`rank ≥ 3` follows from *any* non-singular `3×3` minor, so one could in principle
choose a **different** minor at each order (columns `h^1,h^2,h^3` at `N=3`, and so
on) and get genuinely per-order pivots. That is strictly more work than the
constant and buys nothing the column-extension argument does not give for free.
What is measured here is that the **natural** minor — the first three columns, the
one the corpus already uses — is truncation-invariant.

**Consequence: route 2 (the column-extension linkage) is the route**, and it is
more tractable than this bean's title suggests. The mathematical content is that
the first three columns of the order-`N` Jacobian *are* the base minor — true by
Taylor stability, as measured above — plus `Matrix.rank_submatrix_le` and
`Matrix.rank_le_height`, both already named in `JetOrderIndependence.lean`'s own
docstring. **The blocker is that the Lean has no definition of the order-`N`
Jacobian at all**; `jacobianRank` is an abstract class field, and the file says so
at L328-331. That is a definition to write, not a theorem to discover.

### 2. 🛑 The committed pivots do not reproduce — `det` is `−11/4` today, not `1/16`

Found while doing the above. The Lean's `jetJacobianBase` / `jetPivots` and the
committed witness agree with each other and **both disagree with the live
producer**:

| | committed (Lean + witness) | live producer, today |
|---|---|---|
| `4_1` | `(1/4, −1, 55/16)` | **`(1/4, 0, 11/4)`** |
| `5_2` | `(1/2, 0, −1/16)` | **`(1/2, 1, 1/4)`** |
| `Borromean` | `(1, 0, 0)` | `(1, 0, 0)` — unchanged |
| elimination det | `1/16` | **`−11/4`** |
| LU pivots | `(1/4, 2, 1/8)` | **`(1/4, 1, −11)`** |

Both sets are internally consistent (each det equals its own pivot product), so
this is a genuine data change, not an arithmetic slip on either side.

**It is ordinary producer drift, not import-cone drift.** `jet_order_pivots.py`'s
own `scriptHash` is `1eadd3f17d76` against the witness's `380671554d5b` — the
source changed. The witness is from **2026-06-08**, three months old.

**The braid words are NOT the cause.** `braid_word_for_knot` today returns
`(σ₁σ₂⁻¹)²`, `σ₁⁻¹σ₂σ₁⁻¹σ₂²`, `(σ₁σ₂⁻¹)³` — exactly the words the Lean docstring
names. And the `h^0` column is unchanged for all three knots; only `h^1` and `h^2`
moved, and only for `4_1` and `5_2`. That is the signature of a change in the
trace's normalisation or expansion, not in which knots are being traced.

**What did change is not established.** The witness's `scriptCommitSha`
`9ce80195f72c` is not in this shallow clone (6079 boundary commits), so the
producer cannot be diffed against the version that wrote the witness — the exact
limitation AGENTS.md records as *"diff the producer first is unrunnable for half
the queue"*. **I am not asserting which of the two number sets is correct.**

### What this does NOT break, and it matters

**The conjecture and every Lean theorem survive.** `−11/4 ≠ 0` just as `1/16 ≠ 0`,
so jet-order independence at the base order holds under either set; the full
order-5 Jacobian measures rank exactly 3. `jetOrder3_certificate`,
`jetJacobianBase_det`, `jetJacobianBase_rank` and `eliminationDet_ne_zero` are all
still true statements — `jetJacobianBase_det` and `jetJacobianBase_rank` about the
matrix as literally written in the file, which is now a matrix the producer no
longer emits.

So the exposure is **provenance, not correctness**: the Lean docstring says these
rows are *"witnessed from the framework's own canonical Markov traces
(`jet_order_pivots.py`)"* and that sentence is no longer true of today's producer.

### Options

**A. Re-run the producer and re-wire the Lean to the fresh numbers.**
- *Means*: `jetJacobianBase := !![1/4, 0, 11/4; 1/2, 1, 1/4; 1, 0, 0]`, det
  `−11/4`, `jetPivots := (1/4, 1, −11)`; `jetJacobianBase_det` and the docstrings
  follow. Every theorem re-proves (the proofs are `simp`/`norm_num` on the
  literals).
- *Costs*: one witness re-run, one Lean file, `lean`-direct re-verification.
- *Risks*: adopts today's producer as correct **without knowing what changed** —
  and the 2026-06 numbers may be the right ones. Moves a number in a content
  block's cone.
- *Commits to*: the live producer being canonical.

**B. Establish what changed first, then A.**
- *Means*: unshallow enough history to diff the producer, or reconstruct which
  commit moved `markov_trace_of_word`'s normalisation.
- *Costs*: a deep fetch, or a bisect over an expensive symbolic producer.
- *Risks*: none beyond time.
- *Commits to*: nothing.

**C. Record the divergence in the Lean docstring and leave the numbers.**
- *Means*: the file stops claiming its literals are what the producer emits.
- *Costs*: a docstring.
- *Risks*: leaves two live answers with neither adjudicated.

**D. Do nothing.** The Lean keeps asserting a provenance that does not hold, and
the next agent re-derives this.

### Default and recommendation

**Default is D** — nothing moves, and the stale provenance stays.

**My judgement, not a finding: B then A.** Re-wiring to numbers whose derivation
changed for unknown reasons is the same move the anti-laundering discipline warns
about, one level down — and the corpus has three months of work citing `1/16`.
Establishing *what* changed is cheap relative to a wrong adoption. **I have not
done either**: both are changes to another arc's published artifact, which the
2026-09-07 ASK-THE-OWNER directive does not exempt.

**This bean stays open** (rule 13a — its subject is the open conjecture).
Measurement only; no repo file touched but this bean and `qou-1n7g`.

- Round 83 (`lane-e667`): Formalized `qou-xc8t`, `cdup`, `qdzu`, `qou-9e7p`, `qou-c98z` in `QOU.Foundations.TruncatedJetMinorStabilityCellAxialContentBridgePrecisionFloorSignSeparationOrderedImportInheritanceConjectureAuditLedger` with 80-dps `mpmath` 2-commit witness stamp (`aa00fee380c7d4aad9c2a05a9bab09078a582bd9` -> `36e5ef216683fe9a0a37836e3fbfd0bf5fd7ed3a`, `scriptHash=0bcb4f55d2e1bf88729ec0af6984c5f97ce5fe17beee4851f2d6cc29ea159aa8`) in PR `litlfred/qou#8446` (`status: in-progress`).
