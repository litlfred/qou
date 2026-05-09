Since $\hat{\tau}_n$ is an idempotent endomorphism of the $R$-algebra
$\mathrm{End}_{\mathbf{C}}(A_{n+1})$, the standard idempotent splitting
gives a direct sum decomposition

$$
  \mathrm{End}_{\mathbf{C}}(A_{n+1})
  = 
  \mathrm{im}\hat{\tau}_n  \oplus  \ker\hat{\tau}_n.
$$

Indeed, every $\alpha \in \mathrm{End}_{\mathbf{C}}(A_{n+1})$ decomposes
uniquely as $\alpha = \hat{\tau}_n(\alpha) + (\alpha - \hat{\tau}_n(\alpha))$, where
$\hat{\tau}_n(\hat{\tau}_n(\alpha)) = \hat{\tau}_n(\alpha)$ (so $\hat{\tau}_n(\alpha) \in \mathrm{im}\hat{\tau}_n$) and
$\hat{\tau}_n(\alpha - \hat{\tau}_n(\alpha)) = \hat{\tau}_n(\alpha) - \hat{\tau}_n(\alpha) = 0$
(so $\alpha - \hat{\tau}_n(\alpha) \in \ker\hat{\tau}_n$).  The two summands
intersect trivially: if $\alpha \in \mathrm{im}\hat{\tau}_n \cap \ker\hat{\tau}_n$, then $\alpha = \hat{\tau}_n(\beta)$ for some $\beta$ and
$0 = \hat{\tau}_n(\alpha) = \hat{\tau}_n^2(\beta) = \hat{\tau}_n(\beta) = \alpha$.

When $\mathrm{End}_{\mathbf{C}}(A_{n+1})$ carries a $*$-involution
compatible with $\hat{\tau}_n$ (i.e.\ $\hat{\tau}_n(\alpha^*) = \hat{\tau}_n(\alpha)^*$),
the decomposition respects the $*$-structure: both summands are
$*$-subalgebras.

For item (1), let $\alpha \in \mathrm{End}_{\mathbf{C}}(A_{n+1})$ lie
in the image of the ascent $\ell_n$: $\alpha = \ell_n(\beta)$ for some
$\beta \in \mathrm{End}_{\mathbf{C}}(A_n)$.  Bosonic modes are
characterised categorically by the
([algebraic filter](#rem\:algebraic-filter)) as those commuting with the
categorical curvature.  Then
$\hat{\tau}_n(\alpha) = \ell_n(\mathfrak{d}_{n+1}(\ell_n(\beta))) = \ell_n(\beta) = \alpha$,
using $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$
([:refterm[descent]{#descent}](#lem\:descent)).  Hence $\alpha \in \mathcal{A}_{n+1}^{\mathrm{desc}}$.

For item (2), an endomorphism $\alpha \in \mathrm{End}_{\mathbf{C}}(A_{n+1})$ that does not factor through
level $n$ satisfies $\mathfrak{d}_{n+1}(\alpha) = 0$ in
$\mathrm{End}_{\mathbf{C}}(A_n)$, so $\hat{\tau}_n(\alpha) = \ell_n(0) = 0$
and $\alpha \in \mathcal{A}_{n+1}^{\mathrm{trans}}$.  Those level-$(n{+}1)$
endomorphisms that do factor through level $n$ lie in
$\mathcal{A}_{n+1}^{\mathrm{desc}}$ by the argument of item (1).  The
fermionic/ladder modes therefore split between the two summands according
to whether they have a pre-image under $\mathfrak{d}_{n+1}$.
