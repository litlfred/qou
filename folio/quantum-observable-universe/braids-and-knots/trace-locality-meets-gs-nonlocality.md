Let $\beta = \sigma_{i_1} \cdots \sigma_{i_N}$ have Gröbner–Shirshov normal form $\mathrm{NF}_{\mathrm{GS}}(\beta) = e_{j_1} \cdots e_{j_M}$. Two facts describe the locality of single Hecke crossings with the non-locality of Gröbner–Shirshov reduction.

1. **Markov locality.** For every $x$,
$$
  \mathrm{tr}_{M, n+1}(x \sigma_n) = z\, \mathrm{tr}_{M, n}(x), \qquad
  \mathrm{tr}_{M, n+1}(x \sigma_n^{-1}) = z_{-}\, \mathrm{tr}_{M, n}(x), \qquad
  z_{-} = z - (q - q^{-1}).
$$
A single newly-added crossing contributes a scalar — depending only on the crossing sign — independent of the upstream history.
2. **GS non-locality.** $\mathrm{NF}_{\mathrm{GS}}(\beta)$ depends on the full word; rewriting rules act non-locally across $\beta$.

The two are compatible because they concern different operations: the first is a property of the trace, the second of the reduction to normal form. Whether the trace of the normal form factorises over its letters is discussed in [the product-factorisation check](#rem:trace-locality-product-factorisation-check).
