The substrate parameter $q \colon M \to k^\times$ ([substrate parameter](#def:substrate-parameter)) is a field, not a background constant. A hadron ([hadron](#def:hadron)) is a multi-component knot composite containing internal Hopf junctions and crossings. It perturbs the local value of $q$ through its topological linking structure. The effective substrate parameter observed by a nucleus is:

$$
  q_{\mathrm{eff}}(p, n)
  = 
  q_0 +  \delta q(p, n).
$$

The background substrate value is $q_0$ ([local substrate $q$](#prop:local-substrate-q)). The hadron self-deformation is $\delta q(p, n)$.

**Proposition.**
Let $\mathcal{N}(Z, N) = Z\mathfrak{p} \oplus N\mathfrak{n}$ be a nucleus ([stable nucleus](#def:stable-nucleus)). The signed crossing excess determines the self-deformation of the substrate parameter. This excess is the imbalance between positive ($\mathfrak{p}$--$\mathfrak{p}$) and negative ($\mathfrak{n}$--$\mathfrak{n}$) Hopf crossings:

$$
  \delta q(p, n)
  = 
  \frac{\ell_{\mathrm{net}}(p, n)}{A^2}
  \cdot \hbar_q^2.
$$

The quantum Planck constant is $\hbar_q = 1 - q_0^{-1}$. The net signed crossing number is:

$$
  \ell_{\mathrm{net}}(p, n)
  = 
  \binom{p}{2} - \binom{n}{2}
  = 
  \frac{p(p-1) - n(n-1)}{2}.
$$

For neutron-rich nuclei ($n > p$), $\ell_{\mathrm{net}} < 0$ and the local $q$ drops. For proton-rich nuclei, $\ell_{\mathrm{net}} > 0$ and $q$ rises.

**Net signed crossing.**

The $q$-deformed wedge product $\wedge_q$ in the gauge sector of the canonical action ([canonical action](#prop:qou-canonical-action)) assigns weights to crossings:
- $q$ to $\mathfrak{p}$--$\mathfrak{p}$ crossings (positive).
- $q^{-1}$ to $\mathfrak{n}$--$\mathfrak{n}$ crossings (negative).
- $(q + q^{-1})/2$ to $\mathfrak{p}$--$\mathfrak{n}$ crossings (neutral average).

Neutral crossings contribute symmetrically and produce no shift in $q$. The imbalance between positive and negative crossings generates the substrate field deformation. The $A^2$ normalization reflects linking density. Crossings occupy a volume proportional to $A$, making the crossing density per unit volume $\ell_{\mathrm{net}} / A^2$.

**Magnitude.**

We evaluate at the background substrate $q_0$. We find $\hbar_q \approx 0.0991$ and $\hbar_q^2 \approx 0.00982$. For representative nuclei:

See [Table](#tbl:hadron-q-self-correction-table-data).

The self-deformation is small. We observe $|\delta q / q_0| < 0.1\%$ for all nuclei.

**Effect on beta decay: the differential shift.**

In beta decay, $A$ remains fixed while $(p, n)$ shifts by $(+1, -1)$. The daughter nucleus exhibits a different self-deformation from the parent. The change in effective $q$ across the decay is:

$$
  \Delta q_{\mathrm{eff}}
  = 
  \delta q(p+1, n-1) - \delta q(p, n)
  = 
  \frac{A - 1}{A^2} \cdot \hbar_q^2.
$$

This shift is strictly positive. The daughter acquires one more proton and thus more positive crossings. This yields a higher effective $q$. A higher $q$ increases the crossing asymmetry. This results in a larger $Q$-value ([transition energy](#def:Q-value-transition)) than predicted by the background alone. The Sargent rule $f(Q) \propto Q^5$ applies. The enlarged $Q$-value increases the decay rate and shortens the half-life.

The shift $\Delta q_{\mathrm{eff}}$ is exactly the $q$-anomaly $\delta_q$ of the transition energy. We evaluate the daughter at the shifted $q + \Delta q_{\mathrm{eff}}$, not the background $q$. This embodies $q$-deformed energy balance, overriding classical conservation.

**Effect on the decay rate.**

The differential shift $\Delta q_{\mathrm{eff}}$ modifies the effective substrate parameter at the converting nucleon. The decay rate depends on $q$ with sensitivity $\approx 48$ ([half-life regimes](#rem:hadron-half-life-regimes)). A shift of $\Delta q / q_0 \sim 0.1$--$0.4\%$ induces a measurable change in the decay rate.

For ${}^{3}\mathrm{H}$ ($A = 3$), the shift $\Delta q_{\mathrm{eff}} = (2/9) \times \hbar_q^2 \approx 0.00218$ is the maximum correction. This categorical quantity derives directly from $q$, $A$, and the linking structure of the nuclear braid.

**Universality.**

The self-deformation applies whenever $q$ acts on a specific hadron configuration. This extends beyond half-lives. The beta-stability line ([beta-stability](#prop:beta-stability)) and the topological mass formula receive identical structural corrections when $q_{\mathrm{eff}}$ replaces $q_0$.
