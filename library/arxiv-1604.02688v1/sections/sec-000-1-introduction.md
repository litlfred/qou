---
doc_id: arxiv-1604.02688v1
doc_title: "THE 3D-INDEX AND NORMAL SURFACES"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1604.02688v1.pdf
source_sha256: bdcafe379519287c
doc_brief: "THE 3D-INDEX AND NORMAL SURFACES — Dimofte, Gaiotto and Gukov introduced a powerful invariant, the 3D-index, associated to a suitable ideal triangulation of a 3-manifold with torus boundary"
---
Acknowledgements 3
2. The tetrahedral index 4
3. Notation and conventions for triangulated 3-manifolds 5
3.1. Gluing equations 5
3.2. Generalised angle structures 6
4. The 3D-index of an ideal triangulation 6
5. Dependence on the choice of triangulation 8
6. Some Q-normal surface theory 10
6.1. Construction of spun normal surfaces 11
6.2. Geometric generators for Q-normal classes 13
7. Combinatorics of ideal triangulations and integer normal surface theory 16
7.1. Geometric generators for integer Q-normal classes 19
8. The 3D-index via normal surfaces 20
8.1. Convergence of the index sum 21
8.2. Non 1-eﬃcient ideal triangulations 24
9. Invariance under 2-3 and 0-2 moves 25
10. Generalised normal surfaces 27
10.1. Generalised normal and spun normal surfaces 27
10.2. Degrees of index terms 29
10.3. Normalisation and barriers 30
11. Some examples 35
11.1. Solid torus 35
11.2. Trefoil complement 35
11.3. T2× I 36
11.4. A toroidal example 36
1
arXiv:1604.02688v1  [math.GT]  10 Apr 2016
2 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, NEIL R. HOFFMAN, AND J. HYAM RUBINSTEIN
11.5. m009 37
12. Notes on connectedness of the 1-eﬃcient Pachner Graph 39
12.1. A census of ideal triangulations 41
12.2. Two tetrahedron ideal triangulations 42
12.3. Angle Structures, 1-eﬃciency and Pachner moves 44
12.4. Connected components of normal surfaces 45
Appendix A. Generalised angle structures and the Euler characteristic 50
A.1. Euler characteristic from generalised angle structures 51
References 55
1. Introduction
Recently, the physicists Dimofte, Gaiotto and Gukov [DGG13, DGG14] introduced a pow-
erful new invariant for a compact orientable 3-manifoldM with non-empty boundary∂M
consisting of tori, called the3D-index. This invariant arises from a gauge theory withN = 2
supersymmetry under a low energy limit, and seems to contain a great deal of information
about the geometry and topology of the manifold. The 3D-index is a collection ofq-series,
i.e. formal Laurent series inq1/2, deﬁned as an inﬁnite sum over integer weights attached to
the edges of a chosen ideal triangulationT of M. The q-series IT(b) are parametrised by a
choice of peripheral homology classb∈H1(∂M ; Z).
Our goal is to explain how the 3D-index can be viewed as a generating series of normal
surfaces onT; see Deﬁnition 8.1 and Corollary 8.2 below. Normal surfaces depend heavily on
the ideal triangulation whereas the 3D-index should not. Our results show a connection of
the 3D-index with classical normal surface theory, and fulﬁll a ‘folk dream’ of constructing
topological invariants of 3-manifolds using normal surfaces.
In this paper we ﬁrst recall how the 3D-index of an ideal triangulation is deﬁned, following
[GHRS15], and discuss some of its key properties. Throughout the paper, by a triangulation
ofacompact3-manifoldwemeanan ideal triangulationsinthesenseofThurston[Thu77](see
also [NZ85, Neu92]). Physics predicts that the 3D-index should give atopological invariant
of the underlying manifoldM, but this is not known in general. In fact, the sum deﬁning the
3D-index need not even converge (as a formal Laurent series) for all ideal triangulationsT.
But we can characterise the good triangulations using thenormal surface theorydeveloped
by Haken [Hak61b, Hak61a]. (Haken’s theory applies to ideal triangulations, when restricting
to closed normal surfaces.) In fact, the work of [GHRS15] shows the index sum forIT(b)
converges for allb∈H1(∂M ; Z) if and only if the triangulation is1-eﬃcient, i.e. contains no
embedded closed normal surfacesS of Euler characteristicχ(S)≥ 0 except peripheral tori.
By work of Matveev and Piergallini, (see [Mat87, Mat03, Pie88, BP97]), any two ideal
triangulations T, T′ (with at least 2 tetrahedra) of a given compact 3-manifoldM with non-
empty boundary can be connected by a sequence of 2-3 and 3-2 Pachner moves. Similarly,
we can also consider 0-2 and 2-0 moves on a triangulation as shown in Figure 4 below.
The work of [Gar15, GHRS15] shows that the index is invariant under 2-3/3-2 and 0-2/2-0
moves provided all ideal triangulations involved are 1-eﬃcient. However it is not currently
THE 3D-INDEX AND NORMAL SURF ACES 3
known whether any two 1-eﬃcient triangulations of a given manifold can be connected by
2-3/3-2 and 0-2/2-0 moves preserving 1-eﬃciency.
We then give a new formulation of the deﬁnition of index as a sum over certainsingular
normal surfaces. The minimum degree of each term in this sum then has a simple geometric
interpretation involving theEuler characteristicand the number ofdouble arcsof the corre-
sponding surface. This leads to new, more direct proofs of results on the convergence of the
series for the 3D-index. We also introduce a class of embeddedgeneralised normal surfaces,
and show how to express the index as a sum over terms corresponding to these embedded
surfaces.
Next we show that the work of Neumann [Neu92] on combinatorics of ideal triangula-
tions can be reinterpreted to give a precise description of the set Q(T; Z) of all integer
solutions to theQ-matching equations of Tollefson [Tol98]. Each such solutionS represents
a (possibly singular) spun normal surface [KR04, Til08] with well-deﬁned homology class
[S]2∈H2(M,∂M ; Z/2Z) and boundary [∂S]∈H1(∂M ; Z) such that the mod2 reduction of
[∂S] is the image of[S] under the boundary map∂∗ :H1(M; Z/2Z)→H1(∂M ; Z/2Z). Fur-
ther, each pair(a,b )∈H2(M,∂M ; Z/2Z)×H1(∂M ; Z) such that∂∗a =b mod 2 arises in this
way, and theQ-normal classesS with [S]2 = 0 and [∂S] = 0 are the integer linear combina-
tions of the “edge solutions” and the “tetrahedral solutions” constructed by Kang-Rubinstein
[KR04].
We then show that the deﬁnition of 3D-index can be extended to give aq-series Ia
T(b) for
each (a,b ) as above; this is a sum overQ-normal classesS with [S] =a and [∂S] =b modulo
tetrahedral solutions. The previous deﬁnition of 3D-index only applies to the cases where
a = 0 and b∈H1(∂M ; 2Z); we haveI0
T(b) =IT(2b) in the notation of [GHRS15]. HereI0
T(b)
is also deﬁned forb∈ K = Ker (H1(∂M ; Z)→H1(M; Z/2Z)).
We then give some computations of the 3D-index, including an example showing that
that the series for the 3D-indexIa
T(b) can sometimes converge forb⁄= 0 even when the
triangulation T is not 1-eﬃcient (so the series forI0
T(0) does not converge).
We conclude with some discussion of experimental results on the connectedness of the set
of 1-eﬃcient ideal triangulations of a given manifold under 2-3/3 and 0-2/2-0 Pachner moves.
(Recall that such moves do not change the 3D-index.) In particular, we ﬁnd examples of
1-eﬃcient triangulations of the solid torus with six tetrahedra that cannot be connected
by sequences of 2-3/3-2 moves through 1-eﬃcient triangulations. These triangulations can,
however, be connected via 1-eﬃcient triangulations if 0-2 and 2-0 moves are also allowed;
hence they have the same 3D-index.
Finally, the appendix gives some results on generalised angle structures and Euler charac-
teristic for Q-normal surfaces; these extend well-known results of Luo-Tillmann [LT08] for
closed normal surfaces.
