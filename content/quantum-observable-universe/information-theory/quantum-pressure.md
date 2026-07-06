Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with quantum temperature $T_q = \hbar_q$
([quantum temperature](#def:quantum-temperature)).
Let $U \subset M$ be a region of the brane with boundary
$\partial U$, and let $\mathfrak{S}_q(K)$ denote the categorical action
of a knot configuration $K$ in $U$
([categorical action](#def:categorical-action)).
The **quantum pressure** on $\partial U$ is

$$
  P_q(U) \;:=\;
  -\,\frac{\partial F_q}{\partial V_q}\bigg|_{T_q},
$$

where $F_q = -T_q \ln Z_q$ is the quantum free energy and

$$
  Z_q(U) \;=\;
  \mathrm{tr}_{\mathrm{Ad}}
  \!\sum_{K \,\in\, \mathrm{Conf}(U)}
  e^{-\beta_q \, \mathfrak{S}_q(K)}
$$

is the partition function over the configuration space
$\mathrm{Conf}(U)$ of knot states in $U$, with
$\beta_q = 1/\hbar_q = t_P(q)$.

The pressure decomposes as

$$
  P_q \;=\; P_q^{(\mathrm{bulk})}
  \;+\; P_q^{(\mathrm{boundary})},
$$

where the bulk term is the volume derivative of
$\ln Z_q$ at fixed boundary conditions, and the boundary
term arises from the $q$-anomaly ($d_q^2 \neq 0$):

$$
  P_q^{(\mathrm{boundary})}
  \;=\; \frac{\hbar_q^2}{V_q}
  \,\mathrm{tr}_{\mathrm{Ad}}
  \!\oint_{\partial U}
  \langle d_q K \,,\, d_q K \rangle_A,
$$

where $\langle\,\cdot\,,\,\cdot\,\rangle_A$ is the
Frobenius pairing
([Frobenius pairing](#def:frobenius-pairing)).

**Archimedean specialisation (§7c).** This block is stated over the real field $\mathbb{R}$ — the archimedean side of the substrate wall: its constructs are real-valued (physical observables, real-analytic bounds, or numerical evaluations at the substrate parameter $q_0$) rather than generic-ring $q$-deformation data. The generic categorical / $q$-deformation machinery it draws on is stated over an abstract coefficient ring in its own blocks; only the archimedean realisation is specialised here.
