---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-004-31-gluing-equations
section_title: "Gluing equations"
section_number: 3.1
pages: 5-6
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.918
latex_coverage_ratio: 0.934
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{gluing_eqn_sect}

We now briefly describe how to encode the combinatorics of a triangulation 
contained in Thurston's gluing equations (compare  \cite[Chapter 4]{Th}), 
while also including notation for normal disks in a tetrahedron. 
First, in each tetrahedron there are three pairs of opposite edges, which 
are disjoint from the three quadrilateral disks from normal surface theory. 
We label these quadrilaterals by the pair of edges they face, as in 
Regina \cite{regina}; Figure \ref{fig:edgesAndQuad} shows the quads
$q_A=q_{A:01:23}$, $q_A'=q_{A:02:13}$, $q_A''=q_{A:03:12}$ in a tetrahedron 
labelled $A$. As our discussion unfolds the quadrilaterals will be the 
focus, however we also provide a labelling for the  triangular disks for 
completeness: $t_{A:j}$ refers the the triangle in tetrahedron $A$ that 
cuts off vertex $j$.
 
 
 
\begin{figure}[htpb]



\includegraphics[width=0.25\textwidth]{figures/qa0123}\hspace{0.5cm}
\includegraphics[width=0.25\textwidth]{figures/qa0213}\hspace{0.5cm}
\includegraphics[width=0.25\textwidth]{figures/qa0312}
\label{fig:qa0312}
\caption{The labelling of the 3 quadrilateral disk types of tetrahedron $A$. 
Left: $q_A=q_{A:01:23}$, centre: $q_A'=q_{A:02:13}$, right: $q_A''=q_{A:03:12}$.}
\label{fig:edgesAndQuad}
\end{figure}

Central to the construction of Thurston's gluing equations is the 
observation that edges in each tetrahedron form equivalence classes in 
the triangulation. In Thurston's notes, a set of logarithmic equations 
is associated to the $n$ edge classes of the triangulation. First, we 
associate a complex tetrahedral parameter $z_j$ to the $01,23$ edges in 
tetrahedron $j$, $z_j'=\frac{1}{1-z_j}$ to the $02,13$ edges and 
$z_j''=\frac{z_j-1}{z_j}$ to the $03,12$ edges. 

Then we can build the following {\em edge equations}:
\be
\label{log_edge_eqns}
\sum_j \left(a_{i,j} \log(z_j )+ b_{i,j} \log(z_j' )
+ c_{i,j} \log(z_j'')\right)=0+2\pi \sqrt{-1} 
\mbox{ for } i\in\{1,\ldots, n\},
\ee
where $a_{i,j},b_{i,j},c_{i,j}$ record the number of times the edges 
opposite quads $q_j, q_j', q_j''$ of tetrahedron $j$ appear in the $i$th 
edge class. (Our convention is that 
$\arg(z_j), \arg(z_j'), \arg(z_j'')  \in (-\pi,\pi]$.)

Note that the tetrahedral parameters also satisfy the relation 
\be
\label{log_tet_eqns}
\log(z_j )+\log(z_j') + \log(z_j'')= \pi \sqrt{-1}.
\ee

We can also build $2r$ {\em cusp equations} using the same tetrahedral 
parameters: 
\be
\label{log_cusp_eqns}
\sum_j \left(a_{i,j} \log(z_j )
+ b_{i,j} \log(z_j' )+ c_{i,j} \log(z_j'')\right)
=0+\pi \sqrt{-1} \mbox{ for } i\in\{n+1,\ldots, n+2r\},
\ee
however here $a_{i,j},b_{i,j},c_{i,j}$ record the number of times a 
peripheral curve winds anti-clockwise (or minus the number of clockwise 
times) around the edges opposite the quads  $q_j, q_j', q_j''$ in 
tetrahedron $j$. 

The coefficients in the edge and cusp equations define a 
$(n+2r) \times 3n$ \emph{gluing matrix} $[ a_{i,j} ~ b_{i,j} ~ c_{i,j} ]$, 
which is also given by the {\tt gluing\_equations()} function in 
SnapPy \cite{SnapPy}.

Throughout the paper, we will write $E_i$ for the vector of coefficients 
in the $i$th edge equation, and we will also label the cusp equation 
coefficients coming from the $k$th cusp by $M_k$ and $L_k$ and the 
corresponding curves $\mu_k$ and $\lambda_k$ where it proves convenient.
