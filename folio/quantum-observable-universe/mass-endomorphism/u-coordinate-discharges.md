**Macdonald coordinate $u = q^2$ substantive discharges for $H_3 / V_{(2,1)}$ scalar invariants.**

Many scalar invariants in the Hecke and Wenzl-bridge algebras are rational in the Macdonald coordinate $u = q^2$, even when their defining formulas involve square roots in $q$. We use this Macdonald substitution to eliminate square roots. This provides concrete closed-form identities that verify algebraically the explicit-residual discharges required in [$c_k$ extraction from four algebraic reduction rules](#rem:ck-extraction-from-algebraic-rules) and related proofs.

## Substantive identities

See [Table](#tbl:u-coordinate-discharges-table-data).

Because the substitution removes square roots, each identity reduces to an equality of rational functions in $u$, verified by clearing denominators, with no further input.

## Significance

An explicit-residual discharge that only records that a residual evaluates to $0$ is abstractly trivial: no concrete computation connects it to the underlying substrate arithmetic. The $u$-coordinate identities express the underlying scalars as rational functions in a single variable $u$, so each equality becomes a mechanically checkable identity of rational functions.

For example, the Hecke quadratic relation for every generator of $H_3(q)$ requires a residual to vanish. The substantive reason for this vanishing is the relation $q \cdot (q - q^{-1}) = u - 1$, a non-trivial rational identity.

## Downstream dependencies

These $u$-coordinate identities act as the computational backing for several downstream blocks:

- [$c_k$ extraction from four algebraic reduction rules](#rem:ck-extraction-from-algebraic-rules) rests on these identities for its explicit-residual discharges.
- [$H_3(q)$ Hecke idempotents](#rem:h3-hecke-idempotents) reduces its computation of $\dim_q(V_{(2,1)})^2$ to a rational function of $u$.
- [Hoefsmit seminormal matrix for $V_{(2,1)}$ and the Markov-symmetrized cos character](#prop:hoefsmit-V21-cos-symmetrization) gives a square-root-free closed form for the Hoefsmit coupling $b^2$ as a rational function of $u$.
