**$n$-strand braid group + Markov closure + Hecke quotient scaffolding.**

Generalises the 2-strand foundation in
[`rem:braid-link-types`](#rem:braid-link-types) and the 3-strand
typed-$\mathbf{B}_3$ infrastructure in
[`rem:typed-b3-sub-braid-extraction`](#rem:typed-b3-sub-braid-extraction)
to an arbitrary number of strands $n \in \mathbb{N}$.

## What's defined

See [Table 1](#tbl:braid-group-n-strand-table1-data).

## Specialisations

See [Table 2](#tbl:braid-group-n-strand-table2-data).

## Why this matters

The categorical-derivation chain through $N=4$ in
[`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)
sits on the 3-strand typed-$\mathbf{B}_3$ infrastructure. Validating
the **two convergence mechanisms** documented in
[`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms)
— per-knot $c(K)$ brane-tower bound + inter-knot linking-number
locality — requires at minimum $n = 6$ infrastructure (to test
$\tau_M(K_1 \sqcup K_2) = \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k$
on a concrete 2-baryon disjoint braid via Markov axiom M3).

The Lean class system makes the scaffolding **per-$n$ extensible**:
each new $n$ adds an `instance HeckeQuotient n q_0` and
`instance MarkovTraceN n q_0`, and downstream theorems
auto-specialise.

## Specialisations landed

See [Table 3](#tbl:braid-group-n-strand-table3-data).

Note: the parameterised `BraidCrossing n` in this block coexists with
the unparameterised `TypedCrossing` from
[`rem:typed-b3-sub-braid-extraction`](#rem:typed-b3-sub-braid-extraction);
the latter additionally carries the `averaged` Hecke-specific crossing
type, so the conversion `BraidWord 3 → TypedBraidWord3` is into the
`sigma`/`sigma_inv` subset (the `averaged` channel has no counterpart
in the generic n-strand types).

## Open R&D

- Per-$n$ discharge of `MarkovTraceN n q` from a fixed Markov-trace
  operator on the inductive limit $\bigcup_n \mathbf{B}_n$.
- Higher-$n$ `closureN` discharges: Borromean link at $n=3$,
  di-baryon at $n=6$, etc. (current $n \geq 3$ returns `Link.unknot`
  as a ansatz).
