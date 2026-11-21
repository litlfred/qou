Let $(\mathbf{C}, A, \tau)$ be a quantum universe over $R$, with [Grothendieck group](#def:grothendieck-group-of-a-qou) $K_0(\mathbf{C})$ and degree-zero [Hochschild homology](#def:hochschild-homology) $HH_0(\mathbf{C})$, the direct sum of the endomorphism modules of the objects modulo the relations $fg = gf$.

**Definition.** The **:defterm[Chern character]{#chern-character}** of $\mathbf{C}$ is the homomorphism

$$
  \mathrm{ch} \colon K_0(\mathbf{C}) \longrightarrow HH_0(\mathbf{C}), \qquad [X] \longmapsto [\mathrm{id}_X],
$$

sending the class of an object to the Hochschild class of its identity morphism. It is well defined because $\mathrm{id}_{X \oplus Y} = \mathrm{id}_X \oplus \mathrm{id}_Y$ and the two summands are orthogonal, so $[\mathrm{id}_{X \oplus Y}] = [\mathrm{id}_X] + [\mathrm{id}_Y]$ \cite{bghl-2017}.

**The block presentation.** By Wedderburn semisimplicity the central idempotents $p_\lambda \in \operatorname{End}(A)$, one per block $\lambda \in \widehat{A}$, span $HH_0(\mathbf{C})$: every endomorphism of a simple object is a scalar, every object is a sum of simple ones, and morphisms between different blocks contribute nothing to the cocenter. So $HH_0(\mathbf{C}) \cong R^{\widehat{A}}$, spanned by the classes $[p_\lambda] = [\mathrm{id}_{V_\lambda}]$, and in this basis

$$
  \mathrm{ch}\Bigl(\sum_\lambda n_\lambda [V_\lambda]\Bigr) \;=\; \sum_\lambda n_\lambda\, [p_\lambda] \;=\; (n_\lambda)_{\lambda \in \widehat{A}} .
$$

The Chern character is therefore the map $\mathbb{Z}^{\widehat{A}} \to R^{\widehat{A}}$ induced by the ring map $\mathbb{Z} \to R$: injective when $R$ has characteristic zero, and in every case an isomorphism after tensoring with $R$.

**The factorisation of the quantum dimension.** The rigid trace $\mathrm{tr} \colon \operatorname{End}(X) \to \operatorname{End}(\mathbf{1}) = R$ of a [rigid monoidal category](#def:rigid-monoidal-category) satisfies $\mathrm{tr}(fg) = \mathrm{tr}(gf)$, so it descends to a linear map

$$
  \mathrm{ev} \colon HH_0(\mathbf{C}) \longrightarrow R, \qquad \mathrm{ev}[p_\lambda] = \dim_q(V_\lambda),
$$

and the quantum dimension on $K_0(\mathbf{C})$ is the composite

$$
  K_0(\mathbf{C}) \xrightarrow{\ \mathrm{ch}\ } HH_0(\mathbf{C}) \xrightarrow{\ \mathrm{ev}\ } R, \qquad \dim_q = \mathrm{ev} \circ \mathrm{ch}.
$$

The factorisation holds on all of $K_0(\mathbf{C})$, because both sides are additive and they agree on each generator $[V_\lambda]$. Its content is a separation of roles: the Chern character records *which* simple constituents an object has and how many times, an integer datum independent of the deformation; the evaluation records *what the trace assigns to each block*, which is where the deformation enters. A quantum dimension is one number obtained from the whole character by one evaluation — for the group $\mathrm{SU}(2)$, the evaluation at the pivotal element of a Laurent polynomial whose evaluation at $1$ is the ordinary dimension, as the next example makes explicit. It is not itself an Euler characteristic of anything, and the base curve's Euler characteristic, which is an alternating sum over *all* the Hochschild degrees of a different object, is not obtained from it.
