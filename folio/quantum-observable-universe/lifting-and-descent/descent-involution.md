**Definition.**
Let $\ell_n \colon A_n \hookrightarrow A_{n+1}$ be the ascent embedding ([jet prolongation](#prop:jet-prolongation)). Let $\mathfrak{d}_{n+1} \colon \mathrm{End}_{\mathbf{C}}(A_{n+1}) \to \mathrm{End}_{\mathbf{C}}(A_n)$ be the :refterm[descent]{#descent} homomorphism ([descent](#lem:descent)). The *descent involution* at level $n$ is the endomorphism:
$$
  \hat{\tau}_n = \ell_n \circ \mathfrak{d}_{n+1} \colon \mathrm{End}_{\mathbf{C}}(A_{n+1}) \longrightarrow \mathrm{End}_{\mathbf{C}}(A_{n+1}).
$$
The map $\ell_n$ embeds $A_n$ as a direct summand retracted by $\mathfrak{d}_{n+1}$. One has $\mathfrak{d}_{n+1} \circ \ell_n = \mathrm{id}$ on $\mathrm{End}_{\mathbf{C}}(A_n)$. Therefore:
$$
  \hat{\tau}_n^2 = \ell_n \circ \mathfrak{d}_{n+1} \circ \ell_n \circ \mathfrak{d}_{n+1} = \ell_n \circ (\mathfrak{d}_{n+1} \circ \ell_n) \circ \mathfrak{d}_{n+1} = \ell_n \circ \mathrm{id} \circ \mathfrak{d}_{n+1} = \hat{\tau}_n.
$$
The map $\hat{\tau}_n$ is an idempotent. Its image is the *descended subalgebra* $\mathcal{A}_{n+1}^{\mathrm{desc}} \subseteq \mathrm{End}_{\mathbf{C}}(A_{n+1})$. This subalgebra contains the level-$(n+1)$ endomorphisms that factor through the level-$n$ algebra via ascent.
