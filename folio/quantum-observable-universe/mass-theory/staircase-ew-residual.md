**Conjecture (staircase EW-residual).**
*Let $\rho_k = (k, k-1, \ldots, 1)$ be the staircase partition. Let $V_{\rho_k}$ be the corresponding Specht module of $H_{n_k}(q)$. Let $\beta_{\mathrm{EW}}\,\bowtie_K^{\mathrm{minimal}} \in H_{n_k}(q)$ be the canonical electroweak braid word. For every $k \geq 2$, the matrix image*

$$
  \rho_{\rho_k}\!\bigl(\beta_{\mathrm{EW}}\,
                       \bowtie_K^{\mathrm{minimal}}\bigr)
  \;\in\;
  \mathrm{Mat}_{f^{\rho_k} \times f^{\rho_k}}\!\bigl(\mathbb Q(q)\bigr)
$$

*has two nonzero eigenvalues whose pairwise ratio equals*

$$
  q^{1 / h_{\mathrm{corner}}(\rho_k)}
  \;=\; q^{1 / (2k - 1)}.
$$

*The corner-hook length $h_{\mathrm{corner}}(\rho_k)$ is $2k - 1$.*

**Empirical content.**

* For $k = 3$, the residual factor $q^{1/5}$ takes the cot $\theta_W$ discrepancy from $2.19\%$ to $0.13\%$. The exponent is selected rather than derived, and the carrier note below applies; this figure is not a framework accuracy result.
* For $k = 4$, the top eigenvalue is degenerate. The conjecture is checked instead on a pairwise ratio $e[254]/e[188] \approx q^{1/7}$ with $0.14\%$ relative error.
* For $k = 2$, the word collapses to length $0$. This leaves no matrix multiplication to inspect and renders the case untestable.

**Carrier.** The staircase $\rho_k$ has exactly $k$ rows, so the Schur–Weyl row cap — $\dim V_\lambda = 0$ whenever $\ell(\lambda) > N$ — gives $N_{\min}(\rho_k) = k$. The mass fibre is the fundamental of $\mathrm{SU}_q(2)$, so $N = 2$, and exactly one staircase has states: $k = 2$, which the third bullet above calls untestable. Both cases carrying empirical content, $k = 3$ and $k = 4$, lie in the kernel of $H_{n_k}(q) \to \mathrm{TL}_{n_k}(q)$, where the Ocneanu weight $y_{\rho_k}$ vanishes identically.

This bounds what the empirical bullets can mean; it does not touch the conjecture. The conjecture is a statement about Specht modules of $H_{n_k}(q)$, which exist for every partition whatever $N$ is, and the eigenvalue ratio is unaffected. What the row cap removes is the reading. Every route from a block with $\ell(\lambda) > N$ to a physical number is either a Markov trace, which the row cap sends to zero, or a spectrum, which has no states to act on. Subtraction does not open a third: a quantity recovered as a difference of Markov traces is itself a Markov trace, by linearity, and inherits the same vanishing.

**Status.** The statement is a conjecture; results that use it are conditional on it.
