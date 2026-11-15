---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-030-124-connected-components-of-normal-surfaces
section_title: "Connected components of normal surfaces"
section_number: 12.4
pages: 45-50
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.94
latex_coverage_ratio: 0.905
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
In Figure \ref{fig:twoThreeBipyramid}, there are two bipyramids related by 
a 2-3 move, one with two tetrahedra which we call $\BTwo$ and one with 
three tetrahedra which we call $\BThree$. We will also think of these as 
subsets of two triangulations related by a 2-3 move, $\T_n$ and $\T_{n+1,f}$ 
where $f$ is face identified in $\BTwo$. In this discussion, we assume that 
the exterior faces of $\BTwo$ are not identified. However, if the exterior 
faces of $\BTwo$ are identified (and therefore $\BThree$), then some of 
these pieces might not appear as subsets of embedded normal surfaces.

If $S_n$ is a normal surface of $\T_n$ then each piece will have at most 
one normal arc in face $f$. Using the notation from 
Section \ref{gluing_eqn_sect} and Figure \ref{fig:edgesAndQuad}, 
we thus obtain a census of connected components $S_n \cap \BTwo$ as follows: 

\begin{enumerate}
\item  
$t_{A0},t_{B1}$;
\item  
$(t_{A1}+t_{B1})$, $(t_{A2}+t_{B3})$, $(t_{A3}+t_{B2})$;
\item  
$(q_{A01:23}+t_{B1})$, $(q_{A02:13}+t_{B3})$, $(q_{A03:12}+t_{B2})$, 
$(q_{B01:23}+t_{A1})$, $(q_{B02:13}+t_{A3})$, and $(q_{B03:12}+t_{A2})$;
\item  
$(q_{A01:23}+q_{B01:23})$, $(q_{A02:13}+q_{B03:12})$,  $(q_{A03:12}+q_{B02:13})$.
\end{enumerate}

If $S_{n+1}$ is a normal surface of $\T_{n+1,f}$, we can obtain an analogous 
result. Namely, the observation that each connected component of 
$S_{n+1}\cap \BThree$ intersects an interior face of $\BThree$ in at most 
one normal arc, yields the following list:

\begin{enumerate}
\item  
$(t_{C0}+t_{D0}+t_{E0})$, $(t_{C1}+t_{D1}+t_{E1})$;
\item  
$(t_{C2}+t_{E3})$, $(t_{D2}+t_{C3})$,  $(t_{D3}+t_{E2})$;
\item  
$(t_{D0}+q_{C02:13}+q_{E03:12})$, $(t_{E0}+q_{D02:13}+q_{C03:12})$, 
$(t_{C0}+q_{E02:13}+q_{D03:12})$, $(q_{D01:23}+t_{C3}+t_{E2})$, 
$(t_{E1}+q_{D03:12}+q_{C02:13})$,  $(t_{C1}+q_{E03:12}+q_{D02:13})$;
\item  
$(q_{D01:23}+t_{C3}+t_{E2})$, $(q_{E01:23}+t_{D3}+t_{C2})$, 
$(q_{C01:23}+t_{E3}+t_{D2})$;
\item  
$(q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3})$, $(q_{D01:23}+q_{E01:23}+t_{C2}+t_{C3})$, 
$(q_{E01:23}+q_{C01:23}+t_{D2}+t_{D3})$;  
\item 
$(q_{C01:23}+q_{D01:23}+q_{E01:23})$.
\end{enumerate}

Examples of the normal surface pieces of type 3) and 4) are given in 
Figures \ref{fig:twoThreeQuadTri} and \ref{fig:twoThreeQuadQuad}.

\begin{figure}[htpb]
\centering
\includegraphics[width=0.5\textwidth]{figures/twoThreeQuadTri}

\caption{\label{fig:twoThreeQuadTri} The effect of a 2-3 move on a 
normal disk comprised of a triangle and quad.}
\end{figure}

\begin{figure}[htpb]
\centering
\includegraphics[width=0.5\textwidth]{figures/twoThreeQuadQuad}

