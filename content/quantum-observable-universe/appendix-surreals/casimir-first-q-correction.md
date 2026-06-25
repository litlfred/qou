**Conjecture (first substrate correction to the Casimir force is
carried by $4_1$).**
*Assume the plate-constrained mode-count of
[`conj:casimir-epsilon-vacuum`](#conj:casimir-epsilon-vacuum), whose
leading $1/d^{4}$ term is built from disjoint free-photon modes (the
bare photon being the identity $\mathbf{1}$, $q$-independent) and is
therefore independent of the substrate deformation. The
first contribution carrying substrate-$q$ dependence arises from the
interacting sector — vacuum modes whose braid words have degree
$\geq 2$ and whose closures are hyperbolic — and its minimal carrier
is the figure-eight knot $4_1$, entering with relative weight equal
to its Markov trace*

$$
J_{4_1}(q) \;=\; q^{-2} - q^{-1} + 1 - q + q^{2}
\;=\; 1 \;+\; \tfrac{3}{4}\,h^{2} \;+\; O(h^{4}),
\qquad h = q - q^{-1}.
$$

## Why the leading term carries no $q$

The leading parallel-plate term is assembled from free photon modes:
each is the identity braid, whose Markov closure is a disjoint union
of unknots, and degree-$\leq 1$ closures are non-hyperbolic with
vanishing volume
([`lem:degree-one-braid-trivial-volume`](#lem:degree-one-braid-trivial-volume)).
A mode that does not braid transmits no substrate deformation, so the
$\zeta(-3)$ prefactor $\pi^{2}/720$ of the parent conjecture is
undeformed. Substrate corrections can therefore enter only where
modes braid — the interacting sector.

## Torus closures contribute nothing

Degree $\geq 2$ is necessary for hyperbolicity but not sufficient.
The minimal degree-$\geq 2$ closures — the Hopf link
($\sigma_1^{2}$), the trefoil $3_1$ ($\sigma_1^{3}$), and the
$(2,5)$-torus knot $5_1$ ($\sigma_1^{5}$) — are torus links with
$\mathrm{Vol} = 0$, hence carry no substrate weight. The first
hyperbolic closure is the figure-eight knot $4_1$
($\sigma_1\sigma_2^{-1}\sigma_1\sigma_2^{-1}$), the unique
minimal-volume hyperbolic knot, with
$\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3) \approx 2.0299$.

## The $3/4$ is exact algebra

With $h = q - q^{-1}$, the figure-eight weight satisfies the exact
field identity

$$
J_{4_1}(q) \;=\; 1 + \tfrac{3}{4}\,h^{2}
\;+\; \frac{h^{4}}{4\left(h^{2} + 8 + 4(q + q^{-1})\right)},
$$

with the remainder denominator strictly positive for $q > 0$. The
coefficient $3/4$ is forced by the identity — there is no fitted
constant. The expansion is proved sorry-free in
`FigureEightCasimirWeight.lean` (`jones41_taylor`,
`jones41_three_quarters_cleared`, `jones41_remainder_denom_pos`).
At the substrate anchor the relative weight $\tfrac{3}{4}h^{2}$
evaluates to $\approx 3\%$.

## Self-consistency with the substrate

$4_1$ is not an arbitrary carrier: the substrate parameter $q_0$ is
itself fixed through $\mathrm{Vol}(4_1)$ (the $m_p/m_e$ pin). The
knot that defines the framework's one calibrated deformation
parameter is also the carrier of the vacuum's first substrate
correction — the correction introduces no independent scale.

## What is open (the actual conjecture)

Two items, both requiring the interacting-mode mode-sum — the
Yekutieli-homotopy lift of the parent conjecture's mode-count
restricted to degree-$\geq 2$ closures:

1. **The power of $1/d$.** The radiative-correction analogy
   suggests $1/d^{6}$; this is an expectation, not a derivation.
2. **The absolute magnitude.** The relative weight
   $1 + \tfrac{3}{4}h^{2}$ multiplies an interacting-sector
   amplitude suppressed by $\sim \alpha\,\lambda_C/d$, far below
   the precision of current Casimir-force measurements (see the
   falsification note of the parent block); the conjecture is a
   structural prediction target, not a near-term experimental
   discriminator.

## Falsification path

Construct the interacting-mode mode-sum and extract the sector
coefficients. If the first non-vanishing substrate correction is
*not* weighted by $J_{4_1}$ — for example, if a torus-sector
contribution survives with nonzero weight, or a different
hyperbolic closure dominates — the conjecture is refuted.
## See also

- [`conj:casimir-epsilon-vacuum`](#conj:casimir-epsilon-vacuum) —
  parent conjecture: the leading $1/d^{4}$ term and the
  $\varepsilon$-vacuum mechanism.
- [`lem:degree-one-braid-trivial-volume`](#lem:degree-one-braid-trivial-volume) —
  degree-$\leq 1$ closures carry no volume, hence no substrate
  weight.
- [`conj:vacuum-epsilon`](#conj:vacuum-epsilon) — the
  $\varepsilon$-relaxed vacuum axiom upstream of both Casimir
  blocks.
