---
doc_id: arxiv-1907.00949v2
doc_title: "OPTIMIZATION ON FLAG MANIFOLDS"
section_id: sec-014-5-flag-manifolds-as-matrix-manifolds
section_title: "Flag manifolds as matrix manifolds"
section_number: 5
pages: 16-17
source_pdf: 1907.00949v2.pdf
source_sha256: 865defaa34bf42be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.956
doc_brief: "OPTIMIZATION ON FLAG MANIFOLDS — A ﬂag is a sequence of nested subspaces."
---
[]{#sec:mfld label="sec:mfld"}

By Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"}[\[it:cls1\]](#it:cls1){reference-type="eqref" reference="it:cls1"} and [\[it:cls2\]](#it:cls2){reference-type="eqref" reference="it:cls2"}, we see that a flag manifold may be regarded as a submanifold of a product of Grassmannians. Since a Grassmannian can be represented as a subset of matrices in $\mathbb{R}^{n\times n}$ [@Nicolaescu Example 1.2.20], $$\label{eq:P}
\mathop{\mathrm{Gr}}(k,n) \cong \{P\in \mathbb{R}^{n\times n}: P^2 = P = P^{\scriptscriptstyle\mathsf{T}},\; \mathop{\mathrm{tr}}(P) = k\},$$ so can a flag manifold; and we will discuss two different ways do this, corresponding to [\[it:cls1\]](#it:cls1){reference-type="eqref" reference="it:cls1"} and [\[it:cls2\]](#it:cls2){reference-type="eqref" reference="it:cls2"} in Proposition [\[prop:geometric structure\]](#prop:geometric structure){reference-type="ref" reference="prop:geometric structure"}: $$\begin{aligned}
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\subseteq \mathop{\mathrm{Gr}}(n_1,n)\times  \mathop{\mathrm{Gr}}(n_2,n) \times \dots \times \mathop{\mathrm{Gr}}(n_d,n),\\
\mathop{\mathrm{Flag}}(n_1,\dots,n_d;n) &\subseteq \mathop{\mathrm{Gr}}(n_1,n)\times  \mathop{\mathrm{Gr}}(n_2-n_1,n) \times \dots \times \mathop{\mathrm{Gr}}(n_d-n_{d-1},n).
\end{aligned}$$

The correspondence in [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"} is given by a map that takes a $k$-dimensional subspace $\mathbb{W}\in \mathop{\mathrm{Gr}}(k,n)$ to its orthogonal projector, $$\label{eq:epsGr}
\varepsilon: \mathop{\mathrm{Gr}}(k,n) \to \mathbb{R}^{n\times n}, \quad \mathbb{W} \mapsto W W^{\scriptscriptstyle\mathsf{T}},$$ where $W \in \mathbb{R}^{n \times k}$ is any orthonormal basis of $\mathbb{W}$. Note that if $W'$ is another such $n \times k$ matrix, then $W' = W Q$ for some $Q\in \mathop{\mathrm{O}}(k)$ and so $W'W^{\prime{\scriptscriptstyle\mathsf{T}}} =WW^{\scriptscriptstyle\mathsf{T}}$ and the map $\varepsilon$ is well-defined. It is also injective and its image is precisely the set on the right of [\[eq:P\]](#eq:P){reference-type="eqref" reference="eq:P"}.
