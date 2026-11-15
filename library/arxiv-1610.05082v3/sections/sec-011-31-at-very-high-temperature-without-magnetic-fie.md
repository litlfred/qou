---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-011-31-at-very-high-temperature-without-magnetic-fie
section_title: "At very high temperature, without magnetic field"
section_number: 3.1
pages: 8-12
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.971
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
[]{#Sect:CE_HT label="Sect:CE_HT"}

### The cluster expansion of the (multivariate) moment generating function

Let us start with the regime where $h=0$ and $\beta$ is sufficiently small (very high temperature).

Fix a finite domain $\Lambda \subset \mathbb{Z}^d$ and let $A=\{x_1,\dots,x_r\}$ be a set of points in $\Lambda$. We consider the (multivariate) moment generating function $$\left\langle \exp\left(\sum_{j=1}^r t_j \sigma_{x_j} \right) \right\rangle_{\Lambda;\beta,0} = 
\frac{\sum_{\omega \in \Omega_{\Lambda}} 
\exp\left(\sum_{j=1}^r t_j \sigma_{x_j}(\omega) \right) e^{-H_{\Lambda;\beta,0}(\omega)}}{Z_{\Lambda; \beta,0}}.$$

Let us call $Z^A_{\Lambda; \beta,0}$ the numerator of the right-hand side. The denominator $Z_{\Lambda; \beta,0}$ is then exactly $Z^\emptyset_{\Lambda; \beta,0}$. Let $\mathcal{E}^{\text{even}}_{A}$ (resp. $\mathcal{E}^{\text{even}}_{\Lambda,A}$) be the set of pairs $(E,B)$, where $E \subset \mathcal{E}_{\mathbb{Z}^d}$ (resp. $E \subset \mathcal{E}_\Lambda$) and $B\subseteq A$ are such that a vertex of $\Lambda$ is incident to an odd number of edges in $E$ if and only if it is in $B$. For such a pair $(E,B)$, we denote $\mathop{\mathrm{wt}}(E,B)=(\tanh\, \beta)^{|E|} \prod_{j \in B} (\tanh\, t_j)$.

::: lemma
We have $$Z^A_{\Lambda; \beta,0} = 2^{|\Lambda|} (\cosh\, \beta)^{|\mathcal{E}_\Lambda|}
\left(\prod_{j=1}^r \cosh(t_j) \right) \Xi^A_{\Lambda;\beta,0},
\label{eq:PartFunction_HighTemperature_Modified}$$ where $\Xi^A_{\Lambda;\beta,0}=\sum_{(E,B) \in \mathcal{E}^{\text{even}}_{\Lambda,A}} \mathop{\mathrm{wt}}(E,B)$. []{#lem:HTR label="lem:HTR"}
:::

::: proof
*Proof.* This proof is a straight-forward extension of the case $A=\emptyset$, see e.g. [@Velenik Eq. (5.40)]. We write in short $\sigma_i$ for $\sigma_i(\omega)$. Since $\sigma_{x_j}$ is in $\{-1,+1\}$, we can write $$\begin{aligned}
    \exp(t_j \sigma_{x_j}) &= \cosh(t_j) + \sigma_{x_j} \sinh(t_j) 
    = \cosh(t_j) \big(1 + \sigma_{x_j} \tanh(t_j));\\
    \exp(\beta \sigma_i \sigma_j) &= \cosh(\beta) \big(1 + \sigma_i \sigma_j \tanh(\beta) \big).
  
\end{aligned}$$ This gives the following expression for $Z^A_{\Lambda; \beta,0}$: $$Z^A_{\Lambda; \beta,0}= (\cosh\, \beta)^{|\mathcal{E}_\Lambda|}
  \left(\prod_{j=1}^r \cosh(t_j) \right) \sum_{\omega \in \Omega_{\Lambda}}
  \left[ \sum_{E \subseteq \mathcal{E}_\Lambda} \prod_{\{i,j\} \in E} (\sigma_i \sigma_j \tanh(\beta)) \right]\\
  \cdot\left[ \sum_{B \subseteq A} \prod_{x_j \in B} (\sigma_{x_j} \tanh(t_j)) \right].$$ Changing the order of summation we should evaluate, for $E \subseteq \mathcal{E}_\Lambda$ and $B \subseteq A$, the quantity $$\sum_{\omega \in \Omega_{\Lambda}}  \prod_{\{i,j\} \in E} 
  (\sigma_i \sigma_j) \prod_{x_j \in B} (\sigma_{x_j}).$$ By an easy symmetry argument, this sum is zero unless all $\sigma_i$'s appear an even number of times, which corresponds to the condition $(E,B) \in \mathcal{E}^{\text{even}}_{\Lambda,A}$. In this latter case, the sum is the number of spin configurations $|\Omega_{\Lambda}|=2^{|\Lambda|}$. This ends the proof of the high temperature expansion. ◻
:::

Pairs $(E,B)$ in $\mathcal{E}^{\text{even}}_{\Lambda,A}$ can be considered as subgraphs of $\Lambda$, where the vertices are all vertices incident to an edge of $E$ and the edge-set is precisely $E$ (vertices in $B$ must be adjacent to at least one edge in $E$). This graph has a unique decomposition (up to reordering) into $r$ connected components, each again being the graph of some $(E_i,B_i)$ (for $1 \le i \le r$). Notice that the weight function is multiplicative with respect to connected components, *i.e.* $\mathop{\mathrm{wt}}(E,B)=\prod_i \mathop{\mathrm{wt}}(E_i,B_i)$. Therefore using notation of [@Velenik], $$\Xi^A_{\Lambda;\beta,0} = 1 + \sum_{r \ge 1} \frac{1}{r!} \sum_{(E_1,B_1), \dots, (E_r,B_r) \atop \text{connected}}
\ \prod_{i=1}^r \mathop{\mathrm{wt}}(E_i,B_i) \, \prod_{1 \le i<j \le r} \delta\big[(E_i,B_i),(E_j,B_j) \big],$$ where $\delta\big[(E_i,B_i),(E_j,B_j) \big]=1$ if the graphs corresponding to $(E_i,B_i)$ and $(E_j,B_j)$ do not share a vertex, and $0$ otherwise (this factor encodes the fact that connected components should not intersect). We set $\zeta((E,B),(E',B'))=\delta\big[(E,B),(E',B')\big]-1$ as usual for cluster expansions.

To compute cumulants, we need an expansion of $\log\left(\left\langle \exp\left(i \sum_{j=1}^r t_j \sigma_{x_j} \right) \right\rangle_{\Lambda;\beta,0} \right)$ and thus of $\log(\Xi^A_{\Lambda;\beta,0})$. Such an expansion will be given by cluster expansion, but we should first check some conditions ensuring convergence, *e.g.* the ones given in [@Velenik Section 5.4]. We let $\overline{\mathop{\mathrm{wt}}}(E,B)=(\tanh\, \beta)^{|E|}$, which dominates all functions $\mathop{\mathrm{wt}}(E,B)$ when the $t_j$'s are complex parameters of moduli at most $\tanh^{-1}(1)$.

::: lemma
[]{#lem:Cv_CE_HighTemperature label="lem:Cv_CE_HighTemperature"} For $(E,B) \in \mathcal{E}^{\text{even}}_{\Lambda,A}$, let $a(E;B)=|V(E,B)|$, that is the number of vertices in the graph associated to $(E,B)$. Then, there exists a constant $\beta^{\text{ht}}_{\text{ce}}(d)$ such that the following holds for $\beta<\beta^{\text{ht}}_{\text{ce}}(d)$:

1.  for any $\Lambda \subset \mathbb{Z}$, we have $\displaystyle \qquad \sum_{(E,B) \in \mathcal{E}^{\text{even}}_{\Lambda,A}} |\overline{\mathop{\mathrm{wt}}}(E,B)| e^{a(E,B)}  < \infty ;$

2.  []{#item:deux label="item:deux"} for each fixed pair $(E_\star,B_\star)$ where $E_\star$ is a finite subset of $\mathcal{E}_{\mathbb{Z}^d}$ and $B^\star \subseteq A$, one has $$S_{(E_\star,B_\star)}:=\sum_{(E,B) \in \mathcal{E}^{\text{even}}_{A} \atop (E,B) \text{ connected}} |\overline{\mathop{\mathrm{wt}}}(E,B)| e^{a(E,B)}
    |\zeta\big[(E,B),(E_\star,B_\star)\big]| \le a(E_\star,B_\star).$$
:::

::: remark
To prove the convergence of cluster expansion, it is actually enough to prove a weaker version of Item [\[item:deux\]](#item:deux){reference-type="eqref" reference="item:deux"}, where $(E_\star,B_\star)$ is necessarily in $\mathcal{E}^{\text{even}}_{\Lambda,A}$ and the sum only runs on $(E,B) \in \mathcal{E}^{\text{even}}_{\Lambda,A}$. The stronger version stated here will nevertheless be useful in the proof of [\[lem:BoudingTheSum_HT\]](#lem:BoudingTheSum_HT){reference-type="ref" reference="lem:BoudingTheSum_HT"} below and is proved in the same way, which explains our choice.
:::

::: proof
*Proof.* The first condition is trivial since the set $\mathcal{E}^\text{even}_{\Lambda,A}$ is finite. Let us consider the second one. By definition, $\zeta\big[(E,B),(E_\star,B_\star)\big]=-1$ if $(E,B)$ and $(E_\star,B_\star)$ share a vertex and $0$ otherwise. Thus $$S_{(E_\star,B_\star)} \le \sum_{v \in V(E_\star,B_\star)} \left[\sum_{E \subset \mathcal{E}_{\mathbb{Z}^d} , B \subset \mathbb{Z}^d \text{ s.t. } (E,B) \text{ connected}
\atop \text{and } v \in V(E,B)}
|\overline{\mathop{\mathrm{wt}}}(E,B)|\, e^{|V(E,B)|}\right].$$ A simple translation argument shows that the quantity between brackets is independent of $v$ so that $$S_{(E_\star,B_\star)} \le  |V(E_\star,B_\star)| 
\left[\sum_{E \subset \mathcal{E}_{\mathbb{Z}^d}, B \subset \mathbb{Z}^d \text{ s.t. } (E,B) \text{ connected}
\atop \text{and } 0 \in V(E,B)}
|\overline{\mathop{\mathrm{wt}}}(E,B)|\, e^{|V(E,B)|}\right].$$ Note that $(E,B)$ connected implies in particular that $B$ is included in the vertex set of the graph associated to $E$. Therefore the sum can be simplified as a sum only over $E$ by paying a factor $2^{|V(E,B)|}$. Moreover connectedness implies $|V(E,B)| \le |E|+1$. Thus we get: $$S_{(E_\star,B_\star)} \le  |V(E_\star,B_\star)| \left[\sum_{E \subset \mathcal{E}_{\mathbb{Z}^d} \text{ connected} \atop \text{s.t. } 0 \in V(E)}
2^{|E|+1} \, (\tanh\, \beta)^{|E|} \, e^{|E|+1} \right].$$ The summand depends only on the size $k$ of $E$. From [@Velenik Lemma 3.59], the number of connected sets $E \subset \mathcal{E}_{\mathbb{Z}^d}$ containing $0$ of size $k$ is bounded from above by $(2d)^{2k}$, so that $$S_{(E_\star,B_\star)} \le |V(E_\star,B_\star)|  \left[ \sum_{k \ge 1} (2d)^{2k} \, 2^{k+1} \, (\tanh\, \beta)^{k}\, e^{k+1} \right].$$ For $\beta$ small enough, say $\beta < \beta^{\text{ht}}_{\text{ce}}(d)$, the sum is smaller than $1$ and the second inequality is fulfilled. ◻
:::

We can now state the *cluster expansion* of $\log(\Xi^A_{\Lambda;\beta,0})$. In this context, a cluster is a multiset $X=\{(E_1,B_1),\dots,(E_r,B_r)\}$ of elements of $\mathcal{E}^{\text{even}}_{\Lambda,A}$. The multiplicity of $(E,B)$ in the multiset $X$ is denoted $n_X(E,B)$. The support $\overline{X}$ is the union of the vertex-sets $V(E_i,B_i)$. We say that two clusters intersect if $\zeta\big[(E,B),(E_\star,B_\star)\big]=-1$ i.e. if they share a *vertex*.

::: proposition
For $\beta<\beta^{\text{ht}}_{\text{ce}}(d)$, We have the following expansion: $$\log(\Xi^A_{\Lambda;\beta,0})
= \sum_{X: \overline{X} \subset \Lambda} \Psi_{\beta}(X),
\label{eq:CE_HighTemperature}$$ where for a cluster $X= \{(E_1,B_1),\dots,(E_r,B_r)\}$, $$\Psi_\beta(X):= \left( \prod_{(E,B) \in \mathcal{E}^\text{even}_{\Lambda,A}}
 \frac{1}{n_X(E,B)!} \right)  \, \phi((E_1,B_1),\dots,(E_r,B_r)) \, \left( \prod_{ i=1}^r \mathop{\mathrm{wt}}(E_i,B_i) \right),$$ where $$\phi(( E_1,B_1),\dots,(E_r,B_r)) =\sum_{G \subset G_r\, \text{connected}} \left( \prod_{\{i,j\} \in G}
\zeta\big[(E_i,B_i),(E_j,B_j)\big] \right),$$ and $G_r$ denotes the complete graph on $r$ vertices. The convergence of the series in [\[eq:CE_HighTemperature\]](#eq:CE_HighTemperature){reference-type="ref" reference="eq:CE_HighTemperature"} holds in the sense of locally uniform convergence of analytic functions in the complex parameters $t_1$, ..., $t_r$ for $|t_1|,\dots,|t_r| \le \tanh^{-1}(1)$. []{#prop:CE_HighTemperature label="prop:CE_HighTemperature"}
:::

::: proof
*Proof.* This follows from the general theory of cluster expansions, see e.g. [@Velenik Chapter 5]. For the analyticity in the parameters, see specifically [@Velenik Section 5.5]. ◻
:::

Notice that the functional $\phi((E_1,B_1),\dots,(E_r,B_r))$ depends only on which pairs $(E_i,E_j)$ intersect and vanishes if $X$ can be split into two mutually non-intersecting subsets.

### Bounds on joint cumulants {#SectBoundHT}

Recall that $A=\{x_1,\dots,x_r\}$ is a set of points in the finite domain $\Lambda$. The joint cumulant $\kappa_{\Lambda;\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r})$ is the coefficient of $t_1 \dots t_r$ in $$\begin{gathered}
 \log \left\langle \exp\left(\sum_{j=1}^r t_j \sigma_{x_j} \right) \right\rangle_{\Lambda,\beta,0}
=\log Z^A_{\Lambda; \beta,0}  - \log Z^\emptyset_{\Lambda; \beta,0} \\
= |\Lambda|\, \log 2 + |\mathcal{E}_\Lambda| \, \log(\cosh\, \beta)
+\sum_{j=1}^r  \log (\cos\, t_j) + \log \Xi^A_{\Lambda;\beta,0}
-  \log Z^\emptyset_{\Lambda; \beta,0}.
\end{gathered}$$ Only the summand $\log \Xi^A_{\Lambda;\beta,0}$ contributes to the coefficient of $t_1 \dots t_r$. Therefore, using [\[prop:CE_HighTemperature\]](#prop:CE_HighTemperature){reference-type="ref" reference="prop:CE_HighTemperature"}, we have $$\label{eq:cumulants_cluster}
\kappa_{\Lambda;\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) = [t_1 \dots t_r] \sum_{X: \overline{X} \subset \Lambda} \Psi_{\beta}(X)
=  \sum_{X: \overline{X} \subset \Lambda}  [t_1 \dots t_r]  \Psi_{\beta}(X).$$ The exchange of infinite sum and coefficient extraction is valid since we have uniform convergence of analytic functions on a neighborhood of $0$. A cluster $X=\{(E_1,B_1),\dots,(E_r,B_r)\}$ contributes to the coefficient of $t_1 \dots t_r$ only if $A=B_1 \uplus \dots \uplus B_r \subseteq \overline{X}$. Then $$\begin{gathered}
\Psi_{\beta}(X) = 
\left( \prod_{(E,B) \in \mathcal{E}^\text{even}_{\Lambda,A}}
 \frac{1}{n_X(E,B)!} \right)  \, \varphi((E_1,B_1),\dots,(E_r,B_r)) \, (\tanh \beta)^{e(X)}\\
 \le C_r \, \bm{1}[X \text{ is connected}] \, (\tanh \beta)^{e(X)},
 
\end{gathered}$$ where $e(X)=|E_1|+\dots+|E_r|$ and $\bm{1}[\text{event}]$ is the indicator function of the corresponding event. Back to [\[eq:cumulants_cluster\]](#eq:cumulants_cluster){reference-type="ref" reference="eq:cumulants_cluster"}, we get $$|\kappa_{\Lambda;\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) | \le
  \sum_{X: \overline{X} \subset \Lambda, X\text{ connected,}\atop \text{and } A \subseteq \overline{X}}
  C_r (\tanh \beta)^{e(X)}.$$ Taking the limit $\Lambda \uparrow \mathbb{Z}^d$, we get a similar upper bound for the cumulant $\kappa_{\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r})$ under the probability measure $\mu_{\beta,0}$ corresponding to the whole lattice $\mathbb{Z}^d$: $$\label{eq:BoundCum1}
|\kappa_{\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) | \le
  \sum_{X\text{ connected}\atop \text{s.t. } A \subseteq \overline{X}}
  C_r (\tanh \beta)^{e(X)}.$$ The key point in the above formula is that any connected cluster $X$ with $A \subseteq \overline{X}$ fulfills $e(X) \ge \ell_T(A)$. We now need the following lemma, whose proof is inspired by the end of the proof of Theorem 5.27 in [@Velenik].

::: lemma
[]{#lem:BoudingTheSum_HT label="lem:BoudingTheSum_HT"} There exist constants $\beta^{\text{ht}}_{\text{jc}}(d)>0$ and $\varepsilon>0$ such that, for $\beta \le \beta^{\text{ht}}_{\text{jc}}(d)$, we have the following inequality: $$\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}\text{and } e(X) \ge R} (\tanh \beta)^{e(X)}
 \le \varepsilon^R.$$
:::

::: proof
*Proof.* The proof involves different values of the inverse temperature $\beta$ so that we will here make explicit the dependency of the weight in $\beta$: we write $\overline{\mathop{\mathrm{wt}}}_\beta(E,B)$ instead of $\overline{\mathop{\mathrm{wt}}}(E,B)$. We first prove that for $\beta' \le \beta^{\text{ht}}_{\text{jc}}(d)$, we have $$\label{eq:SumPsiLeqOne}
\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}} (\tanh \beta')^{e(X)} =\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}}  \prod_{i=1}^r \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_i,B_i)  \le 1.$$ This uses the same argument as in [@Velenik Eq. (5.31)]: $$\begin{gathered}
 \sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}}  \prod_{i=1}^r \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_i,B_i)
 \le \sum_{r \ge 1} r \sum_{(E_1,B_1) \text{ connected} \atop \text{s.t. } x_1 \in V(E_1,B_1)} \ \sum_{(E_2,B_2),\dots,(E_r,B_r)}
 \prod_{i=1}^r \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_i,B_i) \\
 \le \sum_{(E_1,B_1) \text{ connected} \atop \text{s.t. } x_1 \in V(E_1,B_1)}  \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_1,B_1) e^{|a(E_1,B_1)|}
 \le a(\emptyset, \{x_1\}) =1,
 
\end{gathered}$$ where we used [\[lem:Cv_CE_HighTemperature\]](#lem:Cv_CE_HighTemperature){reference-type="ref" reference="lem:Cv_CE_HighTemperature"} and [@Velenik Theorem 5.4]. This proves [\[eq:SumPsiLeqOne\]](#eq:SumPsiLeqOne){reference-type="eqref" reference="eq:SumPsiLeqOne"}.

Let us fix a value $\beta'$ as above. There exists a constant $\varepsilon<1$ such that for $\beta$ small enough, we have $\tanh \beta < \varepsilon\, \tanh \beta'$. We can now write $$\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X} \text{and } e(X) \ge R} (\tanh \beta)^{e(X)} 
 \le  \varepsilon^R \sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X} \text{and } e(X) \ge R} (\tanh \beta')^{e(X)} \le \varepsilon^R,$$ where the last inequality uses [\[eq:SumPsiLeqOne\]](#eq:SumPsiLeqOne){reference-type="eqref" reference="eq:SumPsiLeqOne"}. This ends the proof of the lemma. ◻
:::

Combining [\[eq:BoundCum1,lem:BoudingTheSum_HT\]](#eq:BoundCum1,lem:BoudingTheSum_HT){reference-type="ref" reference="eq:BoundCum1,lem:BoudingTheSum_HT"}, we get the desired bound: for $\beta \le \beta^{\text{ht}}_{\text{jc}}(d)$, $$|\kappa_{\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) | \le C_r \varepsilon^{\ell_T(A)}.$$
