The three $q$-deformed kinematic quantities — $q$-momentum ([q-momentum](#def:q-momentum)), $q$-angular momentum ([q-angular momentum](#def:q-angular-momentum)), and $q$-energy ([q-energy](#def:q-energy)) — form a **$q$-deformed Noether dictionary**. Each arises from a symmetry of the categorical action $\mathfrak{S}_q$ ([categorical action](#def:categorical-action)) through the variational equations ([variational equations](#prop:variational-equations)), strictly analogous to Noether's theorem.

| Symmetry | Generator | Conserved quantity ($q = 1$) | $q$-Deformed quantity | Source |
|----------|-----------|-------|---------|--------|
| Time translation | Reeb flow $\xi_R$ | Energy $E$ | $\mathfrak{E}_q(K)$ | Categorical action $\mathfrak{S}_q$ |
| Spatial translation | Braid stabilisation | Momentum $p$ | $p_q(\beta)$ (writhe) | Markov II shift |
| Rotation | $\mathrm{SU}(2)$ action | Angular momentum $J^2$ | $J_q^2 = [j]_q[j+1]_q$ | $\mathrm{SU}_q(2)$ Casimir |
| Gauge | Quantum gauge group $G_q$ | Charge | Coulomb charge $Q(K)$ | Tannaka–Krein reconstruction |

**Classical limit.** At $q = 1$, the $q$-deformations collapse. We have $\hbar_q \to 0$ and $[n]_q \to n$, and each $q$-quantity reduces to its classical counterpart. Noether's theorem holds exactly. The variational equations yield the standard Einstein, Yang–Mills, and Dirac equations.

**$q$-Anomaly.** At $q \neq 1$, the correspondence deforms rather than breaks. The key mechanism is $d_q^2 \neq 0$ ([non-vanishing of $d_q^2$](#prop:categorical-dq-squared)). The $q$-differential does not square to zero, so the classical chain of "symmetry $\Rightarrow$ closed current $\Rightarrow$ conserved charge" acquires a correction term at each step. Concretely:

1. **Energy** is not naively conserved in transitions. The $Q$-value of a nuclear decay differs from the sum of product kinetic energies by a $q$-anomaly $\delta_q \propto \hbar_q^2$ ([q-value transition](#def:Q-value-transition)). The "missing" energy is absorbed by a shift in the effective substrate parameter. The conserved quantity is the full categorical action evaluated at the shifted $q$.

2. **Momentum** acquires an anomalous correction $\delta p_q \propto \hbar_q$ from the non-commutativity of the Iwahori--Hecke algebra.

3. **Angular momentum** remains exactly conserved because the $\mathrm{SU}_q(2)$ Casimir commutes with the coproduct. However, its eigenvalues are $q$-deformed: $[j]_q[j+1]_q \neq j(j+1)$.

Noether's theorem survives the $q$-deformation. The conserved quantities are categorical: they live in the Hecke algebra $H_n(R, q)$, not in classical phase space. The archimedean numerical values obtained by applying the fibre functor $\tau$ carry $q$-corrections. These are measurable as anomalies in precision experiments.
