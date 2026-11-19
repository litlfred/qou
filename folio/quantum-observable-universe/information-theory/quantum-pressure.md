Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with quantum temperature $T_q = \hbar_q$. Let $U \subset M$ be a region of the brane with boundary $\partial U$. Let $\mathfrak{S}_q(K)$ denote the categorical action of a knot configuration $K$ in $U$.

The **quantum pressure** on $\partial U$ is defined as
$$
  P_q(U) = -\,\frac{\partial F_q}{\partial V_q}\bigg|_{T_q}.
$$
Here $F_q = -T_q \ln Z_q$ is the quantum free energy and
$$
  Z_q(U) = \mathrm{tr}_{\mathrm{Ad}} \!\sum_{K \,\in\, \mathrm{Conf}(U)} e^{-\beta_q \, \mathfrak{S}_q(K)}
$$
is the partition function over the configuration space $\mathrm{Conf}(U)$ of knot states in $U$, taking $\beta_q = 1/\hbar_q = t_P(q)$.

The pressure decomposes into bulk and boundary components:
$$
  P_q = P_q^{(\mathrm{bulk})} + P_q^{(\mathrm{boundary})}.
$$
The bulk term represents the volume derivative of $\ln Z_q$ at fixed boundary conditions. The boundary term arises directly from the $q$-anomaly ($d_q^2 \neq 0$) at $\partial U$:
$$
  P_q^{(\mathrm{boundary})} = \frac{\hbar_q^2}{V_q} \,\mathrm{tr}_{\mathrm{Ad}} \!\oint_{\partial U} \langle d_q K \,,\, d_q K \rangle_A.
$$
The pairing $\langle\,\cdot\,,\,\cdot\,\rangle_A$ is the Frobenius pairing.
