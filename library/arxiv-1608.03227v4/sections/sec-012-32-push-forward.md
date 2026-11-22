---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-012-32-push-forward
section_title: "Push forward"
section_number: 3.2
pages: 14-14
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
text_source: latex
latex_prose_ratio: 0.945
latex_coverage_ratio: 0.99
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
[]{#ssec: noneq push f label="ssec: noneq push f"} Let us assume that $R=S/I$ where $I=(f_1,\dots,f_n)$ and functions $f_i$ form a regular sequence in $S$. In other words, the Koszul complex $K(I)=(\Lambda^\bullet W\otimes \CC[\calZ],d_K)$, $W=\CC^n$ has homologies only in degree $0$. For $W\in S$ let $w$ be its image under the quotient map $j\colon S\rightarrow R$.

For a matrix factorization $\calF=(M,D)\in \MFs(R,w)$, $M=R^k$, we can construct a matrix factorization $j_*(\calF)\in \MFs(S,W)$ in two steps.

*Step 1:* Let us choose a lift $\tilde{D}\in \Hom (\tilde{M},\tilde{M})$, $\tilde{M}:=

S^k$ for the matrix coefficients of $D$.

*Step 2 :* The difference $D^2- (\tilde{D})^2$ has entries in the ideal $I$. The data $((\tilde{M}\otimes\Lambda^\bullet W,\tilde{D}),d_K)$ defines an element of $\Com_{per}^n(\calZ)$. By our first remark this element satisfies the second condition of lemma [\[lem:  ext MF\]](#lem:  ext MF){reference-type="ref" reference="lem:  ext MF"} and the regularity of the sequence $f_i$ implies the first condition.Thus we can apply the lemma to obtain differentials $d^-_{ij}: \tilde{M}\otimes \Lambda^i W\to \tilde{M}\otimes \Lambda^j W$ such that $$(\tilde{M}\otimes \Lambda^\bullet W, d_K+D+d^-)_{per}\in \MFs(\calZ,F),$$ we denote this element $j_*(\calF)$.

The first step of our construction involves a choice of $\tilde{D}$, but the homotopy class of $((\tilde{M}\otimes\Lambda^\bullet W,\tilde{D}),d_K)\in \Com_{per}^n(\calZ)$ is independent of this choice since any two choices of lift $D$ differ by the endomorphism that is homotopic to $0$. The second step produces an element that is unique up to automorphism according to lemma [\[lem: uniq MF+\]](#lem: uniq MF+){reference-type="ref" reference="lem: uniq MF+"}.

To show that the element $j_*(\calF)\in \MFs(\calZ,F)$ is well-defined, we also need to show that we can extend $j_*$ to the space of morphisms between the objects and that homotopy equivalent morphisms get mapped into the homotopy equivalent maps. We prove this later for the equivariant version of the push-forward and since there is a natural forgetful functor from the equivariant to non-equivariant category the well defines of $j_*(\calF)$ follows.

::: remark
[]{#rem: section label="rem: section"} In the case when $j$ is a section of a map $\pi$ the first step of our construction could be made canonical and we encounter this situation in our work. In more details: suppose there is map $\pi:\calZ\to \calZ_0$ such that $\pi\circ j=\mathrm{id}$ and $\calF\in \MFs(\calZ_0,w)$. Then the pull back $\pi^*(\calF)\in \MFs(\calZ,\pi^*(w))$ provides an extension of $\calF$ on $\calZ$ required by the first step of our construction.
:::
