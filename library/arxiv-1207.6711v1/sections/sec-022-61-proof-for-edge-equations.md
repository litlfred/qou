---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-022-61-proof-for-edge-equations
section_title: "Proof for edge equations"
section_number: 6.1
pages: 18-19
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.804
latex_coverage_ratio: 0.975
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{subsection:ProofForEdgeEqn}
Let $K$ be the space defined by cyclically gluing together $k$ simplices $\Delta_0,\dots,\Delta_{k-1}$ along the common edge $01$, pairing all faces via the permutation $(23)$, see Figure~\ref{fig:EdgeLocal}. 

\begin{figure}[htb]
\begin{center}
\begin{minipage}[b]{0.45\textwidth}
\begin{center}
\scalebox{0.75}{
\includegraphics{figures_gen/LocalModelEdgeGluing_included}}
\end{center}
\end{minipage}
\hfill
\begin{minipage}[b]{0.45\textwidth}
\begin{center}
\scalebox{0.5}{
\includegraphics{figures_gen/LocalModelFaceGluing_included}}
\end{center}
\end{minipage}
\\
\begin{minipage}[t]{0.45\textwidth}
\caption{Local model near an edge point.}\label{fig:EdgeLocal}
\end{minipage}
\hfill
\begin{minipage}[t]{0.45\textwidth}
\caption{Local model near a face point.}\label{fig:FaceLocal}
\end{minipage}
\end{center}
\end{figure}

\begin{lemma}\label{lemma:edgelocalmodel}
If $\{c_{\Delta_i}\}$ is a Ptolemy assignment on $K$, the assignments $\{\mu(c_{\Delta_i})\}$ satisfy the edge equations for all integral points on the edge $01$. The same holds for the complex $K'$ obtained by reordering the vertices of the simplices of $K$.
\end{lemma}
\begin{proof}
An integral point $p$ on $01$ has representatives $(t,\Delta_i)$ with $t=(t_0,t_1,0,0)$ being fixed. The left hand side of the edge equation for $p$ is given by
\begin{equation}\label{eq:edgeequationforK}
z^{1100}_{s,0}z^{1100}_{s,1}\cdots z^{1100}_{s,k-1}\qquad\mbox{with}~s=(t_0-1,t_1-1,0,0),
\end{equation}
which expands to
$$\frac{c_{s+1001,0}c_{s+0110,0}}{c_{s+1010,0}c_{s+0101,0}}\frac{c_{s+1001,1}c_{s+0110,1}}{c_{s+1010,1}c_{s+0101,1}}\cdots \frac{c_{s+1001,k-1}c_{s+0110,k-1}}{c_{s+1010,k-1}c_{s+0101,k-1}}.$$
Since the Ptolemy coordinates $c_{1001,i}=c_{1010,i+1}$ and $c_{0101,i}=c_{0110,i+1}$ on two adjacent simplices are identified, all terms cancel. Hence, \eqref{eq:edgeequationforK} equals $1$ as desired. The corresponding result for $K'$ follows from compatibility under reordering (Lemmas~\ref{lemma:ReorderCompatibility}, \ref{lemma:reorderingshapes} and \ref{lemma:reorderingPtolemys}).

\end{proof}


\begin{corollary} Theorem~\ref{thm:PtolemyYieldsShapes} holds for the edge equations.
\end{corollary}
\begin{proof}
The complex $K$ models a neighborhood around an edge $e$ of $\T$ in the sense that there is a simplical map $\pi\colon K\to\widehat{M}$ mapping $01$ to $e$, which is unique up to changing the orientation of $K$ and cyclically relabeling the simplices. By compatibility under reordering, we may assume that $\pi$ is order preserving. A Ptolemy assignment on $\T$ pulls back to a Ptolemy assignment on $K$, such that edge equations on $01$ descend to the corresponding edge equations on $e$. The result now follows from Lemma~\ref{lemma:edgelocalmodel}.  




\end{proof}
