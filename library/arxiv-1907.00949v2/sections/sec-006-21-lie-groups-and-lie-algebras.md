---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-006-21-lie-groups-and-lie-algebras
section_title: "Lie groups and Lie algebras"
section_number: 2.1
pages: 5-5
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.962
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:Lie label="sec:Lie"} Let $M$ be a smooth manifold and $T^\ast M$ be its cotangent bundle. A *Riemannian metric* on $M$ is a smooth section $g: M \to T^\ast M \otimes T^\ast M$ such that $g_x \coloneqq g(x) \in T^\ast_xM \otimes T^\ast_x M$ is a positive definite symmetric bilinear form on the tangent space $T_xM$ for every $x\in M$. Intuitively, a Riemannian metric gives an inner product on $T_xM$ for every $x\in M$ and it varies smoothly with respect to $x\in M$. Let $G$ be a group and let $m:G\times G \to G$ be the multiplication map $m(a_1,a_2) = a_1a_2$ and $i: G \to G$ be the inversion map $i(a) = a^{-1}$. Then $G$ is a *Lie group* if it is a smooth manifold and the group operations $m$ and $i$ are smooth maps. The tangent space $\mathfrak{g}$ of $G$ at the identity $e\in G$ is a *Lie algebra*, i.e., a vector space equipped with a *Lie bracket*, a bilinear map $[\cdot, \cdot]: \mathfrak{g} \times \mathfrak{g} \to \mathfrak{g}$ satisfying $[X,Y] = -[Y,X]$ (skew-symmetry) and $[X,[Y,Z]] + [Z,[X,Y]] + [Y,[Z,X]] = 0$ (Jacobi identity). For example, if $G$ is the orthogonal group $\mathop{\mathrm{O}}(n)$ of all $n\times n$ real orthogonal matrices, then its Lie algebra $\mathfrak{so}(n)$ is the vector space of all $n\times n$ real skew-symmetric matrices.

For a Lie group $G$, we may define the *left* and *right translation* maps $L_a,R_a:G \to G$ by $L_a(x) = m(a,x) = ax$ and $R_a(x) = m(x,a) = xa$. We say that a Riemannian metric $g$ on $G$ is *left invariant* if for all $a \in G$, $$g_{L_a(x)} \bigl((dL_a)_x (X), (dL_a)_x (Y)\bigr) = g_x(X,Y);$$ *right invariant* if for all $b \in G$, $$g_{R_b(x)} \bigl((dR_b)_x (X), (dR_b)_x (Y)\bigr) = g_x(X,Y);$$ and *bi-invariant* if for all $a,b\in G$, $$g_{R_b \circ L_a(x)} \bigl( (d (R_b \circ L_a))_x (X), (d (R_b \circ L_a))_x (Y)\bigr) = g_x(X,Y)$$ over all $X,Y\in T_xM$.
