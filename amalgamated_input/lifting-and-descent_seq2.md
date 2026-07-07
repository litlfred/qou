<!-- FILE_START: sdescent-prelim-intro.md -->
With the brane tower in hand, we can ask what structure passes from $A_{n+1}$ back down to $A_n$. Lemma: Descent preserves the quantum observable universe shows that the restriction $r_n \colon A_n \to A_{n-1}$ induces a surjective algebra homomorphism $\mathfrak{d}_n$ on endomorphism algebras that intertwines the $G_q$-actions, so each level inherits the full QOU structure. Definition: Descent involution then composes ascent and descent into the idempotent $\hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1}$, whose image cuts out the descended subalgebra inside $\mathrm{End}_{\mathbf{C}}(A_{n+1})$. The $\mathrm{SU}(2)$ examples pin both constructions to the archimedean model. The Yekutieli-lifting section that follows takes the descent involution and the surjectivity of $\mathfrak{d}_n$ as inputs to the obstruction calculus.

_(draft.)_
<!-- FILE_END: sdescent-prelim-intro.md -->

<!-- FILE_START: descent-lemma.md -->
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe and let
$\{A_n\}_{n \geq 0}$ be the
([recursive brane tower](#def:recursive-brane-tower)), with $n \geq 1$; let $q$ denote the substrate parameter.  The
restriction morphism $r_n \colon A_n \to A_{n-1}$ yields a Frobenius--Hopf
object $A_{n-1}$ such that $(\mathbf{C}, A_{n-1}, \tau)$ is again a
quantum observable universe.  Moreover, the induced :refterm[descent]{#descent} homomorphism

$$
  \mathfrak{d}_n  \colon 
  \mathrm{End}_{\mathbf{C}}(A_n)
   \longrightarrow 
  \mathrm{End}_{\mathbf{C}}(A_{n-1})
$$

is a surjective algebra homomorphism that intertwines the $G_q$-actions at
levels $n$ and $n{-}1$.  In the archimedean realisation, this recovers
the surjective $*$-homomorphism
$\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2)) \to \Gamma(J^1 \mathcal{S}_{n-1}, \mathrm{SU}_{q_{n-1}}(2))$.
<!-- FILE_END: descent-lemma.md -->

<!-- FILE_START: descent-lemma-su2.md -->
Continuing the [brane tower for SU(2)](#ex:recursive-brane-tower-su2),
we verify the [:refterm[descent]{#descent} lemma](#lem:descent) at the first level.

**The :refterm[descent]{#descent} map.** The :refterm[descent]{#descent}
$\mathfrak{d}_1 \colon \mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2))) \to \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ sends a jet-level
endomorphism to its base-level shadow by averaging over the cotangent
fibre directions.

**Dimensions.** The domain is $6$-dimensional:
The group $\mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))$ decomposes as
$3$ dimensions for the $\mathrm{SU}(2)$ base directions (spanned by
the left-invariant vector fields $L_{e_1}, L_{e_2}, L_{e_3}$) plus
$3$ dimensions for the cotangent directions (the fibre of
$T^*\mathrm{SU}(2)$). The codomain
$\mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ is $3$-dimensional,
spanned by the adjoint action of $\mathfrak{su}(2)$.

**Surjectivity.** Every base-level endomorphism $\phi \in \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ lifts to
$\tilde{\phi} = \phi \otimes \mathrm{id}_{\Omega^1}$ in
$\mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))$, giving
$\mathfrak{d}_1(\tilde{\phi}) = \phi$. Hence $\mathfrak{d}_1$ is
surjective.

