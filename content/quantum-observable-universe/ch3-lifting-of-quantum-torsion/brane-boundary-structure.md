The defining boundary $\partial A_n$
([Definition](#def:brane-boundary)) has the following properties:

1. *Codimension.*  In the archimedean realisation,
   $\partial A_n$ corresponds to a closed subset of real codimension at
   least 2 in $E_n$.
2. *Exceptional object.*  At each degeneration locus of the
   restriction $r_n$, the kernel $\ker(r_n|_S)$ is isomorphic to a
   simple object of $\mathcal{C}$; in the archimedean realisation
   this is $\mathbb{P}^1(\mathbb{C}) \cong S^2$, the exceptional divisor of the
   topological blow-up.
3. *Involution symmetry.*  The descent involution $\tau_n$
   ([Definition](#def:descent-involution)) restricts to an
   endomorphism of $\partial A_n$, whose fixed subobjects coincide
   with the monodromy fixed points of the quantum characteristic
   classes ([Definition](#def:quantum-characteristic-classes)).
4. *Chirality interface (archimedean realisation).*
   When $n = 1$, $\partial E_1$ separates the macroscopic spacetime
   coordinates from the internal chiral modes: it is the geometric
   boundary between the base manifold $M$ and the gauge fibre, across
   which the Reeb involution $\xi \mapsto -\xi$
   ([Remark](#rem:descartes-chirality)) reverses orientation.

---

*(1).* The descent map $\mathfrak{d}_{n+1}$ is a surjective
$*$-homomorphism of fibre algebras ([Lemma](#lem:descent)).  Its kernel at a
generic point is zero because the ascent $\ell_n$ embeds $A$ as a direct
summand of $J^1(A)$ and the restriction $r_n$ is the left-inverse of this
embedding.  The kernel becomes non-trivial only where the direct-summand
splitting degenerates, which is a closed algebraic condition on the
Frobenius pairing $\varepsilon \circ m$.  Since $A$ is a Frobenius--Hopf
object in a rigid monoidal category, this degeneracy locus has real
codimension at least 2 by the standard codimension bound for degeneracy loci
of morphisms between vector bundles of equal rank.

*(2).* At a blow-up centre $p \in \partial E_n$ the kernel of
$r_n|_p$ is the fibre of $\Omega^1(A)$ over $p$ modulo the image of
$\eta\colon \mathbf{1} \to A$.  Since
$\Omega^1(A) \hookrightarrow A \otimes A$ and $A$ has fibre
$\mathrm{SU}(2)$, the quotient is isomorphic to the projectivisation of
the $2$-dimensional representation, i.e.
$\mathbb{P}^1(\mathbb{C}) \cong S^2$.  This is the exceptional divisor introduced
by the topological blow-up that resolves the singularity at $p$.

*(3).* The descent involution $\tau_n = \ell_n \circ \mathfrak{d}_{n+1}$
([Definition](#def:descent-involution)), acting on sections of
$J^1 E_{n+1}$, restricts to the boundary locus $\partial E_n$ as follows.
Since $\partial E_n$ is defined by $\ker(\mathfrak{d}_{n+1}|_p) \neq 0$,
and $\tau_n$ projects onto the image of $\ell_n$, the restriction
$\tau_n|_{\partial E_n}$ acts as an involution whose fixed points are
the sections at boundary points that are entirely in the descended
subalgebra---precisely the monodromy fixed-point condition that
defines the quantum characteristic classes
([Definition](#def:quantum-characteristic-classes)).

*(4).* At $n = 1$ the base manifold is $M$ and the total space
$E_1$ fibres over $M$ with fibre $\mathrm{SU}(2)/\mathrm{U}(1) \cong S^2$.
The defining boundary $\partial E_1$ is the locus where the jet
restriction degenerates; by item (2) each fibre of $\partial E_1$ is
$\mathbb{P}^1(\mathbb{C})$, which separates the base (spacetime) coordinates from the
fibre (chiral) coordinates.  The Reeb vector field $\xi$ is vertical, so
its reversal $\xi \mapsto -\xi$ exchanges the two sides of $\partial E_1$:
one side carries left-handed fermions (positive Reeb eigenspace), the other
right-handed (negative eigenspace), in agreement with
[Remark](#rem:descartes-chirality).
