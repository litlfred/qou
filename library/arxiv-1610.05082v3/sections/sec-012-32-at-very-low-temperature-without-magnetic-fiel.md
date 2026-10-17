---
doc_id: arxiv-1610.05082v3
doc_title: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL"
section_id: sec-012-32-at-very-low-temperature-without-magnetic-fiel
section_title: "At very low temperature, without magnetic field"
section_number: 3.2
pages: 12-16
source_pdf: 1610.05082v3.pdf
source_sha256: 90c8089953ff2d97
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.963
doc_brief: "WEIGHTED DEPENDENCY GRAPHS AND THE ISING MODEL — Weighted dependency graphs have been recently introduced by the second author, as a toolbox to prove central limit theorems."
---
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

Let $A \subseteq \Lambda$ and let us define $\sigma_A := \prod_{i \in A} \sigma_i$. Its expectation is given by $$\langle \sigma_A \rangle^+_{\Lambda;\beta,0}= \sum_{\omega \in \Omega^+_{\Lambda}} \sigma_A(\omega) \frac{e^{-H_{\Lambda;\beta,0}(\omega)}}{Z^+_{\Lambda; \beta,0}}.$$ For any spin configuration $\omega \in \Omega^+_{\Lambda}$ and any contour $\gamma \in \Gamma'(\omega)$, let us define the *interior* of $\gamma$ (written $\mathop{\mathrm{Int}}(\gamma)$) as the set of points of $\Lambda$ which would have spin $-1$ if $\gamma$ was the only contour of $\omega$. We also write $\mathop{\mathrm{Int}}(X):=  \bigcup_{\gamma \in X} \mathop{\mathrm{Int}}(\gamma).$ Thus for any $\omega \in \Omega^+_{\Lambda}$ and any $i \in \Lambda$, $$\sigma_i(\omega) = (-1)^{| \{\gamma \in \Gamma'(\omega) : i \in \mathop{\mathrm{Int}}(\gamma)\}|},$$ and thus $$\begin{aligned}
\sigma_A(\omega) &= (-1)^{\sum_{i \in A} | \{\gamma \in \Gamma'(\omega) : i \in \mathop{\mathrm{Int}}(\gamma)\}|}
\\&= (-1)^{\sum_{\gamma \in \Gamma'(\omega)} | \{i \in A : i \in \mathop{\mathrm{Int}}(\gamma)\}|}.
\end{aligned}$$ Therefore one can write $$\langle \sigma_A\rangle^+_{\Lambda;\beta,0}= \frac{\Xi^{+,A}_{\Lambda;\beta,0}}{\Xi^+_{\Lambda;\beta,0}},$$ where $$\Xi^{+,A}_{\Lambda;\beta,0} := \sum_{\Gamma' \subseteq \Gamma_{\Lambda} admissible} \prod_{\gamma \in \Gamma'} (-1)^{| \{i \in A : i \in \mathop{\mathrm{Int}}(\gamma)\}|} e^{-2 \beta |\gamma|}.$$ The cluster expansion converges, which means that we have an analogue of Proposition [\[prop:cluesterexp\]](#prop:cluesterexp){reference-type="ref" reference="prop:cluesterexp"} for $\Xi^{+,A}_{\Lambda;\beta,0}$, and thus $\langle \sigma_A \rangle^+_{\Lambda;\beta,0}$ can be expressed as $$\langle \sigma_A\rangle^+_{\Lambda;\beta,0} = \exp \left( \sum_{X: \overline{X} \subseteq \Lambda} \Psi^A_{\beta}(X) -  \sum_{X: \overline{X} \subseteq \Lambda} \Psi_{\beta}(X) \right),$$ where for a cluster $X= \{\gamma_1, \dots, \gamma_r\}$,

$$\begin{aligned}
\Psi^A_\beta(X):=& \left( \prod_{\gamma \in \Gamma_{\Lambda}} \frac{1}{n_X(\gamma)!} \right) \left( \sum_{G \subseteq G_r connected} \zeta(\gamma_i,\gamma_j) \right)
\\& \times (-1)^{ \sum_{j=1}^r | \{i \in A : i \in \mathop{\mathrm{Int}}(\gamma_j)\}|} e^{-2 \beta \sum_{j=1}^r |\gamma_j|}.
\end{aligned}$$

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
*Proof.* Using Proposition [\[prop:expectation\]](#prop:expectation){reference-type="ref" reference="prop:expectation"}, we have $$\log Q \left(\sigma_j; j \in A \right)  = \sum_{\delta \subseteq A, \delta \neq \emptyset} (-1)^{|\delta|} \sum_{X \sim \delta} (\Psi^{\delta}_{\beta}(X) -  \Psi_{\beta}(X)).$$ Recall that $X \sim \delta$ means that at least one point of $\delta$ is in the interior of a contour in $X$. We split the second sum depending on the exact subset $I \subseteq \delta$ of points that are in the interior of a contour in $X$. By definition of $\Psi$ observe, if $I$ is as above, $\Psi^{\delta}_{\beta}(X)= \Psi^{I}_{\beta}(X)$. Therefore $$\begin{aligned}
\log Q \left(\sigma_j; j \in A \right) &=  \sum_{\delta \subseteq A, \delta \neq \emptyset} (-1)^{|\delta|} \sum_{ I \subseteq \delta : \atop I \neq \emptyset} \sum_{X : \atop \mathop{\mathrm{Int}}(X) \cap \delta =I } (\Psi^{I}_{\beta}(X) -  \Psi_{\beta}(X))
\\ &= \sum_{ I \subseteq A : \atop I \neq \emptyset} \sum_{X : \atop I \subseteq \mathop{\mathrm{Int}}(X)} (\Psi^{I}_{\beta}(X) -  \Psi_{\beta}(X)) \sum_{\delta : \atop I \subseteq \delta \subseteq (I \cup  (A \setminus \mathop{\mathrm{Int}}(X)))} (-1)^{|\delta|}.
\end{aligned}$$ But the last sum is equal to $0$ unless $A$ is contained in $\mathop{\mathrm{Int}}(X)$. Therefore we obtain $$\begin{aligned}
\log Q  \left(\sigma_j; j \in A \right)  &= \sum_{X : \atop A \subseteq \mathop{\mathrm{Int}}(X)} \sum_{ I \subseteq A : \atop I \neq \emptyset} (-1)^{|I|}(\Psi^{I}_{\beta}(X) -  \Psi_{\beta}(X)).
\end{aligned}$$ Finally, there are $2^r-1$ non-empty subsets of $A$, and $|\Psi^{I}_{\beta}(X)| \leq |\Psi_{\beta}(X)|$ for all $X$ and $I$, thus $$\label{eq:boundlogQ}
\left| \log Q \left(\sigma_j; j \in A \right) \right| \leq \sum_{X : \atop A \subseteq \mathop{\mathrm{Int}}(X)} 2(2^r-1) |\Psi_{\beta}(X)|.$$ We conclude by using a trick similar to Lemma [\[lem:BoudingTheSum_HT\]](#lem:BoudingTheSum_HT){reference-type="ref" reference="lem:BoudingTheSum_HT"}. By [@Velenik Equation (5.31)], if $\beta \geq \beta_{\text{ce}}^{\text{lt}}(d)$, for any vertex $v \in \mathbb{Z}^d$, we have the bound $$\sum_{X: \overline{X} \ni v} \left| \Psi_{\beta} (X)\right| \leq 1.$$ Thus if $\beta \geq 2 \beta_{\text{ce}}^{\text{lt}}(d)$, $$\sum_{X: \overline{X} \ni v} \left| \Psi_{\beta}(X) e^{\beta |\overline{X}|}\right| \leq \sum_{X: \overline{X} \ni v} \left| \Psi_{\frac{\beta}{2}} (X)\right| \leq 1.$$ So for any positive integer $R$, $$\label{eq:boundbetaLT}
\sum_{X: \overline{X} \ni v \atop |\overline{X}| \geq R} \left| \Psi_{\beta}(X)\right| \leq  e^{-\beta R} \sum_{X: \overline{X} \ni v} \left| \Psi_{\beta}(X) e^{\beta |\overline{X}|}\right| \leq e^{-\beta R}.$$ Let us now turn back to Eq. [\[eq:boundlogQ\]](#eq:boundlogQ){reference-type="eqref" reference="eq:boundlogQ"}. Every cluster $X$ such that $A \subseteq \mathop{\mathrm{Int}}(X)$ satisfies $|\overline{X}| \geq 2 \ell_T(A).$ Moreover, if a cluster of size $R$ has $j_1 \in A$ in its interior, then it contains at least a point $v$ which is at distance at most $R$ of $j_1$. There are at most $C R^d$ such points, therefore $$\begin{aligned}
\sum_{X : \atop A \subseteq \mathop{\mathrm{Int}}(X)} |\Psi_{\beta}(X)| &\leq \sum_{R \geq 2\ell_T(A)} C R^d  \left[\sum_{X: \overline{X} \ni v \atop |\overline{X}| = R} \left| \Psi_{\beta}(X)\right| \right] \\
&\leq C \sum_{R \geq 2\ell_T(A)} R^d e^{-\beta R} \\
&\leq C' e^{-c \beta \ell_T(A)},
\end{aligned}$$ for $\beta$ large enough, where $C'$ and $c$ are some positive constants (and $c$ depends on the dimension $d$ of the ambiant space). Thus by [\[eq:boundlogQ\]](#eq:boundlogQ){reference-type="eqref" reference="eq:boundlogQ"}, $$\left| \log Q \left(\sigma_j; j \in A \right) \right| \leq C'_r e^{-c \beta \ell_T(A)},$$ for some positive constant $C'_r$ depending on $r$. Exponentiating completes the proof. ◻
:::

Now we can convert this estimate into the desired bound on joint cumulants.

::: proposition
[]{#prop:boundcum label="prop:boundcum"} Let $A$ be a finite subset of $\mathbb{Z}^d$ of size $r$. Then, for $\beta$ large enough, $$|\kappa_{\beta,0} \left(\sigma_j; j \in A \right)| 
\leq D_r e^{\frac{-c \beta \ell_T(A)}{2}},$$ where $c=c(d)$ is given by [\[lem:quotient\]](#lem:quotient){reference-type="ref" reference="lem:quotient"} and $D_r$ is a positive constant depending on $r$.
:::

::: proof
*Proof.* By Lemma [\[lem:quotient\]](#lem:quotient){reference-type="ref" reference="lem:quotient"}, $$Q_{\beta,0} \left(\sigma_j; j \in A \right) = 1+ \mathcal{O}(\mathcal{M} \big( G[A] \big)),$$ where $G$ is the weighted graph defined on $\mathbb{Z}^d$ such that for each $e=(i,j)$, $w_e = e^{\frac{-c \beta \|i - j\|_1}{2}}$. Indeed in that case $\mathcal{M} \big( G[A] \big) = e^{\frac{-c \beta \ell_T'(A)}{2}} \geq e^{-c \beta \ell_T(A)}$; see the discussion in [\[Subsect:Spanning\]](#Subsect:Spanning){reference-type="ref" reference="Subsect:Spanning"}.

Then using Proposition 5.8 of [@Valentin], we deduce that $$|\kappa_{\beta,0} \left(\sigma_j; j \in A \right)| = \prod_{j \in A} \langle\sigma_j\rangle_{\beta,0}^+ \times \mathcal{O}(\mathcal{M} \big( G[A] \big)).$$ But for all $j \in A$, we have $\langle \sigma_j \rangle_{\beta,0}^+ \leq 1,$ and for $\beta$ large enough, $\langle \sigma_j \rangle_{\beta,0}^+ > 0.$ Hence $$0 < \prod_{j \in A} \langle \sigma_j \rangle_{\beta,0}^+ \leq 1.$$ Moreover by Proposition [\[prop:2longueurs\]](#prop:2longueurs){reference-type="ref" reference="prop:2longueurs"}, $$\mathcal{M} \big( G[A] \big) = e^{\frac{-c_d \beta \ell_T'(A)}{2}} \leq e^{\frac{-c_d \beta \ell_T(A)}{2}}.$$ Thus $|\kappa_{\beta,0} \left( \sigma_j; j \in A \right)| \leq D_r  e^{\frac{-c_d \beta \ell_T(A)}{2}}$, as claimed. ◻
:::
