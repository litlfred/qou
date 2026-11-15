---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-002-12-index-structures-and-1-efficiency
section_title: "Index structures and 1-efficiency"
section_number: 1.2
pages: 3-4
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.811
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
[]{#sub.1eff label="sub.1eff"}

::: thm
[]{#index_structure_iff_1-efficient label="index_structure_iff_1-efficient"} An ideal triangulation $\mathcal{T}$ of an oriented 3-manifold with cusps admits an index structure if and only if $\mathcal{T}$ is 1-efficient.
:::

The above theorem has some consequences for our sought topological invariants.

::: rmk
[]{#rem.1 label="rem.1"} 1-efficiency of $\mathcal{T}$ implies restrictions on the topology of $M$: it follows that $M$ is irreducible and atoroidal. Note that here by *atoroidal*, we mean that any *embedded* torus is either compressible or boundary parallel. It follows by Thurston's Hyperbolization Theorem in dimension $3$ that $M$ is hyperbolic or small Seifert-fibred.
:::

::: rmk
[]{#rem.2 label="rem.2"} If $K$ is the connected sum of the $4_1$ and $5_2$ knots, or $K'$ is the Whitehead double of the $4_1$ knot and $\mathcal{T}$ is any ideal triangulation of the complement of $K$ or $K'$, then $\mathcal{T}$ is not 1-efficient, thus $I_{\mathcal{T}}$ never exists. On the other hand, the (coloured) Jones polynomial, the Kashaev invariant and the $\mathrm{PSL}(2,\mathbb C)$-character variety of $K$ and $K'$ happily exist; see [@Jo; @Ka; @CCGLS].
:::

::: thm
[]{#semi-angle => 1-efficient label="semi-angle => 1-efficient"} Let $\mathcal{T}$ be an ideal triangulation of an oriented atoroidal 3--manifold with at least one cusp. If $\mathcal{T}$ admits a semi--angle structure then $\mathcal{T}$ is 1--efficient.
:::

::: rmk
[]{#rem.3 label="rem.3"} Taut and strict angle structures are examples of semi-angle structures, and for these cases this is proved in [@KR2 Thm.2.6]. In Section [\[sec: index structures and 1-efficiency\]](#sec: index structures and 1-efficiency){reference-type="ref" reference="sec: index structures and 1-efficiency"}, we give a brief outline of the argument for a general semi--angle structure.
:::

::: rmk
In Corollary [\[atoroidal=\>1-efficient\]](#atoroidal=>1-efficient){reference-type="ref" reference="atoroidal=>1-efficient"}, we note that a construction of Lackenby produces triangulations with taut angle structures, which are therefore 1--efficient, on all irreducible an-annular cusped 3--manifolds. However, it is not clear that the triangulations produced by this construction are connected by the appropriate 2--3 and 0--2 moves, so we cannot prove that the 3D index is independent of the choice of taut triangulation for the manifold.
:::
