Let $(\mathbf{C}, A, \tau)$ be a quantum observable universe equipped with the [recursive brane tower](#def:recursive-brane-tower) $\{A_n\}_{n \geq 0}$. Let $\mathfrak{d}_{n+1}$ be the :refterm[descent]{#descent} homomorphism ([:refterm[descent]{#descent}](#lem:descent)). The **defining boundary** of the $n$-th brane is the full subcategory of $\mathbf{C}$ comprising subobjects of $A_n$ where the restriction morphism $r_n \colon A_n \to A_{n-1}$ has a non-trivial kernel:

$$
  \partial A_n
  = 
  \bigl\{ S \hookrightarrow A_n \bigm|
    \ker(r_n|_S) \neq 0 \bigr\}.
$$

In the archimedean realisation, $\partial A_n$ corresponds to the geometric locus $\partial \mathcal{S}_n = \{p \in \mathcal{S}_n \mid \ker(\mathfrak{d}_{n+1}|_p) \neq 0\} \subseteq \mathcal{S}_n$, which is exactly the degeneracy locus of the fibrewise :refterm[descent]{#descent} map.
