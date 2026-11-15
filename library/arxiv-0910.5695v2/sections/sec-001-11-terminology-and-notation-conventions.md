---
doc_id: arxiv-0910.5695v2
doc_title: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St)"
section_id: sec-001-11-terminology-and-notation-conventions
section_title: "Terminology and notation conventions"
section_number: 1.1
pages: 2-2
source_pdf: 0910.5695v2.pdf
source_sha256: 703c2a2f1f9380b1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.91
latex_coverage_ratio: 0.984
doc_brief: "ON BLOCKS OF DELIGNE’S CATEGORY Rep(St) — We describe blocks in Deligne’s category Rep(St)."
---
[]{#notation label="notation"} Let $F$ be a field. A *tensor category* is an $F$-linear[^1] category $\mathcal{T}$ along with an $F$-linear bifunctor $\otimes:\mathcal{T}\times\mathcal{T}\to\mathcal{T}$ and associativity, commutativity, and unit constraints satisfying the triangle, pentagon, and hexagon axioms (see [@MR1797619]). Moreover, we require our tensor categories to be rigid with $\text{End}_\mathcal{T}({\bf 1})=F$.

A *Young diagram* is an infinite tuple of nonnegative integers $\lambda=(\lambda_1, \lambda_2,\ldots)$ with $\lambda_i\geq\lambda_{i+1}$ for all $i>0$ such that $\lambda_k=0$ for some $k>0$. As usual, we identify a Young diagram with an array of boxes: $$\includegraphics{diss74.pdf}$$ Let $|\lambda|$ denote the number of boxes in $\lambda$. Given Young diagrams $\lambda=(\lambda_1, \lambda_2,\ldots)$ and $\lambda'=(\lambda_1', \lambda_2',\ldots)$ write $\lambda\subset\lambda'$ if $\lambda_i\leq\lambda_i'$ for all $i>0$. If $|\lambda|=|\lambda'|$ we write $\lambda\prec\lambda'$ if $\sum_{i=1}^m\lambda_i\leq\sum_{i=1}^m\lambda_i'$ for all $m>0$. Occasionally it will be useful to give a Young diagram by its *multiplicities*. We will write $(l_1^{m_1},\ldots, l_r^{m_r})$ to denote the Young diagram with $m_i$ rows of length $l_i$ for each $i=1,\ldots, r$. If $F$ has characteristic zero and $d$ is a nonnegative integer, the simple modules of the symmetric group $S_d$ are labelled by Young diagrams $\lambda$ with $|\lambda|=d$ (see e.g. [@MR1153249 4.2]). Let $L_\lambda$ denote the simple $S_d$-module corresponding to $\lambda$. For example, $L_{(d,0,\ldots)}$ is the trivial representation of $S_d$. Finally, for arbitrary $t\in F$, the *$t$-completion of $\lambda$* is $\lambda(t):=(t-|\lambda|, \lambda_1, \lambda_2,\ldots)$.

# The tensor category $\underline{\operatorname{Re}}\!\operatorname{p}(S_t)$

[^1]: Notice that we do not require our tensor categories to be abelian, or even additive.
