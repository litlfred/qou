---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-026-the-baggy-cardy-condition
section_title: "The Baggy Cardy Condition."
section_number: null
pages: 29-31
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 0.983
latex_coverage_ratio: 0.992
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
In the case of a manifold $X$ that is not necessarily Calabi-Yau we don't have the same coincidence of structure as above: we no longer have a Frobenius algebra $\mathop{\mathrm{HH}}^\bullet(X)$; rather we have an algebra $\mathop{\mathrm{HH}}^\bullet(X)$ and an inner product space $\mathop{\mathrm{HH}}_\bullet(X)$. This means that we can not formulate the Cardy Condition as it stands. We now state a condition which makes sense for an arbitrary, non-Calabi-Yau manifold and which is equivalent to the Cardy Condition in the Calabi-Yau case.

::: Theorem
Suppose that $\textsf{O}$ is a Calabi-Yau category and $\textsf{C}$ is an inner product space, such that for each $A\in \textsf{O}$ there are adjoint maps $i^A\colon \textsf{O}_{AA}\to \textsf{C}$ and $i_A\colon
  \textsf{C}\to \textsf{O}_{AA}$. Then the Cardy Condition $$\mu_{BAB}\circ\tau\circ\delta_{ABA}=i_B\circ i^A$$ is equivalent to the following equality holding for all $a\in
  \textsf{O}_{AA}$ and $b\in \textsf{O}_{BB}$, where the map ${}_{a}m_{b}\colon
  \textsf{O}_{AB}\to \textsf{O}_{AB}$ is the map obtained by pre-composing with $a$ and post-composing with $b$: $$\left\langle i^B{-},i^A{-}\right\rangle_\textsf{C}=
  \mathop{\mathrm{Tr}}{}_{-}m_{-}.$$
:::

::: Proof
The first thing to do is examine the left-hand side of the Cardy Condition. As $\textsf{O}$ is a Calabi-Yau category there is the following equality of morphisms $\textsf{O}_{AA}\to \textsf{O}_{BB}$. $$\raisebox{-.45\height}{}=\raisebox{-.45\height}{}$$ Note that this does not require any reference to $\textsf{C}$, but it does fundamentally require the symmetry of the inner product. This is reflected in the fact that the surfaces underlying the above pictures are diffeomorphic but not ambient isotopic.

This means that the Cardy Condition is equivalent to the following equality. $$\raisebox{-.45\height}{}=\raisebox{-.45\height}{}$$ By the non-degeneracy of the inner product on $\textsf{O}_{BB}$ this is equivalent to the equality of two maps $\textsf{O}_{BB}\otimes
  \textsf{O}_{AA}\to\textsf{k}$ which are drawn as follows. $$\raisebox{-.45\height}{}=\raisebox{-.45\height}{}$$ The right-hand side is instantly identifiable as $\left\langle
    i^B{-},i^A{-}\right\rangle_\textsf{C}$. The left-hand side is identifiable as the trace of the triple composition map $\textsf{O}_{BB}\otimes\textsf{O}_{BA}\otimes\textsf{O}_{AA}\to \textsf{O}_{BA}$ which gives the required result.
:::

We can now show that the alternative condition given in the above theorem holds for the derived category and Hochschild homology of *any* space: in particular, the Cardy Condition holds for Calabi-Yau spaces.

::: Theorem
[]{#thm:cardy label="thm:cardy"} Let $X$ be a space, let ${\mathscr E}$ and ${\mathscr F}$ be objects in $\mathbf{D}(X)$ and consider morphisms $$e\in \mathop{\mathrm{Hom}}_{\mathbf{D}(X)}({\mathscr E}, {\mathscr E}) \quad\text{and}\quad f\in
\mathop{\mathrm{Hom}}_{\mathbf{D}(X)}({\mathscr F}, {\mathscr F}).$$ Define the operator $${}_f m_e \colon\mathop{\mathrm{Hom}}^\bullet_{\mathbf{D}(X)}({\mathscr E}, {\mathscr F}) \rightarrow
\mathop{\mathrm{Hom}}^\bullet_{\mathbf{D}(X)}({\mathscr E}, {\mathscr F})$$ to be post-composition by $f$ and pre-composition by $e$. Then we have $$\mathop{\mathrm{Tr}}{}_f m_e={\ensuremath{\left\langle \iota^{\mathscr E}(e),\, \iota^{\mathscr F}(f)\right\rangle_{\rm M}}},$$ where $\iota^{\mathscr E}$, $\iota^{\mathscr F}$ are the maps defined in Section [\[subsec:iotae\]](#subsec:iotae){reference-type="ref" reference="subsec:iotae"}, and $\mathop{\mathrm{Tr}}$ denotes the (super) trace.
:::

::: Proof
The proof is very similar to the proof of the Semi-Hirzebruch-Riemann-Roch Theorem (Theorem [\[thm:hrr\]](#thm:hrr){reference-type="ref" reference="thm:hrr"}). The first thing to observe is that $\mathop{\mathrm{Hom}}({\mathscr E},{\mathscr F})\cong {\mathscr E}^{\scriptscriptstyle\vee}\circ {\mathscr F}$ and that ${}_f m_e$ is just $e^{\scriptscriptstyle\vee}\circ f$. However, we have $\tau_R(e)=\Sigma_{\mathsf{pt}}\circ e^{\scriptscriptstyle\vee}$ and $\Sigma_{\mathsf{pt}}$ is trivial so $e^{\scriptscriptstyle\vee}=\tau_R(e)$. Putting this together with the invariance of the Serre trace under the partial trace we get the following sequence, and hence the required result. $$\begin{aligned}
    \mathop{\mathrm{Tr}}{}_f m_e&=\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right)
    =\mathop{\mathrm{Tr}}\left( \raisebox{-.45\height}{}\right)\\
    &=\mathop{\mathrm{Tr}}\left( \raisebox{-.45\height}{}\right)
    =\mathop{\mathrm{Tr}}\left( \raisebox{-.45\height}{}\right)\\
    &={\ensuremath{\Biggl\langle \raisebox{-.45\height}{},\, \raisebox{-.45\height}{}\Biggr\rangle_{\rm M}}}
    ={\ensuremath{\left\langle \iota^{\mathscr E}\!(e),\, \iota^{\mathscr F}\!(f)\right\rangle_{\rm M}}}.\qedhere
  
\end{aligned}$$
:::

Observe that the Semi-Hirzebruch-Riemann-Roch Theorem is a direct consequence of the Baggy Cardy Condition, with $e=\mathsf {Id}_{\mathscr E}$, $f=\mathsf {Id}_{\mathscr F}$.
