Continuing [Frobenius $\mathrm{SU}(2)$](#ex:frobenius-su2), the category
$\mathbf{C} = \mathrm{Rep}(\mathrm{SU}(2))$ carries a canonical
involutive structure built from the antipode:

- *What it does.* For a morphism $f \colon V_j \to V_k$
  (an equivariant linear map between representations),
  $f^{\dagger}$ is the *Hilbert-space adjoint*: the unique
  map $f^{\dagger} \colon V_k \to V_j$ satisfying
  $\langle f^{\dagger}(w), v \rangle_j = \langle w, f(v) \rangle_k$
  for all $v \in V_j$, $w \in V_k$.
- *Why it exists.* Each irreducible representation $V_j$
  carries a unique (up to scalar) $\mathrm{SU}(2)$-invariant
  inner product. The adjoint $f^{\dagger}$ with respect to
  these inner products is automatically equivariant, so
  $f^{\dagger}$ is again a morphism in $\mathbf{C}$.
- *On the algebra.* On $A = \mathcal{O}(\mathrm{SU}(2))$,
  $f^{\dagger} = \int_A \circ \mu(S(f) \otimes -)$, where
  $S(f)(g) = f(g^{-1})$ is the antipode. The involution
  $f \mapsto f^{\dagger}$ is complex conjugation composed with
  pullback by inversion: $f^{\dagger}(g) = \overline{f(g^{-1})}$.
- *Positive-definiteness.* For a non-zero state
  $f \colon \mathbb{C} \to V_j$, the composite
  $f^{\dagger} \circ f = \lVert f(1) \rVert^2 > 0$.
  This is the statement that the inner product on each $V_j$ is
  positive-definite --- the categorical encoding of unitarity.
