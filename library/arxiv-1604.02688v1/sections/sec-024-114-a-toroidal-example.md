---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-024-114-a-toroidal-example
section_title: "A toroidal example"
section_number: 11.4
pages: 36-37
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
toc_source: outline
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.964
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
\label{toroidal_ex}

The 2-tetrahedron ideal triangulation $\T$ with isomorphism signature
`cPcbbbdei' is not 1-efficient.  In fact it gives a manifold containing an 
incompressible torus which splits the manifold in 
two Seifert fibres pieces $SFS[D^2(2,1)(3,1)]$ and $SFS[A^2(2,1)]$. The 
gluing equation/holonomy coefficients (from SnapPy) are given by:
$$
\begin{bmatrix} 1 & 1 & 0 & 1 & 0 & 1 \\ 1 & 1 & 2 & 1&2&1\\
0 & -1 & 0 & 1 & 0 & 0\\ 0 & 0 & 2 & 0 & 0& 0
\end{bmatrix}
$$

Hence, summing over edge 1,  the 3D-index is given by
$$
I_\T(x \mu + y\lambda ) =\sum_{k \in \Z} q^k \JD(k,k-x,2y) \JD(k+x,0,k)
= \sum_{k \in \Z} \ID(x,2y-k) \ID(-x,-k).
$$

If $x=0,y=0$ then the above sum $\sum_k \ID(0,-k)^2$ 
is divergent, as expected by Theorem \ref{index_structure_iff_1-efficient}, 
since each term with $k \le 0$ has degree $0$.

However for $x \ne 0$ the sum converges, and experimentation suggests the sum 
simplifies to the following geometric series:
$$
I_\T(x \mu + y \lambda) = \frac{ (-1)^x q^{|x|(|y + x/2| + 1/2)}}{(1 - q^{|x|})}, 
\text{ for } x\ne 0.
$$

Putting 
$$
x \mu + y \lambda = a \mu +(b-a/2)\lambda = a(\mu-\lambda/2)+b\lambda =
a \bar \mu + \b \bar \lambda
$$
we have symmetries
$I_\T(a \bar \mu + b \bar\lambda) = 
I_\T( \pm a \bar \mu + \pm b \bar\lambda)$ for $a \ne 0$ 
(by the duality and triality identities) and experimentally it seems that
$$
I_\T(a \bar \mu + b \bar\lambda) = \frac{(-1)^a q^{a(b+1/2)}} {1-q^a},  
\text{ for }a>0, b \ge 0.
$$
