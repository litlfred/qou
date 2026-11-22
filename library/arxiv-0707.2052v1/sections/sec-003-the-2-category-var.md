---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-003-the-2-category-var
section_title: "The 2-category Var."
section_number: null
pages: 9-10
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
toc_source: outline
text_source: latex
latex_prose_ratio: 1.0
latex_coverage_ratio: 0.974
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasizing the importance of a pairing which generalizes Mukai’s pairing on the cohomology of K3"
---
The 2-category ${\mathscr{V}\textsf{ar}}$, of spaces and integral kernels, is defined as follows. The objects are spaces, as defined in the introduction, and the hom-category $\mathop{\mathrm{\textbf{\textsf{Hom}}}}_{\mathscr{V}\textsf{ar}}(X,Y)$ from a space $X$ to a space $Y$ is the derived category $\mathbf{D}(X\times Y)$, which is to be thought of as the category of integral kernels from $X$ to $Y$. Explicitly, this means that the 1-morphisms in ${\mathscr{V}\textsf{ar}}$ from $X$ to $Y$ are objects of $\mathbf{D}(X\times Y)$ and the 2-morphisms from $\Phi$ to $\Phi'$ are morphisms in $\mathop{\mathrm{Hom}}_{\mathbf{D}(X\times Y)}(\Phi,\Phi')$, with vertical composition of 2-morphisms just being usual composition in the derived category.

Composition of 1-morphisms in ${\mathscr{V}\textsf{ar}}$ is defined using the convolution of integral kernels: if $\Phi\in \mathbf{D}(X\times Y)$ and $\Psi\in
\mathbf{D}(Y\times Z)$ are 1-morphisms then define the convolution $\Psi\circ\Phi\in\mathbf{D}(X\times Z)$ by $$\Phi\circ \Psi := \pi^{}_{XZ, *} ( \pi_{YZ}^* \Psi \otimes
\pi_{XY}^* \Phi),$$ where $\pi_{XZ}$, $\pi_{XY}$ and $\pi_{YZ}$ are the projections from $X\times Y\times Z$ to the appropriate factors. The horizontal composition of 2-morphisms is similarly defined. Finally, the identity 1-morphism $\mathsf {Id}_X\colon X\rightarrow X$ is given by ${\mathscr O}_{\Delta}\in \mathbf{D}(X\times X)$, the structure sheaf of the diagonal in $X\times X$.

The above 2-category is really what is at the heart of the study of integral transforms, and it is entirely analogous to ${\mathscr{A}\textsf{lg}}$, the 2-category of algebras described above. For example, the Hochschild cohomology groups of a space $X$ arise as the second homotopy groups of the 2-category ${\mathscr{V}\textsf{ar}}$, at $X$: $$\begin{aligned}
  \mathop{\mathrm{HH}}^\bullet(X) &:=\mathop{\mathrm{Ext}}_{X\times X}^\bullet({\mathscr O}_\Delta,{\mathscr O}_\Delta)
  \cong \mathop{\mathrm{Hom}}^\bullet_{D(X\times X)}({\mathscr O}_\Delta,{\mathscr O}_\Delta)\\
  &=:\mathop{\mathrm{{2\mbox{-}Hom}}}_{{\mathscr{V}\textsf{ar}}}(\mathsf {Id}_X,\mathsf {Id}_X).
\end{aligned}$$

There is a 2-functor from ${\mathscr{V}\textsf{ar}}$ to ${\mathscr{C}\textsf{at}}$ which encodes integral transforms: this 2-functor sends each space $X$ to its derived category $\mathbf{D}(X)$, sends each kernel $\Phi\colon X\to Y$ to the corresponding integral transform $\overline \Phi\colon D(X)\to D(Y)$, and sends each map of kernels to the appropriate natural transformation. Many of the statements about integral transforms have better formulations in the language of the 2-category ${\mathscr{V}\textsf{ar}}$.
