---
doc_id: arxiv-0808.2716v4
doc_title: "CUSP AREAS OF F AREY MANIFOLDS"
section_id: sec-002-12-cusp-area-and-link-diagrams
section_title: "Cusp area and link diagrams"
section_number: 1.2
pages: 3-6
source_pdf: 0808.2716v4.pdf
source_sha256: ea66f7ddcf9e9fe6
doc_brief: "CUSP AREAS OF F AREY MANIFOLDS — This paper gives the ﬁrst explicit, two–sided estimates on t he cusp area of once– punctured torus bundles, 4–punctured sphere bundles, and 2 –bridge link"
text_source: latex
latex_prose_ratio: 0.948
latex_coverage_ratio: 0.978
---
[]{#sec:diagram-intro label="sec:diagram-intro"}

A closely related class of manifolds are complements of 2--bridge links. Using similar techniques, in this paper we are also able to bound the lengths of slopes on maximal cusps in hyperbolic 2--bridge links. Since all 2--bridge links can be represented by an alternating diagram, our results give further evidence for a conjectural picture of the cusp shapes and maximal cusp metrics of alternating knots.

For general alternating knots and links, there is increasing evidence that the cusp shape and maximal cusp metric ought to be bounded in terms of the twist number of a reduced diagram. We say that a link diagram is *reduced* if it does not contain any crossings that separate the diagram: that is, any crossings in the projection plane such that there is a simple closed curve meeting the diagram transversely in only that crossing. Similarly, two crossings are said to be equivalent if there exists a simple closed curve meeting the knot diagram transversely in those two crossings, disjoint from the knot diagram elsewhere. The *twist number* is the number of equivalence classes of crossings (called *twist regions*).

::: conjecture
The area of a maximal cusp metric on an alternating knot is bounded above and below by linear functions of the twist number of a reduced, alternating diagram. Similarly, the length of the shortest non-meridional slope of an alternating knot is bounded above and below by a linear function of the twist number of the diagram. []{#conj:alt-knot-cusp label="conj:alt-knot-cusp"}
:::

We first became aware of this conjecture several years ago by viewing slides of a talk by Thistlethwaite, in which he showed using SnapPea that the conjecture holds for many simple alternating knots. Lackenby proved a close variant the conjecture, relating the twist number of a diagram to the *combinatorial length* of slopes [@lackenby:word]. However, Lackenby's methods are purely combinatorial and cannot be applied to give the geometric information of the conjecture.

In this paper we prove the conjecture for 2--bridge link complements. In particular, we show the following.

::: named
Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"} Let $K$ be a 2--bridge link in $S^3$, whose reduced alternating diagram has twist number $t$. Let $C$ be a maximal neighborhood about the cusps of $S^3 {\smallsetminus}
K$, in which the two cusps have equal volume if $K$ has two components. Then $$\frac{8\sqrt{3}}{147}\,(t-1) \: \leq \: {\rm area}({\partial}C) \:
<\: 2\sqrt{3}\,\, \frac{v_8}{v_3}\,(t-1).$$ Furthermore, if $K$ is a knot, let $\gamma$ be any non-trivial arc that starts on a meridian and comes back to the same meridian (for example, a non-meridional simple closed curve). Then its length satisfies $$\ell(\gamma) \: \geq \: \frac{4\sqrt{6\sqrt{2}}}{147}\, (t-1).$$
:::

This result should be compared to that of Adams *et al.* [@adams-students:cusp-area], where they prove upper bounds on cusp area in terms of the crossing number $c$ of a knot. For alternating knots, including 2--bridge knots, they show that the cusp area satisfies ${\rm area}({\partial}C) \leq 9c - 36 + 36/c$. For those 2--bridge knots whose diagrams have very few crossings per twist region (in particular, when $c/t < 1.39$), the bound of Adams *et al.* is sharper than the upper bound of Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"}. For more general 2--bridge knots that have more crossings per twist region, the upper bound of Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"} is a significant improvement. To the best of our knowledge, the lower bound of Theorem [\[thm:2bridge\]](#thm:2bridge){reference-type="ref" reference="thm:2bridge"} does not have any predecessors in the literature.

## Applications to hyperbolic Dehn filling

The shapes of the cusps and their actual metrics give information not just on the 3--manifold itself, but also on the Dehn fillings of that manifold.

For example, modulo the geometrization conjecture, several theorems imply that Dehn fillings on slopes of sufficient length yield hyperbolic manifolds (these are the $2\pi$--Theorem, due to Gromov and Thurston [@bleiler-hodgson]; the 6--Theorem, due to Agol [@agol:bounds] and Lackenby [@lackenby:word]; and the $7.515$--Theorem, due to Hodgson and Kerckhoff [@hk:univ]). When we combine these theorems with the results on maximal cusp areas and slope lengths above, we find that Farey manifolds with long monodromy admit no non-trivial Dehn fillings, where "long" is explicit.

In particular, Bleiler and Hodgson [@bleiler-hodgson] note that the work of Jørgensen [@jorgensen] combined with the $2\pi$--Theorem implies that there is a constant $N$ such that every non-trivial Dehn filling of a punctured torus bundle with monodromy length $s>N$ gives a hyperbolic 3--manifold. However, they remark on the lack of an explicit value for the constant $N$. Now Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"}, coupled with the 6--Theorem, allows the estimate $N\leq 90$.

More recently, the authors proved a result that bounds the volume of manifolds obtained by Dehn filling along a slope of length at least $2\pi$, in terms of the length of that slope [@fkp-07]. Thus we may combine Theorem [\[thm:ptorus-area\]](#thm:ptorus-area){reference-type="ref" reference="thm:ptorus-area"} with this recent result to estimate the volumes of the manifolds obtained by Dehn filling. For example, if $M$ is a punctured--torus bundle with monodromy of length $s>94$, then the length of any non-trivial slope $\gamma$ on the cusp of $M$ (i.e. any slope transverse to the fibers) will be at least $2\pi$. Then by [@fkp-07 Theorem 1.1], the volume of the manifold $M(\gamma)$ obtained by Dehn filling $M$ along $\gamma$ will be bounded explicitly below. See Corollary [\[cor:ptorus-volume\]](#cor:ptorus-volume){reference-type="ref" reference="cor:ptorus-volume"}.

One large class of examples obtained by Dehn filling 4--punctured sphere bundles is the class of closed 3--braids, which has been extensively studied by others (see e.g. Murasugi [@murasugi:3braids], Birman and Menasco [@birman-menasco:3braids]). In this paper, we classify the hyperbolic links that are closed 3--braids (see Theorem [\[thm:hyperbolic-3braid\]](#thm:hyperbolic-3braid){reference-type="ref" reference="thm:hyperbolic-3braid"}), and obtain the first estimates on volumes of these links.

<figure id="fig:3braid-generators">
<div class="center">
<embed src="figures/Fig_braid-generators.eps" />
</div>
<figcaption>Braid group generators <span class="math inline"><em>σ</em><sub>1</sub></span> and <span class="math inline"><em>σ</em><sub>2</sub></span>.</figcaption>
</figure>

To state these results, let $\sigma_1$, $\sigma_2$ denote the generators for $B_3$, the braid group on three strands, as in Figure [1](#fig:3braid-generators){reference-type="ref" reference="fig:3braid-generators"}. Let $C= (\sigma_1 \sigma_2)^3$. It is known, by work of Schreier [@schreier], that most $3$--braids are conjugate to words of the form $w = C^k \sigma_1^{p_1} \sigma_2^{-q_1}
\cdots \sigma_1^{p_s} \sigma_2^{-q_s}$, where $p_i$, $q_i$ are all positive. In particular, all $3$--braids with hyperbolic closures are of this form, as we shall show in Theorem [\[thm:hyperbolic-3braid\]](#thm:hyperbolic-3braid){reference-type="ref" reference="thm:hyperbolic-3braid"}. Following Birman and Menasco [@birman-menasco:3braids], we call such braids *generic*.

::: named
Theorem [\[thm:3braid-volume\]](#thm:3braid-volume){reference-type="ref" reference="thm:3braid-volume"} Let $K= \hat{w}$ be the closure of a generic 3--braid $w = C^k
\sigma_1^{p_1} \sigma_2^{-q_1} \cdots \sigma_1^{p_s} \sigma_2^{-q_s}$, where $C= (\sigma_1 \sigma_2)^3$, and $p_i$, $q_i$ are all positive. Suppose, furthermore, that $w$ is not conjugate to $\sigma_1^{p}
\sigma_2^q$ for arbitrary $p$, $q$. Then $K$ is hyperbolic, and $$4v_3 \, s - 277 \: < \: {\rm vol}(S^3 {\smallsetminus}K) \: < \: 4v_8 \, s,$$

where $v_3 = 1.0149...$ is the volume of a regular ideal tetrahedron and $v_8 = 3.6638...$ is the volume of a regular ideal octahedron. Furthermore, the multiplicative constants in both the upper and lower bounds are sharp.
:::

## Volume and Jones polynomial invariants

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
