---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics"
section_id: sec-034-452-how-to-produce-an-algebra-from-soergel-bimod
section_title: "How to produce an algebra from Soergel bimodules"
section_number: 4.5.2
pages: 26-27
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.962
latex_coverage_ratio: 0.961
doc_brief: "Gentle introduction to Soergel bimodules I: The basics — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
Let us introduce the

::: nota
[]{#poly label="poly"} If $p=\sum_i a_i v^i \in \mathbb N[v,v^{-1}]$ and $M$ is a graded bimodule, we will denote by $p\cdot M$ the graded bimodule $$\bigoplus_{i\in \mathbb Z}M(i)^{\oplus a_i}$$
:::

One can see that Soergel bimodules encode all the information of the Hecke algebra. Let us try to make this idea more precise. Consider the following "algebra" $\mathbb N\mathcal B(S_3)$ over $\mathbb N[v,v^{-1}]$ (this is not a ring because it lacks of additive inverse, so $\mathbb N\mathcal B(S_3)$ is strictly speaking not an algebra, but apart from this "detail" it satisfies all the other defining properties of an algebra): the elements of $\mathbb N\mathcal B(S_3)$ are Soergel bimodules modulo isomorphism. We denote by $\langle M\rangle$ the isomorphism class of $M$. In this algebra, the sum is defined to be direct sum $\langle M\rangle+\langle N\rangle:=\langle M\oplus N\rangle$, the product is defined to be tensor product $\langle M\rangle \cdot \langle N\rangle:=\langle M N\rangle$ and multiplication by $v$ is shifting your graded bimodule by $1$, i.e. $v\cdot \langle M\rangle:= \langle M(1)\rangle$.

::: prop
[]{#iso label="iso"} There is an isomorphism of "algebras" $$\begin{aligned}
\mathbb N\mathcal B(S_3)&\cong \bigoplus_{w\in S_3}\mathbb N[v,v^{-1}]b_w\subset \mathcal H=\bigoplus_{w\in S_3}\mathbb Z[v,v^{-1}]b_w\\ 
\langle B_w\rangle &\mapsto b_w.
\end{aligned}$$
:::

::: proof
*Proof.* The equations ([\[BsBs\]](#BsBs){reference-type="ref" reference="BsBs"}), ([\[BsBsrs\]](#BsBsrs){reference-type="ref" reference="BsBsrs"}), ([\[sr\]](#sr){reference-type="ref" reference="sr"}), ([\[w0\]](#w0){reference-type="ref" reference="w0"}) and Proposition [\[dec\]](#dec){reference-type="ref" reference="dec"} tell us that the multiplication rules in both algebras are equal. The only problem that might appear is that $\mathbb N\mathcal B(S_3)$ might not be free as a $\mathbb N[v,v^{-1}]$- module over the set $\langle B_w\rangle_{w\in S_3}$, i.e. one might have that $$\sum_{w\in S_3}p_w \langle B_w\rangle\cong \sum_{w\in S_3}q_w \langle B_w\rangle$$ with $p_w, q_w\in \mathbb N[v,v^{-1}]$. But this is not possible because we have that the category of $\mathbb Z$-graded finitely generated $R$-bimodules (or, what is the same, $R\otimes_{\mathbb R}R$-modules) admits the Krull-Schmidt Theorem. For a proof see [@Pi Section 5.4]. ◻
:::
