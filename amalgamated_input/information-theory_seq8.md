<!-- FILE_START: stat-mech-intro.md -->
The statistical mechanical structure of the QOU acts not as an analogy, but as the exact mechanism by which continuous physics emerges from discrete Reeb dynamics. The Planck time $t_P(q) = q/(q-1)$ ([Planck time](#def:planck-time)) functions strictly as the inverse temperature $\beta$. It counts the precise number of microscopic operations (Julia set iterations on the exceptional divisor) comprising each macroscopic time unit.

The thermodynamic limit $\beta \to \infty$ ($q \to 1$) coincides identically with the classical limit. Infinitely many discrete operations seamlessly average into smooth Reeb flow, precisely as infinitely many molecular collisions average into thermodynamic equilibrium. The subsequent corrections to the continuous approximation are $O(1/\beta) = O(\hbar_q)$. Consequently, quantum-gravitational effects stand literally as finite-size corrections to the thermodynamic limit of time.

This section derives the partition function, entropy, and free energy of the Reeb dynamics. These quantities firmly establish the statistical mechanical framework underlying information-theoretic time ([information-theoretic time](#def:information-theoretic-time)).
<!-- FILE_END: stat-mech-intro.md -->

<!-- FILE_START: quantum-temperature.md -->
> **SUPERSEDED-$\rho_q$ note .** Any use of the
> scalar substrate density $\rho_q = 1/\hbar_q^2$ in this block is the
> structurally-wrong leading-order ansatz per
> [`mass-endomorphism-tower.md` §SUPERSEDED](../braids-and-knots/mass-endomorphism-tower.md);
> the canonical replacement is the operator-valued $A^\lambda_{\mu, \nu}(I)$
> graded expansion [`prop:rho-k-graded-expansion`](../braids-and-knots/rho-k-graded-expansion.md).
> Full purge tracking: [`docs/audits/-superseded-rho-q-purge.md`](../../../docs/audits/-superseded-rho-q-purge.md).

Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$ and Planck time $t_P(q) = q/(q-1) = 1/\hbar_q$ ([Planck time](#def:planck-time)). The **quantum temperature** of a region $U \subset M$ is defined as

$$
  T_q(U) \;:=\; \hbar_q \;=\; \frac{q - 1}{q}.
$$

The inverse temperature is $\beta_q := 1/T_q = t_P(q)$.

The Kashaev volume--density reading ([Kashaev volume--density](#rem:kashaev-volume-density)) introduces the substrate density $\rho_q = 1/\hbar_q^{2}$. In these terms, the temperature and its inverse square are

$$
  T_q \;=\; \rho_q^{-1/2},
  \qquad
  \beta_q^{2} \;=\; \rho_q.
$$

Temperature and substrate density are conjugate square roots. A state at high drag density (small $\hbar_q$) rests at low temperature, while the inverse-temperature squared matches the density itself. This relationship absorbs several dimensional-analysis identities that would otherwise demand independent derivations.

The quantum temperature is the thermodynamic conjugate of the quantum entropy $S_q(U)$ ([quantum entropy](#def:quantum-entropy)):

$$
  \frac{1}{T_q}
  \;=\; \frac{\partial S_q}{\partial \mathfrak{E}_q}\bigg|_V
  \;=\; \frac{1}{\hbar_q}.
$$
<!-- FILE_END: quantum-temperature.md -->

<!-- FILE_START: quantum-entropy.md -->
**Definition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with substrate parameter $q$, and let $U \subset M$ be a region. The **quantum entropy** of $U$ is the non-abelian surface integral

$$
  S_q(U) \;:=\; -\,\mathrm{tr}_{\mathrm{Ad}}
  \!\oint_{\partial U}
  \omega_{\mathcal{F}} \,\wedge\, *\eta_q.
$$

Here $\mathcal{F} = \mathrm{Ad}(A)$ is the adjoint bundle, $\omega_{\mathcal{F}}$ is the adjoint connection, and $\eta_q = (2q-1)/q^3$ is the operational entropy density ([operational entropy](#def:operational-entropy)). The operator $*$ is the Hodge star on $\partial U$.

The measurability conditions $c_1(\mathcal{F}) = 0$ and $c_2(\mathcal{F}) = 0$ ([quantum observable universe](#def:quantum-observable-universe)) ensure that the surface integral is independent of the choice of bounding surface via the Yekutieli non-abelian Stokes theorem ([Yekutieli triple](#def:yekutieli-triple)).
<!-- FILE_END: quantum-entropy.md -->

<!-- FILE_START: quantum-temperature-interpretation.md -->
Classical statistical mechanics defines temperature implicitly through the Boltzmann distribution $\rho \propto e^{-\beta H}$. Here $\beta = 1/(k_B T)$ is a Lagrange multiplier enforcing energy conservation. In the QOU, $\beta_q$ holds direct operational meaning. It is the number of discrete Reeb operations (Julia set iterations $f_q$ on the exceptional divisor) that compose one macroscopic time unit. Temperature is not a statistical average over kinetic energies. It is the tick rate of the quantum substrate.

**Surface character of temperature.**
The entropy $S_q(U)$ is defined as a surface integral over $\partial U$, rather than a bulk integral over $U$. This structure follows from two ingredients.

First, the non-abelian Stokes theorem ([Yekutieli triple](#def:yekutieli-triple)) converts the bulk curvature integral to a boundary holonomy. The flatness conditions ($c_1 = 0$, $c_2 = 0$) render the boundary integral independent of the choice of bounding surface. The entropy is entirely a boundary datum.

Second, the Frobenius pairing ([Frobenius pairing](#def:frobenius-pairing)) is non-degenerate. Internal degrees of freedom are fully determined by boundary data via the categorical trace. This encodes the content-object version of the holographic principle. The boundary $\partial U$—not the bulk $U$—controls the number of distinguishable states in $U$.

Temperature is the derivative of entropy with respect to energy. It strictly inherits this boundary character.

**Classical limit.**
As $q \to 1$, we find $T_q \to 0$, $\beta_q \to \infty$, and $S_q(U) \to S_{\mathrm{classical}}(U)$. The non-abelian Stokes integral degenerates to the classical Gauss law. The Frobenius trace becomes the ordinary matrix trace. The Boltzmann constant emerges as $k_B = \hbar_q / T_{\mathrm{phys}}$ in the correspondence limit, where physical temperature $T_{\mathrm{phys}}$ is measured in SI units.
<!-- FILE_END: quantum-temperature-interpretation.md -->

<!-- FILE_START: quantum-pressure.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with quantum temperature $T_q = \hbar_q$ ([quantum temperature](#def:quantum-temperature)). Let $U \subset M$ be a region of the brane with boundary $\partial U$. Let $\mathfrak{S}_q(K)$ denote the categorical action of a knot configuration $K$ in $U$ ([categorical action](#def:categorical-action)). 

The **quantum pressure** on $\partial U$ is defined as

$$
  P_q(U) \;:=\;
  -\,\frac{\partial F_q}{\partial V_q}\bigg|_{T_q}.
$$

Here $F_q = -T_q \ln Z_q$ is the quantum free energy and

$$
  Z_q(U) \;=\;
  \mathrm{tr}_{\mathrm{Ad}}
  \!\sum_{K \,\in\, \mathrm{Conf}(U)}
  e^{-\beta_q \, \mathfrak{S}_q(K)}
$$

is the partition function over the configuration space $\mathrm{Conf}(U)$ of knot states in $U$, taking $\beta_q = 1/\hbar_q = t_P(q)$.

The pressure decomposes into bulk and boundary components:

$$
  P_q \;=\; P_q^{(\mathrm{bulk})}
  \;+\; P_q^{(\mathrm{boundary})}.
$$

The bulk term is the volume derivative of $\ln Z_q$ at fixed boundary conditions. The boundary term arises from the $q$-anomaly ($d_q^2 \neq 0$) at $\partial U$:

$$
  P_q^{(\mathrm{boundary})}
  \;=\; \frac{\hbar_q^2}{V_q}
  \,\mathrm{tr}_{\mathrm{Ad}}
  \!\oint_{\partial U}
  \langle d_q K \,,\, d_q K \rangle_A.
$$

The pairing $\langle\,\cdot\,,\,\cdot\,\rangle_A$ is the Frobenius pairing ([Frobenius pairing](#def:frobenius-pairing)).

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall: it invokes real- or complex-analytic constructs — real-valued physical observables, real-analytic bounds, transcendental constants, or numerical evaluation at the substrate parameter $q_0$. Any generic categorical / $q$-deformation identities it draws on remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: quantum-pressure.md -->

<!-- FILE_START: quantum-pressure-interpretation.md -->
Classical kinetic pressure arises from billiard-ball momentum transfer at a boundary. This derivation assumes point particles, elastic reflection, and a passive wall. All three assumptions fail in the QOU.

First, particles are knots, not points. The configuration $K$ is a braid closure in the Reeb bundle $S^3 \to \mathcal{S}_p$ ([Reeb bundle](#def:reeb-bundle)). 

Second, the boundary participates in the Hecke algebra. Momentum transfer at $\partial U$ is governed by the Frobenius pairing ([Frobenius pairing](#def:frobenius-pairing)). A morphism $K$ approaching $\partial U$ pairs with the boundary datum via $\langle K|_{\partial U}\,,\, \partial U \rangle_A$, yielding a scalar in $\mathrm{End}_{\mathbf{C}}(\mathbf{1})$.

Third, the $q$-anomaly from $d_q^2 \neq 0$ renders the momentum transfer inelastic. Each interaction with the boundary shifts the action by $\delta \mathfrak{S}_q \propto \hbar_q^2$. This shift contributes a direct quantum correction to the pressure. 

Consequently, the boundary pressure $P_q^{(\mathrm{boundary})}$ has no classical analogue. It vanishes as $q \to 1$ (when $\hbar_q \to 0$) and drives the quantum corrections to the ideal gas law. 

Operationally, quantum pressure measures the rate at which the partition function changes under dilation of $U$. Expanding $U$ by $\delta V_q$ admits new knot configurations into $\mathrm{Conf}(U)$. As the Reeb bundle gains volume, longer braids become available. The pressure quantifies the information cost, in units of $T_q$, per unit volume of these additional configurations.
<!-- FILE_END: quantum-pressure-interpretation.md -->

<!-- FILE_START: quantum-volume.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $\mathcal{S} \to M$ be the state bundle with Reeb bundle $S^3 \to \mathcal{S}_p$ at each brane point $p$ ([Reeb bundle](#def:reeb-bundle)). The **quantum volume** of a region $U \subset M$ is defined as

$$
  V_q(U) \;:=\;
  \int_U \mathrm{Vol}_{S^3}(\mathcal{S}_p)\;
  \epsilon_q(p).
$$

Here $\epsilon_q$ is the categorical volume form on $\Lambda^2 V$, uniquely preserved by the rigid duality of $(\mathbf{C}, A, \tau)$ ([quantum observable universe](#def:quantum-observable-universe)).

For a homogeneous gas exhibiting uniform $q$ throughout $U$, all fibres are isometric. This yields

$$
  V_q(U) \;=\;
  |U| \cdot \mathrm{Vol}(S^3_q),
$$

where $|U|$ is the number of brane points in $U$. The term

$$
  \mathrm{Vol}(S^3_q)
  \;=\; \pi^2 \cdot [2]_q
  \;=\; \pi^2(q + q^{-1})
$$

is the volume of $S^3$ measured in the $q$-deformed metric. At $q = 1$, this trivially recovers the classical volume $\mathrm{Vol}(S^3) = 2\pi^2$.
<!-- FILE_END: quantum-volume.md -->

<!-- FILE_START: quantum-volume-interpretation.md -->
The quantum volume determines the configuration space $\mathrm{Conf}(U)$ available to particle knots. A knot $K$ with $n$ crossings demands a minimal $S^3$ volume, proportional to $n \cdot \hbar_q$, to embed within a fibre. The number of single-fibre configurations at a brane point $p$ is therefore

$$
  |\mathrm{Conf}_p|
  \;\sim\;
  \frac{\mathrm{Vol}(S^3_q)}{n_K \cdot \hbar_q},
$$

where $n_K$ is the crossing number of $K$. For a gas of $N$ hydrogen atoms, each modeled by the knot structure $\mathcal{A}(1,0)$ ([hydrogen knot structure](#ex:hydrogen-knot-structure)), the total configuration count scales as $|\mathrm{Conf}(U)| \sim |\mathrm{Conf}_p|^{|U|}$.

The $q$-deformation stretches or compresses the Hopf fibres of the $S^1 \hookrightarrow S^3 \to S^2$ fibration precisely according to the substrate parameter.

**Classical limit.**
As $q \to 1$, $[2]_q \to 2$. The fibre volume approaches $2\pi^2$. The quantum volume $V_q(U)$ reduces to the standard Riemannian volume of $U$ scaled by the classic $S^3$ volume. The categorical volume form $\epsilon_q$ degenerates smoothly to the standard Riemannian volume element.
<!-- FILE_END: quantum-volume-interpretation.md -->

<!-- FILE_START: quantum-ideal-gas-law.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe containing $N$ non-interacting particle knots in a region $U \subset M$. Let $P_q$, $V_q$, and $T_q$ denote the quantum pressure ([quantum pressure](#def:quantum-pressure)), quantum volume ([quantum volume](#def:quantum-volume)), and quantum temperature ([quantum temperature](#def:quantum-temperature)) of $U$. The equation of state is

$$
  P_q \, V_q
  \;=\; N \, T_q
  \left(
    1 \;+\; \frac{\hbar_q^2}{[2]_q}
    \,\langle \mathfrak{S}_q \rangle
  \right).
$$

Here $\langle \mathfrak{S}_q \rangle$ is the thermal expectation of the categorical action ([categorical action](#def:categorical-action)) and $[2]_q = q + q^{-1}$.
<!-- FILE_END: quantum-ideal-gas-law.md -->

<!-- FILE_START: quantum-ideal-gas-law-interpretation.md -->
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
<!-- FILE_END: quantum-ideal-gas-law-interpretation.md -->

<!-- FILE_START: boltzmann-constant.md -->
In natural QOU units, we set the Boltzmann constant to unity:

$$
  k_B \;=\; 1.
$$

The quantum Planck constant $\hbar_q$ replaces the classical thermal energy $k_B T_{\mathrm{phys}}$:

$$
  k_B \, T_{\mathrm{phys}} \;=\; \hbar_q \;=\; \frac{q-1}{q}.
$$
<!-- FILE_END: boltzmann-constant.md -->

<!-- FILE_START: gas-constant-derivation.md -->
We derive the gas constant $R_q = N_A(q) \cdot k_B$ from $q$ and the Borromean volume. A **categorical mole** consists of $N_A(q) = 12 / \mathfrak{m}_{C\text{-}12}(q)$ particles. The mass of Carbon-12 in QOU natural units is:

$$
  \mathfrak{m}_{C\text{-}12}(q)
  \;=\;
  \frac{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }{\hbar_q^2}.
$$

Here $\mathrm{Vol}(\mathcal{B}_3) = 7.32772\ldots$ is the Borromean volume, $\delta_{\mathfrak{n}}$ is the neutron--proton Skein mass difference, and $B_{12}(q)$ is the nuclear binding energy computed from the 66-crossing transfer matrix ([terminal resolution](#prop:terminal-resolution)).

The gas constant evaluates to:

$$
  R_q
  \;=\;
  \frac{12\,\hbar_q^3}{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }.
$$

At leading order, neglecting binding energy and neutron mass corrections, this simplifies to:

$$
  R_q
  \;\approx\;
  \frac{(q-1)^3}{q^3 \cdot \mathrm{Vol}(\mathcal{B}_3)}.
$$

The gas constant $R$ requires precisely two inputs: the algebraic parameter $q$ and the topological invariant $\mathrm{Vol}(\mathcal{B}_3)$. Because the mass predictions already match CODATA to sub-keV precision, $R$ is automatically correct. It is strictly downstream of the mass spectrum.

**Fundamental constants dictionary.**

| Constant | QOU expression | Depends on |
|----------|----------------|------------|
| $c$ | $1/(q-1)$ | $q$ only |
| $\hbar$ | $(q-1)/q$ | $q$ only |
| $G$ | $c_q^3 \hbar_q / S_{\mathrm{cell}}$ | $q$ only |
| $k_B$ | $1$ (natural units) | — |
| $R$ | $12\hbar_q^3 / (12\,\mathrm{Vol}(\mathcal{B}_3) + \cdots)$ | $q$, $\mathrm{Vol}(\mathcal{B}_3)$ |

The first four constants depend on $q$ alone. The gas constant $R$ additionally requires the Borromean topological invariant because it maps the substrate geometry to the baryonic mass scale.
<!-- FILE_END: gas-constant-derivation.md -->

<!-- FILE_START: hydrogen-partition-function.md -->
**Setup.**
Consider a monatomic hydrogen gas comprising $N$ atoms of $\mathcal{A}(1,0)$ ([hydrogen knot structure](#ex:hydrogen-knot-structure)) at quantum temperature $T_q = \hbar_q$ in a region $U$ with quantum volume $V_q$ ([quantum volume](#def:quantum-volume)). Each hydrogen atom unites a proton (Borromean link $\mathcal{B}_3$ with Hopf binding $\mathcal{L}_H$) and an electron (trefoil $T_{2,3}$). We treat the atom as a single composite knot $K_H = \mathcal{A}(1,0)$.

This provides the simplest non-trivial gas. Hydrogen possesses the lightest knot structure and the fewest internal degrees of freedom. We examine monatomic $H$ (plasma regime) rather than molecular $H_2$ to avoid inter-atomic bonding braids.

**Single-atom partition function.**
The atom $K_H$ resides in an $S^3$ fibre. Its internal degrees of freedom dictate the partition function:

1. **Translational**: the brane point $p \in U$ where the atom sits. This yields a factor of $|U|$ (the number of available brane points).

2. **Rotational**: the $\mathrm{SU}_q(2)$ orientation of the Borromean link within the fibre. The $q$-angular momentum eigenvalues are $J_q^2 = [j]_q [j+1]_q$ ([q-energy](#def:q-energy)). The rotational partition function is

$$
  z_q^{(\mathrm{rot})}
  =
  \sum_{j=0}^{j_{\max}}
  [2j+1]_q 
  e^{-\beta_q \, [j]_q [j+1]_q \, \hbar_q}.
$$

3. **Vibrational**: the writhe of the braid closure governing $q$-momentum $p_q(\beta)$. The amphichiral Borromean link exhibits writhe $w(\mathcal{B}_3) = 0$. The translational kinetic contribution vanishes at lowest order.

4. **Internal (action)**: the categorical action $\mathfrak{S}_q(K_H) = \mathrm{tr}_\tau(\rho(\beta_H))$, where $\beta_H$ is the braid representative of $K_H$. This provides the rest-mass contribution.

The single-atom partition function evaluates to:

$$
  z_q
  =
  e^{-\beta_q \, \mathfrak{S}_q(K_H)}
  \cdot z_q^{(\mathrm{rot})}
  \cdot z_q^{(\mathrm{vib})},
$$

where $z_q^{(\mathrm{vib})} = 1 + O(\hbar_q^2)$ for the amphichiral Borromean proton. The vanishing writhe suppresses the leading vibrational mode.

**$N$-atom gas.**
The quantum ideal gas law ([quantum ideal gas law](#prop:quantum-ideal-gas-law)) applies:

$$
  P_q \, V_q
  = N \, \hbar_q
  \left(
    1 +
    \frac{\hbar_q^2}{[2]_q}
    \,\mathfrak{S}_q(K_H)
  \right).
$$

The correction term $\hbar_q^2 \, \mathfrak{S}_q(K_H) / [2]_q$ measures the ratio of the $q$-anomaly energy (induced by the boundary interaction of hydrogen's non-trivial knot topology) to the fibre volume. For a gas of unknots (hypothetical structureless particles with $\mathfrak{S}_q = 0$), this correction vanishes, reproducing the exact leading-order law $P_q V_q = N \hbar_q$.

**Simplicity of hydrogen.**
Among all atoms $\mathcal{A}(Z, N)$:

- Hydrogen possesses the simplest knot: one Borromean link paired with one trefoil, yielding composite crossing number $n_K = 13$ ([crossing parity](#prop:composite-crossing-parity)).
- The amphichiral Borromean link ($w = 0$) zeroes the leading-order momentum contribution.
- The proton mass dominates. The term $\mathrm{Vol}(\mathcal{B}_3) / \hbar_q^2$ accounts for $\sim 99.95\%$ of the atomic mass. The electron trefoil $T_{2,3}$ acts as a torus knot with $\mathrm{Vol}(T_{2,3}) = 0$. It contributes zero hyperbolic volume. Its mass arises entirely from vacuum drag (Skein corrections).

**Heat capacity.**
The constant-volume heat capacity emerges from $C_V = -\beta_q^2 (\partial^2 \ln Z_q / \partial \beta_q^2)$. At high temperature ($\beta_q \to 0$, deep quantum regime), only the $j = 0$ rotational mode populates, sending $C_V \to 0$. At low temperature ($\beta_q \to \infty$, classical limit), all rotational modes contribute, taking $C_V \to \frac{3}{2} N \hbar_q$. This recovers the classical monatomic result $C_V = \frac{3}{2} N k_B$. The crossover follows the rotational temperature $T_q^{(\mathrm{rot})} = [1]_q [2]_q \, \hbar_q^2$, denoting the energy gap between $j = 0$ and $j = 1$.
<!-- FILE_END: hydrogen-partition-function.md -->

