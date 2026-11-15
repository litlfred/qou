---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-003-13-central-limit-theorems
section_title: "Central limit theorems"
section_number: 1.3
pages: 3-5
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.932
latex_coverage_ratio: 0.716
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
Central limit theorems (CLTs) play a key role in probability theory and have also been a subject of interest in the study of the Ising model. We refer to the second edition of Georgii's classical book [@Georgii2011 Bibliographic Notes on Section 8.2, p469] for an overview of the different methods used to get such results.

The theory of weighted dependency graphs gives access to CLTs for the number of occurrences of *patterns of spins* in a growing box $\Lambda_{n} := [-n,n]^d$. To illustrate this, we consider two kinds of patterns: *local* and *global* patterns.

We define a *local pattern* $\mathcal{P}$ to be a pair $(\mathcal{D}, \mathfrak{s})$, where $\mathcal{D}$ is a finite subset of $\mathbb{Z}^d$ containing $0$ and $\mathfrak{s}$ is a function $\mathcal{D} \longrightarrow \{+,-\}.$ The cardinality of $\mathcal{D}$ is called the *size* of the pattern $\mathcal{P}.$ An example of local pattern is a positive spin surrounded by negative ones. In that case the subset is $\mathcal{D} = \{j \in \mathbb{Z}^d: \|j\|_1 \le 1\}$, while the sign function is given by $\mathfrak{s}(0)=+$ and $\mathfrak{s}(j) = -$ for all $j \in \mathcal{D} \setminus \{0\}$. This pattern has size $2d+1$. An *occurrence* of a local pattern $\mathcal{P}=(\mathcal{D}, \mathfrak{s})$ is a set $\{(i+j,\mathfrak{s}(j)) : j \in \mathcal{D}\}$, where $i \in \mathbb{Z}^d$ is the *position* of the occurrence.

While in local patterns we consider spins that are at a fixed distance from one another, in global patterns they can be as far as we want, as long as they have a certain global shape. Formally, we define a *global pattern* $\tilde{\mathcal{P}}$ of size $m$ to be a pair $(\mathcal{O}, \mathfrak{s})$, where $\mathcal{O}=(\leq_1, \dots , \leq_d)$ is a $d$-tuple of total orders over $\{1, \dots , m\}$, and $\mathfrak{s}$ is a function $\{1, \dots , m\} \longrightarrow \{+,-\}.$ An *occurrence* of $\tilde{\mathcal{P}}$ in a spin configuration $\omega$ is a set $\{x^{(1)}, \dots ,x^{(m)}\}$ of $m$ elements of $\mathbb{Z}^d$ such that there exists some ordering $(x^{(1)}, \dots , x^{(m)})$ of these elements such that

1.  for all $i \in \{1, \dots , m\}$, $\sigma_{x^{(i)}}(\omega) = \mathfrak{s}(i),$

2.  for all $i,j \in \{1, \dots , m\}$, for all $k \in \{1, \dots d \}$, $x^{(i)}_k \leq x^{(j)}_k$ if and only if $i \leq_k j.$

For example, if $d=2$, $\leq_1, \leq_2$ are both the natural ordering and $\mathfrak{s}(i) =+$ for all $i$, then the global pattern $(\mathcal{O}, \mathfrak{s})$ is a North-East chain of $m$ positive spins.

CLTs for local and global patterns in other structures than the Ising model have attracted attention in the literature. We mention Markov chains (see [@Regnier_Spankowski:CLTPattern; @FlajoletValleePatterns; @Valentin] and references therein), patterns in random permutations (see [@BonaMonotonePatterns; @JansonNakamuraZeilberger] for global patterns and [@GoldsteinConsecutifs; @BonaMonotonePatterns; @ElizaldeEtAlConsecutifs] for local patterns) and arc configurations in random set-partitions (CLTs for the number of arcs of size $1$, which is a local pattern, and the number of crossings, which is a global pattern, were given in [@CLT_SetPartitionsStatistics]). Note that Markov chains are (discrete) one-dimensional Markov random fields, while the random permutation model is a non-Markovian two-dimensional model (when considering patterns, we think of permutations as permutation matrices). Finding such CLT results in Markov random fields of dimension two or more, and in particular in the Ising model, is therefore a natural problem.

We first prove a CLT for local patterns. Let $S_{n,\mathcal{P}}$ denote the number of occurrences of a given local pattern $\mathcal{P}$ in $\Lambda_n$.

