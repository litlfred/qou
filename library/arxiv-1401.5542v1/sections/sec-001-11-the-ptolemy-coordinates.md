---
doc_id: arxiv-1401.5542v1
doc_title: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS"
section_id: sec-001-11-the-ptolemy-coordinates
section_title: "The Ptolemy coordinates"
section_number: 1.1
pages: 2-2
source_pdf: 1401.5542v1.pdf
source_sha256: f7cd278a274f37c5
toc_source: outline
text_source: latex
latex_prose_ratio: 0.971
latex_coverage_ratio: 0.985
doc_brief: "THE PTOLEMY FIELD OF 3-MANIFOLD-REPRESENTATIONS — The Ptolemy coordinates for boundary-unipotent SL(n, C)-representations of a 3-manifold group were introduced in [7] inspired by the A-coordinates on"
---
\label{sub.ge}

The Ptolemy coordinates for boundary-unipotent representations of a 
3-manifold group in $\SL(n,\C)$ were introduced in 
Garoufalidis--Thurston--Zickert~\cite{GaroufalidisThurstonZickert} inspired by the $\mathcal A$-coordinates 
on higher Teichm\"{u}ller space due to Fock and Goncharov
\cite{FockGoncharov}. In this paper we will focus primarily on representations in $\SL(2,\C)$ and $\PSL(2,\C)$.  


Given a topological ideal triangulation $\T$ of an oriented compact 3-manifold $M$, 
a \emph{Ptolemy assignment} (for $\SL(2,\C)$) is an assignment of a non-zero 
complex number (called a \emph{Ptolemy coordinate}) to each $1$-cell of $\CT$, such that for each simplex, the Ptolemy coordinates assigned to the edges $\varepsilon_{ij}$
satisfy the \emph{Ptolemy relation}
\begin{equation}\label{eq:PtolemyRelation}
c_{03}c_{12}+c_{01}c_{23}=c_{02}c_{13}.
\end{equation}
The set of Ptolemy assignments is thus an affine variety $P_2(\T)$, which is cut out by homogeneous quadratic polynomials. 

In this paper we define the Ptolemy field of a boundary-unipotent representation and show that it is isomorphic to the trace field. This gives rise to an efficient algorithm for \emph{exact} computation of the trace field of a hyperbolic manifold.
