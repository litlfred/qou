---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-014-4-weighted-dependency-graphs-and-central-limit-t
section_title: "Weighted dependency graphs and central limit theorems"
section_number: 4
pages: 16-19
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.934
latex_coverage_ratio: 0.984
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
[]{#sec:clt label="sec:clt"} We will now use the bounds on cumulants obtained in the previous section to show that the family of random variables $\{\sigma_i : i \in \mathbb{Z}^d \}$ has a weighted dependency graph, and we will use this fact to deduce central limit theorems. We consider any of the regimes studied in the previous section: very high temperature, or very low temperature with $+$ boundary condition, or strong magnetic field with any boundary condition. To have uniform notation, we omit from now on the notation of the boundary condition in low temperature.

## Weighted dependency graph for the $\sigma_i$'s and central limit theorem for the magnetization

### The weighted dependency graph {#Sect:WDG_Spins}

We start by proving Theorem [\[th:depgraph\]](#th:depgraph){reference-type="ref" reference="th:depgraph"}, which gives a weighted dependency graph for $\{\sigma_i : i \in \mathbb{Z}^d \}$.

::: proof
*Proof of Theorem [\[th:depgraph\]](#th:depgraph){reference-type="ref" reference="th:depgraph"}.* Let $B = \{i_1, ..., i_r \}$ be a multiset of elements of $\mathbb{Z}^d$ and consider the induced subgraph $G[B].$ Then the maximum weight $\mathcal{M}(G[B])$ of a spanning tree in $G[B]$ satisfies $$\mathcal{M}(G[B])= \varepsilon^{\frac{\ell'_T(B)}{2}}.$$ Thus by Proposition [\[prop:2longueurs\]](#prop:2longueurs){reference-type="ref" reference="prop:2longueurs"}, $$\label{eq:boundsM}
\varepsilon^{\ell_T(B)} \leq \mathcal{M}(G[B]) \leq \varepsilon^{\frac{\ell_T(B)}{2}}.$$

By Proposition 5.2 of [@Valentin], it is sufficient to show that $$\left| \kappa_{\beta,h} \left( \prod_{\alpha \in B_1} \sigma_{\alpha}, \dots, \prod_{\alpha \in B_k} \sigma_{\alpha} \right) \right| \leq D_r \mathcal{M}(G[B]),$$ for some sequence $\mathbf{D}= (D_r)_{r \geq 1}$, where $B_1, \dots , B_k$ are the vertex-set of the connected components of $G_1[B]$, which is the graph induced by edges of weight $1$ of $G$ on $B$.

The vertices $i$ and $j$ are connected in $G_1$ if and only if $i=j$, because of the definition of the weights $w_e$ in $G.$ Moreover the random variables $\sigma_{i}$ are equal to $+1$ or $-1$, thus $$\sigma_i^j = \begin{cases}
\sigma_i \text{ if $j$ odd,}\\
1 \text{ if $j$ even.}
\end{cases}$$ Therefore it is sufficient to prove that for any set $B'$ of distinct $i_1, \dots, i_r$, $$\label{eq:condprop5.2}
\left| \kappa_{\beta,h} \left( \sigma_{i_1}, \dots, \sigma_{i_r} \right) \right| \leq D_r \mathcal{M}(G[B']).$$

But by Theorem [\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref" reference="thm:bound_joint_cumulants"}, $$\left| \kappa_{\beta,h} \left( \sigma_{i_1}, \dots, \sigma_{i_r} \right) \right| \leq D_r \varepsilon^{\ell_T(B')},$$ for some sequence $\mathbf{D}$ depending only on $r$. Thus using [\[eq:boundsM\]](#eq:boundsM){reference-type="eqref" reference="eq:boundsM"}, Equation [\[eq:condprop5.2\]](#eq:condprop5.2){reference-type="eqref" reference="eq:condprop5.2"} is proved, which completes the proof of the theorem. ◻
:::

::: remark
For all $i \in \mathbb{Z}^d$, let us define $X_i = \frac{\sigma_i+1}{2}$. Thus $X_i = 1$ (resp. $0$) if and only if $\sigma_i=1$ (resp. $-1$). In the remainder of this paper, it will sometimes be more convenient to consider the $X_i$'s rather than the $\sigma_i$'s. Since $\kappa_{\beta,h}(X_{i_1},\dots,X_{i_r})=\tfrac{1}{2^r} \kappa_{\beta,h}(\sigma_1,\dots,\sigma_r)$ for $r\ge 2$, the weighted graph $G$ defined in Theorem [\[th:depgraph\]](#th:depgraph){reference-type="ref" reference="th:depgraph"} is also a $\mathbf{C}$-weighted dependency graph for the family $\{X_i : i \in \mathbb{Z}^d \}$, for some sequence $\mathbf{C} = (C_r)_{r \geq 1}$.
:::

### The central limit theorem

We now use the weighted dependency graph from last section to obtain the central limit theorem for the magnetization.

We consider the Ising model on $\mathbb{Z}^d$, with inverse temperature $\beta$ and magnetic field $h$. For any positive integer $n$, we define $\Lambda_{n} := [-n,n]^d$ the $d$-dimensional cube centred at $0$ of side $2n$. We define the *magnetization* $$S_{n} := \sum_{i \in \Lambda_n} \sigma_i,$$ and let $v_n^{2}$ denote the variance of $S_n$. Let us further define the covariance $$\langle\sigma_i;\sigma_j\rangle_{\beta,h} := \langle\sigma_i \sigma_j\rangle_{\beta,h} -\langle\sigma_i\rangle_{\beta,h} \langle\sigma_j\rangle_{\beta,h}.$$

We now reprove the following well-known central limit for the magnetization $S_n$ (for an early reference, see [@Newman80]). This serves as a warm up, to illustrate the method of dependency graphs; moreover, some computation made in this proof will be re-used in the next section, when studying patterns.

::: theorem
[]{#th:cltmagnet label="th:cltmagnet"} Consider the Ising model on $\mathbb{Z}^d$, with inverse temperature $\beta$ and magnetic field $h$, such that either $h > h_1(d)$ or $(h=0;\, \beta < \beta_1(d))$ or $(h=0;\, \beta > \beta_2(d))$. Then, for some $v$, $$\frac{S_n - \mathbb{E}(S_n) }{\sqrt{|\Lambda_n|}} \xrightarrow[n\to\infty]{d} \mathcal{N}(0, v^{2}).$$ Moreover $v^2 >0$ so the Gaussian law is non-degenerate.
:::

We start by a lemma of [@Ellis] on the asymptotics of the variance of $S_n$.

::: lemma
[@Ellis Lemma V.7.1] []{#lem:ellis label="lem:ellis"} The limit $$v^{2} := \lim_{n \rightarrow \infty} \frac{v_n^{2}}{|\Lambda_n|}$$ exists as an extended real valued number and $$v^{2} = \sum_{i \in \mathbb{Z}^d} \langle\sigma_0;\sigma_i\rangle_{\beta,h}.$$
:::

But by Theorem [\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref" reference="thm:bound_joint_cumulants"}, in the regimes we consider, the cumulants (so in particular the covariance) are exponentially small, so the sum is absolutely convergent and we actually have the stronger statement:

::: corollary
[]{#cor:ellisfini label="cor:ellisfini"} Suppose that either $h > h_1$ or ($h=0$ and $\beta < \beta_1$) or ($h=0$ and $\beta > \beta_2$). The limit $$v^{2} := \lim_{n \rightarrow \infty} \frac{v_n^{2}}{|\Lambda_n|} =\sum_{i \in \mathbb{Z}^d} \langle\sigma_0;\sigma_i\rangle_{\beta,h}$$ is finite.
:::

::: proof
*Proof of Theorem [\[th:cltmagnet\]](#th:cltmagnet){reference-type="ref" reference="th:cltmagnet"}.* We will use Theorem [\[th:4.11modif\]](#th:4.11modif){reference-type="ref" reference="th:4.11modif"}. Let $G$ be the weighted dependency graph defined in Theorem [\[th:depgraph\]](#th:depgraph){reference-type="ref" reference="th:depgraph"}. Then for all $n$, $G[\Lambda_n]$ is a $\mathbf{C}$-weighted dependency graph for $\{\sigma_i; i \in \Lambda_n\}$. The number of vertices of $G[\Lambda_n]$ is $$N_n = \left| \Lambda_n \right| = (2n+1)^d,$$ and its maximal weighted degree is $$\Delta_n -1 = \max_{i \in \Lambda_n} \sum_{j \in \Lambda_n} \varepsilon^{\frac{\|i - j\|_1}{2}}.$$

There are $2^d {d+y-1 \choose d-1}$ points at distance $y$ of $0$ in $\mathbb{Z}^d$. Indeed such a point has coordinates $(y_1, \dots, y_d)$ such that $|y_1| + \cdots + |y_d|=y.$ There are ${d+y-1 \choose d-1}$ choices for the values of $|y_1|, \dots, |y_d|$, and each $y_i$ can be either positive or negative, which multiplies the number of choices by $2^d.$ Thus there are at most $2^d {d+y-1 \choose d-1}$ points at distance $y$ of any point $x$ in $\Lambda_n$, and $$\Delta_n -1 \leq \sum_{y=0}^{2dn} \varepsilon^{\frac{y}{2}} 2^d {d+y-1 \choose d-1}
 \leq C,$$ for some constant $C$ because the infinite series is absolutely convergent.

We now have to find a sequence $(a_n)$ and integers $s$ and $v$ such that conditions (1)-(3) of Theorem [\[th:4.11modif\]](#th:4.11modif){reference-type="ref" reference="th:4.11modif"} are satisfied. We set for all n, $a_n= \sqrt{|\Lambda_n|}=(2n+1)^{\frac{d}{2}},$ $v= \sqrt{ \sum_{i \in \mathbb{Z}^d} \langle\sigma_0;\sigma_i\rangle_{\beta,h}}$ as in Lemma [\[lem:ellis\]](#lem:ellis){reference-type="ref" reference="lem:ellis"} and we can choose $s$ to be any integer $\geq 3$.

Now condition (1) is satisfied because of Lemma [\[lem:ellis\]](#lem:ellis){reference-type="ref" reference="lem:ellis"}, as $$\frac{v_n^{2}}{|\Lambda_n|} = \frac{v_n^{2}}{a_n^2} \xrightarrow[n \to\infty]{} v^{2}.$$

Condition (2) is also satisfied as $a_n^2 = (2n+1)^d = N_n$.

Finally, for some constant $C'$, $$\left( \frac{N_n}{\Delta_n} \right) ^{\frac{1}{s}} \frac{\Delta_n}{a_n} \leq C' \frac{(2n+1)^{\frac{d}{s}}}{(2n+1)^{\frac{d}{2}}},$$ and the right-hand side tends to $0$ as $n$ tends to infinity for $s \geq 3$. So (3) is satisfied too.

The central limit theorem is proved.

Moreover, whatever the values of $\beta$ and $h$ are, the spin at $0$ is not constant, thus $\langle \sigma_0,\sigma_0 \rangle_{\beta,h} >0$. On the other hand, because of the GKS inequalities [@Griffiths; @KS], for all $i \in \mathbb{Z}^d$, $\langle\sigma_0;\sigma_i\rangle_{\beta,h} \geq 0$ (see eg. [@Velenik]). Therefore, $$v^{2} = \langle\sigma_0,\sigma_0\rangle_{\beta,h} + \sum_{i \in Z^d \setminus \{0\} } \langle\sigma_0;\sigma_i\rangle_{\beta,h} > 0,$$ which ends the proof of the theorem. ◻
:::
