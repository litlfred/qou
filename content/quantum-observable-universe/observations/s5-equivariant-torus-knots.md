**Proposition.**
Let $\Sigma$ be a Riemann surface with automorphism group
$\mathrm{Aut}(\Sigma) = S_5$
(the paradigmatic example being [Bring's surface](#def:brings-surface)).
A torus knot $T_{2, s}$ with $s \geq 3$ coprime to $2$ admits an
*equivariant* embedding into $\Sigma$ --- that is, an embedding
preserving its intrinsic cyclic symmetry $\mathbb{Z}_s$ --- if and
only if

$$
  s  \in  \{3,\, 5\}.
$$

*Proof.*
An equivariant embedding requires $\mathbb{Z}_s \hookrightarrow \mathrm{Aut}(\Sigma) = S_5$,
since the knot's cyclic symmetry must be realised by a
symmetry of the ambient surface.  An injection
$\mathbb{Z}_s \hookrightarrow S_5$ exists iff $S_5$ has an
element of order $s$, i.e.\ iff $s$ is the order of some
permutation in $S_5$.  The orders of elements of $S_5$ are the
least common multiples of the parts of the five-element
partitions:

| Cycle type | Order |
|------------|:-----:|
| $(1)^5$ | $1$ |
| $(2)(1)^3$ | $2$ |
| $(2)^2(1)$ | $2$ |
| $(3)(1)^2$ | $3$ |
| $(3)(2)$ | $6$ |
| $(4)(1)$ | $4$ |
| $(5)$ | $5$ |

so the orders realised in $S_5$ are $\{1, 2, 3, 4, 5, 6\}$.
Restricting to odd $s \geq 3$ (forced by $\gcd(2, s) = 1$)
leaves $\{3, 5\}$.  $\square$

**Corollary.**  Among torus knots of the form $T_{2, s}$ with
$s \geq 3$, exactly two --- $T_{2, 3}$ and $T_{2, 5}$ --- admit
embeddings into $\Sigma_4$ (Bring's surface) that preserve the
cyclic rotational symmetry of the knot.  Every other torus
knot of this family either breaks the symmetry in the embedding
or fails to embed topologically (the latter occurring for Seifert
genus $> 4$, i.e.\ $s \geq 11$).

**Comparison with genus-based embedding.**  Pure topological
(Seifert-genus) embedding into $\Sigma_4$ admits $T_{2, 3}$,
$T_{2, 5}$, $T_{2, 7}$, $T_{2, 9}$ but excludes $T_{2, 11}$ ---
four knots survive the genus filter.  The stronger
equivariant criterion of the present proposition keeps only
$T_{2, 3}$ and $T_{2, 5}$; $T_{2, 7}$ and $T_{2, 9}$ are
topologically admissible but symmetry-broken.
Interpretation for the paper's particle spectrum is given in
[rem:symmetry-preserving-leptons](#rem:symmetry-preserving-leptons).
