---
doc_id: arxiv-2605.28781v1
doc_title: "The sum-product conjecture is false for real numbers"
section_id: sec-007-3-algebraic-number-theory
section_title: "Algebraic number theory"
section_number: 3
pages: 7-7
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
toc_source: outline
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.98
doc_brief: "The sum-product conjecture is false for real numbers — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily large A ⊂R (whose elements are algebraic integers in a"
---
In this section we review the necessary concepts required from algebraic number theory; with the exception of Theorem [\[th-tower\]](#th-tower){reference-type="ref" reference="th-tower"}, these are all classical results that can be found in most textbooks on the subject.

Let $K$ be a totally real number field of degree $d$ over $\mathbb{Q}$, and let $\Delta_K$ be the discriminant of $K$ (which is strictly positive if $K$ is totally real). Let $R_K$ be the regulator of $K$. For those unfamiliar with algebraic number theory, the important role of these parameters for our purposes is that they control the covolume of the lattices of the algebraic integers and units respectively. The only fact that we will require about $K$ (aside from it being totally real) is that these are both bounded above by $O(1)^d$. This is usually done with emphasis on $\Delta_K$, but similar control on $R_K$ follows from the following lemma.

::: lemma
[]{#lem-regbound label="lem-regbound"} If $K$ is a totally real number field of degree $d\geq 2$ then $$R_K \leq \Delta_K.$$
:::

::: proof
*Proof.* As in the proof of [@La70 XIII, Theorem 3], for any real $s>1$, if $h_K$ is the class number of $K$ then $$2^dR_Kh_K\leq 2s(s-1)(\pi^{-d/2}\Delta_K^{1/2})^s \Gamma(s/2)^d\zeta(s)^d.$$ In particular, letting $s=2$, since $h_K\geq 1$ and $d\geq 2$, $$R_K\leq R_Kh_K \leq 4(\pi/12)^d\Delta_K\leq \Delta_K.\qedhere$$ ◻
:::

It therefore suffices to produce $K$ with $\Delta_K\leq O(1)^d$, for arbitrarily large $d$. Such towers were first constructed by Martinet [@Ma78].

::: theorem
[]{#th-tower label="th-tower"} There exists an absolute constant $C>0$ such that, for infinitely many $d$, there exist totally real number fields $K$ with degree $d$ with $\Delta_K\leq C^d$.
:::

There are $d$ embeddings $K\hookrightarrow \mathbb{R}$. These let us view the algebraic integers as $d$-dimensional lattices. As we are concerned with both sums and products, both the additive and multiplicative versions of these lattices will be useful to us.
