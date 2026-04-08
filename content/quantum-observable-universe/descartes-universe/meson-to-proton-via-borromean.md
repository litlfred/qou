A [proton](#def:categorical-proton) is **not** formed by adding a
quark to a [meson](#def:categorical-meson).  A meson is a
quark--antiquark pair ($q\bar{q}$, baryon number $B = 0$); a single
quark has $B = 1/3$.  Their sum $q\bar{q} + q$ has $B = 1/3$, not
$B = 1$ as required for a baryon.  The antiquark inside the meson
cannot spontaneously convert into a quark — baryon number is
conserved.

## Three pair productions $\to$ proton

The proton requires three quarks ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$)
with no antiquarks.  These come from three independent
[quark--antiquark productions](#def:quark-antiquark-production),
each of which creates a $q\bar{q}$ pair from colliding colored
photons:

$$
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_1 + \bar{\mathfrak{u}}_1
  \qquad
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_2 + \bar{\mathfrak{u}}_2
  \qquad
  \gamma\gamma \xrightarrow{L_-}
  \mathfrak{d}_3 + \bar{\mathfrak{d}}_3
$$

From these six particles, take three quarks
($\mathfrak{u}_1$, $\mathfrak{u}_2$, $\mathfrak{d}_3$)
and confine them via the [Borromean braid](#conj:borromean-quark)
$\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$:

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})
$$

The three antiquarks ($\bar{\mathfrak{u}}_1$, $\bar{\mathfrak{u}}_2$,
$\bar{\mathfrak{d}}_3$) either annihilate back to photons or form
an antiproton $\bar{\mathfrak{p}}$.  Total baryon number is conserved:
$3 \times (1/3 - 1/3) = 0$ in, $1 + (-1) = 0$ out.

## Typed crossings: the physical proton and neutron

The untyped composition gives $\mathrm{net} \approx 1.506$, not the
CODATA proton net $\approx 0.999$.  The gap is closed by **typed
crossings**: the quark flavor determines the crossing eigenvalue in
$H_3(q)$.

| Crossing type | Hecke eigenvalue |
|:---|:---|
| $\mathfrak{u}$-$\mathfrak{u}$ ($\sigma$) | $+q$ |
| $\mathfrak{d}$-$\mathfrak{d}$ ($\sigma - H_A\cdot\mathbf{1}$) | $-q^{-1}$ |
| $\mathfrak{u}$-$\mathfrak{d}$ ($\sigma - \tfrac{1}{2}H_A\cdot\mathbf{1}$) | mixed |

where $H_A = q - q^{-1}$.  The down-quark crossings carry a
$-H_A\cdot\mathbf{1}$ shift that reduces the net.

With typed crossings at $q_0 \approx 1.1100$:

| Nucleon | Quark content | $\mathrm{net}$ |
|:---|:---|---:|
| Proton $\mathfrak{p}$ | $\mathfrak{u}\mathfrak{u}\mathfrak{d}$ | $+0.9991$ |
| Neutron $\mathfrak{n}$ | $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ | $+0.8108$ |

## Why $\mathbf{E}_0 = Q / |\Delta\mathrm{net}|$

The NF coefficients are dimensionless Laurent polynomials in $q$.
To convert to physical energies (MeV), a single scale
$\mathbf{E}_0$ is needed.  This scale is **fixed by one
observable**: the beta decay $Q$-value.

1. **Linearity.**  The normal form $\mathrm{NF}$ is coordinate
   extraction in the Gröbner--Shirshov basis — a **linear map** on
   the 6-dimensional vector space $H_3(q)$.  Therefore
   $\mathrm{NF}(\mathfrak{n} - \mathfrak{p}) =
   \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p})$, and the
   net difference is the sum of all coefficient differences:

   $$
     \Delta\mathrm{net}
     = 
     \mathrm{net}(\mathfrak{n}) - \mathrm{net}(\mathfrak{p})
     = 
     0.8108 - 0.9991
     = 
     -0.1883.
   $$

2. **Calibration.**  Beta decay
   $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$ releases
   $Q_\beta = \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}}
   - \mathfrak{m}_e \approx 0.782 \text{MeV}$.  This is the energy
   equivalent of the dimensionless transition $\Delta\mathrm{net}$:

   $$
     \mathbf{E}_0
     = 
     \frac{Q_\beta}{|\Delta\mathrm{net}|}
     = 
     \frac{0.782}{0.1883}
      \approx  4.155 \text{MeV}.
   $$

3. **Why this works.**  The ratio is well-defined because:
   - $q_0$ is already fixed (substrate parameter), so all NF
     coefficients are determined — no remaining free parameters
     in the algebra.
   - $Q_\beta$ is the best-measured nuclear transition energy
     ($\pm 0.6$ eV precision from CODATA 2022).
   - The sign $\Delta\mathrm{net} < 0$ (neutron net $<$ proton net)
     is a consequence of typed crossings: the extra down quark in
     $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ introduces
     $-H_A$ shifts that lower the neutron's net below the proton's.

Once $\mathbf{E}_0$ is set, every other NF coefficient difference
$\Delta_i$ contributes $\Delta_i \times \mathbf{E}_0$ MeV to the
decay energy budget — and the six terms sum exactly to $Q_\beta$
([energy scale](#rem:beta-decay-energy-scale)).

Witness: `meson-nucleon-nf.witness.json`,
`beta-decay-energy-scale.witness.json`.
