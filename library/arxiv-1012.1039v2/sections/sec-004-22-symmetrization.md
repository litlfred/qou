---
doc_id: arxiv-1012.1039v2
doc_title: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS"
section_id: sec-004-22-symmetrization
section_title: "Symmetrization"
section_number: 2.2
pages: 6-8
source_pdf: 1012.1039v2.pdf
source_sha256: acb2575050db419d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.955
doc_brief: "SIMPLICIAL VOLUME AND FILLINGS OF HYPERBOLIC MANIFOLDS — Let M be a hyperbolic n–manifold whose cusps have torus cross- sections."
---
[]{#ss:symm label="ss:symm"} It will be convenient in the arguments of Section [\[s:main\]](#s:main){reference-type="ref" reference="s:main"} to assume that all chains considered are *symmetric*. Here we say what this means and justify the assumption.

Consider the abstract $n$--simplex $\Delta^n$. The symmetric group $S_{n+1}$ acts in an obvious way on the vertices, and any permutation $p\in S_{n+1}$ extends to $\Delta^n$ as an affine transformation.

Let $X$ be some space. Any singular simplex $\sigma\colon\thinspace\Delta^n\to X$ can be altered by precomposition with some $p\in S_{n+1}$ and the singular simplices $\sigma$ and $\sigma\circ p$ are generally different, though if $p$ is an odd permutation and $q$ is an even one (so $\mathrm{sgn}(p)=-1$ and $\mathrm{sgn}(q)=1$), we'd really like to think of $\sigma\circ p$ as being the same as $\sigma \circ q$ or $\sigma$, just with opposite orientation. We would also like to avoid the annoying bookkeeping which is standard when dealing with simplices. We therefore define the *symmetrization* map $$S\colon\thinspace C_*(X;\mathbb{R})\to C_*(X;\mathbb{R})$$ on singular $n$-simplices $\sigma$ by $$\label{symmsum}
S(\sigma) = \frac{1}{(n+1)!}
   \sum_{p\in S_{n+1}}\mathrm{sgn}(p)\left(\sigma\circ p\right),$$ and extend linearly over $C_*(X;\mathbb{R})$.

::: lemma
[]{#l:chhom label="l:chhom"} $S$ is a chain map, chain homotopic to the identity. Moreover $\|S(c)\|_1\leq\|c\|_1$ for any chain $c$.
:::

::: proof
*Proof.* It is evident that norm does not increase. The chain homotopy is described in Appendix [\[a:symm\]](#a:symm){reference-type="ref" reference="a:symm"}. ◻
:::

Define $C_*^S(X;R)$ to be the subcomplex of $C_*(X;R)$ consisting of chains in the image of $S$; the transformation $S$ restricts to the identity on this subcomplex. Lemma [\[l:chhom\]](#l:chhom){reference-type="ref" reference="l:chhom"} implies that in computing Gromov norms, we may as well restrict attention to $C_*^S(X;R)$.

Suppose $X$ has the structure of a simplicial complex (or more generally just a CW complex so that each cell is a simplex, and so that each restriction of a gluing map to a face is affine) with triangulation $\mathcal{T}$.

::: definition
We call a singular simplex $\sigma\colon\thinspace\Delta^n \to X$ *affine* if $\sigma = \tau\circ a$ where $a\colon\thinspace\Delta^n\to \Delta^k$ is some affine surjection taking vertices to vertices, and $\tau$ is the characteristic map of some $k$--simplex of $\mathcal{T}$. A linear combination of affine simplices is an *affine chain*, and so on.
:::

::: remark
[]{#r:inclusion label="r:inclusion"} There is a nice inclusion $$\mathcal{C}^{\mathcal{T}}_*(X;\mathbb{R}) \stackrel{i}{\longrightarrow} C_*^S(X;\mathbb{R})$$ of simplicial chains $\mathcal{C}^{\mathcal{T}}_*(X;\mathbb{R})$ given by sending a simplex of $X$ to the symmetrization of its characteristic map. This gives a way to think of simplicial chains as symmetric affine singular chains.
:::

In fact, the image of the map $i$ from Remark [\[r:inclusion\]](#r:inclusion){reference-type="ref" reference="r:inclusion"} contains *all* of the symmetric affine simplices; the symmetrization of an affine simplex which drops dimension must vanish:

::: lemma
[]{#l:vanish label="l:vanish"} Let $X$ have a triangulation $\mathcal{T}$, and suppose that $\sigma$ is an affine singular $n$--simplex with image in the $(n-1)$--skeleton of $X$. Then $S(\sigma) = 0$.
:::

::: proof
*Proof.* Since $\sigma$ has image in the $(n-1)$--skeleton, there must be a pair of vertices $\{v_i,v_j\}$ of the standard simplex $\Delta^n$ which are identified by $\sigma$. Let $p$ be a permutation of the vertices of $\Delta^n$, and let $\tau$ be the transposition switching $v_i$ and $v_j$. The maps $\sigma\circ p$ and $\sigma\circ\tau\circ
  p$ are the same as singular simplices, but the permutations $p$ and $\tau\circ p$ have opposite signs, so the terms $\mathrm{sgn}(p)(\sigma\circ p)$ and $\mathrm{sgn(\tau\circ
    p)}(\sigma\circ\tau p)$ cancel in the sum [\[symmsum\]](#symmsum){reference-type="eqref" reference="symmsum"}. ◻
:::
