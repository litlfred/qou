---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-002-13-regular-ideal-triangulations-and-topological
section_title: "Regular ideal triangulations and topological invariance"
section_number: 1.3
pages: 4-5
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
we restrict our attention to hyperbolic 3-manifoldsM with at least one cusp. All we need
is a canonical set XM of 1–eﬃcient ideal triangulations ofM such that any two of these
triangulations are related by moves that preserveIT. From Theorem 1.1, we know that
we can use 2–3 and 3–2 moves for this purpose. Given the choice we will make forXM
below, it turns out that we will also need to use 0–2 and 2–0 moves to connect together
the triangulations ofXM. Using the dual language of special spines, it is shown in [Mat07,
Lem.2.1.11] and [Pie88] (see also [Pet95, Prop.I.1.13]) that the 0–2 and 2–0 moves can be
derived from the 2–3 and 3–2 moves, as long as the triangulation has at least two tetrahedra.
However, the required sequence of 2–3 and 3–2 moves takes us out of our setXM, and it is
not clear that the triangulations the sequence passes through are 1–eﬃcient.
Every cusped hyperbolic 3–manifoldM has a canonicalcell decomposition[EP88] where
the cells are convex ideal polyhedra inH3. The cells can be triangulated into ideal tetrahedra,
with layered ﬂat tetrahedra inserted to form a bridge between two polyhedron faces that
are supposed to be glued to each other but whose induced triangulations do not match.
Unfortunately, it is not known whether any two triangulations of a 3-dimensional polyhedron
are related by 2–3 and 3–2 moves; the corresponding result trivially holds in dimension 2 and
nontrivially fails in dimension5; [DLRS10, San06]. Nonetheless, it was shown by Gelfand-
Kapranov-Zelevinsky that any tworegulartriangulations of a polytope inRn are related by
a sequence of geometric bistellar ﬂips; [GKZ94]. Using the Klein model ofH3, we deﬁne
the notion of aregular ideal triangulation of an ideal polyhedron and observe that every
two regular ideal triangulations are related by a sequence of geometric 2–2, 2–3 and 3–2
moves. Our set XEP
M of ideal triangulations of a cusped hyperbolic manifoldM consists
of all possible choices of regular triangulation for each ideal polyhedron, together with all
possible “bridge regions” of layered ﬂat tetrahedra joining the induced triangulations of each
identiﬁed pair of polyhedron faces. From the geometric structure of the cell decomposition,
we obtain a natural semi-angle structure on each triangulation ofXEP
M , which shows that they
are all 1-eﬃcient by Theorem 1.5, and so the 3D index is deﬁned for each triangulation by
Theorems 1.1(a) and 1.2. We show that any two of these triangulations are related to each
other by a sequence of 2–3, 3–2, 0–2 and 2–0 moves through 1–eﬃcient triangulations, the
moves all preserving the 3D index, using Theorems 1.1(b), 1.2 and 5.1. (The intermediate
triangulations are mostly also withinXEP
M , although we sometimes have to venture outside of
the set brieﬂy.) Therefore we obtain a topological invariant of cusped hyperbolic 3–manifolds
M.
Theorem 1.8. If M is a cusped hyperbolic 3-manifold, andT∈ XEP
M we haveIM := IT is
well-deﬁned.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 5
The next theorem is of independent interest, and may be useful for the problem of con-
tructing topological invariants of cusped hyperbolic 3-manifolds. For a deﬁnition of the
gluing equations of an ideal triangulation, see [NZ85, Thu77] and also Section 4.3 below.
Theorem 1.9.Fix a cusped hyperbolic 3-manifoldM.
(a) For everyT∈ XEP
M , there exists a solutionZT to the gluing equations ofT which recovers
the complete hyperbolic structure on M. Moreover, all shapes of ZT have non-negative
imaginary part.
(b) If T, T′∈ XEP
M are related by 2–3, 3–2, 0–2 and 2–0 moves, then so areZT and ZT′.
(c) For everyT, the arguments ofZT give a semi-angle structure onT.
Remark 1.10. In [HRS12], it is shown that a cusped hyperbolic 3–manifoldM admits an
ideal triangulation with strict angle structure ifH1(M,∂M ; Z2) = 0. All link complements
in the 3–sphere satisfy this condition. Such triangulations admit index structures but it is
not known if they can be connected by 2–3 and 0–2 moves within the class of 1–eﬃcient
triangulations.
Remark 1.11. For a typical cusped hyperbolic manifold, one expects that the Epstein-Penner
ideal cell decomposition consists of ideal tetrahedra, i.e., thatXEP
M consists of one element.
Many examples of such cusped hyperbolic manifolds appear in the census [CDW] and also
in [Aki01, GS10].
Remark 1.12. In a later paper we will extend this work in the following ways:
• extend the domain of the 3D indexIT([ϖ]) to [ϖ]∈ H1(∂M ; 1
2 Z) such that 2[ϖ]∈
Ker(H1(∂M ; Z)→H1(M; Z/2Z)),
• give a deﬁnition of the 3D index using singular normal surfaces inM.
Remark 1.13. Theorem 1.8 constructs a family ofq-seriesIM([ϖ])(q) (parametrized by[ϖ]∈
H1(∂M, Z)) associated to a cusped hyperbolic manifold M. When M = S3\K is the
complement of a knotK, we can choose[ϖ] = µ to be the homology class of the meridian
and consider the series
(2) Itot
K (q) =
∑
e∈Z
IM(eµ)(q)
Since the semi-angle structures of Theorem 1.9 have zero holonomy at all peripheral curves,
it can be shown thatItot
K (q) is well-deﬁned. It turns out thatItot
K (q) is closely related to
the state-integral invariants of Andersen-Kashaev and Kashaev-Luo-Vartanov [AK, KLV12].
The relation between state-integrals of the quantum dilogarithm andq-series is explained in
detail in [GK]. An empirical study of the asymptotics of the seriesItot
41 (q) is given in [GZ].
