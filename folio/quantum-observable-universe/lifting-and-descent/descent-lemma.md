Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe. Let $\{A_n\}_{n \geq 0}$ be the [recursive brane tower](#def:recursive-brane-tower) for $n \geq 1$. Let $q$ denote the aether parameter. The restriction morphism $r_n \colon A_n \to A_{n-1}$ is split by the structure map $\ell_n$, and for $A = \mathcal{O}(G)$ both are Hopf maps. At $n = 1$ it returns $A_0 = A$, so $(\mathbf{C}, A_0, \tau)$ is the original quantum observable universe. At $n \ge 2$ only the Hopf structure of $A_{n-1}$ is recovered: no Frobenius form is required on $A_{n-1}$ ([jet prolongation](#prop:jet-prolongation)), and $(\mathbf{C}, A_{n-1}, \tau)$ is not claimed to be a quantum observable universe.

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

If $r_n$ and $\ell_n$ are Hopf morphisms, they are equivariant for the adjoint action $h \triangleright a = \sum h_{(1)}\, a\, S(h_{(2)})$, with $A_{n-1}$ acting on $A_n$ through $\ell_n$. The descent map then intertwines the induced $G_q$-actions on endomorphisms: it commutes with every operator $\varphi \mapsto \sum_i \rho_n(u_i) \circ \varphi \circ \rho_n(v_i)$, in particular with the Hopf adjoint action and with group conjugation, and these actions preserve $\mathrm{End}_{\mathbf{C}}(A_n)^{e_n}$.

In the archimedean realisation the levels are Hilbert spaces $H_n \supseteq H_{n-1}$, the section $\ell_n$ is an isometry and $r_n = \ell_n^{\dagger}$. Then $\mathfrak{d}_n(\varphi) = \ell_n^{\dagger} \varphi \ell_n$ satisfies $\mathfrak{d}_n(\varphi^{\dagger}) = \mathfrak{d}_n(\varphi)^{\dagger}$, the bounded operators commuting with $e_n = \ell_n \ell_n^{\dagger}$ form a $*$-subalgebra, and $\mathfrak{d}_n$ is a surjective $*$-homomorphism from it onto $B(H_{n-1})$. Under the identification of the section algebras $\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2))$ with these operator algebras, this is the surjective $*$-homomorphism $\Gamma(J^1 \mathcal{S}_n, \mathrm{SU}_{q_n}(2)) \to \Gamma(J^1 \mathcal{S}_{n-1}, \mathrm{SU}_{q_{n-1}}(2))$ on block-diagonal sections.
