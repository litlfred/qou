**Proof.**
The coface maps are composites of the jet prolongation with the
Cech face maps $\partial^i$ of the cover $\{U_i\}$.  The
codegeneracy maps are composites of the :refterm[descent]{#descent} homomorphism with the
Cech degeneracy maps $s^j$.  The identities
$\delta^j \circ \delta^i = \delta^i \circ \delta^{j-1}$ for $i < j$
and $\sigma^j \circ \sigma^i = \sigma^i \circ \sigma^{j+1}$ for $i \leq j$
follow from the functoriality of jet prolongation and :refterm[descent]{#descent}: the ascent
$\ell_n$ is a natural transformation from the identity functor on
$\mathfrak{G}_n$ to the restriction of $\mathfrak{G}_{n+1}$, and the
:refterm[descent]{#descent} $\mathfrak{d}_{n+1}$ is its left adjoint.  The mixed identity
$\sigma^j \circ \delta^i$ reduces to three cases
($i < j$, $i = j$ or $i = j + 1$, $i > j + 1$), each verified using
the retraction property $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$
([:refterm[descent]{#descent}](#lem\:descent)).

For concreteness, the case $i < j$ proceeds as follows.  The coface
$\delta^i$ inserts $\ell_n$ at position $i$, while the codegeneracy
$\sigma^j$ composes with $\mathfrak{d}_{n+1}$ at position $j$.  Since
$i < j$, the two operations act on disjoint positions, so

$$
  \sigma^j \circ \delta^i
  = (\mathrm{id} \otimes \cdots \otimes \mathfrak{d}_{n+1}^{(j)}
     \otimes \cdots) \circ
    (\mathrm{id} \otimes \cdots \otimes \ell_n^{(i)} \otimes \cdots)
  = \delta^i \circ \sigma^{j-1},
$$

where the re-index $j \mapsto j - 1$ accounts for the inserted
position.  The retraction property is used only indirectly via the
functoriality of $\ell_n$ and $\mathfrak{d}_{n+1}$.  The case
$i = j$ uses the retraction directly:
$\sigma^i \delta^i = \mathfrak{d}_{n+1} \ell_n = \mathrm{id}$.  The
case $i = j + 1$ is symmetric.  The case $i > j + 1$ is dual to
$i < j$ by swapping roles.  All four identities thus reduce either
to disjoint-support commutation or to the retraction.  $\square$
