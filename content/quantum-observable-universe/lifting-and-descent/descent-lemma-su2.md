Continuing the [brane tower for SU(2)](#ex\:recursive-brane-tower-su2),
we verify the [:refterm[descent]{#descent} lemma](#lem\:descent) at the first level.

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
