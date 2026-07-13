<!-- FILE_START: glossary-observed-value.md -->
Let $\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z$ be the color tube coordinates at a point of Bring's surface. The **:defterm[observed spacetime value]{#observed-value}** is the element of $\mathbb{A}^1$ recovered from the color tube coordinates by the Vieta identity:

```tex
\begin{equation}\label{eq:observed-value}
  \mathbf{r}_z + \mathbf{g}_z + \mathbf{b}_z + 4z + 1 =  0.
\end{equation}
```

This identity defines the polynomial projection $\pi_z \colon R_z \times G_z \times B_z \to \mathbb{A}^1$, $(\mathbf{r}_z, \mathbf{g}_z, \mathbf{b}_z) \mapsto z$. At a branch point $z_c$ where chiral sheets merge, the exceptional divisor is coordinatised by the limiting color vector. The observed spacetime value reads off $z_c$ from the color data via the identity above, providing a coordinate on the exceptional $\mathbb{P}^1(\mathbb{C})$.

**Archimedean specialisation (§7c).** This block sits on the archimedean side of the substrate wall. It invokes real- or complex-analytic constructs. Generic categorical identities remain valid over an abstract coefficient ring; only their archimedean realisation is specialised here.
<!-- FILE_END: glossary-observed-value.md -->

<!-- FILE_START: glossary-weierstrass-projection.md -->
**Definition.**
Let $\mathcal{E}_q$ be the Descartes elliptic curve with Weierstrass coefficients $p(q)$, $r(q)$, and let $\Lambda_q \subset \mathbb{C}$ be the period lattice of $\mathcal{E}_q$. The **:defterm[Weierstrass projection]{#weierstrass-projection}** is the meromorphic function $\wp_q : \mathbb{C}/\Lambda_q \to \mathbb{P}^1$ defined by

$$
  \wp_q(z) =  \frac{1}{z^2}
  +  \sum_{\omega \in \Lambda_q \setminus \{0\}}
  \left(\frac{1}{(z - \omega)^2} - \frac{1}{\omega^2}\right).
$$

**Period lattice.**
The lattice $\Lambda_q$ is spanned by the two fundamental periods $\omega_1(q)$, $\omega_2(q)$ obtained by integrating the holomorphic differential $\mathrm{d}x / y$ over a basis of $H_1(\mathcal{E}_q, \mathbb{Z})$. The lattice modulus $\tau_q = \omega_2(q)/\omega_1(q)$ satisfies $\mathrm{Im}(\tau_q) > 0$ and encodes the conformal class of $\mathcal{E}_q$.

**Uniformisation.**
The map

$$
  \mathbb{C}/\Lambda_q \xrightarrow{ \sim } \mathcal{E}_q,
  \qquad
  z  \longmapsto  [\wp_q(z) : \wp_q'(z) : 1]
$$

is an isomorphism of Riemann surfaces. This exhibits $\mathbb{C}/\Lambda_q$ as the universal cover of $\mathcal{E}_q$.

**Differential equation.**
The function $\wp_q$ satisfies

$$
  \wp_q'(z)^2 =  4\wp_q(z)^3
  +  4p(q)\wp_q(z)
  +  4r(q),
$$

which is the standard Weierstrass equation $\wp'^2 = 4\wp^3 - g_2\wp - g_3$ with invariants $g_2(q) = -4p(q)$ and $g_3(q) = -4r(q)$. The factor of $4$ converts the short Weierstrass form to the classical $\wp$-function normalisation.

**Regime table.**

| Regime | $q$ | Lattice shape | Physics |
|--------|-----|---------------|---------|
| Classical | $q = 1$ | $\Lambda_1$ rectangular | Degenerate curve $\mathcal{E}_1$; no crossing asymmetry |
| Physical | substrate $q$ | $\Lambda_q$ rhombic | Our universe; $\mathcal{E}_q$ smooth, $\Delta < 0$ |
| Deep quantum | $q \to \infty$ | $\Lambda_q \to$ hexagonal | CM lattice; maximal symmetry |

**Notation convention.**
We reserve the symbol $\wp$ for the Weierstrass elliptic function associated to $\mathcal{E}_q$. We never repurpose it. We write $\wp(z)$ for $\wp_q(z)$ when the dependence on $q$ is clear.
<!-- FILE_END: glossary-weierstrass-projection.md -->

