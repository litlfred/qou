---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-001-11-the-3d-index-of-dimofte-gaiotto-gukov
section_title: "The 3D index of Dimofte-Gaiotto-Gukov"
section_number: 1.1
pages: 1-4
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
1.2. Index structures and 1-e
ciency 3
1.3. Regular ideal triangulations and topological invariance 4
1.4. Plan of the paper 5
2. De
nitions 6
3. Index structures and 1e
ciency 9
4. A review of the index of an ideal triangulation 16
4.1. The tetrahedron index and its properties 16
4.2. The degree of the tetrahedron index 17
4.3. Angle structure equations 17
4.4. Peripheral equations 18
4.5. The index of an ideal triangulation 19
4.6. Choice of edges in the summation for index 20
4.7. A reformulation of the de
nition of the index 24
4.8. Invariance of index under isotopy of peripheral curve 26
5. Invariance of index under the 02 move 29
6. The XEP
M class of triangulations 32
6.1. Subdivisions of the EpsteinPenner decomposition 32
Date : January 14, 2015.
S.G. was supported in part by grant DMS-0805078 of the US National Science Foundation. C.D.H,
J.H.R, H.S were supported by the Australian Research Council grant DP1095760.
2010 Mathematics Classi
cation. Primary 57N10, 57M50. Secondary 57M25.
Key words and phrases: ideal triangulations, hyperbolic 3-manifolds, gluing equations 3D index, invariants,
1-e
cient triangulations.
1
2 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
6.2. Regular triangulations 34
6.3. Interpreting 
ip moves using 23 moves 39
6.4. Moving paths in the 1skeleton of the associahedron using 23 and 02 moves 40
7. Computations 43
7.1. How to compute the coe
cients of a q-series 43
7.2. The index of the 41 knot complement 44
7.3. The index of the sister of the 41 knot complement 45
7.4. The index of the 52 knot complement 45
7.5. The index of the (−2, 3, 7) pretzel knot complement 47
7.6. The index of the 61 knot complement 48
7.7. The index of the 72 knot complement 49
7.8. Acknowledgments 51
Appendix A. The 23 move 51
References 57
1. Introduction
1.1. The 3D index of Dimofte-Gaiotto-Gukov. The goal of this paper is to convert the
index of an ideal triangulation T (a remarkable collection of Laurent series in q1/2 introduced
by Dimofte-Gaiotto-Gukov [DGG14, DGG13] and further studied in [Garb]) to a topological
invariant of oriented cusped hyperbolic 3-manifolds M . Our goal will be achieved in two
steps.
The 
rst step identi
es the existence of an index structure of T (a necessary and su
cient
condition for the existence of the index of T; see [Garb]) with the non-existence of sphere or
non vertex-linking torus normal surfaces of T; see Theorem 1.2 below. Such ideal triangula-
tions are called 1-e
cient in [JR03, KR05]. The unexpected connection between the index of
an ideal triangulation (a recent quantum object) and the classical theory of normal surfaces
places restrictions on the topology of M ; see Remark 1.3 below.
The second step constructs a canonical collection XEP
M of triangulations of the Epstein-
Penner ideal cell decomposition of a cusped hyperbolic 3-manifold M , such that the index
behaves well with respect to 23 and 02 moves that connect any two members of XEP
M . The
index of those triangulations then gives the desired topological invariant of M ; see Theorem
1.8 below.
We should point out that normal surfaces were also used by Frohman-Bartoszynska [FKB08]
in an attempt to construct topological invariants of 3-manifolds, in the style of a Turaev-Viro
TQFT. Strict angle structures (a stronger form of an index structure) play a role in quan-
tum hyperbolic geometry studied by Baseilhac-Benedetti [BB05, BB07]. In the recent work
of Andersen-Kashaev [AK14], strict angle structures were used as su
cient conditions for
convergence of analytic state-integral invariants of ideal triangulations. The latter invariants
are expected to depend on the underlying cusped 3-manifold and to form a generalization
of the Kashaev invariant [Kas97]. The q-series of Theorem 1.8 below are q-holonomic, of
Nahm-type and, apart from a meromorphic singularity at q = 0, admit analytic continuation
in the punctured unit disc.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 3
Before we get to the details, we should stress that the origin of the 3D index is the
exciting work of Dimofte-Gaiotto-Gukov [DGG14, DGG13] (see also [BDP]) who studied
gauge theories with N = 2 supersymmetry that are associated to an ideal triangulation T
of an oriented 3-manifold M with at least one cusp. The low-energy limit of these gauge
theories gives rise to a partially de
ned function, the so-called 3D index
(1) I :{ideal triangulations }−→ Z((q1/2))H1(∂M ;Z), T↦→IT([ϖ])∈ Z((q1/2))
for [ϖ]∈ H1(∂M ; Z). 1 The function I is only partially de
ned because the expression for
the 3D index may not converge. The above gauge theories provide an analytic continuation
of the coloured Jones polynomial and play an important role in Chern-Simons perturbation
theory and in categori
cation. Although the gauge theory depends on the ideal triangulation
T, and the 3D index in general may not be de
ned, physics predicts that the gauge theory
ought to be a topological invariant of the underlying 3-manifold M . Recall that any two
ideal triangulations of a cusped 3-manifold are related by a sequence of 2-3 moves [Mat87,
Mat07, Pie88]. In [Garb] the following was shown. For the de
nition of an index structure,
see Section 2.
Theorem 1.1. (a) IT is well-de
ned if and only if T admits an index structure .
(b) If T and T′ are related by a 23 move and both admit an index structure, then IT =IT′.
1.2. Index structures and 1-e
ciency.
Theorem 1.2. An ideal triangulation T of an oriented 3-manifold with cusps admits an
index structure if and only if T is 1-e
cient.
The above theorem has some consequences for our sought topological invariants.
Remark 1.3 . 1-e
ciency of T implies restrictions on the topology of M : it follows that M is
irreducible and atoroidal. Note that here by atoroidal , we mean that any embedded torus is
either compressible or boundary parallel. It follows by Thurston's Hyperbolization Theorem
in dimension 3 that M is hyperbolic or small Seifert-
bred.
Remark 1.4 . If K is the connected sum of the 41 and 52 knots, or K′ is the Whitehead
double of the 41 knot and T is any ideal triangulation of the complement of K or K′, then T
is not 1-e
cient, thus IT never exists. On the other hand, the (coloured) Jones polynomial,
the Kashaev invariant and the PSL(2, C)-character variety of K and K′ happily exist; see
[Jon87, Kas97, CCG +94].
Theorem 1.5. Let T be an ideal triangulation of an oriented atoroidal 3manifold with at
least one cusp. If T admits a semiangle structure then T is 1e
cient.
Remark 1.6 . Taut and strict angle structures are examples of semi-angle structures, and for
these cases this is proved in [KR05, Thm.2.6]. In Section 3, we give a brief outline of the
argument for a general semiangle structure.
1 Here and below we will use the notation M for both a cusped hyperbolic 3-manifold and the corresponding
compact manifold with boundary ∂M consisting of a disjoint union of tori; the intended meaning should be
clear from the context.
4 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Remark 1.7 . In Corollary 3.4, we note that a construction of Lackenby produces triangu-
lations with taut angle structures, which are therefore 1e
cient, on all irreducible cusped
3manifolds containing no essential annulus. However, it is not clear that the triangulations
produced by this construction are connected by the appropriate 23 and 02 moves, so we
cannot prove that the 3D index is independent of the choice of taut triangulation for the
manifold.
