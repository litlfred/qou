---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-022-52-uniform-weighted-dependency-graphs
section_title: "Uniform weighted dependency graphs"
section_number: 5.2
pages: 41-42
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.97
latex_coverage_ratio: 0.958
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
If $A_1,\ldots,A_r$ are real-valued random variables, there is a notion of joint cumulant that generalize the cumulants of Section [\[sec:dependency\]](#sec:dependency){reference-type="ref" reference="sec:dependency"}: $$\kappa(A_1,A_2,\ldots,A_r) = [z_1z_2\cdots z_r]\left(\log \mathbb{E}[\E^{z_1A_1+z_2A_2+\cdots+z_rA_r}]\right).$$ The joint cumulants are multilinear and symmetric functionals of $A_1,\ldots,A_r$. On the other hand, $$\kappa^{(r)}(X) = \kappa(X,X,\ldots,X)$$ with $r$ occurrences of $X$ in the right-hand side. In particular, if $S=\sum_{v \in V}A_v$ is a sum of random variables, then $$\kappa^{(r)}(S) = \sum_{v_1,\ldots,v_r \in V} \kappa(A_{v_1},A_{v_2},\ldots,A_{v_r}).$$

::: definition
[]{#def:UWDG label="def:UWDG"} Let $(A_v)_{v \in V}$ be a family of random variables defined on the same probability space. A weighted graph $G=(V,E,w_G)$ is a $C$-uniform weighted dependency graph for $(A_v)_{v \in V}$ if, for any multiset $B=\{v_1,\ldots,v_r\}$ of elements of $V$, one has $$\left| \kappa\big( A_v,\, v \in B \big) \right| \leq
    C^{|B|} \sum_{T \in \mathop{\mathrm{ST}}(G[B])} w(T).$$
:::

::: proposition
[]{#Prop:BoundCumulantUWDG label="Prop:BoundCumulantUWDG"} Let $(A_v)_{v \in V}$ be a finite family of random variables with a $C$-uniform weighted dependency graph $G$. Assume that $G$ has $N=|V|$ vertices, and maximal weighted degree $D-1$, that is: $$\forall v \in V,\,\,\,\sum_{\substack{v':\,v' \ne v \\ \{v,v'\} \in E_G}} w_G(\{v,v'\}) \leq D-1.$$ Then, for $r \ge 1$, $$\left| \kappa^{(r)}\left( \sum_{v \in V} A_v \right) \right|
  \le N\, r^{r-2} D^{r-1}\,C^r.$$
:::

Consider a sequence $(S_n)_{n\in \mathbb{N}}$, where each $S_n$ writes as $\sum_{v \in V_n} A_{v,n}$. Set $N_n=|V_n|$ and assume that, for each $n$, $(A_v)_{v \in V_n}$ has $C$-uniform weighted dependency graph of maximal degree $D_n-1$ (by assumption, $C$ does not depend on $n$). Then the sequence $(S_n)$ admits uniform bounds on cumulants with parameters $(\tfrac{D_n}{2},N_n,C)$ and the results of Section [\[sec:dependency\]](#sec:dependency){reference-type="ref" reference="sec:dependency"}, in particular Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"}, apply.

::: proof
*Proof.* By multilinearity and definition of a uniform weighted dependency graph, we have $$\left| \kappa_r\left( \sum_{v \in V} A_v \right) \right|
  \le C^r \sum_{v_1,\ldots,v_r} \sum_{T \in \mathop{\mathrm{ST}}(G[v_1,\ldots,v_r])} w(T). 
  \label{eq:BoundCumulants1}$$ By possibly adding edges of weight $0$, we may assume that $G[v_1,\ldots,v_r]$ is always the complete graph $K_r$ so that $\mathop{\mathrm{ST}}(G[v_1,\ldots,v_r]) \simeq \mathop{\mathrm{ST}}(K_r)$ as sets. The weight of a tree $T$ however depends on $v_1,\cdots,v_r$, namely $$w(T)=\prod_{\{i,j\} \in T} w_G(\{v_i,v_j\}),$$ where $w_G(\{v_i,v_j\})$ is the weight of the edge $\{v_i,v_j\}$ in $G$ (or $1$ if $v_i=v_j$).

With this viewpoint, we can exchange the order of summation in [\[eq:BoundCumulants1\]](#eq:BoundCumulants1){reference-type="eqref" reference="eq:BoundCumulants1"}. We claim that the contribution of a fixed tree $T \in \mathop{\mathrm{ST}}(K_r)$ can then be bounded as follows: $$\sum_{v_1,\ldots,v_r} w(T) = \sum_{v_1,\ldots,v_r} \prod_{\{i,j\} \in T} w_G(\{v_i,v_j\}) \leq N D^{r-1}.
    \label{eq:ContributionT}$$ Let us prove this claim by induction on $r$. The case $r=1$ is trivial. Up to renaming the vertices of $T$, we may assume that $r$ is a leaf of $T$ so that $T$ is obtained from a spanning tree $\widetilde{T}$ of $K_{r-1}$ by adding an edge $\{i_0,r\}$ for some $i_0<r$. Then $$\begin{aligned}
  &\sum_{v_1,\ldots,v_r} \prod_{\{i,j\} \in T} w_G(\{v_i,v_j\})\\
  &= \sum_{v_1,\ldots,v_{r-1}} \left( \prod_{\{i,j\} \in \widetilde{T}} w_G(\{v_i,v_j\}) 
  \right) \left[\sum_{v_r \in V}  w_G(\{v_{i_0},v_r\}) \right].
  
\end{aligned}$$ The expression in square brackets is by definition smaller than $D$ for all $v_{i_0}$ (the sum for $v_r \ne v_{i_0}$ is smaller than $D-1$ and the term for $v_r = v_{i_0}$ is 1). By induction hypothesis, the sum of the parenthesis is smaller than $N D^{r-2}$. This concludes the proof of [\[eq:ContributionT\]](#eq:ContributionT){reference-type="eqref" reference="eq:ContributionT"} by induction. The lemma now follows immediately, since the number of spanning trees of $K_r$ is well known to be $r^{r-2}$.0◻ ◻
:::

::: remark
A classical dependency graph with a uniform bound $A$ on all variables $A_v$ can be seen as a $C$-uniform weighted dependency graph for $C=2A$ (all edges have weight 1); see [@FMN16 Section 9.4]. In this case, Proposition [\[Prop:BoundCumulantUWDG\]](#Prop:BoundCumulantUWDG){reference-type="ref" reference="Prop:BoundCumulantUWDG"} reduces to Theorem [\[thm:boundcumulant\]](#thm:boundcumulant){reference-type="ref" reference="thm:boundcumulant"}. The proof of Proposition [\[Prop:BoundCumulantUWDG\]](#Prop:BoundCumulantUWDG){reference-type="ref" reference="Prop:BoundCumulantUWDG"} given here is a simple adaptation of the second part of the proof of Theorem [\[thm:boundcumulant\]](#thm:boundcumulant){reference-type="ref" reference="thm:boundcumulant"} (see [@FMN16 Chapter 9]) to the weighted context. The first, and probably the hardest part of the proof of Theorem [\[thm:boundcumulant\]](#thm:boundcumulant){reference-type="ref" reference="thm:boundcumulant"} consisted in showing that a classical dependency graph is indeed a $C$-uniform weighted dependency graph.
:::

::: remark
In the case where the set $V$ is a subset of $\mathbb{Z}^d$ and the weight function only depends on the distance, the notion of uniform weighted dependency graph coincides with the notion of *strong cluster properties*, proposed by Duneau, Iagolnitzer and Souillard in [@Duneau1]. These authors also observed that this implies uniform bounds on cumulants when $D$ is bounded, see [@Duneau1 Eq. (10)].
:::

::: remark
A weaker notion of weighted dependency graph, where the bound on cumulant is not uniform on $r$, was recently introduced in [@WDG]. This weaker notion only enables to prove central limit theorem, without normality zone or speed of convergence results. However, it seems to have a larger range of applications.
:::
