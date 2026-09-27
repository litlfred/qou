**Conjecture (archimedean remainder exponential decay).**

*Fix a free-neutron sector $K \subset H_3(q)$. Let $\mathfrak{Q}_\beta^{(N)}$ be the depth-$N$ brane-tower truncation of the $\beta$-decay $Q$-value. Let $\mathfrak{Q}_\beta^{\mathrm{exact}}$ be the value of the full spectral decomposition. Then there exist constants $C(K), c(K) > 0$ such that the truncation remainder $R_N(K) \;:=\; \mathfrak{Q}_\beta^{(N)} - \mathfrak{Q}_\beta^{\mathrm{exact}}$ decays exponentially in the truncation depth:*

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  C(K)\,e^{-c(K)\,N}
  \qquad (N \ge 0).
$$

## Geometric and exponential phrasings coincide

The exponential form above and the geometric form used by the categorical precision ladder are the same statement. With $\hbar_q = (q_0 - 1)/q_0$, the Hecke quadratic structure gives the explicit ceiling

$$
  \bigl\lvert R_N(K) \bigr\rvert
  \;\le\;
  \frac{\hbar_q^{\,2(N+1)}}{1 - \hbar_q^{2}}.
$$

This is exactly $C \, e^{-c N}$ with $c \;=\; -2\ln \hbar_q$ and $C \;=\; \frac{\hbar_q^{2}}{1 - \hbar_q^{2}}$. The geometric ceiling above acts as the canonical witness rate.

## Purpose of the bound

This open conjectural input collapses the formally infinite brane-tower product to a finite-precision real prediction. With the bound in hand, each new rung tightens the prediction by a factor $\hbar_q^{2} \approx 100^{-1}$. This provides the precision-ceiling used by the precision ladder. Form A at $N = 0$ already yields a $+0.168\%$ residual because the $N = 0$ term sits inside the structural ceiling.
