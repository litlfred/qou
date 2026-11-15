---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-023-53-magnetization-of-the-ising-model
section_title: "Magnetization of the Ising model"
section_number: 5.3
pages: 42-44
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.974
latex_coverage_ratio: 0.969
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#subsec:Ising label="subsec:Ising"} We consider here the nearest-neighbour Ising model on a finite subset $\Lambda$ of $\mathbb{Z}^d$ with a quadratic potential, *i.e.* for a *spin configuration* $\sigma$ in $\{-1,+1\}^{\Lambda}$, its energy is given by $$\mathcal{H}^\Lambda_{\beta,h}(w)=  - \beta\!\!\! \sum_{\substack{ i,j \in \Lambda \\ \{i,j\} \in E_{\mathbb{Z}^d}}} \!\!\! \sigma_i\sigma_j\,\,\,-h \sum_{i \in \Lambda} \sigma_i,$$ where $E_{\mathbb{Z}^d}$ is the set of edges of the lattice $\mathbb{Z}^d$ and $h$ and $\beta$ are two real parameters with $\beta > 0$. The probability $\mu_{\beta,h,\Lambda}[\sigma]$ of taking a configuration $\sigma$ is then proportional to $\exp(- \mathcal{H}^\Lambda_{\beta,h}(\sigma))$.

We now want to make $\Lambda$ grow to the whole lattice $\mathbb{Z}^d$. It is well known that for $h \ne 0$ or $\beta$ smaller than a critical value $\beta_c(d)$ (thus, at high temperature), there is a unique limiting probability measure $\mu_{\beta,h}$ on spin configurations on $\mathbb{Z}^d$, see *e.g.* [@Velenik Theorem 3.41]. In the following, we take parameters $(\beta,h)$ in this domain of uniqueness and consider a random spin configuration $\sigma$, whose law is $\mu_{\beta,h}$.

In [@Duneau2], Duneau, Iagolnitzer and Souillard proved what they call the *strong cluster properties* for spins in the Ising model for $h \ne 0$ or sufficiently small $\beta$. Their result is actually more general (it holds for other models than the Ising model) but for simplicity, we stick to the Ising model here. Reformulated with the terminology of the present article, we have:

::: theorem
Fix the dimension $d\geq 1$ and $h \ne 0,\,\beta>0$.

1.  There exist $C=C(d,\beta,h)$ and $\varepsilon=\varepsilon(d,\beta,h)<1$ such that under the probability measure $\mu_{\beta,h}$, the family $\{\sigma_i,\, i \in \mathbb{Z}^d\}$ has a $C$-uniform weighted dependency graph $G$, where the weight of the edge $\{i,j\}$ in $G$ is $\varepsilon^{\|i-j\|_1}$.

2.  The same holds for $h=0$ and $\beta$ is sufficiently small (*i.e.* $\beta<\beta_1(d)$, for some $\beta_1(d)$ depending on the dimension; this is sometimes refered to as the very high temperature regime).