\caption{\label{fig:twoThreeQuadQuad} The effect of a 2-3 move on a 
normal disk comprised of two quads.}
\end{figure}

Examples of the normal surface pieces of type 5) and 6) are given in 
Figures \ref{fig:folder} and \ref{fig:tube}.

\begin{figure}[htpb]
\centering
\includegraphics[width=0.5\textwidth]{figures/folder}

\caption{\label{fig:folder} An example of a normal surface piece of $\BThree$.}
\end{figure}

\begin{figure}[htpb]
\centering
\includegraphics[width=0.5\textwidth]{figures/tube}

\caption{\label{fig:tube} A second example of a normal surface piece of 
$\BThree$.}
\end{figure}

The following proposition allows us relate the pieces in both list above via 
the 2-3 move that transforms $\BTwo$ to $\BThree$. 

\begin{prop}
\label{cor:oneEfficientDescends}
Let $\T_n$ and $\T_{n+1,f}$ be the triangulations defined above.
For each normal surface $S_n$ of $\T_n$ there exists a normal surface 
$S_{n+1}$ of $\T_{n+1,f}$ obtained by dividing up the normal discs of $S_n$ 
which intersect $\BTwo$. In particular, if $\T_{n+1,f}$ is 1-efficient, then 
$\T_n $ is 1-efficient.
\end{prop}

\begin{proof}
Following Figure \ref{fig:twoThreeBipyramid}, we can consider the images 
of $S_n \cap \BTwo$ under the 2-3 move: 
\begin{enumerate}
\item 
$t_{A0} = t_{C0}+t_{D0}+t_{E0}$, $t_{B0} = t_{C1}+t_{D1}+t_{E1}$
\item 
$t_{A1}+t_{B1} = t_{C2}+t_{E3}$, $t_{A2}+t_{B3} = t_{D2}+t_{C3}$, 
$t_{A3}+t_{B2} = t_{E2}+t_{D3}$
\item 
$q_{A01:23} + t_{B1}= t_{D0}+q_{C02:13}+q_{E03:12}$, 
$q_{A02:13} + t_{B3}= t_{E0}+q_{D02:13}+q_{C03:12}$, 
$q_{A03:12} + t_{B2}= t_{C0}+q_{E02:13}+q_{D03:12}$, 
$q_{B01:23} + t_{A1}= t_{D1}+q_{C03:12}+q_{E02:13}$, 
$q_{B02:13} + t_{A3}= t_{E1}+q_{D03:12}+q_{C02:13}$, 
$q_{B03:12} + t_{A2}= t_{C1}+q_{E03:12}+q_{D02:13}$, 
\item 
$q_{A01:23} + q_{B01:23}= q_{D01:23}+t_{C3}+t_{E2}$, 
$q_{A02:13} + q_{B03:12}= q_{E01:23}+t_{D3}+t_{C2}$, 
$q_{A03:12} + q_{B02:13}= q_{C01:23}+t_{E3}+t_{D2}$.
\end{enumerate}

Relations (1) and (2) follow from Figure \ref{fig:twoThreeBoundary}.

Note that $q_{A01:23} + t_{B1}= t_{D0}+q_{C02:13}+q_{E03:12}$ follows from 
Figure \ref{fig:twoThreeQuadTri}, and the remaining two relations can be 
obtained by an appropriate rotation (and relabelling) of that figure.

Finally, $q_{A01:23} + q_{B01:23}= q_{D01:23}+t_{C3}+t_{E2}$ follows from 
Figure \ref{fig:twoThreeQuadQuad}, and again the remaining two relations 
can be obtained by an appropriate rotation (and relabelling) of that figure.

Thus, for any normal surface of $S_n$, we can map the normal surface 
pieces locally to build a normal surface with the same Euler 
characteristic in $\T_{n+1,f}$. Restricting this observation to the case 
of embedded normal surfaces with non-negative Euler characteristics shows 
if $\T_{n+1,f}$ is 1-efficient, then $\T_n$ must be as well.  
\end{proof}

