Two computational operations seemingly contradict: single Hecke crossings obey Markov locality, yet composite braid evaluation via Gröbner–Shirshov reduction is non-local. Wenzl's product factorisation reconciles them.

Let $\beta = \sigma_{i_1} \cdots \sigma_{i_N}$ have Gröbner–Shirshov normal form $\mathrm{NF}_{\mathrm{GS}}(\beta) = e_{j_1} \cdots e_{j_M}$. 
1. **Markov locality.** For every $x$, $\mathrm{tr}_{M, n+1}(x \sigma_n) = z\, \mathrm{tr}_{M, n}(x)$ and $\mathrm{tr}_{M, n+1}(x \sigma_n^{-1}) = z_{-}\, \mathrm{tr}_{M, n}(x)$, where $z_{-} = z - (q - q^{-1})$. A single newly-added crossing contributes a scalar — depending only on the crossing sign — independent of the upstream history.
2. **GS non-locality.** $\mathrm{NF}_{\mathrm{GS}}(\beta)$ depends on the full word. Rewriting rules act non-locally across $\beta$.
3. **Product factorisation.** The Markov trace of the normal form decomposes locally: $\mathrm{tr}_M(\rho_{\mathrm{NF}}(\beta)) = \prod_{i = 1}^{M} \widehat{V}_i(q)$. Each vertex volume $\widehat{V}_i$ depends only on its own normal-form generator and modified coefficients produced by the GS algorithm.

The GS algorithm digests global entanglement into local coefficients. After digestion, the Markov trace factorises locally over the normal form. The process is therefore local after normalisation.
