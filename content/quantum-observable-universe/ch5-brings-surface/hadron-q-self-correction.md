The substrate parameter is a *field* $q \colon M \to k^\times$
([substrate parameter](#def:substrate-parameter)), not a background
constant.  A hadron ([hadron](#def:hadron)) — a multi-component
knot composite with internal Hopf junctions and crossings —
contributes to the local value of $q$ through its own topological
linking structure.  The effective substrate parameter seen by a
nucleus is therefore

$$
  q_{\mathrm{eff}}(p, n)
  \;=\;
  q_0 \;+\; \delta q(p, n)
$$

where $q_0 = 1.110$ is the background value
([local substrate $q$](#prop:local-substrate-q)) and
$\delta q(p, n)$ is the hadron's self-deformation.

**Proposition.**
Let $\mathcal{N}(p, n) = p\,\mathfrak{p} \bowtie n\,\mathfrak{n}$
be a nucleus ([stable nucleus](#def:stable-nucleus)).  The
self-deformation of the substrate parameter is determined by the
*signed* crossing excess — the imbalance between positive
($\mathfrak{p}$--$\mathfrak{p}$) and negative
($\mathfrak{n}$--$\mathfrak{n}$) Hopf crossings:

$$
  \delta q(p, n)
  \;=\;
  \frac{\ell_{\mathrm{net}}(p, n)}{A^2}
  \cdot \hbar_q^2
$$

where $\hbar_q = 1 - q_0^{-1}$ is the quantum Planck constant and
the net signed crossing number is

$$
  \ell_{\mathrm{net}}(p, n)
  \;=\;
  \binom{p}{2} - \binom{n}{2}
  \;=\;
  \frac{p(p-1) - n(n-1)}{2}.
$$

For nuclei on the neutron-rich side of the valley ($n > p$),
$\ell_{\mathrm{net}} < 0$ and the local $q$ is slightly *reduced*.
For proton-rich nuclei, $\ell_{\mathrm{net}} > 0$ and $q$ is
slightly increased.

**Why the net signed crossing.**
The $q$-deformed wedge product $\wedge_q$ in the gauge sector of the
canonical action
([canonical action](#def:qou-canonical-action))
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
At $q_0 = 1.110$: $\hbar_q \approx 0.0991$ and
$\hbar_q^2 \approx 0.00982$.  For representative nuclei:

| Nucleus | $(p, n)$ | $A$ | $\ell_{\mathrm{net}}$ | $\delta q$ | $\delta q / q_0$ |
|---------|----------|-----|----------------------|-----------|-----------------|
| ${}^{3}\mathrm{H}$ | $(1, 2)$ | 3 | $-1$ | $-0.0011$ | $-0.10\%$ |
| ${}^{14}\mathrm{C}$ | $(6, 8)$ | 14 | $-13$ | $-0.0007$ | $-0.06\%$ |
| ${}^{60}\mathrm{Co}$ | $(27, 33)$ | 60 | $-177$ | $-0.0005$ | $-0.04\%$ |
| ${}^{90}\mathrm{Sr}$ | $(38, 52)$ | 90 | $-623$ | $-0.0008$ | $-0.07\%$ |
| ${}^{137}\mathrm{Cs}$ | $(55, 82)$ | 137 | $-1836$ | $-0.0010$ | $-0.09\%$ |
| ${}^{210}\mathrm{Bi}$ | $(83, 127)$ | 210 | $-4598$ | $-0.0010$ | $-0.09\%$ |

The self-deformation is genuinely small ($|\delta q / q_0| < 0.1\%$
for all nuclei).

**Effect on beta decay: the differential shift.**
In beta decay, $A$ is fixed but $(p, n)$ changes by $(+1, -1)$.
The *daughter* nucleus has a different self-deformation from the
parent.  The change in effective $q$ across the decay is

$$
  \Delta q_{\mathrm{eff}}
  \;=\;
  \delta q(p+1, n-1) - \delta q(p, n)
  \;=\;
  \frac{A - 1}{A^2} \cdot \hbar_q^2.
$$

This is always positive: the daughter (with one more proton) has
more positive crossings, hence a higher effective $q$.  A higher
$q$ means a larger Coulomb splitting and therefore a larger
$Q$-value than the background calculation predicts.  Via the
Sargent rule $f(Q) \propto Q^5$, the corrected $Q$-value
increases the decay rate and *shortens* the half-life.

**Corrected predictions.**
The differential shift $\Delta q_{\mathrm{eff}}$ modifies the
$Q$-value by

$$
  Q_{\mathrm{eff}}
  \;=\;
  Q_0 + \frac{\partial Q}{\partial q}\bigg|_{q_0}
  \cdot \Delta q_{\mathrm{eff}}
  \;=\;
  Q_0\!\left(1 + \frac{\Delta q_{\mathrm{eff}}}{q_0 - q_0^{-1}}
  \right)
$$

where the second equality uses $\partial Q / \partial q \approx
Q_0 / (q - q^{-1})$ from the Coulomb coefficient $a_C = (q - q^{-1})
\cdot \lambda_C$.  The corrected half-life is then

$$
  t_{1/2}^{\mathrm{corr}}
  \;=\;
  t_{1/2}^{\,0}
  \cdot
  \left(1 + \frac{\Delta q_{\mathrm{eff}}}{q_0 - q_0^{-1}}\right)^{-5}.
$$

At $q_0 = 1.110$: $q_0 - q_0^{-1} = 0.2091$ and
$\hbar_q^2 = 0.00982$.  The correction factor for each nucleus is:

| Nucleus | $A$ | $(A-1)/A^2$ | $\Delta q_{\mathrm{eff}}$ | Correction | $t_{1/2}^{\mathrm{corr}}$ | $t_{1/2}^{\mathrm{obs}}$ | Ratio |
|---------|-----|-------------|--------------------------|------------|--------------------------|--------------------------|-------|
| ${}^{3}\mathrm{H}$ | 3 | 0.222 | 0.00218 | 0.951 | $\sim 12.4$ yr | 12.3 yr | 1.01 |
| ${}^{14}\mathrm{C}$ | 14 | 0.0664 | 0.000652 | 0.984 | $\sim 6690$ yr | 5730 yr | 1.17 |
| ${}^{60}\mathrm{Co}$ | 60 | 0.0164 | 0.000161 | 0.996 | $\sim 6.17$ yr | 5.27 yr | 1.17 |
| ${}^{90}\mathrm{Sr}$ | 90 | 0.0110 | 0.000108 | 0.997 | $\sim 31.9$ yr | 28.8 yr | 1.11 |
| ${}^{137}\mathrm{Cs}$ | 137 | 0.00723 | 0.0000710 | 0.998 | $\sim 32.9$ yr | 30.2 yr | 1.09 |
| ${}^{210}\mathrm{Bi}$ | 210 | 0.00474 | 0.0000466 | 0.999 | $\sim 5.79$ d | 5.01 d | 1.16 |

The self-deformation correction is largest for the lightest nuclei
(tritium, where it removes most of the 5.5% overestimate) and
negligible for heavy nuclei.  The remaining systematic bias of
$\sim 10$--$17\%$ for medium and heavy nuclei points to a second
correction: the **Fermi-function Coulomb enhancement**, which
increases the decay rate by a $Z$-dependent factor that grows
with nuclear charge.

**Universality.**
The self-deformation applies to *every* equation where $q$ is
evaluated on a specific hadron configuration — not just half-lives.
The Skein binding Lagrangian
([Skein binding Lagrangian](#def:skein-binding-lagrangian)),
the beta-stability line
([beta-stability](#prop:beta-stability)), and the topological mass
formula all receive analogous corrections when $q_0$ is replaced by
$q_{\mathrm{eff}}$.  For nuclear masses, the correction is already
absorbed into the fitted values of $\lambda_V, \lambda_S, \lambda_C$
(which implicitly include the average $\delta q$ across the periodic
table).  For *differences* — like the $Q$-value driving beta decay —
the $A$-dependent part of $\delta q$ produces a residual that the
background $q_0$ alone does not capture.
