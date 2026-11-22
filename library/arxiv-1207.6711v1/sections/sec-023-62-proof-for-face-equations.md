---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-023-62-proof-for-face-equations
section_title: "Proof for face equations"
section_number: 6.2
pages: 19-19
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.907
latex_coverage_ratio: 1.0
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{subsection:ProofForFaceEqn}
A local model for a neighborhood of a face point $p$ is the complex $K$ obtained by gluing two simplices $\Delta_0$ and $\Delta_1$ by identifying the faces 012 of each simplex in the order-preserving way, see Figure~\ref{fig:FaceLocal}. As for the edge equations, it is enough to verify the face equations on $K$. 
\begin{lemma}
A Ptolemy assigment on $K$ gives shape assignments satisfying the face equations. The same holds after reordering.
\end{lemma}
\begin{proof}
Let $t=(t_0,t_1,t_2,0)=\alpha+1110$ where $\alpha$ is a face point of $\Delta^3_{n-3}$. The representatives of the corresponding face point $p$ of $K$ are $(t,\Delta_0)$ and $(t,\Delta_1)$. Since $\Delta_0$ and $\Delta_1$ have opposite orientations in $K$, the face equation for $p$ involves the terms
\begin{equation}\label{eqn:proofFaceEqn}
z^{0110}_{\alpha+1000,0}z^{1010}_{\alpha+0100,0}z^{1100}_{\alpha+0010,0} \left(z^{0110}_{\alpha+1000,1} z^{1010}_{\alpha+0100,1} z^{1100}_{\alpha+0010,1}\right)^{-1}.
\end{equation}
Using \eqref{eqn:PtolemyToShapes}, the product of the first three terms equals
\begin{equation}\frac{c_{\alpha+2010,0}c_{\alpha+1101,0}}{c_{\alpha+2100,0}c_{\alpha+1011,0}} \left(-\frac{c_{\alpha+1200,0}c_{\alpha+0111,0}}{c_{\alpha+1101,0}c_{\alpha+0210,0}}\right) \frac{c_{\alpha+1011,0}c_{\alpha+0120,0}}{c_{\alpha+1020,0}c_{\alpha+0111,0}},
\end{equation}
which simplifies to
\begin{equation}\label{eq:Xcoordinate}
-\frac{c_{\alpha+2010,0} c_{\alpha+1200,0}c_{\alpha+0120,0}}{c_{\alpha+2100,0} c_{\alpha+0210,0} c_{\alpha+1020,0}}.
\end{equation}
Note that the ratio~\eqref{eq:Xcoordinate} only involves Ptolemy coordinates on the face 012 of $\Delta_0$ and that these are identified with the corresponding Ptolemy coordinates on $\Delta_1$. Hence, \eqref{eq:Xcoordinate} equals the corresponding expression for $z^{0110}_{\alpha+1000,1} z^{1010}_{\alpha+0100,1} z^{1100}_{\alpha+0010,1}$, so \eqref{eqn:proofFaceEqn} equals 1 as desired. The second statement follows from compatibility under reordering.
\end{proof}
\begin{corollary}
Theorem~\ref{thm:PtolemyYieldsShapes} holds for the face equations.\qed
\end{corollary}

\begin{remark}
The ratio \eqref{eq:Xcoordinate} will reappear in later sections as $X$-coordinates. They agree with the $X$-coordinates considered by Fock and Goncharov~\cite{FockGoncharov}. 
\end{remark}
