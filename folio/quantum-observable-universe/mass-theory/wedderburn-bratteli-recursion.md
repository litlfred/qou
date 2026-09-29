*The Jones-Markov weights $\{y_\lambda^{(n)}\}_{n \geq 1}$ satisfy a multiplicity-free Bratteli recursion. For every $\lambda \,\vdash\, n + 1$:*

$$
  y_\lambda^{(n+1)}
  \;=\;
  z \cdot
  \sum_{\mu \nearrow \lambda}
    F_q\bigl(c(\lambda, \mu),\, \mathrm{hooks}(\lambda)\bigr)
  \cdot y_\mu^{(n)}.
$$

*The sum runs over Bratteli edges $\mu \subset \lambda$. The coefficient $F_q$ is a q-rational function determined by the Hoefsmit seminormal eigenvalues.*

This recursion confirms that $\alpha_k(H_n)$ at a fixed $k$ involves only finitely many strata. The tower of Jones-Markov weights propagates without requiring expensive $p(n) \times p(n)$ linear-system solves.
