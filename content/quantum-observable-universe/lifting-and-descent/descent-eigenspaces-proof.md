Because $\hat{\tau}_n$ is an idempotent endomorphism of the $R$-algebra $\mathrm{End}_{\mathbf{C}}(A_{n+1})$, it induces the direct sum decomposition

$$
  \mathrm{End}_{\mathbf{C}}(A_{n+1})
  = 
  \mathrm{im}\hat{\tau}_n  \oplus  \ker\hat{\tau}_n.
$$

Every $\alpha \in \mathrm{End}_{\mathbf{C}}(A_{n+1})$ decomposes uniquely as $\alpha = \hat{\tau}_n(\alpha) + (\alpha - \hat{\tau}_n(\alpha))$, where $\hat{\tau}_n(\hat{\tau}_n(\alpha)) = \hat{\tau}_n(\alpha)$ and $\hat{\tau}_n(\alpha - \hat{\tau}_n(\alpha)) = 0$. If $\alpha \in \mathrm{im}\hat{\tau}_n \cap \ker\hat{\tau}_n$, then $\alpha = \hat{\tau}_n(\beta)$ and $0 = \hat{\tau}_n(\alpha) = \hat{\tau}_n^2(\beta) = \hat{\tau}_n(\beta) = \alpha$, confirming a trivial intersection.

If $\mathrm{End}_{\mathbf{C}}(A_{n+1})$ carries a $*$-involution compatible with $\hat{\tau}_n$ (i.e. $\hat{\tau}_n(\alpha^*) = \hat{\tau}_n(\alpha)^*$), this decomposition respects the $*$-structure, yielding two $*$-subalgebras.

For item (1), let $\alpha \in \mathrm{End}_{\mathbf{C}}(A_{n+1})$ lie in the image of the ascent $\ell_n$: $\alpha = \ell_n(\beta)$ for some $\beta \in \mathrm{End}_{\mathbf{C}}(A_n)$. Bosonic modes are categorically identified by the [algebraic filter](#rem:algebraic-filter) as commuting with the categorical curvature. Then $\hat{\tau}_n(\alpha) = \ell_n(\mathfrak{d}_{n+1}(\ell_n(\beta))) = \ell_n(\beta) = \alpha$, utilizing $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ ([:refterm[descent]{#descent}](#lem:descent)). Hence $\alpha \in \mathcal{A}_{n+1}^{\mathrm{desc}}$.

For item (2), any endomorphism $\alpha \in \mathrm{End}_{\mathbf{C}}(A_{n+1})$ not factoring through level $n$ satisfies $\mathfrak{d}_{n+1}(\alpha) = 0$ in $\mathrm{End}_{\mathbf{C}}(A_n)$, so $\hat{\tau}_n(\alpha) = \ell_n(0) = 0$ and $\alpha \in \mathcal{A}_{n+1}^{\mathrm{trans}}$. Conversely, level-$(n{+}1)$ endomorphisms factoring through level $n$ lie in $\mathcal{A}_{n+1}^{\mathrm{desc}}$ by (1). Thus, fermionic/ladder modes partition across the two summands based exactly on whether they possess a pre-image under $\mathfrak{d}_{n+1}$.
