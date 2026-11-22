---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-024-54-functionals-of-markov-chains
section_title: "Functionals of Markov chains"
section_number: 5.4
pages: 44-49
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.975
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
In this section, we consider a discrete time Markov chain $(M_t)_{t \ge 0}$ on a finite state space $\mathfrak{X}$, which is ergodic (irreducible and aperiodic) with invariant measure $\pi$. Its transition matrix is denoted $P$. To simplify the discussion, we shall also assume that the Markov chain is stationary, that is to say that the initial measure (*i.e.* the law of $M_0$) is $\pi$; most results have easy corollaries for any initial measure, using the fast mixing of such Markov chains.

Let us consider a sequence $(f_t)_{t \ge 0}$ of functions on $\mathfrak{X}$ that is uniformly bounded by a constant $K$. We set $Y_t=f_t(M_t)$. We will show that $\{Y_t\}_{t \in \mathbb{N}}$ admits a uniform weighted dependency graph. The proof roughly follows the one of [@WDG Section 10], where it was proved that it has a (non-uniform) weighted dependency graph, taking extra care of the dependence in the order $r$ of the cumulant in the bounds. Instead of working directly with classical (joint) cumulants, we start by giving a bound for the so-called *Boolean cumulants*. Classical cumulants are then expressed in terms of Boolean cumulants thanks to a formula of Saulis and Statulevičius [@LivreOrange:Cumulants Lemma 1.1]; see also a recent article of Arizmendi, Hasebe, Lehner and Vargas [@ArizmendiHasebeLehnerVargas2014] (we warn the reader that, in [@LivreOrange:Cumulants], Boolean cumulants are called centered moments).

Let $Z_1,\ldots,Z_r$ be random variables with finite moments defined on the same probability space. By definition, their Boolean (joint) cumulant is $$\begin{aligned}
  &B^{(r)}(Z_1,\ldots,Z_r) \\
  &= \sum_{l=0}^{r-1} (-1)^{l} \!\!\!\!\sum_{1\le d_1 < \cdots <d_l \le r-1} \!\!\!\!\!\!\!
\mathbb{E}[Z_1 \cdots Z_{d_1}] \, \mathbb{E}[Z_{d_1+1} \cdots Z_{d_2}] \, \cdots \, \mathbb{E}[Z_{d_l+1} \cdots Z_r].
\end{aligned}$$ While not at first sight, this definition is quite similar to the definition of classical (joint) cumulants, replacing the lattice of all set partitions by the lattice of interval set partitions; see [@ArizmendiHasebeLehnerVargas2014 Section 2] for details. Note however that, unlike classical cumulants, Boolean cumulants are not symmetric functionals.

