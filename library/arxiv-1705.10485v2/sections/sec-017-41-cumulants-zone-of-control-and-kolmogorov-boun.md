---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-017-41-cumulants-zone-of-control-and-kolmogorov-boun
section_title: "Cumulants, zone of control and Kolmogorov bound"
section_number: 4.1
pages: 28-31
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.979
latex_coverage_ratio: 0.964
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
In this section, we will see that appropriate bounds on the cumulants of a sequence of random variables $(S_n)_{n \in \mathbb{N}}$ imply the existence of a large zone of control for a renormalized version of $S_n$. In this whole section and in the next one, the reference stable law is the *standard Gaussian law.* We also assume that the random variables $S_n$ are centered.

Let us first recall the definition of cumulants. If $X$ is a real-valued random variable with exponential generating function $$\mathbb{E}[\E^{zX}] = \sum_{r=0}^\infty \frac{\mathbb{E}[X^r]}{r!}\,z^r$$ convergent in a neighborhood of $0$, then its *cumulants* $\kappa^{(1)}(X),\kappa^{(2)}(X),\ldots$ are the coefficients of the series $$\log \mathbb{E}[\E^{zX}] = \sum_{r=1}^\infty \frac{\kappa^{(r)}(X)}{r!}\,z^r,$$ which is also well defined for $z$ in a neighborhood of $0$ (see for instance [@LS59]). For example, $\kappa^{(1)}(X)=\mathbb{E}[X]$, $\kappa^{(2)}(X)=\mathbb{E}[X^2]-\mathbb{E}[X]^2=\mathrm{Var}(X)$, and $$\kappa^{(3)}(X)=\mathbb{E}[X^3]-3\,\mathbb{E}[X^2]\,\mathbb{E}[X] + 2\,\mathbb{E}[X]^3 .$$ We are interested in the case where cumulants can be bounded in an appropriate way.

