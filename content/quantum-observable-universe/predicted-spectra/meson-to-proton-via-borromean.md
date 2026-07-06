Adding a quark to a meson does not form a proton. A meson is a quark--antiquark pair ($q\bar{q}$) and carries baryon number $B = 0$. A single quark carries $B = 1/3$. Their sum $q\bar{q} + q$ has $B = 1/3$. A baryon requires $B = 1$. The antiquark inside the meson cannot spontaneously convert into a quark, because baryon number is conserved.

## Meson instability at $q_0$

The meson itself is not a stable bound state at $q_0$. The normal form of the $\mathfrak{u}\bar{\mathfrak{d}}$ meson ($\sigma_0 \cdot L_+ \cdot \sigma_0^{-1}$) in $H_3(q)$ is:

$$
  \mathrm{NF}(\mathfrak{M}_+)
  =
  -0.209\sigma_1 - 0.044 L_+ + 1.000 L_- + 0.209 e^-
$$

This yields $\mathrm{net}(\mathfrak{M}_+) \approx +0.956$ and demand profile $\{\sigma_1 = -0.209, L_+ = -0.044\}$. The meson has two negative normal form coefficients. It demands crossing content ($\sigma_1$) and Hopf link content ($L_+$) from its environment.

This aligns with observed physics. Mesons are short-lived. The charged pion decays in $\sim 26$ ns. At $q_0$, the meson's demand makes it a transient intermediate rather than a stable endpoint. The only stable hadronic states are those produced by $\mathcal{B}_3$ confinement, such as the proton and neutron. The Borromean topology provides genuine 3-body binding.

## Three pair productions yield one proton

The proton requires three quarks ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$) with no antiquarks. These originate from three independent quark--antiquark productions. Each production creates a $q\bar{q}$ pair from colliding colored photons:

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

We take three quarks ($\mathfrak{u}_1$, $\mathfrak{u}_2$, $\mathfrak{d}_3$) from these six particles and confine them via the Borromean braid $\mathcal{B}_3 = (\sigma_0\sigma_1^{-1})^3$:

$$
  \mathfrak{p}
  = 
  \mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})
$$

The three antiquarks ($\bar{\mathfrak{u}}_1$, $\bar{\mathfrak{u}}_2$, $\bar{\mathfrak{d}}_3$) either annihilate back to photons or form an antiproton $\bar{\mathfrak{p}}$. Total baryon number is conserved: $3 \times (1/3 - 1/3) = 0$ input, $1 + (-1) = 0$ output.

## Typed crossings: the physical proton and neutron

The untyped composition gives $\mathrm{net} \approx 1.506$. This exceeds the CODATA proton net of $\approx 0.999$. Typed crossings close the gap. The quark flavor determines the crossing eigenvalue in $H_3(q)$.

| Crossing type | Hecke eigenvalue |
|:---|:---|
| $\mathfrak{u}$-$\mathfrak{u}$ ($\sigma$) | $+q$ |
| $\mathfrak{d}$-$\mathfrak{d}$ ($\sigma - H_A\cdot\mathbf{1}$) | $-q^{-1}$ |
| $\mathfrak{u}$-$\mathfrak{d}$ ($\sigma - \tfrac{1}{2}H_A\cdot\mathbf{1}$) | mixed |

Here $H_A = q - q^{-1}$. The down-quark crossings carry a $-H_A\cdot\mathbf{1}$ shift that reduces the net coefficient.

With typed crossings at $q_0 \approx 1.1100$:

| Nucleon | Quark content | $\mathrm{net}$ |
|:---|:---|---:|
| Proton $\mathfrak{p}$ | $\mathfrak{u}\mathfrak{u}\mathfrak{d}$ | $+0.9991$ |
| Neutron $\mathfrak{n}$ | $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ | $+0.8108$ |

## The scale $\mathfrak{E}_0 = Q / |\Delta\mathrm{net}|$

The normal form coefficients are dimensionless Laurent polynomials in $q$. We require a single scale $\mathfrak{E}_0$ to convert them to physical energies (MeV). The beta decay $Q$-value fixes this scale.

1. **Linearity.** The normal form computation is a linear map on the 6-dimensional vector space $H_3(q)$. Therefore, $\mathrm{NF}(\mathfrak{n} - \mathfrak{p}) = \mathrm{NF}(\mathfrak{n}) - \mathrm{NF}(\mathfrak{p})$. The net difference is the sum of all coefficient differences:

   $$
     \Delta\mathrm{net}
     = 
     \mathrm{net}(\mathfrak{n}) - \mathrm{net}(\mathfrak{p})
     = 
     0.8108 - 0.9991
     = 
     -0.1883.
   $$

2. **Calibration.** Beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu_e$ releases $\mathfrak{Q}_\beta = \mathfrak{m}_{\mathfrak{n}} - \mathfrak{m}_{\mathfrak{p}} - \mathfrak{m}_e \approx 0.782 \text{ MeV}$. This is the energy equivalent of the dimensionless transition $\Delta\mathrm{net}$:

   $$
     \mathfrak{E}_0
     = 
     \frac{\mathfrak{Q}_\beta}{|\Delta\mathrm{net}|}
     = 
     \frac{0.782}{0.1883}
      \approx  4.155 \text{ MeV}.
   $$

3. **Well-definedness.** The ratio is well-defined. The substrate parameter $q_0$ is fixed, determining all normal form coefficients. The value $\mathfrak{Q}_\beta$ is measured to high precision ($\pm 0.6$ eV from CODATA 2022). The negative sign $\Delta\mathrm{net} < 0$ follows from typed crossings. The extra down quark in $[\mathfrak{u}, \mathfrak{d}, \mathfrak{d}]$ introduces $-H_A$ shifts, lowering the neutron's net below the proton's.

Setting $\mathfrak{E}_0$ determines the energy budget. Each normal form coefficient difference $\Delta_i$ contributes $\Delta_i \times \mathfrak{E}_0$ MeV to the decay energy. The six terms sum exactly to $\mathfrak{Q}_\beta$.

**Full derivation.**
The chain described above is formalized with full rigor in subsequent sections. Minimum action principles derive the confinement operator $\mathcal{B}_3$. Nucleon normal forms are proven independent of photon polarization. The beta decay channel emerges as the $e^- < 0$ coefficient in the confined normal form.

Witness: `meson-nucleon-nf.witness.json`,
`beta-decay-energy-scale.witness.json`,
`confinement-operator-selection.witness.json`.
