<!-- FILE_START: sdescent-prelim-intro.md -->
We define how structure restricts from $A_{n+1}$ to $A_n$ in the brane tower. We show the restriction map $r_n \colon A_n \to A_{n-1}$ induces a surjective algebra homomorphism $\mathfrak{d}_n$ on the endomorphism algebras. This map intertwines the $G_q$-actions. Each descending level inherits the complete quantum observable universe (QOU) structure. We compose ascent and descent to define the idempotent descent involution $\hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1}$. Its image isolates the descended subalgebra within $\mathrm{End}_{\mathbf{C}}(A_{n+1})$. We compute both mechanisms in the $\mathrm{SU}(2)$ archimedean model. The Yekutieli lifting obstruction calculus requires both the descent involution and the surjectivity of $\mathfrak{d}_n$.
<!-- FILE_END: sdescent-prelim-intro.md -->

<!-- FILE_START: descent-lemma.md -->
**Lemma (Descent preserves QOU).**
Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $\{A_n\}_{n \geq 0}$ be the [recursive brane tower](#def:recursive-brane-tower) for $n \geq 1$. Let $q$ denote the substrate parameter. The restriction morphism $r_n \colon A_n \to A_{n-1}$ produces a Frobenius–Hopf object $A_{n-1}$ such that $(\mathbf{C}, A_{n-1}, \tau)$ is a quantum observable universe.

The induced descent homomorphism
$$
  \mathfrak{d}_n \colon \mathrm{End}_{\mathbf{C}}(A_n) \longrightarrow \mathrm{End}_{\mathbf{C}}(A_{n-1})
$$
is a surjective algebra homomorphism. It intertwines the $G_q$-actions across levels $n$ and $n-1$.

In the archimedean realisation, this recovers the surjective $*$-homomorphism $\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2)) \to \Gamma(J^1 \mathcal{S}_{n-1}, \mathrm{SU}_{q_{n-1}}(2))$.
<!-- FILE_END: descent-lemma.md -->

<!-- FILE_START: descent-lemma-su2.md -->
We verify the [descent lemma](#lem:descent) at the first level for the [brane tower for SU(2)](#ex:recursive-brane-tower-su2).

**The descent map.** The descent $\mathfrak{d}_1 \colon \mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2))) \to \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ sends a jet-level endomorphism to its base-level shadow by averaging over the cotangent fibre directions.

**Dimensions.** The domain has $6$ dimensions. Left-invariant vector fields $L_{e_1}, L_{e_2}, L_{e_3}$ span the $3$ base dimensions. The $T^*\mathrm{SU}(2)$ fibre spans the $3$ cotangent dimensions. The codomain $\mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ has $3$ dimensions, spanned by the adjoint action of $\mathfrak{su}(2)$.

**Surjectivity.** Every base-level endomorphism $\phi \in \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ lifts to $\tilde{\phi} = \phi \otimes \mathrm{id}_{\Omega^1}$ in $\mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))$. We compute $\mathfrak{d}_1(\tilde{\phi}) = \phi$. The map $\mathfrak{d}_1$ is surjective.

**Equivariance.** The descent map intertwines the $\mathrm{SU}_q(2)$-actions. At $q = 1$, we have:
$$
  \mathfrak{d}_1(g \cdot \phi \cdot g^{-1}) = g \cdot \mathfrak{d}_1(\phi) \cdot g^{-1}, \qquad g \in \mathrm{SU}(2).
$$
At $q \neq 1$, this identity holds under the action of $\mathrm{SU}_q(2)$.
<!-- FILE_END: descent-lemma-su2.md -->

<!-- FILE_START: descent-involution.md -->
**Definition.**
Let $\ell_n \colon A_n \hookrightarrow A_{n+1}$ be the ascent embedding ([jet prolongation](#prop:jet-prolongation)). Let $\mathfrak{d}_{n+1} \colon \mathrm{End}_{\mathbf{C}}(A_{n+1}) \to \mathrm{End}_{\mathbf{C}}(A_n)$ be the descent homomorphism ([descent](#lem:descent)). The *descent involution* at level $n$ is the endomorphism:
$$
  \hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1} \colon \mathrm{End}_{\mathbf{C}}(A_{n+1}) \longrightarrow \mathrm{End}_{\mathbf{C}}(A_{n+1}).
$$
The map $\ell_n$ embeds $A_n$ as a direct summand retracted by $\mathfrak{d}_{n+1}$. We have $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ on $\mathrm{End}_{\mathbf{C}}(A_n)$. Therefore:
$$
  \hat{\tau}_n^2 = \ell_n \circ \mathfrak{d}_{n+1} \circ \ell_n \circ \mathfrak{d}_{n+1} = \ell_n \circ (\mathfrak{d}_{n+1} \circ \ell_n) \circ \mathfrak{d}_{n+1} = \ell_n \circ \mathrm{id} \circ \mathfrak{d}_{n+1} = \hat{\tau}_n.
$$
The map $\hat{\tau}_n$ is an idempotent. Its image is the *descended subalgebra* $\mathcal{A}_{n+1}^{\mathrm{desc}} \subseteq \mathrm{End}_{\mathbf{C}}(A_{n+1})$. This subalgebra contains the level-$(n+1)$ endomorphisms that factor through the level-$n$ algebra via ascent.
<!-- FILE_END: descent-involution.md -->

<!-- FILE_START: descent-involution-su2.md -->
We construct the [descent involution](#def:descent-involution) on $\mathrm{End}_{\mathbf{C}}(A_1)$ for $A_1 = J^1\mathcal{O}(\mathrm{SU}(2))$ ([jet prolongation for SU(2)](#ex:jet-prolongation-su2)).

**The endomorphism algebra.** The space $A_1 \cong \mathcal{O}(\mathrm{SU}(2)) \otimes \mathrm{span}\{\omega_1, \omega_2, \omega_3\}$. The endomorphism algebra $\mathrm{End}_{\mathbf{C}}(A_1)$ has $6$ dimensions: $3$ from the base $\mathrm{SU}(2)$ and $3$ from the cotangent fibre.

**Definition.** The descent involution $\hat{\tau}_1$ on $\mathrm{End}_{\mathbf{C}}(A_1)$ is the composition $\hat{\tau}_1 = \ell \circ \mathfrak{d}$. The map $\mathfrak{d}$ is descent, averaging over $\mathrm{U}(1)$-orbits in the Hopf fibration $\mathrm{SU}(2) \to \mathbb{CP}^1$. The map $\ell$ is ascent, the jet prolongation of the descended endomorphism.

**Idempotence.** Descent averages the $\mathrm{U}(1)$ action. Ascent embeds the result. We obtain $\hat{\tau}_1^2 = \hat{\tau}_1$. For $\phi \in \mathrm{End}_{\mathbf{C}}(A_1)$, we compute:
$$
  \hat{\tau}_1(\phi)(f \otimes \omega_a) = \frac{1}{2\pi} \int_0^{2\pi} \phi\bigl(e^{i\varTheta} \cdot (f \otimes \omega_a)\bigr) d\varTheta,
$$
where $e^{i\varTheta}$ acts via the maximal torus $\mathrm{U}(1) \hookrightarrow \mathrm{SU}(2)$. The fixed-point set $\mathrm{End}_{\mathbf{C}}(A_1)^{\hat{\tau}_1}$ contains exactly the $\mathrm{U}(1)$-equivariant endomorphisms.
<!-- FILE_END: descent-involution-su2.md -->