**Equivariance.** The :refterm[descent]{#descent} map intertwines the
$\mathrm{SU}_q(2)$-actions: for $q = 1$ (the classical case),

$$
  \mathfrak{d}_1(g \cdot \phi \cdot g^{-1})
  =  g \cdot \mathfrak{d}_1(\phi) \cdot g^{-1},
  \qquad g \in \mathrm{SU}(2).
$$

At $q \neq 1$, the same identity holds with $g$ replaced by the
quantum group action of $\mathrm{SU}_q(2)$, ensuring compatibility with
deformation.
<!-- FILE_END: descent-lemma-su2.md -->

<!-- FILE_START: descent-involution.md -->
Let $\ell_n \colon A_n \hookrightarrow A_{n+1}$ denote the ascent embedding
([jet prolongation](#prop:jet-prolongation)) and
$\mathfrak{d}_{n+1} \colon \mathrm{End}_{\mathbf{C}}(A_{n+1}) \to \mathrm{End}_{\mathbf{C}}(A_n)$ the :defterm[descent]{#descent} homomorphism
([descent](#lem:descent)).  The *descent involution* at level $n$ is
the endomorphism of the level-$(n{+}1)$ endomorphism algebra:

$$
  \hat{\tau}_n =  \ell_n \circ \mathfrak{d}_{n+1}
   \colon 
  \mathrm{End}_{\mathbf{C}}(A_{n+1})
   \longrightarrow 
  \mathrm{End}_{\mathbf{C}}(A_{n+1}).
$$

Since $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ on
$\mathrm{End}_{\mathbf{C}}(A_n)$ (the descent of the ascent recovers the
original endomorphism, because $\ell_n$ embeds $A_n$ as a direct summand of
$A_{n+1}$ and $\mathfrak{d}_{n+1}$ is the retraction), we have

$$
  \hat{\tau}_n^2
  = 
  \ell_n \circ \mathfrak{d}_{n+1} \circ \ell_n \circ \mathfrak{d}_{n+1}
  = 
  \ell_n \circ (\mathfrak{d}_{n+1} \circ \ell_n) \circ \mathfrak{d}_{n+1}
  = 
  \ell_n \circ \mathrm{id} \circ \mathfrak{d}_{n+1}
  = 
  \hat{\tau}_n,
$$

so $\hat{\tau}_n$ is idempotent.  Its image is the
*descended subalgebra* $\mathcal{A}_{n+1}^{\mathrm{desc}} \subseteq \mathrm{End}_{\mathbf{C}}(A_{n+1})$, consisting of endomorphisms at
level $n{+}1$ that factor through the level-$n$ algebra via the ascent
embedding.
<!-- FILE_END: descent-involution.md -->

<!-- FILE_START: descent-involution-su2.md -->
Continuing the [jet prolongation for SU(2)](#ex:jet-prolongation-su2),
we construct the [:refterm[descent]{#descent} involution](#def:descent-involution) on
$\mathrm{End}_{\mathbf{C}}(A_1)$ where
$A_1 = J^1\mathcal{O}(\mathrm{SU}(2))$.

**The endomorphism algebra.** Since
$A_1 \cong \mathcal{O}(\mathrm{SU}(2)) \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$,
the endomorphism algebra $\mathrm{End}_{\mathbf{C}}(A_1)$ is
$6$-dimensional: $3$ dimensions from the base $\mathrm{SU}(2)$
directions and $3$ from the cotangent fibre directions.

**Definition.** The :refterm[descent]{#descent} involution $\hat{\tau}_1$ on
$\mathrm{End}_{\mathbf{C}}(A_1)$ is the composition
$\hat{\tau} = \ell \circ \mathfrak{d}$, where $\mathfrak{d}$ is the :refterm[descent]{#descent}
map (averaging over $\mathrm{U}(1)$-orbits in the Hopf fibration
$\mathrm{SU}(2) \to \mathbb{CP}^1$) and $\ell$ is the ascent
(jet prolongation of the descended endomorphism).

**Idempotence.** Since :refterm[descent]{#descent} is averaging over the $\mathrm{U}(1)$
action and ascent re-embeds the result, we have $\hat{\tau}^2 = \hat{\tau}$. That
is, $\hat{\tau}$ is a projection, not only an involution of order $2$.
Explicitly, for $\phi \in \mathrm{End}_{\mathbf{C}}(A_1)$,

$$
  \hat{\tau}(\phi)(f \otimes \omega_a)
  =  \frac{1}{2\pi} \int_0^{2\pi}
  \phi\bigl(e^{i\varTheta} \cdot (f \otimes \omega_a)\bigr) d\varTheta,
$$

where $e^{i\varTheta}$ acts via the $\mathrm{U}(1) \hookrightarrow \mathrm{SU}(2)$
maximal torus. The fixed-point set $\mathrm{End}_{\mathbf{C}}(A_1)^{\hat{\tau}}$
consists of the $\mathrm{U}(1)$-equivariant endomorphisms.
<!-- FILE_END: descent-involution-su2.md -->

