---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-022-111-solid-torus
section_title: "Solid torus"
section_number: 11.1
pages: 35-35
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.959
latex_coverage_ratio: 1.0
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{solid_torus_ex}

The (open) solid torus has a 1-efficient triangulation $\T$  by 2 
tetrahedra with isomorphism signature `cMcabbgds', 
and gluing equation/holonomy coefficient matrix (from SnapPy) given by:
$$\begin{bmatrix} 2 & 1 & 2 & 2 & 2 & 2 \\ 0 & 1 & 0 & 0&0&0\\
0 & 1 & 0 & 0 & -1 & 0\\ 0 & 1 & 0 & 0 & 0& 2
\end{bmatrix}$$
(Here the peripheral curves $\mu,\lambda$ correspond to the meridian and 
longitude for the unknot in $S^3$.)
Summing over integer weights $k$ on edge 2 gives the 3D-index 
\begin{align*}
I_\T(x \mu + y \lambda) & =\sum_{k \in \Z} q^k \JD(0,k+x+y,0)\JD(0,-x,2y) \\
& =J(0,-x,2y) q^{-x-y} \sum_{k\in\Z} q^kJ(0,k,0)=0
\end{align*}
since
$$
\sum_{k\in\Z} q^k \JD(0,k,0) = 
\sum_{k\in\Z} \ID(0,k) q^k = I(0,q,q)= \frac{(q q^{-1};q)_\infty}{(q)_\infty;q}=0
$$
using equation (\ref{ID_gen_func}). 

It follows that the 3D-index {\em vanishes identically} for
all 118753 1-efficient ideal triangulations of the solid torus with 
at most 6 tetrahedra, since we have checked that these are all connected to 
$\T$ by 2-3, 3-2, 0-2 and 2-0 moves preserving 1-efficiency.
