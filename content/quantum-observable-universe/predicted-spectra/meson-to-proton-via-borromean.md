A [proton](#def:categorical-proton) is **not** formed by adding a
quark to a [meson](#def:categorical-meson).  A meson is a
quark--antiquark pair ($q\bar{q}$, baryon number $B = 0$); a single
quark has $B = 1/3$.  Their sum $q\bar{q} + q$ has $B = 1/3$, not
$B = 1$ as required for a baryon.  The antiquark inside the meson
cannot spontaneously convert into a quark — baryon number is
conserved.

## Mesons are unstable at $q_0$

Before discussing proton formation, note that the meson itself is
**not a stable bound state** at $q_0$.  The NF of the $\mathfrak{u}\bar{\mathfrak{d}}$
meson ($\sigma_0 \cdot L_+ \cdot \sigma_0^{-1}$) in $H_3(q)$ is:

$$
  \mathrm{NF}(\mathfrak{M}_+)
  =
  -0.209\sigma_1 - 0.044 L_+ + 1.000 L_- + 0.209 e^-
$$

with $\mathrm{net}(\mathfrak{M}_+) \approx +0.956$ and demand profile
$\{\sigma_1 = -0.209, L_+ = -0.044\}$.  The meson has two negative
NF coefficients — it demands crossing content ($\sigma_1$) and
Hopf link content ($L_+$) from its environment.

This is consistent with observed physics: mesons are short-lived
(the charged pion decays in $\sim 26$ ns).  At $q_0$, the meson's
demand makes it a transient intermediate, not a stable endpoint.
The only stable hadronic states are those produced by
$\mathcal{B}_3$ confinement (proton, neutron), where the Borromean
topology provides genuine 3-body binding.

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

## Why $\mathfrak{E}_0 = Q / |\Delta\mathrm{net}|$

The NF coefficients are dimensionless Laurent polynomials in $q$.
To convert to physical energies (MeV), a single scale
$\mathfrak{E}_0$ is needed.  This scale is **fixed by one
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
   $\mathfrak{Q}_\beta = \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}}
   - \mathfrak{m}_e \approx 0.782 \text{MeV}$.  This is the energy
   equivalent of the dimensionless transition $\Delta\mathrm{net}$:

   $$
     \mathfrak{E}_0
     = 
     \frac{\mathfrak{Q}_\beta}{|\Delta\mathrm{net}|}
     = 
     \frac{0.782}{0.1883}
      \approx  4.155 \text{MeV}.
   $$

3. **Why this works.**  The ratio is well-defined because:
   - $q_0$ is already fixed (substrate parameter), so all NF
     coefficients are determined — no remaining free parameters
     in the algebra.
   - $\mathfrak{Q}_\beta$ is the best-measured nuclear transition energy
     ($\pm 0.6$ eV precision from CODATA 2022).
   - The sign $\Delta\mathrm{net} < 0$ (neutron net $<$ proton net)
     is a consequence of typed crossings: the extra down quark in
     $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ introduces
     $-H_A$ shifts that lower the neutron's net below the proton's.

Once $\mathfrak{E}_0$ is set, every other NF coefficient difference
$\Delta_i$ contributes $\Delta_i \times \mathfrak{E}_0$ MeV to the
decay energy budget — and the six terms sum exactly to $\mathfrak{Q}_\beta$
([energy scale](#rem:beta-decay-energy-scale)).

**Full derivation.**
The chain described above is now formalized with full rigor in
[4-term pair nucleon](#prop:four-term-pair-nucleon): the
confinement operator $\mathcal{B}_3$ is derived from
minimum-action ([confinement selection](#prop:confinement-operator-selection)),
nucleon NFs are proved independent of photon polarization
([confinement universality](#prop:confinement-universality)),
and the beta decay channel emerges as the $e^- < 0$ coefficient
in the confined NF
([demand stability](#prop:demand-stability)).

Witness: `meson-nucleon-nf.witness.json`,
`beta-decay-energy-scale.witness.json`,
`confinement-operator-selection.witness.json`.
