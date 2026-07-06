*Proof sketch.*

Part (1): The topological mass formula $\mathfrak{m} = V/\hbar_q^2$ with $V_B = 7.32772$ yields the Borromean mass. The diquark mass calculation uses $\mathrm{Vol}(\mathcal{L}_H) = 0$.

Part (2): The crossing energy formula gives the binding energies. In the Borromean phase, the binding is topological, originating from the hyperbolic volume of the complement. In the diquark phase, the binding arises from the $R$-matrix braiding of the Hopf link ($2$ crossings per diquark pair, $3$ pairs per $6$-quark unit).

Part (3): Direct evaluation at $q = q_0$.

Part (4): The compression energy is the standard Fermi gas kinetic energy utilizing the $q$-deformed Planck constant $\hbar_q = (q-1)/q$. The Borromean volume $V_B$ enters the mass denominator of the kinetic energy, thereby creating a volume-dependent feedback. The diquark phase contributes zero volume, rendering its kinetic energy independent of $V_B$. $\square$

## Lean formalization

The companion Lean `borromean_hopf_energy_crossover` states the crossover and defers its proof via `sorry` (`-- Ref: [manuscript]`).
