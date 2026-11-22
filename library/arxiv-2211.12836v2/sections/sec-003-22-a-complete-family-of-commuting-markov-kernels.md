---
doc_id: arxiv-2211.12836v2
doc_title: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY"
section_id: sec-003-22-a-complete-family-of-commuting-markov-kernels
section_title: "A complete family of commuting Markov kernels associated to Bk,n"
section_number: 2.2
pages: 4-6
source_pdf: 2211.12836v2.pdf
source_sha256: 4ffbb8b21f8b175d
toc_source: outline
text_source: latex
latex_prose_ratio: 0.96
latex_coverage_ratio: 0.955
doc_brief: "QUANTUM COHOMOLOGY OF THE GRASSMANNIAN AND UNITARY — We study a class of commuting Markov kernels whose simplest element describes the movement of k particles on a discrete circle of size n"
---
In order to state our main results, let us briefly explain how to associate to $B_{k,n}$ a family of Markov chains. By analogy with the space $L^2(T_k)$ of square integrable functions on $T_k$, denote by $L^2(B_{k,n})$ the Hermitian space of functions on $B_{k,n}$ with the distinguished orthonormal basis $\mathcal{B}_0=\left\{ e_{I}, I\in B_{k,n}\right\}$ given by $e_I(J)=\delta_{I,J}$. The edge structure of $B_{k,n}$ can then be encoded by the operator $A:L^2(B_{k,n})\rightarrow L^2(B_{k,n})$ given by $$A(e_I)=\sum_{I\nearrow J} e_{J}.$$ Since $B_{k,n}$ is strongly connected, the adjacency matrix $A$ is irreducible and thus there exist unique (up to a scaling) left and right Perron-Frobenius eigenvectors $h^l$ and $h^r$ of $A$ corresponding to the same Perron-Frobenius eigenvalue $\lambda$. The coordinates $h^r(I),h^l(I), \, I\in B_{k,n}$ are positive and $\lambda>0$ so that the transformed matrix $A^h$ given by $$A^h(e_J)=\frac{1}{\lambda}\sum_{I\in B_{k,n}}\frac{h^r(J)}{h^r(I)}A_{IJ}e_{I}$$ is a stochastic matrix with respect to the basis $\mathcal{B}_0$. The corresponding Markov chain started at any vertex converges then in probability to the invariant measure $\mu_h$ such that $\mu^h(I)=h^l(I)h^r(I)$ for $I\in B_{k,n}$, where $h^l$ and $h^r$ are normalized so that $h^l(I_0)=1$ and $\langle h^l,h^r\rangle=1$. We call $A^h$ the *$h$-transform* of $A$, by analogy with the specific situation where $A$ comes from the Markov kernel of a random walk on $\mathbb{Z}^k$ conditioned to stay in a finite connected domain $D\subset \mathbb{Z}^k$ (see [@Do-87]).

As we will see later, in the case of $B^{k,n}$ we have the explicit expression $$h^l(I)=\frac{\vert V(\xi_n(I))\vert}{V(I_0)}\,,\quad \mu^h(I)=\frac{\vert V(\xi_n(I))\vert^2}{n^k},$$ where $V(\vec{u})$ denoting the Vandermonde determinant of $(\exp(iu_j))_{1\leq j\leq k}$ for $\vec{u}=(u_1,\ldots,u_k)\in\mathbb{R}^k$, so that $$\label{eq:definition_Vandermonde}
V(\xi_n(I))=\prod_{j<j'}\left(e^{2i\pi I_{j'}/n}-e^{2i\pi I_{j}/n}\right)=(2i)^{k(k-1)/2}e^{(k-1)i\pi\frac{\langle I\rangle}{n}}\prod_{j<j'}\sin\left(\frac{(I_{j'}-I_{j})\pi}{n}\right).$$

As this can be readily seen from the graph structure of $B_{k,n}$, $$A^h(e_{I_0})=\frac{1}{\lambda}\frac{\vert V(I_0)\vert}{\vert V(I^1)\vert}e_{I^1}$$ where $I^1=\left\{k,k-2,k-3,\ldots,0\right\}$ and $\lambda$ is the Perron-Frobenius eigenvalue of $A$, which can be proven to be equal to $\sum_{a=1}^ke^{\frac{2i\pi(k+1-a)}{n}}$.

