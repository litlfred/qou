
We verify the cosimplicial identities and the crossed-module axioms.

*Step 1: Cosimplicial identities.*
The coface maps are composites of the jet prolongation with the
Cech face maps $\partial^i$ of the cover $\{U_i\}$.  The
codegeneracy maps are composites of the descent homomorphism with the
Cech degeneracy maps $s^j$.  The identities
$\delta^j \circ \delta^i = \delta^i \circ \delta^{j-1}$ for $i < j$
and $\sigma^j \circ \sigma^i = \sigma^i \circ \sigma^{j+1}$ for $i \leq j$
follow from the functoriality of jet prolongation and descent: the ascent
$\ell_n$ is a natural transformation from the identity functor on
$\mathfrak{G}_n$ to the restriction of $\mathfrak{G}_{n+1}$, and the
descent $\mathfrak{d}_{n+1}$ is its left adjoint.  The mixed identity
$\sigma^j \circ \delta^i$ reduces to three cases
($i < j$, $i = j$ or $i = j + 1$, $i > j + 1$), each verified using
the retraction property $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$
([descent](#lem:descent)).

For concreteness, the case $i < j$ proceeds as follows. The coface
$\delta^i$ inserts $\ell_n$ at position $i$, while the codegeneracy
$\sigma^j$ composes with $\mathfrak{d}_{n+1}$ at position $j$. Since
$i < j$, the two operations act on disjoint positions, so
$$
  \sigma^j \circ \delta^i
  = (\mathrm{id} \otimes \cdots \otimes \mathfrak{d}_{n+1}^{(j)}
     \otimes \cdots) \circ
    (\mathrm{id} \otimes \cdots \otimes \ell_n^{(i)} \otimes \cdots)
  = \delta^i \circ \sigma^{j-1},
$$
where the re-index $j \mapsto j - 1$ accounts for the inserted
position. The retraction property is used only indirectly via the
functoriality of $\ell_n$ and $\mathfrak{d}_{n+1}$. The case
$i = j$ uses the retraction directly:
$\sigma^i \delta^i = \mathfrak{d}_{n+1} \ell_n = \mathrm{id}$. The
case $i = j + 1$ is symmetric. The case $i > j + 1$ is dual to
$i < j$ by swapping roles. All four identities thus reduce either
to disjoint-support commutation or to the retraction.

*Step 2: Crossed-module structure.*
At each level $n$, the pair
$(\mathrm{SU}_{q_n}(2), \mathcal{O}_M^{\times})$ carries the structure
of a crossed module in the sense of [yekutieli2010]: the boundary
map $\partial \colon \mathcal{O}_M^{\times} \to \mathrm{SU}_{q_n}(2)$
sends a unit $a \in \mathcal{O}_M^{\times}$ to the central element
$a \cdot \mathbf{1} \in \mathrm{SU}_{q_n}(2)$ (the central extension),
and the action of $g \in \mathrm{SU}_{q_n}(2)$ on
$a \in \mathcal{O}_M^{\times}$ is conjugation:
$g \cdot a = g a g^{-1}$.  This action is well-defined because
$\mathcal{O}_M^{\times}$ is central in the gerbe band; the Peiffer
identity $\partial(a) \cdot b = a b a^{-1}$ is automatic for a
central extension.

*Step 3: Compatibility.*
The coface and codegeneracy maps respect the crossed-module structure
because the jet prolongation preserves the Hopf-algebra multiplication
([jet prolongation](#prop:jet-prolongation), Step 2) and the descent
homomorphism is a $*$-homomorphism ([descent](#lem:descent), Step 4).
Hence the conjugation action of $g_{ij}^{(n)}$ on $a_{ij}^{(n)}$ is
compatible with the simplicial maps, making the total assignment a
cosimplicial crossed groupoid.
