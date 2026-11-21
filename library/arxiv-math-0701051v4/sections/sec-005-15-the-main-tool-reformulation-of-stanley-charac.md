---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-005-15-the-main-tool-reformulation-of-stanley-charac
section_title: "The main tool: reformulation of Stanley character formula"
section_number: 1.5
pages: 3-4
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.973
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
[]{#subsec:mainresult label="subsec:mainresult"}

Our main tool in our investigations will be the following reformulation of Stanley character formula.

The set of cycles of a permutation $\pi$ is denoted by $C(\pi)$. For given permutations $\sigma_1,\sigma_2\in S_l$ we shall consider colorings $h$ of the cycles of $\sigma_1$ (where each cycle is colored by the number of some column of $\lambda$) and of the cycles of $\sigma_2$ (where each cycle is colored by the number of some row of $\lambda$). Formally, each such coloring can be viewed as a function $h:C(\sigma_1) \sqcup C(\sigma_2)\rightarrow\mathbb{N}$.

We say that a coloring $h$

is compatible with a Young diagram $\lambda$ if for all $c_1\in C(\sigma_1)$ and $c_2\in C(\sigma_2)$ if $c_1\cap c_2\neq \emptyset$ then $(h(c_1),h(c_2))\in\lambda$; in other words $$\label{eq:warunek}
0<h(c_1)\leq \lambda_{h(c_2)}$$ holds true for all $c_1\in C(\sigma_1)$, $c_2\in C(\sigma_2)$ such that $c_1\cap
c_2\neq\emptyset$.

::: theorem
[]{#theo:character-sniady label="theo:character-sniady"} For any Young diagram $\lambda$ and a permutation $\pi\in S_l$ (where $l\leq n$) the value of the normalized character [\[eq:sigma\]](#eq:sigma){reference-type="eqref" reference="eq:sigma"} is given by $$\label{eq:main-theorem}
 \Sigma^{\lambda}(\pi)= \sum_{\substack{\sigma_1,\sigma_2\in S_l,\\ \sigma_1 \sigma_2=\pi}}
(-1)^{|\sigma_1|}\ N^{\lambda}(\sigma_1,\sigma_2),$$ where

$$\begin{gathered}
\label{eq:usual}
N^{\lambda}(\sigma_1,\sigma_2)= 
\#\{h: h \text{ is a coloring of the cycles of $\sigma_1$ and $\sigma_2$} \\
\text{which is compatible with $\lambda$}\}. 
\end{gathered}$$
:::

::: example
[]{#example1 label="example1"} For a given factorization $\pi=\sigma_1 \sigma_2$ it is convenient to consider a bipartite graph with the set of vertices $C(\sigma_1)\sqcup C(\sigma_2)$ and with an edge between vertices $c_1\in C(\sigma_1)$ and $c_2\in C(\sigma_2)$ if and only if $c_1\cap c_2\neq \emptyset$. Notice that the value of $N^{\lambda}(\sigma_1,\sigma_2)$ does not depend on the exact form of $\sigma_1$ and $\sigma_2$ but only on the corresponding bipartite graph.

Figure [1](#fig:bipartite){reference-type="ref" reference="fig:bipartite"} presents such a bipartite graph for $\pi=(12)$, $\sigma_1=(1)(2)$ and $\sigma_2=(12)$. Now it becomes clear that $$\begin{aligned}
 N^{\lambda}\big( (1)(2), (12) \big) & = \sum_i (\lambda_i)^2.\\
\intertext{Similarly, }
 N^{\lambda}\big( (12), (1)(2) \big) & = \sum_i (\lambda'_i)^2,
\end{aligned}$$ where $\lambda'$ denotes the Young diagram conjugate to $\lambda$. In this way, Theorem [\[theo:character-sniady\]](#theo:character-sniady){reference-type="ref" reference="theo:character-sniady"} shows that $$\begin{gathered}
 \Sigma^{\lambda}(12) = n(n-1) \frac{\mathop{\mathrm{Tr}}\rho^{\lambda}(12)}{\mathop{\mathrm{Tr}}\rho^{\lambda}(e)}=\\
N^{\lambda}\big( (1)(2), (12) \big)-N^{\lambda}\big( (12), (1)(2) \big)=
\sum_i (\lambda_i)^2-\sum_i (\lambda'_i)^2.
\end{gathered}$$

![Bipartite graph associated to the factorization $(12)=  (1)(2) \cdot (12)$.](bipartite.eps){#fig:bipartite}
:::
