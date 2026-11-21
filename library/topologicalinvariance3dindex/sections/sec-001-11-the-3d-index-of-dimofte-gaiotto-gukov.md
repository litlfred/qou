---
doc_id: topologicalinvariance3dindex
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-001-11-the-3d-index-of-dimofte-gaiotto-gukov
section_title: "The 3D index of Dimofte-Gaiotto-Gukov"
section_number: 1.1
pages: 2-3
source_pdf: topological.invariance.3Dindex.pdf
source_sha256: 22953b4eee66dca2
toc_source: outline
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
---
index of an ideal triangulation T (a remarkable collection of Laurent series in q1/2 introduced
by Dimofte-Gaiotto-Gukov [DGG14, DGG13] and further studied in [Garb]) to a topological
invariant of oriented cusped hyperbolic 3-manifolds M. Our goal will be achieved in two
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
places restrictions on the topology of M; see Remark 1.3 below.
The second step constructs a canonical collection XEP
M of triangulations of the Epstein-
Penner ideal cell decomposition of a cusped hyperbolic 3-manifold M, such that the index
behaves well with respect to 23 and 02 moves that connect any two members of XEP
M . The
index of those triangulations then gives the desired topological invariant of M; see Theorem
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
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD
3
Before we get to the details, we should stress that the origin of the 3D index is the
exciting work of Dimofte-Gaiotto-Gukov [DGG14, DGG13] (see also [BDP]) who studied
gauge theories with N = 2 supersymmetry that are associated to an ideal triangulation T
of an oriented 3-manifold M with at least one cusp. The low-energy limit of these gauge
theories gives rise to a partially de
ned function, the so-called 3D index
(1)
I : {ideal triangulations} −→Z((q1/2))H1(∂M;Z),
T 7→IT([ϖ]) ∈Z((q1/2))
for [ϖ] ∈H1(∂M; Z).1 The function I is only partially de
ned because the expression for
the 3D index may not converge. The above gauge theories provide an analytic continuation
of the coloured Jones polynomial and play an important role in Chern-Simons perturbation
theory and in categori
cation. Although the gauge theory depends on the ideal triangulation
T, and the 3D index in general may not be de
ned, physics predicts that the gauge theory
ought to be a topological invariant of the underlying 3-manifold M. Recall that any two
ideal triangulations of a cusped 3-manifold are related by a sequence of 2-3 moves [Mat87,
Mat07, Pie88]. In [Garb] the following was shown. For the de
nition of an index structure,
see Section 2.
Theorem 1.1.
(a) IT is well-de
ned if and only if T admits an index structure.
(b) If T and T′ are related by a 23 move and both admit an index structure, then IT = IT′.
