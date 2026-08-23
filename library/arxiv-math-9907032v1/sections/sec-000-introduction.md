---
doc_id: arxiv-math-9907032v1
doc_title: "Combinatorial optimization in geometry"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 9907032v1.pdf
source_sha256: 1850f32a2375c8ce
doc_brief: "Combinatorial optimization in geometry (Rivin) — extends and unifies results on ideal polyhedra in H³ to singular Euclidean structures on surfaces, possibly with infinitely many singularities."
---
In the paper [20] we gave the following description of the angles of ide al polyhedra
in H3: let P be a combinatorial polyhedron, and let A : E(P ) → [0,π ) be a
function. Then, there exists an ideal polyhedron combinatorially eq uivalent to P ,
such that the exterior angle at every edge e is given by A(e) if and only if the sum
of A(e) over all edges adjacent to a vertex of P is equal to 2 π, while the sum of
A(e) over any nontrivial cutset of edges of P (that is, a collection of edges which
separates the 1-skeleton of P , but which are not all adjacent to the same vertex) is
strictly greater than 2π. Furthermore, it was shown in [19] that the dihedral angles
determine the ideal polyhedron up to congruence.
It was observed in [18; 19] that this was a special case of the proble m of char-
acterizing the Delaunay tessellations of singular Euclidean surfaces – there is a
canonical way to associate ideal polyhedra to Delaunay triangulatio ns of a convex
ﬂat disk with convex polygonal boundary. The general situation is d escribed in
detail below, but one of the goals of this paper is to extend the char acterization
1This is a slightly modiﬁed version of a preprint ﬁrst distrib uted in September 1996
· 2
above to the completely general case of singular Euclidean surface s with boundary.
This is duly done, see, eg, Theorems 3.1, 4.8, 4.11:
Consider a surface S, equipped with a Euclidean (or, more generally, a similarity)
structureE, possibly with cone singularities. Assume that there is a discrete colle c-
tionP = {p1,...,p n} of distinguished points on S, and assume that P contains the
cone points of S. There is a canonical tessellation attached to the triple ( S,E,P )
– the so-called Delaunay tessellation (see, eg, [5; 19]). The moduli space M of such
triples is then naturally decomposed into disjoint subsets MT , corresponding to the
diﬀerent combinatorial types T of the Delaunay tessellation. This is a canonical
decomposition of M. In the paper [19] I studied the subsets MT , and showed that
the dihedral angles of the Delaunay triangulation are natural coordinates ( moduli)
for MT , which induce on MT the structure of a convex polytope.
The aformentioned decompositon of moduli space then becomes a p olyhedral
complex, the top-dimensional cells of which corresponds to Delauna y tessellations
which are triangulations, while pairs of adjacent top-dimensional ce lls diﬀer combi-
natorially by a diagonal ﬂip. This decomposition is closely related to the well-known
Harer complex (see, eg, [10]). As mentioned above, the top-dimens ional cells of
this complex are identiﬁed along some of their lower-dimensional face s, while other
lower dimensional faces correspond to degenerations of the Euclid ean structures
of (S,E,P ). It is then clear that the polyhedral structure of the cells MT is of
considerable interest. However, in [19] only an indirect description w as given – MT
was shown to be a convex polytope by virtue of being an image of anot her convex
polytope under a fairly complicated linear map. The methods of [20] co me from
hyperbolic geometry and are based on the study of dihedral angles of compact hy-
perbolic polyhedra in [16], so do not easily generalize to the case of gen eral singular
Euclidean and similarity structures alluded to above. In the current paper, methods
of mathematical programming and the results of [19] are used to giv e a completely
general extension of the result of [20] (described in the beginning o f this Introduc-
tion) to Delaunay triangulations of arbitrary singular surfaces (Th eorems 3.1, 4.8,
4.11). Since the arguments do not depend on the results of [20], we h ave a diﬀerent,
essentially combinatorial, proof of a principal result (Theorem 0.1) o f that paper
(Theorem 4.11 here). The other result of [20] – the characterizat ion of ﬁnite-volume
polyhedra – is, seemingly, not accessible by current methods. The a bove-mentioned
result permit us to get good understanding of the boundary struc ture of the cells
MT , and, consequently, of M itself. Since MT ﬁbers (in multiple ways) over the
moduli space of ﬁnite area hyperbolic structures on S, some information is obtained
about the latter moduli space.
In addition, the methods, combined with a geometric estimate, allow u s to give
a description of dihedral angles of Delaunay tessellations of ( S,E,P ), where (S,P )
is not necessarily of ﬁnite topological type (Theorem 6.1). This stop s well short
of solving the moduli problem, unlike in the ﬁnite case, but a conjectu ral picture
seems fairly clear.
The methods are also brought to bear onto some questions in combin atorial
geometry, and to provide eﬃcient algorithms for solving the “invers e problem” of
determining when a combinatorial complex, or a combinatorial comple x equipped
with dihedral angle data, can be realized as the Delaunay tessellation of a singular
Euclidean surface.
· 3
In addition, we use our methods to prove some observations of Cas son on ideally
triangulated 3-manifolds. That subject is not so far removed from the geometry of
similarity and Euclidean structures on surfaces. Indeed, the basic idea of [19] is to
study the similarity and Euclidean structures by means of construc ting a canonical
hyperbolic polyhedral complex as a “cone” over the surface being s tudied.
The plan of the paper is as follows: In section 1 the relevant deﬁnition s and
results of [19] are recalled. In section 2 we describe a set of constr aints which must
be satisﬁed by the dihedral angles of any (not necessarily Delaunay ) triangulation.
In section 3 we show that these constraints are actually suﬃcient u nder the as-
sumption that the triangulation is Delaunay, and reﬁne them to a minim al set of
constraints. In section 6 we show how the results apply to ideal poly hedra, and
in particular to characterize inﬁnite ideal polyhedra. In section 7 we comment on
the boundary structure of the moduli space of singular Euclidean s tructures, and
describe a correspondence between the Euclidean and hyperbolic s tructures, which
hopefully clariﬁes the picture. In section 10 we apply the methods of section 3 to
the study of ideal triangulations of 3-manifolds. In section 5 we give a network
ﬂow interpretation of the results of section 4. In addition to the int rinsic interest,
this allows us to give eﬃcient algorithms for deciding whether a weighed graph is
the 1-skeleton of a Delaunay triangulation (with weights being the dih edral angles).
These computational issues are discussed in section 8. In section 9 we discuss some
combinatorial-geometric applications of the results of section 4.
