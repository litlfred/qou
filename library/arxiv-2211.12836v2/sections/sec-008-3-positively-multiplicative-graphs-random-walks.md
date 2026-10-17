---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-008-3-positively-multiplicative-graphs-random-walks
section_title: "Positively multiplicative graphs, random walks and Fourier transform"
section_number: 3
pages: 14-15
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.908
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
[]{#sec:pm_graph label="sec:pm_graph"} In this section, we introduce the notion of integrable positively multiplicative graph which is the central property of the family of graph $\{B_{k,n}; 1\leq k\leq n\}$. We also introduce a general Fourier transform formalism to study a class of Markov chains naturally constructed from those graphs. Although some results of the present section are needed in the sequel of the paper, its content is quite general to enlighten a universal behavior.

Let us recall the definition of a positively multiplicative graph from [@GLT]. In this paper, a (directed) graph is the data of a finite set $V$ and a adjacency matrix $A$ on the vector space $L^2(V)=\bigoplus_{v\in V} e_v$, by which we mean an operator $A\in\mathcal{B}(L^2(V))$ such that $Ae_v=\sum_{v'\in V}A_{v'v}e_{v'}$ with $a_{vv'}\geq 0$ for all $v,v'\in V$. We add a Hilbert space structure on $L^2(V)$ with the scalar product $\langle e_v,e_{v'}\rangle=\delta_{vv'}$. The Hilbert space $L^2(V)$ can be seen as the algebra of $L^2$-functions on $V$ with respect to the counting measure, and for $x\in L^2(V)$, we write $x(v)$ for the coordinate of $x$ along $e_v$.

::: definition
[]{#def:PM-graph label="def:PM-graph"} A finite graph $\Gamma=(V,A)$ is said positively multiplicative (abbreviated PM) at $v_0\in V$ if there is a commutative algebra $\mathcal{A}$ such that $\mathbb{C}[A]\subset \mathcal{A}\subset End(L^2(V))$ and such that $\mathcal{A}$ admits a basis $\mathcal{B}=\{s_v,v\in V\}$ with $s_{v}e_{v_0}=e_v$, $$As_v=\sum_{v'\in V}A_{v'v}s_{v'},\, s_vs_{v'}\in\sum_{v''\in V}\mathbb{R}^+s_{v''}.$$ A PM graph is said integrable if $A$ is diagonalizable on $L^2(V)$.
:::

The algebra $\mathcal{A}$ is called the enveloping algebra of $\Gamma$ in the sequel. Remark that in general $\mathcal{A}$ is bigger that $\mathbb{C}[A]$, since $A$ may for example have eigenvalues with multiplicities larger than $1$. For a PM-graph there is a isomorphism $$\label{eq:isomor_L2_CA}
S:\left\lbrace \begin{aligned} L^2(V)&\rightarrow &\mathcal{A}\\ e_v&\mapsto &s_v\end{aligned}\right.$$ (which reflects the fact that $\dim \mathcal{A}=|V|$. It can then be deduced that $s_{v_0}=Id_{L^2(V)}$ (see [@GLT Theorem 3.12]).
