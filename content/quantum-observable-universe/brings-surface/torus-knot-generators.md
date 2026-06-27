*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The Euler characteristic $\chi(A) = -6$ of the Bring's surface is
the reason torus knots serve as the generators of the particle
spectrum. Because the Bring's surface has genus $g = 4$
(from $\chi = 2 - 2g = -6$), there is a hard upper bound on
which torus knots can be localized in the fibre: any $T_{m,n}$
whose Seifert genus exceeds $4$ cannot embed. This
constraint selects a finite, enumerable generator set
$\mathcal{G}$ ([knot-particle generation](#def:knot-particle-generation))
whose cardinality is entirely determined by $\chi$.

**Proposition.**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe with
$\chi(A) = -6$ (Descartes universe). The torus knot $T_{m,n}$
with $\gcd(m,n) = 1$ and $m < n$ embeds into the Seifert genus-$g$
surface of $A$ only if the Seifert genus satisfies

$$
  g(T_{m,n}) =  \frac{(m-1)(n-1)}{2}  \leq  g(A) =  4.
$$

The constraint $(m-1)(n-1) \leq 8$ admits exactly six coprime pairs
with $m \geq 2$, tabulated in
[Table: Torus-knot generators](#tbl:torus-knot-generators-table-data).
Together with the unknot $T_{1,0} = 0_1$ (genus $0$), the generator
set has $|\mathcal{G}| = 7$.

**Genus bound from $\chi(A) = -6$.**
The Bring's surface $\Sigma_4$ has genus $g = 4$ and Euler
characteristic $\chi = 2 - 2g = -6$. A knot $T_{m,n}$ localized
in the fibre $\mathcal{S}_c$
([localized knot](#def:localized-knot)) inherits a Seifert surface
that must embed in the genus-$4$ handlebody provided by $\Sigma_4$.
The Seifert genus of $T_{m,n}$ is $(m-1)(n-1)/2$, so
embeddability requires $(m-1)(n-1) \leq 2g = 8$.
