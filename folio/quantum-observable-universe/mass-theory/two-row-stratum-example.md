We have $|\Lambda^2(n)| = \lfloor n/2 \rfloor + 1$. For the $^4\mathrm{He}$ strand count ($n = 12$), we obtain **7** partitions:
$$
\Lambda^2(12) = \{(12), (11,1), (10,2), (9,3), (8,4), (7,5), (6,6)\}.
$$

Distinguished partitions include:
- $\lambda = (n)$: the trivial representation. It is one-dimensional, $V_{(n)} = \mathbb{C}$.
- $\lambda = (n-1, 1)$: the standard representation. It has dimension $n - 1$.
- Self-conjugate $\lambda \in \Lambda^2(n)$: this is only $(n/2, n/2)$ for even $n$, the **balanced two-row** partition. For $n = 12$, this is $(6, 6)$.

The non-self-conjugate partitions $(n-k, k)$ with $k < n/2$ form mirror pairs under the bar involution $q \mapsto q^{-1}$. The conjugate partition $(n-k, k)'$ exits $\Lambda^2(n)$, so each $(n-k, k)$ pairs with itself under the involution.

**Empirical use.**

We compute the per-partition decomposition $c_\lambda := y_\lambda(q_0) \cdot \chi^\lambda_q(\beta_{^4\mathrm{He}})$ across all 77 partitions of 12. The two-row stratum $\Lambda^2(12)$ carries the total trace $\mathrm{tr}_M(\beta_{^4\mathrm{He}})$ **exactly** — $100\,\%$, not as a measurement but as an identity, since $y_\lambda = 0$ for the $70$ partitions of $12$ with $\ell(\lambda) > 2$. The figure $86.6\,\%$ previously quoted here is the convention-C value and is withdrawn (2026-08-09); with it goes the reading of the result as a *dominance* rather than a support statement. We formalize this in [he4 two row dominance](#prop:he4-two-row-dominance).

We establish the identical pattern across the $\{D, T, {}^3\mathrm{He}, {}^4\mathrm{He}\}$ series. The dominant block for each atom always lies in $\Lambda^2(3A)$.
