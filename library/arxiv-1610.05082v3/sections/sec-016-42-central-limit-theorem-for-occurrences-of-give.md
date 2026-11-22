---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-016-42-central-limit-theorem-for-occurrences-of-give
section_title: "Central limit theorem for occurrences of given patterns"
section_number: 4.2
pages: 19-23
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.961
latex_coverage_ratio: 0.976
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
[]{#sec:wdgconfig label="sec:wdgconfig"}

### Power of weighted dependency graphs

A major advantage of the theory of weighted dependency graphs is that this structure is stable by taking *powers*.

::: definition
Let $G$ be an edge-weighted graph with vertex set $A$ and weight function $w$; we also consider a positive integer $m$. We denote by $\mathrm{MSet}_{\leq m}(A)$ the subset of multisets of elements of $A$ with cardinality at most $m$. Then the $m$-th power $G^m$ of $G$ is by definition the graph with vertex-set $\mathrm{MSet}_{\leq m}(A)$ and where the weight between $I$ and $J$ is given by $w_m(I,J)=\max_{i \in I,j \in J} w(i,j)$. (Edges not in the graph should be seen as edges of weight $0$.)
:::

This definition is justified by the following property, proved in [@Valentin Section 5.3].

::: proposition
[]{#Prop:powers label="Prop:powers"} Let $\{Y_a, a \in A\}$ be a family of random variables with a weighted dependency graph $G$. Then $G^m$ is a weighted dependency graph for the family $\{Y_I, I \in \mathrm{MSet_{\leq m}(A)}\}$, where $Y_I = \prod_{a \in I} Y_a$.
:::

Instead of applying this to the variables $\sigma_i$, we will rather work with the variables $X_{(i,+)}:=X_i=\tfrac{1+\sigma_i}{2}$ and $X_{(i,-)}=1-X_i$. Start with the following observation. We have, for all $A = \{i_1, \dots, i_r\} \subseteq \mathbb{Z}^d$, $$\left| \kappa_{\beta,h} (X_{i_1}, \dots, X_{i_r}) \right| = \left| \kappa_{\beta,h} (Y_{i_1}, \dots, Y_{i_r}) \right|,$$ where on some subset $B$ of $A$, $Y_i = X_{(i,+)}$, and on $A \setminus B$, $Y_i = X_{(i,-)}.$

Mimicking the proof of Theorem [\[th:depgraph\]](#th:depgraph){reference-type="ref" reference="th:depgraph"}, we obtain the following. Let $G_s$ be the complete weighted graph with vertex set $\mathbb{Z}^d \times \{+,-\}$, such that for all $i,j \in \mathbb{Z}^d$, $$w'((i,+),(j,+))=w'((i,+),(j,-))= \varepsilon^{\frac12 \|i - j\|_1}.$$ In other words, we ignore the sign and use the weight function $w$ from the previous section. Then $G_s$ is a $\mathbf{C}$-weighted dependency graph for the family $\{X_{(i,s)}; i \in \mathbb{Z}^d, s \in \{+,-\} \}$, for some sequence $\mathbf{C} = (C_r)_{r \geq 1}$.

By considering the powers of $G_s$ and using [\[Prop:powers\]](#Prop:powers){reference-type="ref" reference="Prop:powers"}, we obtain weighted dependency graphs for the products of $X_{(i,+)}$'s and $X_{(i,-)}$'s with a bounded number of terms.

::: theorem
Consider the Ising model on $\mathbb{Z}^d$, with inverse temperature $\beta$ and magnetic field $h$, either for $h > h_1$ or ($h=0$ and $\beta < \beta_1$) or ($h=0$ and $\beta > \beta_2$). Let $m$ be a fixed positive integer; for multisets $I$ of elements of $\mathbb{Z}^d \times \{+,-\}$, we define $Z_I := \prod_{i \in I} X_i$. Then $G_s^m$ is a $\mathbf{D}_m$-weighted dependency graph for the family of random variables $\{Z_I;I \in \mathrm{MSet_{\leq m}\left(\mathbb{Z}^d \times \{+,-\}\right)}\}$, for some sequence $\mathbf{D}_m$ depending only on $m$. []{#th:powers label="th:powers"}
:::

### Local patterns

In this section, we prove Theorem [\[th:cltpower\]](#th:cltpower){reference-type="ref" reference="th:cltpower"}, the CLT for the number of occurrences of a given local pattern of spins (for example isolated $+$ spins).

To find a weighted dependency graph for the potential occurrences of a pattern $\mathcal{P}$ of size $m$, we consider $G_{\mathcal{P}}$ the restriction of $G_s^m$ to the $Z_I$'s of the form $$Z_i^{\mathcal{P}}= \prod_{j \in \mathcal{D}} X_{(i+j,\mathfrak{s}(j))}.
  \label{eq:ZiP}$$ Note that vertices of $G_{\mathcal{P}}$ are canonically indexed by $i \in \mathbb{Z}^d$ so that we will think of $G_{\mathcal{P}}$ as a graph with vertex set $\mathbb{Z}^d$. The weight of the edge between $i_1$ and $i_2$ is then $$w_{\mathcal{P}}(i_1,i_2)=\max_{j_1 \in \mathcal{D},j_2 \in \mathcal{D}} w(i_1+j_1,i_2+j_2) \le 
\varepsilon^{\frac{1}{2} \left(\|i_1 - i_2\|_1 - \max_{\alpha,\beta \in \mathcal{D}} \|\alpha - \beta\|_1\right)}.$$ The graph $G_{\mathcal{P}}$ is a $\mathbf{D}$-weighted dependency graph for $\{Z_i, i \in \mathbb{Z}^d\}$, for some sequence $\mathbf{D}$ depending only on $\mathcal{P}$. Indeed, it is a restriction of the weighted dependency graph given in [\[th:powers\]](#th:powers){reference-type="ref" reference="th:powers"}.

We define $$S_{n,\mathcal{P}} := \sum_{i \in \Lambda_n} Z_i^{\mathcal{P}},$$ the number of occurrences of $\mathcal{P}$ whose position is in $\Lambda_n$. In the example of isolated $+$ spins, we have $$S_{n,\mathcal{P}} := \sum_{i \in \Lambda_{n} } \left(X_{i} \prod_{j : \|i - j\|_1=1} (1-X_j) \right).$$ It is also easy to encode in this framework the number of $+$ connected components of any given shape.

Let $v_{n,\mathcal{P}}^2$ denote the variance of $S_{n,\mathcal{P}}$. We have a lemma analogous to Lemma [\[lem:ellis\]](#lem:ellis){reference-type="ref" reference="lem:ellis"}.

::: lemma
[]{#lem:ellispower label="lem:ellispower"} As $n$ tends to infinity, the quantity $\frac{v_{n,\mathcal{P}}^2}{|\Lambda_n|}$ tends to $v_{\mathcal{P}}^2 := \sum_{k \in \mathbb{Z}^d} \langle Z_0^{\mathcal{P}} ; Z_k^{\mathcal{P}} \rangle_{\beta,h}<\infty$.
:::

::: proof
*Proof.* That $G_{\mathcal{P}}$ is a weighted dependency graph for the family $Z^\mathcal{P}_i$ implies that $$\langle Z_0^{\mathcal{P}} ; Z_k^{\mathcal{P}} \rangle_{\beta,h} \le 
  D_2 \varepsilon^{\frac{1}{2} \left(k - \max_{\alpha,\beta \in \mathcal{D}} \|\alpha - \beta\|_1\right)}.$$ This proves that $v_{\mathcal{P}}^2$ is finite as claimed.

Let $\varepsilon>0$ be fixed. We want to show that for $n$ large enough, $$\left| \frac{v_{n,\mathcal{P}}^2}{|\Lambda_n|} - \sum_{k \in \mathbb{Z}^d} \langle Z_0^{\mathcal{P}} ; Z_k^{\mathcal{P}} \rangle_{\beta,h} \right| \leq \varepsilon.$$ We have $$\begin{aligned}
\frac{v_{n,\mathcal{P}}^2}{|\Lambda_n|} &= \frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n} \sum_{j \in \Lambda_n} \langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}} \rangle_{\beta,h}
\\&= \frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n} \sum_{j \in \mathbb{Z}^d} \langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}}\rangle_{\beta,h} - \frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n} \sum_{j \in \mathbb{Z}^d \setminus \Lambda_n} \langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}} \rangle_{\beta,h}.
\end{aligned}$$ By translation invariance of $\langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}} \rangle_{\beta,h}$, the first sum equals $\sum_{k \in \mathbb{Z}^d} \langle Z_0^{\mathcal{P}} ; Z_k^{\mathcal{P}} \rangle_{\beta,h}$. Thus the only thing left to do is to show that for $n$ large enough, the absolute value of the second term is bounded by $\varepsilon$. We cut the sum on $i$ into two parts : the points that are far from the boundary of $\Lambda_n$ and those which are not. Recall that the boundary $\partial \Lambda_n$ consists of points $j$ not in $\Lambda$, which have a neighbour in $\Lambda_n$. We denote $\delta(i,\partial \Lambda_n)=\min_{j \in \partial \Lambda_n} \parallel i-j \parallel_1$, which is the distance between $i$ and $\partial \Lambda_n$ For $R$ a positive integer, let us consider the points $i \in \Lambda_n$ at distance more than $R$ from the boundary of $\Lambda_n$. We have, again by translation invariance $$\frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n \atop \delta(i, \partial \Lambda_n) >R} \sum_{j \in \mathbb{Z}^d \setminus \Lambda_n} |\langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}} \rangle_{\beta,h}| \leq \sum_{k \in Z^d \atop |k| > R}  |\langle Z_0^{\mathcal{P}} ; Z_k^{\mathcal{P}} \rangle_{\beta,h}|.$$ But the series $\sum_{k \in \mathbb{Z}^d} |\langle Z_0^{\mathcal{P}} ; Z_k^{\mathcal{P}} \rangle_{\beta,h}|$ is absolutely convergent so the sum above tends to $0$ as $R$ tends to infinity. Therefore, there exists some integer $R_0$ such that $$\label{eq:premierepsilon}
\frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n \atop \delta(i, \partial \Lambda_n) >R_0} \sum_{j \in \mathbb{Z}^d \setminus \Lambda_n} |\langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}} \rangle_{\beta,h}| \leq \frac{\varepsilon}{2}.$$

