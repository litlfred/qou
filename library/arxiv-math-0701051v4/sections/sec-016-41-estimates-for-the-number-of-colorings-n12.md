---
doc_id: arxiv-math-0701051v4
doc_title: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e)"
section_id: sec-016-41-estimates-for-the-number-of-colorings-n12
section_title: "Estimates for the number of colorings N(1,2)"
section_number: 4.1
pages: 12-13
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.959
doc_brief: "VALENTIN FÉRAY AND PIOTR ŚNIADY Tr ρλ(π) a max Tr ρλ(e) — We prove an upper bound for characters of the symmetric groups."
---
[]{#eq:estimate-lambda label="eq:estimate-lambda"}

As we already mentioned in Example [\[example1\]](#example1){reference-type="ref" reference="example1"} to permutations $\sigma_1,\sigma_2$ we can associate a bipartite graph $C(\sigma_1)\sqcup C(\sigma_2)$ with an edge between $c_1\in C(\sigma_1)$ and $c_2\in C(\sigma_2)$ if $c_1\cap c_2\neq \emptyset$.

For a bipartite graph $G=C_1\sqcup C_2$ (not necessarily arising from the above construction) and a Young diagram $\lambda$ we define $N^{\lambda}(G)$ as the number of colorings $h$ of the vertices of $C_1\sqcup C_2$ which are compatible with the Young diagram $\lambda$ (the definition of compatibility in this context is a natural extension of the old one, i.e. we require that if $c_1\in C_1$ and $c_2\in C_2$ are connected by an edge then $\big( h(c_1),h(c_2) \big)\in \lambda$).

We denote by $G_{p,q}$ a full bipartite graph for which $|C_1|=p$ and $|C_2|=q$.

::: lemma
[]{#lem:grafGprim label="lem:grafGprim"}

Let $G$ be a finite bipartite graph with a property that the degree of any vertex is non-zero. It is possible (not necessarily in a unique way) to remove some of the edges of $G$ in such a way that the resulting graph $\tilde{G}$ is a disjoint union of the graphs of the form $G_{1,1}$, $G_{k,1}$, $G_{1,k}$.

Assume that a Young diagram $\lambda$ consists of $n$ boxes. Then, for any $A \geq r(\lambda),c(\lambda)$ $$\label{eq:szacowanie-lambdy}
N^{\lambda}(G)\leq A^{\text{(number of vertices of $G$)}} 
\left(\frac{n}{A^2}\right)^{\text{(number of connected components of
$\tilde{G}$)}}.$$
:::

::: proof
*Proof.* If the graph $G$ contains an edge which connects two vertices of degree bigger than one we remove it and iterate this procedure; if no such edge exists then the resulting graph $\tilde{G}$ has the desired property.

Clearly, $N^\lambda(G)\leq N^\lambda(\tilde{G})$ therefore it is enough to find a suitable upper bound for $N^\lambda(\tilde{G})$. Since both sides of [\[eq:szacowanie-lambdy\]](#eq:szacowanie-lambdy){reference-type="eqref" reference="eq:szacowanie-lambdy"} are multiplicative with respect to the disjoint sum of graphs it is enough to prove [\[eq:szacowanie-lambdy\]](#eq:szacowanie-lambdy){reference-type="eqref" reference="eq:szacowanie-lambdy"} for $\tilde{G}\in\{G_{1,1},G_{k,1}, G_{1,k}\}$. Now, the lemma follows from: $${N^\lambda}(G_{k,1})=\sum_i \lambda_i^k\leq  
\sum_i \lambda_i A^{k-1} = n A^{k-1}$$ and the analogous inequality for ${N^\lambda}(G_{1,k})$. ◻
:::

::: proposition
[]{#prop:bipartite-graphs label="prop:bipartite-graphs"} Suppose that $r(\lambda),c(\lambda) \leq A \leq n$ and $\sigma_1,\sigma_2\in S_l$ and $\pi=\sigma_1 \sigma_2$. Then $$\begin{gathered}
\label{eq:swider}
N^\lambda(\sigma_1,\sigma_2)  \leq  A^{|C(\sigma_1)|+|C(\sigma_2)|}\left(\frac{n}{A^2}\right)^{\mathop{\mathrm{orbits}}(\sigma_1,\sigma_2)} 
\\ \leq   A^{l-|C(\pi)|} n^{|C(\pi)|}
\left(\frac{1}{A}\right)^{o(\sigma_1,\sigma_2)},
\end{gathered}$$ where $\mathop{\mathrm{orbits}}(\sigma_1,\sigma_2)$ denotes the number of orbits in the action of $\langle \sigma_1,\sigma_2\rangle$ on the set $\{1,\dots,n\}$ and $$o(\sigma_1,\sigma_2)=l-|C(\sigma_1)|-|C(\sigma_2)| +\mathop{\mathrm{orbits}}(\sigma_1,\sigma_2).$$
:::

::: proof
*Proof.* The first inequality is a simple corollary from Lemma [\[lem:grafGprim\]](#lem:grafGprim){reference-type="ref" reference="lem:grafGprim"} since $A^2\geq r(\lambda) c(\lambda) \geq n$ and the number of connected components of $\tilde{G}$ is bounded from below by $\mathop{\mathrm{orbits}}(\sigma_1,\sigma_2)$. The second inequality follows by multiplying by $$\left( \frac{n}{A}
\right)^{|C(\pi)|-\mathop{\mathrm{orbits}}(\sigma_1,\sigma_2)} 
\geq 1.\qedhere$$ ◻
:::
