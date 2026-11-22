---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-018-42-dependency-graphs
section_title: "Dependency graphs"
section_number: 4.2
pages: 31-35
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.908
latex_coverage_ratio: 0.984
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#subsec:dependency label="subsec:dependency"} In this paragraph, we will see that the uniform bounds on cumulants are satisfied for sums $S_n = \sum_{i=1}^n A_{i,n}$ of dependent random variables with specific dependency structure.

More precisely, if $(A_v)_{v \in V}$ is a family of real valued random variables, we call *dependency graph* for this family a graph $G=(V,E)$ with the following property: if $V_1$ and $V_2$ are two disjoint subsets of $V$ with no edge $e \in E$ joining a vertex $v_1 \in V_1$ to a vertex $v_2 \in V_2$, then $(A_v)_{v \in V_1}$ and $(A_v)_{v \in V_2}$ are independent random vectors. For instance, let $(A_1,\ldots,A_7)$ be a family of random variables with dependency graph drawn on Figure [1](#fig:dependency){reference-type="ref" reference="fig:dependency"}. Then the vectors $(A_1,A_2,A_3,A_4,A_5)$ and $(A_6,A_7)$ corresponding to different connected components must be independent. Moreover, note that $(A_1,A_2)$ and $(A_4,A_5)$ must be independent as well: although they are in the same connected component of the graph $G$, they are not directly connected by an edge $e \in E$.

<figure id="fig:dependency">
<div class="center">

</div>
<figcaption>A dependency graph for <span class="math inline">7</span> real-valued random variables.<span id="fig:dependency" label="fig:dependency"></span></figcaption>
</figure>

::: theorem
[]{#thm:boundcumulant label="thm:boundcumulant"} Let $(A_v)_{v \in V}$ be a family of random variables, with $|A_v| \leq A$ a.s., for all $v \in V$. We suppose that $G=(V,E)$ is a dependency graph for the family and denote

-   $N=\tfrac{\sum_{v\in V} \mathbb{E}|A_v|}{A} \le \mathrm{card}\, V$;

-   $D$ the maximum degree of a vertex in $G$ *plus one*.

If $S=\sum_{v \in V} A_v$, then for all $r \geq 1$, $$|\kappa^{(r)}(S)| \leq N\,r^{r-2}\,(2D)^{r-1}\,A^r.$$
:::

Consider a sequence $(S_n)_{n \in \mathbb{N}}$, where each $S_n$ writes as $\sum_{v \in V_n} A_{v,n}$, with the $A_{v,n}$ uniformly bounded by $A$ (in a lot of examples, the $A_{v,n}$ are indicator variables, so that we can take $A=1$). Set $$N_n=\tfrac{\sum_{v\in V_n} \mathbb{E}|A_{v,n}|}{A}$$ and assume that, for each $n$, $(A_{v,n})_{v \in V_n}$ has a dependency graph of maximal degree $D_n-1$. Then the sequence $(S_n)_{n \in \mathbb{N}}$ admits uniform bounds on cumulants with parameters $(D_n,N_n,A)$ and the result of the previous section applies. Note that in this setting we have the bound $\widetilde{\sigma}_n\leq A$, so the bound of Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"} holds with the better constant 52.52.

::: remark
The parameter $D$ is equal to the maximal number of neighbors of a vertex $v \in V$, plus $1$. In the following, we shall simply call $D$ the maximal degree, being understood that one always has to add $1$. Another way to deal with this convention is to think of dependency graphs as having one loop at each vertex.
:::

::: example
The following example, though quite artificial, shows that one can construct families of random variables with arbitrary parameters $N$ and $D$ for their dependency graphs. Let $(U_k)_{k \in \mathbb{Z}/ N\mathbb{Z}}$ be a family of independent Bernoulli random variables with $\mathbb{P}[U_k=1]=1-\mathbb{P}[U_k=0]=q$; and for $i \in \mathbb{Z}/ N\mathbb{Z}$, $$A_{i} = 2\left(\prod_{k=i+1}^{i+D} U_k\right)-1.$$ Each $A_i$ is a Bernoulli random variable with $\mathbb{P}[A_i=1] = 1-\mathbb{P}[A_i=-1] = q^D$, which we denote $p$ ($p$ is considered independent of $N$). We are interested in the fluctuations of $S=\sum_{i=1}^N A_i$. Note that the partial sums $\sum_{i=1}^{k \leq N}A_i$ correspond to random walks with correlated steps: as $D$ increases, the consecutive steps of the random walk have a higher probability to be in the same direction, and therefore, the variance of the sum $S = \sum_{i=1}^N A_i$ grows. We refer to Figure [2](#fig:correlated_walk){reference-type="ref" reference="fig:correlated_walk"}, where three such random walks are drawn, with parameters $p=\frac{1}{2}$, $N=1000$ and $D \in \{5,15,30\}$.

<figure id="fig:correlated_walk">
<div class="center">

</div>
<figcaption>Random walks with <span class="math inline">1000</span> steps and correlation lengths <span class="math inline"><em>D</em> = 5</span>, <span class="math inline"><em>D</em> = 15</span> and <span class="math inline"><em>D</em> = 30</span>.<span id="fig:correlated_walk" label="fig:correlated_walk"></span></figcaption>
</figure>

If $d(i,j) \geq D$ in $\mathbb{Z}/N\mathbb{Z}$, then $A_i$ and $A_j$ do not involve any common variable $U_k$, and they are independent. It follows that if $G$ is the graph with vertex set $\mathbb{Z}/N\mathbb{Z}$ and with an edge $e$ between $i$ and $j$ if $d(i,j) \leq D$, then $G$ is a dependency graph for the $A_i$'s. This graph has $N$ vertices, and maximal degree $2D-1$. Moreover, one can compute exactly the expectation and the variance of $S=\sum_{i=1}^N A_i$: $$\begin{aligned}
\mathbb{E}[S] &= N(2p-1); \\
\mathrm{Var}(S) &= 4 \sum_{i,j=1}^N \mathrm{cov}(U_{i+1}\cdots U_{i+D}, U_{j+1}\cdots U_{j+N}) \\
&=4 \sum_{i,j=1}^N \big(q^{D+\min(D,d(i,j))} -p^2\big) = 4Np \sum_{j=-(D-1)}^{D-1} (q^{|j|}-p) \\
&= 4Np \left(\frac{1+p^{\frac{1}{D}}-2p}{1-p^{\frac{1}{D}}}-(2D-1)p\right).
\end{aligned}$$ If $N$ and $D$ go to infinity with $D=o(N)$, then $q=p^{\frac{1}{D}} = 1+\frac{\log p}{D} + O(\frac{1}{D^2})$, and $$\begin{aligned}
\mathbb{E}[S] &= N(2p-1); \\
\mathrm{Var}(S) &= 8N(D+O(1))\,p\left(\frac{1-p}{-\log p}-p \right).
\end{aligned}$$ So, one can apply Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"} to the sum $S$, and one obtains: $$d_\mathrm{Kol}\left(\frac{S-\mathbb{E}[S]}{\sqrt{\mathrm{Var}(S)}},\,\mathcal{N}_{\mathbb{R}}(0,1)\right) \leq \frac{6}{\left(p\left(\frac{1-p}{-\log p}-p\right)\right)^{3/2}}\,\sqrt{\frac{D}{N}}.$$
:::

::: example
Fix $p \in (0,1)$, and consider a random *Erdös--Rényi graph* $G=G_n=G(n,p)$, which means that one keeps at random each edge of the complete graph $K_n$ with probability $p$, independently from every other edge. Note that we only consider the case of fixed $p$ here; for $p \to 0$, we would get rather weak bounds, see [@FMN16 Section 10.3.3] for a discussion on bounds on cumulants in this framework.

Let $H=(V_H,E_H)$ and $G=(V_G,E_G)$ be two graphs. The number of copies of $H$ in $G$ is the number of injections $i : V_H \to V_G$ such that, if $(h_1,h_2) \in E_H$, then $(i(h_1),i(h_2)) \in E_G$. In random graph theory, this is called the *subgraph count* statistics; we denote it by $I(H,G)$. We refer to Figure [3](#fig:counttriangle){reference-type="ref" reference="fig:counttriangle"} for an example, where $H=K_3$ is the triangle and $G$ is a random Erdös--Rényi graph of parameters $n=30$ and $p=\frac{1}{10}$.

<figure id="fig:counttriangle">
<div class="center">

</div>
<figcaption>Count of triangles in a random Erdös–Rényi graph of parameters <span class="math inline"><em>n</em> = 30</span> and <span class="math inline"><em>p</em> = 0.1</span>. Here, there are <span class="math inline">4 × 3! = 24</span> ways to embed a triangle in the graph.</figcaption>
</figure>

One can always write $I(H,G)$ as a sum of dependent random variables. Identify $V_H$ with $\left[\!\left[1,k\right]\!\right]$ and $V_G$ with $\left[\!\left[1,n\right]\!\right]$, and denote $\mathfrak{A}(n,k)$ the set of arrangements $(a_1,\ldots,a_k)$ of size $k$ in $\left[\!\left[1,n\right]\!\right]$. Given such an arrangement, the *induced subgraph* $G[a_1,\ldots,a_k]$ is the graph with vertex set $\left[\!\left[1,k\right]\!\right]$, and with an edge between $i$ and $j$ if $(a_i,a_j) \in E_G$. Then, $$I(H,G) = \sum_{A \in \mathfrak{A}(n,k)} I_A(H,G),$$ where $I_A(H,G)=1$ if $H \subset G[A]$, and $0$ otherwise.

A dependency graph for the random variables $I_A(H,G_n)$ has vertex set $\mathfrak{A}(n,k)$ of cardinality $N_n = n^{\downarrow k} =n(n-1)(n-2)\cdots (n-k+1)$, and an edge between two arrangements $(a_1,\ldots,a_k)$ and $(b_1,\ldots,b_k)$ if they share at least two points (otherwise, the random variables $I_A(H,G_n)$ and $I_B(H,G_n)$ involve disjoint sets of edges and are therefore independent). As a consequence, the maximal degree of the graph is smaller than $$D_n=\left(\binom{k}{2}^2 2(n-2)(n-3)\cdots (n-k+1) \right),$$ and of order $n^{k-2}$. Therefore, $\frac{D_n}{N_n} \leq \frac{2 \binom{k}{2}^2}{n(n-1)} = O(\frac{1}{n^2})$, and on the other hand, if $h$ is the number of edges of $H$, one can compute the asymptotics of the expectation and of the variance of $I(H,G_n)$: $$\begin{aligned}
\mathbb{E}[I(H,G_n)] &= n^{\downarrow k} p^h ;\\
 \mathrm{Var}(I(H,G_n)) &= 2h^2p^{2h-1}(1-p)\,n^{2k-2} + O(n^{2k-3}),
\end{aligned}$$ see [@FMN16 Section 10] for the details of these computations. In particular, $$\lim_{n \to \infty} \frac{\mathrm{Var}(S_n)}{N_n\,D_n} = p^{2h-1}(1-p) \left(\frac{h}{\binom{k}{2}}\right)^{\!2} = \widetilde{\sigma}^2 >0.$$ Thus, using Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"}, we get $$d_\mathrm{Kol}\left(\frac{I(H,G_n) - \mathbb{E}[I(H,G_n)]}{\sqrt{\mathrm{Var}(I(H,G_n))}},\,\mathcal{N}_{\mathbb{R}}(0,1)\right) \leq \frac{4.65\,(k(k-1))^4}{p^{3h}\,(\frac{1}{p}-1)^{3/2}\,h^3} \,\,\frac{1}{n}$$ for $n$ large enough. For instance, if $T_n=I(K_3,G_n)$ is the number of triangles in $G_n$, then $$\begin{aligned}
\mathbb{E}[T_n]&=n^{\downarrow 3}\,p^3 \\
\mathrm{Var}[T_n]&=18\,n^{\downarrow 4}\,p^5(1-p) + 6\,n^{\downarrow 3}\,p^3(1-p^3)
\end{aligned}$$ and $$\begin{aligned}
&d_\mathrm{Kol}\left(\frac{T_n-n^{\downarrow 3}p^3}{\sqrt{18\,n^{\downarrow 4}\,p^5(1-p) + 6\,n^{\downarrow 3}\,p^3(1-p^3)}},\,\mathcal{N}_{\mathbb{R}}(0,1)\right) \\
&\leq \frac{234}{p^9(\frac{1}{p}-1)^{\frac{3}{2}}}\,\frac{1}{n} \, (1 +O(\tfrac1n)).
\end{aligned}$$

This result is not new, except maybe the explicit constant. We refer to [@BKR89] for an approach of speed of convergence for subgraph counts using Stein's method. More recently, Krokowski, Reichenbachs and Thäle [@KRT15] applied Malliavin calculus to the same problem. Our result corresponds to the case where $p$ is constant of their Theorem 1. Similar bounds could be obtained by Stein's method, see [@Rin94].
:::

To conclude our presentation of the convergence of sums of bounded random variables with sparse dependency graphs, let us analyse precisely the case of *uncorrelated* random variables.

::: corollary
[]{#cor:uncorrelated label="cor:uncorrelated"} Let $S_n=\sum_{i=1}^{N_n} A_{i,n}$ be a sum of centered and bounded random variables, that are uncorrelated and with $\mathbb{E}[(A_{i,n})^2]=1$ for all $i$. We suppose that the random variables have a dependency graph of parameters $N_n \to +\infty$ and $D_n$.

1.  If $D_n = O((N_n)^{1/2-\varepsilon})$ for $\varepsilon>0$, then $Y_n=\frac{S_n}{\sqrt{N_n}}$ converges in law towards the Gaussian distribution.

2.  If $D_n = o((N_n)^{1/4})$, then the Kolmogorov distance between $Y_n$ and $\mathcal{N}_{\mathbb{R}}(0,1)$ is a $O((D_n)^2/(N_n)^{1/2})$.
:::

::: proof
*Proof.* It is an immediate consequence of Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"} and Proposition [\[thm:CLT_Janson\]](#thm:CLT_Janson){reference-type="ref" reference="thm:CLT_Janson"}, since $S_n$ admits uniform control on cumulants (see Theorem [\[thm:boundcumulant\]](#thm:boundcumulant){reference-type="ref" reference="thm:boundcumulant"}) and $$\mathrm{Var}(S_n) = \sum_{i=1}^{N_n} \mathbb{E}[(A_{i,n})^2] = N_n.\qquad\qed$$ ◻
:::