Now let us consider the points of $\Lambda_n$ that are at distance at most $R_0$ of $\partial \Lambda_n$. There are at most $C |\partial \Lambda_n| R_0^d$ such points. Therefore $$\frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n \atop \delta(i, \partial \Lambda_n)\leq R_0} \sum_{j \in \mathbb{Z}^d \setminus \Lambda_n} |\langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}} \rangle_{\beta,h}| \leq \frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n \atop \delta(i, \partial \Lambda_n)\leq R_0} \sum_{k \in \mathbb{Z}^d} |\langle Z_0^{\mathcal{P}} ; Z_k^{\mathcal{P}} \rangle_{\beta,h}|
\leq C' \frac{|\partial \Lambda_n|}{|\Lambda_n|} R_0^d.$$

But as $n$ tends to $\infty$, $\frac{|\partial \Lambda_n|}{|\Lambda_n|}$ tends to $0$. Therefore for $n$ large enough, $$\label{eq:deuxiemeepsilon}
\frac{1}{|\Lambda_n|} \sum_{i \in \Lambda_n \atop \delta(i, \partial \Lambda_n)\leq R_0} \sum_{j \in \mathbb{Z}^d \setminus \Lambda_n} |\langle Z_i^{\mathcal{P}} ; Z_j^{\mathcal{P}} \rangle_{\beta,h}| \leq \frac{\varepsilon}{2}.$$

