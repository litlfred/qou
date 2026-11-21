---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-010-42-projective-convexity-and-laguerres-theorem
section_title: "Projective Convexity and Laguerre's Theorem"
section_number: 4.2
pages: 12-13
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 0.978
latex_coverage_ratio: 0.992
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
---
[]{#proj_conv_subsect label="proj_conv_subsect"}

Circular regions play a key role in Grace's theorem and its corollaries. The main reason for this is Laguerre's theorem, which essentially says that polar derivatives with respect to points of a circular region preserve stability for that circular region. This theorem in turn relies on the Gauss-Lucas theorem, which deals with convex regions.

A *circular region* in $\mathbb{C}$ is defined to be a disc, half-plane, or complement of a disc, and such a circular region can be either open or closed. The generalization of circular regions to $\mathbb{CP}^1$ is the obvious one. A *circular region* in $\mathbb{CP}^1$ is defined to be the sets in $\mathbb{CP}^1$ for which the stereographic projection is a circular region in $\mathbb{C}$. Note that $\mathop{\mathrm{SL}}_2(\mathbb{C})$ acts transitively on the set of all circular regions in $\mathbb{C}$ or in $\mathbb{CP}^1$. We now state a lemma to Laguerre's theorem, which gets at the heart of the importance of circular regions.

::: lemma
Let $C \subseteq \mathbb{CP}^1$ be a circular region, and let $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$ be such that its pole is not in $C$. Then, the stereographic projection of $\phi \cdot C$ is convex.
:::

::: proof
*Proof.* Let $(x_0:y_0) \notin C$ be the pole of $\phi$. Then, $\phi$ maps $(x_0:y_0)$ to $\infty \in \mathbb{CP}^1$ and maps $C$ to another circular region. Since $(x_0:y_0) \notin C$ implies $\infty \notin \phi \cdot C$, the sterographic projection of $\phi \cdot C$ is either an open half-plane or is bounded away from $\infty$. Since $\phi \cdot C$ is a circular region, it must be convex. ◻
:::

This then leads to a natural extension of the notion of a circular region.

::: definition
Given $C \subseteq \mathbb{CP}^1$, we say that $C$ is *projectively convex* if for every $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$ with pole not in $C$, the stereographic projection of $\phi \cdot C$ is convex.
:::

We now classify all projectively convex sets in $\mathbb{CP}^1$ in the following. This result has been demonstrated before in [@zervos1960aspects], where projectively convex regions are referred to as generalized circular regions.

::: proposition
[]{#proj_conv_characterization label="proj_conv_characterization"} Let $C \subseteq \mathbb{CP}^1$ be projectively convex. Then, $C = C^\circ \cup \gamma$, where $C^\circ$ is an open circular region which is the interior of $C$, and $\gamma$ is a connected subset of the boundary of $C^\circ$. In particular, projective convexity is preserved under taking complements.
:::

So, one example of a projectively convex set which is not quite a circular region is $\mathcal{H}_+\cup \mathbb{R}_+$. Another is $\mathcal{H}_+\cup [0,1]$. Yet another (albeit after a bit of consideration) is $\mathcal{H}_+\cup (-\infty,0) \cup (1,\infty]$. We now state a homogeneous version of Laguerre's theorem, extended to projectively convex sets.

::: proposition
[]{#laguerre_prop label="laguerre_prop"} Let $C \subseteq \mathbb{CP}^1$ be projectively convex, and fix $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$. If the pole of $\phi$ is in $C$, then $d_\phi$ preserves strong $C$-stability.
:::

::: proof
*Proof.* Gauss-Lucas and the fact that $\mathbb{CP}^1 \setminus C$ is projectively convex give the result. Specifically, for $C$-stable $p \in V(n)$ consider $\phi \cdot p$, which is stable in $\phi \cdot C \ni \infty$. Letting $B$ be the complement of $C$, the dehomogenization of this polynomial is then of degree exactly $n$ with all of its roots in the stereographic projection of $\phi \cdot B$. By projective convexity, $\phi \cdot B$ is convex and therefore Gauss-Lucas implies $\partial_x(\phi \cdot p)$ is $\phi \cdot C$-stable and not identically zero. Applying $\phi^{-1}$ then implies $d_\phi p = (\phi^{-1} \partial_x \phi) p$ is $C$-stable. ◻
:::

::: corollary
[]{#laguerre_cor label="laguerre_cor"} Let $C_k \subseteq \mathbb{CP}^1$ be projectively convex regions for $k \in [m]$, and fix $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$. If the pole of $\phi$ is in $C_{k_0}$, then $d_\phi$ acting on the variables $(x_{k_0},y_{k_0})$ preserves strong $(C_1 \times \cdots \times C_m)$-stability.
:::

::: proof
*Proof.* Follows from the fact that taking derivatives in some variables commutes with evaluation in the others. Specifically, $p \in V(\lambda)$ is $(C_1 \times \cdots \times C_m)$-stable iff $p \neq 0$ for all evaluations in $C_1 \times \cdots \times C_m$. So, evaluating $p$ in all variables in that product of sets except $(x_{k_0},y_{k_0})$ gives us a $C_{k_0}$-stable polynomial in $V(\lambda_{k_0})$. Applying the previous proposition then gives the result. ◻
:::
