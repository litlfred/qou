*Let $\sigma_i$ be the symmetric Hecke generators with eigenvalues $q, -q^{-1}$. The central coefficients $y_\lambda$ in the Jones-Markov trace admit the closed form:*

$$
  \boxed{\;
    y_\lambda \;=\; \frac{s_\lambda(1, Q, Q^2, \ldots, Q^{r-1})}
                        {\sum_{\mu \,\vdash\, n} d_\mu \cdot s_\mu(1, Q, Q^2, \ldots, Q^{r-1})}
  \;}
$$

*where $Q = q^2$, $d_\mu$ is the hook-length dimension, and $r$ is the unique solution to:*

$$
  q \cdot z \;=\; \frac{Q^r (1 - Q)}{1 - Q^r}.
$$

*This resolves the convention mismatch between the symmetric Hecke formulation and the standard Wenzl formulas.*

The Wenzl-bridge identifies $y_\lambda$ symbolically. Substitute $Q=q^2$ and $z_{\mathrm{GL}}=q \cdot z$ into the principal-specialisation Schur element. This avoids explicit linear-system solves and delivers polynomial q-rational forms in a fraction of the computation time.
