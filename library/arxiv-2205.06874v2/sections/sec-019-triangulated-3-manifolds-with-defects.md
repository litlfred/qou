---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defects based on spherical fusion categories"
section_id: sec-019-triangulated-3-manifolds-with-defects
section_title: "Triangulated 3-manifolds with defects"
section_number: null
pages: 28-29
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
toc_source: outline
text_source: latex
latex_prose_ratio: 0.955
latex_coverage_ratio: 0.995
doc_brief: "State sum models with defects based on spherical fusion categories — We define a Turaev-Viro-Barrett-Westbury state sum model of triangulated 3-manifolds with surface, line and point defects."
---
\label{subsec:triangsec}


We consider a compact oriented 3d PL manifold  $M$ with (possibly empty) boundary $\partial M$. Defect structures are assigned to a compact  oriented embedded 2d PL submanifold $D\subset M$ with boundary  $\partial D\subset \partial M$ that is a finite sum of circles. The submanifold $D$ is equipped with a (finite, possibly empty) embedded PL graph $D^1$ with vertex set $D^0$  such that $D^1\cap \partial D\subset D^0$ contains only univalent vertices. 
Connected components of $M\setminus D$ are called {\bf regions} of $M$, 
connected  components of $D$  {\bf defect surfaces}, connected components of $D\setminus D^1$ {\bf defect areas}, connected components of $D^1\setminus D^0$ {\bf defect lines},  elements of $D^0\setminus \partial D$ {\bf defect vertices}. 


We equip each defect line and defect surface with an orientation. In pictures we indicate the orientation of a defect surface by a positive normal vector to the surface  and the orientation of a defect line by an arrow on the line.
Regions and  defect areas,   lines and  vertices are labeled with categorical data as follows, see Figure \ref{fig:dectet} for an illustration:
\begin{itemize}
\item Regions of $M$ are assigned spherical fusion categories.
\item Each oriented defect area is assigned a pair $(\mam,\theta)$ of a  $(\mac,\mad)$-bimodule category $\mam$ and a $(\mac,\mad)$-bimodule trace $\theta$ on $\mam$, where $\mac$ and $\mad$ are the spherical fusion categories for  the regions at the tip and the tail of the surface's normal vector.

Reversing the orientation of a defect area amounts to replacing  $\mam$ by the opposite bimodule category $\mam^\#$ from Example \ref{ex:dualcat}.

\item  Each oriented defect line is assigned a $(\mac,\mad)$-bimodule functor $F:\mam\to\man$, where $\mam$ and $\man$ are the $(\mac,\mad)$-bimodule categories 
to the left and to the right of the defect line, viewed in the direction of its orientation and from $\mac$.

Reversing the orientation of a defect line corresponds to replacing  $F:\mam\to\man$ by its left adjoint $F^l:\man\to\mam$. Reversing the orientation of the adjacent defect areas and the orientation of the line corresponds to replacing $\mam,\man$ by  $\mam^\#, \man^\#$ and  $F$ by  $F^\#:\mam^\#\to\man^\#$ from Example \ref{ex:modulefuncs}, 7.

\item A defect vertex whose incident defect lines are labeled by  $(\mac,\mad)$-bimodule functors is assigned a cyclic equivalence class of $(\mac,\mad)$-bimodule natural transformations between them, whose sources and targets are determined by the orientation and the cyclic ordering of the incident defect lines. 

\end{itemize}





Defect areas between two regions labeled both with  $\mac$ may be labeled with  $\mac$ as a bimodule category over itself  and with its trace as a bimodule trace. Such defect areas are called {\bf trivial defect areas}. Similarly, a defect line between two defect areas labeled  with  $(\mam,\theta)$ may be labeled with the identity functor  $F=\id_\mam:\mam\to\mam$ as a $(\mac,\mad)$-bimodule functor. Such defect lines are called {\bf trivial defect lines}. A defect vertex labeled with  $\id_F$ or with a counit $\epsilon^F$, $\epsilon'^F$ or unit $\eta^F, \eta'^F$ of the adjunction $F^l\vdash F$ is called a {\bf trivial defect vertex}. 

