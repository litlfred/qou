This block generalizes the 2-strand foundation ([`rem:braid-link-types`](#rem:braid-link-types)) and the 3-strand typed-$\mathbf{B}_3$ infrastructure ([`rem:typed-b3-sub-braid-extraction`](#rem:typed-b3-sub-braid-extraction)) to an arbitrary number of strands $n \in \mathbb{N}$ for the braid group, Markov closure, and Hecke quotient.

## Defined objects

See [Table 1](#tbl:braid-group-n-strand-table1-data).

## Specializations

See [Table 2](#tbl:braid-group-n-strand-table2-data).

## Significance

The categorical derivation chain through $N=4$ ([`prop:q-beta-categorical-precision-ladder`](#prop:q-beta-categorical-precision-ladder)) rests on the 3-strand typed-$\mathbf{B}_3$ infrastructure. To validate the two convergence mechanisms documented in [`prop:categorical-chain-convergence-mechanisms`](#prop:categorical-chain-convergence-mechanisms)—the per-knot $c(K)$ brane-tower bound and inter-knot linking-number locality—we require at least $n=6$ strands. This allows us to test the Markov axiom M3, $\tau_M(K_1 \sqcup K_2) = \tau_M(K_1) \cdot \tau_M(K_2) \cdot z^k$, on a concrete 2-baryon disjoint braid.

The scaffolding is per-$n$ extensible. Each new $n$ introduces an `instance HeckeQuotient n q_0` and `instance MarkovTraceN n q_0`, ensuring downstream theorems automatically specialize.

## Implemented specializations

See [Table 3](#tbl:braid-group-n-strand-table3-data).

The parameterized `BraidCrossing n` coexists with the unparameterized `TypedCrossing` from [`rem:typed-b3-sub-braid-extraction`](#rem:typed-b3-sub-braid-extraction). The latter carries the `averaged` Hecke-specific crossing type. Therefore, the conversion `BraidWord 3 → TypedBraidWord3` lands in the `sigma`/`sigma_inv` subset, as the `averaged` channel has no counterpart in the generic $n$-strand types.

## Open tasks

- Discharge `MarkovTraceN n q` for each $n$ from a fixed Markov-trace operator on the inductive limit $\bigcup_n \mathbf{B}_n$.
- Discharge higher-$n$ `closureN` cases (e.g., Borromean link at $n=3$, di-baryon at $n=6$). Currently, $n \geq 3$ returns `Link.unknot` as an ansatz.
