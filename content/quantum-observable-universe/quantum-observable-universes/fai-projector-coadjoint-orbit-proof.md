**Proof.**
*(1) Embedding via rank-$1$ projectors.*
Let $\rho \colon V \to V$ be a rank-$1$ projector in $\mathbf{C}$:
an endomorphism satisfying $\rho^2 = \rho$ and
$\mathrm{tr}(\rho) = \mathrm{id}_{\mathbf{1}}$ (categorical trace
via evaluation and coevaluation).  Since $V$ has categorical
dimension $2$, define the traceless component

$$
  \sigma(\rho) = \rho - \tfrac{1}{2}\mathrm{id}_V
   \in  \mathrm{Ad}(A).
$$

This is well-defined because
$\mathrm{tr}(\sigma(\rho)) = 1 - \tfrac{1}{2} \cdot 2 = 0$.
The set of such projectors is precisely
$\mathbb{P}(V) = G/T$, the quotient by the maximal torus.

*(2) The involution.*
Under the positive-definite involutive structure $\dagger$
([involutive structure](#def:involutive-structure)), every rank-$1$
projector satisfies $\rho^{\dagger} = \rho$ (self-adjointness).
Computing the square of the traceless component:

$$
  \sigma(\rho)^2
  = \bigl(\rho - \tfrac{1}{2}\mathrm{id}_V\bigr)^2
  = \rho^2 - \rho + \tfrac{1}{4}\mathrm{id}_V
  = \tfrac{1}{4}\mathrm{id}_V.
$$

Thus $2\sigma(\rho)$ is an involution in $\mathrm{End}(V)$: it
squares to the identity.  Geometrically, $\sigma$ identifies
$\mathbb{P}(V)$ with a coadjoint orbit in $\mathrm{Ad}(A)$.  The
orbit is closed by rigidity of $\mathbf{C}$ and determines a
sub-object of $\mathrm{Ad}(A)$ isomorphic to $\mathbb{P}(V)$.
Conversely, given this sub-object, the stabiliser of any point
is $T$, so $\mathbb{P}(V) \cong G/T$ as $G$-spaces.  $\square$
