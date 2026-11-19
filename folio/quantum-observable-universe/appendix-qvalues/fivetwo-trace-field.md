**Proposition.** *Let $R$ be a commutative ring and let $y_1, y_2, y_3 \in R$
satisfy the Vieta relations of the $5_2$ saddle cubic,*

$$
y_1 + y_2 + y_3 = 2, \qquad
y_1y_2 + y_1y_3 + y_2y_3 = 3, \qquad
y_1y_2y_3 = 1 .
$$

*Then their discriminant is*

$$
\bigl((y_1 - y_2)(y_1 - y_3)(y_2 - y_3)\bigr)^{2} \;=\; -23 .
$$

Consequently the invariant trace field of the $5_2$ knot (the field generated
by the shapes of its three ideal tetrahedra) is the **cubic field of
discriminant $-23$**, $K = \mathbb{Q}[\xi]$ with
$\xi^{3} - 2\xi^{2} + 3\xi - 1 = 0$.

## Formulation over a generic commutative ring

The discriminant identity is an algebraic consequence of the three symmetric
functions and nothing else. It needs no ordering, no square root and no
archimedean construct, so it is stated over a generic commutative ring rather
than over $\mathbb{R}$ or $\mathbb{C}$; the geometric reading in the next
section is the archimedean specialisation rather than the content of the identity.

The proof is Vieta substitution into the symmetric form of the discriminant:
$4\cdot 9 - 4\cdot 27 - 4\cdot 8 + 18\cdot 6 - 27 = -23$.

## The three places, and the shape that is geometric

$K$ has one real embedding and one complex-conjugate pair. Numerically the
three roots of $\xi^{3} - 2\xi^{2} + 3\xi - 1$ are

$$
\xi_{1} \approx 0.78492 + 1.30714\,i, \qquad
\xi_{2} = \bar{\xi_{1}}, \qquad
\xi_{3} \approx 0.43016 ,
$$

and $\xi_1$ is the geometric solution: the one whose shapes have positive
imaginary part and reproduce
$\mathrm{Vol}(5_2) \approx 2.82812$. The reciprocal cubic
$1 - 2z + 3z^{2} - z^{3}$ and the Landen image $z^{3} - z^{2} + 1$ generate the
same field, being related to the above by rational maps; each has discriminant
$-23$.

Among complex cubic fields, $-23$ is the smallest discriminant in absolute
value.

## The one quadratic attached to $K$

$K$ is not Galois. Its Galois closure has group $S_3$, whose unique index-$2$
subgroup $A_3$ fixes exactly one quadratic field, the quadratic resolvent
$\mathbb{Q}(\sqrt{\mathrm{disc}\,K}) = \mathbb{Q}(\sqrt{-23})$. Since
$-23$ is squarefree this is the whole of it: **$\mathbb{Q}(\sqrt{-23})$ is the
only quadratic field attached to the $5_2$ trace field.**

This matters because the bar involution separates the conjugate pair
$\xi_1, \bar{\xi_1}$, so any bar-odd datum built from the two complex
embeddings lands on the $\sqrt{-23}$ line, the structural analogue of the
$\mathbb{Q}(\sqrt{-3})$ line for the amphichiral $4_1$.

## Independence of the trace field from the knot determinant

$\det(5_2) = 7$, and the Alexander polynomial
$\Delta_{5_2}(t) = 2t^{2} - 3t + 2$ has discriminant $-7$ with roots
$(3 \pm i\sqrt{7})/4$. So $\mathbb{Q}(\sqrt{-7})$ *is* genuinely attached to
$5_2$, as the **Alexander root field**, equivalently the quadratic subfield of
$\mathbb{Q}(\zeta_7)$, where the abelian data of the $\mathbb{Z}/7$ double
branched cover lives.

It is not the geometric trace field, and it cannot be a subfield of one:
$[\mathbb{Q}(\sqrt{-7}):\mathbb{Q}] = 2$ does not divide $[K:\mathbb{Q}] = 3$,
so the tower law forbids the embedding outright. The two fields belong to
different layers of the knot, and reading the geometric field off the
determinant conflates them.
