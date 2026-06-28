The confinement LP ([confinement LP](#prop:confinement-lp)) selects the
Borromean link $\mathcal{B}_3$ as the unique optimizer over the $6$-element
NF basis of $H_3(q)$.  We now formulate the **general LP** for knot operator
selection in $H_n(q)$ for arbitrary strand number $n$, with the confinement
LP recovered as the special case $n = 3$, $d = 6$.

## Input / Output

**Input.**

- Strand number $n \geq 2$.
- A basis $\{b_1, \ldots, b_d\}$ of $H_n(q)$ (the NF basis, with
  $d = \dim H_n(q) = n!$).
- Markov traces $t_i = \mathrm{tr}_M(b_i)$ for each basis element.
- The $d \times d$ Frobenius Gram matrix
  $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$
  ([Frobenius Gram matrix](#prop:frobenius-gram-matrix)).
- A target net value $n_{\mathrm{target}} \in \mathbb{R}_{>0}$
  (the normalised categorical mass of the desired state).

**Output.**

- The optimal coefficient vector $x^* \in \mathbb{R}^d$ such that
  $\Phi^* = \sum_{i=1}^{d} x_i^* b_i$ is the minimum-action knot
  operator satisfying all Frobenius positivity and net constraints.
- The dual certificate $(y_0^*, y^*)$ proving optimality.

## Primal program (operator selection)

**Proposition (general operator selection LP).**
*The knot operator $\Phi = \sum_{i=1}^{d} x_i b_i \in H_n(q)$ for a
target interaction with net value $n_{\mathrm{target}}$ is the solution
of the linear program:*

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

*where $M > 0$ is a sufficiently large constant ensuring boundedness of
the feasible polyhedron.*

The objective $\sum_{i} t_i x_i = \mathrm{tr}_M(\Phi)$ is the categorical
action ([knot operator selection](#prop:knot-operator-selection), part iv).
Minimizing it selects the operator of least action among all operators
compatible with the Frobenius structure.

The Frobenius positivity constraints $Gx \geq 0$ encode the
demand--supply balance: $\Phi$ must pair non-negatively with every
basis element under the Frobenius inner product, so no channel
carries unbounded demand.

**LP over motivic shadows, not real numbers.**
*The data feeding the LP — Markov traces $t_i = \mathrm{tr}_M(b_i)$
and Frobenius Gram entries $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$ —
are formal elements of $\mathbb{Z}[q^{\pm 1/2}, (q-q^{-1})^{-1}]$,
hence elements of the Habiro completion $\widehat{\mathbb{Z}[q]}$
([Habiro ring](#def:habiro-ring)). The selection of the operator
$\Phi^* = \sum_i x_i^* b_i$ is therefore a combinatorial problem
over the **motivic shadows** of the
[motivic substrate](#def:motivic-substrate) — the algebraic data
of the Hecke algebra independently of any place-realization.
Strong duality (which produces the Borromean $\mathcal{B}_3$ as the
unique optimizer at $n=3$) is a purely algebraic consequence of the
LP; only **after** the optimizer is selected does the archimedean
realization $\rho_\infty$
([archimedean realization](#def:archimedean-realization-functor))
project the dual prices and objective value into physical binding
energies in $\mathbb{R}$. The non-archimedean realizations
$\rho_p$ recover the LP's cyclotomic shadows at each finite place
$p$ — useful for verifying optimality at roots of unity without
$\mathbb{C}$-evaluation.*

## Dual program (demand pricing)

By LP duality, the dual of the primal is:

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

For large $M$ the slack variables $s_i$ are driven to zero at optimality,
and the effective dual simplifies to:

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
