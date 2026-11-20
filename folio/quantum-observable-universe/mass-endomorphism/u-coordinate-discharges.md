**Macdonald coordinate $u = q^2$ substantive discharges for $H_3 / V_{(2,1)}$ scalar invariants.**

Many scalar invariants in the Hecke and Wenzl-bridge algebras are rational in the Macdonald coordinate $u = q^2$, even when their defining formulas involve square roots of expressions in $q$. The Macdonald substitution eliminates the square roots and yields concrete, closed-form rational identities that algebraically verify the explicit-residual discharges required in [$c_k$ extraction from four algebraic reduction rules (Yang-Baxter](#rem:ck-extraction-from-algebraic-rules) and related proofs.

## Substantive identities

See [Table](#tbl:u-coordinate-discharges-table-data).

Because the substitution removes square roots, each scalar identity reduces to an identity of rational functions in $u$ and is proved by clearing denominators.

## Significance

A residual that is merely asserted to vanish carries no computation connecting it to the underlying substrate arithmetic. The $u$-coordinate identities express the underlying scalars as rational functions in a single variable $u$, so the equalities reduce to identities of rational functions.

For example, the Hecke quadratic residual vanishes for all generators of $H_3$. The substantive reason for this vanishing is the relation $q \cdot (q - q^{-1}) = u - 1$, a non-trivial rational identity.

## Downstream dependencies

These $u$-coordinate identities act as the computational backing for several downstream results:

- [$c_k$ extraction from four algebraic reduction rules](#rem:ck-extraction-from-algebraic-rules) uses these identities to justify its residual discharges.
- [$H_3(q)$ Hecke idempotents](#rem:h3-hecke-idempotents) uses the $u$-form of $\dim_q(V_{(2,1)})^2$.
- [The Hoefsmit seminormal matrix for $V_{(2,1)}$](#prop:hoefsmit-V21-cos-symmetrization) has a square-root-free closed form in $u$ for the Hoefsmit coupling $b^2$.