::: definition
[]{#def:virtual label="def:virtual"} Let $(S_n)_{n \in \mathbb{N}}$ be a sequence of (centered) real-valued random variables. We say that $(S_n)_{n \in \mathbb{N}}$ admits *uniform bounds on cumulants* with parameters $(D_n,N_n,A)$ if, for any $r\geq 2$, we have $$|\kappa^{(r)}(S_n)| \leq N_n\,r^{r-2}\,(2D_n)^{r-1}\,A^r.$$
:::

In the following, it will be convenient to set $(\widetilde{\sigma}_n)^2 = \frac{\mathrm{Var}(S_n)}{N_n D_n}$. The inequality of Definition [\[def:virtual\]](#def:virtual){reference-type="ref" reference="def:virtual"} with $r = 2$ gives $(\widetilde{\sigma}_n)^2 \leq 2A^2$.

::: lemma
Let $(S_n)_{n \in \mathbb{N}}$ be a sequence with uniform bounds on cumulants with parameters $(D_n,N_n,A)$. Set $$X_n = \frac{S_n}{( N_n)^{1/3}\,(D_n)^{2/3}} 
  \ \text{ and }\ t_n=(\widetilde{\sigma}_n)^2 (\tfrac{N_n}{D_n})^{1/3}=\mathrm{Var}(X_n).$$ Then, we have for $(X_n)_{n \in \mathbb{N}}$ a zone of control $[-K\,t_n\,,\,K\,t_n]$ of index $(3,3)$, with the following constants: $$K=\frac{1}{(8+4\E)\,A^3}, \qquad K_1 = K_2 = (2+\E)\,A^3.$$ []{#lem:Cumulants_Zone label="lem:Cumulants_Zone"}
:::

::: proof
*Proof.* From the definition of cumulants, since $X_n$ is centered and has variance $t_n$, we can write $$\begin{aligned}
 \theta_n(\xi)&=\mathbb{E}[\E^{\I \xi X_n}] \,\exp\left(\frac{t_n\,\xi^2}{2}\right) \\
 &= \exp\left(\sum_{r= 3}^\infty \frac{\kappa^{(r)}(S_n)}{r!}\,\frac{(\I\xi)^r}{(N_n(D_n)^2)^{r/3}}\right) = \exp(z),
 
\end{aligned}$$ with $$|z| \leq \frac{1}{2} \frac{N_n}{D_n}\,\sum_{r=3}^\infty \frac{r^{r-2}}{\E^r\,r!} \,\left(\left(\frac{D_n}{N_n}\right)^{\!1/3}\,2\E A\, |\xi|\right)^{\!r}.$$ We set $y=(\frac{D_n}{N_n})^{1/3}\,2\E A\, |\xi|$ and suppose that $y \leq 1$, that is to say that $\xi \in [-L\,(\frac{N_n}{D_n})^{1/3}\,,\,L\,(\frac{N_n}{D_n})^{1/3}]$ with $L=\frac{1}{2\E A}$.

By Stirling's bound, the series $S(y)=\sum_{r=3}^\infty \frac{r^{r-2}}{r!\,\E^r}\,y^r$ is convergent for any $y \in [0,1]$, and we have the inequality $S(y) \le \frac{y^3}{2\E^3\,(1-y)}$, which implies $$|z| \leq 2\,\frac{(A\,|\xi|)^3}{1-\left(\frac{D_n}{N_n}\right)^{\!1/3}\,2\E A\, |\xi|}.$$ We now consider the zone of control $[-Kt_n,Kt_n]$ with $K = \frac{1}{(4\E+8) A^3}$. If $\xi$ is in this zone, then we have indeed $$|\xi| \leq \frac{(\widetilde{\sigma}_n)^2}{4\E A^3} \left(\frac{N_n}{D_n}\right)^{\!1/3} \leq \frac{1}{2\E A}\,\left(\frac{N_n}{D_n}\right)^{\!1/3} = L\left(\frac{N_n}{D_n}\right)^{\!1/3}$$ by using the remark just before the lemma. Then, $$|z| \leq \frac{2A^3}{1-\frac{2\E A\,(\widetilde{\sigma}_n)^2}{(4\E+8)A^3}}\,|\xi|^3\leq \frac{2A^3}{1-\frac{\E}{\E+2}}\,|\xi|^3  =(2+\E)A^3\,|\xi|^3.$$ Thus, on the zone of control, $|\theta_n(\xi)-1| = |\E^{z}-1| \leq |z|\,\E^{|z|}$, whence a control of index $(3,3)$ and with constants $$K_1 = K_2 = (2+\E)A^3.$$ We have chosen $K$ so that $K=\frac{1}{4K_2}$, hence, the inequalities of Condition [\[hyp:secondcondition\]](#hyp:secondcondition){reference-type="ref" reference="hyp:secondcondition"} are satisfied.0◻ ◻
:::

Using the results of Section [\[sec:testfunctions\]](#sec:testfunctions){reference-type="ref" reference="sec:testfunctions"}, we obtain:

::: corollary
[]{#cor:Cumulants_Kol label="cor:Cumulants_Kol"} Let $S_n$ be a sequence with a uniform bounds on cumulants with parameters $(D_n,N_n,A)$ and let $Y_n=\tfrac{S_n}{\sqrt{\mathrm{Var}(S_n)}}$. Then we have $$d_\mathrm{Kol}(Y_n\,,\,\mathcal{N}_{\mathbb{R}}(0,1)) \leq \frac{76.36\,A^3}{(\widetilde{\sigma}_n)^3}\,\sqrt{\frac{D_n}{N_n}}.$$
:::

::: proof
*Proof.* We can apply Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}, choosing $\gamma=1$, and $\lambda=0.193$. It yields a constant smaller than $77.911$. It is however possible to get the better constant given above by redoing some of the computations in this specific setting. With $\rho>4$, set $K=\frac{1}{(4\E+\rho)\,A^3}$, and $\varepsilon_n = \frac{1}{K\,(t_n)^{3/2}}$. On the zone $\xi \in [-\frac{1}{\varepsilon_n},\frac{1}{\varepsilon_n}]$, we have a bound $|\theta_n(\xi)-1|\leq M|\xi|^3\exp(M|\xi|^3)$, this time with $M = (2 + \frac{8\E}{\rho})A^3$. Hence, $$\begin{aligned}
|\mathbb{E}[f_{a,\varepsilon_n}(Y_n)] - \mathbb{E}[f_{a,\varepsilon_n}(Y)]| &\leq \frac{M}{2\pi\,(t_n)^{3/2}}\int_{-\frac{1}{\varepsilon_n}}^{\frac{1}{\varepsilon_n}}  |\xi|^{2}\,\E^{-\frac{\xi^2}{2}+ M \frac{|\xi|^3}{(t_n)^{3/2}}}\,d\hspace*{-0.3mm}{\xi} \\
&\leq \frac{M}{2\pi\,(t_n)^{3/2}}\int_{\frac{1}{\varepsilon_n}}^{\frac{1}{\varepsilon_n}}  |\xi|^{2}\,\E^{-\xi^2\left(\frac{1}{2}-\frac{2}{\rho}\right)}\,d\hspace*{-0.3mm}{\xi} 
\\ 
&\leq \frac{M}{\sqrt{2\pi}\,(t_n)^{3/2}\,(1-\frac{4}{\rho})^{3/2}}  =\frac{1}{\sqrt{2\pi}}\,\frac{2}{\rho(1-\frac{4}{\rho})^{3/2}}\,\varepsilon_n.
\end{aligned}$$ By Theorem [\[theorem:tao\]](#theorem:tao){reference-type="ref" reference="theorem:tao"}, we get for any $\lambda > 0$: $$\begin{aligned}
&d_\mathrm{Kol}\left(\frac{S_n}{\sqrt{\mathrm{Var}(S_n)}}\,,\,\mathcal{N}_{\mathbb{R}}(0,1)\right) \\
&\leq \frac{(1+\lambda)}{\sqrt{2\pi}}\,\left(\frac{2}{\rho(1-\frac{4}{\rho})^{3/2}}+\frac{1}{\sqrt[3]{\pi}}\left(4\sqrt[3]{1+\frac{1}{\lambda}}+3\sqrt[3]{3}\right)\right)\,\varepsilon_n.
\end{aligned}$$ The best constant is then obtained with $\rho=6.79$ and $\lambda=0.185$.0◻ ◻
:::

::: remark
There is a trade-off in the bound of Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"} between the *a priori* upper bound on $(\widetilde{\sigma}_n)^2$, and the constant $C$ that one obtains such that the Kolmogorov distance is smaller than $$\frac{CA^3}{(\widetilde{\sigma}_n)^3}\,\sqrt{\frac{D_n}{N_n}}.$$ This bound gets worse when $(\widetilde{\sigma}_n)^2$ is small, but on the other hand, the knowledge of a better *a priori* upper bound (that is precisely when $(\widetilde{\sigma}_n)^2$ is small) yields a better constant $C$. So, for instance, if one knowns that $(\widetilde{\sigma}_n)^2\leq A^2$ (instead of $2A^2$), then one gets a constant $C=52.52$. A general bound that one can state and that takes into account this trade-off is: $$d_\mathrm{Kol}(Y_n\,,\,\mathcal{N}_{\mathbb{R}}(0,1)) \leq 27.55 \left(\left(\frac{A}{\widetilde{\sigma}_n}\right)^3 + \frac{A}{\widetilde{\sigma}_n}\right)\,\sqrt{\frac{D_n}{N_n}}.$$ We are indebted to Martina Dal Borgo for having pointed out this phenomenon. In the sequel, we shall freely use this small improvement of Corollary [\[cor:Cumulants_Kol\]](#cor:Cumulants_Kol){reference-type="ref" reference="cor:Cumulants_Kol"}.
:::

The above corollary ensures asymptotic normality with a bound on the speed of convergence when $$\left(\frac{1}{(\widetilde{\sigma}_n)^3}\,\sqrt{\tfrac{D_n}{N_n}} \to 0 \right) \iff \left( (\widetilde{\sigma}_n)^2\,\left(\frac{N_n}{D_n}\right)^{\!1/3} \to +\infty \right).$$ Using a theorem of Janson, the asymptotic normality can be obtained under a less restrictive hypothesis, but without bound on the speed of convergence. Even if the main topic of the paper is to find bounds on the speed of convergence, we will recall the result here for the sake of completeness.

::: proposition
As above, let $S_n$ be a sequence with a uniform bounds on cumulants with parameters $(D_n,N_n,A)$ and assume that $$\lim_{n \to \infty}\, \frac{\mathrm{Var}(S_n)}{N_n\, D_n}\,\left(\frac{N_n}{D_n}\right)^{\!\varepsilon} = \lim_{n \to \infty}(\widetilde{\sigma}_n)^2\,\left(\frac{N_n}{D_n}\right)^{\!\varepsilon}= +\infty$$ for some parameter $\varepsilon\in (0,1)$. Then, $$\frac{S_n}{\sqrt{\mathrm{Var}(S_n)}} \rightharpoonup \mathcal{N}_{\mathbb{R}}(0,1).$$ []{#thm:CLT_Janson label="thm:CLT_Janson"}
:::

::: proof
*Proof.* Note that the bounds on cumulants can be rewritten as $$\begin{aligned}
|\kappa^{(r)}(Y_n)| &\leq C_r\left(\frac{\mathrm{Var}(S_n)}{N_n\,D_n}\,\left(\frac{N_n}{D_n}\right)^{1-\frac{2}{r}}\right)^{\!\!-\frac{r}{2}}
\end{aligned}$$ for some constant $C_r$. Choosing $r$ large enough so that $1-\frac{2}{r} \geq \varepsilon$, we conclude that $\kappa^{(r)}(Y_n) \to 0$ for $r$ large enough. This is a sufficient condition for the convergence in law towards a Gaussian distribution, see [@Jan88 Theorem 1] and [@Gri92].0◻ ◻
:::

::: remark
Up to a change of parameters, it would be equivalent to consider bounds of the kind $$|\kappa^{(r)}(S_n)| \leq (Cr)^r \alpha_n (\beta_n)^r,\,\,
  \text{ or } \left|\kappa^{(r)}\!\left(\tfrac{S_n}{\sqrt{\mathop{\mathrm{Var}}(S_n)}}\right) \right| \le \frac{r!}{\Delta_n^{r-2}},$$ as done by Saulis and Statulevičius in [@LivreOrange:Cumulants] or by the authors of this paper in [@FMN16]. In particular, it was proved in [@FMN16 Chapter 5], that under slight additional assumptions on the second and third cumulants, we have the following: the sequence $(X_n)_{n \in \mathbb{N}}$ defined in Lemma [\[lem:Cumulants_Zone\]](#lem:Cumulants_Zone){reference-type="ref" reference="lem:Cumulants_Zone"} converges in the mod-Gaussian sense with parameters $(t_n)_{n \in \mathbb{N}}$.
:::
