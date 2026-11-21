---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-009-61-construction-of-spun-normal-surfaces
section_title: "Construction of spun normal surfaces"
section_number: 6.1
pages: 11-13
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.925
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{spun_normal_construction}

Next we give a brief exposition of the construction of a spun normal surface
from solutions to the Q-matching equations following \cite{DuGa} and 
\cite{Ti}. (This approach goes back to lectures of W. Thurston and was used 
by J. Weeks in SnapPea.)

For a spun normal surface, there is a fixed pattern of normal arcs in each 
ideal triangle, consisting  of three infinite families of parallel arcs 
(one at each corner). Further there is a well-defined ``middle'' interval 
in each edge of the triangle separating two of these families. The union 
of these three intervals with 3 normal arcs form a hexagon, as described 
in \cite{DuGa}.

\begin{center}
\begin{figure}[htpb]
\includegraphics[width=0.2\textwidth]{figures/hexagon}

\caption{\label{fig:hexagon} The hexagon $\mathcal{H}$ has three arcs 
which are normal arcs and three arcs (labelled by double lines) that 
are not normal arcs and represent the "middle" intervals.}
\end{figure}
\end{center}

Next consider the arc pattern on the boundary of a tetrahedron: 
Along each edge,  there is an integer ``shear'' or ``shift'' parameter 
which specifies how the adjacent arc patterns fit together, and we choose 
a sign convention as shown in Figure \ref{fig:shear} below (as viewed 
from outside the tetrahedron).

\begin{center}
\begin{figure}[htpb]
\includegraphics[width=0.35\textwidth]{figures/shear}

\caption{\label{fig:shear} A shift of -3 from $\mathcal{H}_r$ to 
$\mathcal{H}_l$. (In general, shearing parameters measure the offset 
from right to left as viewed from outside the tetrahedron.)}
\end{figure}
\end{center}

We require that  the sum of shear parameters along the three edges meeting 
at a vertex is zero. This means that there is an infinite family of 
parallel normal triangles at each tetrahedron vertex, and also implies 
that the shear parameters on opposite edges are equal. With our sign 
convention, quad coordinates $(a,b,c)$ for quad types 
$q_{A:01:23},q_{A:02:13},q_{A:03:12}$ in a tetrahedron correspond to 
shear parameters $(c-b,a-c,b-a)$ along the edges of the tetrahedron facing 
$q_{A:01:23},q_{A:02:13},q_{A:03:12}$. (Figure \ref{fig:shearing_tet} below shows 
the case of two quads of type $q_{A:01:23}$, separating vertices 0, 1 from 
vertices 2, 3.)

\begin{figure}[htpb]
\begin{center}
\includegraphics[width=0.3\textwidth]{figures/shear_tet} \hspace{1cm}
\includegraphics[width=0.3\textwidth]{figures/tet_shearing_change}

\end{center}
\caption{\label{fig:shearing_tet} With two quads at the bottom edge of 
the left hexagon and top edge of the right hexagon, we have a shear of +2 
along the edge between. The right figure gives all of the shearing 
coordinates on the tetrahedron.} 
\end{figure}

Now there is a unique way to glue together the arc patterns in two 
tetrahedra meeting along a common face, as the middle intervals in the faces 
must match up. The arc patterns from all the tetrahedra in the triangulation 
then fit together consistently (without any shearing) around an edge class 
if and only the sum of the shear parameters over all edges in the edge 
class vanishes. These conditions are precisely the Q-matching equations.
