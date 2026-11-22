---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-035-453-recovering-the-hecke-algebra
section_title: "Recovering the Hecke algebra"
section_number: 4.5.3
pages: 27-29
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 0.961
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
If we want to produce an algebra isomorphic to $\mathcal H$ starting with the category of Soergel bimodules and not just "the positive part", we just need to add formally to $\mathbb N\mathcal B(S_3)$ the element $-\langle M\rangle$ for every Soergel bimodule $M$. This element will satisfy the equation $-\langle M\rangle+\langle M\rangle=0.$ In this manner we obtain a honest algebra over $\mathbb Z[v,v^{-1}]$, isomorphic to $\mathcal H.$ One formal way of doing this is with the following general definition.

::: defi
Let $\mathcal A$ be an additive category. The *split Grothendieck group* of $\mathcal A$ denoted by $\langle \mathcal A\rangle$ is the free abelian group over the objects modulo the relations $M=N+P$ whenever we have $M\cong N\oplus P.$ Given an object $A\in \mathcal A$, let $\langle A\rangle$ denote its class in $\langle \mathcal A\rangle$.
:::

In the case of $\langle \mathcal B(S_3)\rangle$, this group can be endowed with a structure of $\mathbb Z[v,v^{-1}]$-algebra, as we have seen (addition is direct sum, product is tensor product, etc).

::: sca
If $W$ is $S_3$ we have

-   The set $W\times \mathbb Z$ is in bijection with the set of indecomposable Soergel bimodules via the map $$(w,m)\mapsto B_w(m)$$

-   The map $$\begin{aligned}
    \langle \mathcal B(S_3)\rangle& \rightarrow \mathcal H(S_3)\\ \langle B_w\rangle &\mapsto b_w\\ \langle R(1)\rangle&\mapsto v 
    \end{aligned}$$ is an isomorphism of $\mathbb Z[v,v^{-1}]$-algebras.
:::

::: proof
*Proof.* The first part has already been proved. The second one also, modulo the remark that before we used the notation $\langle N\rangle =\langle M\rangle$ if $N$ and $M$ are isomorphic, and now we are using it for two elements equal in the Grothendieck group and this could be confusing notation. In fact, due to the Krull-Schmidt property explained in the proof of [\[iso\]](#iso){reference-type="ref" reference="iso"} these two notations mean the same thing. ◻
:::

The morphisms between Bott-Samelson bimodules (i.e. bimodules of the form $B_sB_r\cdots B_t$ for $s,r, \ldots, t\in S$) in principle could be quite complicated, or even atrocious, but we are, oh so very lucky. Two miracles happen. Firstly the Hom spaces are free as $R$-modules. This is highly non-trivial.

The second miracle is that there is a combinatorial set (defined by the author in [@Li1]) in the Hom spaces, called "Light leaves" that is a basis of this free Hom space. In the next section we will introduce Soergel bimodules for any Coxeter group and we will explain the construction of light leaves before we can calculate the indecomposable Soergel bimodules for the examples B, C and D in Section [\[final\]](#final){reference-type="ref" reference="final"}.
