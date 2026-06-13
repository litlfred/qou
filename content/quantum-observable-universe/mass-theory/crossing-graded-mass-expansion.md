## Crossing-graded mass expansion

**Parent framework.** The expansion below sits on top of two
already-established objects:

- [def:crossing-energy](#def:crossing-energy) — per-crossing weights
  are the **Hecke eigenvalues** $(q, -q^{-1})$ of $T$ on
  $S^2 V \oplus \Lambda^2 V$, derived from rigid-monoidal structure
  (not postulated).
- [def:algebraic-quantum-volume](#def:algebraic-quantum-volume)
  $\mathrm{Vol}_q(\beta) = \prod_i \hat{V}_i(q) \in
  \mathbb{Z}[q^{1/2}, q^{-1/2}]$ — the algebraic quantum volume of a
  braid, a Laurent polynomial in $q^{1/2}$.

The [mass-volume factorization](#conj:mass-volume-factorization) can
be organized as a perturbative expansion graded by the number of
"lifted" (volume-carrying) crossings.  The $n = 0$ term reproduces
the existing Gröbner-Shirshov NF mass; each higher order picks up
the per-crossing $(q, -q^{-1})$ eigenvalue contribution to
$\mathrm{Vol}_q(\beta)$.

## Statement

**Conjecture.**
*Let $\mathcal{K}$ be an atomic braid with braid word $\beta$ of
$c$ crossings, living in $H_{3A}(q)$.  Fix the universal shape
parameter $z_q \in \mathbb{C}$ from the [Descartes elliptic
curve](#prop:descartes-elliptic-curve) via its Legendre
$\lambda$-invariant, and define the depth scalar*

$$
  \xi(q) \;:=\; \frac{D(z_q)}{\hbar_q^2},
$$

*where $D$ is the Bloch-Wigner dilogarithm and $\hbar_q^2 = V(4_1) /
(m_\mu/m_e)$ is the pinned quantum of action.  Then the categorical
mass endomorphism admits a crossing-graded expansion*

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \sum_{n = 0}^{c(\mathcal{K})} \xi(q)^n \cdot
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K}),
$$

*where*

$$
  \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K})
  \;=\;
  \sum_{\substack{S \subseteq \{1, \ldots, c\} \\ \lvert S \rvert = n}}
  \mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted, rest flat}}),
$$

*and $\mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S,\mathrm{flat}})$ is
the Gröbner-Shirshov normal form of $\beta$ with crossings in $S$
carrying the shape $z_q$ (volume-contributing) and the remainder
skein-resolved (flat, zero-volume).*

## Order-by-order meaning

See [Table: Crossing-graded mass expansion](#tbl:crossing-graded-mass-expansion-table-data).
| $\vdots$ | $\vdots$ | $\vdots$ |
| $n = c$ | $\xi^c \cdot \mathfrak{m}^{(c)}_{\mathrm{GB}}$ | full Thurston volume — all crossings lifted |

## Locality corollary

If lifted-crossing contributions factorize pairwise — the
[lifted-crossing locality hypothesis](#conj:lifted-crossing-locality) —
the sum collapses to an exponential in crossing count:

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
The GB framework is the **real-axis degeneration** of the
volumized theory.

## Why this is a conjecture

This statement is a **conjecture** rather than a theorem because:

1. The universal shape parameter $z_q = \lambda(\mathcal{E}_q)$ is
   pinned by the Descartes curve, but its agreement with per-knot
   Thurston gluing is only an approximation (the
   $\lambda$-witness shows $D(z_q)/v_3 \approx 0.9015$ at $q_0$).
2. The separation of lifted vs flat crossings requires the
   [locality hypothesis](#conj:lifted-crossing-locality) as an
   independent assumption.
3. The exponential collapse to $(1 + \xi)^c$ further needs locality.

Each component is tracked separately as a conjecture so the status
of the overall expansion can be refined as derivations mature.