We point out that the Luo-Tillmann's definition of Euler characteristic 
on quadrilateral discs in the presence of a generalised angle structure 
(compare  \cite[Lemma 15]{LT} in the case that the curvature is 0) provides 
a useful mnemonic for keeping track of relations of type (3) and (4). 
Namely, these relations are just the angle sums which occur after a 
2-3 move, e.g. edge $A01$ decomposes into edges $C02$ and $E03$ and 
edges $A23$ and $B23$ form $D23$.

\begin{prop}
\label{prop:oneEfficientFails}
Let $\T_n$ and $\T_{n+1,f}$ be the triangulations defined above, such that 
the exterior faces of $\BTwo$ are not identified.
If $\T_n$ is 1-efficient and $\T_{n+1,f}$ is not 1-efficient, then 
$\T_{n+1,f}$ exhibits an embedded normal surface with exactly two of the 
three quad types parallel to the degree three edge created by the 2-3 move.  
\end{prop}

\begin{proof}
If $\T_n$ is 1-efficient and $\T_{n+1,f}$ is not 1-efficient, then there 
must be an embedded normal surface $S_{n+1}$ in $\T_{n+1,f}$ which 
intersects  $\BThree$. If this intersection is only triangular discs then 
$S_{n+1}$ would descend to an embedded normal surface in $\T_n$, and so 
$S_{n+1}\cap \BThree$ must contain at least one connected component with at 
least one quad.  However, the case analysis in 
Proposition~\ref{cor:oneEfficientDescends} of the normal discs in 
$\BThree$ shows that each connected component $S_{n+1}\cap \BThree$ is in 
the image of an embedded normal disk of $\BTwo$ save four: 
$q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$,
$q_{D01:23}+q_{E01:23}+t_{C2}+t_{C3}$, 
$q_{E01:23}+q_{C01:23}+t_{D2}+t_{D3}$,
and $(q_{C01:23}+q_{D01:23}+q_{E01:23})$.
 
However, if the last piece is part of $S_{n+1}\cap \BThree$, then there 
exists a collection of embedded normal spheres $\hat{S}_{n+1}$ of 
$\T_{n+1,f}$ formed by cutting out all copies of this annulus and capping 
off with triangles. If none of these spheres have pieces of the form:
$q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$,
$q_{D01:23}+q_{E01:23}+t_{C2}+t_{C3}$, and 
$q_{E01:23}+q_{C01:23}+t_{D2}+t_{D3}$,
then there exists an embedded normal sphere in $\T_n$, a contradiction. 
If no annuli of the form $(q_{C01:23}+q_{D01:23}+q_{E01:23})$ exist in 
$S_{n+1}\cap \BThree$, then again there must be at least one piece of the form: 
$q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$,
$q_{D01:23}+q_{E01:23}+t_{C2}+t_{C3}$, and 
$q_{E01:23}+q_{C01:23}+t_{D2}+t_{D3}$, which completes the proof.
\end{proof}

Although $q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$, 
$q_{D01:23}+q_{E01:23}+t_{C2}+t_{C3}$, and $q_{E01:23}+q_{C01:23}+t_{D2}+t_{D3}$ 
are not in the image of embedded normal discs of $\T_n$, they are in the 
image of a pair of immersed normal discs. For example,
$q_{A03:12} + q_{B02:13}+q_{A01:23} + q_{B01:23}=
q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}+t_{C3}+t_{D2}$. This is the key observation 
in the proof of the following lemma.

\begin{prop}
\label{prop:strictAngToOneEff}
Let $\T_n$ and $\T_{n+1,f}$ be the triangulations defined above, such that 
the exterior faces of $\BTwo$ are not identified.
If $\T_n$ admits a strict angle structure, then $\T_{n+1,f}$ is 1-efficient. 
\end{prop}

\begin{proof}
Suppose $\T_{n+1,f}$ is not 1-efficient. Then there is a closed embedded 
normal surface $S_{n+1}$ of $\T_{n+1,f}$ with non-negative Euler characteristic. 