A compact oriented 3d PL manifold $M$, possibly with boundary, together with  defects  $D^0\subset D^1\subset D$ is called a {\bf defect 3-manifold}. A defect 3-manifold together with a labeling of the defects with
categorical data is called a {\bf 3-manifold with defect data}.

To define a state sum model for a 3-manifold with defect data, we require a triangulation  of $M$. It must be sufficiently refined to resolve all defect surfaces and must intersect the defect surfaces generically.

\begin{definition} \label{def:gentrans} Let $M$ be a defect 3-manifold and $T$ a triangulation of $M$. 
\begin{compactenum}
\item A triangle in $T$ is called {\bf transversal}, if
\begin{compactitem}
\item each of its sides contains at most one point on a defect surface,
\item its intersection with each defect surface is empty or a line with endpoints on its sides,
\end{compactitem}

and {\bf generic} if
\begin{compactitem}
\item none of its vertices is on a defect surface,
\item none of its sides intersects a defect line, 
\item it does not contain a defect vertex.\\[-2ex]
\end{compactitem}
\item A tetrahedron in $T$ is transversal, if all  of its faces  are transversal and 
 its intersection with each defect surface is either empty or a polygon with vertices on its edges. It is  generic, if all  its faces are generic. \\[-2ex]

\item The  triangulation $T$ is transversal  or  generic if all of its tetrahedra are transversal or generic.
\end{compactenum}
\end{definition}

It follows directly that a generic transversal tetrahedron either  intersects a single defect surface in three edges incident at a common vertex, as in Figure \ref{fig:dectet} (a), 
 intersects a defect surface in two pairs of opposite edges, as  in Figure \ref{fig:dectet} (b), or 
does not  intersect any defect surface at all.

Any transversal triangulation can be deformed into a generic one by slightly perturbing the defect surfaces and 
the defect graphs. By taking  derived subdivisions, see Rourke and Sanderson \cite[Ch.~2]{RS}, and perturbing  defect surfaces and defect graphs one can transform any triangulation into one that is both transversal and generic.  In particular,  one can achieve that the defect manifold is  a subcomplex of  a first derived subdivision.  



We orient the edges of a generic transversal triangulation in such a way that 
\begin{compactenum}[(i)]
\item   edges in each triangle do not form a cycle,
\item  in each tetrahedron, the edges that intersect a defect surface are  oriented parallel to its positive normal vector.
\end{compactenum}
This does not restrict generality.  Condition (i) can be achieved by numbering the vertices of the triangulation and orienting each edge in such a way that it points from the vertex with the smaller number to the vertex with the bigger number. This is possible because any PL triangulation is determined by an underlying combinatorial simplicial complex, see for instance 
\cite[Th.~2.11]{RS}. 





Given a generic transversal  triangulation that satisfies (i),  reverse the orientation of each edge that intersects a defect surface and is oriented against its positive normal vector.  Each triangle that intersects a defect surface intersects it in exactly two edges.  After this orientation reversal these two edges are  either both incoming or  outgoing at a common vertex and hence cannot be part of a cycle.  The resulting triangulation satisfies (i) and (ii). 


A defect 3-manifold  together with an oriented triangulation is called a {\bf  triangulated defect 3-manifold}. A 3-manifold with defect data together with an oriented triangulation is called a {\bf triangulated 3-manifold with defect data}.
They are called {\bf transversal} or {\bf generic} if the triangulation is transversal or generic. 



\begin{figure} 
\centering
\def\svgwidth{.75\columnwidth}

\caption{Generic transversal tetrahedra that intersect a defect surface. \newline
(a) labeling with  $F:\mathcal P\to\mam$, $G:\man\to\mam$, $H:\map\to\man$ and  $\nu:F\Rightarrow GH$,\newline
(b) labeling with  $F:\maq\to \map$, $G:\man\to\maq$, $H:\mam\to\map$, $K:\man\to\mam$ and  $\nu: FG\Rightarrow HK$.
}
\label{fig:dectet}
\end{figure}
