---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-001-2-preliminaries-and-notation
section_title: "Preliminaries and notation"
section_number: 2
pages: 5-6
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
toc_source: outline
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.959
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on truncated"
---
[]{#notation label="notation"} In this section we discuss some background on partitions and set the notation used frequently in the article.

We write $\lambda \vdash n$ to mean that $\lambda$ is a partition of $n$. We say that $\lambda$ has size $n$ if the parts of $\lambda$ add up to $n$ and write $|\lambda|$ for the size of $\lambda$. The length of $\lambda$, denoted $\ell(\lambda)$, is the number of parts in $\lambda$. We denote by $\ell_e(\lambda)$ (respectively $\ell_o(\lambda)$) the number of even (respectively odd) parts in $\lambda$. We also work with vectors of partitions and write $(\lambda^{(1)}, \lambda^{(2)}, \ldots, \lambda^{(t)})\vdash n$ to mean that $\lambda^{(1)}, \lambda^{(2)}, \ldots, \lambda^{(t)}$ are partitions with $|\lambda^{(1)}|+|\lambda^{(2)}|+\cdots+|\lambda^{(t)}|=n.$

We denote by $\mathcal P(n)$ the set of all partitions of $n$. In general, if $\mathcal A(n)$ denotes a set of partitions of $n$ satisfying certain conditions, we set $\mathcal A:=\bigcup_{n\geq 0}\mathcal A(n).$ Moreover, if $f$ is a partition counting function, say $f(n)=|\mathcal A(n)|$, we use the convention that $f(x)=0$ if $x\not\in \mathbb N_0$. We use the notation $\mathbb N_0$ for the set of non-negative integers.

The Ferrers diagram of a partition $\lambda=(\lambda_1, \lambda_2, \ldots, \lambda_\ell)$ is an array of left justified boxes such that the $i$th row from the top contains $\lambda_i$ boxes. For example, the Ferrers diagram of $\lambda=(5, 3, 2, 2, 1)$ is shown below

::: center
:::

We abuse notation and write $\lambda$ to mean a partition, its Ferrers diagram, or its multiset of parts. We write $a\in \lambda$ to mean the positive integer $a$ is a part of $\lambda$. The number of times $a>0$ appears in $\lambda$ is denoted by $m_\lambda(a)$ and is called the multiplicity of $a$ in $\lambda$. When convenient, we use the frequency notation for partitions: the exponent of a part is the multiplicity of the part. For example, $\lambda=(5^2, 3^4, 1)$ is the partitions $(5,5,3,3,3,3,1)$. We also use the convention that $\lambda_j=0$ for all $j>\ell(\lambda)$ and set $\lambda_0:=\infty$.

We define the following operations on partitions. If $\lambda$ and $\mu$ are partitions, by $\lambda\cup \mu$ and $\lambda\setminus \mu$ we mean the corresponding operations on the multisets of parts of $\lambda$ and $\mu$. Moreover $\lambda\setminus \mu$ is only defined if $\mu \subseteq \lambda$ as multisets.

Given an integer $R\geq 2$, and a partition $\lambda$, the $R$-modular diagram of $\lambda$ is a Ferrers diagram with $\ell(\lambda)$ rows such that, if $\lambda_i=q_iR+S_i$ for $q_i\geq 0$ and $0< S_i\leq R$, then the $i$th row from the top has $q_i+1$ boxes: the first $q_i$ boxes are filled with $R$ and the last box is filled with $S_i$. For example, if $R=3$ and $\lambda=(10, 9, 8,8, 7, 3, 2)$, the $3$-modular diagram of $\lambda$ is $${\young(3331,333,332,332,331,3,2)}$$

Given integers $R\geq 2$ and $0<S<R$, we denote by $\mathcal P_{\pm S,R}(n)$ the set of partitions of $n$ with parts congruent to $\pm S$ modulo $R$. For $j\geq 1$, we denote by $\delta_{S,R, j}$ the partition in $\mathcal P_{\pm S,R}$ with distinct parts equal to $iR+S$ for $0\leq i\leq j-1$. If $j=0$, we set $\delta_{S,R,0}:=\emptyset$. The $R$-modular Ferrers diagram of $\delta_{S, R, j}$ is a staircase shaped diagram with $j$ rows, each having $S$ in the last box. For example, the $5$-modular diagram of $\delta_{3, 5, 4}$ is $$\young(5553,553,53,3)$$

Moreover, $|\delta_{S, R, j}|=j(j-1)R/2+jS$. If $R$ is clear from the context, we drop the subscript $R$ from $\delta_{S,R, j}$ to write $\delta_{S, j}$.

For a partition $\lambda$, we write $\lambda_{\ell-i}$ for the $(i+1)^{\textrm{st}}$ part counted from the last: $\lambda_\ell$ is the last part, $\lambda_{\ell-1}$ is the second to last part, etc.

If $r\geq 2$ and $0\leq s<r$ we write $\lambda^{s,r}$ for the partitions whose parts are the parts of $\lambda$ that are congruent to $s$ modulo $r$ (with the same multiplicity as in $\lambda$) and we set $\lambda^{\pm s, r}:=\lambda^{s,r}\cup \lambda^{r-s, r}$.

We use the customary shorthand notation $$(a_1,a_2, \ldots, a_j;q)_\infty:=(a_1;q)_\infty(a_2;q)_\infty\cdots(a_j;q)_\infty.$$
