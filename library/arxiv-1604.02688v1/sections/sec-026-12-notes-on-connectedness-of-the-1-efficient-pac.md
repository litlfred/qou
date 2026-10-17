---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-026-12-notes-on-connectedness-of-the-1-efficient-pac
section_title: "Notes on connectedness of the 1-efficient Pachner Graph"
section_number: 12
pages: 39-41
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.972
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{PachnerGraph}

In this section we study the \emph{Pachner graph} for a compact orientable 
3-manifold $M$ with non-empty boundary consisting of tori. 
This is a graph where each vertex corresponds to an ideal triangulation 
(up to the equivalence of relabelling) of the manifold $M$,
 with an edge connecting two vertices if their corresponding triangulations 
can be obtained from one another via 2-3 or 3-2 
 Pachner moves (as shown in Figures \ref{fig:twoThreeBipyramid} and 
\ref{fig:twoThreeBoundary}.)
 We give some general results, then describe a census of all ideal 
triangulations with at most 6 tetrahedra which provides 
a number of examples with interesting properties. 
 
\begin{figure}[htpb]
\centering
\includegraphics[width=0.6\textwidth]{figures/twoThreeLabels}

\caption{\label{fig:twoThreeBipyramid} A 2-3 move on labelled tetrahedra. 
As the black square indicates, edges $A12$ and $B13$ are identified with $C23$}
\end{figure}

\begin{figure}[htpb]
\centering
\includegraphics[width=0.8\textwidth]{figures/twoThreeTriangles}

\caption{\label{fig:twoThreeBoundary}The effect of the 2-3 move on the 
boundary triangles.}
\end{figure}

Throughout the section, we will use Burton's isomorphism signature 
notation \cite{BurtonIsoSig} to identify triangulations. 
Interested readers can replicate the results of this section by inputing 
these signatures into Regina to construct the relevant triangulations. 
Readers new to this concept will find it helpful to know that if the first 
letter of the signature (of those used in this paper) is the 
$n$-th letter of the alphabet, then the corresponding triangulation is 
comprised of $n-1$ tetrahedra. 

As mentioned in the introduction, the 
the Pachner graph of a $3$-manifold with non-empty boundary is connected, and so it is 
interesting to consider basic properties of subgraphs of this graph: 
number of vertices, connectedness, etc. For example,  we say the 
\emph{geometric Pachner graph} is the subgraph of ``geometric'' 
triangulations such that Thurston's gluing equations have a solution where each 
tetrahedral shape has positive imaginary part.

It has been recently shown that the figure eight knot complement admits 
infinitely many geometric triangulations, however the geometric subgraph 
of the Pachner graph is disconnected 
(see \cite[Theorem 1.1 and Remark 3.3]{DaddDuan}). 

One can also define the \emph{1-efficient Pachner graph} as the subgraph 
of the Pachner graph containing only 1-efficient triangulations and the 
edges between them. 

Before discussing the 1-efficient Pachner graph, we mention that our 
notation (used here and in the accompanying code) for Seifert fibred 
spaces with non-empty boundary, is consistent with Hatcher \cite{Hat}. 
Namely, a Seifert fibre space over the surface $F$ with exceptional fibres 
given by the parameters $\{(a_i,b_i)\}_{i=1} ^k$ (with $a_i>b_i>0$ if $F$ is 
punctured) will be denoted by $SFS[F(a_1,b_1)...(a_k,b_k)]$. 

First, we point out that for many 3-manifolds 
the 1-efficient Pachner graph is infinite. Although this is presumably 
known to the experts, we include it for the sake of completeness. 

\begin{prop}
Let $M$ be an cusped irreducible, atoroidal orientable 3-manifold other 
then the solid torus  $S^1\times D^2$. Then $M$ admits infinitely many 
1-efficient triangulations.
\end{prop}

The key idea for this proof is to exhibit ideal triangulations that 
support a {\em taut angle structure}, i.e.
a semi-angle structure where all angles are either 0 or $\pi$. 
(A semi-angle structure is an assignment of non-negative angles to the 
edges in the ideal tetrahedra, so that the angle sum at each ideal vertex 
in such a tetrahedron is $\pi$.)
Also, in \cite[Theorem 1]{La1}, Lackenby shows that an-annular cusped 
manifolds  admit taut ideal triangulations,
 which give such a  taut angle structure.
