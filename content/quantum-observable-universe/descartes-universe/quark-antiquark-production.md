A **quark--antiquark production** is a Breit--Wheeler pair creation
([pair production](#def:breit-wheeler-pair-production)) in which
the colored photon's Hopf link content $L_+$ acts as the
**quark creation operator**, transmuting the leptonic trefoil
channel into a hadronic channel.

**Mechanism.**
In the normal form of a colored photon pair $\gamma_\phi^2$,
the Hopf link terms $L_+ = \sigma_0\sigma_1$ and
$L_- = \sigma_1\sigma_0$ appear with coefficient $\phi^2$.
The positive Hopf link $L_+$ applied to the trefoil channel
$e^- = \sigma_0\sigma_1\sigma_0$ yields:

$$
  L_+ \cdot e^-
  \;=\;
  (\sigma_0\sigma_1)(\sigma_0\sigma_1\sigma_0)
  \;\xrightarrow{\mathrm{NF}}\;
  \text{quark content} + \phi\cdot e^-
$$

The Hopf link operator creates a quark ($\mathfrak{u}$) from an
electron ($e^-$) by wrapping it in the Borromean color tube
([up quark](#def:up-quark)).  The mirror operator $L_-$ creates
an antiquark ($\bar{\mathfrak{d}}$) from the positron channel.

**Two independent productions.**
When two independent colored photon pairs undergo pair creation
simultaneously, each produces a quark--antiquark channel:

$$
  \gamma_\phi^2 \;\to\;
  \mathfrak{u} + \bar{\mathfrak{u}}
  \qquad\text{(production 1: up-type)}
$$

$$
  \gamma_\phi^2 \;\to\;
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
  \;\xrightarrow{\mathcal{L}_H}\;
  \mathfrak{M}_+
  \;=\; T_{01} \cdot \mathcal{L}_H \cdot T_{10}
$$

The remaining $\bar{\mathfrak{u}}$ and $\mathfrak{d}$ either
annihilate back to photons or form the antimeson $\mathfrak{M}_-$.
This is the categorical expression of $\gamma\gamma \to
q\bar{q} + q\bar{q} \to \mathfrak{M} + \mathfrak{M}$.

**Witness**: `breit-wheeler-nucleon-nf.witness.json`,
`meson-nucleon-nf.witness.json`.
