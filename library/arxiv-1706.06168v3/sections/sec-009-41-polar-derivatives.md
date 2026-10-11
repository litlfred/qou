---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-009-41-polar-derivatives
section_title: "Polar Derivatives"
section_number: 4.1
pages: 11-13
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
text_source: latex
latex_prose_ratio: 0.986
latex_coverage_ratio: 0.981
---
A crucial tool of classical stability theory is the polar derivative. In particular, this notion leads to Laguerre's theorem (Proposition [\[laguerre_prop\]](#laguerre_prop){reference-type="ref" reference="laguerre_prop"}), which is the main lemma toward Grace's theorem. By passing to homogeneous polynomials the polar derivative becomes conceptually simpler, and this in turn sheds further light on the general connection to $\mathop{\mathrm{SL}}_2(\mathbb{C})$-invariance and the $D$ map. One example of this, as we will see below, is that the polar derivative can be defined as the conjugation of $\partial_x$ by some $\mathop{\mathrm{SL}}_2(\mathbb{C})$ action.

Given some "pole" $x_0 \in \mathbb{C}$, the *polar derivative* with respect to $x_0$ of $f \in \mathbb{C}^n[x]$ is classically defined as follows. $$(d_{x_0}f)(x) := nf(x) - (x-x_0)f'(x)$$ Noticing that the term of degree $n$ cancels out, the resulting polynomial is of degree $n-1$. It is typically said that this operator generalizes the ordinary derivative in the sense that $\lim_{x_0 \rightarrow \infty} x_0^{-1}d_{x_0}f(x) = f'(x)$. However, this operator also generalizes the ordinary derivative in more natural way, which we see by passing to $V(n)$.

Fix any $\phi = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \in \mathop{\mathrm{SL}}_2(\mathbb{C})$. Define the *pole* of $\phi$ to be $(-d:c) \in \mathbb{CP}^1$. For $p \in V(n)$, we then define the polar derivative with respect to $\phi$ as follows. $$d_\phi p := (\phi^{-1}\partial_x\phi)p = -(-d\partial_x + c\partial_y)p$$ Notice that $d_\phi$ depends only on $\phi^{-1}\binom{-1}{0} = \binom{-d}{c}$. With this, the pole of $\phi$ should be interpreted as the element of $\mathbb{CP}^1$ that $\phi$ sends to $\infty = (-1:0)$.

This definition of the polar derivative with respect to $\phi$ is at very least a natural one, as it can be simply described as the conjugation of $\partial_x$ by the action of $\phi$. The following result then shows that this is actually the correct definition.

::: proposition
Fix $\phi \equiv \begin{bmatrix} a & b \\ c & d \end{bmatrix} \in \mathop{\mathrm{SL}}_2(\mathbb{C})$ with pole $(-d:c)$, and define $x_0 := \frac{-d}{c}$ (for $c \neq 0$). Then: $$d_\phi \circ \mathop{\mathrm{Hmg}}_n = \mathop{\mathrm{Hmg}}_{n-1} \circ (-c \cdot d_{x_0})$$ That is, the polar derivative $d_\phi$ on $V(n)$ is the homogenization of the classical polar derivative $d_{x_0}$ on $\mathbb{C}^n[x]$ (up to scalar).
:::

::: proof
*Proof.* Straightforward computation. ◻
:::

As mentioned above, $d_\phi$ depends only on $(-d:c)$, the pole of $\phi$. So given any pole in $\mathbb{CP}^1$, we can actually choose $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$ to be a rotation of the Riemann sphere (i.e., $\mathbb{CP}^1$). This then gives the following intuitive description of the polar derivative.

::: remark
Fix a rotation $\phi \in \mathop{\mathrm{SL}}_2(\mathbb{C})$ with pole $(-d:c)$. The polar derivative $d_\phi$ then acts on $p \in V(n)$ in the following way. First, consider the zeros of $p$ as being placed in the Riemann sphere via stereographic projection. Next, rotate the sphere via $\phi$, which moves $(-d:c)$ to infinity at the top of the sphere. Apply the derivative to the new polynomial given by the new locations of the zeros. Finally, undo the original rotation via $\phi^{-1}$, which moves infinity back to the pole $(-d:c)$.
:::

## Projective Convexity and Laguerre's Theorem {#proj_conv_subsect}

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