Given the hypotheses of the Proposition, we point out that an-annular is 
shorthand for Seifert fibre spaces over the disk 
over than $S^1\times D^2$ or $SFS[D(2,1)(2,1)]$, and hyperbolic manifolds. 

\begin{proof}
If $M$ is hyperbolic or a Seifert fibre space over the disk (other than 
$S^1\times D^2$ or $SFS[D(2,1)(2,1)]$), then by \cite[Theorem 1]{La1}, 
$M$ admits a taut ideal triangulation, say with $n$ tetrahedra. 
In this triangulation, about any edge we can find two faces of the 
triangulation incident 
to that edge which (in an open neighbourhood of the edge) separate the 
two angles labelled by $\pi$. Performing a 0-2 move along these two 
faces produces a new triangulation with $n+2$ tetrahedra. To see that 
this triangulation supports a taut angle structure, label each edge in the 
new edge class of degree 2 by $\pi$, the opposite edges in the tetrahedron 
by $\pi$, and the remaining edges $0$. As this is a semi-angle 
structure, this new triangulation is 1-efficient since $M$ is atoroidal 
(see \cite[Theorem 2.6]{KR2}). 

If $M$ is Seifert fibred over an annulus with exactly one exceptional 
fibre, then $M$ is fibred over the circle with fibre a surface of negative 
Euler characteristic. Therefore, $M$ admits a layered triangulation 
obtained from expressing the monodromy of its fibration in terms of edge 
flips on an ideal triangulation of the fibre (see for example 
\cite[Section 2]{La1}). Using this ideal layered triangulation, we again 
obtain a taut angle structure and complete the proof in the same manner 
as above. 
\end{proof}

The following remark uses a dual notion to 1-efficiency, introduced by 
Garoufalidis \cite{Gar}, to obtain a similar result. Let $\T$ be an ideal 
triangulation with $n$ tetrahedra and $\Lambda=\{\lambda_i\}_{i=1}^{3n}$ a 
set of $3^n$ generalised angle structures. Then $\Lambda$ is a 
\emph{index structure} on $\T$ if for each $Q=(Q_1, ..., Q_n)$ where $Q_j$ 
is a choice of quadrilateral type in tetrahedron $j$,  there exist 
$\lambda_i$ such that for all $j$ the edges opposite $Q_j$ in $\T$ have 
positive angles in $\lambda_i$. This is an obstruction to having embedded 
surfaces of non-negative Euler characteristic, and in fact it is known to 
be equivalent to $\T$ being 1-efficient by \cite[Theorem 1.2]{GHRS}. 

\begin{rmk}
An ideal triangulation of a solid torus will not admit a taut angle 
structure (by \cite{KR2}, the existence of an embedded generalised 
normal torus in a solid torus is an obstruction to existence of a taut 
angle structure). Nevertheless, an analogous method can be used to 
obtain infinitely many 1-efficient triangulations of the solid torus. For 
example, the triangulation `dLQacccbnbb' has a gluing matrix: 
$$
\begin{pmatrix} 
1& 0& 0& 0& 0& 0& 0& 0& 0\\
1& 2& 2& 1& 2& 2& 1& 2& 2\\
0& 0& 0& 1& 0& 0& 1& 0& 0\\
\end{pmatrix}
$$
and so $\{(2\pi, \beta_0, -\pi- \beta_0, \pi, \beta_1, 
-\beta_1, \pi, \beta_2, -\beta_2)\mid \beta_0,\beta_1,\beta_2\in \R \}$ 
is a subset of the generalised angle structures on `dLQacccbnbb'. 
Furthermore, one has the freedom to adjust these parameters to find an 
index structure. In fact, after performing a 0-2 move along the two faces 
incident to the degree two edge, we see that a new index structure is 
obtained since we can obtain new generalised angle structures by just 
introducing two new tetrahedra subject to same constraint as the last two 
tetrahedra above, i.e. the angles are $(\pi, \beta_j, -\beta_j)$. 
Furthermore, one can then perform 0-2 moves along the faces incident to 
any degree 2 edge in the resulting triangulations to obtain more 
1-efficient triangulations, and so by an inductive argument there are 
infinitely many 1-efficient triangulations of the solid torus.
\end{rmk}
