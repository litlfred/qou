---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-010-partial-traces
section_title: "Partial traces."
section_number: null
pages: 16-17
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 1.0
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
We can now define the important notion of partial traces.

::: Definition
For a kernel $\Phi\colon X\to Y$, and kernels $\Psi,\Theta\colon Z\to X$ define the *left partial trace* $$\mathop{\mathrm{{2\mbox{-}Hom}}}(\Phi\circ\Theta,\Sigma_Y\circ\Phi\circ\Psi) \to
  \mathop{\mathrm{{2\mbox{-}Hom}}}(\Theta,\Sigma_X\circ\Psi)$$ as $$\raisebox{-.45\height}{}\mapsto\raisebox{-.45\height}{}.$$ Similarly we define a *right partial trace* $$\mathop{\mathrm{{2\mbox{-}Hom}}}(\Theta'\circ\Phi,\Psi'\circ\Phi\circ\Sigma_X) \to
  \mathop{\mathrm{{2\mbox{-}Hom}}}(\Theta',\Psi'\circ\Sigma_Y)$$ as $$\raisebox{-.45\height}{}\mapsto\raisebox{-.45\height}{}.$$
:::

The following key result, proved in the appendix, says that taking partial trace does not affect the Serre trace.

::: Theorem
For a kernel $\Phi\colon X\to Y$, a kernel $\Psi\colon Z\to X$ and a kernel morphism $\alpha\in\mathop{\mathrm{Hom}}(\Phi\circ{\mathscr F},\Sigma_Y\circ\Phi\circ\Psi\circ\Sigma_Z)$ then the left partial trace of $\alpha$ has the same Serre trace as $\alpha$, i.e., pictorially $$\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right)=\mathop{\mathrm{Tr}}\left(\raisebox{-.45\height}{}\right).$$ The analogous result holds for the right partial trace.
:::
