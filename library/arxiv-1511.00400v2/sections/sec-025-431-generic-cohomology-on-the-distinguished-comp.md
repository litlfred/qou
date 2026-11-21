---
doc_id: arxiv-1511.00400v2
doc_title: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties"
section_id: sec-025-431-generic-cohomology-on-the-distinguished-comp
section_title: "Generic cohomology on the distinguished component"
section_number: 4.3.1
pages: 29-30
source_pdf: 1511.00400v2.pdf
source_sha256: 6cb493049394ce3a
toc_source: outline
text_source: latex
latex_prose_ratio: 0.946
latex_coverage_ratio: 0.969
doc_brief: "Reidemeister torsion, hyperbolic three-manifolds, and character varieties — This is a survey on Reidemeister torsion for hyperbolic three-manifolds of ﬁnite volume."
---
[]{#sec:genericfunctions label="sec:genericfunctions"}

Some cohomology preliminaries are required before defining the torsion of $\operatorname{Sym}^{k_1,k_2}$ as function on $X_0(M^3)$. To simplify, use the notation $$\rho^{k_1,k_2}:=\operatorname{Sym}^{k_1,k_2}\circ\rho$$ for any representation $\rho\colon\pi_1M^3\to \mathrm{SL}_2(\mathbb{C})$.

::: definition
[]{#def:exceptional label="def:exceptional"} A character $\chi\in X_0(M^3)$ is called $(k_1,k_2)$-*exceptional* if there exists a representation $\rho\in\hom(\pi_1M^3,\mathrm{SL}_2(\mathbb{C}))$ with character $\chi_\rho=\chi$ such that $H^0(M^3;\rho^{k_1,k_2})\neq 0$.

The set of $(k_1,k_2)$-exceptional characters is denoted by $\mathrm{E}^{k_1,k_2}$.
:::

If a character is irreducible, then the set of representations with this character is precisely a conjugation orbit, but for reducible characters there may be representations with the same characters that are not conjugate.

Notice that in Proposition [\[prop:rational\]](#prop:rational){reference-type="ref" reference="prop:rational"} we have shown that $\mathrm{E}^{1,0}$ consist of the trivial character, when it belongs to $X_0(M^3)$ (hence $\mathrm{E}^{1,0}= \emptyset$ when $b_1(M^3)=1$).

::: lemma
[]{#lem:exceptionalclosed label="lem:exceptionalclosed"} If $k_1\neq k_2$, then a $(k_1,k_2)$-exceptional character is reducible. In particular the $(k_1,k_2)$-exceptional set $\mathrm{E}^{k_1,k_2}$ is a finite subset of $X_0(M^3)$.
:::

The proof of this lemma is provided in Appendix [\[sec:cohomology\]](#sec:cohomology){reference-type="ref" reference="sec:cohomology"} (Lemma [\[lem:exceptionalclosedA\]](#lem:exceptionalclosedA){reference-type="ref" reference="lem:exceptionalclosedA"}).

For further results, the following definition is convenient.

::: definition
A subset of $X_0(M^3)$ is *generic* if it is non empty and Zariski open. Here the ground field is assumed to be $\mathbb{C}$ when working with an holomorphic representation $\operatorname{Sym}^{k}$, and $\mathbb{R}$ for $\operatorname{Sym}^{k_1,k_2}$ when $k_2\neq 0$.
:::

For the generic behavior of other cohomology groups, one must distinguish the case where $k_1$ or $k_2$ is odd from the case they are both even. All proofs are postponed to Appendix [\[sec:cohomology\]](#sec:cohomology){reference-type="ref" reference="sec:cohomology"}.

::: prop
Let $M^3$ be orientable, hyperbolic and with one cusp. Assume $k_1\neq k_2$. []{#prop:generic label="prop:generic"}

(a) If $k_1$ or $k_2$ is odd, then $$\left\{ \chi_\rho\in X_0(M^3) \mid  \rho^{k_1,k_2}\textrm{ is acyclic}\right\}$$ is generic.

(b) If both $k_1$ and $k_2$ are even, then $$\left\{ \chi_\rho\in X_0(M^3) \mid \dim H_i(M^3 ; \rho^{k_1,k_2})=1 \textrm{ 
       for } i=1, 2 
       \textrm{ and 0 otherwise} \right\}$$ is generic.
:::

When $k_1$ and $k_2$ are even, we need to discuss the choice of basis in homology and perhaps we still need to remove a Zarsiki closed subset. We shall consider, for $k_1$ and $k_2$ even, $$\label{eqn:FF}
  \mathrm{F}^{k_1,k_2}= \left\{ \chi_\rho\in X_0(M^3) \mid \dim H^0(T^2 ; 
\rho^{k_1,k_2})\neq 1\right\}\cup \mathrm{E}^{k_1,k_2} \, ,$$ which is Zarsiki closed subset of $X_0(M^3)$ (over $\mathbb{C}$ for $k_2=0$, over $\mathbb{R}$ otherwise). In particular it is finite when $k_2=0$ or $k_1=0$.

::: lemma
[]{#lemma:generictorus label="lemma:generictorus"} Let $T^2$ denote the peripheral torus. If both $k_1$ and $k_2$ are even, then $\mathrm{F}^{k_1,k_2}$ is a Zarsiki closed subset of $X_0(M^3)$ (over $\mathbb{C}$ for $k_2=0$ or $k_1=0$, over $\mathbb{R}$ otherwise). In particular it is finite when $k_2=0$ or $k_1=0$.
:::

Consider the cap product $$\cap\colon H^0(T^2; \rho^{k_1,k_2})\times H_i(T^2; \mathbb{C})\to H_i(T^2; 
\rho^{k_1,k_2}).$$ It can be described as follows. Choose $a\in H^0(T^2; \rho^{k_1,k_2})$, $a\neq 
0$, and view it as an element of $\mathbb{C}^{(n_1+1)(n_2+1)}$ invariant by the action of $\rho^{k_1,k_2} (\pi_1 T^2)$. Any element in $H_i(T^2; \mathbb{C})$ is represented by a simplicial cycle: $z\in C_*(K; \mathbb{C})$ with $\partial z=0$ (here $K$ is a triangulation of $T^2$). Choose a lift of $z$ to the universal covering, $\tilde z\in C_*(\widetilde K; \mathbb{C})$, then $a\otimes \tilde z\in C_i(K;\rho^{k_1,k_2})$ is a cocycle and $$\label{eqn:cap}
a\cap [z]= [a\otimes \tilde z] ,$$ where the brackets denote the class in homology.

In the next proposition $[T^2]\in H_2(T^2; \mathbb{Z})$ denotes a fundamental class, $\langle \cdot \rangle$ the linear span, and $i\colon T^2\to M^3$ the inclusion.

::: prop
[]{#prop:genericbasis label="prop:genericbasis"} Let $k_1\neq k_2$ be even integers. For $0\neq a\in  H^0(T^2; \rho^{k_1,k_2})$ and $0\neq \gamma\in H_1(T^2; \mathbb{C})$, the set $$\begin{gathered}
  \left\{ \chi_\rho\in X_0(M^3) \mid \langle i_*(a\cap \gamma ) \rangle = 
H_1(M^3;    \rho^{k_1,k_2})\textrm{ and }   \right.            
   \\
\left.    \langle i_*(a\cap [T^2]) \rangle = H_2(M^3;    \rho^{k_1,k_2})
   \right\} 
   
\end{gathered}$$ is generic.
:::
