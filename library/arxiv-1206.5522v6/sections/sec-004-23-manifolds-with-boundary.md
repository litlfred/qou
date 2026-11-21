---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-004-23-manifolds-with-boundary
section_title: "Manifolds with boundary"
section_number: 2.3
pages: 11-12
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 0.99
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds, after Beilinson, Drinfeld and Lurie, are homology-type theories for topological n-manifolds"
---
We will also employ the category of topological manifolds with boundary.

::: definition
$\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^\partial$ is the symmetric monoidal topological category of topological $n$-manifolds, possibly with boundary, which have finite good covers by Euclidean spaces $\mathbb R^n$ and upper half spaces $\mathbb R_{\geq 0} \times \mathbb R^{n-1}$. Morphisms are open embeddings which map boundary to boundary. $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^\partial$ is the full symmetric monoidal topological subcategory of $\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^\partial$ consisting of finite disjoint unions of $\mathbb R^n$ and $\mathbb R_{\geq 0}\times \mathbb R^{n-1}$.
:::

::: remark
The category $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^\partial$ is designed to be minimal with respect to the condition that any finite subset of an $n$-manifold with boundary has an open neighborhood homeomorphic to an object of $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^\partial$. In particular, the closed $n$-disk $\mathbb D^n$ is consequently not an object of $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^\partial$.
:::

The following property is essential.

::: prop
[]{#product label="product"} The functor $$\mathbb R_{\geq 0}\times-:\mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_{n-1} \longrightarrow \mathop{\mathrm{{\mathcal M}\mathsf{fld}}}_n^\partial$$ is homotopically fully faithful. That is, for every pair of $(n-1)$-manifolds $M$ and $N$, the map $$\mathop{\mathrm{\mathsf{Emb}}}(M,N) \longrightarrow \mathop{\mathrm{\mathsf{Emb}}}\bigl(\mathbb R_{\geq 0}\times M,\mathbb R_{\geq 0}\times N\bigr)$$ is a homotopy equivalence.
:::

::: proof
*Proof.* This follows by the standard method of pushing off to infinity in the $\mathbb R_{\geq 0}$ direction (as in the Alexander trick or the contractibility of foliations on $\mathbb R^n$ up to integrable homotopy). That is, define a deformation retraction onto the subspace $\mathop{\mathrm{\mathsf{Emb}}}(M,N)$ by defining for each $t\in [0,1]$ the map $$h_t: \mathop{\mathrm{\mathsf{Emb}}}\bigl(\mathbb R_{\geq 0}\times M, \mathbb R_{\geq 0}\times N\bigr)\longrightarrow \mathop{\mathrm{\mathsf{Emb}}}\bigl(\mathbb R_{\geq 0}\times M, \mathbb R_{\geq 0}\times N\bigr)$$ by

$$h_t(g)(s,x)= \left\{ 
  \begin{array}{l l}
    (s, g_0(x)) 
    & 
    \quad \text{for $s< (1-t)^{-1}-1$}
    \\
    g(s +1 - (1-t)^{-1}, x) 
    & 
    \quad \text{for $s\geq (1-t)^{-1}-1$}
  \end{array} \right.$$ where $g_0: M\hookrightarrow N$ is the restriction of $g$ at the value $s=0$. ◻
:::

::: remark
Together with the Kister--Mazur Theorem [@kister], the previous proposition implies that the map $$\mathop{\mathrm{\mathsf{Top}}}(n-1)\hookrightarrow\mathop{\mathrm{\mathsf{Emb}}}(\mathbb R_{\geq 0}\times \mathbb R^{n-1}, \mathbb R_{\geq 0}\times\mathbb R^{n-1})$$ is a homotopy equivalence. Likewise, $\mathop{\mathrm{{\mathcal D}\sf isk}}^\partial_n$ is an unoriented variant of the Swiss cheese operad of Voronov [@voronov]. Namely, the framed variant $\mathop{\mathrm{{\mathcal D}\sf isk}}_n^{\partial, \mathop{\mathrm{\sf fr}}}$ is homotopy equivalent to the PROP associated to the Swiss cheese operad.
:::
