
The algebra $\mathcal{A}_\infty$ is the direct limit of the fibre algebras
$\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$
([direct limit algebra](#def:direct-limit-algebra)), each of which is a
$C^*$-algebra carrying a continuous $\mathrm{SU}(2)$ action by automorphisms.

*Existence.*
At each finite level $n$ the algebra
$\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$ is a type-I $C^*$-algebra
(it is a section algebra of a locally trivial bundle with compact fibre).
By compactness of $\mathrm{SU}(2)$, averaging any state $\psi_n$ over the
Haar measure $\mu$ produces an $\mathrm{SU}(2)$-invariant state:
$$
  \omega_n(a)
  \;=\;
  \int_{\mathrm{SU}(2)} \psi_n(g \cdot a)\; d\mu(g).
$$
The descent homomorphisms $\mathfrak{d}_n$ ([descent](#lem:descent)) are
equivariant and surjective, so the invariant states $\{\omega_n\}$ form a
compatible system.  By the universal property of the direct limit, they
determine a state $\omega$ on $\mathcal{A}_\infty$ satisfying
$\omega(g \cdot a) = \omega(a)$.

*Uniqueness.*
The vanishing condition
$\mathrm{Hom}(\mathbf{1}, \mathrm{Ad}(A)) = 0$ of the quantum observable
universe axioms implies that the trivial representation appears with
multiplicity one in each $\Gamma(J^1 E_n,\, \mathrm{SU}_{q_n}(2))$ (it
occurs only in the scalar summand $\mathbb{C} \cdot \mathbf{1}$).  Any
$\mathrm{SU}(2)$-invariant state must factor through the projection onto
this trivial isotypic component, which is one-dimensional.  Hence
$\omega$ is the unique such state.
