**Proposition (archimedean brane-tower truncation remainder exponential decay).**

*Let $q > 1$ be a real deformation parameter with quantum Planck ratio $\hbar_q = (q - 1)/q = 1 - q^{-1}$.*

1. *Strict unit-interval containment and exact quadratic brane-tower remainder:* *The ratio satisfies $0 < \hbar_q < 1$ and $0 < \hbar_q^2 < 1$, and for every truncation depth $N \ge 0$ the partial sum $S_N(q) = \sum_{k=0}^N \hbar_q^{2k}$ satisfies*
   $$
     \frac{1}{1 - \hbar_q^2} - \sum_{k=0}^{N} \hbar_q^{2k}
     \;=\;
     \frac{\hbar_q^{\,2(N+1)}}{1 - \hbar_q^2}
     \;=\;
     C(q)\,e^{-c(q)\,N},
   $$
   *where the prefactor and decay rate are strictly positive:*
   $$
     C(q) \;=\; \frac{\hbar_q^2}{1 - \hbar_q^2} \;>\; 0,
     \qquad
     c(q) \;=\; -2\ln\hbar_q \;>\; 0.
   $$
2. *General geometrically majorized spectral and ladder series:* *Let $(a_k)_{k \ge 0}$ be any real sequence satisfying $\lvert a_k \rvert \le M\,r^k$ with $M > 0$ and $0 < r < 1$. Then $\sum_{k=0}^\infty a_k$ converges absolutely, and the depth-$N$ tail remainder $R_N(a) := \sum_{k=0}^\infty a_k - \sum_{k=0}^N a_k$ satisfies*
   $$
     \bigl\lvert R_N(a) \bigr\rvert
     \;\le\;
     \frac{M\,r^{N+1}}{1 - r}
     \;=\;
     \frac{M\,r}{1 - r}\,e^{-(-\ln r)\,N}
     \qquad (N \ge 0),
   $$
   *with positive structural constants $C = M r / (1 - r) > 0$ and $c = -\ln r > 0$.*

## Proof

Since $q > 1$, both $q - 1 > 0$ and $q > 0$, whence $0 < (q - 1)/q < 1$ and $0 < \hbar_q^2 < 1$. Induction on $N$ over any field with $r \ne 1$ gives the telescoping identity $(1 - r)^{-1} - \sum_{k=0}^N r^k = r^{N+1}/(1 - r)$; specializing to $r = \hbar_q^2$ yields the first equality in (1). Because $\hbar_q > 0$, $\exp(2 N \ln\hbar_q) = (\exp(\ln\hbar_q))^{2N} = \hbar_q^{2N}$, so $C(q)\,\exp(-c(q)\,N) = \frac{\hbar_q^2}{1 - \hbar_q^2}\hbar_q^{2N} = \frac{\hbar_q^{2(N+1)}}{1 - \hbar_q^2}$, while $0 < \hbar_q < 1$ gives $\ln\hbar_q < 0$ and therefore $c(q) = -2\ln\hbar_q > 0$.

For (2), comparison with the convergent geometric series $\sum_{k=0}^\infty M r^k$ establishes absolute summability of $(a_k)$ and identifies $R_N(a) = \sum_{j=0}^\infty a_{j + N + 1}$. Triangle inequality on the shifted tail gives $\lvert R_N(a)\rvert \le \sum_{j=0}^\infty M r^{N+1} r^j = M r^{N+1}/(1 - r)$, and rewriting $r^N = \exp(N\ln r) = \exp(-(-\ln r)N)$ completes the bound. $\square$

## Precision ceiling across brane-tower and Convention-D expansions

At the canonical substrate parameter $q_0 \approx 1.1100$, $\hbar_q^2 \approx 9.82 \times 10^{-3} < 10^{-2}$, so each additional rung of the quadratic Hecke brane tower contracts the remainder by more than two orders of magnitude ($c(q_0) = -2\ln\hbar_q \approx 4.624$, $C(q_0) \approx 9.91 \times 10^{-3}$). Applied to the Convention-D $\mathfrak{Q}_\beta$ generating series $\Pi_{\mathrm{op}}(u) = 1 + \sum_{n=2}^\infty p_n u^n$, whose Lagrange–Bürmann radius of convergence $R_u \approx 0.3690$ yields a contraction ratio $r = u(q_0)/R_u \approx 0.02308 < 1/40$, part (2) bounds the $N = 9$ tail strictly below $10^{-16}$ ($< 1\,\mathrm{ppQ}$).