Adding [\[eq:premierepsilon\]](#eq:premierepsilon){reference-type="eqref" reference="eq:premierepsilon"} and [\[eq:deuxiemeepsilon\]](#eq:deuxiemeepsilon){reference-type="eqref" reference="eq:deuxiemeepsilon"} completes the proof. ◻
:::

We are now ready to prove the central limit theorem.

::: proof
*Proof of [\[th:cltpower\]](#th:cltpower){reference-type="ref" reference="th:cltpower"}.* We proceed as in the proof of Theorem [\[th:cltmagnet\]](#th:cltmagnet){reference-type="ref" reference="th:cltmagnet"}. We consider $G_{\mathcal{P}}[\Lambda_n]$.

The number of vertices is $N_n = |\Lambda'_n| = |\Lambda_n|$ and, from the discussion above, its maximal weighted degree $\Delta_n-1$ is bounded as follows: $$\Delta_n -1 \le \max_{i \in \Lambda_n} \sum_{j \in \Lambda_n} \varepsilon^{\tfrac{1}{2} \left(\|i - j\|_1 - \max_{\alpha,\beta \in \mathcal{D}} \|\alpha - \beta\|_1\right)}
   \leq \max_{i \in \Lambda_n} \sum_{j \in \Lambda_n} C_{\mathcal{P}}\varepsilon^{\tfrac{1}{2} \|i - j\|_1},$$ where $C_{\mathcal{P}}$ is a positive constant depending only on the pattern $\mathcal{P}.$ Thus by the same argument as in the proof of Theorem [\[th:cltmagnet\]](#th:cltmagnet){reference-type="ref" reference="th:cltmagnet"}, $\Delta_n -1 \leq C'_{\mathcal{P}},$ for some other constant $C'_{\mathcal{P}}$.

Again we set for all $n$, $a_n= \sqrt{|\Lambda_n|}.$ We also set $v = v_{\mathcal{P}}$ as in Lemma [\[lem:ellispower\]](#lem:ellispower){reference-type="ref" reference="lem:ellispower"} and we can choose $s$ to be any integer $\geq 3$.

Conditions (1) to (3) of Theorem [\[th:4.11modif\]](#th:4.11modif){reference-type="ref" reference="th:4.11modif"} are satisfied again and the theorem is proved. ◻
:::

::: remark
The variance $v_{\mathcal{P}}$ appearing in [\[th:cltpower\]](#th:cltpower){reference-type="ref" reference="th:cltpower"} might be equal to $0$ for some patterns $\mathcal{P}$, in which case the central limit theorem is degenerate. If the pattern has only plus spins, the same proof as before gives $v_{\mathcal{P}}>0$.
:::

### Global patterns

In this final section, we establish Theorem [\[thm:GlobalPatterns\]](#thm:GlobalPatterns){reference-type="ref" reference="thm:GlobalPatterns"}, the central limit theorem for the number of occurrences of a global pattern of spins.

To find a weighted dependency graph for the potential occurrences of $\mathcal{\tilde{P}}$ of size $m$, we consider $G_{\mathcal{\tilde{P}}}$ the restriction of $G_s^m$ to the $Z_I$'s of the form $$Z_{\{x^{(1)}, \dots ,x^{(m)}\}}^{\mathcal{\tilde{P}}}= \prod_{i=1}^m X_{(x^{(i)},\mathfrak{s}(i))}.
  \label{eq:ZXGP}$$ In $G_{\mathcal{\tilde{P}}}$, the weight of the edge between $\{x^{(1)}, \dots ,x^{(m)}\}$ and $\{y^{(1)}, \dots ,y^{(m)}\}$ is given by $$w_{\mathcal{\tilde{P}}}(\{x^{(1)}, \dots ,x^{(m)}\},\{y^{(1)}, \dots ,y^{(m)}\})=\max_{i,j \in \{1, \dots , m\}} w(x^{(i)},y^{(j)})=\varepsilon^{\frac{1}{2} \min_{i,j \in \{1, \dots , m\}}\|x^{(i)} - y^{(j)}\|_1}.$$ Again, the graph $G_{\mathcal{\tilde{P}}}$ is a $\mathbf{D}$-weighted dependency graph for $\{ Z_{\{x^{(1)}, \dots ,x^{(m)}\}}^{\mathcal{\tilde{P}}},
\{x^{(1)}, \dots ,x^{(m)}\} \subset \mathbb{Z}^d\}$, for some sequence $\mathbf{D}$ depending only on $\mathcal{P}$ as it is a restriction of the weighted dependency graph given in [\[th:powers\]](#th:powers){reference-type="ref" reference="th:powers"}.

Now define $$S_{n,\mathcal{\tilde{P}}} := \sum_{\{x^{(1)}, \dots ,x^{(m)}\} \subset \Lambda_n} Z_{\{x^{(1)}, \dots ,x^{(m)}\}}^{\mathcal{\tilde{P}}},$$ the number of occurrences of $\mathcal{\tilde{P}}$ in $\Lambda_n$. Let $v_{n,\mathcal{\tilde{P}}}^2$ denote the variance of $S_{n,\mathcal{\tilde{P}}}$.

::: proof
*Proof of [\[thm:GlobalPatterns\]](#thm:GlobalPatterns){reference-type="ref" reference="thm:GlobalPatterns"}.* Consider the weighted dependency graph $G_{\mathcal{\tilde{P}}}[\Lambda_n]$. Its number of vertices is $N_n^m = |\Lambda_n|^m$. Let us now bound its maximal weighted degree $\Delta_n-1$. Fix $\{x^{(1)}, \dots ,x^{(m)}\} \subset \Lambda_n.$ We have $$\begin{aligned}
  \sum_{\{y^{(1)}, \dots , y^{(m)}\} \subset \Lambda_n} \varepsilon^{\frac{1}{2} \min_{i,j \in \{1, \dots , m\}}\|x^{(i)} - y^{(j)}\|_1} &\leq \sum_{y^{(1)}, \dots , y^{(m)} \in \Lambda_n} \sum_{i=1}^m \sum_{j=1}^m \varepsilon^{\frac{1}{2} \|x^{(i)} - y^{(j)}\|_1} \\
&\leq \sum_{i=1}^m m |\Lambda_n|^{m-1} \sum_{y \in \Lambda_n} \varepsilon^{\frac{1}{2} \|x^{(i)} - y\|_1}.
\end{aligned}$$ By the proof of Theorem [\[th:cltmagnet\]](#th:cltmagnet){reference-type="ref" reference="th:cltmagnet"}, the last sum is bounded by a certain constant $C$. Thus $$\Delta_n-1 = \max_{\{x^{(1)}, \dots ,x^{(m)}\} \subset \Lambda_n} \sum_{y^{(1)}, \dots , y^{(m)} \in \Lambda_n} \varepsilon^{\frac{1}{2} \min_{i,j \in \{1, \dots , m\}}\|x^{(i)} - y^{(j)}\|_1} \leq m^2 |\Lambda_n|^{m-1} C.$$

We want to apply [\[th:4.11modif\]](#th:4.11modif){reference-type="ref" reference="th:4.11modif"} and set $a_n=\sqrt{v_{n,\mathcal{\tilde{P}}}^2}$. Condition (1) is trivial, while (2) holds for all weighted dependency graphs when $a_n$ is the standard deviation of $X_n$ (see [@Valentin Lemma 4.10]). Condition (3) is fulfilled since, using [\[eq:Hypo_Variance\]](#eq:Hypo_Variance){reference-type="eqref" reference="eq:Hypo_Variance"} and the inequality above for $\Delta_n$, $$\left( \frac{N_n}{\Delta_n} \right) ^{\frac{1}{s}} \frac{\Delta_n}{a_n} \le \left(\frac{|\Lambda_n|^m}{ m^2 |\Lambda_n|^{m-1} C}\right) ^{\frac{1}{s}} \frac{m^2 |\Lambda_n|^{m-1} C}{\sqrt{A |\Lambda_n|^{2m-2+\varepsilon}}}
\le \text{cst} |\Lambda_n|^{1/s-\varepsilon/2}$$ and the right-hand side tends to $0$ for $n$ big enough. ◻
:::

We now show a simple sufficient condition -- the pattern consisting in positive spins only -- so that the bound [\[eq:Hypo_Variance\]](#eq:Hypo_Variance){reference-type="eqref" reference="eq:Hypo_Variance"} of the variance is fulfilled.

We start with a lemma.

::: lemma
[]{#lem:cov_Une_Egalite label="lem:cov_Une_Egalite"} Fix $m \ge 2$. There exist some constants $R>0$ and $B>0$ such that the following holds. For any lists $(x^{(1)},\dots,x^{(m)})$ and $(y^{(1)},\dots,y^{(m)})$ such that $x^{(1)}=y^{(1)}$ but no two elements in the set $\{x^{(1)},\dots,x^{(m)},y^{(2)},\dots,y^{(m)}\}$ are at distance less than $R$, we have $$\mathop{\mathrm{Cov}}\left( \prod_{i=1}^m X_{(x^{(i)},+)}, \prod_{i=1}^m X_{(x^{(i)},+)} \right) \ge B.$$
:::

::: proof
*Proof.* By definition, and using that $X_{(x^{(1)},+)} X_{(y^{(1)},+)}=X_{(x^{(1)},+)}^2=X_{(x^{(1)},+)}$, we have $$\begin{gathered}
    \mathop{\mathrm{Cov}}\left( \prod_{i=1}^m X_{(x^{(i)},+)}, \prod_{i=1}^m X_{(x^{(i)},+)} \right) 
  =\mathbb{E}\big[ X_{(x^{(1)},+)} \cdots X_{(x^{(m)},+)} X_{(y^{(2)},+)} \dots X_{(y^{(m)},+)}\big] \\
  -\mathbb{E}\big[ X_{(x^{(1)},+)} \cdots X_{(x^{(m)},+)} \big] 
  \mathbb{E}\big[ X_{(x^{(1)},+)}  X_{(y^{(2)},+)} \dots X_{(y^{(m)},+)}\big].
\end{gathered}$$ Using the expression of joint moments in terms of cumulants -- see, e.g. [@Valentin Eq. (3)] -- and the bound for cumulants of spins ([\[thm:bound_joint_cumulants\]](#thm:bound_joint_cumulants){reference-type="ref" reference="thm:bound_joint_cumulants"}), we have that there exists a constant $\text{cst}_m$ such that $$\big|\mathbb{E}\big[ X_{(x^{(1)},+)} \dots X_{(x^{(m)},+)} \big] -
  \mathbb{E}\big[ X_{(x^{(1)},+)}] \dots.\mathbb{E}\big[ X_{(x^{(m)},+)}\big]\big|
  \le \text{cst}_m \varepsilon^R,$$ whenever the $x^{(i)}$ all lie at distance at least $R$ from each other. The same holds for the other products above and we get $$\begin{gathered}
    \mathop{\mathrm{Cov}}\left( \prod_{i=1}^m X_{(x^{(i)},+)}, \prod_{i=1}^m X_{(x^{(i)},+)} \right)
  = \big(\mathbb{E}\big[ X_{(x^{(1)},+)}\big] - \mathbb{E}\big[ X_{(x^{(1)},+)}\big]^2\big) \\
  \cdot
  \mathbb{E}\big[ X_{(x^{(2)},+)}] \cdots.\mathbb{E}\big[ X_{(x^{(m)},+)}\big]
  \mathbb{E}\big[ X_{(y^{(2)},+)}] \cdots.\mathbb{E}\big[ X_{(y^{(m)},+)}\big]
  +\text{error},
\end{gathered}$$ where the error is uniformly bounded by $\text{cst}_m \varepsilon^R$. The main term in the above equation is positive (as a product of positive terms) and independent from the $x^{(i)}$ and the $y^{(i)}$ (by translation invariance), while the error can be made as small as wanted by making $R$ tend to infinity. This proves the lemma. ◻
:::

::: proposition
[]{#prop:Variance_Lower_Bound label="prop:Variance_Lower_Bound"} Let $\mathcal{\tilde{P}}$ be a global pattern of size $m$ and assume that the function $\mathfrak{s}$ defining $\mathcal{\tilde{P}}$ takes only value $+1$. Then there exists a constant $A$ such that $\mathop{\mathrm{Var}}(S_{n,\mathcal{\tilde{P}}}) \ge A n^{2m-1}$.
:::

::: proof
*Proof.* We expand the variance as $$\mathop{\mathrm{Var}}(S_{n,\mathcal{\tilde{P}}}) = \sum_{\{x^{(1)}, \dots ,x^{(m)}\} \subset \Lambda_n \atop \{y^{(1)}, \dots ,y^{(m)}\} \subset \Lambda_n}
  \mathop{\mathrm{Cov}}(Z_{\{x^{(1)}, \dots ,x^{(m)}\}}^{\mathcal{\tilde{P}}}, Z_{\{y^{(1)}, \dots ,y^{(m)}\}}^{\mathcal{\tilde{P}}}).$$ When $\mathcal{\tilde{P}}$ involves only positive spins, the FKG inequality ensures that all summands are positive. Restricting the sum to sets with an ordering that fulfills the hypothesis of [\[lem:cov_Une_Egalite\]](#lem:cov_Une_Egalite){reference-type="ref" reference="lem:cov_Une_Egalite"} gives a lower bound. Therefore $\mathop{\mathrm{Var}}(S_{n,\mathcal{\tilde{P}}}) \ge B \cdot N_1$, where $N_1$ is the number of pairs of sets $(\{x^{(1)}, \dots ,x^{(m)}\},\{y^{(1)}, \dots ,y^{(m)}\})$ as in [\[lem:cov_Une_Egalite\]](#lem:cov_Une_Egalite){reference-type="ref" reference="lem:cov_Une_Egalite"}. For fixed $R>0$, this number is clearly of order $N^{2m-1}$, finishing the proof of the proposition. ◻
:::
