---
doc_id: arxiv-1112.5179v1
doc_title: "3-Manifolds and 3d Indices"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 2-7
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices — We identify a large classR of three-dimensionalN = 2 superconformal ﬁeld the- ories."
---
2 Actions on the 3d index 6
2.1 The Sp(2N, Z) action 7
2.2 Aﬃne shifts 9
2.3 Adding a superpotential 10
2.4 A discrete symmetry ρ 11
2.5 An operator algebra 12
3 The tetrahedron index 15
3.1 Parity and ρ symmetry 16
3.2 Triality 17
3.3 Diﬀerence equations 18
4 The index of TM 20
4.1 Gluing rules 21
4.2 The bipyramid 24
4.3 Some knot complements 27
4.4 Mapping tori and T [SU (2)] 30
4.5 Quantum Lagrangian operators 33
4.6 Tentacles and vacua 36
4.7 Mutation invariance from gauge theory 41
5 The index from four dimensions and line operators 45
5.1 Line operator algebra 49
5.2 Boundary conditions for hypermultiplets 50
5.3 Non-abelian line defects 51
6 The index as SL(2, C) Chern-Simons theory 55
6.1 Quantization at k = 0 57
6.2 Symplectic action 61
6.3 Chern-Simons theory from 6d 64
A Proof of triality for the tetrahedron index 67
B Figure-eight index from six tetrahedra 69
C Quantum Lagrangian calculations 70
– 1 –
D Tentacles and diﬀerence equations 72
1 Introduction
The space of three-dimensional superconformal ﬁeld theories is vast and only partially ex-
plored. Many superconformal ﬁeld theories can be deﬁned as the IR ﬁxed point of super-
symmetric gauge theories coupled to matter. The inclusion of Chern-Simons couplings gives
a large variety of IR ﬁxed points, as the CS coupling does not ﬂow. Furthermore, in super-
symmetric CS theories coupled to matter, the CS coupling controls the strength of several
interaction terms in the Lagrangian.
Theories with diﬀerent UV Lagrangian deﬁnitions can ﬂow to the same IR SCFT, in
which case they are typically called “mirror” descriptions of the same theory. The terminology
arises from the case of gauge theories with N = 4 supersymmetry and no CS terms, where
supersymmetry protects the geometry of the Higgs branch, and non-trivial IR identiﬁcations
typically exchange the Higgs and Coulomb branches of the theory. In this paper we concern
ourselves withN = 2 SCFTs. This is a rather interesting amount of supersymmetry, as it
allows one to add superpotential couplings to the theory, and the UV U(1)R R-symmetry can
mix with other ﬂavor symmetries to give interesting anomalous dimensions in the IR [1, 2].
There are several basic known “mirror symmetries” for N = 2 theories, which typically
arise as a reformulation or deformation of N = 4 mirror symmetries [3–6]. One can lever-
age these basic examples to build large networks of dualities, starting with a complicated
Lagrangian L, and applying known mirror symmetries to a subsector L′ of the theory. This
strategy is not without danger: it relies on the assumption that in order to understand the
IR behavior of L it is reasonable to ﬁrst have the subsector L′ ﬂow to the IR, where it can
be given alternative descriptions, and then to turn on the couplings between L′ and the rest
of the theory. Despite this danger, the strategy is still rather useful.
Given the large set of dualities constructed this way, one may seek methods for charac-
terizing distinct IR ﬁxed points. There are several protected quantities that can be computed
in the UV, and provide information on the IR SCFT. There are three such quantities that are
related in a surprising manner: the moduli space L[T ] of supersymmetric vacua for massive
deformations of the SCFT compactiﬁed on a circle [7–9], the ellipsoid partition functionZb[T ]
[10–12] and the reﬁned index I[T ] [13–17].
The moduli spaceL[T ] is a useful notion if the 3d SCFT has “enough” ﬂavor symmetries:
to each ﬂavor symmetry one can associate a real mass deformation of the SCFT, and a crucial
assumption is that we have enough mass deformation parameters to make the SCFT develop
a mass gap. Upon compactiﬁcation on a circle, the real masses are complexiﬁed to C∗ valued
twisted masses Xi, and one can introduce the notion of an eﬀective twisted superpotential
W(Xi) [18]. Crucially,W(Xi) can be usually computed in the UV. The twisted superpotential
is multivalued, both because the theory will have multiple massive vacua, and becauseW(Xi)
– 2 –
is only deﬁned up to shifts by integer multiples of the twisted masses. The SUSY-preserving
“eﬀective FI parameters”
Pi = ∂W
∂Xi
(1.1)
(really a complexiﬁcation of the vev of moment map operators) are also circle-valued. Then,
upon exponentiating (1.1), one is left with a well deﬁned and UV-computable parameter space
of supersymmetric vacuaL[T ] as a Lagrangian submanifold of ( C∗)2N. Here and in the rest
of the paper, N denotes the number of abelian ﬂavor symmetry generators available in the
UV.
The ellipsoid partition function Zb[T ] is deﬁned by a deformation of the ﬂat space La-
grangian for the theory T that allows for some supersymmetry to be preserved upon com-
pactiﬁcation on an ellipsoid. The deformation requires a choice of R-symmetry, which does
not have to be the actual R-symmetry in the IR, and can be any linear combination of the
UV R-symmetry and the other ﬂavor symmetry generators. The choice of R-symmetry and
the real mass deformation parameters can be combined into N complex parameters ˆXi. The
partition functionZb( ˆXi) can be computed in the UV by localization methods, and bears a
close relationship with the manifoldL. Indeed, it satisﬁed two sets of recursion relations that
are a “quantization” of the equations that carve out L in (C∗)2N [9, 19].
This phenomenon can be explained by recasting the 3d SCFT T as a boundary condition
for an U(1)N free abelian four-dimensional gauge theory. Then the equations that deﬁne L
can be promoted to Ward identities for supersymmetric ’tHooft-Wilson loops brought to the
boundary. If one realizes the 3d ellipsoid as the equator of a four-dimensional half-sphere,
the supersymmetric line defects act as operators on Zb( ˆXi), and the Ward identities become
operator equations for Zb( ˆXi). The “quantization” of the operator algebra arises from a
known subtlety in the OPE of supersymmetric line defects [20, 21].
One of the result of this paper is to establish a similar correspondence for a third invariant
of SCFTs: the reﬁned index. The index is deﬁned by another deformation of the Lagrangian
for T , which allows a supersymmetric compactiﬁcation of T on S2. The deformation again
requires a choice of R-symmetry, which does not have to be the actual R-symmetry in the
IR, and can be any linear combination of the UV R-symmetry and the other ﬂavor symmetry
generators.1 Then one can deﬁne a reﬁned Witten index for the theory on the sphere, that
will be a power series in a fugacity q that measures the energy minus half the R-charge of
the states. The index is also a function of N parameters valued in (S1× Z), associated to
the ﬂavor symmetries of the theory. We will show that the reﬁned index I[T ] satisﬁes two
sets of recursion relations, which again quantize the equations which carve out L in (C∗)2N.
The quantization arises in the same way as for Zb( ˆXi), and the construction again uses an
appropriate four-dimensional setup.
The three invariantsL[T ],Zb[T ],I[T ] provide scant information on the superpotential
couplings of the theoryT . Mainly, the superpotential aﬀects the calculation by breaking ﬂavor
1It is important to remark that this deformation is not the same as a topological twist on S2. Rather, it is
akin to a superconformal transformation from ﬂat space to S2× R.
– 3 –
symmetries, and thus reducing the space of available parameters. Although this may seem
trivial, it is surprisingly powerful. For example, the eﬀect onL of adding toT a superpotential
term that carries some ﬂavor charge vector c is simply to do a symplectic quotient with a
moment map C = c·X in the ambient space ( C∗)2N, reducing the dimension of L by one.
This accounts automatically for the eﬀect of the superpotential on the space of vacua of the
theory! Similar statements hold for Zb[T ] andI[T ].
Ultimately, we would like to identify an arena of N = 2 SCFTs where we can reliably
label distinct SCFTs by the invariants L[T ],Zb[T ],I[T ] or by some reﬁnement of these.
For this purpose, we will impose two restrictions: ﬁrst, we only consider abelian Chern-
Simons matter theories. In the absence of a superpotential we may give many diﬀerent
mirror abelian CSM descriptions of the same theory T0. Our second restriction is to deﬁne a
theoryT by a restricted class of superpotential deformations of a theory T0: we only consider
a superpotential that is the linear combination of operators OI with the property that for
eachOI we have an abelian CSM mirror frame where OI is a product of elementary ﬁelds.
Notice that in other mirror frames, OI will be a non-perturbative monopole operator, and
there may be no mirror frame where all theOI are simultaneously elementary. We will denote
the resulting class of theories as “class R.”
The invariants of the theory T0 are related by a simple “change of polarization” to the
invariants ofn free chiral multiplets, which we can denote as L[∆]n,Zb[∆]n,I[∆]n. In other
words, any Chern-Simons levels and gauging can be undone with an appropriate Sp(2n, Z)
transformation [22] on T0. Thus the invariants L[T ],Zb[T ],I[T ] of a theory in the class R
come equipped with a canonical presentation as the symplectic quotient of L[∆]n,Zb[∆]n,
I[∆]n by a list of n−N moment mapsCI. It is easy to characterize the admissible sets of CI
which correspond to allowed superpotentials. We can label the UV Lagrangians for theories
in the classR by the choice of polarization Π and the list of admissible moment maps CI.
The classR is closed under a basic abelian mirror symmetry operation, which replaces
three chiral multiplets with a superpotential of the form XYZ with Nf = 1 QED, a theory
involving two chiral multiplets of opposite charge under a dynamical gauge ﬁeld. This “2–
3 move” changes n by one unit. All known abelian mirror symmetries can be reduced to
a combination of several 2–3 moves. The 2–3 move acts on a simple fashion on the labels
(Π,CI). Thus it is natural to conjecture that we can label IR ﬁxed points of theories in the
classR by the equivalence classes of sets of admissible (Π,CI) under the action of 2–3 moves.
The set of such equivalence classes is a beautiful, intricate combinatorial object, which
is not fully understood. But there is at least a subset of R that which can be given a simple
geometric interpretation, in terms of hyperbolic geometry of three-manifolds. The spaceL[∆]
can be identiﬁed with the space of “ideal tetrahedra,” i.e. tetrahedra in hyperbolic space
with vertices on the boundary. There is a class of orientable 3d manifolds that can be glued
together from n ideal tetrahedra. Hyperbolic geometry gives us for free a polarization [23]
and a set of linear moment maps, which have a crucial feature: the 2–3 move relates diﬀerent
decompositions of the same manifold, and any two decompositions of the same manifold can
– 4 –
be related by a sequence of 2–3 moves. 2 Thus for every such manifold M we get a speciﬁc IR
ﬁxed point TM in the classR!
The invariantsL[TM],Zb[TM],I[TM] must coincide with geometric invariants of M. In-
deed, in [8, 19] it was proven that L[TM] is the space of hyperbolic metrics, or equivalently
ﬂat SL(2, C) connections on M, andZb[TM] behaves as an analytically continued SL(2, R)
Chern-Simons partition function on M [9, 27] – sometimes called an “ SL(2)” Chern-Simons
partition function [28–31]. In this paper, we show how I[TM] also admits a geometric inter-
pretation, and behaves as a SL(2, C) Chern-Simons partition function on M.
Conjecturally, the theoryTM has an alternative, mirror description: it can be deﬁned by
the twisted compactiﬁcation of the A1 6d SCFT on M. This higher dimensional deﬁnition
allows a connection to the rich subject of four-dimensional theories that can be deﬁned in
terms of the A1 6d SCFT compactiﬁed on C [32, 33]. This connection was an important
inspiration behind the construction. It also featured prominently in a complementary recent
construction of the theories TM, based on “R-ﬂow” in four-dimensional theories [34]. In this
paper we will explore the connection of I[TM] to the reﬁned indices of the four-dimensional
gauge theories. We expect our dictionary to be rather useful for four-dimensional N = 2
gauge theories, allowing one to compute the reﬁned index of 4d theories in the presence of
line defects and domain walls by borrowing results from the AGT correspondence [35–38].
Finally, we would like to remark that we expect higher rank generalizations of our con-
struction, say based on spaces of ﬂat GC connections on three manifolds for any G, or even
more general Lagrangian submanifolds of cluster varieties, to describe larger subsets of theo-
ries in the classR. For example, for G =SU (N) such theories would arise from a compactiﬁ-
cation ofK M5 branes on a three-manifoldM. Mathematically, some extensions of hyperbolic
invariants of 3-manifolds to higher rank have been investigated in [39, 40], following [41], and
are known to still lie in the classical Bloch group ( cf. Footnote 2). The generalization of
theories TM to higher rank should similarly lie in R. It would also be interesting to ﬁnd an
example of a 3d N = 2 SCFT that is not in the class R — say has a parameter space L
which cannot be given as a symplectic quotient of L[∆]n by linear moment maps. We leave
this problem to future work.
Our main goal in the remainder of the paper is to understand the index I[T ] for the
theories TM deﬁned in [19]. We will also make statements applicable to more general theo-
ries in class R (or even outside class R) whenever possible. Thus, we begin in Section 2 by
describing the general form of the index for 3d N = 2 SCFT’s with a U(1)N global sym-
metry, and deﬁning several familiar operations on it — for example, the descendant of the
Sp(2N, Z) action on the SCFT’s themselves. We introduce the line operators that will play
an important role throughout the paper. In Section 3, we then specialize to the index I[∆]
2Mathematically, it is well known that hyperbolic 3-manifolds deﬁne elements in the Bloch group B(C)
[24–26]. The class β(M) corresponding to a 3-manifold M can be deﬁned by using any ideal triangulation
of M, and it is invariant under 2–3 moves. Our family R of theories can be viewed as an extreme quantum
generalization (and in fact reﬁnement) of the classical Bloch group.
– 5 –
for the tetrahedron theory T∆, the basic building block of all theories in class R. Although
T∆ is extremely simple, consisting only of a single chiral multiplet, its index turns out to have
several surprising properties that will serve as model examples for the general properties of
theories inR.
We construct the indicesI[TM] of 3-manifold theoriesTM in Section 4, using the building
blocksI[∆] and the actions of Section 2. We give a simple, combinatorial set of rules for
buildingI[TM]. As prefaced above, I[TM] is obtained as the “symplectic reduction” of a
product indexI[∆]n, with the reduction realized via a certain inﬁnite summation over broken
ﬂavor charges. We explain how the algebra of line operators acts on I[TM], and explore the
relation between the index and the parameter spaceL[TM] of SUSY vacua. One self-consistent
observation is that unconstrained chiral operators in TM — seen as “ﬂat directions” in the
index — can be easily detected by the asymptotics of the algebraic parameter space L[TM].
In Section 5, we continue analyzing the quantum line operator algebra by viewing TM as a
boundary condition for a 4d N = 2 theory T [∂M ], and considering line operators inserted
into a 4d index.
Finally, in Section 6, we describe the index I[TM] as an intrinsic topological invariant
of M — arguing that it is equivalent to an SL(2, C) Chern-Simons partition function on M.
The fact that the index is a Chern-Simons partition function can be motivated by dualities
in six dimensions, highly reminiscent of recent work on M-theory realizations of Khovanov
homology [42]. Indeed, since the index is naturally deﬁned as an Euler characteristic of a
graded vector space, both in three and six dimensions, it is perfectly ripe for categoriﬁcation.
We hope this topic will be explored in future work.
