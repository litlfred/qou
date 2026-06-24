The argument proceeds in two steps.

*Step 1: Reachability from the unknot.*
Every knot $K$ has a finite unknotting number $u(K)$ — the minimum
number of crossing changes needed to convert $K$ into the unknot
$0_1 = T_{1,0}$.  Since crossing changes are involutions (each change
is its own inverse), the same $u(K)$ crossing changes applied to
$T_{1,0}$ produce $K$.  Because $T_{1,0} \in \mathcal{G}$, the knot
$K$ is reachable from $\mathcal{G}$ by at most $u(K)$ Skein
operations.

*Step 2: The spectral filter selects genus $\leq 4$.*
Not every knot reachable from $T_{1,0}$ by crossing changes has
genus $\leq 4$ — intermediate steps may pass through arbitrarily
high genus.  However, the Bring's surface imposes a spectral filter:
in the Skein module $\mathrm{Sk}_q(\mathbf{C})$, the mass functional
$\mathcal{M} \colon \mathrm{Sk}_q \to \mathbb{R}_{\geq 0}$ annihilates
any term whose knot type has $g > 4$
([embeddability closure](#thm:embeddability-closure)).  The physical
content of the Skein resolution is the projection onto the submodule
spanned by knots with $g(K) \leq 4$.

The composition of Steps 1 and 2 gives: for any knot $K$ with
$g(K) \leq 4$, there exists a finite sequence of Skein crossing
changes $\sigma_1, \ldots, \sigma_r$ (with $r \leq u(K)$) such that
$K$ appears with nonzero coefficient in the Skein expansion of
$\sigma_r \circ \cdots \circ \sigma_1(T_{1,0})$, and $K$ passes the
spectral filter since $g(K) \leq 4$.
$\qquad\blacksquare$
