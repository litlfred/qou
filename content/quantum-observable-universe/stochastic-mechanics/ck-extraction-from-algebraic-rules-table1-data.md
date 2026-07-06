| # | Rule | Lean class | Substantive content |
|---:|---|---|---|
| 1 | Braid (Yang-Baxter) cubic | `YangBaxterRule n q` | $\sigma_i \sigma_{i+1} \sigma_i = \sigma_{i+1} \sigma_i \sigma_{i+1}$. At $n=3$ on $V_{(2,1)}$, this follows from `hoefsmit_sigma{0,1}` matrix identities. |
| 2 | $q$-Young symmetrizers | `QYoungSymmetrizers n q` | Hecke idempotents $e_\lambda \in H_n(q)$ project onto Wedderburn blocks $V_\lambda$, with $\sum_{\lambda \vdash n} e_\lambda = 1$. |
| 3 | Hecke quadratic at every generator | `HeckeQuadraticAllGenerators n q` | $\sigma_i^2 = (q-q^{-1})\sigma_i + 1$ for all $i$. At $V_{(2,1)}$, this is discharged by `hoefsmit_sigma{0,1}_hecke_quadratic`. |
| 4 | Gröbner-Shirshov / jet reduction | `GBJetReduction k` | This specifies a unique normal form for the typed-$\mathbf{B}_3$ character at order $(q-1)^{2k}$ in the jet polynomial ring. |
