---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-020-43-link-with-the-representation-theory-of-the-in
section_title: "Link with the representation theory of the infinite symmetric group"
section_number: 4.3
pages: 16-17
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
toc_source: outline
text_source: latex
latex_prose_ratio: 0.984
latex_coverage_ratio: 1.0
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
This result on the first order asymptotics could alternatively have been obtained by using general results coming from the representation theory of the infinite symmetric group $\mathfrak{S}_{\infty}$, see in particular [@KV81; @Ker03; @KOV04]. However, it seems impossible to understand the fluctuations with this approach.

Recall that the Thoma simplex $$\Omega=\left\{\big((\alpha_i)_{i \geq 1},(\beta_i)_{i \geq 1}\big) \,\,\big|\,\, \alpha_1\geq \alpha_2\geq \cdots \geq 0,\,\, \beta_1\geq \beta_2\geq \cdots \geq 0,\,\, \gamma=1-\sum_{i=1}^\infty (\alpha_i+\beta_i) \geq 0\right\}$$ parametrizes the normalized irreducible characters of $\mathfrak{S}_{\infty}$ ([@Tho64]). Besides, to each point $\omega \in \Omega$, one can associate a system $(M^{\omega}_{n})_{n\in \mathbb{N}}$ of probability measures on the sets $\mathscr{Y}_{n}$ of Young diagrams: $$M^{\omega}_{n}(\lambda)=(\dim \lambda)\,s_{\lambda}(\omega),$$ where $s_{\lambda}(\omega)$ is the generalized Schur function defined by the following specialization of the algebra of symmetric functions: $$p_{1}(\omega)=1\ ;\qquad p_{k\geq 2}(\omega)=p_{k}(\alpha-(-\beta))=\sum_{i\geq 1}(\alpha_{i})^{k}+(-1)^{k-1}\sum_{i \geq 1}(\beta_{i})^{k}.$$ This system is called coherent because it fulfills the relation: $$\forall n,\,\,\,\forall \lambda \in \mathscr{Y}_{n},\,\,\,M^{\omega}_{n}(\lambda)=\sum_{\lambda \nearrow \Lambda} \frac{\dim \lambda}{\dim \Lambda}\,M^{\omega}_{n+1}(\Lambda).$$

Moreover, one can describe all coherent systems $(M^{m}_{n})_{n\in \mathbb{N}}$ of probability measures on the sets $\mathscr{Y}_{n}$: given a probability measure $m \in \mathscr{M}(\Omega)$, let us define: $$M^{m}_{n}(\lambda)=\int_{\Omega}M^{\omega}_{n}(\lambda)\,dm(\omega)=\int_{\Omega}(\dim\lambda)\,s_{\lambda}(\omega)\,dm(\omega).$$ This system is coherent and the correspondence is one-to-one. In other terms $\Omega$ is the Martin boundary of the Young graph ([@KOO97]). The set of probability measures $\mathscr{M}(\Omega)$ is also in correspondence with normalized (but non necessarily irreducible) characters of $\mathfrak{S}_{\infty}$.

A deep result due to Kerov and Vershik ensures that the Thoma simplex is also in some sense the "geometric boundary" of the Young graph. More precisely, let us restate here Theorem 9.7.3 of [@KOV04] (we refer also to [@KV81]). To each Young diagram $\lambda \in \mathscr{Y}_{n}$, we associate a point $\omega_{n}(\lambda)$ of the Thoma simplex by scaling its Frobenius coordinates: $$\omega_{n}(\lambda)=\left(\frac{a_{1}^{*}(\lambda)}{n},\ldots,\frac{a_{d}^{*}(\lambda)}{n},0,\ldots ;\frac{b_{1}^{*}(\lambda)}{n},\ldots,\frac{b_{d}^{*}(\lambda)}{n},0,\ldots\right).$$ We endow $\Omega$ with the compact topology of simple convergence of coordinates.

::: theorem
Let $m$ be a probability measure on $\Omega$; we denote by $(M^{m}_{n})_{n \in \mathbb{N}}$ the associated coherent system of measures. The push-forward $(\omega_{n})_{\star}M^{m}_{n}$ converges in law towards $m$ in $\mathscr{M}(\Omega)$.
:::

That said, the $q$-Plancherel measures $(M_{n,q})_{n \in \mathbb{N}}$ form the coherent system associated to the Dirac mass at the point $$\omega_{q}=\big((1-q),(1-q)q,(1-q)q^{2},\ldots;0,0,\ldots\big).$$ Indeed, for any partition $\lambda$, the generic degree $D_{\lambda}(q)$ can be written as $D_{\lambda}(q)=\{n!\}_{q}\,s_{\lambda}(\omega_{q})$, see [@Mac95 Chapter 1,§3, examples 1-5]. So, the scaled Frobenius coordinates under $q$-Plancherel measures should converge towards the vector $(1-q,(1-q)q,(1-q)q^{2},\ldots;0,0,\dots)$, which is exactly our Theorem [\[th:first_order_as_rows\]](#th:first_order_as_rows){reference-type="ref" reference="th:first_order_as_rows"} and Remark [\[RemColumns\]](#RemColumns){reference-type="ref" reference="RemColumns"}.
