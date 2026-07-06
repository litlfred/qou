*(1).* The :refterm[descent]{#descent} map $\mathfrak{d}_{n+1}$ is a surjective
$*$-homomorphism of fibre algebras ([:refterm[descent]{#descent}](#lem:descent)).  Its kernel at a
generic point is zero because the ascent $\ell_n$ embeds $A$ as a direct
summand of $J^1(A)$ and the restriction $r_n$ is the left-inverse of this
embedding.  The kernel becomes non-trivial only where the direct-summand
splitting degenerates, which is a closed algebraic condition on the
[Frobenius pairing](#def:frobenius-pairing) $\varepsilon \circ m$.  Since $A$ is a Frobenius--Hopf
object in a rigid :refterm[monoidal category]{#monoidal-category}, this degeneracy locus has real
codimension at least 2 by the standard codimension bound for degeneracy loci
of morphisms between vector bundles of equal rank.

*(2).* At a blow-up centre $p \in \partial \mathcal{S}_n$ the kernel of
$r_n|_p$ is the fibre of $\Omega^1(A)$ over $p$ modulo the image of
$\eta\colon \mathbf{1} \to A$.  Since
$\Omega^1(A) \hookrightarrow A \otimes A$ and $A$ has fibre
$\mathrm{SU}(2)$, the quotient is isomorphic to the projectivisation of
the $2$-dimensional representation, i.e.
$\mathbb{P}^1(\mathbb{C}) \cong S^2$.  This is the exceptional divisor introduced
by the topological blow-up that resolves the singularity at $p$.

*(3).* The :refterm[descent]{#descent} involution $\hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1}$
([:refterm[descent]{#descent} involution](#def:descent-involution)), acting on sections of
$J^1 \mathcal{S}_{n+1}$, restricts to the boundary locus $\partial \mathcal{S}_n$ as follows.
Since $\partial \mathcal{S}_n$ is defined by $\ker(\mathfrak{d}_{n+1}|_p) \neq 0$,
and $\hat{\tau}_n$ projects onto the image of $\ell_n$, the restriction
$\hat{\tau}_n|_{\partial \mathcal{S}_n}$ acts as an involution whose fixed points are
the sections at boundary points that are entirely in the descended
subalgebra---precisely the monodromy fixed-point condition that
defines the
([quantum characteristic classes](#def:quantum-characteristic-classes)).

*(4).* At $n = 1$ the base manifold is $M$ and the total space
$\mathcal{S}_1$ fibres over $M$ with fibre $\mathrm{SU}(2)/\mathrm{U}(1) \cong S^2$.
The defining boundary $\partial \mathcal{S}_1$ is the locus where the jet
restriction degenerates; by item (2) each fibre of $\partial \mathcal{S}_1$ is
$\mathbb{P}^1(\mathbb{C})$, which separates the base (spacetime) coordinates from the
fibre (chiral) coordinates.  The Reeb vector field $\xi$ is vertical, so
its reversal $\xi \mapsto -\xi$ exchanges the two sides of $\partial \mathcal{S}_1$:
one side carries left-handed fermions (positive Reeb eigenspace), the other
The right-handed (negative eigenspace), in agreement with
[Descartes chirality](#rem:archimedean-chirality).
