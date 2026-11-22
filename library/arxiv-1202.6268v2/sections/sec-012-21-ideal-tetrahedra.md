---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-012-21-ideal-tetrahedra
section_title: "Ideal tetrahedra"
section_number: 2.1
pages: 11-11
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
toc_source: outline
text_source: latex
latex_prose_ratio: 0.931
latex_coverage_ratio: 0.99
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
[]{#sec.tet label="sec.tet"}

Combinatorially, an *oriented ideal tetrahedron* $\Delta$ is a topological ideal tetrahedron with three complex *shape parameters* $(z,z',z'')$ assigned to pairs of opposite edges (Figure [1](#fig.tet){reference-type="ref" reference="fig.tet"}). The shapes always appear in the same cyclic order (determined by the orientation) around every vertex, and they satisfy

$$\label{tetexp}
  \begin{equation} zz'z'' = -1\,, \hspace{0in}\label{tetexpP}   \end{equation} 

and

  \begin{equation} z''+z^{-1}-1=0\,. \hspace{0in}\label{tetLag}   \end{equation}$$

In other words, $z'=1/(1-z)$ and $z''=1-z^{-1}$. We call the tetrahedron *non-degenerate* if none of the shapes take values in $\{0,1,\infty\}$, *i.e.*, $z,z',z''\in \mathbb{C}^*\backslash\{1\}$. It is sufficient to impose this on a single one of the shapes.

![An ideal tetrahedron ](tet){#fig.tet width="2in"}

Borrowing common terminology from the theory of normal surfaces, *cf.* [@Bu; @Kang; @KR; @Till2], we define the *quadrilateral type* (in short, *quad type*) of $\Delta$ to be the distinguished pair of opposite edges labelled by $z$. Clearly, there is a three-fold choice of quad type for any oriented ideal tetrahedron. Different choices correspond to a cyclic permutation of the vector $(z,z,',z'')$, which leaves relations [\[tetexp\]](#tetexp){reference-type="eqref" reference="tetexp"} invariant.

Geometrically, the shape parameters determine a $\mathrm{PSL}(2,\mathbb{C})$ structure on $\Delta$. Equivalently, they determine a hyperbolic structure, possibly of negative volume. We can then describe the ideal hyperbolic tetrahedron $\Delta$ as the convex hull of four ideal points in hyperbolic three-space $\mathbb H^3$, whose cross-ratio is $z$ (or $z'$, or $z''$). Each shape $z$ fixes the complexified dihedral angle on the edge it labels, via

$$z = \exp(\text{torsion \!+\! $i$\,angle})\,,$$

and similarly for $z'$, $z''$.