Anticipating with the continuous case, let us denote by $\mathcal{M}_{\geq 0}(B_{k,n})$ the set of positive measures on $B_{k,n}$, which can be viewed as vectors of $L^2(B_{k,n})$ with nonnegative entries, and $\mathcal{M}_{1}(B_{k,n})\subset \mathcal{M}_{\geq 0}(B_{k,n})$ the subset of vectors of $\mathcal{M}_{\geq 0}(B_{k,n})$ integrating to $1$ with respect to $\mu^h$, namely $$\mathcal{M}_{1}(B_{k,n})=\left\{\mu\in L^2(B_{k,n})\,\left\vert \sum_{I\in B_{k,n}} \mu(I)\mu^h(I)=1, \, \mu(I)\geq 0, I\in B_{k,n}\right.\right\}.$$ Elements of $\mathcal{M}_1(B_{k,n})$ are called *$h$-probability measures* in the sequel.

Our first results give a product structure on $L^2(B_{k,n})$ which restricts to a convolution product on the set $\mathcal{M}_{1}(B_{k,n})$ of $h$-probability measures.

::: proposition
[]{#prop:result_1 label="prop:result_1"} There exists a unique product $*:L^2(B_{k,n})\times L^2(B_{k,n})\rightarrow L^2(B_{k,n})$ such that

1.  $(L^2(B_{k,n}),+,*)$ is a commutative algebra,

2.  $\mathcal{M}_{1}(B_{k,n})*\mathcal{M}_{1}(B_{k,n})\subset \mathcal{M}_{1}(B_{k,n})$,

3.  $\frac{1}{\lambda}A^h(y)=\frac{e_{I^1}}{\mu^h(I^1)}*y$ for all $y\in L^2(B_{k,n})$,

4.  $\left(\frac{e_{I}}{\mu^h(I)}\right)* \left(\frac{e_{I_0}}{\mu^h(I_0)}\right)=\frac{e_{I}}{\mu^h(I)}$ for all $I\in B_{k,n}$.
:::

The existence of this convolution product on $L^2(B_{k,n})$ reflects the fact that $B_{k,n}$ is a positively multiplicative graph, as introduced in [@GLT]. Such graphs have several properties which we recall in Appendix [\[sec:pm_graph\]](#sec:pm_graph){reference-type="ref" reference="sec:pm_graph"}.

::: remark
[]{#rem:qcoho_convolution label="rem:qcoho_convolution"} The existence of this convolution product extending the action of $A$ and under which $\mathcal{M}_1(B_{k,n})$ is stable reflects the fact that $B_{k,n}$ encodes the Pieri rules in the small quantum cohomology of the Grassmannian (see Appendix [\[sec:quantum_cohomology\]](#sec:quantum_cohomology){reference-type="ref" reference="sec:quantum_cohomology"} for an introduction to this notion), which is an algebra having nonnegative structure coefficients in a particular basis. As we will see in Section [\[sec:formal_model_pm\]](#sec:formal_model_pm){reference-type="ref" reference="sec:formal_model_pm"}, the ring $(L^2(B_{k,n}),+,*)$ is actually isomorphic to the ring of symmetric functions specialized at $k$-tuples of distinct roots of $(-1)^{k+1}$. In particular, one can see through this isomorphism that the convolution by $\frac{e_{I^S}}{\mu^h(I^S)}$ for $I^S=(k,k-1,\ldots,1)$ corresponds to the operator $S^h$ on $L^2(B_{k,n})$, where $S$ is the shift operator $Se_{I}=e_{\tilde{I}}$ where $\{\tilde{I}_i,1\leq i\leq k\}=\{I_i+1 \,[n], 1\leq i\leq k\}$.
:::

::: remark
The convolution algebra $\mathcal{M}_1(B_{k,n})$ is also deeply related to the fusion algebra for the semi-simple Lie algebra of type $A_k$, see [@De]. The latter is also a quotient of the small quantum cohomology ring of the Grassmannian, and the structure coefficients of each of those algebras can be easily deduced from the other.
:::
