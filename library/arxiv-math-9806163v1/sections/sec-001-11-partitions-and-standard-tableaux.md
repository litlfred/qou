---
doc_id: arxiv-math-9806163v1
doc_title: "Weights of Markov traces on Hecke algebras"
section_id: sec-001-11-partitions-and-standard-tableaux
section_title: "Partitions and Standard Tableaux"
section_number: 1.1
pages: 3-4
source_pdf: 9806163v1.pdf
source_sha256: dba44975f29cb017
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.99
latex_coverage_ratio: 0.99
doc_brief: "Weights of Markov traces on Hecke algebras — We compute the weights, i.e. the values at the minimal idempotents, for the Markov trace on the Hecke algebra of type Bn and type Dn."
---
A *partition* of $n$ is a sequence of positive numbers $\alpha=(\alpha_1,\ldots, \alpha_k)$ such that $\alpha_1\geq \alpha_2\geq \ldots \geq \alpha_k \geq 0$ and $n=|\alpha|=\alpha_1+\alpha_2+\ldots +\alpha_k$. The $\alpha_i$'s are called the *parts* of $\alpha$, and the number of nonzero parts of $\alpha$ is called the *length* of $\alpha$, denoted by $l(\alpha)$. If we say $l(\alpha)\leq r_1$, then we we will mean that there are $s\leq r_1$ nonzero parts and the remaining $r_1-s$ are equal to zero. We use the notation $\alpha\vdash n$ to mean $\alpha$ is a partition of $n$. A *Young diagram* is a pictorial representation of a partition $\alpha$ as an array of $n$ boxes with $\alpha_1$ boxes in the first row, $\alpha_2$ boxes in the second row, and so on. We count the rows from top to bottom. We shall denote the Young diagram and the partitions by the same symbol $\alpha$. We use the word *shapes* interchangeably with the word partitions. The set of all partitions of $n$ is denoted by $\Lambda_n$. If $\alpha$ and $\beta$ are two partitions with $|\alpha| \leq |\beta|$, then we write $\alpha\subset \beta$ if $\alpha_i\leq \beta_i$ for all $i$. In this case we say that $\alpha$ is contained in $\beta$. If $\alpha\subset \beta$ then the set-theoretic difference $\beta-\alpha$ is called a *skew diagram*, $\alpha/\beta$. A *standard tableaux* of shape $\alpha$ is a filling of the boxes with numbers $1, 2,\ldots, n$ such that the numbers in each row increase from left to right and in every column from top to bottom. The notation $t^{\alpha}$ will be used to denote a standard tableaux of shape $\alpha$. We say $t^{\alpha}\subset t^{\beta}$ if $t^{\alpha}$ is obtained by removing appropriate boxes from $t^{\beta}$, i.e. the numbers $1, 2, \ldots, |\alpha|$ are in the same boxes of both in $t^{\alpha}$ and in $t^{\beta}$. In this case we say that $t^{\alpha}$ is contained in $t^{\beta}$. A *double partition* of size $n$, $(\alpha,\beta)$, is an ordered pair of partitions $\alpha$ and $\beta$ such that $|\alpha|+|\beta|=n$. The length of a double partition is $l(\alpha, \beta)=l(\alpha)+l(\beta)$. A double partition can be associated with a pair of Young diagrams. The set of all pairs of Young diagrams with $n$ boxes is denoted by $\Lambda_n^D$. We write as for single partitions $(\alpha,\beta) \subset (\delta,\gamma)$ if $\alpha_i \leq \delta_i$ and $\beta_j \leq \gamma_j$ for all $i$ and $j$. That is, $(\alpha,\beta)$ is obtained from $(\delta,\gamma)$ by removing appropriate boxes of $(\delta,\gamma)$, or equivalently $(\alpha,\beta)$ is contained in $(\delta,\gamma)$. $t^{(\alpha,\beta)}=(t^{\alpha},t^{\beta})$ is a pair of standard tableaux if the arrangement of the numbers is in increasing order in the rows and columns of both $t^{\alpha}$ and $t^{\beta}$. For any double partition $(\alpha,\beta)$, let $T_{(\alpha,\beta)}$ denote the set of standard tableaux of shape $(\alpha,\beta)$ and $\mathcal{T}_n$ denote the set of all pairs of tableaux with $n$ boxes. For example, the diagram below is a pair of standard tableaux of shape $([2,1,1],[3,2])$

::: picture
(200,60)(0,0) (175,50)(12,12)1 (175,38)(12,12)2 (175,26) (12,12)4 (187,50)(12,12)6 (225,50)(12,12)3 (225,38)(12,12)5 (237,50)(12,12)7 (237,38)(12,12)8 (249,50)(12,12)9 (160,40)${(}$ (205,38), (270,40)${)}$ (200,0)Figure 1
:::

We say that a box in $(\alpha, \beta)$ has coordinates $(i,j)$ if the box is in the $i$-th row and $j$-th column of either $\alpha$ or $\beta$. Two boxes in $(\alpha, \beta)$ can have the same coordinates if they occur in the same box in $\alpha$ as in $\beta$; for instance, the left-top-most box in $\alpha$ and the left-top-most box in $\beta$ both have coordinates $(1,1)$. The following observation will be used throughout the sequel. For $m, r_1, n\in \mathbb{N}$, let $m>n$ and $r_1>n$. Consider a pair of Young diagrams $(\alpha,\beta)$ with $n$ boxes. We construct from the pair $(\alpha,\beta)$ a Young diagram $\mu$ with $mr_1+n$ boxes by adjoining a rectangular box with $r_1$ rows and $m$ columns, as in Figure 2. The diagram described corresponds to the following partition: $$\mu = (m+\alpha_1,m+\alpha_2,\ldots,m+\alpha_{r_1},\beta_1,\beta_2,\ldots,\beta_{r_2})$$ **Observation: ** Let $n$, $m$, and $r_1$ be as above. Let $[m^{r_1}]\vdash f$. Then there is a 1-1 correspondence between pairs of Young diagrams with $n$ boxes and Young diagrams containing $[m^{r_1}]$ with $n+f$ boxes.

::: picture
(400,210)(0,0) (175,200)(1,0)100 (175,100)(0,0)100 (275,100)(0,0)100 (175,100)(1,0)100 (275,200)(1,0)75 (350,175)(0,0)25 (325,175)(1,0)25 (325,150)(0,0)25 (300,150)(1,0)25 (275,125)(1,0)25 (300,125)(0,0)25 (175,25)(0,0)75 (175,25)(1,0)25 (200,25)(0,0)25 (200,50)(1,0)25 (225,50)(0,0)25 (225,75)(1,0)25 (250,75)(0,0)25 (215,210)(-1,0)40 (235,210)(1,0)40 (220,210)$m$ (165,160)(0,1)40 (165,140)(0,-1)40 (160,150)$r_1$ (300,175)$\alpha$ (200,60)$\beta$ (180,0)Figure 2 (135,100)$\mu \rightarrow$
:::

.1in
