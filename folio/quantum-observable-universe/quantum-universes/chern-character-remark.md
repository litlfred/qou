**Well-definedness.** The Chern character is well defined because $\mathrm{id}_{X \oplus Y} = \mathrm{id}_X \oplus \mathrm{id}_Y$ and the two summands are orthogonal, so $[\mathrm{id}_{X \oplus Y}] = [\mathrm{id}_X] + [\mathrm{id}_Y]$ \cite{bghl-2017}.

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

This factorisation is proved in the Lean formalisation. Its content is a separation of roles: the Chern character records *which* simple constituents an object has and how many times, an integer datum independent of $q$; the evaluation records *what the trace assigns to each block*, which is where $q$ enters. A quantum dimension is one number obtained from the whole character by one evaluation — for the group $\mathrm{SU}(2)$, the evaluation at the pivotal element of a Laurent polynomial whose evaluation at $1$ is the ordinary dimension, as the next example makes explicit. It is not itself an Euler characteristic of anything, and the base curve's Euler characteristic, which is an alternating sum over *all* the Hochschild degrees of a different object, is not obtained from it.
