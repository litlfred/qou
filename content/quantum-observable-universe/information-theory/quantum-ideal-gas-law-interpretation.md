**Noether invariant.**
The quantum ideal gas law is the Ward identity of a scale symmetry of the partition function. Under the $q$-deformed Noether dictionary ([Noether theorem](#rem:noether-theorem-callout)), the conserved quantity under simultaneous rescaling of $V_q$ and $\beta_q$ is the quantum free energy $F_q$.

We define the thermodynamic Noether current:

$$
  \mathcal{J}_q^{\mathrm{thermo}}
  \;:=\;
  V_q \,\frac{\partial}{\partial V_q}
  \;+\;
  \beta_q \,\frac{\partial}{\partial \beta_q}.
$$

The identity $\mathcal{J}_q^{\mathrm{thermo}}(\ln Z_q) = 0$ holds at the equation-of-state surface. The quantum ideal gas law $P_q V_q = N T_q (1 + \cdots)$ is exactly the content of this vanishing. It acts as the analogue of the classical Euler relation $E = TS - PV + \mu N$.

**Comparison with the classical derivation.**

See [Table](#tbl:quantum-ideal-gas-law-interpretation-table-data).

**Classical limit.**
As $q \to 1$, $T_q = \hbar_q \to 0$. However, $N T_q = N \hbar_q$ remains finite in physical units via $k_B$. The correction vanishes as $\hbar_q^2 \to 0$. We recover the classical ideal gas law $PV = Nk_BT$.
