Confinement operator selection takes the form of a linear program over the NF basis of $H_3(q)$. This connects the categorical minimum-action principle to standard LP duality theory, providing a rigorous proof of uniqueness.

## Primal program (operator selection)

**Proposition.**
*The confinement operator $\Phi = \sum_{i=1}^{6} x_i b_i \in H_3(q)$ for quark types $(f_1, f_2, f_3)$ is the solution of:*

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

*where $t_i = \mathrm{tr}_M(b_i)$ are the Markov traces of the basis elements, $G_{ij}$ is the Frobenius Gram matrix, $n_{\mathrm{target}}$ is the invariant net demand of the state, and $M$ is a large constant.*

The objective $\sum t_i x_i = \mathrm{tr}_M(\Phi)$ is the categorical action. The Frobenius positivity constraint $Gx \geq 0$ ensures that $\Phi$ pairs non-negatively with all basis elements.

## Dual program (deficit satisfaction)

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

The dual variable $y_0$ is the shadow price of the net constraint. The dual variables $y_i$ are the shadow prices of the Frobenius positivity constraints.

Strong duality holds because the feasible set is non-empty and bounded.

## $\mathcal{B}_3$ as the LP solution

At specific topological evaluations, the LP has an optimal vertex at $x^* = \mathrm{NF}(\mathcal{B}_3)$.

The Frobenius positivity constraints are tight at two indices ($\sigma_0$ and $L_-$), giving the two active deficit channels that correspond to the residual deficit.

## Caveat: $\mathcal{B}_3$ is a local minimum

With the corrected Markov trace $\mathrm{tr}_M(e^-) = z^3$, the Gram matrix acquires a negative eigenvalue. The LP has a global minimum at $\mathrm{tr}_M = 0$. The Borromean solution $\mathcal{B}_3$ is a local minimum.

## Quadratic extension

When the interaction involves a bilinear Frobenius pairing $\langle \Phi, K \rangle_F = x^T G y$, the optimization becomes a quadratic program:

$$
  \min_{x} \quad x^T G y
  \qquad \text{s.t.} \quad
  \mathbf{1}^T x = n_1, \quad
  \mathbf{1}^T y = n_2, \quad
  Gx \geq 0
$$

When $y$ is fixed, $x^T G y$ is linear in $x$, reducing to a standard LP. When both $x$ and $y$ vary, the objective is bilinear with **degenerate** $G$ — under convention D the Markov–Gram form has a one-dimensional radical (the $(1^3)$ block), so the quadratic program is posed on the quotient rather than on the full NF span. On the star pairing $\mathrm{tr}_M(b_i b_j^*)$ the form is positive semidefinite, $(5,0,1)$; the older reading as indefinite quoted the bilinear pairing without naming it and is withdrawn (2026-08-09). **Open (2026-08-09).** Whether the cone constraint $G x \geq 0$ above is to be taken in the full six-dimensional NF span or in the radical quotient is not settled here; it is the same question as Term 4 of the six-term mass identity and is reserved for the owner. The nuclear assembly step fixes $y = \mathrm{NF}(\mathfrak{N}_{k+1})$ and solves the resulting LP.
