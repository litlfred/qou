*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with $N$ non-interacting particle knots in a region
$U \subset M$.  Let $P_q$, $V_q$, $T_q$ be the quantum
pressure, volume, and temperature of $U$
([quantum pressure](#def:quantum-pressure),
[quantum volume](#def:quantum-volume),
[quantum temperature](#def:quantum-temperature)).
Then the equation of state is

$$
  P_q \, V_q
  \;=\; N \, T_q
  \left(
    1 \;+\; \frac{\hbar_q^2}{[2]_q}
    \,\langle \mathfrak{S}_q \rangle
  \right),
$$

where $\langle \mathfrak{S}_q \rangle$ is the thermal expectation of
the categorical action
([categorical action](#def:categorical-action)) and
$[2]_q = q + q^{-1}$.

*Proof.*
The single-particle partition function in a single $S^3$
fibre is

$$
  z_q
  \;=\;
  \sum_{K \,\in\, \mathrm{Conf}_p}
  e^{-\beta_q \, \mathfrak{S}_q(K)}.
$$

For $N$ non-interacting knots across $|U|$ brane points:

$$
  Z_q
  \;=\; \frac{1}{N!}
  \left( |U| \cdot z_q \right)^N,
$$

where $1/N!$ arises from the braid group action on
$\mathrm{Conf}(U)$ (isotopy-indistinguishability).
The free energy $F_q = -T_q \ln Z_q$ gives, via Stirling
and $V_q = |U| \cdot \pi^2 [2]_q$:

$$
  P_q \, V_q
  \;=\; -V_q\,\frac{\partial F_q}{\partial V_q}\bigg|_{T_q}
  \;=\; N \, T_q
$$

at leading order.  The $q$-anomaly correction from
$d_q^2 \neq 0$ at $\partial U$ shifts the single-fibre
partition function by $\delta \ln z_q = \hbar_q^2 \langle \mathfrak{S}_q \rangle / [2]_q$, producing the full
equation of state.  $\square$
