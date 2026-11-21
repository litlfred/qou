---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-016-52-the-setup-of-the-proof
section_title: "The setup of the proof"
section_number: 5.2
pages: 12-13
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.947
latex_coverage_ratio: 0.973
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
Since the natural cocycle is given in terms of the Ptolemy coordinates, it follows that $\rho$ is defined over the Ptolemy field. Hence, the trace field is a subfield of the Ptolemy field.

Fix a maximal tree $G$ with $1$ or $3$-cycle as in Figures~\ref{fig:TreeWithCycle} or \ref{fig:TreeWithThreeCycle}. As explained in Section~\ref{sec:AlphaStarBasic} the edges of $G$ are basic generators of $\alpha^*$. We may thus assume without loss of generality that the Ptolemy coordinates $c_i$ of the edges $\varepsilon_i$ of $G$ are $1$. By~\eqref{eq:kc}, it is thus enough to show that the Ptolemy coordinates of the remaining $1$-cells are in the trace field.


Let $\gamma$ denote the (lifted) natural cocycle of $c$. Then $\gamma$ assigns to each edge path $p$ in $\widehat M$ a matrix $\gamma(p)\in\SL(2,\C)$. Let
\begin{equation}\label{eq:AlphaBeta}
\alpha(a)=\begin{pmatrix}0&-a^{-1}\\a&0\end{pmatrix},\qquad \beta(b)=\begin{pmatrix}1&b\\0&1\end{pmatrix}.
\end{equation}
As shown in Figure~\ref{fig:PtolemyToCocycle}, $\gamma$ takes long and short edges to elements of the form $\alpha(a)$ and $\beta(b)$, respectively, where $a$ and $b$ are given in terms of the Ptolemy coordinates.

Since $\rho$ is boundary-non trivial, there exists for each cusp $i$ of $M$ a peripheral loop $M_i$ with $\gamma(M_i)\in P$ non-trivial. We shall here refer to such loops as \emph{non-trivial}. Fix such non-trivial loops $M_i$, once and for all, and let $m_i\neq 0$ be such that $\gamma(M_i)=\beta(m_i)$.
For any edge path $p$ with end point on a cusp $i$ we can alter $M_i$ by a conjugation if necessary (this does not change $m_i$) so that $p$ is composable with $M_i$.
