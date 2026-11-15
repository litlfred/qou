---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-013-22-the-gluing-matrices
section_title: "The gluing matrices"
section_number: 2.2
pages: 11-12
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.964
latex_coverage_ratio: 0.964
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.glue label="sec.glue"}

We now discuss an important combinatorial invariant of ideal triangulations, namely the gluing and Neumann-Zagier matrices, their symplectic properties, and the notion of a combinatorial flattening. Although these notions are motivated by hyperbolic geometry (namely the gluing of ideal tetrahedra around their faces and edges to describe a complete hyperbolic structure on a cusped manifold), we stress that these notions make sense for arbitrary 3-manifolds with torus boundary, and for triangulations whose gluing equations may not have solutions in $\mathbb C\setminus\{0,1\}$.

Let $M$ be an oriented one-cusped manifold with an ideal triangulation $\mathcal T=\{\Delta_i\}_{i=1}^N$ and a choice of quad type.

The choice of quad, combined with the orientation of $\mathcal{T}$ and $M$ allow us to attach variables $(Z_i,Z_i',Z_i'')$ to each tetrahedron $\Delta_i$. An Euler characteristic argument shows that the triangulation has $N$ edges $E_I$, $I=1,...,N$. For each edge $E_I$ we introduce a gluing equation of the form

$$E_I:\quad \sum_{i=1}^N \big(\mathbf{G}_{Ii}Z_i+\mathbf{G}_{Ii}'Z_i'
+\mathbf{G}_{Ii}''Z_i''\big) = 2\pi i\,\qquad I=1,...,N\,, \label{glue}$$

where $\mathbf{G}_{Ii} \in \{0,1,2\}$ (resp., $\mathbf{G}_{Ii}'$, $\mathbf{G}_{Ii}''$) is the number of times an edge of tetrahedron $\Delta_i$ with parameter $Z_i$ (resp., $Z_i'$, $Z_i''$) is incident to the edge $E_I$ in the triangulation. In addition, we impose the equations $$Z_i + Z_i'+Z_i''=i\pi \label{tetP}\,.$$ for $i=1,\dots,N$. The Equations [\[glue\]](#glue){reference-type="eqref" reference="glue"} are not all independent. For a one-cusped manifold, every edge begins and ends at the cusp, which implies $\sum_{I=1}^N \mathbf G_{Ii}=\sum_{I=1}^N \mathbf G_{Ii}'=\sum_{I=1}^N \mathbf G_{Ii}''=2$, and therefore that the sum of the left-hand sides of Equations [\[glue\]](#glue){reference-type="eqref" reference="glue"} equals $2\pi i N$. This is the only linear dependence in case of one cusp. In general, there is one relation per cusp of $M$, as follows from [@Neumann-combi Thm.4.1].

An oriented peripheral simple closed curve $\mu$ (such as a meridian) on the boundary of $M$, in general position with the triangulation of the boundary torus that comes from $\mathcal{T}$, also gives rise to a gluing equation. We assume that the curve is simple (has no self intersections), and set the signed sum of edge parameters on the dihedral angles subtended by the curve to zero. A parameter is counted with a plus sign (resp. minus sign) if an angle is subtended in a counterclockwise (resp. clockwise) direction as viewed from the boundary. These rules are the same as described in [@Neumann-combi], and demonstrated in Section [\[sec.41triang\]](#sec.41triang){reference-type="ref" reference="sec.41triang"} below.

Let us choose such a peripheral curve $\mu$. We choose a meridian if $M$ is a knot complement. The gluing equation associated to $\mu$ then takes the form

$$\mu:\quad  \sum_{i=1}^N \big( \mathbf{G}_{N+1,i} Z_i+\mathbf{G}_{N+1,i}' Z_i'
+\mathbf{G}_{N+1,i}''Z_i'' \big) = 0\,,  \label{merid}$$

with $\mathbf{G}_{N+1,i},\,\mathbf{G}_{N+1,i}',\,\mathbf{G}_{N+1,i}''\in \mathbb{Z}$.
