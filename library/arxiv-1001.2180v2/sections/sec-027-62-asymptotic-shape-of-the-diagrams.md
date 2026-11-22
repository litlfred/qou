---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-027-62-asymptotic-shape-of-the-diagrams
section_title: "Asymptotic shape of the diagrams"
section_number: 6.2
pages: 24-26
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.954
latex_coverage_ratio: 0.978
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
In the previous paragraph, we introduced some measures on Young diagrams of size $n$. Here we are interested in the asymptotic shape of typical diagrams when $n$ tends to infinity. That means, as the measure we introduced also depends on an other parameter $N$, that we have to choose a value of $N$ for each $n$. The case where the parameter $N$ is equivalent of an expression of the kind $1/c \cdot n^\alpha$ with $\alpha \geq 1/2$ has already been solved by P. Biane [@Bia01 paragraph 3.1]. So we will look at the case $\alpha < 1/2$.

Using the formula for expectation of normalized character values of the previous paragraph, one has: $$\label{eq:equiv_Esigma}
\mathbb{E}[\varSigma_\rho] = n^{\downarrow |\rho|} \cdot N^{\ell(\rho)-|\rho|} \sim c^{|\rho| - \ell(\rho)} n^{|\rho| + \alpha \ell(\rho) -\alpha |\rho|}.$$ As in section [\[sect:first_order\]](#sect:first_order){reference-type="ref" reference="sect:first_order"}, the first step is to show that the power sums have the same asymptotic behavior. Lemma [\[lem:major_Ex_deg\]](#lem:major_Ex_deg){reference-type="ref" reference="lem:major_Ex_deg"} is true in this context, but not strong enough to obtain such a result. Unfortunately, with the gradation we give in section [\[sect:observables\]](#sect:observables){reference-type="ref" reference="sect:observables"}, it is not possible to have a stronger upper bound. Thus one has to introduce another gradation on $\mathscr{O}$.

### Gradations on $\mathscr{O}$

Let us define (this may not be an integer, but it does not matter): $$\deg_\alpha(p_\rho) = |\rho| + \alpha \ell(\rho) -\alpha |\rho|.$$ As in the case $\alpha=0$, the expression of $\varSigma_k$ in terms of power sums (Proposition [\[prop:sigma_pk\]](#prop:sigma_pk){reference-type="ref" reference="prop:sigma_pk"}) gives us the degree and the top homogeneous component of $\varSigma_\rho$.

::: lemma
[]{#lem:prho_encore_dominant label="lem:prho_encore_dominant"} For any $\rho \in \mathscr{Y}$, one has: $$\varSigma_\rho = p_\rho + \text{terms of lower degree}.$$
:::

::: proof
*Proof.* It is enough to prove this for $\rho=(k)$. Note that the $\alpha$-degree can be written as: $$\deg_\alpha(p_\lambda)= (1 - 2 \alpha) |\lambda| + \alpha (|\lambda| + \ell(\lambda)).$$

1.  The first term is a positive multiple (recall that $\alpha<1/2$) of the usual gradation, so if $p_\lambda$ appears with a non-zero coefficient in $\varSigma_k$, one has $|\lambda| \leq k$, with equality if and only if $\lambda=(k)$.

2.  The second term is a non-negative multiple of $2 \deg_{1/2}(\lambda)=|\lambda| + \ell(\lambda)$. An easy consequence of Proposition [\[prop:sigma_pk\]](#prop:sigma_pk){reference-type="ref" reference="prop:sigma_pk"} is that all $p_\lambda$ appearing in $\varSigma_k$ fulfill the condition $|\lambda| + \ell(\lambda) \leq k+1$. Note that we do not have the same necessary condition of equality as before: in fact, $\deg_{1/2}$ is a classical gradation of $\mathscr{O}$ (see [@IO02]), for which the top homogeneous component of $\varSigma_\rho$ *is not* $p_\rho$.

Finally, $\varSigma_\rho$ has degree $|\rho| + \alpha \ell(\rho) -\alpha |\rho|$, and its top homogeneous component for the new gradation is $p_\rho$. ◻
:::

### Convergence of rescaled power sums and concentration of characters

Using equation ([\[eq:equiv_Esigma\]](#eq:equiv_Esigma){reference-type="ref" reference="eq:equiv_Esigma"}), one has the following analog of Lemma [\[lem:major_Ex_deg\]](#lem:major_Ex_deg){reference-type="ref" reference="lem:major_Ex_deg"} (the gradation has been chosen for this purpose):

::: lemma
[]{#lem:Ex_encore_majore label="lem:Ex_encore_majore"} For any $x \in \mathscr{O}$, one has: $\mathbb{E}[x] = O(n^{\deg_\alpha(x)})$.
:::

Now, we have all the tools to prove the convergence of rescaled powers sums:

::: proposition
[]{#prop:cv_powersums_encore label="prop:cv_powersums_encore"} Let $(N_n)_{n \geq 1}$ be a sequence of positive integers such that $N_n \sim c \cdot n^\alpha$ for some $\alpha <1/2$. Under the measure associated with the action of the symmetric groups on the spaces $(\mathbb{C}^{N_n})^{\otimes n}$, one has the following convergence in probability: $$\frac{p_k}{n^{k + \alpha - \alpha k}} \rightarrow c^{k-1}.$$
:::

::: proof
*Proof.* Equation ([\[eq:equiv_Esigma\]](#eq:equiv_Esigma){reference-type="ref" reference="eq:equiv_Esigma"}), Lemma [\[lem:prho_encore_dominant\]](#lem:prho_encore_dominant){reference-type="ref" reference="lem:prho_encore_dominant"} and Lemma [\[lem:Ex_encore_majore\]](#lem:Ex_encore_majore){reference-type="ref" reference="lem:Ex_encore_majore"} imply that: $$\mathbb{E}[p_\rho] \sim c^{\rho - \ell(\rho)} n^{|\rho| + \alpha \ell(\rho) -\alpha |\rho|}.$$ The result follows thanks to Bienaymé-Chebyshev inequality as in the case $\alpha=0$. ◻
:::

::: corollary
Under the same assumptions, in probability, $$\frac{\varSigma_\rho}{n^{|\rho| + \alpha \ell(\rho) -\alpha |\rho|}} \rightarrow c^{|\rho|-\ell(\rho)}.$$
:::

### Consequences on the shape of diagrams

To deduce some results on the shape of diagrams from the convergence of the quantities $p_k/(n^{k + \alpha - \alpha k})$, one has to interpret them as the moments of some measure-valued random variables. Therefore we define for a Young diagram $\lambda$ the measure: $$X_{\lambda,\alpha}=\sum_{i=1}^d (a_i^*(\lambda)/n^{1-\alpha}) \, \frac{\delta_{(a_i^*(\lambda)/n^{1-\alpha})}}{n^\alpha} + (b_i^*(\lambda)/n^{1-\alpha}) \, \frac{\delta_{(-b_i^*(\lambda)/n^{1-\alpha})}}{n^\alpha}.$$ With this definition, Proposition [\[prop:cv_powersums_encore\]](#prop:cv_powersums_encore){reference-type="ref" reference="prop:cv_powersums_encore"} can be read as the convergence in probability of the moments of this random-valued measure towards the sequence $(1,c,c^2,\ldots)$, which is obviously the sequence of the moments of the measure $\delta_c$ (the Dirac mass at $c$). Since the probability measure $\delta_{c}$ is characterized by its moments, this implies the convergence in law $X_{\lambda,\alpha} \to \delta_{c}$ in probability in the space of probability measures $\mathscr{M}(\mathbb{R})$.

Now, the negative part of $X_{\lambda,\alpha}$ is in fact negligible. Indeed, since $\ell(\lambda)\leq N$ with probability $1$, the total weight of $$\sum_{i=1}^{d} (b_{i}^{*}(\lambda)/n^{1-\alpha})\,\frac{\delta_{(-b_{i}^{*}(\lambda)/n^{1-\alpha})}}{n^{\alpha}}$$ is bounded from above and with probability $1$ by: $$\sum_{i=1}^{N}\frac{N}{n} = \frac{N^{2}}{n}\simeq c^{-2}\,n^{2\alpha-1}\to 0$$ As a consequence, one can replace $X_{\lambda,\alpha}$ by its positive part $\sum_{i=1}^{d}(a_{i}^{*}(\lambda)/n^{1-\alpha})\,\frac{\delta_{(a_{i}^{*}(\lambda)/n^{1-\alpha})}}{n^{\alpha}}$, and even by the simpler probability measure $$Y_{\lambda,\alpha}=\sum_{i=1}^{N} (\lambda_{i}/n^{1-\alpha})\,\frac{\delta_{\lambda_{i}/n^{1-\alpha}}}{n^{\alpha}}=\sum_{i=1}^{N} \frac{\lambda_{i}}{n}\delta_{\lambda_{i}/n^{1-\alpha}};$$ this random measure converges in probability towards $\delta_{c}$ in $\mathscr{M}(\mathbb{R})$.

We fix some positive real numbers $\theta$, $\eta$ and $\varepsilon$, and we consider a continuous function $f:\mathbb{R}\to [0;1]$ such that $f(x)=0$ outside the interval $[c(1-\eta/2),c(1+\eta/2)]$, and $f(c)=1$. Then, for $n$ big enough and with probability greater than $1-\varepsilon$, $$1-\theta=f(c)-\theta \leq \sum_{i=1}^{N} \frac{\lambda_{i}}{n}\,f\left(\frac{\lambda_{i}}{n^{1-\alpha}} \right) \leq f(c)+\theta=1+\theta$$ because of the convergence in law $Y_{\lambda,\alpha}\to \delta_{c}$. The sum involved in this estimate is bounded from above by $\sum_{\left\{i\,\,|\,\,\lambda_{i}/n^{1-\alpha} \in [c(1-\eta/2),c(1+\eta/2)]\right\}}\frac{\lambda_{i}}{n}$, and therefore by $$\frac{c(1+\eta/2)}{n^{\alpha}}\,\,\mathrm{card}\,\left\{i\,\,\bigg|\,\,\frac{\lambda_{i}}{n^{1-\alpha}} \in [c(1-\eta/2),c(1+\eta/2)]\right\}.$$ As a consequence, the number of rows $\lambda_{i}$ such that $c(1-\eta/2)\leq \lambda_{i}/n^{1-\eta} \leq c(1+\eta/2)$ is bigger than $$\frac{1-\theta}{c(1+\eta/2)} \,n^{\alpha}\geq \frac{(1-\theta)(1-\eta/2)}{c}\,n^{\alpha}\geq \frac{1-\eta}{c}\,n^{\alpha}$$ for $\theta$ small enough. As by the very definition of our measure, our random diagrams can not have columns of length bigger than $N$, the proof of Theorem [\[prop:SW_asymptotic_shape\]](#prop:SW_asymptotic_shape){reference-type="ref" reference="prop:SW_asymptotic_shape"} is over.

::: remark
The vector space $(\mathbb{C}^N)^{\otimes n}$ is also a representation of the unitary group $U_N$ and, using Schur-Weyl duality, its isotypic components under the action of $U_N$ are the same as under the action of $S_n$. As a consequence, the results of article [@CollinsSniady09] can be used to study the asymptotic shape of the diagram. It turns out that, in the case $\alpha <1/2$, this approach gives finer results than ours. Nevertheless, as they are two independent parameters, the space $(\mathbb{C}^N)^{\otimes n}$ remains a good example to show that our method works with any intermediate decay of character values between $O(1)$ and $O(\sqrt{n}^{-|\rho|+\ell(\rho)})$.
:::
