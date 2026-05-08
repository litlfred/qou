The proton and neutron are **derived** — not asserted — from
three independent $\gamma\gamma$ pair productions using the full
4-term photon color content.

## The 4-term photon

Each photon carries the full color content
([color content](#rem:knot-basis-color-content)):

$$
  \gamma_k
  =
  \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1
  + \varphi_{01}\sigma_0\sigma_1
$$

where $\varphi_{01}\sigma_0\sigma_1 = \varphi_{01}L_+$ is the
Hopf link dressing
([photon knot operations](#rem:physics-names-knot-operations)).
In the 3-term specialization $\varphi_{01} = 0$, the $e^-$ channel
is closed; with $\varphi_{01} \neq 0$, the trefoil channel opens
directly in the $\gamma\gamma$ product.

## Three pair productions

Three independent $\gamma\gamma$ collisions produce three
quark--antiquark pairs
([quark--antiquark production](#def:quark-antiquark-production)):

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

Each collision NF has six terms (at $\varphi_{01} = 0.02$):

| Basis | Coefficient | Role |
|:---:|---:|:---|
| $\gamma$ | $+1.005$ | Photon identity (vacuum) |
| $\sigma_0$ | $+0.099$ | Horizontal polarization |
| $\sigma_1$ | $+0.099$ | Vertical polarization |
| $L_+$ | $+0.043$ | Hopf link dressing |
| $L_-$ | $+0.003$ | Cross-color Hopf |
| $e^-$ | $+0.002$ | Trefoil channel (4-term only) |

The quark is the crossing content ($\sigma_0$ or $\sigma_1$); the
antiquark is the mirror crossing ($\sigma_0^{-1}$ or $\sigma_1^{-1}$).

## Confinement: $\mathcal{B}_3$ selected by minimum action

From the three pairs, take three quarks
($\mathfrak{u}_1, \mathfrak{u}_2, \mathfrak{d}_3$ for the proton)
and confine them via the Borromean braid $\mathcal{B}_3$.
This operator is not assumed — it is the unique minimum-action
confinement operator
([confinement selection](#prop:confinement-operator-selection)).

The derivation chain is:

$$
  \mathfrak{p}
  =
  \mathcal{B}_3
  \cdot C(\mathfrak{u},\mathfrak{u};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_0)
  \cdot C(\mathfrak{u},\mathfrak{d};\sigma_1)
$$

where $C(f_i, f_j; \sigma_k)$ is the typed crossing
([categorical proton](#def:categorical-proton)).

## Proton NF

After Gröbner--Shirshov reduction at $q_0 \approx 1.1100$:

| Basis | Coefficient | Physical role |
|:---:|---:|:---|
| $\gamma$ | $-0.100$ | Vacuum deficit (mass source) |
| $\sigma_0$ | $+0.036$ | Residual crossing |
| $\sigma_1$ | $+0.998$ | Dominant up-quark channel |
| $L_+$ | $+0.099$ | Gluon field (Hopf) |
| $L_-$ | $+0.009$ | Mirror gluon |
| $e^-$ | $-0.043$ | Beta decay channel |

$$
  \mathrm{net}(\mathfrak{p}) \approx +0.999
$$

## Neutron NF

For quarks $(\mathfrak{u}_1, \mathfrak{d}_2, \mathfrak{d}_3)$:

| Basis | Coefficient | Physical role |
|:---:|---:|:---|
| $\gamma$ | $-0.202$ | Larger vacuum deficit |
| $\sigma_0$ | $+0.048$ | Residual crossing |
| $\sigma_1$ | $+1.009$ | Dominant channel |
| $L_+$ | $-0.010$ | Gluon deficit (Hopf demand) |
| $L_-$ | $+0.009$ | Mirror gluon |
| $e^-$ | $-0.044$ | Larger beta decay channel |

$$
  \mathrm{net}(\mathfrak{n}) \approx +0.811
$$

The neutron has larger demand in $\gamma$ ($-0.202$ vs $-0.100$)
and additional demand in $L_+$ ($-0.010$) — this extra deficit
drives beta decay $\mathfrak{n} \to \mathfrak{p} + e^- + \bar\nu$.

## Confinement universality

The nucleon NF is **independent of the photon polarization**
$(\varphi_0, \varphi_1, \varphi_{01})$.  Sweeping $\varphi_{01}$
from $0$ to $0.2$ leaves the proton and neutron NFs unchanged to
all digits.  The photon initial conditions determine *which*
quark pairs are created, but once the quarks are selected and
confined by $\mathcal{B}_3$, the NF depends only on $q_0$ and
the quark flavors.

**Witness**: `four-term-photon-to-atoms.witness.json`.
