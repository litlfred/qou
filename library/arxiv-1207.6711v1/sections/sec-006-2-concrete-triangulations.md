---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-006-2-concrete-triangulations
section_title: "Concrete triangulations"
section_number: 2
pages: 6-7
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
toc_source: outline
text_source: latex
latex_prose_ratio: 0.952
latex_coverage_ratio: 0.984
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
\label{sec:TriangulationSection}



In all of the following $M$ denotes a compact, oriented $3$-manifold with (possibly empty) boundary. Let $\widehat M$ be the space obtained from $M$ by collapsing each boundary component of $M$ to a point. An \emph{ordered simplex} is a simplex together with an ordering of its vertices.

\begin{definition}
An \emph{abstract triangulation} $\mathcal{T}$ of $M$ is an identification of $\widehat{M}$ with a space obtained from a finite collection of $3$-simplices by gluing together pairs of faces via \emph{face-pairings}, i.e.~affine homeomorphisms. A \emph{concrete triangulation} $\mathcal{T}$ of $M$ is an abstract triangulation together with a fixed identification of each $3$-simplex with a standard ordered $3$-simplex.
\end{definition}

The advantage of a concrete triangulation is that each simplex inherits a vertex ordering from the standard simplex. This extra datum gives us a concrete indexing scheme for the vertices and edges and allows us to concretely write down defining equations for the gluing equation variety and the Ptolemy variety. An abstract triangulation can be thought of as an equivalence class of concrete triangulations under reordering. As we shall see, a reordering changes the varieties by canonical isomorphisms. Hence, they only depend on the abstract triangulation.

Note that the vertex ordering of each simplex induces an orientation, which may or may not agree with the orientation inherited from $M$.

\begin{definition}
A concrete triangulation of $M$ is an \emph{oriented triangulation} if the orientation of each simplex agrees with the orientation of $M$. A concrete triangulation of $M$ is an \emph{ordered triangulation} if the face-pairings are order-preserving. An abstract triangulation is {\it orderable} if it supports an ordered triangulation.
\end{definition}




As we shall see, the shape coordinates are most conveniently expressed in terms of \emph{oriented triangulations}, whereas the Ptolemy coordinates are most conveniently expressed in terms of \emph{ordered triangulations}. Note that since $M$ is assumed to be oriented, one can always order the vertices making the triangulation oriented.



 
\begin{remark} 
One can always obtain an orderable triangulations by performing a sequence of $2$-$3$ moves and $1$-$4$ moves. One can do this systematically in such a way that the total number of simplices is increased by at worst a factor of $6$. Alternatively, a barycentric subdivision always provides an ordered triangulation by ordering vertices by codimension.  
\end{remark}

\begin{figure}[htpb]
\centering
\begin{minipage}[c]{0.49\textwidth}
\includegraphics[width=8.4cm]{figures_gen/Figure8ordered_included}
\captionsetup{width=10cm}
\caption{An ordered, but not oriented triangulation of the figure $8$ knot. No vertex ordering exists making the triangulation both ordered and oriented.}\label{fig:Fig8Ordered}
\end{minipage}	
\begin{minipage}[c]{0.49\textwidth}
\includegraphics[width=8.4cm]{figures_gen/Figure8Sister_included}
\captionsetup{width=10cm}
\caption{An oriented, but not ordered triangulation of the figure $8$ knot sister. The underlying abstract triangulation is unorderable.}
\end{minipage}					

\end{figure}
