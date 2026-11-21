---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-009-left-and-right-adjoints-of-kernels
section_title: "Left and right adjoints of kernels."
section_number: null
pages: 14-16
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.958
latex_coverage_ratio: 0.983
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
[]{#subsec:leftrightadjoints label="subsec:leftrightadjoints"} []{#subsec:yphimphi label="subsec:yphimphi"} In an arbitrary 2-category a given 1-morphism might or might not have a left or a right adjoint, but in the 2-category ${\mathscr{V}\textsf{ar}}$ every 1-morphism, that is every kernel, has both a left and a right adjoint. We will see below that for a kernel $\Phi\colon X\to Y$ there are adjunctions $$\Phi^{\scriptscriptstyle\vee}\circ\Sigma_Y\dashv\Phi\dashv\Sigma_X\circ
\Phi^{\scriptscriptstyle\vee},$$ where $\Phi^{\scriptscriptstyle\vee}\colon Y\to X$ means the object $\mathop{\mathrm{\underline{Hom}}}_{\mathbf{D}(X\times
  Y)}(\Phi,{\mathscr O}_{X\times Y})$ considered as an object in $\mathbf{D}(Y\times
X)$. This should be compared with the fact that if $M$ is an $A$-$B$-bimodule then $M^{\scriptscriptstyle\vee}$ is naturally a $B$-$A$-bimodule. We shall see that the two adjunctions above are related in some very useful ways.

::: Proposition
[]{#prop:deltalstar label="prop:deltalstar"} If $X$ is a space and $\Delta\colon X\to X\times X$ is the diagonal embedding then $\Delta_*\colon \mathbf{D}(X)\to \mathbf{D}(X\times X)$, the push-forward on derived categories, is a monoidal functor where $\mathbf{D}(X)$ has the usual monoidal tensor product $\otimes$ and $\mathbf{D}(X\times X)$ has the composition $\circ$ as the monoidal structure.
:::

::: Proof
The proof is just an application of the projection formula.
:::

This has the following immediate consequence.

::: Lemma
If ${\mathscr E}$ and ${\mathscr F}$ are dual as objects in $\mathbf{D}(X)$ then $\Delta_*{\mathscr E}$ and $\Delta_*{\mathscr F}$ are both left and right adjoint to each other as 1-morphisms in ${\mathscr{V}\textsf{ar}}$.
:::

In order not to hold-up the flow of the narrative, the proofs of the remaining results from this section have been relegated to Appendix [\[sec:duality\]](#sec:duality){reference-type="ref" reference="sec:duality"}.

We begin with some background on the Serre kernel $\Sigma_X$. Recall from Section [\[sec:serre\]](#sec:serre){reference-type="ref" reference="sec:serre"} that the anti-Serre kernel $\Sigma^{-1}_X$ is defined to be $\Delta_*\omega^{-1}_X[-\dim X]$, and that the Serre kernel $\Sigma_X$ is denoted by a dashed-dotted line, while the anti-Serre kernel $\Sigma^{-1}_X$ is denoted by a dashed-dotted line with a horizontal bar. The above proposition means that we actually have maps $$\raisebox{-.45\height}{},\quad
\raisebox{-.45\height}{},\quad
\raisebox{-.45\height}{},\quad
\raisebox{-.45\height}{}$$ satisfying the following relations $$\raisebox{-.45\height}{}=\raisebox{-.45\height}{},\quad
\raisebox{-.45\height}{}=\raisebox{-.45\height}{},\quad
\raisebox{-.45\height}{}=\raisebox{-.45\height}{},\quad$$ and all obvious variations thereof.

In the appendix it is shown that for a kernel $\Phi$ there are natural morphisms ${\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}_\Phi\colon \Phi\circ\Sigma_X\circ\Phi^{\scriptscriptstyle\vee}\to {\mathscr O}_\Delta$ and $\gamma_\Phi\colon \Sigma_X^{-1}\to \Phi^{\scriptscriptstyle\vee}\circ \Phi$, denoted in the following fashion, where the solid, upward oriented lines are labelled with $\Phi$ and the solid, implicitly downward oriented lines are labelled by $\Phi^{\scriptscriptstyle\vee}$: $${\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}_\Phi:\raisebox{-.45\height}{}\quad \text{and}\quad \gamma_\Phi:\raisebox{-.45\height}{}.$$ The main property of ${\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}_\Phi$ and $\gamma_\Phi$ is that if we define $\epsilon_\Phi$, $\overline \epsilon_\Phi$, $\eta_\Phi$ and $\overline\eta_\Phi$ via $$\begin{gathered}
 \eta_\Phi: \raisebox{-.45\height}{}:=\raisebox{-.45\height}{},\qquad
\overline\eta_\Phi: \raisebox{-.45\height}{}:=\raisebox{-.45\height}{},\\
\epsilon_\Phi:={\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}_{\Phi^{\scriptscriptstyle\vee}}=\raisebox{-.45\height}{},\qquad
\overline\epsilon_\Phi:={\begin{turn}{270}$\!\!\!\epsilon\ $\end{turn}}_{\Phi}=\raisebox{-.45\height}{},
\end{gathered}$$ then these are the units and counits of adjunctions $$\Phi^{\scriptscriptstyle\vee}\circ\Sigma_Y\dashv\Phi\dashv\Sigma_X\circ
\Phi^{\scriptscriptstyle\vee}.$$
