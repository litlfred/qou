---
doc_id: arxiv-1207.6711v1
doc_title: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1207.6711v1.pdf
source_sha256: 320c4301ac66fff1
doc_brief: "GLUING EQUATIONS FOR PGL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS — In [11] we parametrized boundary-unipotent representations of a 3-manifold group into SL(n, C) using Ptolemy coordinates, which were"
---
1.1. Thurston’s gluing equations 2
1.2. Our main results 3
1.3. Computations and applications 5
1.4. Overview of the Paper 5
1.5. Acknowledgement 6
2. Concrete triangulations 6
2.1. Face pairing permutations 7
3. Thurston’s gluing equations 8
3.1. Symplectic properties of the gluing equations 8
4. Generalized gluing equations 9
4.1. Simplex coordinates 9
4.2. Symmetries of a simplex 9
4.3. Shape assignments 9
4.4. Gluing equations for oriented triangulations 10
4.5. The pullback of a shape assignment under a symmetry 13
4.6. Gluing equations for general concrete triangulations 14
5. Review of Ptolemy coordinates 14
5.1. Ptolemy assignments for ordered triangulations 14
Date: July 25, 2012.
S. G. and C. Z. were supported in part by the NSF.
1991 Mathematics Classiﬁcation. Primary 57N10. Secondary 57M27.
Key words and phrases: Generalized gluing equations, shape coordinates, Ptolemy coordinates, Neumann-
Zagier datum.
1
arXiv:1207.6711v1  [math.GT]  28 Jul 2012
2 STA VROS GAROUF ALIDIS, MATTHIAS GOERNER, AND CHRISTIAN K. ZICKERT
5.2. The pullback of a Ptolemy assignment under a symmetry 15
5.3. Ptolemy assignments for general concrete triangulations 16
6. From Ptolemy coordinates to shapes 17
6.1. Proof for edge equations 18
6.2. Proof for face equations 19
6.3. Proof for internal equations 19
7. Symplectic properties and quantum topology 20
7.1. Applications in quantum topology 23
8. Decorations 25
8.1. Generic decorations, Ptolemy coordinates and shapes 26
9. The natural cocycle of a generic decoration 28
9.1. Truncated and doubly truncated simplices 28
9.2. Cocycles 29
9.3. The natural cocycle of a generic decoration 29
10. Explicit formulas for the natural cocycles 31
10.1. Diamond and ratio coordinates 31
10.2. X-coordinates 33
10.3. From natural (SL( n, C),N )-cocycles to natural (PGL(n, C),B,H )-cocycles. 36
11. From shape assignments to cocycles 39
12. Duality 41
13. The cusp equations 41
13.1. Simplifying the cusp equations 42
14. Example: the ﬁgure-eight knot 43
References 45
1. Introduction
1.1. Thurston’s gluing equations. Thurston’s gluing equations are a system of polyno-
mial equations deﬁned for a compact 3-manifoldM together with a topological ideal triangu-
lationT of the interior of M. The gluing equations were introduced to concretely construct
a complete hyperbolic structure on M from a (suitable) solution to the gluing equations.
Although Thurston only considered manifolds whose boundary components are tori (a
necessary condition for the existence of a solution yielding a hyperbolic structure), the gluing
equations are deﬁned for manifolds with arbitrary (possibly empty) boundary. The existence
of hyperbolic structures is of no concern to us here.
The gluing equations consist of an edge equation for each 1 cell of T and a cusp equation
for each generator of the fundamental group of each boundary component ofM. The system
may be written in the form
(1.1)
∏
j
z
Aij
j
∏
j
(1−zj)Bij =ϵi,
where A and B are matrices whose columns are parametrized by the simplices of T and
ϵi is a sign (which is 1 for the edge equations). Each variable zj may be thought of as
GLUING EQUATIONS FOR PGL( n, C)-REPRESENTATIONS OF 3-MANIFOLDS 3
an assignment of an ideal simplex shape to a simplex of T . If the shapes zj∈ C\{ 0, 1}
satisfy (1.1), as well as some extra conditions on the arguments of zi, the ideal simplices
glue together to form a complete hyperbolic structure on M. Ignoring the cusp equations
gives structures that are incomplete. This gives rise to an eﬃcient algorithm for constructing
hyperbolic structures, which has been eﬀectively implemented in software packages such as
SnapPea [18], Snap [12], and SnapPy [3].
Among the numerous important features of the gluing equations we will focus on two:
(a) The symplectic property of the exponent matrix ( A|B) of the gluing equations due
to Neumann and Zagier [15].
(b) The link to PGL(2, C) representations via a developing map
(1.2) V2(T )→{ρ: π1(M)→ PGL(n, C)}
/
Conj
whereV2(T ) denotes the aﬃne variety of solutions in C\{0, 1} to the edge equations,
and the right hand side denotes the set of conjugacy classes of representations of
π1(M) in PGL(2, C).
We may thus think of V2(T ) as a parametrization of representations. Note, however, that
V2(T ) depends on the triangulation, and that the developing map need neither be onto nor
ﬁnite to one. However, if the triangulation is suﬃciently ﬁne (a single barycentric subdivision
suﬃces) the developing map is onto, i.e. every representation is detected (including reducible
ones). A solution satisfying the cusp equations as well gives rise to a representation that is
boundary-unipotent, i.e. takes peripheral curves to unipotent elements. Our goal is to
• Extend Thurston’s gluing equations to PGL( n, C) preserving the above features for
n = 2, using suitable shape parameters.
• Relate the Ptolemy parameters of [11] to the shape parameters via a monomial map.
The Ptolemy and shape coordinates were inspired by theA-coordinates andX -coordinates
on higher Teichm¨ uller spaces due to Fock and Goncharov [8]. Note, however, that Fock and
Goncharov study surfaces, whereas we study 3-manifolds. Shape coordinates for n = 3 have
been studied independently by Bergeron, Falbel and Guilloux [1].
There is a very interesting interplay between the shape coordinates and the Ptolemy
coordinates. The groups PGL( n, C) and SL(n, C) are Langlands dual, and we believe that
this interplay is a 3-dimensional aspect of the duality discussed for surfaces by Fock and
Goncharov [8, p. 33]. The duality is particularly explicit when all the boundary components
of M are tori, see Proposition 12.3.
While the Ptolemy variety naturally parametrizes boundary-unipotent representations,
the gluing equations also parametrize representations that are not necessarily boundary-
unipotent. The boundary-unipotent ones can be determined by adding additional equations,
which are generalizations of Thurston’s cusp equations. This is studied in Section 13.
