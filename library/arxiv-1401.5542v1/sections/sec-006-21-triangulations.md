---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-006-21-triangulations
section_title: "Triangulations"
section_number: 2.1
pages: 6-7
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.959
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
Let $M$ be a compact oriented $3$-manifold with (possibly empty) boundary. We refer to the boundary components as \emph{cusps} (although they may not be tori). Let $\widehat M$ be the space obtained from $M$ by collapsing each boundary component to a point.
\begin{definition}
A (concrete) \emph{triangulation} of $M$ is an identification of $\widehat M$ with a space obtained from a collection of simplices by gluing together pairs of faces by affine homeomorphisms. For each simplex $\Delta$ of $\T$ we fix an identification of $\Delta$ with a standard simplex.  
\end{definition}
\begin{remark}
By drilling out disjoint balls if necessary (this does not change the fundamental group), we may assume that the triangulation of $M$ is \emph{ideal}, i.e.~that each $0$-cell corresponds to a boundary-component of $M$. For example, we regard a triangulation of a closed manifold as an ideal triangulation of a manifold with boundary a union of spheres.
\end{remark}

\begin{definition}

A triangulation is \emph{oriented} if the identifications with standard simplices are orientation preserving.
\end{definition}
\begin{remark}
All of the triangulations in the SnapPy censuses \texttt{OrientableCuspedCensus}, \texttt{LinkExteriors} and \texttt{HTLinkExteriors}~\cite{SnapPy} are oriented. Unless otherwise specified we shall assume that our triangulations are oriented.
\end{remark}


A triangulation gives rise to a triangulation of $M$ by truncated simplices, and to a triangulation of $\Mtildehat$.
