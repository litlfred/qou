*Let $n$ be the Hecke strand count at confinement level $\ell$. Let $(\pi_\lambda)_{\lambda \vdash k, k \le n}$ be the central idempotents projecting onto the Wedderburn blocks of $H_n(q)$. Let $T$ be the cost operator. The confined operator at $q$ is the solution $\Phi^* \succeq 0$ of the primal matrix program:*

$$
  \min_{\Phi \succeq 0} \quad \langle T, \Phi \rangle
$$

*subject to:*

1. *(Per-block Frobenius positivity)* $\langle \pi_\lambda, \Phi \rangle \ge 0$ for all $\lambda \vdash k, k \le n$.
2. *(Adjacent-pair PSD)* Every $2 \times 2$ block corresponding to an adjacent generator pair $(\sigma_i, \sigma_{i+1})$ is positive semi-definite.
3. *(Normalisation)* $\mathrm{tr}(\Phi) = n_{\mathrm{target}}$.

*The dual program determines the matrix shadow prices:*

$$
  \max_{y_0, (y_\lambda \ge 0)} \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to the matrix inequality:*

$$
  y_0 \cdot I \;+\; \sum_\lambda y_\lambda \cdot \pi_\lambda \;-\; T
  \;\preceq\; 0.
$$

*At the generic $q$ optimum, strong duality holds and complementary slackness applies as a matrix equation.*
