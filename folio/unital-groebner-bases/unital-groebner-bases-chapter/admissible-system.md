A *monomial ordering* for a [monomial basis](#def:monomial-basis)
$B$ of an algebra $A$ is a well-ordering $<$ on $B$ such that for
$b, b', r, s \in B$:

1. If $b < b'$ then $r \cdot b \cdot s < r \cdot b' \cdot s$
   whenever $r \cdot b \cdot s \neq 0$ and
   $\mathrm{LM}(r \cdot b' \cdot s) \neq 0$.
2. If $b' = \mathrm{LM}(r \cdot b \cdot s) \neq 0$ with $r$ or
   $s \neq 1$, then $b < \mathrm{LM}(b')$.

If $B$ admits a monomial ordering $<$, then the pair $(B, <)$ is an
**admissible system**.

**Divisibility.** If $(B, <)$ is an admissible system and
$0 \neq f \in A$, we say $\beta \in B$ *divides* $f$ (written
$\beta \mid f$) if there exist $u, v \in B$ and $\lambda \in R^*$
such that

$$
  \lambda\,\mathrm{LT}(u \cdot \beta \cdot v) = \mathrm{LT}(f).
$$
