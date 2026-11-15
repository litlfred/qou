---
doc_id: arxiv-2108.09349v2
doc_title: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS"
section_id: sec-008-25-equivalence-classes-of-edges-in-the-triangula
section_title: "Equivalence classes of edges in the triangulation"
section_number: 2.5
pages: 10-11
source_pdf: 2108.09349v2.pdf
source_sha256: 4c732bfcbf3dfb16
toc_source: outline
text_source: latex
latex_prose_ratio: 0.942
latex_coverage_ratio: 0.932
doc_brief: "GEOMETRIC TRIANGULATIONS OF A FAMILY OF HYPERBOLIC 3-BRAIDS — We construct topological triangulations for complements of (−2, 3, n)-pretzel knots and links with n ≥7."
---
\label{sec:edges}

Knowing the relationships between the edges of $\tau_{p}$ will prove helpful because their equivalence classes form the edges of $X_{p}$ and the (internal) dihedral angles along these edges will dictate its geometry.  In determining equivalence classes, we can use Figure~\ref{fig:anyp} or Table~\ref{table:anyp}, whichever is easier.

As an example, we will determine all edges identified to the 01 edge of $w_0^\prime$.  In the braid picture, $w_0^\prime(01)$ slides down through the first $\sigma_1$ half-twist to be identified with $w_1(10)$ and $w_1^\prime(10)$, so the equivalence class of $w_0^\prime(01)$, $[w_0^\prime(01)]$, contains the 01 edge of $w_1$ and of $w_1^\prime$.  Continuing to move the~01 edge through more half-twists shows the 01 edges of $w_i$ and $w_i^\prime$ belong to $[w_0^\prime(01)]$ for all~$i$.  Two edges of $s$ also appear in this equivalence class, which can be seen most easily in Table~\ref{table:anyp}:  $w_1^\prime(01)\sim s(bc)$ and $w_{p-1}(01)\sim s(ad)$.  These edges of $s$, $s(bc)$ and $s(ad)$, are also identified to $w_{p-1}^\prime(25)$ and $w_1(25)$, respectively, which can themselves be slid along along the braid to show that the 25 edges of each $w_i$ and~$w_i^\prime$ are in~$[w_0^\prime(01)]$.  We have not yet considered face pairings between $w_0^\prime$ and $w_p$.  The first in Table~\ref{table:anyp}, $w_0^\prime(012)\sim w_p(021)$ shows $w_p(02)$ and $w_0^\prime(02)$ are also in~$[w_0^\prime(01)]$.  Based on how the tetrahedra are positioned in the braid complement, 02 is the top edge in $w_0^\prime$ and the bottom edge in $w_p$, which allows us to describe~$[w_0^\prime(01)]$ as follows.

\begin{observation}\label{obs:veeringred}
The equivalence class $[w_0^\prime(01)]$ contains a total of $4p+4$ edges:  the 01 edges and 25 edges of each $w_i$ and $w_i^\prime$; $s(bc)$ and $s(ad)$; the top edge of $w_0^\prime$ and the bottom edge of $w_p$.  These edges are colored red in Figure~\ref{fig:anyp}.
\end{observation}

\begin{observation}\label{obs:veeringblue5}
A similar analysis shows that $X_{p}$ has two edges with degree~5.  The edge $[w_0^\prime(05)]$ arises from 
$$
w_0^\prime(05)\sim w_1(15)\sim s(cd)\sim w_{p-1}^\prime(51)\sim w_p(05)\sim_{\text{back to}} w_0^\prime(05)
$$
and, when $p>1$, the edge $[w_0^\prime(12)]$ from
$$
w_0^\prime(12)\sim w_1^\prime(02)\sim s(ba)\sim w_{p-1}(20)\sim w_p(21)\sim_{\text{back to}} w_0^\prime(12).
$$
When $p=1$, $w_1^\prime(02)$ and $w_{p-1}(20)$ are undefined and are replaced by $s(db)$ and~$s(ac)$.
\end{observation}

It turns out that the remaining $2p-2$ edges have degree~4.
