Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $\{A_n\}_{n \geq 0}$ be the [recursive brane tower](#def:recursive-brane-tower) for $n \geq 1$. Let $q$ denote the substrate parameter. The restriction morphism $r_n \colon A_n \to A_{n-1}$ produces a Frobenius–Hopf object $A_{n-1}$ such that $(\mathbf{C}, A_{n-1}, \tau)$ is a quantum observable universe.

Let $\ell_n \colon A_{n-1} \to A_n$ be the ascent map, a section of $r_n$, so that $r_n \circ \ell_n = \mathrm{id}$, and put $e_n = \ell_n \circ r_n$. The induced :defterm[descent]{#descent} map is the compression

$$
  \mathfrak{d}_n(\varphi) = r_n \circ \varphi \circ \ell_n,
  \qquad
  \mathfrak{d}_n \colon \mathrm{End}_{\mathbf{C}}(A_n) \longrightarrow \mathrm{End}_{\mathbf{C}}(A_{n-1}).
$$

It is a surjective linear map. Its restriction to the block-diagonal subalgebra

$$
  \mathrm{End}_{\mathbf{C}}(A_n)^{e_n} = \{\varphi \in \mathrm{End}_{\mathbf{C}}(A_n) : \varphi \circ e_n = e_n \circ \varphi\}
$$

is a surjective algebra homomorphism onto $\mathrm{End}_{\mathbf{C}}(A_{n-1})$. On all of $\mathrm{End}_{\mathbf{C}}(A_n)$ the map $\mathfrak{d}_n$ is not multiplicative in general. When $A_n$ is a direct sum of $k$ copies of a simple object $X$ with $\mathrm{End}_{\mathbf{C}}(X) = K$ a field, and $A_{n-1}$ is a sum of $j$ copies of $X$ with $0 < j < k$, no surjective algebra homomorphism $\mathrm{End}_{\mathbf{C}}(A_n) \to \mathrm{End}_{\mathbf{C}}(A_{n-1})$ exists at all.

The descent map intertwines the $G_q$-actions across levels $n$ and $n-1$, and in the archimedean realisation it recovers a surjective $*$-homomorphism $\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2)) \to \Gamma(J^1 \mathcal{S}_{n-1}, \mathrm{SU}_{q_{n-1}}(2))$ on the corresponding block-diagonal sections.
