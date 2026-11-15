---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-009-41-polar-derivatives
section_title: "Polar Derivatives"
section_number: 4.1
pages: 11-12
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.974
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨and´en characterized all linear operators on multivariate polynomials which preserve the"
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
