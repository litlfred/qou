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

* For $k = 3$, the residual factor $q^{1/5}$ closes the cot $\theta_W$ discrepancy from $2.19\%$ to $0.13\%$.
* For $k = 4$, the top eigenvalue is degenerate. We verify the conjecture via a pairwise ratio $e[254]/e[188] \approx q^{1/7}$ with $0.14\%$ relative error.
* For $k = 2$, the word collapses to length $0$. This leaves no matrix multiplication to inspect and renders the case untestable.

**Lean status.** We axiomatise the conjecture as a hypothesis-only `class`. We state the spectral content explicitly using `HoefsmitRepresentation.HasEigenvalueRatio`. Downstream Lean theorems take this class as an instance hypothesis and remain rigorous-conditional results.
