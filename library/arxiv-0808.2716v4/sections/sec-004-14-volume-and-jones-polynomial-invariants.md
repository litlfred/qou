---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF FAREY MANIFOLDS"
section_id: sec-004-14-volume-and-jones-polynomial-invariants
section_title: "Volume and Jones polynomial invariants"
section_number: 1.4
pages: 5-6
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
toc_source: outline
text_source: latex
latex_prose_ratio: 0.943
latex_coverage_ratio: 0.984
doc_brief: "CUSP AREAS OF FAREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on the cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2–bridge link complements."
---
The volume estimate of Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} has a very interesting application to conjectures on the relationship of the volume to the Jones polynomial invariants of hyperbolic knots.

For a knot $K$, let $$J_K(t)= \alpha_K t^m+ \beta_K t^{m-1}+ \ldots + \beta'_K t^{r+1}+
\alpha'_K t^r$$

denote the Jones polynomial of $K$. We will always denote the second and next--to--last coefficients of $J_K(t)$ by $\beta_K$ and $\beta'_K$, respectively.

The Jones polynomial fits into an infinite family of knot invariants: the *colored Jones* polynomials. These are Laurent polynomial knot invariants $J^n_K(t)$, $n>1$, where $J^2_K(t)=J_K(t)$. The volume conjecture [@kashaev:volume-conj; @murakami-squared] states that for a hyperbolic knot $K$, $$2\pi \lim_{n\to \infty} { \frac{\log {\left\vert J^n_K(e^{2\pi i / n} )
 \right\vert}} {n}}= {\rm vol}(S^3 {\smallsetminus}K),$$

where $e^{2\pi i /n}$ is a primitive $n$-th root of unity. If the volume conjecture is true, then one expects correlations between ${\rm vol}(S^3 {\smallsetminus}K)$ and the coefficients of $J_K^n(t)$, at least for large values of $n$. For example, for $n\gg 0$ one would have $${\rm vol}(S^3 {\smallsetminus}K)\: < \: C || J_K^n ||,$$

where $|| J_K^n ||$ denotes the sum of absolute values of the coefficients of $J_K^n(t)$ and $C$ is a constant independent of $K$. At the same time, several recent results and much experimental evidence [@ckp:simplest-knots; @dasbach-lin:volumeish; @fkp-07; @fkp:conway] actually indicate that there may be a correlation between ${\rm vol}(S^3{\smallsetminus}K)$ and the coefficients of the Jones polynomial itself. These results prompt the following question.

