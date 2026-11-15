---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-020-53-ptolemy-assignments-for-general-concrete-tria
section_title: "Ptolemy assignments for general concrete triangulations"
section_number: 5.3
pages: 16-17
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.843
latex_coverage_ratio: 0.945
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:OrderAgnosticPtolemy}


For general concrete triangulations the Ptolemy coordinates on faces of different simplices must be identified by signs given by the face pairing permutations.
\begin{definition}\label{def:PtolemyAssignmentGeneral}
A Ptolemy assignment on $(M,\T)$ is a Ptolemy assignment for each simplex of $\T$ such that Ptolemy coordinates on identified faces are identified via the pullback of the permutation matrix. More precisely, if $f_0\subset\Delta_0$ is paired with $f_1\subset\Delta_1$ via the permutation $\sigma$, we require that 
\begin{equation}
(\sigma^*c_{\Delta_1})_{t_0}= (c_{\Delta_0})_{t_0}
\end{equation}
for each $t_0\in\Delta_n^3$ on face $f_0$. Equivalently, we require that $(c_{\Delta_0})_{t_0} = \det(I_{\sigma,\sigma(t_0)}) (c_{\Delta_1})_{\sigma(t_0)}$.
The variety of Ptolemy assignments is denoted by $P_n(\T)$.
\end{definition}

\begin{figure}[htb]
\begin{center}
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(270.99988,128.25317)
 \put(0,0){\includegraphics{figures_gen/PtolemyFaceIdentification_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(-0.554993,78.152906){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$\Delta_0$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(254.178707,80.349006){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{127.655896pt}
\textcolor{inkcol1}{\large{$\Delta_1$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(83.855035,105.343002){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{93.708112pt}
\textcolor{inkcol1}{\normalsize{$t_0\!\!=\!0031$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(121.852035,91.978402){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{90.982816pt}
\textcolor{inkcol1}{\normalsize{$t_1\!\!=\!0103$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
 
\end{center}
\caption{Identification of Ptolemy coordinates.}\label{fig:PtolemyIdentification}
\end{figure}

Note that if $\T$ is an ordered triangulation, all face pairings are order preserving, so all signs are positive, and the definition agrees with Definition~\ref{def:PtolemyAssignment}.

\begin{lemma}\label{lemma:reorderingPtolemys}
Let $\T'$ be the triangulation obtained from $\T$ by reordering the vertices of $\Delta_i$ by a permutation $\sigma_i$.
Then $\{\sigma_i^*c_{\Delta_i}\}$ is a Ptolemy cochain on $\T'$.
\end{lemma}

\begin{proof} We must prove that the coordinates on identified faces are identified via the pullback.
Let $c_{\Delta_i'}=\sigma_i^*c_{\Delta_i}$. Suppose $f_i\subset\Delta_i$ is glued to $f_j\subset\Delta_j$ by a permutation $\tau$. The corresponding face pairing involving $\Delta_i'$ and $\Delta_j'$ is then $\tau'=\sigma_j^{-1}\tau\sigma_i$. Since $\tau^*c_{\Delta_j}$ agrees with $c_{\Delta_i}$ on face $f_0$, it follows from the standard pullback properties that $\tau'^*c_{\Delta_j'}$ and $c_{\Delta_i'}$ also agree on $f_0$. This proves the result.
\end{proof}
\begin{corollary}
Up to canonical isomorphism, the Ptolemy variety only depends on the abstract triangulation.\qed
\end{corollary}
