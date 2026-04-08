A [meson](#def:categorical-meson) contains two quarks ($q\bar{q}$).
Adding a third quark and confining all three via the Borromean
braid $\mathcal{B}_3$ produces a [proton](#def:categorical-proton).

## Meson + quark $\to$ proton

Take the meson $\mathfrak{M}_+ = T_{01} \cdot \mathcal{L}_H \cdot T_{10}$
(a $\mathfrak{u}\bar{\mathfrak{d}}$ pair) and a third up quark
$\mathfrak{u} = T_{01}$ from an independent
[quark--antiquark production](#def:quark-antiquark-production).
The [Borromean braid](#conj:borromean-quark)
$\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ confines the three
color lines:

$$
  \mathfrak{p}
  \;=\;
  \mathcal{B}_3(\mathfrak{u},\, \mathfrak{u},\, \mathfrak{d})
  \;=\;
  \mathfrak{M}_+ \;\cdot\; \mathcal{B}_3
$$

In untyped crossings, $\mathfrak{M}_+ \cdot \mathcal{B}_3$ yields:

$$
  \mathrm{NF}(\mathfrak{M}_+ \cdot \mathcal{B}_3)
  \;=\;
  -0.042\,\nu
  \;+\; 0.001\, H^0
  \;+\; 0.200\, H^1
  \;+\; 1.040\, L_+
  \;+\; 0.089\, L_-
  \;+\; 0.218\, e^-
$$

with $\mathrm{net} = +1.506$.  The Borromean factor
$\mathcal{B}_3$ contributes only $\sim 1\%$ to the net
(B₃ alone has $\mathrm{net} = +1.000$) but is essential for
three-strand confinement.

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
     \;=\;
     \mathrm{net}(\mathfrak{n}) - \mathrm{net}(\mathfrak{p})
     \;=\;
     0.8108 - 0.9991
     \;=\;
     -0.1883.
   $$

2. **Calibration.**  Beta decay
   $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$ releases
   $Q_\beta = \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}}
   - \mathfrak{m}_e \approx 0.782\;\text{MeV}$.  This is the energy
   equivalent of the dimensionless transition $\Delta\mathrm{net}$:

   $$
     \mathbf{E}_0
     \;=\;
     \frac{Q_\beta}{|\Delta\mathrm{net}|}
     \;=\;
     \frac{0.782}{0.1883}
     \;\approx\; 4.155\;\text{MeV}.
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
