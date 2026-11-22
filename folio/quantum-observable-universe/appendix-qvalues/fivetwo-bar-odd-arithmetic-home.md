The bar involution $q \mapsto q^{-1}$ acts on the three embeddings of the $5_2$
trace field by exchanging the complex-conjugate pair $\xi_1 \leftrightarrow
\bar{\xi_1}$ and fixing the real embedding $\xi_3$. That single observation
fixes where a bar-odd datum can live, and it is stated separately from the
identity it follows from.

## The even and odd channels are geometrically distinguishable

Write $P$ for any quantity attached to an embedding — a shape, a series
coefficient, a period. The two combinations

$$
P^{\mathrm{even}} = P(\xi_1) + P(\bar{\xi_1}), \qquad
P^{\mathrm{odd}} = P(\xi_1) - P(\bar{\xi_1})
$$

behave differently under the bar. The even combination is real and is what a
Galois trace over the conjugate pair sees; the odd combination is purely
imaginary and lies on the $\sqrt{-23}$ axis of $K \otimes \mathbb{C}$, since
$\sqrt{-23}$ generates the quadratic resolvent that $A_3$ fixes.

**The bar-even channel is the
one a symmetric pairing can reach; the bar-odd channel is confined to a single
line, and that line is determined by the discriminant of the trace field.**

## Why $5_2$ rather than $4_1$

For an amphichiral knot the mirror is the knot itself, so the Jones polynomial
satisfies $J_{K^{*}}(q) = J_K(q^{-1}) = J_K(q)$ and the bar-odd part vanishes
identically. The figure-eight $4_1$ is amphichiral; its bar-odd channel is
empty for a structural reason.

$5_2$ is chiral. Its bar-odd channel is not forced to vanish, which is why it is
the knot the odd-channel question has to be asked on. The trace-field degree
tracks the same distinction: $4_1$ has the quadratic $\mathbb{Q}(\sqrt{-3})$ and
$5_2$ the cubic of discriminant $-23$, with a genuine complex-conjugate pair to
separate.

## What is and is not settled

Settled: the *location*. Any bar-odd datum assembled from the conjugate pair
lies on the $\sqrt{-23}$ line. This is a consequence of the field structure
alone and needs no analytic input.

Not settled: the *value*. Locating the line does not evaluate anything on it,
and no bar-odd action value is asserted here or in the propositions this remark
interprets. The sum rule
([The $5_2$ saddle sum rule](#prop:fivetwo-saddle-sum-rule)) is symmetric in
the conjugate pair and therefore bar-even; it constrains the even channel and
leaves the odd one open.

## Alexander layer versus geometric layer

The bar-odd channel's arithmetic home is not $\mathbb{Q}(\sqrt{-7})$, the
field one would infer from $\det(5_2) = 7$. That is the Alexander layer, not
the geometric one, and it cannot be a subfield of a cubic. The line is
$\sqrt{-23}$, already visible in the $\sigma$-pair data.

The lesson generalises to a question to ask of any such claim: *which layer of
the knot is this field attached to?* Abelian invariants — the
determinant, the Alexander polynomial, the branched cover — carry one field;
the geometric $\mathrm{SL}_2(\mathbb{C})$ representation carries another. They
coincide for no general reason.
