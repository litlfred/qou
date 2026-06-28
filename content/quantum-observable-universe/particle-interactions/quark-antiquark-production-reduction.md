The [quark--antiquark production definition](#def:quark-antiquark-production)
names the chain $\gamma\gamma \to q\bar{q}$; here is the mechanism, step
by step, with no gap between photon pair and quark output.

**Step 0: two colored photons collide.**
Each photon is the Hecke algebra element
$\gamma = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1 + \varphi_{01}\sigma_0\sigma_1$
with independent color weights $\varphi_0, \varphi_1, \varphi_{01}$
([pair production](#def:breit-wheeler-pair-production)).
The derivation below uses the 3-term specialization $\varphi_{01} = 0$.

**Step 1: expand the product $\gamma_1 \cdot \gamma_2$.**
Given two colored photons (3-term specialization)
$\gamma_1 = \mathbf{1} + \varphi_0\sigma_0 + \varphi_1\sigma_1$
and
$\gamma_2 = \mathbf{1} + \psi_0\sigma_0 + \psi_1\sigma_1$,
their product NF in $H_3(q)$ is
([color content](#rem:knot-basis-color-content)):

$$
  \mathrm{NF}(\gamma_1 \cdot \gamma_2)
  = 
  (1 + \varphi_0\psi_0 + \varphi_1\psi_1)\gamma
  + 
  (\varphi_0 + \psi_0 + \varphi_0\psi_0h)\sigma_0
  + 
  (\varphi_1 + \psi_1 + \varphi_1\psi_1h)\sigma_1
  + 
  \varphi_0\psi_1L_+
  + 
  \varphi_1\psi_0L_-
$$

where $h = q - q^{-1}$.  The Hopf link terms
$L_+ = \sigma_0\sigma_1$ and $L_- = \sigma_1\sigma_0$ arise
exclusively from **cross-color** products: $\varphi_0\psi_1$
and $\varphi_1\psi_0$.

**Quark creation: step-by-step reduction of $L_+ \cdot e^-$.**
The positive Hopf link $L_+ = \sigma_0\sigma_1$ applied to the
trefoil $e^- = \sigma_0\sigma_1\sigma_0$ gives the five-letter
word $\sigma_0\sigma_1\sigma_0\sigma_1\sigma_0$.  Reduce using
the braid relation $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$
and the Hecke relation $\sigma_i^2 = h\sigma_i + \mathbf{1}$
(where $h = q - q^{-1}$):

$$
  \sigma_0\sigma_1 \cdot \sigma_0\sigma_1\sigma_0
  = 
  \sigma_0 \cdot (\sigma_1 \cdot \sigma_0\sigma_1\sigma_0)
$$

**Inner product** $\sigma_1 \cdot \sigma_0\sigma_1\sigma_0$:
apply the braid relation $\sigma_0\sigma_1\sigma_0 = \sigma_1\sigma_0\sigma_1$:

$$
  \sigma_1 \cdot \sigma_1\sigma_0\sigma_1
  = 
  \sigma_1^2 \cdot \sigma_0\sigma_1
  = 
  (h\sigma_1 + \mathbf{1}) \cdot \sigma_0\sigma_1
  = 
  h\sigma_1\sigma_0\sigma_1 + \sigma_0\sigma_1
$$

Apply the braid relation again ($\sigma_1\sigma_0\sigma_1 = \sigma_0\sigma_1\sigma_0$):

$$
  = 
  h\sigma_0\sigma_1\sigma_0 + \sigma_0\sigma_1
$$

**Outer product** $\sigma_0 \cdot (h\sigma_0\sigma_1\sigma_0 + \sigma_0\sigma_1)$:

$$
  h\sigma_0^2\sigma_1\sigma_0
  + 
  \sigma_0^2\sigma_1
$$

Apply $\sigma_0^2 = h\sigma_0 + \mathbf{1}$ to each:

$$
  h(h\sigma_0 + \mathbf{1})\sigma_1\sigma_0
  + 
  (h\sigma_0 + \mathbf{1})\sigma_1
$$

Distribute:

$$
  h^2\sigma_0\sigma_1\sigma_0
  + 
  h\sigma_1\sigma_0
  + 
  h\sigma_0\sigma_1
  + 
  \sigma_1
$$

**Result in the NF basis** $\{\mathbf{1}, \sigma_0, \sigma_1, L_+, L_-, e^-\}$:

$$
  \mathrm{NF}(L_+ \cdot e^-)
  = 
  \sigma_1
  + 
  h\sigma_0\sigma_1
  + 
  h\sigma_1\sigma_0
  + 
  h^2\sigma_0\sigma_1\sigma_0
$$

$$
  = 
  \sigma_1
  + 
  hL_+
  + 
  hL_-
  + 
  h^2e^-
$$

At $q_0 \approx 1.110$ ($h \approx 0.209$):

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\sigma_1$ | $\sigma_1$ | $1.000$ |
| $\sigma_0\sigma_1$ | $L_+$ | $h \approx 0.209$ |
| $\sigma_1\sigma_0$ | $L_-$ | $h \approx 0.209$ |
| $\sigma_0\sigma_1\sigma_0$ | $e^-$ | $h^2 \approx 0.044$ |

The Hopf link operator $L_+$ transmutes the trefoil electron into
a virtual crossing $\sigma_1$ plus residual Hopf and trefoil content.
The $e^-$ coefficient $h^2$ is the **residual electron** —
physically, the fraction of the original lepton that survives the
quark creation. The dominant output $\sigma_1$ is the
hadronic crossing that becomes the quark
([up quark](#def:up-quark)).  The mirror operator $L_-$ creates
an antiquark ($\bar{\mathfrak{d}}$) from the positron channel.

**Two independent productions.**
When two independent colored photon pairs undergo pair creation
simultaneously, each produces a quark--antiquark channel:

$$
  \gamma_1 \cdot \gamma_2  \to 
  \mathfrak{u} + \bar{\mathfrak{u}}
  \qquad\text{(production 1: up-type)}
$$

$$
  \gamma_3 \cdot \gamma_4  \to 
  \mathfrak{d} + \bar{\mathfrak{d}}
  \qquad\text{(production 2: down-type)}
$$

The quark type (up vs down) is determined by the crossing
orientation: $\sigma$ gives $\mathfrak{u}$ (positive), while
$\sigma^{-1}$ gives $\mathfrak{d}$ (negative)
([down quark](#def:down-quark)).

**Meson formation.**
When the $\mathfrak{u}$ from production 1 and the
$\bar{\mathfrak{d}}$ from production 2 come within Hopf linking
distance, they bind via $\mathcal{L}_H$ to form a meson
([categorical meson](#def:categorical-meson)):

$$
  \mathfrak{u} + \bar{\mathfrak{d}}
  \xrightarrow{\mathcal{L}_H}
  \mathfrak{M}_+
  =  T_{01} \cdot \mathcal{L}_H \cdot T_{10}
$$

The remaining $\bar{\mathfrak{u}}$ and $\mathfrak{d}$ either
annihilate back to photons or form the antimeson $\mathfrak{M}_-$.
This is the categorical expression of $\gamma\gamma \to
q\bar{q} + q\bar{q} \to \mathfrak{M} + \mathfrak{M}$.

**Three independent productions $\to$ nucleon.**
For baryon production, three independent pair creations produce
three quark--antiquark pairs.  Selecting one quark from each pair
gives a quark triple ($\mathfrak{u}\mathfrak{u}\mathfrak{d}$ for
proton, $\mathfrak{u}\mathfrak{d}\mathfrak{d}$ for neutron)
which is confined by the Borromean braid $\mathcal{B}_3$
([4-term pair nucleon](#prop:four-term-pair-nucleon)).
The confinement operator is derived, not asserted — see
[confinement selection](#prop:confinement-operator-selection).

**Witness**: `breit-wheeler-nucleon-nf.witness.json`,
`meson-nucleon-nf.witness.json`,
`four-term-photon-to-atoms.witness.json`.
