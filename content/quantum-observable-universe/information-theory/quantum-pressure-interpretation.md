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
   $\delta \mathfrak{S}_q \propto \hbar_q^2$, contributing a
   quantum correction to pressure.

The boundary pressure $P_q^{(\mathrm{boundary})}$ has no
classical analogue.  It vanishes as $q \to 1$
($\hbar_q \to 0$) and is responsible for quantum
corrections to the ideal gas law.

**Operational meaning.**
The quantum pressure measures the rate at which the
partition function changes under dilation of $U$.
Expanding $U$ by $\delta V_q$ admits new knot
configurations into $\mathrm{Conf}(U)$ — specifically,
longer braids become available as the Reeb bundle has
more room.  The pressure is the information cost (in
units of $T_q$) per unit volume of these additional
configurations.
