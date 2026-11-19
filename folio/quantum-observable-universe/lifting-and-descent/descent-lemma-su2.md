The [descent lemma](#lem:descent) holds at the first level for the [brane tower for SU(2)](#ex:recursive-brane-tower-su2) as follows.

**The descent map.** The descent $\mathfrak{d}_1 \colon \mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2))) \to \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ sends a jet-level endomorphism to its base-level shadow by averaging over the cotangent fibre directions.

**Dimensions.** The domain has $6$ dimensions. Left-invariant vector fields $L_{e_1}, L_{e_2}, L_{e_3}$ span the $3$ base dimensions. The $T^*\mathrm{SU}(2)$ fibre spans the $3$ cotangent dimensions. The codomain $\mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ has $3$ dimensions, spanned by the adjoint action of $\mathfrak{su}(2)$.

**Surjectivity.** Every base-level endomorphism $\phi \in \mathrm{End}(\mathcal{O}(\mathrm{SU}(2)))$ lifts to $\tilde{\phi} = \phi \otimes \mathrm{id}_{\Omega^1}$ in $\mathrm{End}(J^1\mathcal{O}(\mathrm{SU}(2)))$, satisfying $\mathfrak{d}_1(\tilde{\phi}) = \phi$. The map $\mathfrak{d}_1$ is surjective.

**Equivariance.** The descent map intertwines the $\mathrm{SU}_q(2)$-actions. At $q = 1$:
$$
  \mathfrak{d}_1(g \cdot \phi \cdot g^{-1}) = g \cdot \mathfrak{d}_1(\phi) \cdot g^{-1}, \qquad g \in \mathrm{SU}(2).
$$
At $q \neq 1$, this identity holds under the action of $\mathrm{SU}_q(2)$.
