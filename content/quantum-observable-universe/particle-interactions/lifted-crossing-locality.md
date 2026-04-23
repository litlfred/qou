## Lifted-crossing locality hypothesis

The [crossing-graded mass expansion](#conj:crossing-graded-mass-expansion)
is a finite sum over subsets of "lifted" crossings; in general, each
order-$n$ term is a non-trivial sum over $\binom{c}{n}$ configurations.
The **locality hypothesis** asserts that these per-configuration
contributions **factorize** into products of single-crossing
contributions whenever the crossings are topologically separated —
so that the expansion collapses to a closed-form exponential.

## Statement

**Conjecture.**
*Let $\mathcal{K}$ be an atomic braid and $\mathrm{Cr}(\mathcal{K})$
its set of crossings.  For any subset $S \subseteq \mathrm{Cr}(\mathcal{K})$,
let $\mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted}})$ denote
the Gröbner-Shirshov mass with exactly the crossings in $S$ carrying
the universal shape parameter $z_q$.  Then*

$$
  \mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{S \text{ lifted}})
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in S} \eta(c),
$$

*where $\eta(c)$ is a purely local factor depending on the crossing
$c$ alone, its sign $\varepsilon(c) \in \{\pm 1\}$, and the substrate
parameter $q$ — but not on which other crossings are lifted.*

## Consequence: exponential closed form

Given locality, the crossing-graded expansion collapses:

$$
  \mathfrak{m}(\mathcal{K}; q)
  \;=\;
  \sum_{n = 0}^c \xi(q)^n \cdot \mathfrak{m}^{(n)}_{\mathrm{GB}}(\mathcal{K})
  \;=\;
  \mathfrak{m}_{\mathrm{GB}}(\mathcal{K}) \cdot
  \prod_{c \in \mathrm{Cr}(\mathcal{K})} (1 + \xi(q)\,\eta(c)).
$$

For the homogeneous case $\eta(c) = 1$ for all $c$, this is simply
$(1 + \xi(q))^{c(\mathcal{K})}$.

## Why locality is non-trivial

Without locality, lifting two crossings $c_1, c_2$ could produce
interference: the joint amplitude
$\mathfrak{m}_{\mathrm{GB}}(\beta\lvert_{\{c_1,c_2\}})$ could contain
cross-terms that do **not** factor as
$\eta(c_1)\eta(c_2)\mathfrak{m}_{\mathrm{GB}}(\mathcal{K})$.  The
obstruction is a curvature / holonomy: parallel transport of the
shape parameter around a loop encircling both crossings would accumulate
a non-trivial phase.  Locality is the statement that this holonomy
vanishes at generic $q$.

See the [$q$-holonomy derivation](#rem:q-holonomy-locality-derivation)
for why flatness of the Knizhnik-Zamolodchikov connection at generic
(non-root-of-unity) $q$ enforces the locality factorization.

## Dependence on $q$ regime

Locality is **not** universal in $q$.  It holds on the generic stratum
and fails at special values:

- **Generic real $q$** (including substrate $q_0 \approx 1.11$):
  $U_q(\mathfrak{sl}_2)$-reps are semisimple, the KZ connection is
  flat, and locality holds.  This is the physical regime.
- **Roots of unity $q = e^{2 \pi i / \ell}$**: the category becomes
  non-semisimple (Jones-Wenzl truncation); the KZ connection
  develops obstructions and locality fails at level $\ell$.
- **Golden-ratio threshold $q = 1/\varphi^2$**: the Descartes curve
  degenerates ([cusp in $\mathcal{E}_q$](#prop:descartes-elliptic-curve)),
  $z_q \to 0$ or $1$, and locality becomes vacuous since $\xi(q) = 0$.

Locality holding at $q_0$ but **failing away from it** is what makes
the substrate parameter physically distinguished: it sits in the
locality window where the crossing-graded expansion has its cleanest
closed form.

## Empirical test

Locality predicts $\mathfrak{m}(\mathcal{K}) = \mathfrak{m}_{\mathrm{GB}}
\cdot \prod_c (1 + \xi \eta(c))$.  Deviations from this scaling —
residuals in binding energies not accounted for by the product formula —
quantify locality violations.  For doubly-magic atoms the product form
is within $\leq 6\%$ (see the
[JSJ/$\alpha$-clustering witness](#conj:mass-volume-factorization)),
consistent with approximate locality at $q_0$.
