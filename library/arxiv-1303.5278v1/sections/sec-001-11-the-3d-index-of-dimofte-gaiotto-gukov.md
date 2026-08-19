---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-001-11-the-3d-index-of-dimofte-gaiotto-gukov
section_title: "The 3D index of Dimofte-Gaiotto-Gukov"
section_number: 1.1
pages: 1-4
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
1.2. Index structures and 1-eﬃciency 3
1.3. Regular ideal triangulations and topological invariance 4
1.4. Plan of the paper 5
2. Deﬁnitions 6
3. Index structures and 1–eﬃciency 9
4. A review of the index of an ideal triangulation 16
4.1. The tetrahedron index and its properties 16
4.2. The degree of the tetrahedron index 17
4.3. Angle structure equations 17
4.4. Peripheral equations 18
4.5. The index of an ideal triangulation 19
4.6. Choice of edges in the summation for index 20
4.7. A reformulation of the deﬁnition of the index 24
4.8. Invariance of index under isotopy of peripheral curve 26
5. Invariance of index under the 0–2 move 29
6. The XEP
M class of triangulations 32
6.1. Subdivisions of the Epstein–Penner decomposition 32
Date: October 31, 2018.
S.G. was supported in part by grant DMS-0805078 of the US National Science Foundation. C.D.H,
J.H.R, H.S are supported by the Australian Research Council grant DP1095760.
2010 Mathematics Classiﬁcation.Primary 57N10, 57M50. Secondary 57M25.
Key words and phrases: ideal triangulations, hyperbolic 3-manifolds, gluing equations 3D index, invariants,
1-eﬃcient triangulations.
1
arXiv:1303.5278v1  [math.GT]  21 Mar 2013
2 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
6.2. Regular triangulations 34
6.3. Interpreting ﬂip moves using 2–3 moves 39
6.4. Moving paths in the 1–skeleton of the associahedron using 2–3 and 0–2 moves 41
7. Computations 43
7.1. How to compute the coeﬃcients of aq-series 43
7.2. The index of the 41 knot complement 44
7.3. The index of the sister of the41 knot complement 45
7.4. The index of the 52 knot complement 45
7.5. The index of the (−2, 3, 7) pretzel knot complement 47
7.6. The index of the 61 knot complement 48
7.7. The index of the 72 knot complement 49
7.8. Acknowledgments 51
Appendix A. The 2–3 move 51
References 57
1. Introduction
1.1. The 3D index of Dimofte-Gaiotto-Gukov.The goal of this paper is to convert the
index of an ideal triangulationT (a remarkable collection of Laurent series inq1/2 introduced
by Dimofte-Gaiotto-Gukov [DGGb, DGGa] and further studied in [Garb]) to a topological
invariant of oriented cusped hyperbolic 3-manifoldsM. Our goal will be achieved in two
steps.
The ﬁrst step identiﬁes the existence of an index structure ofT (a necessary and suﬃcient
condition for the existence of the index ofT; see [Garb]) with the non-existence of sphere or
non vertex-linking torusnormal surfacesof T; see Theorem 1.2 below. Such ideal triangula-
tions are called 1-eﬃcient in [JR03, KR05]. The unexpected connection between the index of
an ideal triangulation (a recent quantum object) and the classical theory of normal surfaces
places restrictions on the topology ofM; see Remark 1.3 below.
The second step constructs a canonical collectionXEP
M of triangulations of the Epstein-
Penner ideal cell decomposition of a cusped hyperbolic 3-manifoldM, such that the index
behaves well with respect to 2–3 and 0–2 moves that connect any two members ofXEP
M . The
index of those triangulations then gives the desired topological invariant ofM; see Theorem
1.8 below.
WeshouldpointoutthatnormalsurfaceswerealsousedbyFrohman-Bartoczynska[FKB08]
in an attempt to construct topological invariants of 3-manifolds, in the style of a Turaev-
Viro TQFT. Strict angle structures (a stronger form of an index structure) play a role in
quantum hyperbolic geometry studied by Baseilhac-Benedetti [BB05, BB07]. In the recent
work of Andersen-Kashaev [AK], strict angle structures were used as suﬃcient conditions for
convergence of analytic state-integral invariants of ideal triangulations. The latter invariants
are expected to depend on the underlying cusped 3-manifold and to form a generalization
of the Kashaev invariant [Kas97]. Theq-series of Theorem 1.8 below areq-holonomic, of
Nahm-type and, apart from a meromorphic singularity atq = 0, admit analytic continuation
in the punctured unit disc.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 3
Before we get to the details, we should stress that the origin of the 3D index is the exciting
work of Dimofte-Gaiotto-Gukov [DGGb, DGGa] (see also [BDP]) who studied gauge theories
with N = 2 supersymmetry that are associated to an ideal triangulationT of an oriented
3-manifoldM with at least one cusp. The low-energy limit of these gauge theories gives rise
to a partially deﬁned function, the so-called3D index
(1) I :{ideal triangulations}−→ Z((q1/2))H1(∂M ;Z), T↦→IT([ϖ])∈ Z((q1/2))
for [ϖ]∈ H1(∂M ; Z).1 The functionI is only partially deﬁned because the expression for
the 3D index may not converge. The above gauge theories provide an analytic continuation
of the coloured Jones polynomial and play an important role in Chern-Simons perturbation
theory and in categoriﬁcation. Although the gauge theory depends on the ideal triangulation
T, and the 3D index in general may not be deﬁned, physics predicts that the gauge theory
ought to be a topological invariant of the underlying 3-manifoldM. Recall that any two
ideal triangulations of a cusped 3-manifold are related by a sequence of 2-3 moves [Mat87,
Mat07, Pie88]. In [Garb] the following was shown. For the deﬁnition of an index structure,
see Section 2.
Theorem 1.1.(a) IT is well-deﬁned if and only ifT admits anindex structure.
(b) If T and T′ are related by a 2–3 move and both admit an index structure, thenIT =IT′.
1.2. Index structures and 1-eﬃciency.
Theorem 1.2. An ideal triangulation T of an oriented 3-manifold with cusps admits an
index structure if and only ifT is 1-eﬃcient.
The above theorem has some consequences for our sought topological invariants.
Remark 1.3. 1-eﬃciency ofT implies restrictions on the topology ofM: it follows thatM is
irreducible and atoroidal. Note that here byatoroidal, we mean that anyembedded torus is
either compressible or boundary parallel. It follows by Thurston’s Hyperbolization Theorem
in dimension 3 that M is hyperbolic or small Seifert-ﬁbred.
Remark 1.4. If K is the connected sum of the 41 and 52 knots, or K′ is the Whitehead
double of the41 knot and T is any ideal triangulation of the complement ofK orK′, then T
is not 1-eﬃcient, thusIT never exists. On the other hand, the (coloured) Jones polynomial,
the Kashaev invariant and thePSL(2, C)-character variety ofK and K′ happily exist; see
[Jon87, Kas97, CCG+94].
Theorem 1.5. Let T be an ideal triangulation of an oriented atoroidal 3–manifold with at
least one cusp. IfT admits a semi–angle structure thenT is 1–eﬃcient.
Remark 1.6. Taut and strict angle structures are examples of semi-angle structures, and for
these cases this is proved in [KR05, Thm.2.6]. In Section 3, we give a brief outline of the
argument for a general semi–angle structure.
1Hereandbelowwewillusethenotation M forbothacuspedhyperbolic3-manifoldandthecorresponding
compact manifold with boundary∂M consisting of a disjoint union of tori; the intended meaning should be
clear from the context.
4 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
Remark 1.7. In Corollary 3.3, we note that a construction of Lackenby produces triangula-
tions with taut angle structures, which are therefore 1–eﬃcient, on all irreducible an-annular
cusped 3–manifolds. However, it is not clear that the triangulations produced by this con-
struction are connected by the appropriate 2–3 and 0–2 moves, so we cannot prove that the
3D index is independent of the choice of taut triangulation for the manifold.