::: proposition
[]{#prop:Bound_Boolean label="prop:Bound_Boolean"} Let $r\geq 1$. With the above notation, there exists a constant $\theta_{P}$ depending on $P$ with the following property. For any integers $t_1 \le t_2 \le \cdots \le t_r$, we have $$\left|B^{(r)}(Y_{t_1},\ldots,Y_{t_r}) \right| \le M^{\frac{r-1}{2}} \,K^r\, (\theta_P)^{t_r-t_1},$$ where $M = |\mathfrak{X}|$.
:::

The proof of this bound relies on arguments due to Diaconis, Stroock and Fill, see [@DS91; @Fil91]. We also refer to [@LivreOrange:Cumulants Section 4.1] for an alternate approach. Given an ergodic transition matrix $P$ on $\mathfrak{X}$ with invariant measure $\pi$, we denote $\widetilde{P}$ the time reversal of $P$, which is the stochastic matrix defined by the equation $$\widetilde{P}(x,y) = \frac{\pi(y)\,P(y,x)}{\pi(x)}.$$ This new transition matrix is again ergodic, with stationary measure $\pi$. The multiplicative reversiblization of $P$ is the matrix $M(P)=P\widetilde{P}$. It is a stochastic matrix, which is ergodic with stationary measure $\pi$, and with all its eigenvalues that are real and belong to $[0,1]$. Indeed, if $D$ is the diagonal matrix $D = \mathrm{diag}(\pi)$, then $\widetilde{P} = D^{-1}P^tD$, and $$\begin{aligned}
\mathrm{Spec}(M(P)) &= \mathrm{Spec}\left(D^{1/2}P\widetilde{P}D^{-1/2}\right) \\
&= \mathrm{Spec}\left((D^{1/2}PD^{-1/2})(D^{-1/2}P^t D^{1/2})\right) \\
&= \mathrm{Spec}\left((D^{1/2}PD^{-1/2})(D^{1/2}PD^{-1/2})^t\right).
\end{aligned}$$ Thus, $M(P)$ has the spectrum of a symmetric positive matrix, so it belongs to $\mathbb{R}_+$, and in fact to $[0,1]$ since $M(P)$ is also stochastic. We denote $$(\theta_P)^2 = \max\{|z|\,|\,z \text{ eigenvalue of }M(P),\,z \neq 1\}.
  \label{eq:def_thetaP}$$ Notice that if $P$ is reversible, then $\widetilde{P}=P$ and $M(P)=P^2$, so in this case $$\theta_P=\max\{|z|\,|\,z \text{ eigenvalue of }P,\,z \neq 1\}.$$ In general, one can think of $\theta_P$ as the analogue of the second largest eigenvalue for non-reversible transition matrices. The following result estimates the rate of convergence of the Markov chain associated to $P$ in terms of $\theta$:

::: theorem
[]{#thm:fill label="thm:fill"} For any $x \in \mathfrak{X}$, $$\begin{aligned}
\sum_{y \in \mathfrak{X}} |P^t(x,y)-\pi(y)| &\leq \frac{(\theta_P)^t}{\sqrt{\pi(x)}}; \\
\sum_{y \in \mathfrak{X}} \frac{|P^t(x,y)-\pi(y)|}{\sqrt{\pi(y)}} &\leq \sqrt{M}\,\frac{(\theta_P)^t}{\sqrt{\pi(x)}}
\end{aligned}$$ where $M = |\mathfrak{X}|$.
:::

::: proof
*Proof.* For completeness, we reproduce here the discussion of [@Fil91 Section 2], which relies on the following identity due to Mihail. If $f$ is a function on $\mathfrak{X}$, we denote $\mathrm{Var}(f)$ its variance under the stationary probability measure $\pi$. We also introduce the Dirichlet form $$\mathscr{E}(f,g) = \frac{1}{2}\sum_{x,y\in \mathfrak{X}} (f(x)-f(y))(g(x)-g(y))\,\pi(x)\,M(P)(x,y).$$ Then, for any function $f$, $$\mathrm{Var}(f) = \mathrm{Var}(\widetilde{P}f) + \mathscr{E}(f,f).$$ Indeed, one can assume w.l.o.g. that $\pi(f)=\sum_{x\in \mathfrak{X}}\pi(x)f(x)=0$. If $\left\langle f\vphantom{g}\,\right |\left.g \vphantom{f}\right\rangle_{\pi} = \sum_{x\in\mathfrak{X}} \pi(x)\,f(x)\,g(x)$, then $$\begin{aligned}
\mathscr{E}(f,f) &= \left\langle f\vphantom{(\mathrm{id}- M(P))f}\,\right |\left.(\mathrm{id}- M(P))f \vphantom{f}\right\rangle_\pi = \left\langle f\vphantom{f}\,\right |\left.f \vphantom{f}\right\rangle_\pi - \left\langle f\vphantom{P\widetilde{P}f}\,\right |\left.P\widetilde{P}f \vphantom{f}\right\rangle_\pi \\
&=\left\langle f\vphantom{f}\,\right |\left.f \vphantom{f}\right\rangle_\pi - \left\langle \widetilde{P}f\vphantom{\widetilde{P}f}\,\right |\left.\widetilde{P}f \vphantom{\widetilde{P}f}\right\rangle_\pi = \mathrm{Var}(f)-\mathrm{Var}(\widetilde{P}f)
\end{aligned}$$ since $\widetilde{P}$ is the adjoint of $P$ for the action on the left of functions and with respect to the scalar product $\left\langle \cdot\vphantom{\cdot}\,\right |\left.\cdot \vphantom{\cdot}\right\rangle_\pi$. Consider now a Markov chain $(X_t)_{t \in \mathbb{N}}$ on $\mathfrak{X}$ with arbitrary initial distribution $\pi_0$, and denote $\pi_t = \pi_0P^t$ the distribution at time $t$. We introduce the quantity $$(\chi_t)^2 = \sum_{y \in \mathfrak{X}} \frac{(\pi_t(y)-\pi(y))^2}{\pi(y)}.$$ This is the variance of $f_t=\frac{\pi_t}{\pi}$ with respect to the probability measure $\pi$. By Mihail's identity, $$(\chi_{t+1})^2 = \mathrm{Var}(f_{t+1})=\mathrm{Var}(\widetilde{P}f_t) =\mathrm{Var}(f_t) - \mathscr{E}(f_t,f_t) = (\chi_t)^2 - \mathscr{E}(f_t,f_t).$$ By the minimax characterization of eigenvalues of symmetric positive matrices, $$(\theta_P)^2 = 1-\inf\left\{ \frac{\mathscr{E}(f,f)}{\mathrm{Var}(f)},\,f\text{ non-constant}\right\}.$$ Therefore, $(\chi_{t+1})^2 \leq (\theta_P)^2\,(\chi_t)^2$, and $(\chi_t)^2 \leq (\theta_P)^{2t}\,(\chi_0)^2$ by induction on $t$. On the other hand, the Cauchy-Schwarz inequality yields $$\sum_{y \in \mathfrak{X}} |\pi_t(y)-\pi(y)| \leq \sqrt{\sum_{y\in \mathfrak{X}} \pi(y)}\,\sqrt{\sum_{y \in \mathfrak{X}} \frac{(\pi_t(y)-\pi(y))^2}{\pi(y)}} = \chi_t.$$ If we choose $\pi_0=\delta_x$, we finally obtain: $$\sum_{y \in \mathfrak{X}} |P^t(x,y)-\pi(y)| \leq (\theta_P)^t\,\chi_0 = (\theta_P)^t \sqrt{\frac{1}{\pi(x)}-1} \leq \frac{(\theta_P)^t}{\sqrt{\pi(x)}}.$$ Similarly, $$\sum_{y \in \mathfrak{X}} \frac{|P^t(x,y)-\pi(y)| }{\sqrt{\pi(y)}} \leq \sqrt{M}\,\chi_t \leq \sqrt{M}\,(\theta_P)^t\,\chi_0 \leq \sqrt{M}\,\frac{(\theta_P)^t}{\sqrt{\pi(x)}}.\qquad\qed$$ ◻
:::

::: proof
*Proposition [\[prop:Bound_Boolean\]](#prop:Bound_Boolean){reference-type="ref" reference="prop:Bound_Boolean"}.* If $f:\mathfrak{X}\to \mathbb{R}$, denote $D_f=\mathrm{diag}(f(x),x\in \mathfrak{X})$. Then, the Boolean cumulant has the following matrix expression: $$B^{(r)}(Y_{t_1},\ldots,Y_{t_r}) = \pi\,D_{f_{t_1}}\,(P^{t_2-t_1}-\textbf{1}\,\pi)\,\cdots\, D_{f_{t_{r-1}}}\,(P^{t_r-t_{r-1}}-\textbf{1}\,\pi)\,D_{f_{t_r}}\,\textbf{1},$$ where $\textbf{1}$ is the column vector with all its entries equal to $1$; see [@WDG Lemma 10.1]. If we expand this expression as a sum, and denote $Q_t = P^t - \textbf{1}\,\pi$ and $\delta_i=t_{i+1}-t_i$, then $$\begin{aligned}
  &B^{(r)}(Y_{t_1},\ldots,Y_{t_r}) \\
  & = \sum_{x_1,\ldots,x_r}\pi(x_1)\,f_{t_1}(x_1)\,Q_{t_2-t_1}(x_1,x_2)\,f_{t_2}(x_2)\,\cdots\, Q_{t_r-t_{r-1}}(x_{r-1},x_r)\,f_{t_r}(x_r) 
\end{aligned}$$ and we obtain $$\begin{aligned}
|B^{(r)}&(Y_{t_1},\ldots,Y_{t_r})|\leq K^r \sum_{x_1,\ldots,x_r}\pi(x_1)\,|Q_{\delta_1}(x_1,x_2)|\,\cdots\,|Q_{\delta_{r-1}}(x_{r-1},x_r)| \\
&\leq K^r\,(\theta_P)^{\delta_{r-1}} \sum_{x_1,\ldots,x_{r-1}}\pi(x_1)\,|Q_{\delta_1}(x_1,x_2)|\,\cdots\,\frac{|Q_{\delta_{r-2}}(x_{r-2},x_{r-1})|}{\sqrt{\pi(x_{r-1})}}\\
&\qquad\vdots \\
&\leq K^r\,M^{\frac{r-2}{2}}\,(\theta_P)^{t_r-t_1} \sum_{x_1}\sqrt{\pi(x_1)} \leq K^{r} M^{\frac{r-1}{2}}\,(\theta_P)^{t_r-t_{1}}.\qquad\qed
\end{aligned}$$ ◻
:::

::: proposition
[]{#prop:UWDG_Markov label="prop:UWDG_Markov"} The family of random variables $\{Y_t\}_{t \in \mathbb{N}}$ admits a $K\sqrt{M}$-uniform weighted dependency graph, where, for integers $s<t$, the weight between $Y_t$ and $Y_s$ is $2(\theta_P)^{t-s}$.
:::

::: proof
*Proof.* A lemma of Saulis and Statulevičius [@LivreOrange:Cumulants Lemma 1.1] expresses usual cumulants in terms of Boolean cumulants: $$\kappa^{(r)}(Y_{t_1},\ldots,Y_{t_r}) = \sum_{\pi \in \mathcal{P}([r])} (-1)^{|\pi|-1}
 N(\pi) \prod_{C \in \pi} B^{(|C|)}(Y_{t_j},\,  j \in C).
 \label{eq:Boolean2Classical}$$ Here, the sum runs over set-partitions $\pi$ of $[r]:=\{1,\ldots,r\}$; $|\pi|$ is the number of blocks of a set-partition $\pi$, the product runs over blocks $C$ in $\pi$ and $B^{(|C|)}(Y_{t_j},\, j \in C)$ is the Boolean cumulant of the subfamily $(Y_{t_j})$ indexed by integers $j$ in the block $C$, with the times ordered in increasing order (recall that the Boolean are not symmetric functionals). Finally $N(\pi)$ is a combinatorial factor that can be computed as follows. For each block $C$ of $\pi$, denote $m_C$ and $M_C$ its smallest and biggest elements; then call $n_C$ the number of blocks $C' \ne C$ such that $m_C$ is in the interval $[m_{C'};M_{C'}]$. We finally define $N(\pi)=\prod_{C \in \pi; 1 \notin C} n_C$. In other terms, $N(\pi)$ counts the functions $g$ mapping each block $C$ of $\pi$ (except the one containing $1$) to a block $g(C) \ne C$ such that $m_C \in [m_{g(C)};M_{g(C)}]$.

Let us make an observation. If $\pi$ is a partition and $k$ an integer such that each block of $\pi$ either contains only numbers smaller than or equal to $k$ or only numbers bigger than $k$ ($\pi$ is then said to be *disconnected*), then no function $g$ as above exists (there is no possible image for the block $C$ containing $k+1$) and $N(\pi)=0$. On the other hand, for *connected* partitions $\pi$, we always have $N(\pi)>0$, so that the sum in [\[eq:Boolean2Classical\]](#eq:Boolean2Classical){reference-type="eqref" reference="eq:Boolean2Classical"} is in effect a sum over connected partitions.

Eq. [\[eq:Boolean2Classical\]](#eq:Boolean2Classical){reference-type="eqref" reference="eq:Boolean2Classical"} and Proposition [\[prop:Bound_Boolean\]](#prop:Bound_Boolean){reference-type="ref" reference="prop:Bound_Boolean"} imply the bound $$\left|\kappa^{(r)}(Y_{t_1},\ldots,Y_{t_r}) \right| \leq \left(K\sqrt{M}\right)^r
   \sum_{\pi \in \mathcal{P}([r])} 
   N(\pi) \prod_{C \in \pi} (\theta_P)^{t_{M_C}-t_{m_C}}.$$ We would like to prove $$\left|\kappa^{(r)}(Y_{t_1},\ldots,Y_{t_r}) \right| \leq 2^{r-1}\,\left(K\sqrt{M}\right)^r
   \sum_{T \in \mathop{\mathrm{ST}}(K_r)} w(T),$$ where $w(T)=\prod_{ \{j,j'\} \in E_T, \, j<j'} (\theta_P)^{t_{j'}-t_j}$. Therefore it is sufficient for us to find an injective mapping $\eta$ from pairs $(\pi,g)$ as above to edge-bicolored spanning trees $\widetilde{T}$ such that $$w\big( \eta(\pi,g) \big) =  \prod_{C \in \pi} (\theta_P)^{t_{M_C}-t_{m_C}}; 
  \label{eq:eta_Conserve_Poids}$$ here, by convention, the weight $w(\widetilde{T})$ of a colored tree is the weight $w(T)$ of its uncolored version. In the following, we describe such a mapping, concluding the proof of the proposition.

Let $(\pi,g)$ be a pair of objects as above: $\pi$ is a set-partition of $[r]$ and $g$ is function mapping each block $C$ of $\pi$ (except the one containing $1$) to a block $g(C) \ne C$ such that $m_C \in [m_{g(C)};M_{g(C)}]$. For each block $C$ of $\pi$, we consider the set $$S(C)=C \cup \{m_{C'},\, C' \in g^{-1}(C)\}.$$ Let us call $P_C$ the path with vertex-set $S(C)$, where the vertices are in increasing order along the path. We also color in blue (resp. in red) edges of this path whose extremity with smaller label is in $C$ (resp. in $\{m_{C'},\, C' \in g^{-1}(C)\}$).

As an example, take $\pi=\{C_1,\cdots,C_6\}$ with $C_1=\{1,5,10\}$, $C_2=\{2,11\}$, $C_3=\{3,9\}$, $C_4=\{4,6,13\}$, $C_5=\{7,12\}$, $C_6=\{8\}$. As function $g$, we take $g(C_2)=C_1$, $g(C_3)=C_1$, $g(C_4)=C_2$, $g(C_5)=C_1$ and $g(C_6)=C_4$. In this case, we get $S(C_1)=\{1,2,3,5,7,10\}$, $S(C_2)=\{2,4,11\}$, $S(C_4)=\{4,6,8,13\}$ and $S(C_i)=C_i$ for $i \in \{3,5,6\}$. The associated bicolored paths are drawn in Fig. [1](#fig:example_eta){reference-type="ref" reference="fig:example_eta"}.

<figure id="fig:example_eta">
<div class="center">

</div>
<figcaption>Illustration of the construction <span class="math inline"><em>η</em></span> in the proof of Proposition <a href="#prop:UWDG_Markov" data-reference-type="ref" data-reference="prop:UWDG_Markov">[prop:UWDG_Markov]</a>: the path <span class="math inline"><em>P</em><sub><em>C</em><sub><em>i</em></sub></sub></span> and their gluing <span class="math inline"><em>η</em>(<em>π</em>,<em>g</em>)</span>. For readers of a black-and-white printed version, red edges are thicker.</figcaption>
</figure>

As in Fig. [1](#fig:example_eta){reference-type="ref" reference="fig:example_eta"}, we then take the union of the paths $P_{C_i}$, identifying vertices with the same label (the minimum $m_C \ne 1$ of a block $C$ appears in the path $S(C)$ and in the path $S(g(C))$). Doing that, we get an edge-bicolored graph that we call $\eta(\pi,g)$. Let us first check that $\eta(\pi,g)$ is a tree. To this purpose, we order the blocks $C_1,\ldots, C_{|\pi|}$ of $\pi$ in increasing order of their minima (as done in the example). Observe that this implies that $g(C_i)=C_j$ for some $j<i$. We will prove by induction that, for each $i \le |\pi|$, $P_{C_1} \cup \cdots \cup P_{C_i}$ is a tree. The case $i=1$ is trivial. For $i>1$, the graph $P_{C_1} \cup \cdots \cup P_{C_i}$ is obtained by gluing the path $P_{C_i}$ on the graph $P_{C_1} \cup \cdots \cup P_{C_{i-1}}$, identifying $m_{C_i}$ which appears in both. Since $P_{C_1} \cup \cdots \cup P_{C_{i-1}}$ is a tree by induction hypothesis, the resulting graph $P_{C_1} \cup \cdots \cup P_{C_i}$ is a tree as well, concluding the induction. Thus $\eta(\pi,g)= P_{C_1} \cup \cdots \cup P_{C_{|\pi|}}$ is a tree.

The equality [\[eq:eta_Conserve_Poids\]](#eq:eta_Conserve_Poids){reference-type="eqref" reference="eq:eta_Conserve_Poids"} is easy: since the edge set of $\eta(\pi,g)$ is the union of the edge sets of the $P_{C_i}$, we have $$w\big( \eta(\pi,g) \big) = \prod_{i=1}^{|\pi|} w(P_{C_i}) = \prod_{i=1}^{|\pi|} (\theta_P)^{t_{M_{C_i}}-t_{m_{C_i}}}.$$ We finally need to prove that $\eta$ is injective, *i.e.* that we can recover $(\pi,g)$ from $\eta(\pi,g)$. We start by the following easy observation: in $\eta(\pi,g)$, vertices with a red incident edge going to a vertex with bigger label are exactly the vertices with a label which is the minimum $m_C \ne 1$ of a block $C$ of $\pi$. By construction, such vertices have at most three incident edges, which are as follow:

1.  []{#item:edge2 label="item:edge2"} as said above, a first one is red and goes to a vertex to bigger label;

2.  []{#item:edge3 label="item:edge3"} a second one is either blue or red and goes to a vertex of lower label.

3.  []{#item:edge1 label="item:edge1"} possibly, a last one is blue and goes to a vertex to bigger label (there is such an edge when $m_C$ is not alone in its block);

Indeed, in the construction, edges [\[item:edge2\]](#item:edge2){reference-type="ref" reference="item:edge2"} and [\[item:edge3\]](#item:edge3){reference-type="ref" reference="item:edge3"} comes from $S_{g(C)}$ while edge [\[item:edge1\]](#item:edge1){reference-type="ref" reference="item:edge1"} comes from $S_C$. We split the vertex $m_C$ into two, keeping edges [\[item:edge2\]](#item:edge2){reference-type="ref" reference="item:edge2"} and [\[item:edge3\]](#item:edge3){reference-type="ref" reference="item:edge3"} in the same component. Doing that for the $|\pi|-1$ vertices $m_C \ne 1$, we inverse the gluing step of the construction of $\eta(\pi,g)$. It is then straightforward to recover $(\pi,g)$.0◻ ◻
:::

::: theorem
[]{#thm:kolmogorovmarkov label="thm:kolmogorovmarkov"} Let $(X_t)_{t \in \mathbb{N}}$ be an ergodic Markov chain on a finite state space $\mathfrak{X}$ of size $M$, and $\theta_P<1$ the constant associated by [\[eq:def_thetaP\]](#eq:def_thetaP){reference-type="eqref" reference="eq:def_thetaP"} with the transition matrix $P$. We consider a sum $S_n= \sum_{t = 1}^n f_t(X_t)$ with $\|f_t\|_{\infty} \le K$. Then, for any $r \ge 1$, $$\left|\kappa^{(r)}(S_n)\right| \le n \, r^{r-2}  \left(2\,\frac{1+\theta_P}{1-\theta_P}\right)^{r-1} \left(K\sqrt{M}\right)^r.
    \label{eq:BorneCumulantMarkov}$$ As a consequence:

1.  When $\frac{\mathop{\mathrm{Var}}(S_n)}{n^{2/3}} \to +\infty$, we have $$d_\mathrm{Kol}\left( \frac{S_n-\mathbb{E}[S_n]}{\sqrt{\mathop{\mathrm{Var}}(S_n)}}\,,\, \mathcal{N}_{\mathbb{R}}(0,1)\right)
      \le 76.36\,\left(\frac{K\sqrt{M}}{\sqrt{\frac{\mathrm{Var}(S_n)}{n}}}\right)^{\!3}\,\left(\frac{1+\theta_P}{1-\theta_P}\right)^2\,\frac{1}{\sqrt{n}},$$ and in particular, $\frac{S_n-\mathbb{E}[S_n]}{\sqrt{\mathrm{Var}(S_n)}}$ converges in law to a standard Gaussian.

2.  This convergence in law happens as soon as $\frac{\mathrm{Var}(S_n)}{n^{\varepsilon}} \to \infty$ for some $\varepsilon>0$.
:::

::: proof
*Proof.* Combining Propositions [\[prop:UWDG_Markov\]](#prop:UWDG_Markov){reference-type="ref" reference="prop:UWDG_Markov"} and [\[Prop:BoundCumulantUWDG\]](#Prop:BoundCumulantUWDG){reference-type="ref" reference="Prop:BoundCumulantUWDG"}, the sum $S_n$ admits uniform bounds on cumulants with parameters $$D_n=\left(1+2\sum_{t=1}^\infty (\theta_P)^t\right) = \frac{1+\theta_P}{1-\theta_P},$$ $N_n=n$ and $A = K\sqrt{M}$. Observe that $D_n$ is here independent of $n$. We can apply Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"} to get the first part of the theorem. The second follows from Theorem [\[thm:CLT_Janson\]](#thm:CLT_Janson){reference-type="ref" reference="thm:CLT_Janson"}.0◻ ◻
:::

::: remark
A bound similar to Eq. [\[eq:BorneCumulantMarkov\]](#eq:BorneCumulantMarkov){reference-type="eqref" reference="eq:BorneCumulantMarkov"} is given in [@LivreOrange:Cumulants Theorem 4.19]. We believe however that the proof given there is not correct. Indeed, the proof associates with each partition $\pi$ such that $N(\pi) \ne 0$ a sequence of number $q_j$; the authors then claim that "obviously $q_j \le q_{j+1}$" (p. 93, after eq. (4.53)). This is unfortunately not the case as can be seen on the example of partitions given p. 81 in *loc. cit.*: for this partition $q_3=3$, while $q_4=2$. As a consequence of this mistake, the authors forget many partitions $\pi$ when expressing classical cumulants in terms of Boolean cumulants (since they encode partitions with only non-decreasing sequences $q_i$), which make the resulting bound on classical cumulants too sharp. We have not found a simpler way around this error than the use of uniform weighted dependency graphs presented here. Note nevertheless that our proof still uses several ingredients from [@LivreOrange:Cumulants]: the use of Boolean cumulants and the relation between Boolean and classical cumulants.
:::

::: remark
If the functions $f_t$ are indicators $f_t(x)=1_{x=s_t}$, then one can remove the size $(\sqrt{M})^3$ in the bound on the Kolmogorov distance. Indeed, in this case, we have $$B^{(r)}(Y_{t_1},\ldots,Y_{t_r}) = \pi(s_1)\,Q_{t_2-t_1}(s_1,s_2)Q_{t_3-t_2}(s_2,s_3)\cdots Q_{t_{r}-t_{r-1}}(s_{r-1},s_r).$$ On the other hand, the individual terms of the matrix $Q_{t}(x,y)$ can be bounded by $$|Q_{t}(x,y)| \leq \sqrt{\frac{\pi(y)}{\pi(x)}}\,(\theta_P)^t,$$ by adapting the proof of Theorem [\[thm:fill\]](#thm:fill){reference-type="ref" reference="thm:fill"}. Therefore, $$\begin{aligned}
\left|B^{(r)}(Y_{t_1},\ldots,Y_{t_r})\right| &\leq (\theta_P)^{t_r-t_1}\, \pi(s_1)\,\sqrt{\frac{\pi(s_2)}{\pi(s_1)}} \cdots \sqrt{\frac{\pi(s_r)}{\pi(s_{r-1})}} \\
&\leq (\theta_P)^{t_r-t_1} \sqrt{\pi(s_1)\pi(s_r)} \leq (\theta_P)^{t_r-t_1}.
\end{aligned}$$ Thus, in this case, one has the bound of Theorem [\[thm:kolmogorovmarkov\]](#thm:kolmogorovmarkov){reference-type="ref" reference="thm:kolmogorovmarkov"} without the factor $(\sqrt{M})^3$.
:::
