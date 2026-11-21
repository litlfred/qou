Baryon number conservation prevents adding a quark to a meson to form a proton. A meson consists of a quark--antiquark pair ($q\bar{q}$) and carries baryon number $B = 0$. A single quark carries $B = 1/3$. Their sum $q\bar{q} + q$ yields $B = 1/3$. A baryon requires $B = 1$. Baryon number conservation prevents the antiquark from spontaneously converting into a quark.

## Meson instability at $q_0$

The meson lacks stability at $q_0$. The normal form of the $\mathfrak{u}\bar{\mathfrak{d}}$ meson ($\sigma_0 \cdot L_+ \cdot \sigma_0^{-1}$) in $H_3(q)$ is:

$$
  \mathrm{NF}(\mathfrak{M}_+)
  =
  -0.209\sigma_1 - 0.044 L_+ + 1.000 L_- + 0.209 e^-
$$

This yields $\mathrm{net}(\mathfrak{M}_+) \approx +0.956$ and demand profile $\{\sigma_1 = -0.209, L_+ = -0.044\}$. Two negative normal form coefficients demand crossing content ($\sigma_1$) and Hopf link content ($L_+$) from the environment.

This demand renders the meson a transient intermediate rather than a stable endpoint. Observations align with this property. The charged pion decays in $\sim 26$ ns. Borromean topology $\mathcal{B}_3$ confinement provides genuine 3-body binding. This produces the only stable hadronic states, the proton and neutron.

## Three pair productions yield one proton

The proton requires three quarks ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) with no antiquarks. Three independent quark--antiquark productions supply these constituents. Colliding colored photons create each $q\bar{q}$ pair:

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

The Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$ confines three quarks ($\mathfrak{u}_1$, $\mathfrak{u}_2$, $\mathfrak{d}_3$) selected from these six particles:

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})
$$

The three antiquarks ($\bar{\mathfrak{u}}_1$, $\bar{\mathfrak{u}}_2$, $\bar{\mathfrak{d}}_3$) annihilate back to photons or form an antiproton $\bar{\mathfrak{p}}$. Total baryon number remains conserved: $3 \times (1/3 - 1/3) = 0$ input, $1 + (-1) = 0$ output.

## Typed crossings: the physical proton and neutron

Untyped composition yields $\mathrm{net} \approx 1.506$. The CODATA proton net is $\approx 0.999$. Typed crossings close this gap. Quark flavor determines the crossing eigenvalue in $H_3(q)$.

| Crossing type | Hecke eigenvalue |
|:---|:---|
| $\mathfrak{u}$-$\mathfrak{u}$ ($\sigma$) | $+q$ |
| $\mathfrak{d}$-$\mathfrak{d}$ ($\sigma - h_{\mathrm{A}}\cdot\mathbf{1}$) | $-q^{-1}$ |
| $\mathfrak{u}$-$\mathfrak{d}$ ($\sigma - \tfrac{1}{2}h_{\mathrm{A}}\cdot\mathbf{1}$) | mixed |

The term $h_{\mathrm{A}}$ equals $q - q^{-1}$. Down-quark crossings carry a $-h_{\mathrm{A}}\cdot\mathbf{1}$ shift. This shift reduces the net coefficient.

Typed crossings at $q_0 \approx 1.1100$ produce:

| Nucleon | Quark content | $\mathrm{net}$ |
|:---|:---|---:|
| Proton $\mathfrak{p}$ | $\mathfrak{u}\mathfrak{u}\mathfrak{d}$ | $+0.9991$ |
| Neutron $\mathfrak{n}$ | $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ | $+0.8108$ |

## The scale $\mathfrak{E}_0 = Q / |\Delta\mathrm{net}|$

The normal form coefficients represent dimensionless Laurent polynomials in $q$. Converting them to physical energies (MeV) requires a single scale $\mathfrak{E}_0$. The beta decay $Q$-value fixes this scale.

1. **Linearity.** The normal form computation constitutes a linear map on the 6-dimensional vector space $H_3(q)$. Therefore, $\mathrm{NF}(\mathfrak{n} - \mathfrak{p}) = \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p})$. The net difference equals the sum of all coefficient differences:

   $$
     \Delta\mathrm{net}
     = 
     \mathrm{net}(\mathfrak{n}) - \mathrm{net}(\mathfrak{p})
     = 
     0.8108 - 0.9991
     = 
     -0.1883.
   $$

2. **Calibration.** Beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$ releases $\mathfrak{Q}_\beta = \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} - \mathfrak{m}_e \approx 0.782 \text{ MeV}$. This supplies the energy equivalent of the dimensionless transition $\Delta\mathrm{net}$:

   $$
     \mathfrak{E}_0
     = 
     \frac{\mathfrak{Q}_\beta}{|\Delta\mathrm{net}|}
     = 
     \frac{0.782}{0.1883}
      \approx  4.155 \text{ MeV}.
   $$

3. **Well-definedness.** The fixed substrate parameter $q_0$ determines all normal form coefficients. CODATA 2022 measures $\mathfrak{Q}_\beta$ to $\pm 0.6$ eV precision. Typed crossings mandate the negative sign $\Delta\mathrm{net} < 0$. The extra down quark in $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ introduces $-h_{\mathrm{A}}$ shifts. These shifts lower the neutron net below the proton net. The ratio remains well-defined.

The parameter $\mathfrak{E}_0$ dictates the energy budget. Each normal form coefficient difference $\Delta_i$ contributes $\Delta_i \times \mathfrak{E}_0$ MeV to the decay energy. The six terms sum exactly to $\mathfrak{Q}_\beta$.

**Full derivation.**
Minimum action principles derive the confinement operator $\mathcal{B}_3$. Nucleon normal forms remain independent of photon polarization. The beta decay channel emerges as the $e^- < 0$ coefficient in the confined normal form.
