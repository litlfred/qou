*Let $x^* \in \mathbb{R}^6$ be an optimum of the operator-selection linear program*

$$
  \min_x \; t^\top x
  \quad\text{subject to}\quad
  \sum_i x_i = n_{\mathrm{target}}, \qquad G x \geq 0, \qquad x \geq 0,
$$

*where $G$ is the Frobenius Gram matrix and $t$ is the mass-coefficient vector, so that $t^\top x^* = \mathrm{tr}_M(x^*)$. Then:*

1. *$x^*$ is LP-stable: $Gx^* \geq 0$ in all six channels.*
2. *Strong duality holds: there is a dual optimum whose net-constraint shadow price $y_0^*$ satisfies $\mathrm{tr}_M(x^*) = y_0^* \cdot n_{\mathrm{target}}$.*

Both parts hold for every Gram matrix $G$ and cost vector $t$. Part 1 is the feasibility of $x^*$, and part 2 is finite-dimensional linear-programming strong duality. The confinement-specific properties of the six-channel matrix at the substrate are recorded in the [confinement reading](#rem:lp-dual-stability-confinement-reading).
