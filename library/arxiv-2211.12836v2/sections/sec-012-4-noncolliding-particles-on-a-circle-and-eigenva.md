---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-012-4-noncolliding-particles-on-a-circle-and-eigenva
section_title: "Noncolliding particles on a circle and eigenvalues of unitary matrices"
section_number: 4
pages: 21-22
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.917
latex_coverage_ratio: 0.968
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
[]{#sec:formal_model_pm label="sec:formal_model_pm"}

Recall from Section [\[sec:intro_model\]](#sec:intro_model){reference-type="ref" reference="sec:intro_model"} the definition of $B_{k,n}$. Due to the relation between $B_{k,n}$ and the quantum cohomology of the Grassmannian whose ring structure is described by Schur functions, it is sometimes better to see $B_{k,n}$ as a graph of partitions (see Appendix [\[sec:quantum_cohomology\]](#sec:quantum_cohomology){reference-type="ref" reference="sec:quantum_cohomology"} for some reminders on partitions). We denote by $\Lambda_{k}$ the set of generalized partitions of length $k\geq 1$, which are nondecreasing sequences of integers of length $k$ and $\Lambda_{k,n}$ the set of partitions of length $k$ such that the first part is smaller that $n-k$. There is a bijection $\phi$ from $\Lambda_{k,n}$ to $B_{k,n}$ defined by the shift $$\phi(\lambda)=\lambda+I_0,$$ where we recall that $I_0=(k-1,\ldots,0)$. By the latter bijection, $\phi(\emptyset)=I_0$ and we then have $\phi^{-1}(I)=I-I_0$. Since we will make an extensive use of the maps $\phi$ and $\phi^{-1}$, we will simply write $I_{\lambda}=\phi(\lambda)$ and $\lambda_{I}=\phi^{-1}(I)$ when there is no ambiguity. Remark that the map $\phi$ is independent of $n$ and extends to a map from $\Lambda_{k}$ to $B_{k}$, where $B_{k}$ denotes the set of increasing sequences of integers of length $k$. The graph structure of $B_{k,n}$ yields a graph structure on $\Lambda_{k,n}$ given by the following rule, which is a specialization of the so-called quantum Pieri rule, see [@B].

::: lemma
[]{#lem:equivalence_graph_pieri label="lem:equivalence_graph_pieri"} There is an oriented edge between $I$ and $J$ in $B_{k,n}$ if and only if either $\lambda_{I}\nearrow \lambda_{J}$ in the usual sense of partition or if $(\lambda_{I})_1=n-k$, $(\lambda_{I})_{k}>0$ and $\lambda_{J}=\widetilde{\lambda_{I}}$, where for $\lambda\in \Lambda_{k,n}$ such that $\lambda_1=n-k$ and $\lambda_k>0$, we write $$\tilde{\lambda}=(\lambda_2-1,\ldots,\lambda_k-1,0).$$
:::

The proof of the latter lemma is a simple transposition to partitions of the edge rule for $B_{k,n}$, which we do not detail here. Finally, recall from Section [\[subsec:intro_model\]](#subsec:intro_model){reference-type="ref" reference="subsec:intro_model"} that we also embed $B_{k,n}$ into $T_{k}$ with the map $$\xi_n:\left\lbrace \begin{aligned}
&\quad B_{k,n}&\rightarrow &\quad T_{k}\\
& \quad \quad I&\mapsto& R_{\frac{k-1}{2n}} \left(\frac{2\pi}{n}I\right)
\end{aligned}\right.,$$ and we have set $T_{k,n}=\xi_{n}(B_{k,n})$. To summarize, we have then three sets of cardinal $\binom nk$ related together as in the following picture.

::: center
:::
