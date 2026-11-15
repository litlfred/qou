---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-029-123-angle-structures-1-efficiency-and-pachner-mo
section_title: "Angle Structures, 1-efficiency and Pachner moves"
section_number: 12.3
pages: 44-45
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.968
latex_coverage_ratio: 0.732
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
A natural question is how are various properties of triangulations related 
by Pachner moves. Throughout this section, $\T_n$ will be a triangulation 
with $n$ tetrahedra, $f$ will be a face in this triangulation that 
identifies two distinct tetrahedra $t_{f,1}$ and $t_{f,2}$, and $\T_{n+1,f}$ 
will be the result of performing a 2-3 move along the face $f$. If we call 
the pairs of edges incident to $f$ in the bi-pyramid defined by $t_{f,1}$ 
and $t_{f,2}$, the \emph{belt of $f$}, then we can make the following 
observation that is well-known to the experts. We include it because it 
promotes a useful mentality and compares favourably to our discussion of 
1-efficiency and Pachner moves.

\begin{prop}
Let $\T_n$ be a triangulation with $n$ tetrahedra. With all notation as 
above, $\T_{n+1,f}$ admits a strict angle structure if and only if the set 
of angle structures contains a strict angle structure (resp. semi-angle 
structure) such that each of the three pairs of edges along the belt of 
$f$ have a sum in $(0,\pi)$ (resp. $[0,\pi]$).
\end{prop}

\begin{proof}
We only need to consider the tetrahedra in the bi-pyramid as the other 
angles will be unaffected by a 2-3 move. 

Considering Figure \ref{fig:twoThreeBoundary}, this problem reduces to a 
problem in the Euclidean plane: namely showing that the triangles incident 
to the vertices at the top and bottom of the bi-pyramid each split into 3 
triangles with angles in the desired range. However, the angles
around the vertex are all in $(0,\pi)$ (resp. $[0,\pi]$), so the vertex 
is embedded in the interior (resp. interior or a side). 

The other direction is obvious as an angle structure on $\T_{n+1,f}$ implies 
that all angles along the edges of the bi-pyramid are positive (resp. 
non-negative). 
\end{proof}
