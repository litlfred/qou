Let $\beta = \sigma_{i_1} \cdots \sigma_{i_N}$ have Gröbner–Shirshov normal form $\mathrm{NF}_{\mathrm{GS}}(\beta) = e_{j_1} \cdots e_{j_M}$. Three facts reconcile the locality of single Hecke crossings with the non-locality of Gröbner–Shirshov reduction.

1. **Markov locality.** For every $x$,
$$
  \mathrm{tr}_{M, n+1}(x \sigma_n) = z\, \mathrm{tr}_{M, n}(x), \qquad
  \mathrm{tr}_{M, n+1}(x \sigma_n^{-1}) = z_{-}\, \mathrm{tr}_{M, n}(x), \qquad
  z_{-} = z - (q - q^{-1}).
$$
A single newly-added crossing contributes a scalar — depending only on the crossing sign — independent of the upstream history.
2. **GS non-locality.** $\mathrm{NF}_{\mathrm{GS}}(\beta)$ depends on the full word; rewriting rules act non-locally across $\beta$.
3. **Product factorisation.** The Markov trace of the normal form decomposes locally, $\mathrm{tr}_M(\rho_{\mathrm{NF}}(\beta)) = \prod_{i = 1}^{M} \widehat{V}_i(q)$, where each vertex volume $\widehat{V}_i$ depends only on its own normal-form generator and modified coefficients produced by the GS algorithm.
