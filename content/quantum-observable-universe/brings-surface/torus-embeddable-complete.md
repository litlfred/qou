*Lean sibling: archimedean specialisation over $\mathbb{R}$ (AGENTS.md §7c). Underlying combinatorial content stays generic to any commutative ring with the same $q$-data.*

The generator set $\mathcal{G}$
([finiteness of generators](#prop:torus-knot-generators)) is not only
a convenient choice — it is the *complete* list of torus knots
embeddable in the genus-$4$ fiber of the Bring's surface.

**Proposition.**
Let $T_{m,n}$ be a torus knot with $\gcd(m,n) = 1$ and $1 < m < n$.
Then $T_{m,n}$ embeds in the Seifert genus-$4$ surface $\Sigma_4$ of
the Bring's surface if and only if $(m,n)$ belongs to the set

$$
  \{(2,3),(2,5),(2,7),(2,9),(3,4),(3,5)\}.
$$

Together with the unknot $T_{1,0}$, these are the only torus knots
that can appear as localized knots in the Descartes universe.

**Proof.**
The Seifert genus of $T_{m,n}$ is $g(T_{m,n}) = (m-1)(n-1)/2$.
Embeddability requires $g(T_{m,n}) \leq g(\Sigma_4) = 4$, i.e.,
$(m-1)(n-1) \leq 8$. We enumerate all coprime pairs $(m,n)$ with
$1 < m < n$ satisfying this bound:

- **$m = 2$:** $(2-1)(n-1) = n-1 \leq 8$, so $n \leq 9$.
 Odd coprime values: $n \in \{3, 5, 7, 9\}$.

- **$m = 3$:** $(3-1)(n-1) = 2(n-1) \leq 8$, so $n \leq 5$.
 Coprime to $3$: $n \in \{4, 5\}$.

- **$m = 4$:** $(4-1)(n-1) = 3(n-1) \leq 8$, so $n \leq 3$.
 But $m < n$ requires $n \geq 5$; no solution.

- **$m \geq 5$:** $(m-1)(n-1) \geq 4 \cdot m > 8$ for $n > m \geq 5$;
 no solution.

This exhausts all cases. The six nontrivial torus knots listed above,
together with the unknot, form the complete set of torus knots
embeddable in $\Sigma_4$. No torus knot outside $\mathcal{G}$ admits
a localized knot structure in the Descartes universe. $\square$

**Remark.**
The completeness is purely number-theoretic: it depends only on the
Diophantine constraint $(m-1)(n-1) \leq 2g$ with a coprimality
condition. For any QOU with fiber genus $g'$, an analogous finite
enumeration determines the torus knot generator set. The Descartes
value $g = 4$ is the *smallest* genus that accommodates all three
lepton generations (requiring genera $1, 2, 3$) plus a non-trivial
quark sector (requiring $m = 3$ generators).
