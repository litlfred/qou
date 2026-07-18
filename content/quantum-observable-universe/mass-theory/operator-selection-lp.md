**Proposition (general operator-selection LP).**
*Let $n \geq 2$, let $\{b_1, \ldots, b_d\}$ be a basis of $H_n(q)$ (the NF basis, with $d = n!$), let $t_i = \mathrm{tr}_M(b_i)$ be the Markov traces, let $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ be the $d \times d$ Frobenius Gram matrix, and let $n_{\mathrm{target}} \in \mathbb{R}_{>0}$ be a target net value. The knot operator $\Phi = \sum_{i=1}^{d} x_i b_i \in H_n(q)$ for a target interaction with net value $n_{\mathrm{target}}$ is the solution $x^* \in \mathbb{R}^d$ of the linear program*

$$
  \min_{x \in \mathbb{R}^d} \quad \sum_{i=1}^{d} t_i \, x_i
$$

*subject to:*

$$
  \sum_{i=1}^{d} x_i = n_{\mathrm{target}}
  \qquad (\text{net constraint})
$$

$$
  \sum_{j=1}^{d} G_{ij}\, x_j \geq 0
  \quad \forall\, i \in \{1, \ldots, d\}
  \qquad (\text{Frobenius positivity})
$$

$$
  x_i \geq -M \quad \forall\, i
  \qquad (\text{boundedness})
$$

*where $M > 0$ is a constant large enough to ensure boundedness of the feasible polyhedron. The optimizer $\Phi^* = \sum_{i} x_i^* b_i$ is the minimum-action knot operator satisfying all Frobenius positivity and net constraints; the dual certificate $(y_0^*, y^*)$ proves its optimality.*

## Dual program (demand pricing)

By LP duality, the dual is:

$$
  \max_{y_0, \, y \in \mathbb{R}^d} \quad n_{\mathrm{target}} \cdot y_0
  - M \sum_{i=1}^{d} s_i
$$

*subject to:*

$$
  y_0 + \sum_{i=1}^{d} G_{ji}\, y_i - s_j \leq t_j
  \quad \forall\, j \in \{1, \ldots, d\}
$$

$$
  y_i \geq 0, \quad s_i \geq 0 \quad \forall\, i
$$

For large $M$, the slack variables $s_i$ are driven to zero at optimality. The effective dual simplifies to:

$$
  \max_{y_0, \, y \geq 0} \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to:*

$$
  y_0 + \sum_{i=1}^{d} G_{ji}\, y_i \leq t_j
  \quad \forall\, j \in \{1, \ldots, d\}
$$

## Strong duality

**Proposition (strong duality).**
*The primal and dual programs have equal optimal values:*

$$
  \sum_{i=1}^{d} t_i \, x_i^*
  \;=\;
  n_{\mathrm{target}} \cdot y_0^*
$$
