The Boltzmann constant and gas constant are derived from
the substrate parameter $q$, not postulated.

**Boltzmann constant.**
In the quantum ideal gas law
([quantum ideal gas law](#prop:quantum-ideal-gas-law)),
the equation of state at leading order is
$P_q V_q = N T_q = N \hbar_q$.  Comparing with the
classical form $PV = N k_B T$, the Boltzmann constant is

$$
  k_B \;=\; \hbar_q \;=\; \frac{q - 1}{q}.
$$

This is not a redefinition — it is the structural
identification: the Boltzmann constant is the quantum
Planck constant
([quantum Planck constant](#def:quantum-planck-constant)).
Both measure the same quantity from different directions:
$\hbar_q$ measures the discreteness of the Reeb dynamics
(one tick = one $\hbar_q$ of action), while $k_B$ measures
the conversion between energy and temperature.  In the QOU,
temperature *is* the tick rate
([quantum temperature](#def:quantum-temperature)),
so these coincide.

**Derivation from the partition function.**
The identification $k_B = \hbar_q$ follows from the
canonical ensemble.  The Boltzmann distribution over knot
configurations is

$$
  \rho(K) \;=\; \frac{1}{Z_q}\,
  e^{-\beta_q \, S_q(K)},
$$

where $\beta_q = 1/\hbar_q = t_P(q) = q/(q-1)$ is the
inverse temperature (= Planck time = number of Reeb
operations per macroscopic time unit).  The classical
relation $\beta = 1/(k_B T)$ then gives

$$
  k_B \;=\; \frac{1}{\beta_q \, T_q}
  \;=\; \frac{\hbar_q}{1}
  \;=\; \hbar_q,
$$

since $T_q = \hbar_q$ and $\beta_q = 1/\hbar_q$.

**Gas constant.**
The gas constant relates the equation of state to molar
quantities.  A **categorical mole** is $N_A(q)$ particles,
where

$$
  N_A(q) \;=\;
  \frac{12}{\mathfrak{m}_{C\text{-}12}(q)},
$$

and $\mathfrak{m}_{C\text{-}12}(q)$ is the categorical mass
of Carbon-12 in QOU natural units.  From the topological
mass formula, the Carbon-12 mass is

$$
  \mathfrak{m}_{C\text{-}12}(q)
  \;=\;
  \frac{
    6\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\bigl(\mathrm{Vol}(\mathcal{B}_3) + \delta_{\mathfrak{n}}\bigr)
    - B_{12}(q)
  }{\hbar_q^2}
  \;=\;
  \frac{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }{\hbar_q^2},
$$

where:
- $\mathrm{Vol}(\mathcal{B}_3) = 7.32772\ldots$ is the
  hyperbolic volume of the Borromean complement (a
  topological constant),
- $\delta_{\mathfrak{n}}$ is the neutron--proton Skein mass
  difference (from the crossing asymmetry of the
  $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ vs.
  $[\mathfrak{u}, \mathfrak{u}, \mathfrak{d}]$ color-tube
  linking),
- $B_{12}(q)$ is the nuclear binding energy of the
  12-nucleon Hopf link composite, computed from the Skein
  polynomial of the $\binom{12}{2} = 66$ crossing pairs.

The gas constant is then

$$
  R_q
  \;=\; N_A(q) \cdot k_B
  \;=\; \frac{12\,\hbar_q}{
    \mathfrak{m}_{C\text{-}12}(q)
  }
  \;=\;
  \frac{12\,\hbar_q^3}{
    12\,\mathrm{Vol}(\mathcal{B}_3)
    + 6\,\delta_{\mathfrak{n}}
    - B_{12}(q)
  }.
$$

**Simplification.**
The binding energy $B_{12}(q)$ and neutron mass difference
$\delta_{\mathfrak{n}}$ are small corrections.  At leading
order in $\mathrm{Vol}(\mathcal{B}_3)$:

$$
  R_q
  \;\approx\;
  \frac{\hbar_q^3}{\mathrm{Vol}(\mathcal{B}_3)}
  \;=\;
  \frac{(q-1)^3}{q^3 \cdot \mathrm{Vol}(\mathcal{B}_3)}.
$$

**Inputs.**
The gas constant depends on exactly two quantities:
1. $q$ — the substrate parameter (algebraic), and
2. $\mathrm{Vol}(\mathcal{B}_3)$ — the Borromean volume
   (topological).

No empirical measurements enter.  Both are mathematical
constants: $q$ is determined by the Frobenius--Hopf
structure, and $\mathrm{Vol}(\mathcal{B}_3)$ is a
hyperbolic invariant computable to arbitrary precision
by SnapPy.

**Dictionary.**

| Classical constant | QOU expression | Depends on |
|--------------------|----------------|------------|
| $k_B$ | $\hbar_q = (q-1)/q$ | $q$ only |
| $N_A$ | $12\,\hbar_q^2 / (12\,\mathrm{Vol}(\mathcal{B}_3) + 6\delta_{\mathfrak{n}} - B_{12})$ | $q$, $\mathrm{Vol}(\mathcal{B}_3)$, Skein data |
| $R = N_A k_B$ | $12\,\hbar_q^3 / (12\,\mathrm{Vol}(\mathcal{B}_3) + 6\delta_{\mathfrak{n}} - B_{12})$ | $q$, $\mathrm{Vol}(\mathcal{B}_3)$, Skein data |
| $c$ | $c_q = 1/(q-1)$ | $q$ only |
| $\hbar$ | $\hbar_q = (q-1)/q$ | $q$ only |
| $G$ | $c_q^3 \hbar_q / S_{\mathrm{cell}}$ | $q$ only |

The first three constants of nature ($c$, $\hbar$, $G$)
depend on $q$ alone.  The thermodynamic constants
($k_B$, $R$) additionally require the Borromean
topological invariant $\mathrm{Vol}(\mathcal{B}_3)$,
because they connect the substrate geometry to the
mass scale of baryonic matter.

**Classical limit.**
As $q \to 1$: $\hbar_q \to 0$, so $k_B \to 0$ and
$R_q \to 0$.  This reflects the divergence
$\beta_q \to \infty$: in the classical limit,
temperature becomes infinitely fine-grained (continuous),
and the quantum of thermal energy $k_B T$ vanishes.
Physical $k_B$ remains finite in SI because the SI
kelvin is calibrated to the quantum regime at $q = q_0$.
