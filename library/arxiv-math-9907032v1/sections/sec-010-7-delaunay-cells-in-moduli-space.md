---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-010-7-delaunay-cells-in-moduli-space
section_title: "Delaunay cells in moduli space"
section_number: 7
pages: 20-21
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
toc_source: inferred
text_source: latex
latex_prose_ratio: 0.966
latex_coverage_ratio: 1.0
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
[]{#moduli label="moduli"} In the Introduction we alluded to the cell decomposition of the moduli space $\mathcal{M}$ of Euclidean structures, where the cells are given by Euclidean structures where the Delaunay triangulation has a fixed combinatorial type $T$. Each cell is a convex polytope $\mathcal{P}(T)$, and the results above can be used to describe the combinatorial and geometric structure of $\mathcal{P}(T)$ in some detail, although some interesting questions (discussed at the end of this section) remain open.

Consider a codimension $1$ face $f$ of $\mathcal{P}(T)$. The face $f$ may be either a boundary face of the moduli space $\mathcal{M}$ (viewed as a polyhedral complex) or an interior face. In the latter case, $f$ corresponds to a change of combinatorial type of Delaunay triangulation from $T$ to $T^\prime$, and it is well understood that the primitive such change is given by a *diagonal flip*, so $f$ corresponds to a cyclic quadrilateral $ABCD$, where in $T$ the Delaunay triangulation has triangles (for example) $ABC$ and $CDA$, while in $T^\prime$, the triangles are $DAB$ and $BCD$. On $f$, the quadrilateral $ABCD$ can be triangulated either way, but the dihedral angle along (either) diagonal is equal to $\pi$.

Suppose now that $f$ is a boundary face of $\mathcal{M}$ -- in particular, this will mean that none of the dihedral angles of the Euclidean structures in the interior of $f$ are equal to $\pi$. By Theorems [\[versimple\]](#versimple){reference-type="ref" reference="versimple"} and [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}, it follows that there is a simple cocycle $c^*$ of $T^*$ where the inequality [\[kappaineq\]](#kappaineq){reference-type="ref" reference="kappaineq"}\[(b)\] becomes an equality. This means, by the geometric estimates in the beginning of section [\[ideal\]](#ideal){reference-type="ref" reference="ideal"}, that the collar $C$ of $c^*$ is becoming long and thin (that is, the conformal modulus of $C$ diverges to $\infty$), and so $f$ corresponds to the Euclidean structure pinching off along the curve $c^*$. The following construction (discussed in greater detail in an upcoming paper of the author) helps visualize this pinching off in terms of the more usual degeneration of hyperbolic surfaces:

Consider a triangulated singular Euclidean surface $(S, E, P)$. The data given by $(S, E, P)$ (initially using a triangulation, though it is easy to show that the result is independent of triangulation) can be used to construct a cusped hyperbolic surface, as follows:

1.  To each triangle $t$ of the triangulation $T$ of $(S, E, P)$, associate an ideal triangle $h(t)$.

2.  For each pair of adjacent triangles $t_1=ABC$ and $t_2=ABD$ of $T$, we have the log of the modulus of the cross-ratio of the four corresponding points: $$r(t_1, t_2) = \log
      \frac{|AC||BD|}{|BC||AD|}.$$

3.  For each pair of adjacent triangles $t_1$ and $t_2$ as above, glue the hyperbolic triangles $h(t_1)$ and $h(t_2)$ along the edge corresponding to $AB$ with shear (see, eg, [@rivid]) equal to $r(t_1, t_2).$

It is not hard to see that if we start with a Euclidean structure $(S,
E, P)$, we will wind up with a *complete* cusped hyperbolic structure (actually, it is sufficient, but not necessary, to start with a Euclidean structure -- some similarity structures will give a complete structure also). The construction thus defines a map (certainly not injective, but which can be shown to be surjective using the construction of [@penner; @ep; @np]) between the moduli space of Euclidean structures with cone points and that of complete finite-area hyperbolic structures. It can be shown (this was an important part of [@rh; @steiner] for the case of genus $0$) that the degeneration, as above, of the Euclidean structure on $(S, E, P)$, corresponds precisely to the pinching off along a simple closed curve of the hyperbolic structure on $(S, H(E), P)$.

*Remark.* Another surjection between the space of singular Euclidean structures and the space of cusped hyperbolic structures is well-known, and is discussed in the well-known paper of Troyanov [@troy]. The two surjections are *not* the same -- this was remarked by C. T. McMullen.
