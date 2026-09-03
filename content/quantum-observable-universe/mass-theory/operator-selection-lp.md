**Proposition (general operator-selection LP).**
*Let $n \geq 2$, let $\{b_1, \ldots, b_d\}$ be a basis of $H_n(q)$ (the NF basis, with $d = n!$), let $t_i = \mathrm{tr}_M(b_i)$ be the Markov traces, let $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ be the $d \times d$ Frobenius Gram matrix, and let $n_{\mathrm{target}} \in \mathbb{R}_{>0}$ be a target net value. Consider the linear program*

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

*where $M > 0$ is a constant large enough to ensure boundedness of the feasible polyhedron. Any minimiser $\Phi^* = \sum_{i} x_i^* b_i$ lies in $H_n(q)$ and satisfies every Frobenius positivity and net constraint; the dual certificate $(y_0^*, y^*)$ certifies optimality.*

## Degeneracy of this program

Two properties of the program as stated, both proved and neither previously
recorded. They are stated here because downstream blocks have read the program
as a *selection principle*, which it is not.

**The optimal value is identically zero.** The NF basis begins with the empty
word, so $b_1 = \mathbf{1}$ and hence

$$G_{1j} \;=\; \mathrm{tr}_M(\mathbf{1}\cdot b_j) \;=\; t_j .$$

The first row of the Gram matrix is the objective vector, so the Frobenius
positivity constraint at $i = 1$ reads $\sum_j t_j x_j \geq 0$ — the objective
itself, bounded below by zero. The program therefore minimises $t\cdot x$
subject to $t\cdot x \geq 0$, and its optimal value is $0$ whenever it is
feasible. This requires only that the basis contain the identity, so it holds
for every $n$, every $q$, and every trace convention. By strong duality
$n_{\mathrm{target}}\cdot y_0^* = 0$ with $n_{\mathrm{target}} > 0$, so
$y_0^* = 0$: the net constraint carries no shadow price, and
$n_{\mathrm{target}}$ cannot influence the objective.

**The set of minimisers is not a point.** It is
$\{x : \sum_i x_i = n_{\mathrm{target}},\; (Gx)_1 = 0,\; (Gx)_i \geq 0\ (i \geq 2)\}$,
a positive-dimensional face. At $n = 3$ it carries at least six vertices, all at
objective $0$, occurring in mirror pairs under $\sigma_0 \leftrightarrow \sigma_1$.
Since $t$ and $G$ are mirror-invariant the optimal set is mirror-closed, so a
unique minimiser would have to be mirror-symmetric; none of these vertices is.
The program therefore does not determine a distinguished $\Phi^*$, and which
vertex a solver returns is a property of its pivoting rule.

## Dual program (demand pricing)

By LP duality, the dual is:

$$
  \max_{y_0, \, y \in \mathbb{R}^d} \quad n_{\mathrm{target}} \cdot y_0 - M \sum_{i=1}^{d} s_i
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
