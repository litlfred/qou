---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-007-5-dependence-on-the-choice-of-triangulation
section_title: "Dependence on the choice of triangulation"
section_number: 5
pages: 8-10
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 0.966
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Physics predicts that the 3D-index as defined above should give a 
{\em topological invariant} of the underlying manifold $M$, but this is not 
known in general.  

The first difficulty is that the summation in (\ref{JD_index_eq}) need not 
even converge (as a formal power series) for all ideal triangulations $\tri$. 
But the good triangulations can be characterised using normal surface theory.

Given a triangulation $\tri$ of a 3-manifold $M$, an embedded surface 
$S \subset M$ is a {\em normal surface} if it intersects each tetrahedron 
in a finite collection of disjoint normal quadrilaterals (`quads') and 
triangles as shown in Figure \ref{fig:normal_disk_types}. In each 
tetrahedron there are 4 types of normal triangles and 3 types of normal quads.

\begin{center}
\begin{figure}[htpb]
\includegraphics[width=0.45\textwidth]{figures/normal_disk_types}
\caption{\label{fig:normal_disk_types} The four types of triangular disks 
(left) and one of the three types of quadrilateral disks (right).}
\end{figure}
\end{center}

Embedded normal surfaces were introduced by Kneser \cite{Kn} and developed 
by Haken \cite{Ha1,Ha2} to create a normal surface theory which has played 
a key role in the development of algorithmic 3-manifold topology.  Haken 
observed that (not necessarily embedded) closed normal surfaces are 
parametrised by vectors of quad numbers and triangle numbers in $\Z^{7n}$ 
satisfying linear {\em matching equations}. Tollefson \cite{To} 
showed that the quad numbers are enough to determine a closed normal surface 
up to multiples of the boundary tori. These give vectors in $\Z^{3n}$ 
satisfying linear {\em$Q$-matching equations}.

\begin{defn}\cite{JR, KR2}
An ideal triangulation $\tri$ is \emph{1-efficient} if 
\begin{enumerate}
\item[(0)] it contains no embedded normal 2-spheres or projective planes, and
\item[(1)] the only embedded normal tori or Klein bottles are vertex-linking.  
\end{enumerate}
\end{defn}

\begin{thm}\cite[Theorem 1.2]{GHRS}
\label{index_structure_iff_1-efficient}
The sum defining 
$I_{\CT}([\gamma])$ converges for all $[\gamma] \in H_1(\bd M; \Z)$ 
if and only if the sum $I_{\CT}({\bf 0})$ converges 
if and only if the ideal  triangulation $\CT$ is 1-efficient.
\end{thm}

We will outline a new, more direct proof of this result in Section 
\ref{sect:index_via_normal_surfaces} below, by rewriting the index as a 
sum of contributions from normal surfaces.

\medskip
It is shown in \cite{GHRS}  that 1-efficient triangulations exist for many 
important classes of cusped 3-manifolds including all hyperbolic manifolds 
and small Seifert fibre spaces.  But they cannot exist for 3-manifolds
containing (embedded) essential spheres, projective planes, tori or Klein 
bottles which are not boundary parallel. 

\medskip
It is known by the work of Matveev and Piergallini (see \cite{Ma1, Ma2, Pi}) 
that any two triangulations $\CT, \CT'$ (with at least 2 tetrahedra) of a 
given closed 3-manifold $M$ can be connected by a sequence of 2-3 and 3-2 
Pachner moves. We can also consider 0-2 and 2-0 moves on triangulations 
as shown in Figure \ref{2-3 and 0-2 moves}.

\begin{figure}[htpb]
\centering
\subfloat[The 2-3 and 3-2 moves.]{
\labellist
\small\hair 2pt
\pinlabel 2-3 at 139 84
\pinlabel 3-2 at 139 44
\endlabellist
\includegraphics[width=0.44\textwidth]{figures/2-3_moves}
\label{2-3}}
\qquad
\subfloat[The 0-2 and 2-0 moves.]{
\labellist
\small\hair 2pt
\pinlabel 0-2 at 109 84
\pinlabel 2-0 at 109 44
\endlabellist
\includegraphics[width=0.34\textwidth]{figures/0-2_moves}
\label{0-2}}
\caption{Moves on (topological) triangulations.}
\label{2-3 and 0-2 moves}
\end{figure}

The pentagon identity for the tetrahedral index gives the following key 
property of the 3D-index:

\begin{thm} [{\cite[\sect6]{Gar},\cite[Theorem 1.1]{GHRS}}]
\label{thm.00}
If $\CT$ and $\CT'$ are related by a 2-3 move and both are 1-efficient, 
then $I_{\CT}=I_{\CT'}$.
\end{thm}

The quadratic identity for the tetrahedral index gives:

\begin{thm} \cite[Theorem 5.1]{GHRS}
\label{thm.20move.index}
If $\CT$ and $\CT'$ are ideal triangulations related by a 
0-2 move and both are 1-efficient, then $I_{\CT}=I_{\CT'}$.
\end{thm}

\medskip
It is currently unknown whether any two  1-efficient triangulations of a 
given cusped manifold are connected by 2-3/3-2 and 0-2/2-0 moves preserving 
1-efficiency.  See Section \ref{PachnerGraph} for a discussion of some 
experimental results on this question.   

\medskip
However, using the previous results, we can obtain a  
\emph{topological invariant} $I_M$ of any cusped hyperbolic 3-manifold $M$ 
as follows (see [GHRS] for the details).

\begin{itemize}
\item 
Consider the {\em canonical} or {\em Epstein-Penner} decomposition of $M$ 
into convex ideal hyperbolic polyhedra (using horoball cusp neighbourhoods 
of equal volume if $M$ has more than one cusp).
\item 
If the Epstein-Penner decomposition is a triangulation $\tri$,
then we define $I_M=I_\tri$.
\item 
In general, we can define $I_M=I_\tri$ where $\tri$ is any triangulation
in a class $\mathcal{EP}$ consisting of all \emph{regular triangulations} 
of the Epstein-Penner cells, with all possible layered triangulations of 
the bridge regions between any incompatible triangulations of the faces.
\item 
A \emph{regular triangulation} of a set of points $A= \{ a_i \}$ in $\R^n$, 
is obtained by lifting the points vertically to points $(a_i,t_i)$ in 
$\R^{n+1}$, taking the bottom faces of their convex hull in $\R^{n+1}$, and 
then projecting back to $\R^n$. (Use the projective model to extend 
this definition to $\H^n$.)
\item 
All triangulations in class $\mathcal{EP}$ admit semi-angle structures,
hence are 1-efficient.
\item 
Results of Gelfand, Kapranov and Zelevinsky on {regular triangulations} 
imply that $\mathcal{EP}$ is connected by sequences of 2-3, 3-2, 0-2 and 
2-0 moves, staying within 1-efficient triangulations. But the index is 
invariant under such moves, so $I(\tri)$ is the same for all $\tri$ in 
$\mathcal{EP}$.
\item 
Hence we obtain a well-defined invariant for any cusped hyperbolic 3-manifold.
\end{itemize}
