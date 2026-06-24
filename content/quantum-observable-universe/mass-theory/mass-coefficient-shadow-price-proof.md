The [operator selection LP](#prop:operator-selection-lp) at
Hecke level $k$ selects the nuclear operator
$\Phi = \sum_i x_i b_i \in H_k(R, q)$ by:

$$
  \min_x \; \sum_i t_i \, x_i
  \quad \text{s.t.} \quad
  \mathbf{1}^T x = n_{\mathrm{target}}, \;\;
  G x \geq 0
$$

where $t_i = \mathrm{tr}_M(b_i)$ and $G_{ij} = \mathrm{tr}_M(b_i b_j)$
is the [Frobenius Gram matrix](#prop:frobenius-gram-matrix).

In the Wedderburn basis $\{e^\lambda_{ij}\}$, the Gram matrix
block-diagonalises: $G = \bigoplus_\lambda G_\lambda$ with
$G_\lambda = (w_\lambda / d_\lambda) \, I_{d_\lambda^2}$, where
$w_\lambda = \dim_q(\lambda)^2 / [k]_q!$ and $d_\lambda = \dim(\lambda)$.
The Frobenius constraint $Gx \geq 0$ separates into one constraint
per partition $\lambda$:

$$
  \langle \Phi, \pi_\lambda \rangle_F
  = \frac{w_\lambda}{d_\lambda} \, \mathrm{tr}(\Phi_\lambda)
  \geq 0
$$

where $\Phi_\lambda$ is the projection of $\Phi$ onto the
$\lambda$-block and $\pi_\lambda$ is the central idempotent.

**Dual program.**  The dual of the spectral LP is:

$$
  \max_{u_0, \, u_\lambda \geq 0} \;\; n_{\mathrm{target}} \cdot u_0
$$

$$
  \text{s.t.} \quad
  u_0 + \frac{w_\lambda}{d_\lambda} \, u_\lambda
  \leq \frac{w_\lambda}{d_\lambda}
  \quad \forall \, \lambda \vdash k
$$

By strong duality (the feasible set is non-empty and bounded),
primal and dual optima coincide.  The optimal dual variables
$u_\lambda^*$ satisfy complementary slackness:

$$
  u_\lambda^* \cdot \langle \Phi^*, \pi_\lambda \rangle_F = 0
$$

**Factorisation.**  For the nuclear braid $\Phi(Z,N)$, each
dual variable factors as:

$$
  u_\lambda^*(Z,N) = C_\lambda \cdot S_\lambda(Z,N,A)
$$

where:

1. $C_\lambda$ is a **q-integer product** determined by the
   partition algebra (hooks, contents, Frobenius coordinates)
   — independent of any nuclear datum.

2. $S_\lambda(Z,N,A)$ is the **scaling function** determined by
   the content sum $c(\lambda) = \sum_
$\qquad\blacksquare$
