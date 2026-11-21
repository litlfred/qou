---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-030-91-truncated-and-doubly-truncated-simplices
section_title: "Truncated and doubly truncated simplices"
section_number: 9.1
pages: 28-29
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.873
latex_coverage_ratio: 0.933
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\begin{definition}
A \emph{truncated simplex} is a polyhedron obtained from a simplex by truncating its vertices. A \emph{doubly truncated simplex} is a polyhedron obtained from a simplex by first truncating the vertices and then truncating the edges.
\end{definition}
We refer to the edges of a truncated simplex as \emph{long} and \emph{short} edges, and the edges of a doubly truncated simplex as \emph{long}, \emph{middle}, and \emph{short} edges.

Note that a triangulation of $M$ induces a decomposition of $M$ into truncated simplices, as well as a decomposition of $M$ into doubly truncated simplices and \emph{prisms}. 
An \emph{ordering} of a simplex induces an orientation of the edges of the corresponding truncated simplex. Similarly, an \emph{orientation} of a simplex induces orientations of the edges of the corresponding doubly truncated simplex. Note that an ordering is required to obtain natural edge orientations on a truncated simplex.

\begin{figure}[htb]
\begin{center}
\begin{minipage}[b]{0.34\textwidth}
\scalebox{0.9}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(231.02042,183.89163)
 \put(0,0){\includegraphics{figures_gen/TruncatedCocycle_included}}
 \end{picture}
\endgroup
}
\end{minipage}
\hfill
\begin{minipage}[b]{0.34\textwidth}
\scalebox{0.9}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(231.02043,183.89163)
 \put(0,0){\includegraphics{figures_gen/doublyTruncatedCocycle_included}}

\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(88.33367,179.337569){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{123.948104pt}
\textcolor{inkcol1}{\normalsize{$\beta^{132}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(142.93021,93.552469){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{123.948104pt}
\textcolor{inkcol1}{\normalsize{$\alpha^{123}$}}\\
\end{minipage}}}}}


\definecolor{inkcol1}{rgb}{0.0,0.0,0.0}
   \put(38.250965,156.123629){\rotatebox{360.0}{\makebox(0,0)[tl]{\strut{}{
    \begin{minipage}[h]{123.948104pt}
\textcolor{inkcol1}{\normalsize{$\gamma^{123}$}}\\
\end{minipage}}}}}

 \end{picture}
\endgroup
}
\end{minipage}
\hfill
\begin{minipage}[b]{0.3\textwidth}
\qquad
\scalebox{0.9}{
\begingroup
 \setlength{\unitlength}{0.8pt}
 \begin{picture}(69.039253,183.89163)
 \put(0,0){\includegraphics{figures_gen/doublyTruncatedCocycle_Prism_included}}
 \end{picture}
\endgroup
}
\end{minipage}\\ \vspace{-0.4cm}
\begin{minipage}[t]{0.34\textwidth}
\caption{A truncated simplex. Edge orientations induced by the vertex ordering.}\label{fig:Truncated}
\end{minipage}
\begin{minipage}[t]{0.34\textwidth}
\caption{A doubly truncated simplex. Edge orientations induced by the orientation.}\label{fig:DoublyTruncated} 
\end{minipage}
\begin{minipage}[t]{0.3\textwidth}
\caption{A prism.}\label{fig:Prism}
\end{minipage}
\hfill
\end{center}
\end{figure}




 


\begin{remark}
We can view a doubly truncated simplex as the permutohedron of $S_4$. We can embed it in a standard simplex $\Delta^3_1$ as the convex hull of $\frac{1}{11}\Delta^3_{11}(\{0,1,3,7\})$, the set $\frac{1}{11}\Delta^3_{11}(\{0,1,3,7\})$ being the vertex set. With this embedding, the long edges are twice as long as the middle edges, which are again twice as long as the short edges (which have length $\frac{\sqrt{2}}{11}$). Similarly, we may view a truncated simplex as the convex hull of $\frac{1}{5}\Delta^3_{5}(\{0,1,4\})$.
\end{remark}
