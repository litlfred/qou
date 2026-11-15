---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-005-21-the-notion-of-zone-of-control
section_title: "The notion of zone of control"
section_number: 2.1
pages: 7-8
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.954
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
[]{#sec:zone label="sec:zone"}

::: definition
[]{#def:zone label="def:zone"} Let $(X_n)_{n \in \mathbb{N}}$ be a sequence of real random variables, $\phi_{c,\alpha,\beta}$ a reference stable law, and $(t_n)_{n \in \mathbb{N}}$ a sequence growing to infinity. Consider the following assertions:

1.  []{#hyp:firstcondition label="hyp:firstcondition"} Fix $v > 0$, $w > 0$ and $\gamma \in \mathbb{R}$. There exists a zone $[-K(t_n)^\gamma,K(t_n)^\gamma]$ such that, for all $\xi$ in this zone, if $\theta_n(\xi) = \mathbb{E}[\E^{\I \xi X_n}]\,\E^{-t_n \eta_{c,\alpha,\beta}(\I\xi)}$, then $$|\theta_n(\xi)-1| \leq K_1|\xi|^v\,\exp(K_2|\xi|^w)$$ for some positive constants $K_1$ and $K_2$ that are independent of $n$.

2.  []{#hyp:secondcondition label="hyp:secondcondition"} One has $$\alpha \leq w \quad;\quad -\frac{1}{\alpha}\leq  \gamma \leq \frac{1}{w-\alpha}\quad;\quad 0<K \leq \left(\frac{c^\alpha}{2K_2}\right)^{\frac{1}{w-\alpha}}.$$

Notice that [\[hyp:secondcondition\]](#hyp:secondcondition){reference-type="ref" reference="hyp:secondcondition"} can always be forced by increasing $w$, and then decreasing $K$ and $\gamma$ in the bounds of Condition [\[hyp:firstcondition\]](#hyp:firstcondition){reference-type="ref" reference="hyp:firstcondition"}. If Conditions [\[hyp:firstcondition\]](#hyp:firstcondition){reference-type="ref" reference="hyp:firstcondition"} and [\[hyp:secondcondition\]](#hyp:secondcondition){reference-type="ref" reference="hyp:secondcondition"} are satisfied, then we say that we have a *zone of control* $[-K(t_n)^\gamma,K(t_n)^\gamma]$ with *index* $(v,w)$.
:::

Note that although the definition of zone of control depends on the reference law $\phi_{c,\alpha,\beta}$, the latter does not appear in the terminology (throughout the paper, it is considered fixed).

::: proposition
[]{#prop:zone_CLT label="prop:zone_CLT"} Let $(X_n)_{n \in \mathbb{N}}$ be a sequence of random variables, $\phi_{c,\alpha,\beta}$ a reference stable law, $Y$ with distribution $\phi_{c,\alpha,\beta}$ and $Y_n$ as in Proposition [\[prop:clt\]](#prop:clt){reference-type="ref" reference="prop:clt"}. Assume that $(X_n)_{n \in \mathbb{N}}$ has a zone of control $[-K(t_n)^\gamma,K(t_n)^\gamma]$ with index $(v,w)$. If $\gamma>-\frac{1}{\alpha}$, then one has the convergence in law $Y_n \rightharpoonup Y$.
:::

::: proof
*Proof.* Condition [\[hyp:firstcondition\]](#hyp:firstcondition){reference-type="ref" reference="hyp:firstcondition"} implies that, if $Y_n$ is the renormalization of $X_n$ and $Y \sim \phi_{c,\alpha,\beta}$, then for fixed $\xi$, $$\begin{aligned}
\left|\frac{\mathbb{E}[\E^{\I \xi Y_n}]}{\mathbb{E}[\E^{\I \xi Y}]}-1\right| &= \left|\theta_n\!\left(\frac{\xi}{(t_n)^{1/\alpha}}\right)-1\right| \leq  \frac{K_1|\xi|^v}{(t_n)^{v/\alpha}}\,\exp\left(\frac{K_2|\xi|^w}{(t_n)^{w/\alpha}}\right)
\end{aligned}$$ for $t_n$ large enough, and the right-hand side goes to $0$. This proves the convergence in law $Y_n \rightharpoonup Y$.0◻ ◻
:::

The goal of the next few sections will be to get some speed of convergence estimates for this convergence in distribution.

::: remark
In the definition of zone of control, we do not assume the mod-$\phi_{c,\alpha,\beta}$ convergence of the sequence $(X_{n})_{n \in \mathbb{N}}$ with parameters $(t_n)_{n \in \mathbb{N}}$ and limit $\lim_{n \to \infty} \theta_n(\xi) = \theta(\xi)$. However, in almost all the examples considered, we shall indeed have (complex) mod-$\phi$ convergence (convergence of the residues $\theta_n$), with the same parameters $t_n$ as for the notion of zone of control. We shall then speak of *mod-$\phi$ convergence with a zone of convergence $[-K(t_n)^\gamma,K(t_n)^\gamma]$ and with index of control $(v,w)$*. Mod-$\phi$ convergence implies other probabilistic results than estimates of Berry--Esseen type: central limit theorem with a large range of normality, moderate deviations (*cf.* [@FMN16]), local limit theorem ([@DKN11]), *etc.*
:::

::: remark
If one has mod-$\phi_{c,\alpha,\beta}$ convergence of $(X_n)_{n \in \mathbb{N}}$, then there is at least a zone of convergence $[-K,K]$ of index $(v,w)=(0,0)$, with $\gamma=0$; indeed, the residues $\theta_n(\xi)$ stay locally bounded under this hypothesis. Thus, Definition [\[def:zone\]](#def:zone){reference-type="ref" reference="def:zone"} is an extension of this statement. However, we allow in the definition the exponent $\gamma$ to be negative (but not smaller than $-\frac{1}{\alpha}$). Indeed, in the computation of Berry--Esseen type bounds, we shall sometimes need to work with smaller zones than the one given by mod-$\phi$ convergence, see the hypotheses of Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}, and Sections [\[subsec:compoundpoisson\]](#subsec:compoundpoisson){reference-type="ref" reference="subsec:compoundpoisson"} and [\[subsec:ornstein\]](#subsec:ornstein){reference-type="ref" reference="subsec:ornstein"} for examples.
:::

::: remark
In our definition of zone of control, we ask for a bound on $|\theta_n(\xi)-1|$ that holds for any $n \in \mathbb{N}$. Of course, if the bound is only valid for $n \geq n_0$ large enough, then the corresponding bound on the Kolmogorov distance (Theorem [\[thm:kolmogorov\]](#thm:kolmogorov){reference-type="ref" reference="thm:kolmogorov"}) will only hold for $n \geq n_0$.
:::
