---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-002-13-regular-ideal-triangulations-and-topological
section_title: "Regular ideal triangulations and topological invariance"
section_number: 1.3
pages: 4-5
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
we restrict our attention to hyperbolic 3-manifolds M with at least one cusp. All we need
is a canonical set XM of 1e
cient ideal triangulations of M such that any two of these
triangulations are related by moves that preserve IT. From Theorem 1.1, we know that
we can use 23 and 32 moves for this purpose. Given the choice we will make for XM
below, it turns out that we will also need to use 02 and 20 moves to connect together
the triangulations of XM . Using the dual language of special spines, it is shown in [Mat07,
Lem.2.1.11] and [Pie88] (see also [Pet95, Prop.I.1.13]) that the 02 and 20 moves can be
derived from the 23 and 32 moves, as long as the triangulation has at least two tetrahedra.
However, the required sequence of 23 and 32 moves takes us out of our set XM , and it is
not clear that the triangulations the sequence passes through are 1e
cient.
Every cusped hyperbolic 3manifold M has a canonical cell decomposition [EP88] where
the cells are convex ideal polyhedra in H3. The cells can be triangulated into ideal tetrahedra,
with layered 
at tetrahedra inserted to form a bridge between two polyhedron faces that
are supposed to be glued to each other but whose induced triangulations do not match.
Unfortunately, it is not known whether any two triangulations of a 3-dimensional polyhedron
are related by 23 and 32 moves; the corresponding result trivially holds in dimension 2 and
nontrivially fails in dimension 5; [DLRS10, San06]. Nonetheless, it was shown by Gelfand-
Kapranov-Zelevinsky that any two regular triangulations of a polytope in Rn are related by
a sequence of geometric bistellar 
ips; [GKZ94]. Using the Klein model of H3, we de
ne
the notion of a regular ideal triangulation of an ideal polyhedron and observe that every
two regular ideal triangulations are related by a sequence of geometric 22, 23 and 32
moves. Our set XEP
M of ideal triangulations of a cusped hyperbolic manifold M consists
of all possible choices of regular triangulation for each ideal polyhedron, together with all
possible bridge regions of layered 
at tetrahedra joining the induced triangulations of each
identi
ed pair of polyhedron faces. From the geometric structure of the cell decomposition,
we obtain a natural semi-angle structure on each triangulation of XEP
M , which shows that they
are all 1-e
cient by Theorem 1.5, and so the 3D index is de
ned for each triangulation by
Theorems 1.1(a) and 1.2. We show that any two of these triangulations are related to each
other by a sequence of 23, 32, 02 and 20 moves through 1e
cient triangulations, the
moves all preserving the 3D index, using Theorems 1.1(b), 1.2 and 5.1. (The intermediate
triangulations are mostly also within XEP
M , although we sometimes have to venture outside of
the set brie
y.) Therefore we obtain a topological invariant of cusped hyperbolic 3manifolds
M .
Theorem 1.8. If M is a cusped hyperbolic 3-manifold, and T∈ XEP
M we have IM := IT is
well-de
ned.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 5
The next theorem is of independent interest, and may be useful for the problem of con-
tructing topological invariants of cusped hyperbolic 3-manifolds. For a de
nition of the
gluing equations of an ideal triangulation, see [NZ85, Thu77] and also Section 4.3 below.
Theorem 1.9. Fix a cusped hyperbolic 3-manifold M .
(a) For every T∈ XEP
M , there exists a solution ZT to the gluing equations of T which
recovers the complete hyperbolic structure on M . Moreover, all shapes of ZT have
non-negative imaginary part.
(b) If T, T′∈ XEP
M are related by 23, 32, 02 or 20 moves, then so are ZT and ZT′.
(c) For every T, the arguments of ZT give a semi-angle structure on T.
Remark 1.10 . In [HRS12], it is shown that a cusped hyperbolic 3manifold M admits an
ideal triangulation with strict angle structure if H1(M,∂M ; Z2) = 0 . All link complements
in the 3sphere satisfy this condition. Such triangulations admit index structures but it is
not known if they can be connected by 23 and 02 moves within the class of 1e
cient
triangulations.
Remark 1.11 . For a typical cusped hyperbolic manifold, one expects that the Epstein-Penner
ideal cell decomposition consists of ideal tetrahedra, i.e., that XEP
M consists of one element.
Many examples of such cusped hyperbolic manifolds appear in the census [CDW] and also
in [Aki01, GS10].
Remark 1.12 . In a later paper we will extend this work in the following ways:
• extend the domain of the 3D index IT([ϖ]) to [ϖ]∈ H1(∂M ; 1
2 Z) such that 2[ϖ]∈
Ker(H1(∂M ; Z)→H1(M; Z/2Z)),
• give a de
nition of the 3D index using singular normal surfaces in M .
Remark 1.13 . Theorem 1.8 constructs a family of q-series IM([ϖ])(q) (parametrized by [ϖ]∈
H1(∂M, Z)) associated to a cusped hyperbolic manifold M . When M = S3\K is the
complement of a knot K, we can choose [ϖ] = µ to be the homology class of the meridian
and consider the series
(2) Itot
K (q) =
∑
e∈Z
IM(eµ)(q)
Since the semi-angle structures of Theorem 1.9 have zero holonomy at all peripheral curves,
it can be shown that Itot
K (q) is well-de
ned. It turns out that Itot
K (q) is closely related to the
state-integral invariants of Andersen-Kashaev and Kashaev-Luo-Vartanov [AK14, KL V12].
The relation between state-integrals of the quantum dilogarithm and q-series is explained in
detail in [GK]. An empirical study of the asymptotics of the series Itot
41 (q) is given in [GZ].
