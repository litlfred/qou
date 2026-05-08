**Definition.**
Let $\mathcal{E}_q$ be the [Descartes elliptic curve](#prop:descartes-elliptic-curve)
with Weierstrass coefficients $p(q)$, $r(q)$, and let $\Lambda_q \subset \mathbb{C}$
be the period lattice of $\mathcal{E}_q$.  The **:defterm[Weierstrass projection]{#weierstrass-projection}** is the
meromorphic function $\wp_q : \mathbb{C}/\Lambda_q \to \mathbb{P}^1$ defined by

$$
  \wp_q(z) =  \frac{1}{z^2}
  +  \sum_{\omega \in \Lambda_q \setminus \{0\}}
  \left(\frac{1}{(z - \omega)^2} - \frac{1}{\omega^2}\right).
$$

**Period lattice.**
The lattice $\Lambda_q$ is spanned by the two fundamental periods
$\omega_1(q)$, $\omega_2(q)$ obtained by integrating the holomorphic
differential $\mathrm{d}x / y$ over a basis of $H_1(\mathcal{E}_q, \mathbb{Z})$.
The lattice modulus $\tau_q = \omega_2(q)/\omega_1(q)$ satisfies
$\mathrm{Im}(\tau_q) > 0$ and encodes the conformal class of
$\mathcal{E}_q$.

**Uniformisation.**
The map

$$
  \mathbb{C}/\Lambda_q \xrightarrow{ \sim } \mathcal{E}_q,
  \qquad
  z  \longmapsto  [\wp_q(z) : \wp_q'(z) : 1]
$$

is an isomorphism of Riemann surfaces (with $0 \mapsto [0:1:0]$, the
point at infinity).  This exhibits $\mathbb{C}/\Lambda_q$ as the
universal cover of $\mathcal{E}_q$.

**Differential equation.**
The function $\wp_q$ satisfies

$$
  \wp_q'(z)^2 =  4\wp_q(z)^3
  +  4p(q)\wp_q(z)
  +  4r(q),
$$

which is the standard Weierstrass equation $\wp'^2 = 4\wp^3 - g_2\wp - g_3$
with invariants

$$
  g_2(q) = -4p(q), \qquad g_3(q) = -4r(q).
$$

The factor of $4$ arises from converting the short Weierstrass form
$y^2 = x^3 + px + r$ of the [Descartes elliptic curve](#prop:descartes-elliptic-curve)
to the classical $\wp$-function normalisation.

**Regime table.**

| Regime | $q$ | Lattice shape | Physics |
|--------|-----|---------------|---------|
| Classical | $q = 1$ | $\Lambda_1$ rectangular ($\tau_1 \in i\mathbb{R}$) | Degenerate curve $\mathcal{E}_1$; no crossing asymmetry |
| Physical | substrate $q$ | $\Lambda_q$ rhombic ($\mathrm{Im}(\tau_q) \approx 1.07$) | Our universe; $\mathcal{E}_q$ smooth, $\Delta < 0$ |
| Deep quantum | $q \to \infty$ | $\Lambda_q \to$ hexagonal ($\tau_q \to e^{2\pi i/3}$) | $j \to 0$; CM lattice; maximal symmetry |

**Notation convention.**
The symbol $\wp$ is **reserved** throughout this paper for the Weierstrass
elliptic function associated to $\mathcal{E}_q$.  It is never repurposed for
any other quantity.  When the dependence on $q$ is clear from context,
we write $\wp(z)$ for $\wp_q(z)$.
