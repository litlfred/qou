> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$ and Planck time $t_P(q) = q/(q-1) = 1/\hbar_q$ ([Planck time](#def:planck-time)). The **quantum temperature** of a region $U \subset M$ is defined as

$$
  T_q(U) \;:=\; \hbar_q \;=\; \frac{q - 1}{q}.
$$

The inverse temperature is $\beta_q := 1/T_q = t_P(q)$.

The Kashaev volume--density reading ([Kashaev volume--density](#rem:kashaev-volume-density)) introduces the substrate density $\rho_q = 1/\hbar_q^{2}$. In these terms, the temperature and its inverse square are

$$
  T_q \;=\; \rho_q^{-1/2},
  \qquad
  \beta_q^{2} \;=\; \rho_q.
$$

Temperature and substrate density are conjugate square roots. A state at high drag density (small $\hbar_q$) rests at low temperature, while the inverse-temperature squared matches the density itself. This relationship absorbs several dimensional-analysis identities that would otherwise demand independent derivations.

The quantum temperature is the thermodynamic conjugate of the quantum entropy $S_q(U)$ ([quantum entropy](#def:quantum-entropy)):

$$
  \frac{1}{T_q}
  \;=\; \frac{\partial S_q}{\partial \mathfrak{E}_q}\bigg|_V
  \;=\; \frac{1}{\hbar_q}.
$$
