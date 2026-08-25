---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-012-7-delaunay-cells-in-moduli-space
section_title: "DELAUNAY CELLS IN MODULI SPACE"
section_number: 7
pages: 20-21
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
In the Introduction we alluded to the cell decomposition of the modu li space M
of Euclidean structures, where the cells are given by Euclidean stru ctures where
the Delaunay triangulation has a ﬁxed combinatorial type T . Each cell is a convex
polytope P(T ), and the results above can be used to describe the combinatorial
and geometric structure of P(T ) in some detail, although some interesting questions
(discussed at the end of this section) remain open.
Consider a codimension 1 face f of P(T ). The face f may be either a boundary
face of the moduli space M (viewed as a polyhedral complex) or an interior face.
In the latter case, f corresponds to a change of combinatorial type of Delaunay
triangulation from T toT ′, and it is well understood that the primitive such change
is given by a diagonal ﬂip , so f corresponds to a cyclic quadrilateral ABCD , where
inT the Delaunay triangulation has triangles (for example) ABC andCDA, while
in T ′, the triangles are DAB and BCD . On f , the quadrilateral ABCD can be
triangulated either way, but the dihedral angle along (either) diago nal is equal to
π.
Suppose now that f is a boundary face of M – in particular, this will mean that
none of the dihedral angles of the Euclidean structures in the inter ior of f are equal
to π. By Theorems 4.8 and 4.3, it follows that there is a simple cocycle c∗ of T ∗
where the inequality 4.3[(b)] becomes an equality. This means, by the geometric
estimates in the beginning of section 6, that the collar C ofc∗ is becoming long and
thin (that is, the conformal modulus of C diverges to ∞), and so f corresponds to
the Euclidean structure pinching oﬀ along the curve c∗. The following construction
(discussed in greater detail in an upcoming paper of the author) he lps visualize this
pinching oﬀ in terms of the more usual degeneration of hyperbolic su rfaces:
Consider a triangulated singular Euclidean surface ( S,E,P ). The data given by
(S,E,P ) (initially using a triangulation, though it is easy to show that the resu lt is
independent of triangulation) can be used to construct a cusped h yperbolic surface,
as follows:
(1) To each triangle t of the triangulation T of (S,E,P ), associate an ideal triangle
h(t).
(2) For each pair of adjacent triangles t1 =ABC andt2 =ABD ofT , we have the
log of the modulus of the cross-ratio of the four corresponding po ints:
r(t1,t 2) = log |AC||BD|
|BC ||AD|.
(3) For each pair of adjacent triangles t1 and t2 as above, glue the hyperbolic
triangles h(t1) and h(t2) along the edge corresponding to AB with shear (see,
eg, [18]) equal to r(t1,t 2).
· 21
It is not hard to see that if we start with a Euclidean structure ( S,E,P ), we will
wind up with a complete cusped hyperbolic structure (actually, it is suﬃcient, but
not necessary, to start with a Euclidean structure – some similarity structures will
give a complete structure also). The construction thus deﬁnes a m ap (certainly not
injective, but which can be shown to be surjective using the constr uction of [15; 7;
13]) between the moduli space of Euclidean structures with cone po ints and that of
complete ﬁnite-area hyperbolic structures. It can be shown (this was an important
part of [16; 20] for the case of genus 0) that the degeneration, a s above, of the
Euclidean structure on ( S,E,P ), corresponds precisely to the pinching oﬀ along a
simple closed curve of the hyperbolic structure on ( S,H (E),P ).
Remark. Another surjection between the space of singular Euclidean struc tures
and the space of cusped hyperbolic structures is well-known, and is discussed in the
well-known paper of Troyanov [24]. The two surjections are not the same – this
was remarked by C. T. McMullen.
