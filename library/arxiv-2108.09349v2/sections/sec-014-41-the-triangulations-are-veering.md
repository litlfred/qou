---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-014-41-the-triangulations-are-veering
section_title: "The triangulations are veering"
section_number: 4.1
pages: 16-17
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.957
latex_coverage_ratio: 0.963
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:veering}

While the initial triangulations $\hat{\tau}_p$ were not veering, the Pachner moves eliminated the obstructions and 
\begin{prop}\label{prop:veering}
Each triangulation $\tau_{p}$ is veering.
\end{prop}
\begin{proof}
With the exception of $s$, the tetrahedra in $\tau_{p}$ have an upward orientation induced by the product region containing the 6-braid, which is how the non-$s$ tetrahedra of $\tau_{p}$ are flattened in Figure~\ref{fig:anyp}.   Flatten $s$ as indicated in the same figure.  In each tetrahedron, assign an angle of~$\pi$ to the diagonal edges and an angle of~0 to the others.  Use red to color the 01 and 25 edges of each $w_i$ and~$w_i^\prime$; the edges $s(bc)$ and $s(ad)$; and the top diagonal of $w_0^\prime$ along with the bottom diagonal of~$w_p$.  (These are exactly the edges colored red in Figure~\ref{fig:anyp}.)  Color the remaining edges blue.  We claim this coloring forms a veering angle structure on~$\tau_{p}$, which is also transverse taut.  

By Observation~\ref{obs:veeringred}, the edges in the equivalence class $[w_0^\prime(01)]$ are exactly the edges colored red.  Thus, the blue edges compose the remaining equivalence classes, and the colorings are consistent with the face pairings that form~$M$. 

Next we show that the assignment of angles forms a taut angle structure.  The angle assignments themselves guarantee  Conditions~(1) and~(2) of  Definition~\ref{def:anglestructure} as well as the requirement that taut angle structures have angles in $\{0,\pi\}$.  Only diagonals are assigned an angle of~$\pi$, so, if there are exactly two diagonals in each equivalence class, Condition~(3) will also be met (the angle sum around each edge is~$2\pi$).  

The class $[w_0^\prime(01)]$, whose members are listed in Observation~\ref{obs:veeringred}, contains exactly two diagonals,~$w_0^\prime(02)$ and~$w_p(02)$.  The degree~5 edges of $X_{p}$ are completely described in Observation~\ref{obs:veeringblue5}.  The edges $[w_0^\prime(05)]$ and $[w_0^\prime(12)]$ each contain exactly two diagonals:  The top diagonal $w_1(15)$ is matched with the bottom diagonal $w_{p-1}^\prime(51)$  and similarly for $w_1^\prime(02)$ and $w_{p-1}(20)$ (or $s(db)$ and $s(ac)$ when $p=1$, which completes this case). 

To check the remaining $2p-2$ edges of~$X_{p}$ for $p>1$, i.e., those of degree~4, we examine $w_{i-1}(02)$ and $w_{i-1}^\prime(15)$, the bottom diagonals of $w_{i-1}$ and $w_{i-1}^\prime$ in the braid complement in Figure~\ref{fig:anyp}.  The edge $w_{i-1}(02)$ bounds both $w_{i-1}(012)$ and $w_{i-1}(025)$.  After passing through the $\sigma_1$~half-twist, the first of these faces is rotated to the back and identified with $w_{i}^\prime(102)$, whereas the second stays in front and is identified with $w_{i}(125)$.  These faces share the edge 12, which, after another $\sigma_1$ is twisted to the back and identified to $w_{i+1}^\prime(02)$.  A similar argument applies to~$w_{i-1}^\prime(15)$.  Symbolically,
\begin{align} 
\begin{split}\label{eq:deg4}
w_{i-1}(02)\sim w_{i}(12)= w_{i}^\prime(12)\sim w_{i+1}^\prime(02)\quad  &\text{ for } i=2, \dots p-2.\\
w_{i-1}^\prime(15)\sim w_{i}(05)=w_{i}^\prime(05)\sim w_{i+1}(15)\quad	&\text{ for } i=1, \dots p-1.
\end{split}
\end{align}
The only diagonals are the 02 and 15 edges, so the edge classes, $[w_i(12)]$ and $[w_i(05)]$, contain exactly two~$\pi$ angles as required.  The remaining  degree-4 edges contain the diagonals of~$s$, $s(ac)$ and $s(bd)$.  The identifications in Table~\ref{table:anyp} show that their equivalence classes contain exactly one other diagonal:
\begin{align} 
\begin{split}\label{eq:s}
s(ac)	\sim w_1^\prime(21) &= w_1(21) 	\sim w_2^\prime(20) \\ 
s(bd)	\sim w_{p-1}^\prime(21) &= w_{p-1}(21) 	\sim w_{p-2}(20).
\end{split}
\end{align}

With exactly two diagonals in each equivalence class, the angle structure is taut.  Each tetrahedron appears as in Figure~\ref{fig:veering}, and the gluings of Table~\ref{table:anyp} identify bottom faces to top faces, so the \lq\lq upward'' orientations are consistent, forming a transverse taut angle structure, which is also layered.
\end{proof}

\begin{cor}\label{cor:positiveanglestructure}
The triangulation $\tau_{p}$ admits a positive angle structure.
\end{cor}
\begin{proof}
In their main result, \cite[Theorem 1.5]{HodgsonEtal}, Hodgson, Rubinstein, Segerman, and Tillmann prove that veering triangulations admit positive angle structures (which they call strict angle structures).  A constructive proof showing how to deform a veering angle structure to a positive angle structure has also been given by Futer and Gu\'eritaud~\cite[Theorem 1.3]{veering}.
\end{proof}