::: theorem
[]{#th:cltpower label="th:cltpower"} Consider the Ising model on $\mathbb{Z}^d$, with inverse temperature $\beta$ and magnetic field $h$, such that either $h > h_1(d)$ or $(h=0;\, \beta < \beta_1(d))$ or $(h=0;\, \beta > \beta_2(d))$. Let $\mathcal{P}$ be a local pattern. Then $$\frac{S_{n,\mathcal{P}} - \mathbb{E}(S_{n,\mathcal{P}}) }{\sqrt{|\Lambda_n|}} \xrightarrow[n\to\infty]{d} \mathcal{N}(0, v_{\mathcal{P}}^2).$$
:::

Similarly, if $S_{n,\mathcal{\tilde{P}}}$ denotes the number of occurrences of a global pattern $\mathcal{\tilde{P}}$ in $\Lambda_n$, we have the following result.

::: theorem
[]{#thm:GlobalPatterns label="thm:GlobalPatterns"} Consider the Ising model on $\mathbb{Z}^d$, with inverse temperature $\beta$ and magnetic field $h$, such that either $h > h_1(d)$ or $(h=0;\, \beta < \beta_1(d))$ or $(h=0;\, \beta > \beta_2(d))$. Let $\mathcal{\tilde{P}}$ be a global pattern of size $m$. We assume that, for some positive constants $A$ and $\eta$ $$\mathop{\mathrm{Var}}(S_{n,\mathcal{\tilde{P}}}) \ge A n^{2m-2+\eta}.
  \label{eq:Hypo_Variance}$$ Then $$\frac{S_{n,\mathcal{\tilde{P}}} - \mathbb{E}(S_{n,\mathcal{\tilde{P}}}) }{\sqrt{\mathop{\mathrm{Var}}(S_{n,\mathcal{\tilde{P}}})}} \xrightarrow[n\to\infty]{d} \mathcal{N}(0, 1).$$
:::

We do not have in general an estimate for the variance $\mathop{\mathrm{Var}}(S_{n,\mathcal{\tilde{P}}})$. However, when the pattern consists in positive spins only, we can prove that [\[eq:Hypo_Variance\]](#eq:Hypo_Variance){reference-type="eqref" reference="eq:Hypo_Variance"} is satisfied (with $\eta=1$) --- see [\[prop:Variance_Lower_Bound\]](#prop:Variance_Lower_Bound){reference-type="ref" reference="prop:Variance_Lower_Bound"} below. The reverse inequality $\mathop{\mathrm{Var}}(S_{n,\mathcal{\tilde{P}}}) \le B n^{2m-1}$ is always fulfilled (see the proof of [\[thm:GlobalPatterns\]](#thm:GlobalPatterns){reference-type="ref" reference="thm:GlobalPatterns"}).

We finish this introduction with a comparison with other methods. Standard methods to get CLT in random fields are the use of mixing techniques [@neaderhouser1978] or FKG inequalities [@Newman80; @Newman83]. It seems that the CLT for local patterns can be easily obtained with these methods. Indeed, in an exponentially mixing field such as the Ising model, if we denote $Z^{\mathcal P}_i$ the characteristic function of the occurrence of $\mathcal P$ in position $i$ (see [\[eq:ZiP\]](#eq:ZiP){reference-type="eqref" reference="eq:ZiP"}), then the field $(Z^{\mathcal P}_i)_{i \in \mathbb{Z}^d}$ is also exponentially mixing and we can use the criterion given by Neaderhouser [@neaderhouser1978 Section 3]. CLT for functions of neighbouring spins are also accessible with methods based on FKG inequalities, see [@Newman83] for a general result in this direction. On the contrary, for global patterns, we do not know how to adapt these methods to prove [\[thm:GlobalPatterns\]](#thm:GlobalPatterns){reference-type="ref" reference="thm:GlobalPatterns"}. Indeed, if we denote $Z^{\mathcal{\tilde{P}}}_{\{x_1,\dots,x_m\}}$ the characteristic function of the occurrence of $\mathcal{\tilde{P}}$ in position $\{x_1,\dots,x_m\}$ (see [\[eq:ZXGP\]](#eq:ZXGP){reference-type="eqref" reference="eq:ZXGP"}), then $(Z^{\mathcal{\tilde{P}}}_{\{x_1,\dots,x_m\}})$ is not a mixing field anymore.

The theory of weighted dependency graphs enables to deal with these different kinds of patterns in a uniform way. In principle it would also be feasible to mix local and global conditions (as in vincular patterns for permutations [@Lisa]); besides the complexity of notation, a major difficulty is then to get general estimates for the variance.
