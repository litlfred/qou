
The Frobenius isomorphism $A \cong A^{\vee}$ sends $a \mapsto \int_A \circ
\mu(a \otimes -)$, which is non-degenerate by the Frobenius--Hopf axiom.

**(1) Embedding via rank-$1$ projectors.**
Let $\rho \colon V \to V$ be a rank-$1$ projector in $\mathbf{C}$:
an endomorphism satisfying $\rho^2 = \rho$ and
$\mathrm{tr}(\rho) = \mathrm{id}_{\mathbf{1}}$ (categorical trace
via evaluation and coevaluation). Since $V$ has categorical
dimension $2$, define the traceless component

$$
  \sigma(\rho) = \rho - \tfrac{1}{2}\,\mathrm{id}_V
  \;\in\; \mathrm{Ad}(A).
$$

This is well-defined because
$\mathrm{tr}(\sigma(\rho)) = 1 - \tfrac{1}{2} \cdot 2 = 0$.
The set of such projectors is precisely
$\mathbb{P}(V) = G/T$, the quotient by the maximal torus.

**(2) The involution.**
Under the positive-definite involutive structure $\dagger$
([involutive structure](#def:involutive-structure)), every rank-$1$
projector satisfies $\rho^{\dagger} = \rho$ (self-adjointness).
Computing the square of the traceless component:

$$
  \sigma(\rho)^2
  = \bigl(\rho - \tfrac{1}{2}\,\mathrm{id}_V\bigr)^2
  = \rho^2 - \rho + \tfrac{1}{4}\,\mathrm{id}_V
  = \tfrac{1}{4}\,\mathrm{id}_V.
$$

Thus $2\sigma(\rho)$ is an involution in $\mathrm{End}(V)$: it
squares to the identity.  Geometrically, $\sigma$ identifies
$\mathbb{P}(V)$ with a coadjoint orbit in $\mathrm{Ad}(A)$. The
orbit is closed by rigidity of $\mathbf{C}$ and determines a
sub-object of $\mathrm{Ad}(A)$ isomorphic to $\mathbb{P}(V)$.
Conversely, given this sub-object, the stabiliser of any point
is $T$, so $\mathbb{P}(V) \cong G/T$ as $G$-spaces.

**(3) Observability.**
Suppose there exists a non-zero morphism
$f \colon \mathbf{1} \to \mathrm{Ad}(A)$.  Such a morphism would
represent a $G$-invariant element in the adjoint representation.
By the SU(2) emergence theorem
([SU(2) emergence](#thm:su2-emergence)), the reconstructed gauge
group is $G \cong \mathrm{SU}(2)$, and $\mathrm{Ad}(A)$ carries
the irreducible adjoint representation $\mathfrak{su}(2)$
(dimension $3$).  By Schur's lemma, the only intertwining morphism
from the trivial representation $\mathbf{1}$ to an irreducible
non-trivial representation is the zero morphism.  Therefore
$f = 0$, contradicting our assumption.

Hence $\mathrm{Hom}(\mathbf{1},\, \mathrm{Ad}(A)) = 0$. The
non-degeneracy of $\int_A$ excludes any hidden global symmetry:
there is no non-trivial invariant section of the adjoint bundle.
