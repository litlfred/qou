**Proposition (genus-$4$ torus knots are exhausted by two pairs).**
*Let $g \in \mathbb{Z}_{\geq 0}$ and consider torus knots $T_{m,n}$
with $2 \leq m \leq n$ and $\gcd(m, n) = 1$.  The genus is
$g(T_{m,n}) = (m-1)(n-1)/2$
([torus knot generators](#prop:torus-knot-generators)).  At $g = 4$
the equation $(m-1)(n-1) = 8$ has exactly two solutions in positive
integers with $m \leq n$ and $\gcd(m, n) = 1$:*

| Solution | $(m, n)$ | crossing number $c = m(n-1)$ | $\gcd(m, n)$ |
|---|---|---|---|
| $(m{-}1,\, n{-}1) = (1,\, 8)$ | $(2,\, 9)$ | $9$ | $1$ (yes) |
| $(m{-}1,\, n{-}1) = (2,\, 4)$ | $(3,\, 5)$ | $10$ | $1$ (yes) |

*Proof.* The Diophantine equation $(m{-}1)(n{-}1) = 8$ with
$1 \leq m{-}1 \leq n{-}1$ admits only the factorisations
$8 = 1 \cdot 8$ and $8 = 2 \cdot 4$.  The remaining $4 \cdot 2$ and
$8 \cdot 1$ violate $m \leq n$ or recover the listed solutions by
the symmetry $T_{m,n} \cong T_{n,m}$.  Coprimality $\gcd(m,n) = 1$
holds in both cases, so $\{T_{2,9},\, T_{3,5}\}$ is the complete
list of genus-$4$ torus knots up to mirror symmetry. $\square$
