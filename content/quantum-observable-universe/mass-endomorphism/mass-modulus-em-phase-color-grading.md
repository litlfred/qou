The factorization of
[`prop:color-spacetime-s5-factorization`](#prop:color-spacetime-s5-factorization)
fixes how the three observables of a Bring-embeddable knot sit on the single
trace scalar $\mathrm{tr}_M$ and its trace algebra $H_2(q)\oplus H_3(q)$.

## Three readings of one trace

Write the trace scalar in polar form,
$$
  \mathrm{tr}_M \;=\; \lVert\mathrm{tr}_M\rVert\,\exp\!\big(i\,\arg\mathrm{tr}_M\big),
$$
the multiplicative companion of the additive complex-volume reconstruction
$\operatorname{Re}\mathfrak{V}+i\operatorname{Im}\mathfrak{V}=\mathfrak{V}$
([`conj:binding-qbeta-complex-volume`](#conj:binding-qbeta-complex-volume)).
Then:

| reading | quantity | sector | character |
|---|---|---|---|
| **mass** | modulus $\lVert\mathrm{tr}_M\rVert$ | both | nonnegative magnitude |
| **electromagnetism** | argument $\arg\mathrm{tr}_M$ | spacetime / $S_2$ | continuous $U(1)$ |
| **color** | $S_3$ irreducible-representation grading | color / $S_3$ | discrete |

Mass is the magnitude that survives both sectors. The argument is the
continuous $U(1)$ framing / Chern–Simons phase — the $\operatorname{Im}
\mathfrak{V}$ channel, picked up as the ribbon twist $q^{2w\,c(\lambda)}$ on a
framed knot of writhe $w$ ([`bar-parity-split`](../mass-theory/bar-parity-split.md))
— and it lives in the spacetime block, where it is read as the
electromagnetic phase. Color is the discrete grading of the algebra element
across the $H_3(q)$ representations, before the trace collapses it to a
scalar.

## Color is not the phase

Because the color factor $S_3$ fixes the spacetime coordinates and the
spacetime factor $S_2$ fixes the color coordinates
([`prop:color-spacetime-s5-factorization`](#prop:color-spacetime-s5-factorization),
parts 1–2), color and electromagnetism are independent coordinates: the
discrete color charge is not a function of the continuous phase, and
conversely. The rigidity in part 3 of that proposition makes the
non-coincidence sharp — a continuous winding argument cannot factor through a
finite group such as $\mu_5$, so $\arg\mathrm{tr}_M$ is structurally barred
from being a color character.

The two are nonetheless faces of one substrate. The Galois group $S_5$
properly contains $S_2\times S_3$, and its remaining generators carry
spacetime indices into color indices; an electromagnetic-to-color relation is
therefore an $S_5$ statement, realized by those off-block generators, not a
relation internal to the $U(1)$ phase. Mass, electromagnetism, and color are
one trace object read on its modulus, its spacetime phase, and its color
grading.

## Archimedean status

The polar split is the archimedean reading: the modulus and argument require
the realization of the trace over $\mathbb{C}$, on the far side of the
substrate-to-archimedean wall. The structural content of
[`prop:color-spacetime-s5-factorization`](#prop:color-spacetime-s5-factorization)
— the faithful $S_2\times S_3\hookrightarrow S_5$ embedding, the orthogonality
of the two sectors, and the divisibility rigidity — is generic and needs no
such realization.
