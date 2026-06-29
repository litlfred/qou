The confinement operator selection
([confinement selection](#prop:confinement-operator-selection))
can be recast as a **linear program** over the NF basis of $H_3(q)$.
This connects the categorical minimum-action principle to the
standard LP duality theory, providing a rigorous proof of
uniqueness.

## Primal program (operator selection)

**Proposition.**
*The confinement operator $\Phi = \sum_{i=1}^{6} x_i b_i \in H_3(q)$
for quark types $(f_1, f_2, f_3)$ is the solution of:*

$$
  \min_x \quad \sum_{i=1}^{6} t_i \cdot x_i
  \qquad (\text{minimize Markov trace})
$$

*subject to:*

$$
  \sum_{i=1}^{6} x_i = n_{\mathrm{target}}
  \qquad (\text{net constraint})
$$

$$
  \sum_{j=1}^{6} G_{ij} x_j \geq 0
  \quad \forall\, i
  \qquad (\text{Frobenius positivity})
$$

$$
  x_i \geq -M \quad \forall\, i
  \qquad (\text{boundedness})
$$

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the
basis elements, $G_{ij}$ is the Gram matrix
([Frobenius Gram matrix](#prop:frobenius-gram-matrix)),
$n_{\mathrm{target}}$ is the invariant net demand of the state,
and $M$ is a large constant.*

The objective $\sum t_i x_i = \mathrm{tr}_M(\Phi)$ is the
categorical action.  The Frobenius positivity constraint
$Gx \geq 0$ ensures that $\Phi$ pairs non-negatively with all
basis elements.

## Dual program (demand satisfaction)

By LP duality, the dual of the primal is:

$$
  \max_y \quad n_{\mathrm{target}} \cdot y_0
$$

*subject to:*

$$
  y_0 + \sum_{i=1}^{6} G_{ij} y_i \leq t_j
  \quad \forall\, j
$$

$$
  y_i \geq 0 \quad \forall\, i \geq 1
$$

The dual variable $y_0$ is the **shadow price of the net
constraint** — the marginal cost of increasing the target mass.
The dual variables $y_i$ are the **shadow prices of the
Frobenius positivity constraints** — the demand prices.

**Strong duality** (the primal and dual have equal optimal
values) holds because the feasible set is non-empty
($\mathcal{B}_3$ is feasible) and bounded.

## $\mathcal{B}_3$ as the LP solution

At specific topological evaluations (see [numeric probes](#audit:confinement-lp-numeric)), the LP has an optimal vertex
at $x^* = \mathrm{NF}(\mathcal{B}_3)$.

The Frobenius positivity
constraints are **tight** at two indices ($\sigma_0$ and $L_-$),
giving the two active demand channels that correspond to the
residual demand.

## Caveat: $\mathcal{B}_3$ is a local minimum

With the corrected Markov trace $\mathrm{tr}_M(e^-) = z^3$
([corrected trace](#prop:corrected-markov-trace)),
the Gram matrix acquires a negative eigenvalue.
The LP has a global minimum at $\mathrm{tr}_M = 0$ (massless
confined state).  The Borromean solution $\mathcal{B}_3$ is a
**local minimum** — the LP vertex with minimum $|\lambda|$
eigenvalue, not maximum.  See
[$\mathcal{B}_3$ local minimum](#rem:b3-local-minimum)
for interpretation.

## Quadratic extension

When the interaction involves a bilinear Frobenius pairing
$\langle \Phi, K \rangle_F = x^T G y$ (e.g., inter-nucleon
binding), the optimization becomes a **quadratic program**:

$$
  \min_{x} \quad x^T G y
  \qquad \text{s.t.} \quad
  \mathbf{1}^T x = n_1, \quad
  \mathbf{1}^T y = n_2, \quad
  Gx \geq 0
$$

When $y$ is fixed (as in the nuclear assembly step), $x^T G y$
is linear in $x$, reducing to a standard LP.  When both $x$ and
$y$ vary, the objective is bilinear with indefinite $G$ — a
non-convex bilinear program.  The nuclear assembly step (iv) of
the derived atom ([derived atom](#def:derived-atom)) fixes
$y = \mathrm{NF}(\mathfrak{N}_{k+1})$ and solves the resulting LP.
