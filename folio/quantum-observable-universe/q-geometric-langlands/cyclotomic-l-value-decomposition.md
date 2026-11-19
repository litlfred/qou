The cyclotomic $\mathrm{Cl}_n$ values established as a basis for the depth-$n$ content over $\mathbb{Q}(\zeta_K)$ are $\mathbb{Q}$-linearly equivalent to Dirichlet $L$-values $L(\chi, n)$ for primitive Dirichlet characters $\chi$ mod $K$ with $\chi(-1) = (-1)^n$.

For prime $K \geq 3$ and integer $n \geq 1$ with parity matching the character class:

$$
  L(\chi, n) \;=\; \frac{G(\chi)}{K^n}\, \sum_{a = 1}^{K - 1} \overline{\chi(a)} \cdot \mathrm{Cl}_n(2\pi a/K),
$$

where $G(\chi) = \sum_{a = 1}^{K - 1} \chi(a) \zeta_K^a$ is the Gauss sum. Inverting via character orthogonality yields:

$$
  \mathrm{Cl}_n(2\pi a/K)
  \;=\;
  \frac{1}{\varphi(K)}\, \sum_\chi G(\overline{\chi}) \chi(a) \cdot \frac{K^n}{G(\chi)}\, L(\chi, n).
$$

Each $\mathrm{Cl}_n(2\pi a/K)$ is a $\mathbb{Q}(\zeta_K)$-linear combination of $L(\chi, n)$ values, and vice versa.

At $N = 4$ and $n = 3$, this recovers a Catalan-like depth-3 $L$-value:

$$
  \beta(3) \;=\; L(\chi_4, 3) \;=\; \mathrm{Im}\,\mathrm{Li}_3(i) \;=\; \frac{\pi^3}{32},
$$

where $\chi_4$ is the non-trivial Dirichlet character mod 4 ($\chi_4(1) = 1, \chi_4(3) = -1$) and $\beta$ is the Dirichlet beta function. The $N=5$ cyclotomic depth-3 content yields a single generator $\mathrm{Cl}_3(2\pi/5) - \mathrm{Cl}_3(4\pi/5) \approx 0.95572$, corresponding to the two odd Dirichlet characters $\chi_5$, $\chi_5^3$ mod 5.

**Constructive proof from Theorem A.**  By
[Jonquière cyclotomic Tate-rationality](#prop:jonquiere-cyclotomic-tate-rationality)
at $(n, K) = (3, 4)$:

$$
  \mathrm{Im}\,\mathrm{Li}_3(\zeta_4) \;=\; \frac{(K - 1)(K - 2)\pi^3}{3 K^3}
  \;=\; \frac{3 \cdot 2 \cdot \pi^3}{3 \cdot 64} \;=\; \frac{\pi^3}{32}.
$$

Since $\zeta_4 = i$:

$$
  \mathrm{Im}\,\mathrm{Li}_3(i) \;=\; \sum_{m=0}^{\infty} \frac{\sin((2m+1)\pi/2)}{(2m+1)^3}
  \;=\; \sum_{m=0}^{\infty} \frac{(-1)^m}{(2m+1)^3}
  \;=\; \beta(3).
$$

So $\beta(3) = \pi^3/32$, a classical result, is a **corollary of
Theorem A**. $\square$

The numerical verification, the $N=5$ instance, the analytic-number-theory bridge, the Catalan-constant instance, and cross-references are recorded in the [details note](#rem:cyclotomic-l-value-decomposition-details).
