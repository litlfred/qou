The **proton** is the baryon with $2 + 1$ crossing partition:
two up quarks (positive orientation) and one down quark (negative
orientation) in the Borromean link $\mathcal{B}_3$
([Borromean quark](#conj:borromean-quark)).

$$
  \mathfrak{p}
  \;=\;
  \mathcal{B}_3(\mathfrak{u},\, \mathfrak{u},\, \mathfrak{d})
  \;\bowtie\; \mathcal{L}_H
$$

where:

- $\mathcal{B}_3(\mathfrak{u}, \mathfrak{u}, \mathfrak{d})$ is the Borromean link of three
  unknots threaded through coral tubes $(r, g, b)$
  ([color tube coordinates](#def:color-tube-coordinates)):
  two with positive crossing orientation ($\mathfrak{u}$,
  [up quark](#def:up-quark)) and one with negative orientation
  ($\mathfrak{d}$, [down quark](#def:down-quark)),

- $\mathcal{L}_H$ is the Hopf link binding the three
  constituents,

- the $S_3$ permutation symmetry of the coral tubes ensures
  the definition is independent of the color assignment.

**Normal form (typed crossings).**
The quark flavor determines the crossing eigenvalue in $H_3(q)$:
$\mathfrak{u}$-type crossings carry eigenvalue $+q$ (positive
orientation), while $\mathfrak{d}$-type crossings carry a
$-H_A \cdot \mathbf{1}$ shift (where $H_A = q - q^{-1}$) that
reduces the net.  With typed crossings at $q_0 \approx 1.1100$,
the proton NF in the Gröbner–Shirshov basis
$\{\mathbf{1},\, \sigma_0,\, \sigma_1,\,
\sigma_0\sigma_1,\, \sigma_1\sigma_0,\,
\sigma_0\sigma_1\sigma_0\}$ is:

| Basis | Particle | Coefficient |
|:---:|:---:|---:|
| $\mathbf{1}$ | $\nu$ | $-0.0997$ |
| $\sigma_0$ | $H^0$ | $+0.0357$ |
| $\sigma_1$ | $H^1$ | $+0.9976$ |
| $\sigma_0\sigma_1$ | $L_+$ | $+0.0994$ |
| $\sigma_1\sigma_0$ | $L_-$ | $+0.0093$ |
| $\sigma_0\sigma_1\sigma_0$ | $e^-$ | $-0.0432$ |

$$
  \mathrm{net}(\mathfrak{p}) \;=\; +0.9991
$$

The dominant term is $H^1 \approx +0.998$, reflecting
the single up-quark crossing on strand 1.  The small but
nonzero $L_+$ and $L_-$ encode residual Hopf link content
from $\mathcal{B}_3$.  The negative $\nu$ and $e^-$
coefficients arise from the $-H_A$ shifts on the down-quark
crossings.

**Mass.**
The proton mass comes from the hyperbolic volume of the
Borromean link:

$$
  m_{\mathfrak{p}}
  \;=\;
  \frac{\mathrm{Vol}(S^3 \setminus \mathcal{B}_3)}{\hbar_q^2}
  \cdot \lambda_{\mathrm{scale}}
  \;+\; \text{Skein corrections}
$$

The Skein corrections arise from the crossing asymmetry between
the $\mathfrak{u}$ and $\mathfrak{d}$ components.  The pair Skein formula gives:

$$
  m_{\mathfrak{p}}
  \;=\;
  \mathcal{S}_{\mathfrak{u}\mathfrak{u}}(q) + 2\,\mathcal{S}_{\mathfrak{u}\mathfrak{d}}(q)
$$

At the CODATA value $q_0$: $m_{\mathfrak{p}}(q_0) \approx 938.272$ MeV, derived from the substrate parameter ([local substrate](#prop:local-substrate-q)).

**Coulomb charge.**
The proton carries net **positive crossing chirality**: two
positive-orientation unknots ($\mathfrak{u}$) outweigh one negative ($\mathfrak{d}$),
giving a net Coulomb charge

$$
  Q(\mathfrak{p}) \;=\; 2 \cdot (+\tfrac{2}{3}) + 1 \cdot (-\tfrac{1}{3}) \;=\; +1.
$$
