Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe
with quantum temperature $T_q = \hbar_q$
([quantum temperature](#def:quantum-temperature)).
Let $U \subset M$ be a region of the brane with boundary
$\partial U$, and let $S_q(K)$ denote the categorical action
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
  e^{-\beta_q \, S_q(K)}
$$

is the partition function over the configuration space
$\mathrm{Conf}(U)$ of knot states in $U$.  Here
$\beta_q = 1/\hbar_q = t_P(q)$ and the trace is taken in
the adjoint representation of $A$.

**Frobenius structure of pressure.**
In the classical kinetic derivation, pressure arises from
billiard-ball momentum transfer at the wall.  This assumes
(i) point particles, (ii) elastic reflection, and
(iii) a passive boundary.  All three fail in the QOU:

1. **Particles are knots**, not points — the configuration
   $K$ is a braid closure in the Reeb bundle
   $S^3 \to \mathcal{S}_p$
   ([Reeb bundle](#def:reeb-bundle)).
2. **The boundary participates** in the Hecke algebra.
   Momentum transfer at $\partial U$ is governed by the
   Frobenius pairing
   ([Frobenius pairing](#def:frobenius-pairing)):
   a morphism $K$ approaching $\partial U$ pairs with the
   boundary datum via
   $\langle K|_{\partial U}\,,\, \partial U \rangle_A$,
   producing a scalar in $\mathrm{End}_{\mathbf{C}}(\mathbf{1})$.
3. **The $q$-anomaly** from $d_q^2 \neq 0$ means the
   momentum transfer is not elastic.  Each interaction
   with the boundary shifts the action by
   $\delta S_q \propto \hbar_q^2$, contributing a
   quantum correction to pressure.

The pressure decomposes as

$$
  P_q \;=\; P_q^{(\mathrm{bulk})}
  \;+\; P_q^{(\mathrm{boundary})},
$$

where the bulk term comes from the volume derivative of
$\ln Z_q$ at fixed boundary conditions, and the boundary
term arises from the $q$-anomaly:

$$
  P_q^{(\mathrm{boundary})}
  \;=\; \frac{\hbar_q^2}{V_q}
  \,\mathrm{tr}_{\mathrm{Ad}}
  \!\oint_{\partial U}
  \langle d_q K \,,\, d_q K \rangle_A.
$$

This boundary pressure has no classical analogue.  It
vanishes as $q \to 1$ ($\hbar_q \to 0$) and is responsible
for quantum corrections to the ideal gas law.

**Operational meaning.**
The quantum pressure measures the rate at which the
partition function changes under dilation of $U$.
Expanding $U$ by $\delta V_q$ admits new knot
configurations into $\mathrm{Conf}(U)$ — specifically,
longer braids become available as the Reeb bundle has
more room.  The pressure is the information cost (in
units of $T_q$) per unit volume of these additional
configurations.
