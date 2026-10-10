---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-010-3-cluster-expansions-and-bounds-on-joint-cumulan
section_title: "Cluster expansions and bounds on joint cumulants"
section_number: 3
pages: 8-16
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.96
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
[]{#sec:cluster label="sec:cluster"}

The cluster expansion is a powerful tool in statistical mechanics, which consists in studying a system in terms of macroscopic geometrical objects instead of considering its original microscopic components. It was introduced in a work of Mayer and Montroll [@Mayer] studying molecular distribution and has since been used in several other topics; for the Ising model, see for example [@Farrell] or Chapter $5$ of [@Velenik]. In this section, we will use the cluster expansion in three different regimes of the Ising model to prove the bounds on joint cumulants of Theorem [\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref" reference="thm:bound_joint_cumulants"}. This will later be useful to apply the theory of weighted dependency graphs. Theorem [\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref" reference="thm:bound_joint_cumulants"} is proved in [\[SectBoundHT,SectBoundLT,SectBoundMF\]](#SectBoundHT,SectBoundLT,SectBoundMF){reference-type="ref+label" reference="SectBoundHT,SectBoundLT,SectBoundMF"}, depending on the considered regime.

::: remark
As already mentioned, cluster expansion is a key step to obtain bounds for cumulants in each of the three regimes. Therefore we will use each time classical notation for cluster expansion, such as $\Xi$, $\mathop{\mathrm{wt}}$, ... Note however that these quantities may have different meanings in different regimes. Since they are only used for the proof of [\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref+label" reference="thm:bound_joint_cumulants"} and since the proofs in the different regimes are independent from each other, this should not create any difficulty.
:::

## At very high temperature, without magnetic field {#Sect:CE_HT}

### The cluster expansion of the (multivariate) moment generating function

Let us start with the regime where $h=0$ and $\beta$ is sufficiently small (very high temperature).

Fix a finite domain $\Lambda \subset \mathbb{Z}^d$ and let $A=\{x_1,\dots,x_r\}$ be a set of points in $\Lambda$. We consider the (multivariate) moment generating function $$\left\langle \exp\left(\sum_{j=1}^r t_j \sigma_{x_j} \right) \right\rangle_{\Lambda;\beta,0} = 
\frac{\sum_{\omega \in \Omega_{\Lambda}} 
\exp\left(\sum_{j=1}^r t_j \sigma_{x_j}(\omega) \right) e^{-H_{\Lambda;\beta,0}(\omega)}}{Z_{\Lambda; \beta,0}}.$$

Let us call $Z^A_{\Lambda; \beta,0}$ the numerator of the right-hand side. The denominator $Z_{\Lambda; \beta,0}$ is then exactly $Z^\emptyset_{\Lambda; \beta,0}$. Let $\mathcal{E}^{\text{even}}_{A}$ (resp. $\mathcal{E}^{\text{even}}_{\Lambda,A}$) be the set of pairs $(E,B)$, where $E \subset \mathcal{E}_{\mathbb{Z}^d}$ (resp. $E \subset \mathcal{E}_\Lambda$) and $B\subseteq A$ are such that a vertex of $\Lambda$ is incident to an odd number of edges in $E$ if and only if it is in $B$. For such a pair $(E,B)$, we denote $\mathop{\mathrm{wt}}(E,B)=(\tanh\, \beta)^{|E|} \prod_{j \in B} (\tanh\, t_j)$.

::: lemma
We have $$\begin{equation}
Z^A_{\Lambda; \beta,0} = 2^{|\Lambda|} (\cosh\, \beta)^{|\mathcal{E}_\Lambda|}
\left(\prod_{j=1}^r \cosh(t_j) \right) \Xi^A_{\Lambda;\beta,0},
\label{eq:PartFunction_HighTemperature_Modified}
\end{equation}$$ where $\Xi^A_{\Lambda;\beta,0}=\sum_{(E,B) \in \mathcal{E}^{\text{even}}_{\Lambda,A}} \mathop{\mathrm{wt}}(E,B)$. []{#lem:HTR label="lem:HTR"}
:::

::: proof
*Proof.* This proof is a straight-forward extension of the case $A=\emptyset$, see e.g. [@Velenik Eq. (5.40)]. We write in short $\sigma_i$ for $\sigma_i(\omega)$. Since $\sigma_{x_j}$ is in $\{-1,+1\}$, we can write $$\begin{align*}
    \exp(t_j \sigma_{x_j}) &= \cosh(t_j) + \sigma_{x_j} \sinh(t_j) 
    = \cosh(t_j) \big(1 + \sigma_{x_j} \tanh(t_j));\\
    \exp(\beta \sigma_i \sigma_j) &= \cosh(\beta) \big(1 + \sigma_i \sigma_j \tanh(\beta) \big).
\end{align*}$$ This gives the following expression for $Z^A_{\Lambda; \beta,0}$: $$Z^A_{\Lambda; \beta,0}= (\cosh\, \beta)^{|\mathcal{E}_\Lambda|}
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
To prove the convergence of cluster expansion, it is actually enough to prove a weaker version of Item [\[item:deux\]](#item:deux){reference-type="eqref" reference="item:deux"}, where $(E_\star,B_\star)$ is necessarily in $\mathcal{E}^{\text{even}}_{\Lambda,A}$ and the sum only runs on $(E,B) \in \mathcal{E}^{\text{even}}_{\Lambda,A}$. The stronger version stated here will nevertheless be useful in the proof of [\[lem:BoudingTheSum_HT\]](#lem:BoudingTheSum_HT){reference-type="ref+label" reference="lem:BoudingTheSum_HT"} below and is proved in the same way, which explains our choice.
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
For $\beta<\beta^{\text{ht}}_{\text{ce}}(d)$, We have the following expansion: $$\begin{equation}
 \log(\Xi^A_{\Lambda;\beta,0})
= \sum_{X: \overline{X} \subset \Lambda} \Psi_{\beta}(X),
\label{eq:CE_HighTemperature}
\end{equation}$$ where for a cluster $X= \{(E_1,B_1),\dots,(E_r,B_r)\}$, $$\Psi_\beta(X):= \left( \prod_{(E,B) \in \mathcal{E}^\text{even}_{\Lambda,A}}
 \frac{1}{n_X(E,B)!} \right)  \, \phi((E_1,B_1),\dots,(E_r,B_r)) \, \left( \prod_{ i=1}^r \mathop{\mathrm{wt}}(E_i,B_i) \right),$$ where $$\phi(( E_1,B_1),\dots,(E_r,B_r)) =\sum_{G \subset G_r\, \text{connected}} \left( \prod_{\{i,j\} \in G}
\zeta\big[(E_i,B_i),(E_j,B_j)\big] \right),$$ and $G_r$ denotes the complete graph on $r$ vertices. The convergence of the series in [\[eq:CE_HighTemperature\]](#eq:CE_HighTemperature){reference-type="ref+label" reference="eq:CE_HighTemperature"} holds in the sense of locally uniform convergence of analytic functions in the complex parameters $t_1$, ..., $t_r$ for $|t_1|,\dots,|t_r| \le \tanh^{-1}(1)$. []{#prop:CE_HighTemperature label="prop:CE_HighTemperature"}
:::

::: proof
*Proof.* This follows from the general theory of cluster expansions, see e.g. [@Velenik Chapter 5]. For the analyticity in the parameters, see specifically [@Velenik Section 5.5]. ◻
:::

Notice that the functional $\phi((E_1,B_1),\dots,(E_r,B_r))$ depends only on which pairs $(E_i,E_j)$ intersect and vanishes if $X$ can be split into two mutually non-intersecting subsets.

### Bounds on joint cumulants {#SectBoundHT}

Recall that $A=\{x_1,\dots,x_r\}$ is a set of points in the finite domain $\Lambda$. The joint cumulant $\kappa_{\Lambda;\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r})$ is the coefficient of $t_1 \dots t_r$ in $$\begin{multline*}
 \log \left\langle \exp\left(\sum_{j=1}^r t_j \sigma_{x_j} \right) \right\rangle_{\Lambda,\beta,0}
=\log Z^A_{\Lambda; \beta,0}  - \log Z^\emptyset_{\Lambda; \beta,0} \\
= |\Lambda|\, \log 2 + |\mathcal{E}_\Lambda| \, \log(\cosh\, \beta)
+\sum_{j=1}^r  \log (\cos\, t_j) + \log \Xi^A_{\Lambda;\beta,0}
-  \log Z^\emptyset_{\Lambda; \beta,0}.
\end{multline*}$$ Only the summand $\log \Xi^A_{\Lambda;\beta,0}$ contributes to the coefficient of $t_1 \dots t_r$. Therefore, using [\[prop:CE_HighTemperature\]](#prop:CE_HighTemperature){reference-type="ref+label" reference="prop:CE_HighTemperature"}, we have $$\begin{equation}
\label{eq:cumulants_cluster}
\kappa_{\Lambda;\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) = [t_1 \dots t_r] \sum_{X: \overline{X} \subset \Lambda} \Psi_{\beta}(X)
=  \sum_{X: \overline{X} \subset \Lambda}  [t_1 \dots t_r]  \Psi_{\beta}(X).
\end{equation}$$ The exchange of infinite sum and coefficient extraction is valid since we have uniform convergence of analytic functions on a neighborhood of $0$. A cluster $X=\{(E_1,B_1),\dots,(E_r,B_r)\}$ contributes to the coefficient of $t_1 \dots t_r$ only if $A=B_1 \uplus \dots \uplus B_r \subseteq \overline{X}$. Then $$\begin{multline*}
 [t_1 \dots t_r]  \Psi_{\beta}(X) = 
\left( \prod_{(E,B) \in \mathcal{E}^\text{even}_{\Lambda,A}}
 \frac{1}{n_X(E,B)!} \right)  \, \varphi((E_1,B_1),\dots,(E_r,B_r)) \, (\tanh \beta)^{e(X)}\\
 \le C_r \, \bm{1}[X \text{ is connected}] \, (\tanh \beta)^{e(X)},
\end{multline*}$$ where $e(X)=|E_1|+\dots+|E_r|$ and $\bm{1}[\text{event}]$ is the indicator function of the corresponding event. Back to [\[eq:cumulants_cluster\]](#eq:cumulants_cluster){reference-type="ref+label" reference="eq:cumulants_cluster"}, we get $$|\kappa_{\Lambda;\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) | \le
  \sum_{X: \overline{X} \subset \Lambda, X\text{ connected,}\atop \text{and } A \subseteq \overline{X}}
  C_r (\tanh \beta)^{e(X)}.$$ Taking the limit $\Lambda \uparrow \mathbb{Z}^d$, we get a similar upper bound for the cumulant $\kappa_{\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r})$ under the probability measure $\mu_{\beta,0}$ corresponding to the whole lattice $\mathbb{Z}^d$: $$\begin{equation}
\label{eq:BoundCum1}
|\kappa_{\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) | \le
  \sum_{X\text{ connected}\atop \text{s.t. } A \subseteq \overline{X}}
  C_r (\tanh \beta)^{e(X)}.
\end{equation}$$ The key point in the above formula is that any connected cluster $X$ with $A \subseteq \overline{X}$ fulfills $e(X) \ge \ell_T(A)$. We now need the following lemma, whose proof is inspired by the end of the proof of Theorem 5.27 in [@Velenik].

::: lemma
[]{#lem:BoudingTheSum_HT label="lem:BoudingTheSum_HT"} There exist constants $\beta^{\text{ht}}_{\text{jc}}(d)>0$ and $\varepsilon>0$ such that, for $\beta \le \beta^{\text{ht}}_{\text{jc}}(d)$, we have the following inequality: $$\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}\text{and } e(X) \ge R} (\tanh \beta)^{e(X)}
 \le \varepsilon^R.$$
:::

::: proof
*Proof.* The proof involves different values of the inverse temperature $\beta$ so that we will here make explicit the dependency of the weight in $\beta$: we write $\overline{\mathop{\mathrm{wt}}}_\beta(E,B)$ instead of $\overline{\mathop{\mathrm{wt}}}(E,B)$. We first prove that for $\beta' \le \beta^{\text{ht}}_{\text{jc}}(d)$, we have $$\begin{equation}
\label{eq:SumPsiLeqOne}
\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}} (\tanh \beta')^{e(X)} =\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}}  \prod_{i=1}^r \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_i,B_i)  \le 1.
\end{equation}$$ This uses the same argument as in [@Velenik Eq. (5.31)]: $$\begin{multline*}
 \sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X}}  \prod_{i=1}^r \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_i,B_i)
 \le \sum_{r \ge 1} r \sum_{(E_1,B_1) \text{ connected} \atop \text{s.t. } x_1 \in V(E_1,B_1)} \ \sum_{(E_2,B_2),\dots,(E_r,B_r)}
 \prod_{i=1}^r \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_i,B_i) \\
 \le \sum_{(E_1,B_1) \text{ connected} \atop \text{s.t. } x_1 \in V(E_1,B_1)}  \overline{\mathop{\mathrm{wt}}}_{\beta'}(E_1,B_1) e^{|a(E_1,B_1)|}
 \le a(\emptyset, \{x_1\}) =1,
\end{multline*}$$ where we used [\[lem:Cv_CE_HighTemperature\]](#lem:Cv_CE_HighTemperature){reference-type="ref+label" reference="lem:Cv_CE_HighTemperature"} and [@Velenik Theorem 5.4]. This proves [\[eq:SumPsiLeqOne\]](#eq:SumPsiLeqOne){reference-type="eqref" reference="eq:SumPsiLeqOne"}.

Let us fix a value $\beta'$ as above. There exists a constant $\varepsilon<1$ such that for $\beta$ small enough, we have $\tanh \beta < \varepsilon\, \tanh \beta'$. We can now write $$\sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X} \text{and } e(X) \ge R} (\tanh \beta)^{e(X)} 
 \le  \varepsilon^R \sum_{X\text{ connected}\atop \text{s.t. } x_1 \in \overline{X} \text{and } e(X) \ge R} (\tanh \beta')^{e(X)} \le \varepsilon^R,$$ where the last inequality uses [\[eq:SumPsiLeqOne\]](#eq:SumPsiLeqOne){reference-type="eqref" reference="eq:SumPsiLeqOne"}. This ends the proof of the lemma. ◻
:::

Combining [\[eq:BoundCum1,lem:BoudingTheSum_HT\]](#eq:BoundCum1,lem:BoudingTheSum_HT){reference-type="ref+label" reference="eq:BoundCum1,lem:BoudingTheSum_HT"}, we get the desired bound: for $\beta \le \beta^{\text{ht}}_{\text{jc}}(d)$, $$|\kappa_{\beta,0}(\sigma_{x_1},\dots,\sigma_{x_r}) | \le C_r \varepsilon^{\ell_T(A)}.$$

## At very low temperature, without magnetic field

  []{#Sect:CE_LT label="Sect:CE_LT"}

### The cluster expansion of the partition function

We now turn to the regime without magnetic field ($h=0$) and very low temperature ($\beta$ large). Intuitively, in that case, the spin configurations with fewer pairs of neighbours having opposite spins appear with higher probability. To emphasize the role of these pairs, we rewrite the Hamiltonian as follows: $$H^{\eta}_{\Lambda;\beta, h} (\omega)= -\beta |E^{\eta}_{\Lambda}| -\beta \sum_{\{i,j\} \in \mathcal{E}^{\eta}_{\Lambda} } (\sigma_i(\omega) \sigma_j(\omega) - 1).$$ The only non-zero terms in the sum are those where two neighbours $i$ and $j$ have opposite spins. Let us consider a finite subset $\Lambda \subset \mathbb{Z}^d$ with $+$ boundary condition. A typical spin configuration will then look as a sea of $+$'s with some islands of $-$'s. Therefore the interesting macroscopic components for the cluster expansion in that case are the frontiers between the areas of $+$'s and those of $-$'s, which are called *contours*. Let us define them more rigorously.

Given $\omega \in \Omega_{\Lambda}^{+}$, let $\Lambda^{-}(\omega)$ denote the set of lattice points $i$ where $\sigma_i(\omega)=-1.$ For each $i \in \mathbb{Z}^d$ we define $\mathcal{S}_i := i + [\frac{-1}{2},\frac{1}{2}]^d$ to be the unit cube of $\mathbb{R}^d$ centred at $i$. Now let $$\mathcal{M}(\omega) := \bigcup_{i \in \Lambda^{-}(\omega)} \mathcal{S}_i,$$ and consider the set of maximal connected components of the boundary of $\mathcal{M}(\omega)$, which we denote $$\Gamma'(\omega)= \{ \gamma_1, \dots, \gamma_r \}.$$ Each of the $\gamma_i$'s is a *contour* of $\omega.$ Contours are connected sets of $(d-1)$-dimensional faces of the cubes $\mathcal{S}_i$. We denote by $| \gamma_i|$ the number of such faces in $\gamma_i$. Let $\Gamma_{\Lambda} := \{ \gamma \in \Gamma'(\omega) : \omega \in \Omega_{\Lambda}^{+} \}$ denote the set of all possible contours in $\Lambda.$ Finally, a collection of contours $\Gamma' \subset \Gamma_{\Lambda}$ is said to be *admissible* if there exists a spin configuration $\omega \in \Omega_{\Lambda}^{+}$ such that $\Gamma'(\omega) =\Gamma'.$

Thus when $\Lambda$ is simply connected (which we will assume from now on in this paper), the partition function can be rewritten as $$Z^+_{\Lambda; \beta,0} = e^{\beta |\mathcal{E}_{\Lambda}^+|} \Xi^+_{\Lambda;\beta,0} ,$$ where $$\Xi^+_{\Lambda;\beta,0} := \sum_{\Gamma' \subset \Gamma_{\Lambda} admissible} \prod_{\gamma \in \Gamma'} e^{-2 \beta |\gamma|}.$$

The cluster expansion is an expression for $\log \Xi^+_{\Lambda;\beta,0}$ as an absolutely convergent series. In this case, a cluster is a collection $X= \{\gamma_1, \dots, \gamma_r\}$ of contours such that for every two contours $\gamma_i$ and $\gamma_j$, there is a "path" of faces of contours of $X$ connecting $\gamma_i$ and $\gamma_j$. Note that $X$ is actually a multiset, and denote by $n_X(\gamma)$ the number of copies of $\gamma$ appearing in $X$ and by $\overline{X}$ the support of $X$, ie $\overline{X}= \cup_{\gamma \in X} \gamma.$ In the following we write $\overline{X} \subseteq \Lambda$ to say that $\overline{X} \subseteq \cup_{i \in \Lambda} \mathcal{S}_i$ as subsets of $\mathbb{R}^d$.

In can be shown (see e.g. [@Velenik Chapter 5]) that the cluster expansion converges for $\beta$ large enough.

::: proposition
[]{#prop:cluesterexp label="prop:cluesterexp"} There exists $\beta_{\text{ce}}^{\text{lt}}(d)$ such that for all $\beta > \beta_{\text{ce}}^{\text{lt}}(d)$, $$\log \Xi^+_{\Lambda;\beta,0} = \sum_{X: \overline{X} \subseteq \Lambda} \Psi_{\beta}(X),$$ where for a cluster $X= \{\gamma_1, \dots, \gamma_r\}$, $$\Psi_\beta(X):= \left( \prod_{\gamma \in \Gamma_{\Lambda}} \frac{1}{n_X(\gamma)!} \right) \phi(\gamma_1,\dots,\gamma_r)  e^{-2 \beta \sum_{i=1}^r |\gamma_i|},$$ where $$\phi(\gamma_1,\dots,\gamma_r)=\sum_{G \subseteq G_r connected} \prod_{\{i,j\} \in G} \zeta(\gamma_i,\gamma_j),$$ $$\zeta(\gamma_i,\gamma_j) := \begin{cases}
0 \text{ if } \gamma_i \cap \gamma_j = \emptyset,\\
-1 \text{ otherwise,}
\end{cases}$$ and $G_r$ denotes the complete graph on $r$ vertices.
:::

### Bounds on joint cumulants {#SectBoundLT}

This cluster expansion can be used to compute expectations and therefore deduce some bounds on joint cumulants.

Let $A \subseteq \Lambda$ and let us define $\sigma_A := \prod_{i \in A} \sigma_i$. Its expectation is given by $$\langle \sigma_A \rangle^+_{\Lambda;\beta,0}= \sum_{\omega \in \Omega^+_{\Lambda}} \sigma_A(\omega) \frac{e^{-H_{\Lambda;\beta,0}(\omega)}}{Z^+_{\Lambda; \beta,0}}.$$ For any spin configuration $\omega \in \Omega^+_{\Lambda}$ and any contour $\gamma \in \Gamma'(\omega)$, let us define the *interior* of $\gamma$ (written $\mathop{\mathrm{Int}}(\gamma)$) as the set of points of $\Lambda$ which would have spin $-1$ if $\gamma$ was the only contour of $\omega$. We also write $\mathop{\mathrm{Int}}(X):=  \bigcup_{\gamma \in X} \mathop{\mathrm{Int}}(\gamma).$ Thus for any $\omega \in \Omega^+_{\Lambda}$ and any $i \in \Lambda$, $$\sigma_i(\omega) = (-1)^{| \{\gamma \in \Gamma'(\omega) : i \in \mathop{\mathrm{Int}}(\gamma)\}|},$$ and thus $$\begin{align*}
\sigma_A(\omega) &= (-1)^{\sum_{i \in A} | \{\gamma \in \Gamma'(\omega) : i \in \mathop{\mathrm{Int}}(\gamma)\}|}
\\&= (-1)^{\sum_{\gamma \in \Gamma'(\omega)} | \{i \in A : i \in \mathop{\mathrm{Int}}(\gamma)\}|}.
\end{align*}$$ Therefore one can write $$\langle \sigma_A\rangle^+_{\Lambda;\beta,0}= \frac{\Xi^{+,A}_{\Lambda;\beta,0}}{\Xi^+_{\Lambda;\beta,0}},$$ where $$\Xi^{+,A}_{\Lambda;\beta,0} := \sum_{\Gamma' \subseteq \Gamma_{\Lambda} admissible} \prod_{\gamma \in \Gamma'} (-1)^{| \{i \in A : i \in \mathop{\mathrm{Int}}(\gamma)\}|} e^{-2 \beta |\gamma|}.$$ The cluster expansion converges, which means that we have an analogue of Proposition [\[prop:cluesterexp\]](#prop:cluesterexp){reference-type="ref" reference="prop:cluesterexp"} for $\Xi^{+,A}_{\Lambda;\beta,0}$, and thus $\langle \sigma_A \rangle^+_{\Lambda;\beta,0}$ can be expressed as $$\langle \sigma_A\rangle^+_{\Lambda;\beta,0} = \exp \left( \sum_{X: \overline{X} \subseteq \Lambda} \Psi^A_{\beta}(X) -  \sum_{X: \overline{X} \subseteq \Lambda} \Psi_{\beta}(X) \right),$$ where for a cluster $X= \{\gamma_1, \dots, \gamma_r\}$,

$$\begin{align*}
\Psi^A_\beta(X):=& \left( \prod_{\gamma \in \Gamma_{\Lambda}} \frac{1}{n_X(\gamma)!} \right) \left( \sum_{G \subseteq G_r connected} \zeta(\gamma_i,\gamma_j) \right)
\\& \times (-1)^{ \sum_{j=1}^r | \{i \in A : i \in \mathop{\mathrm{Int}}(\gamma_j)\}|} e^{-2 \beta \sum_{j=1}^r |\gamma_j|}.
\end{align*}$$

For all clusters $X$ such that no vertex of $A$ is in the interior of any of its contours, the exponent of $(-1)$ in the definition of $\Psi^A_\beta(X)$ is always $0$ and thus $\Psi^A_\beta(X)=\Psi_\beta(X).$ Therefore we obtain $$\langle \sigma_A\rangle^+_{\Lambda;\beta,0} = \exp \left( \sum_{X \sim A : \overline{X} \subseteq \Lambda} (\Psi^A_{\beta}(X) -  \Psi_{\beta}(X)) \right),$$ where $X \sim A$ means that $X$ contains at least one contour $\gamma$ such that a point of $A$ is in the interior of $\gamma$. The series is absolutely convergent and we can let $\Lambda \uparrow \mathbb{Z}^d$, obtaining the following proposition.

::: proposition
[]{#prop:expectation label="prop:expectation"} For $\beta$ large enough, $$\langle \sigma_A\rangle^+_{\beta,0} = \exp \left( \sum_{X \sim A } (\Psi^A_{\beta}(X) -  \Psi_{\beta}(X)) \right).$$
:::

We now want to find estimates on the joint cumulants of the variables $\{\sigma_i : i \in A\}$, for all $A \subset \mathbb{Z}^d$ finite. But in this case, it is easier to estimate first another quantity related to cumulants. We define, for some set $B$ and random variables $(Y_i)_{i \in B}$ defined on the same probability space, $$Q \left(Y_j; j \in B \right) := \prod_{ \delta \subseteq B \atop \delta \neq \emptyset}  \ \left\langle \prod_{j \in \delta} Yj \right\rangle^{(-1)^{|\delta|}} .$$

For example, $$Q_{\beta,0}(\sigma_1, \sigma_2) = \frac{\langle \sigma_1 \sigma_2 \rangle_{\beta,0}^+ }{\langle\sigma_1\rangle_{\beta,0}^+ \langle\sigma_2\rangle_{\beta,0}^+}.$$

We show a bound on the quantities $Q_{\beta,0} \left(\sigma_j; j \in A \right)$ for all finite $A \subset \mathbb{Z}^d.$

::: lemma
[]{#lem:quotient label="lem:quotient"} Let $A$ be a finite subset of $\mathbb{Z}^d$ of size $r$. Then for $\beta$ large enough, $$\left| Q_{\beta,0} \left(\sigma_j; j \in A \right)  - 1 \right| \leq C_r e^{-c \beta \ell_T(A)},$$ where $c=c(d)$ and $C_r$ are positive constants depending respectively on $d$ and $r$.
:::

::: proof
*Proof.* Using Proposition [\[prop:expectation\]](#prop:expectation){reference-type="ref" reference="prop:expectation"}, we have $$\log Q \left(\sigma_j; j \in A \right)  = \sum_{\delta \subseteq A, \delta \neq \emptyset} (-1)^{|\delta|} \sum_{X \sim \delta} (\Psi^{\delta}_{\beta}(X) -  \Psi_{\beta}(X)).$$ Recall that $X \sim \delta$ means that at least one point of $\delta$ is in the interior of a contour in $X$. We split the second sum depending on the exact subset $I \subseteq \delta$ of points that are in the interior of a contour in $X$. By definition of $\Psi$ observe, if $I$ is as above, $\Psi^{\delta}_{\beta}(X)= \Psi^{I}_{\beta}(X)$. Therefore $$\begin{align*}
\log Q \left(\sigma_j; j \in A \right) &=  \sum_{\delta \subseteq A, \delta \neq \emptyset} (-1)^{|\delta|} \sum_{ I \subseteq \delta : \atop I \neq \emptyset} \sum_{X : \atop \mathop{\mathrm{Int}}(X) \cap \delta =I } (\Psi^{I}_{\beta}(X) -  \Psi_{\beta}(X))
\\ &= \sum_{ I \subseteq A : \atop I \neq \emptyset} \sum_{X : \atop I \subseteq \mathop{\mathrm{Int}}(X)} (\Psi^{I}_{\beta}(X) -  \Psi_{\beta}(X)) \sum_{\delta : \atop I \subseteq \delta \subseteq (I \cup  (A \setminus \mathop{\mathrm{Int}}(X)))} (-1)^{|\delta|}.
\end{align*}$$ But the last sum is equal to $0$ unless $A$ is contained in $\mathop{\mathrm{Int}}(X)$. Therefore we obtain $$\begin{align*}
\log Q  \left(\sigma_j; j \in A \right)  &= \sum_{X : \atop A \subseteq \mathop{\mathrm{Int}}(X)} \sum_{ I \subseteq A : \atop I \neq \emptyset} (-1)^{|I|}(\Psi^{I}_{\beta}(X) -  \Psi_{\beta}(X)).
\end{align*}$$ Finally, there are $2^r-1$ non-empty subsets of $A$, and $|\Psi^{I}_{\beta}(X)| \leq |\Psi_{\beta}(X)|$ for all $X$ and $I$, thus $$\begin{equation}
\label{eq:boundlogQ}
\left| \log Q \left(\sigma_j; j \in A \right) \right| \leq \sum_{X : \atop A \subseteq \mathop{\mathrm{Int}}(X)} 2(2^r-1) |\Psi_{\beta}(X)|.
\end{equation}$$ We conclude by using a trick similar to Lemma [\[lem:BoudingTheSum_HT\]](#lem:BoudingTheSum_HT){reference-type="ref" reference="lem:BoudingTheSum_HT"}. By [@Velenik Equation (5.31)], if $\beta \geq \beta_{\text{ce}}^{\text{lt}}(d)$, for any vertex $v \in \mathbb{Z}^d$, we have the bound $$\sum_{X: \overline{X} \ni v} \left| \Psi_{\beta} (X)\right| \leq 1.$$ Thus if $\beta \geq 2 \beta_{\text{ce}}^{\text{lt}}(d)$, $$\sum_{X: \overline{X} \ni v} \left| \Psi_{\beta}(X) e^{\beta |\overline{X}|}\right| \leq \sum_{X: \overline{X} \ni v} \left| \Psi_{\frac{\beta}{2}} (X)\right| \leq 1.$$ So for any positive integer $R$, $$\begin{equation}
\label{eq:boundbetaLT}
\sum_{X: \overline{X} \ni v \atop |\overline{X}| \geq R} \left| \Psi_{\beta}(X)\right| \leq  e^{-\beta R} \sum_{X: \overline{X} \ni v} \left| \Psi_{\beta}(X) e^{\beta |\overline{X}|}\right| \leq e^{-\beta R}.
\end{equation}$$ Let us now turn back to Eq. [\[eq:boundlogQ\]](#eq:boundlogQ){reference-type="eqref" reference="eq:boundlogQ"}. Every cluster $X$ such that $A \subseteq \mathop{\mathrm{Int}}(X)$ satisfies $|\overline{X}| \geq 2 \ell_T(A).$ Moreover, if a cluster of size $R$ has $j_1 \in A$ in its interior, then it contains at least a point $v$ which is at distance at most $R$ of $j_1$. There are at most $C R^d$ such points, therefore $$\begin{align*}
\sum_{X : \atop A \subseteq \mathop{\mathrm{Int}}(X)} |\Psi_{\beta}(X)| &\leq \sum_{R \geq 2\ell_T(A)} C R^d  \left[\sum_{X: \overline{X} \ni v \atop |\overline{X}| = R} \left| \Psi_{\beta}(X)\right| \right] \\
&\leq C \sum_{R \geq 2\ell_T(A)} R^d e^{-\beta R} \\
&\leq C' e^{-c \beta \ell_T(A)},
\end{align*}$$ for $\beta$ large enough, where $C'$ and $c$ are some positive constants (and $c$ depends on the dimension $d$ of the ambiant space). Thus by [\[eq:boundlogQ\]](#eq:boundlogQ){reference-type="eqref" reference="eq:boundlogQ"}, $$\left| \log Q \left(\sigma_j; j \in A \right) \right| \leq C'_r e^{-c \beta \ell_T(A)},$$ for some positive constant $C'_r$ depending on $r$. Exponentiating completes the proof. ◻
:::

Now we can convert this estimate into the desired bound on joint cumulants.

::: proposition
[]{#prop:boundcum label="prop:boundcum"} Let $A$ be a finite subset of $\mathbb{Z}^d$ of size $r$. Then, for $\beta$ large enough, $$|\kappa_{\beta,0} \left(\sigma_j; j \in A \right)| 
\leq D_r e^{\frac{-c \beta \ell_T(A)}{2}},$$ where $c=c(d)$ is given by [\[lem:quotient\]](#lem:quotient){reference-type="ref+label" reference="lem:quotient"} and $D_r$ is a positive constant depending on $r$.
:::

::: proof
*Proof.* By Lemma [\[lem:quotient\]](#lem:quotient){reference-type="ref" reference="lem:quotient"}, $$Q_{\beta,0} \left(\sigma_j; j \in A \right) = 1+ \mathcal{O}(\mathcal{M} \big( G[A] \big)),$$ where $G$ is the weighted graph defined on $\mathbb{Z}^d$ such that for each $e=(i,j)$, $w_e = e^{\frac{-c \beta \|i - j\|_1}{2}}$. Indeed in that case $\mathcal{M} \big( G[A] \big) = e^{\frac{-c \beta \ell_T'(A)}{2}} \geq e^{-c \beta \ell_T(A)}$; see the discussion in [\[Subsect:Spanning\]](#Subsect:Spanning){reference-type="ref+label" reference="Subsect:Spanning"}.

Then using Proposition 5.8 of [@Valentin], we deduce that $$|\kappa_{\beta,0} \left(\sigma_j; j \in A \right)| = \prod_{j \in A} \langle\sigma_j\rangle_{\beta,0}^+ \times \mathcal{O}(\mathcal{M} \big( G[A] \big)).$$ But for all $j \in A$, we have $\langle \sigma_j \rangle_{\beta,0}^+ \leq 1,$ and for $\beta$ large enough, $\langle \sigma_j \rangle_{\beta,0}^+ > 0.$ Hence $$0 < \prod_{j \in A} \langle \sigma_j \rangle_{\beta,0}^+ \leq 1.$$ Moreover by Proposition [\[prop:2longueurs\]](#prop:2longueurs){reference-type="ref" reference="prop:2longueurs"}, $$\mathcal{M} \big( G[A] \big) = e^{\frac{-c_d \beta \ell_T'(A)}{2}} \leq e^{\frac{-c_d \beta \ell_T(A)}{2}}.$$ Thus $|\kappa_{\beta,0} \left( \sigma_j; j \in A \right)| \leq D_r  e^{\frac{-c_d \beta \ell_T(A)}{2}}$, as claimed. ◻
:::

## With a strong magnetic field {#SectBoundMF}

The last regime we consider is the Ising model with a strong magnetic field, *i.e.* $h$ is bigger than some value $h_1>0$ ($h_1$ is to be determined later). The case of negative $h$ (smaller than $-h_1<0$) is obviously symmetric.

In this regime, there is also a well-known cluster expansion for the partition function [@Velenik Section 5.7]. Let us present it briefly.

Fix $\Lambda \subset \mathbb{Z}^d$ and consider the Ising model on $\Lambda$ with $+$ boundary conditions. We first write its partition function in a suitable form. For a subset $\Lambda^-$ of $\Lambda$, we denote $$\delta_e \Lambda^- = \{ \{i,j\} \in \mathcal{E}_\Lambda^b,\ i \in \Lambda^-,\, j \notin \Lambda^-\}.$$ Define also $\mathop{\mathrm{wt}}(\Lambda^-) = \exp(-2 \beta\, |\delta_e \Lambda^-| -2h|\Lambda^-|)$. Then we have:

::: lemma
With the above notation, $$Z^+_{\Lambda,\beta,h} = \exp \big( \beta|\mathcal{E}_\Lambda^b| +h |\Lambda| \big) 
  \left( \sum_{\Lambda^- \subseteq \Lambda} \mathop{\mathrm{wt}}(\Lambda^-) \right).$$ []{#lem:Z_MF label="lem:Z_MF"}
:::

::: proof
*Proof.* The proof is not difficult and can be found, *e.g.*, in [@Velenik Section 5.7]. It is important to note that the sum over $\Lambda^- \subseteq \Lambda$ corresponds to the sum over spin configurations in the definition of the partition function: the correspondence simply associates with a spin configuration the set $\Lambda^-$ of positions of its minus spins. ◻
:::

Let $A$ be a subset of $\Lambda$. It is straightforward to modify the argument to find a similar expression for the numerators of $\langle \sigma_A \rangle$ (as in [\[Sect:CE_LT\]](#Sect:CE_LT){reference-type="ref+label" reference="Sect:CE_LT"}) or of $\left\langle \exp\left(\sum_{i \in A} t_i \sigma_i \right) \right\rangle$ (as in [0.1](#Sect:CE_HT){reference-type="ref+label" reference="Sect:CE_HT"}). $$\begin{align}
  \sum_{\omega \in \Omega_\Lambda} \sigma_A(\omega) e^{-H^+_{\Lambda;\beta,h}(\omega)} &= \exp \big( \beta|\mathcal{E}_\Lambda^b| +h |\Lambda| \big)              
  \left( \sum_{\Lambda^- \subseteq \Lambda} (-1)^{|A \cap \Lambda^-|} \mathop{\mathrm{wt}}(\Lambda^-) \right).\label{eq:SA_MF}\\
    \sum_{\omega \in \Omega_\Lambda} \exp\left(\sum_{i \in A} t_i \sigma_i \right) &= 
e   \exp \left( \beta|\mathcal{E}_\Lambda^b| +h |\Lambda| + \sum_{i \in A} t_i \right)
    \, \left( \sum_{\Lambda^- \subseteq \Lambda} \left[\prod_{i \in A \cap \Lambda^-} \exp(-2t_i)\right] \mathop{\mathrm{wt}}(\Lambda^-) \right).
    \label{eq:MGF_MF}
\end{align}$$ A set $\Lambda^- \subseteq \Lambda$ can be seen as a subgraph of the lattice $\mathbb{Z}^d$. As such, it admits a unique decomposition as disjoint union of its connected components $\Lambda^-=S_1 \sqcup S_2 \sqcup \dots \sqcup S_r$. The weight $\mathop{\mathrm{wt}}$ behaves multiplicatively with respect to this decomposition $\mathop{\mathrm{wt}}(\Lambda^-)=\prod_{i=1}^r \mathop{\mathrm{wt}}(S_i)$; the same is true for the modified weights $(-1)^{|A \cap \Lambda^-|} \mathop{\mathrm{wt}}(\Lambda^-)$ and $\left[\prod_{i \in A \cap \Lambda^-} \exp(-2t_i)\right] \mathop{\mathrm{wt}}(\Lambda^-)$ which appear in [\[eq:SA_MF,eq:MGF_MF\]](#eq:SA_MF,eq:MGF_MF){reference-type="ref+label" reference="eq:SA_MF,eq:MGF_MF"} above. This enables us to use the technique of cluster expansion.

The convergence of this cluster expansion is proved for the partition function in [@Velenik Section 5.7]. The argument can be directly adapted to get a cluster expansion of the expression in [\[eq:SA_MF,eq:MGF_MF\]](#eq:SA_MF,eq:MGF_MF){reference-type="ref+label" reference="eq:SA_MF,eq:MGF_MF"} above. The same reasoning as in [0.1](#Sect:CE_HT){reference-type="ref+label" reference="Sect:CE_HT"} or in [\[Sect:CE_LT\]](#Sect:CE_LT){reference-type="ref+label" reference="Sect:CE_LT"} leads to similar bounds on joint cumulants, which proves [\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref+label" reference="thm:bound_joint_cumulants"} in the strong magnetic field regime.
