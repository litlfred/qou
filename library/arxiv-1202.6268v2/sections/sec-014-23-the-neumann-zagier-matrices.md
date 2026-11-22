---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-014-23-the-neumann-zagier-matrices
section_title: "The Neumann-Zagier matrices"
section_number: 2.3
pages: 12-13
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.897
latex_coverage_ratio: 0.939
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.NZ label="sec.NZ"}

The matrices $\mathbf G$, $\mathbf G'$ and $\mathbf G''$

have both symmetry and redundancy. We have already observed that any one of the edge constraints [\[glue\]](#glue){reference-type="eqref" reference="glue"} can be removed. Let us then ignore the edge $I=N$. We can also use [\[tetP\]](#tetP){reference-type="eqref" reference="tetP"} to eliminate one of the three shapes for each tetrahedron. We choose this canonically to be $Z_i'$, though which pair of edges is labelled $Z_i'$ depends on the choice of quad type for the tetrahedron. Then the first $N-1$ edge equations and the meridian ($\mu$) equation are equivalent to

$$\sum_{j=1}^N \big(\mathbf A_{ij}Z_j+\mathbf B_{ij}Z_j''\big) = i\pi\, \nu_i\,,
\qquad i=1,...,N\,, 
\label{NZlin}$$

where

$$\mathbf A_{ij} = \left\{\begin{array}{c@{\quad}l}
  \mathbf G_{ij}-\mathbf G_{ij}' & I\neq N \\[.2cm]
    \mathbf G_{N+1,j}-\mathbf G_{N+1,j}' & i= N
  \end{array}\right. \qquad
  \mathbf B_{ij} = \left\{\begin{array}{c@{\quad}l}
  \mathbf G_{ij}''-\mathbf G_{ij}' & I\neq N \\[.2cm]
    \mathbf G_{N+1,j}''-\mathbf G_{N+1,j}' & i= N\,;
  \end{array}\right. \qquad$$

and

$$\nu_i := \left\{\begin{array}{c@{\quad}l}
  2-\sum_{j=1}^N \mathbf G_{ij}' & i\neq N \\[.2cm]
    -\sum_{j=1}^N \mathbf G_{N+1,j}' & i= N\,.
  \end{array}\right.
\label{defn}$$

We will generally assume $Z$, $Z''$, and $\nu$ to be column vectors, and write $\mathbf A\, Z+\mathbf B \,Z''=i\pi \nu\,.$

The matrices $(\mathbf G,\mathbf G',\mathbf G'')$ as well as $(\mathbf A, \mathbf B,\nu)$ can easily be obtained from `SnapPy` [@SnapPy], as is illustrated in Appendix [\[app.compute\]](#app.compute){reference-type="ref" reference="app.compute"}.

The Neumann-Zagier matrices $\mathbf A$ and $\mathbf B$ have a remarkable property: they are the top two blocks of a $2N\times 2N$ symplectic matrix [@NZ]. It follows that

$$\mathbf A\mathbf B^T = \mathbf B\mathbf A^T \,, 
\label{NZsymp}$$

and that the $N\times 2N$ block $(\mathbf A\;\mathbf B)$ has full rank. This symplectic property is crucial for defining the state integral of [@D1], for defining our formal power series invariant $\mathcal{Z}_M(\hbar)$, and for the combinatorial proofs of topological invariance of the $1$-loop invariant. A detailed discussion of the symplectic properties of the Neumann-Zagier matrices $\mathbf A, \mathbf B$ is given in Appendix [\[app.symp\]](#app.symp){reference-type="ref" reference="app.symp"}.