Just as above, $S_{n+1} \cap \BThree$ must contain pieces of the form below, 
otherwise there is a closed embedded surface $S_n$ of $\T_n$ with 
non-negative Euler characteristic:

$q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$,
$q_{D01:23}+q_{E01:23}+t_{C2}+t_{C3}$, 
$q_{E01:23}+q_{C01:23}+t_{D2}+t_{D3}$,
and $(q_{C01:23}+q_{D01:23}+q_{E01:23})$.

By an identical argument to the one used in 
Proposition \ref{prop:oneEfficientFails}, we can rule out the annuli of 
the form  $(q_{C01:23}+q_{D01:23}+q_{E01:23})$. Thus, $S_{n+1} \cap \BThree$ 
contains exactly one of the following pairs of quads:
$q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$,
$q_{D01:23}+q_{E01:23}+t_{C2}+t_{C3}$, or 
$q_{E01:23}+q_{C01:23}+t_{D2}+t_{D3}$.
 
Without loss of generality, assume it is $q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$. 
Create a new surface $S'_{n+1}$, by adding a boundary torus to $S_{n+1}$ until 
$S_{n+1} \cap \BThree$ contains the same number of copies of $(t_{C3}+t_{D2})$ 
as $q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3}$. Note that $\chi(S_{n+1})=\chi(S'_{n+1})$. 
The image of $S'_{n+1}$ under the 3-2 move, is an immersed normal surface 
$S_n$ with the same boundary arcs on 
$\BTwo$ as $\partial \BThree \cap S'_{n+1}$, with the property that for 
each copy of $q_{C01:23}+q_{D01:23}+t_{E2}+t_{E3} + (t_{C3}+t_{D2})$ in 
$\BThree \cap S'_{n+1}$ there is a copy of 
$q_{A03:12} + q_{B02:13}+q_{A01:23} + q_{B01:23}$. In the presence of any 
generalised angle structure on $T_n$, each quad is assigned an Euler 
characteristic, while the Euler characteristic of the triangles vanishes. 
Moreover, this Euler characteristic agrees with the Euler characteristic 
of $S'_{n+1}$. However, if $\T_n$ admits a strict angle structure, then 
each quad has a negative contribution to Euler characteristic while 
each triangle does not contribute to Euler characteristic. This contradicts 
$\chi(S_{n+1})\geq 0.$
\end{proof}

\begin{rmk}
The analogous statement to Proposition \ref{prop:strictAngToOneEff} for 
0-2 moves does not hold. 
In fact, `eLAkbbcdddhjac' has a degree 2 edge and is not 1-efficient. 
However, performing a 2-0 move along this edge results 
in the  1-efficient (in fact, geometric) triangulation of the figure 8 
sister manifold, `cPcbbbdxm'.
\end{rmk}

\begin{ex}
We next provide an example of how a geometric triangulation can `degenerate' 
to a triangulation which is not 1-efficient in two 2-3 moves:  
The triangulation `eLAkbccddhhnqw' is geometric, the 2-3 move along face 
5 gives `fLAMcbccdeemejman' which does not admit a strict angle structure, 
and the 2-3 move along face 8 gives `gLALQaccefffbgfgmqt' which is not 
1-efficient. 

However, perhaps the simplest example of a non 1-efficient triangulation 
arising from a 2-3 move on a 1-efficient triangulation has already 
been discussed in Table \ref{tab:ppTrefoil}. In fact the first Pachner move 
in that path a 2-3 move along face 2 of `cPcbbbadh' resulting 
in `dLQacccbgjs' breaks 1-efficiency. 
We again point out that there is an immersed normal surface in `cPcbbbadh' 
determined by the quads $q_{0:02:13}$, $q_{0:03:12}$, $q_{1:02:13}$, 
and $q_{1:02:13}$ (face 2 is $0(023)=1(023)$), which maps to an embedded normal 
torus in `dLQacccbgjs'. (Note: Regina's labelling routine is different 
from that of the lists in this section.)
\end{ex}
