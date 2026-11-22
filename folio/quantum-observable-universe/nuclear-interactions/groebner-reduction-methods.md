Compute the Hecke algebra normal form by iterative Gröbner–Shirshov reduction with three rewriting rules:

1. **Hecke relation** (Rule 0): $\sigma_i^2 \to (q - q^{-1})\sigma_i + \mathbf{1}$.
2. **Far commutativity** (Rule 1): $\sigma_i \sigma_j \to \sigma_j \sigma_i$ for $|i - j| \geq 2$.
3. **Yang–Baxter relation** (Rule 2): $\sigma_i \sigma_{i+1} \sigma_i \to \sigma_{i+1} \sigma_i \sigma_{i+1}$.

The reduction is confluent. The final normal form is independent of the order in which rules are applied. The intermediate word count, however, depends critically on the reduction strategy.

## The $h_{\mathrm{A}}$-power factorization

For the $\mathfrak{p}\mathfrak{p}\cdots\mathfrak{n}\mathfrak{n}$ ordering, every normal form coefficient factors as $\pm 2^a \times h_{\mathrm{A}}^k$. This factorization enables a compressed representation. For atoms with mixed orderings, the factorization breaks.

## Computational engines

Four Rust engines implement the reduction with increasing optimization: v9 (hecke-bigint), v11 (hecke-modular), v13 (hecke-stream), and v14 (hecke-hapower).

## LP-dual reduction ordering

Since confluent reductions permit arbitrary rule ordering, the LP dual determines the most efficient strategy:

- **Cancellation-first**. Apply Rule 0 when the shortened word already exists in the stable set.
- **Leading-term cancellation**. Consolidate pending words before reduction.
- **Crossing order**. Adjacent generators do not commute. Only far-commuting pairs may be reordered.

## Reproducibility

All computations are reproducible from the Rust source. The engine generates certificates and commits them to the repository. Witness files record every mass prediction with full intermediate values.
