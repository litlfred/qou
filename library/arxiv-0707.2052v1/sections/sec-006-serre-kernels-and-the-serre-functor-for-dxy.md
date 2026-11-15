---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-006-serre-kernels-and-the-serre-functor-for-dxy
section_title: "Serre kernels and the Serre functor for D(XY)."
section_number: null
pages: 11-12
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.986
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#subsec:serXY label="subsec:serXY"} We are interested in kernels and the 2-category ${\mathscr{V}\textsf{ar}}$, so are interested in Serre functors for product spaces $X\times Y$, and these have a lovely description in the 2-categorical language. We can now define one of the key objects in this paper.

::: Definition
For a space $X$, the *Serre kernel* $\Sigma_X\in \mathop{\mathrm{1\mbox{-}Hom}}_{\mathscr{V}\textsf{ar}}(X,X)$ is defined to be $\Delta_*\omega_X[\dim X]\in\mathbf{D}(X\times X)$, the kernel inducing the Serre functor on $X$. Similarly the *anti-Serre kernel* $\Sigma^{-1}_X\in \mathop{\mathrm{1\mbox{-}Hom}}_{\mathscr{V}\textsf{ar}}(X,X)$ is defined to be $\Delta_*\omega^{-1}_X[-\dim X]\in\mathbf{D}(X\times X)$.
:::

::: Notation
In string diagrams the Serre kernel will be denoted by a dashed-dotted line, while the anti-Serre kernel will be denoted by a dashed-dotted line with a horizontal bar through it (see the pictures in Section [\[subsec:leftrightadjoints\]](#subsec:leftrightadjoints){reference-type="ref" reference="subsec:leftrightadjoints"}).
:::

The Serre kernel can now be used to give a natural description, in the 2-category language, of the Serre functor on the product $X\times Y$.

::: Proposition
For spaces $X$ and $Y$ the Serre functor $\mathsf{S}_{X\times Y}\colon
\mathbf{D}(X\times Y)\to \mathbf{D}(X\times Y)$ can be taken to be $\Sigma_Y\circ{-}\circ\Sigma_X$.
:::

::: Proof
The Serre functor on $\mathbf{D}(X\times Y)$ is given by $$\mathsf{S}_{X\times Y}(\Phi)= \Phi\otimes \pi_X^*\omega_X\otimes
\pi_Y^*\omega_Y[\dim X+\dim Y].$$ However, observe that if $\Phi\in \mathbf{D}(X\times Y)$ and ${\mathscr E}\in \mathbf{D}(X)$ then $$\Phi\circ \Delta_*{\mathscr E}\cong \Phi\otimes \pi_X^* {\mathscr E},$$ where $\pi_X\colon X\times Y \to X$ is the projection. This is just a standard application of the base-change and projection formulas. Similarly if ${\mathscr F}\in \mathbf{D}(Y)$ then $\Delta_*{\mathscr F}\circ\Phi\cong \pi_Y^*
{\mathscr F}\otimes\Phi.$ From this the Serre functor can be written as $$\mathsf{S}_{X\times Y}(\Phi)= \Sigma_Y\circ\Phi\circ \Sigma_X.\qedhere$$
:::

This means that the Serre trace map on $X\times Y$ is a map $$\mathop{\mathrm{Tr}}\colon\mathop{\mathrm{{2\mbox{-}Hom}}}_{\mathscr{V}\textsf{ar}}(\Phi, \Sigma_Y \circ\Phi\circ\Sigma_X) \rightarrow\textsf{k}$$ which can be pictured as $$\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right) \in \textsf{k},$$ where the Serre kernel is denoted by the dashed-dotted line.

We will see below that we have 'partial trace' operations which the Serre trace factors through.
