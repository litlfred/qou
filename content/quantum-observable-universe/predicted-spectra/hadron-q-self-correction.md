*Lean sibling: archimedean specialisation over $\mathbb{R}$ (CLAUDE.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The substrate parameter is a *field* $q \colon M \to k^\times$
([substrate parameter](#def:substrate-parameter)), not a background
constant.  A hadron ([hadron](#def:hadron)) — a multi-component
knot composite with internal Hopf junctions and crossings —
contributes to the local value of $q$ through its own topological
linking structure.  The effective substrate parameter seen by a
nucleus is therefore

$$
  q_{\mathrm{eff}}(p, n)
  = 
  q_0 +  \delta q(p, n)
$$

where the substrate $q_0$ is the background value
([local substrate $q$](#prop:local-substrate-q)) and
$\delta q(p, n)$ is the hadron's self-deformation.

**Proposition.**
Let $\mathcal{N}(Z, N) = Z\mathfrak{p} \oplus N\mathfrak{n}$
be a nucleus ([stable nucleus](#def:stable-nucleus)).  The
self-deformation of the substrate parameter is determined by the
*signed* crossing excess — the imbalance between positive
($\mathfrak{p}$--$\mathfrak{p}$) and negative
($\mathfrak{n}$--$\mathfrak{n}$) Hopf crossings:

$$
  \delta q(p, n)
  = 
  \frac{\ell_{\mathrm{net}}(p, n)}{A^2}
  \cdot \hbar_q^2
$$

where $\hbar_q = 1 - q_0^{-1}$ is the quantum Planck constant and
the net signed crossing number is

$$
  \ell_{\mathrm{net}}(p, n)
  = 
  \binom{p}{2} - \binom{n}{2}
  = 
  \frac{p(p-1) - n(n-1)}{2}.
$$

For nuclei on the neutron-rich side of the valley ($n > p$),
$\ell_{\mathrm{net}} < 0$ and the local $q$ is slightly *reduced*.
For proton-rich nuclei, $\ell_{\mathrm{net}} > 0$ and $q$ is
slightly increased.

**Why the net signed crossing.**
The $q$-deformed wedge product $\wedge_q$ in the gauge sector of the
canonical action
([canonical action](#prop:qou-canonical-action))
assigns:
- weight $q$ to $\mathfrak{p}$--$\mathfrak{p}$ crossings (positive),
- weight $q^{-1}$ to $\mathfrak{n}$--$\mathfrak{n}$ crossings
  (negative),
- weight $(q + q^{-1})/2$ to $\mathfrak{p}$--$\mathfrak{n}$ crossings
  (neutral average).

The neutral crossings contribute symmetrically and do not shift $q$.
Only the imbalance between positive and negative crossings
deforms the substrate field.  The normalization by $A^2$ (rather
than $A$) reflects the linking *density*: the crossings occupy a
volume $\propto A$, so the crossing density per unit volume is
$\ell_{\mathrm{net}} / A^2$.

**Magnitude.**
At the substrate $q_0$: $\hbar_q \approx 0.0991$ and
$\hbar_q^2 \approx 0.00982$.  For representative nuclei:

See [Table](#tbl:hadron-q-self-correction-table-data).

The self-deformation is genuinely small ($|\delta q / q_0| < 0.1\%$
for all nuclei).

**Effect on beta decay: the differential shift.**
In beta decay, $A$ is fixed but $(p, n)$ changes by $(+1, -1)$.
The *daughter* nucleus has a different self-deformation from the
parent.  The change in effective $q$ across the decay is

$$
  \Delta q_{\mathrm{eff}}
  = 
  \delta q(p+1, n-1) - \delta q(p, n)
  = 
  \frac{A - 1}{A^2} \cdot \hbar_q^2.
$$

This is always positive: the daughter (with one more proton) has
more positive crossings, hence a higher effective $q$.  A higher
$q$ means a larger crossing asymmetry and therefore a larger
$Q$-value
([transition energy](#def:Q-value-transition)) than the
background calculation predicts.  Via the Sargent rule
$f(Q) \propto Q^5$, the corrected
$Q$ increases the decay rate and *shortens* the
half-life.

**Note:** The $\Delta q_{\mathrm{eff}}$ shift is precisely the
$q$-anomaly $\delta_q$ of the transition energy.  The daughter
is evaluated at the shifted $q + \Delta q_{\mathrm{eff}}$, not
the background $q$.  This is the $q$-deformed energy balance
— not classical conservation.

**Effect on the decay rate.**
The differential shift $\Delta q_{\mathrm{eff}}$ modifies the
effective substrate parameter at the converting nucleon.  Since
the decay rate depends on $q$ with sensitivity $\approx 48$
([half-life regimes](#rem:hadron-half-life-regimes)), a shift
of $\Delta q / q_0 \sim 0.1$--$0.4\%$ produces a measurable
change in the decay rate.

For ${}^{3}\mathrm{H}$ ($A = 3$): $\Delta q_{\mathrm{eff}} = (2/9) \times \hbar_q^2 = 0.00218$, the largest correction.  This
is a categorical quantity: it follows from $q$, $A$, and the
linking structure of the nuclear braid.

**Universality.**
The self-deformation applies to *every* equation where $q$ is
evaluated on a specific hadron configuration — not just half-lives.
The beta-stability line
([beta-stability](#prop:beta-stability)) and the topological mass
formula all receive analogous corrections when $q_0$ is replaced by
$q_{\mathrm{eff}}$.

**Formalization Goal Plausibility.** The intended Lean theorems (establishing `deltaQ <= 0` for neutron-rich nuclei, `differentialShift >= 0`, and `qEff > 1`) contain mathematically sound proof bodies relying on basic arithmetic, `omega`, and `positivity` tactics. Currently, the Lean file structure is technically broken because the theorem headers were commented out (due to their Archimedean/real-number nature not matching the generic `R_q` Laurent polynomial ring). However, closing this gap is highly plausible: it only requires separating the generic definitions from the Archimedean instantiations (e.g., via a ring homomorphism to $\mathbb{R}$) and restoring the theorem headers over the reals. The underlying inequalities are elementary, and the formalization gap is purely structural.

**Remark on Mathematical Novelty:** Although the C(p,2)-C(n,2) signed-crossing excess is a natural back-reaction mechanism, framing it as a topological self-deformation of the substrate field by nuclear linking density (l_net/A^2) provides a genuinely novel geometric formalization of nuclear self-correction dynamics.
