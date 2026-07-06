We derive the proton and neutron from three independent $\gamma\gamma$ pair productions using the full 4-term photon color content.

## The 4-term photon

Each photon carries the full color content ([color content](#rem:knot-basis-color-content)):

$$
  \gamma_k
  =
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1
$$

where $\varphi_{01}\sigma_0\sigma_1 = \varphi_{01}L_+$ is the Hopf link dressing ([photon knot operations](#rem:physics-names-knot-operations)). When $\varphi_{01} = 0$, the $e^-$ channel closes. When $\varphi_{01} \neq 0$, the trefoil channel opens directly in the $\gamma\gamma$ product.

## Three pair productions

Three independent $\gamma\gamma$ collisions produce three quark--antiquark pairs ([quark--antiquark production](#def:quark-antiquark-production)):

$$
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_1 + \bar{\mathfrak{u}}_1,
  \qquad
  \gamma\gamma \xrightarrow{L_+}
  \mathfrak{u}_2 + \bar{\mathfrak{u}}_2,
  \qquad
  \gamma\gamma \xrightarrow{L_-}
  \mathfrak{d}_3 + \bar{\mathfrak{d}}_3.
$$

Each collision NF contains six terms (at $\varphi_{01} = 0.02$):

See [Table 1](#tbl:four-term-pair-nucleon-table1-data).

The quark is the crossing content ($\sigma_0$ or $\sigma_1$). The antiquark is the mirror crossing ($\sigma_0^{-1}$ or $\sigma_1^{-1}$).

## Confinement: $\mathcal{B}_3$ selected by minimum action

We select three quarks ($\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3$ for the proton) from the pairs and confine them via the Borromean braid $\mathcal{B}_3$. This is the unique minimum-action confinement operator ([confinement selection](#prop:confinement-operator-selection)).

The derivation chain is:

$$
  \mathfrak{p}
  =
  \mathcal{B}_3
  \cdot C(\mathfrak{u},\mathfrak{u};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_1)
$$

where $C(f_i, f_j; \sigma_k)$ is the typed crossing ([categorical proton](#def:categorical-proton)).

## Proton NF

Gröbner--Shirshov reduction at $q_0 \approx 1.1100$ yields:

See [Table 2](#tbl:four-term-pair-nucleon-table2-data).

$$
  \mathrm{net}(\mathfrak{p}) \approx +0.999
$$

## Neutron NF

For quarks $(\mathfrak{u}_1, \mathfrak{d}_2, \mathfrak{d}_3)$:

See [Table 3](#tbl:four-term-pair-nucleon-table3-data).

$$
  \mathrm{net}(\mathfrak{n}) \approx +0.811
$$

The neutron exhibits a larger demand in $\gamma$ ($-0.202$ versus $-0.100$) and an additional demand in $L_+$ ($-0.010$). This extra deficit drives beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$.

## Confinement universality

The nucleon NF is independent of the photon polarization $(\varphi_0, \varphi_1, \varphi_{01})$. Sweeping $\varphi_{01}$ from $0$ to $0.2$ leaves the proton and neutron NFs unchanged. The photon initial conditions determine which quark pairs are created. Once we select and confine the quarks by $\mathcal{B}_3$, the NF depends only on $q_0$ and the quark flavors.

**Witness**: `four-term-photon-to-atoms.witness.json`.