::: question
[]{#question label="question"} Do there exist constants $C_i>0$, $i=1, \ldots, 4$, and a function $B_K$ of the coefficients of $J_K(t)$, such that all hyperbolic knots satisfy $$C_1\ B_K-C_2 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \: C_3\ B_K+C_4?
\label{eqn:question}$$
:::

Dasbach and Lin [@dasbach-lin:volumeish] showed that for alternating knots, equation ([\[eqn:question\]](#eqn:question){reference-type="ref" reference="eqn:question"}) holds for $B_K:={\left\vert \beta_K \right\vert}+{\left\vert \beta'_K \right\vert}$. They also presented experimental evidence suggesting linear correlations between ${\left\vert \beta_K \right\vert}+{\left\vert \beta'_K \right\vert}$ and the volume of non-alternating knots; their data is based on knots with a low numbers of crossings. The authors of the current paper have shown that the same function works for several large families in the class of *adequate knots*, which are a vast generalization of alternating knots [@fkp-07; @fkp:conway]. In fact, Dasbach and Lin [@dasbach-lin:head-tail] and Stoimenow [@stoimenow:amphichiral] showed that for adequate knots, the second and next--to--last coefficients of the colored Jones polynomial $J_K^n(t)$ are independent of $n$, equal to those of the Jones polynomial $J_K(t)$. So these results establish strong versions of relations between volume and coefficients of the colored Jones polynomials for these knots, as predicted by the volume conjecture. This led to some hope that not only would Question [\[question\]](#question){reference-type="ref" reference="question"} be answered in the affirmative, but also that $B_K = {\left\vert \beta_K \right\vert} +
{\left\vert \beta'_K \right\vert}$ could always work in equation ([\[eqn:question\]](#eqn:question){reference-type="ref" reference="eqn:question"}).

In this paper we show that a slightly modified function, involving the first two and the last two coefficients of the Jones polynomial, satisfies equation ([\[eqn:question\]](#eqn:question){reference-type="ref" reference="eqn:question"}) for hyperbolic closed 3-braids. Building on Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"}, we prove the following.

::: named
Theorem [\[thm:relations\]](#thm:relations){reference-type="ref" reference="thm:relations"} Let $K$ be a hyperbolic closed $3$--braid. From the Jones polynomial $J_K(t)$, we define ${\zeta_K}, {\zeta'_K}$ as follows. Let $$\zeta_K = \left\{ \begin{array}{r l}
\beta_K, & \mbox{if } {\left\vert \alpha_K \right\vert} = 1 \\
0, & \mbox{otherwise}
\end{array} \right.
\qquad \mbox{and} \qquad
\zeta'_K = \left\{ \begin{array}{r l}
\beta'_K, & \mbox{if } {\left\vert \alpha'_K \right\vert} = 1 \\
0, & \mbox{otherwise.}
\end{array} \right.$$ Define $\zeta = \max \left\{ {\left\vert \zeta_K \right\vert}, {\left\vert \zeta'_K \right\vert} \right\}$. Then $$4v_3 \cdot \zeta - 281 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \:
4v_8 \, ( \zeta +1 ).$$ Furthermore, the multiplicative constants in both the upper and lower bounds are sharp.
:::

We remark that the quantity $\zeta = \max \left\{ {\left\vert \zeta_K \right\vert}, {\left\vert \zeta'_K \right\vert}  \right\}$, as defined in Theorem [\[thm:relations\]](#thm:relations){reference-type="ref" reference="thm:relations"}, will also serve to estimate the volumes of alternating links, sums of alternating tangles, and highly twisted adequate links. In other words, this quantity estimates the volume of every family of knots and links where the volume is known to be bounded above and below in terms of the Jones polynomial. The quantity $\zeta$ depends only on the first two and last two coefficients of $J_K(t)$, and can be taken as positive evidence for Question [\[question\]](#question){reference-type="ref" reference="question"}. On the other hand, we also show that no function of $\beta_K$ and $\beta'_K$ alone can satisfy equation ([\[eqn:question\]](#eqn:question){reference-type="ref" reference="eqn:question"}) for all hyperbolic knots.

::: named
Theorem [\[thm:counterexample\]](#thm:counterexample){reference-type="ref" reference="thm:counterexample"} There does not exist a function $f(\cdot, \cdot)$ of two variables, together with constants $C_i>0$, $i=1, \ldots, 4$, such that $$C_1 f(\beta_K, \beta'_K) - C_2 \: < \: {\rm vol}(S^3{\smallsetminus}K) \:<\:
C_3 f(\beta_K, \beta'_K) + C_4$$

for every hyperbolic knot $K$. In other words, the second and next--to--last coefficients of the Jones polynomial do not coarsely predict the volume of a knot.
:::

Theorem [\[thm:counterexample\]](#thm:counterexample){reference-type="ref" reference="thm:counterexample"} relies on two families of examples: adequate Montesinos knots and closed 3--braids. For both of these families, Stoimenow found upper bounds on volume in terms of outer coefficients of the Jones polynomial [@stoimenow:amphichiral]. While Theorem [\[thm:counterexample\]](#thm:counterexample){reference-type="ref" reference="thm:counterexample"} implies that equation ([\[eqn:question\]](#eqn:question){reference-type="ref" reference="eqn:question"}) cannot hold for any function of $\beta_K$ and $\beta'_K$ alone, there might still be an affirmative answer to Question [\[question\]](#question){reference-type="ref" reference="question"} that uses other coefficients.
