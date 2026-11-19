Let $(\mathbf{C}, A, \tau)$ be a [quantum universe](#def:quantum-universe) over $R$, with [Grothendieck group](#def:grothendieck-group-of-a-qou) $K_0(\mathbf{C})$ and degree-zero [Hochschild homology](#def:hochschild-homology) $HH_0(\mathbf{C})$, the direct sum of the endomorphism modules of the objects modulo the commutator relations $fg = gf$.

**Definition.** The **:defterm[Chern character]{#chern-character}** of $\mathbf{C}$ is the group homomorphism

$$
  \mathrm{ch} \colon K_0(\mathbf{C}) \longrightarrow HH_0(\mathbf{C}), \qquad [X] \longmapsto [\mathrm{id}_X],
$$

sending the isomorphism class of an object to the degree-zero Hochschild class of its identity morphism. It is well defined because $\mathrm{id}_{X \oplus Y} = \mathrm{id}_X \oplus \mathrm{id}_Y$ and the two summands are orthogonal, so $[\mathrm{id}_{X \oplus Y}] = [\mathrm{id}_X] + [\mathrm{id}_Y]$ in $HH_0(\mathbf{C})$ \cite{bghl-2017}.

**The block presentation on a split-semisimple slice.** Whenever an endomorphism algebra or full subcategory splits into a finite set $\widehat{A}$ of orthogonal central idempotents $p_\lambda$ with simple objects $V_\lambda$ ($\lambda \in \widehat{A}$), the classes $[p_\lambda] = [\mathrm{id}_{V_\lambda}]$ span $HH_0$ of that slice: every endomorphism of a simple object is a scalar multiple of the identity, every object in the slice decomposes into simple summands, and morphisms between distinct blocks vanish in the cocenter. On such a slice $HH_0 \cong R^{\widehat{A}}$, and in the block basis

$$
  \mathrm{ch}\Bigl(\sum_\lambda n_\lambda [V_\lambda]\Bigr) \;=\; \sum_\lambda n_\lambda\, [p_\lambda] \;=\; (n_\lambda)_{\lambda \in \widehat{A}} .
$$

On any split-semisimple slice, the Chern character is therefore the map $\mathbb{Z}^{\widehat{A}} \to R^{\widehat{A}}$ induced by the unit map $\mathbb{Z} \to R$: injective whenever $R$ has characteristic zero, and in every case an isomorphism after base change $K_0 \otimes_{\mathbb{Z}} R \xrightarrow{\sim} HH_0$.

**Factorisation of the categorical trace dimension.** In any [rigid monoidal category](#def:rigid-monoidal-category), the rigid trace $\mathrm{tr} \colon \operatorname{End}_{\mathbf{C}}(X) \to \operatorname{End}_{\mathbf{C}}(\mathbf{1}) \cong R$ satisfies $\mathrm{tr}(fg) = \mathrm{tr}(gf)$, so it descends unconditionally to an $R$-linear evaluation map on the cocenter,

$$
  \mathrm{ev} \colon HH_0(\mathbf{C}) \longrightarrow R, \qquad \mathrm{ev}\bigl([\mathrm{id}_X]\bigr) = \mathrm{tr}(\mathrm{id}_X),
$$

with $\mathrm{ev}[p_\lambda] = \mathrm{tr}(\mathrm{id}_{V_\lambda})$ on each simple block. The categorical trace dimension on $K_0(\mathbf{C})$ is the composite

$$
  K_0(\mathbf{C}) \xrightarrow{\ \mathrm{ch}\ } HH_0(\mathbf{C}) \xrightarrow{\ \mathrm{ev}\ } R, \qquad \dim_{\mathbf{C}} = \mathrm{ev} \circ \mathrm{ch}.
$$

This factorisation separates two distinct roles: the Chern character records *which* simple constituents an object carries and with what integer multiplicities, while the cocenter evaluation $\mathrm{ev}$ records *what scalar trace the category assigns to each constituent*. A categorical dimension is a single scalar obtained from the character by one evaluation — for $\mathrm{SU}(2)$, the evaluation at a torus point of a symmetric Laurent polynomial whose value at $1$ is the classical vector-space dimension, as the next example makes explicit. It is not itself an Euler characteristic of a complex, and the Euler characteristic of a curve or surface — which is an alternating sum over all homological degrees — is an invariant of a different kind.
