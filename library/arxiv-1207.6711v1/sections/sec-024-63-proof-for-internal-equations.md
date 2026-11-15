---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-024-63-proof-for-internal-equations
section_title: "Proof for internal equations"
section_number: 6.3
pages: 19-20
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.733
latex_coverage_ratio: 0.846
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{subsection:ProofForInternalEqn}
A local model near an interior point is a single simplex.
\begin{lemma}\label{lemma:InternalEquation} A Ptolemy assignment on $\Delta^3_n$ gives rise to a shape assignment satisfying the internal gluing equations.
\end{lemma}
\begin{proof}
Let $t$ be of the form $t=\alpha+1111$ with $\alpha\in\Delta^{3}_{n-4}(\Z)$. The gluing equation for $t$ involves
\begin{equation}
z^{0011}_{\alpha+1100}  z^{0101}_{\alpha+1010}    z^{0110}_{\alpha+1001}    z^{1001}_{\alpha+0110}     z^{1010}_{\alpha+0101}    z^{1100}_{\alpha+0011}.
\end{equation}
When expanding this using \eqref{eqn:PtolemyToShapes}, the two signs cancel and the numerator and denominator both consist of all Ptolemy coordinates $c_{\alpha+\beta}$ where $\beta$ is a permutation of $(0,1,1,2)$. Hence, the product is 1.
\end{proof}
\begin{corollary}
Theorem~\ref{thm:PtolemyYieldsShapes} holds for the internal gluing equations.\qed
\end{corollary}