[]{#thm:Cumu_Ising label="thm:Cumu_Ising"}
:::

Note that the maximal weighted degree of this graph is a constant $C' < \infty$.

We now consider the magnetization in a finite box $\Delta$ defined as $M_{\Delta}= \sum_{i \in \Delta} \sigma_i$. We see $M_\Delta$ as a sequence of random variables (indexed by the countably many finite subsets of $\mathbb{Z}^d$). Restricting the uniform weighted dependency graph above to $\{\sigma_i,\, i \in \Delta\}$, each $M_\Delta$ is the sum of random variables with a $C$-uniform weighted dependency graph and maximal weighted degree at most $C'$. Therefore, using Proposition [\[Prop:BoundCumulantUWDG\]](#Prop:BoundCumulantUWDG){reference-type="ref" reference="Prop:BoundCumulantUWDG"}, we know that $M_{|\Delta|}$ admits uniform bounds on cumulants with parameters $(\tfrac{C'}{2},|\Delta|,C)$. Moreover, since all spins are positively correlated by the FKG inequality (see [@Velenik Section 3.6]), we have, using translation invariance $$\mathop{\mathrm{Var}}(M_\Delta) \ge \sum_{i \in \Delta} \mathop{\mathrm{Var}}(\sigma_i) = \mathop{\mathrm{Var}}(\sigma_0) |\Delta|.$$ Note that $\mathop{\mathrm{Var}}(\sigma_0)$ is independent of $\Delta$. With the notation of Section [\[sec:dependency\]](#sec:dependency){reference-type="ref" reference="sec:dependency"}, this inequality ensures that $\widetilde{\sigma}_\Delta$ is bounded from below by a constant. Applying Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"}, we get:

::: proposition
Fix the dimension $d \geq 1$ and parameters $h \ne 0,\,\beta>0$. The exists a constant $K=K(d,\beta,h)$ such that, for all subsets $\Delta$ of $\mathbb{Z}^d$, we have under $\mu_{\beta,h}$ $$d_\mathrm{Kol}\left( \frac{M_\Delta-\mathbb{E}[M_\Delta]}{\sqrt{\mathop{\mathrm{Var}}(M_\Delta)}}\,,\, \mathcal{N}_{\mathbb{R}}(0,1)\right) \le \frac{K}{\sqrt{|\Delta|}}.$$ The same holds for $h=0$ and $\beta$ sufficiently small (very high temperature). []{#prop:Kol_Ising label="prop:Kol_Ising"}
:::

::: remark
In this remark, we discuss mod-Gaussian convergence in this setting. Consider a sequence $\Delta_n$ of subsets of $\mathbb{Z}^d$, tending to $\mathbb{Z}^d$ in the Van Hove sense (*i.e.* the sequence is increasing with union $\mathbb{Z}^d$, and the size of the boundary of $\Delta_n$ is asymptotic negligible, compared to the size of $\Delta_n$ itself). Then it is known from [@Ellis Lemma 5.7.1] that $$\lim_{n \to \infty} \tfrac{1}{|\Delta|} \mathop{\mathrm{Var}}(M_\Delta) = \sum_{k \in \mathbb{Z}^d} \mathop{\mathrm{Cov}}(\sigma_0,\sigma_k),$$ and the right-hand side has a finite value $\widetilde{\sigma}^2(\beta,h)$ for parameters $(\beta,h)$ for which Theorem [\[thm:Cumu_Ising\]](#thm:Cumu_Ising){reference-type="ref" reference="thm:Cumu_Ising"} applies. Similarly, we have $$\lim_{n \to \infty} \tfrac{1}{|\Delta|} \,\kappa^{(3)}(M_\Delta) = \sum_{k,l \in \mathbb{Z}^d} \kappa(\sigma_0,\sigma_k,\sigma_l) < \infty.$$ We call $\rho(\beta,h)$ this quantity, and denote $L=\tfrac{\rho(\beta,h)}{\widetilde{\sigma}^3(\beta,h)}$. Let us then consider the rescaled variables $$X_n=\frac{M_{\Delta_n}-\mathbb{E}[M_{\Delta_n}]}{(\mathop{\mathrm{Var}}(M_{\Delta_n}))^{1/3}}.$$ From [@FMN16 Section 5] (with $\alpha_n=\mathop{\mathrm{Var}}(M_\Delta)$ and $\beta_n=1$), we know that $X_n$ converges in the complex mod-Gaussian sense with parameters $t_n=(\mathop{\mathrm{Var}}(M_{\Delta_n}))^{1/3}$ and limiting function $\psi(z)=\exp(\frac{L z^3}{6})$. This mod-Gaussian convergence takes place on the whole complex plane. Using the results of [@FMN16], this implies a normality zone for $(M_\Delta-\mathbb{E}[M_\Delta])/\sqrt{\mathrm{Var}(M_\Delta)}$ of size $o(|\Delta|^{1/6})$, see Proposition 4.4.1 in *loc. cit.*; and moderate deviation estimates at the edge of this normality zone, see Proposition 5.2.1.
:::

::: remark
For $h=0$ and $\beta>\beta_c(d)$ (low temperature regime), there is no weighted dependency graph as above. Indeed, this would imply the analycity of the partition function in terms of the magnetic field $h$, and the latter is known not to be analytic at $h=0$ for $\beta>\beta_c(d)$; see [@MM91 Chapter 6, §5] for details.
:::
