**Setup.** Consider a monatomic hydrogen gas comprising $N$ atoms of $\mathcal{A}(1,0)$ at quantum temperature $T_q = \hbar_q$ in a region $U$ with quantum volume $V_q$. Each hydrogen atom combines a proton (Borromean link $\mathcal{B}_3$ with Hopf binding $\mathcal{L}_H$) and an electron (trefoil $T_{2,3}$). One treats the atom as a single composite knot $K_H = \mathcal{A}(1,0)$. This supplies the simplest non-trivial gas. Hydrogen possesses the lightest knot structure and fewest internal degrees of freedom.

**Single-atom partition function.** The atom $K_H$ resides in an $S^3$ fibre. Its internal degrees of freedom dictate the partition function:

1. **Translational**: the brane point $p \in U$ where the atom sits, yielding a factor of $|U|$.
2. **Rotational**: the $\mathrm{SU}_q(2)$ orientation of the Borromean link within the fibre. The $q$-angular momentum eigenvalues are $J_q^2 = [j]_q [j+1]_q$. The rotational partition function is
$$
  z_q^{(\mathrm{rot})} = \sum_{j=0}^{j_{\max}} [2j+1]_q e^{-\beta_q \, [j]_q [j+1]_q \, \hbar_q}.
$$
3. **Vibrational**: the writhe of the braid closure governing $q$-momentum $p_q(\beta)$. The amphichiral Borromean link exhibits writhe $w(\mathcal{B}_3) = 0$. The translational kinetic contribution vanishes identically at lowest order.
4. **Internal (action)**: the categorical action $\mathfrak{S}_q(K_H) = \mathrm{tr}_\tau(\rho(\beta_H))$. This supplies the rest-mass contribution.

The single-atom partition function evaluates to:
$$
  z_q = e^{-\beta_q \, \mathfrak{S}_q(K_H)} \cdot z_q^{(\mathrm{rot})} \cdot z_q^{(\mathrm{vib})},
$$
where $z_q^{(\mathrm{vib})} = 1 + O(\hbar_q^2)$. The vanishing writhe suppresses the leading vibrational mode.

**$N$-atom gas.** The quantum ideal gas law governs the macro-state:
$$
  P_q \, V_q = N \, \hbar_q \left( 1 + \frac{\hbar_q^2}{[2]_q} \,\mathfrak{S}_q(K_H) \right).
$$
The correction term $\hbar_q^2 \, \mathfrak{S}_q(K_H) / [2]_q$ measures the ratio of the $q$-anomaly energy to the fibre volume. For a hypothetical unknot gas, this correction vanishes, reproducing the exact leading-order law $P_q V_q = N \hbar_q$.

**Simplicity of hydrogen.** Among all atoms $\mathcal{A}(Z, N)$:
- Hydrogen possesses the simplest knot: one Borromean link paired with one trefoil, yielding composite crossing number $n_K = 13$.
- The amphichiral Borromean link ($w = 0$) zeroes the leading-order momentum contribution.
- The proton mass dominates. The term $\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2$ accounts for $\sim 99.95\%$ of the atomic mass. The electron trefoil $T_{2,3}$ acts as a torus knot with $\mathrm{Vol}(T_{2,3}) = 0$, contributing zero hyperbolic volume. Its mass arises entirely from vacuum drag.

**Heat capacity.** The constant-volume heat capacity emerges from $C_V = -\beta_q^2 (\partial^2 \ln Z_q / \partial \beta_q^2)$. At low temperature, only the $j = 0$ rotational mode populates, sending $C_V \to 0$. At high temperature, all rotational modes contribute, driving $C_V \to \frac{3}{2} N \hbar_q$. This recovers the classical equipartition result $C_V = \frac{3}{2} N k_B$ for three rotational degrees of freedom. The crossover occurs at the rotational temperature $T_q^{(\mathrm{rot})} = [1]_q [2]_q \, \hbar_q^2$.
