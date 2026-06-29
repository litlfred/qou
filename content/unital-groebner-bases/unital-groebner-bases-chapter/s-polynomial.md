Let $R$, $A$, and $(B, <)$ be as in the
[Gröbner--Shirshov basis](#def:groebner-basis) definition.

For $f, f' \in A$, an **$S$-polynomial** is
constructible about $f$ and $f'$ if there exist
$u, u', v, v' \in B$, $\lambda, \lambda' \in R^*$ such that

$$
  \lambda\,\mathrm{LT}(u \cdot \mathrm{LT}(f) \cdot v)
  = \lambda'\,\mathrm{LT}(u' \cdot \mathrm{LT}(f') \cdot v').
$$

In this case,

$$
  S(f, f') := \lambda\, u \cdot f \cdot v
    - \lambda'\, u' \cdot f' \cdot v'.
$$
