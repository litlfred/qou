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

The graded-Mikusiński depth-$n$ cyclotomic content coincides with the Dirichlet $L$-value content at integer $n$, up to $\mathbb{Q}(\zeta_K)$-linear combinations. Beilinson's conjecture at $\mathbb{Q}(\zeta_K)$ depth $n$ becomes the Beilinson conjecture on $L$-values of Dirichlet characters.
