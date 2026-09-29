*Proof.*
The single-particle partition function in a single $S^3$ fibre is

$$
  z_q
  \;=\;
  \sum_{K \,\in\, \mathrm{Conf}_p}
  e^{-\beta_q \, \mathfrak{S}_q(K)}.
$$

For $N$ non-interacting knots across $|U|$ brane points, the total partition function is

$$
  Z_q
  \;=\; \frac{1}{N!}
  \left( |U| \cdot z_q \right)^N.
$$

The factor of $1/N!$ accounts for isotopy indistinguishability under the braid group action on $\mathrm{Conf}(U)$. Applying Stirling's approximation and substituting $V_q = |U| \cdot \pi^2 [2]_q$, the free energy $F_q = -T_q \ln Z_q$ yields

$$
  P_q \, V_q
  \;=\; -V_q\,\frac{\partial F_q}{\partial V_q}\bigg|_{T_q}
  \;=\; N \, T_q
$$

at leading order. The $q$-anomaly from $d_q^2 \neq 0$ at $\partial U$ corrects the single-fibre partition function by $\delta \ln z_q = \hbar_q^2 \langle \mathfrak{S}_q \rangle / [2]_q$. This shift produces the full equation of state. $\square$
