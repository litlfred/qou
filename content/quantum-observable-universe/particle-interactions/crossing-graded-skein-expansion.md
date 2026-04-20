## Crossing-graded skein expansion

The [mass-volume factorization](#conj:mass-volume-factorization) can
be organized as a perturbative expansion graded by the number of
"lifted" (volume-carrying) crossings.  This makes the factorization
**backward-compatible** with the existing Gröbner-Shirshov normal-form
computation: the standard NF mass arises as the leading term, and
each successive order injects the hyperbolic 3D depth carried by
additional crossings.

## The expansion

Fix the universal shape parameter $z_q \in \mathbb{C}$ from the
[Descartes elliptic curve](#prop:descartes-elliptic-curve) via its
Legendre $\lambda$-invariant.  Define the **depth scalar**

$$
  \xi(q) \;:=\; \frac{D(z_q)}{\hbar_q^2},
$$

where $D$ is the Bloch-Wigner dilogarithm and $\hbar_q^2 = V(4_1) /
(m_\mu / m_e)$ is the pinned quantum of action.  For a braid word
$\beta$ with $c$ crossings, grade each crossing by a binary label
$s_i \in \{0, 1\}$: $s_i = 0$ means skein-resolved (flat, no volume),
$s_i = 1$ means lifted (carrying shape $z_q$, contributing $D(z_q)$).

**Expansion.**

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \sum_{n = 0}^{c(\mathcal{K})} \xi(q)^n \cdot
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K}),
$$

$$
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K})
  \;=\;
  \sum_{\substack{S \subseteq \{1, \ldots, c\} \\ \lvert S \rvert = n}}
  \mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted, rest flat}}).
$$

## Order-by-order meaning

| Order | Term | Interpretation |
|:------|:-----|:---------------|
| $n = 0$ | $\mathfrak{m}^{(0)}_{\mathrm{GB}}$ | standard Gröbner-Shirshov NF — all crossings skein-resolved |
| $n = 1$ | $c \cdot \xi \cdot \overline{\mathfrak{m}^{(1)}}$ | linear correction; one crossing lifts into 3D |
| $n = 2$ | $\binom{c}{2} \xi^2 \cdot \overline{\mathfrak{m}^{(2)}}$ | pair-correction, tetrahedron-pair interactions |
| $\vdots$ | $\vdots$ | $\vdots$ |
| $n = c$ | $\xi^c \cdot \mathfrak{m}^{(c)}_{\mathrm{GB}}$ | full Thurston volume — all crossings lifted |

## Exponential scaling under locality

If lifted-crossing contributions factor (**locality hypothesis** —
no cross-talk between distant crossings), the sum collapses to an
exponential in crossing count:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  (1 + \xi(q))^{c(\mathcal{K})}.
$$

Each additional crossing multiplies mass by $(1 + \xi)$ — heavier knots
are **exponentially heavier**, not linearly.  Locality violations
would manifest as deviations from this exponential; the order
$n \geq 2$ terms encode the corrections.

## Connection to the quantum dilogarithm

The per-crossing weighting by $D(z_q)$ is the semiclassical limit
of the quantum dilogarithm operator $\Phi_q(z)$ acting at each
Hecke generator.  Expanding $\log \Phi_q(z)$ in the small parameter
$\hbar_q$:

$$
  \log \Phi_q(z)
  \;\sim\;
  \frac{1}{2\pi i \hbar_q}\,\mathrm{Li}_2(z)
  \;+\; O(\log \hbar_q),
$$

whose imaginary part at leading order is exactly $D(z)/(2\pi \hbar_q)$.
The $\xi^n$ expansion is the **Feynman-like ordered sum** in
$\hbar_q$, with each order corresponding to a Pachner-move
reorganization of the ideal triangulation.

## Recovery of the classical limit

Setting $\xi = 0$ (either via $D(z_q) = 0$ or $\hbar_q \to \infty$)
kills every $n \geq 1$ term, recovering the original Gröbner-Shirshov
mass endomorphism.  The condition $D(z_q) = 0$ occurs at real
$z_q$ — precisely the boundary of the Descartes curve at
$q = 1/\varphi^2$ ([golden-ratio degeneration](#prop:descartes-elliptic-curve)) —
so the GB framework is the **real-axis degeneration** of the
volumized theory.
