---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-014-23-the-neumann-zagier-matrices
section_title: "The Neumann-Zagier matrices"
section_number: 2.3
pages: 12-14
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
text_source: latex
latex_prose_ratio: 0.898
latex_coverage_ratio: 0.926
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

## Combinatorial flattenings {#sub.flat}

We now have all ingredients to define what is a combinatorial flattening.

::: definition
[]{#def.flattening label="def.flattening"} Given an ideal triangulation $\mathcal T$ of $M$, a *combinatorial flattening*

is a collection of $3N$ integers $(f_i,f_i',f_i'') \in \mathbb Z^3$ for $i=1,\dots,N$ that satisfy

$$\begin{equation} f_i+f_i'+f_i'' = 1\,,\qquad i=1,...,N\,, \label{flattrip}   \end{equation} 

  \begin{equation} \label{flatG} 
\sum_{i=1}^N \big(\mathbf{G}_{Ii}f_i+\mathbf{G}_{Ii}'f_i'+\mathbf{G}_{Ii}''f_i''\big) 
= \begin{cases} 2 & I=1,...,N \\
0 & I=N+1 \end{cases} \,.
  \end{equation}$$
:::

Note that if we eliminate $f'$ using Equation [\[flattrip\]](#flattrip){reference-type="eqref" reference="flattrip"}, a flattening is a pair of vectors $(f,f'') \in \mathbb Z^{2N}$ that satisfies

$$\label{flatAB} \mathbf A f+\mathbf B f'' = \nu\,.$$ Evidently, Equation [\[flatAB\]](#flatAB){reference-type="eqref" reference="flatAB"} is a system of linear Diophantine equations. Neumann proved in [@Neumann-combi Lem.6.1] that every ideal triangulation $\mathcal{T}$ has a flattening.

::: remark
[]{#rem.Nflattening label="rem.Nflattening"} Combinatorial flattenings should not be confused with the (geometric) flattenings of [@N Defn.3.1]. The latter flattenings are coherent choices of logarithms for the shape parameters $z,z',z''$ of a complex solution to the gluing equations. On the other hand, our combinatorial flattenings are independent of a solution to the gluing equations. In the rest of the paper, the term *flattening* will mean a *combinatorial flattening* in the sense of Definition [\[def.flattening\]](#def.flattening){reference-type="ref" reference="def.flattening"}.
:::
