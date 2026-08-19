---
doc_id: arxiv-1803.04009v2
doc_title: "Prepared for submission to JHEP IPMU-18-0045"
section_id: sec-000-1-introduction-and-summary
section_title: "Introduction and Summary"
section_number: 1
pages: 2-21
source_pdf: 1803.04009v2.pdf
source_sha256: 8b34299b739cd2b0
doc_brief: "Symmetry enhancement and closing of knots in 3d/3d correspondence — We revisit Dimofte-Gaiotto-Gukov’s construction of 3d gauge theories asso- ciated to 3-manifolds with a torus boundary."
---
2 3d N = 2 Superconformal ﬁeld theories labelled by 3-manifolds 4
2.1 6d A1 (2,0) theory on 3-manifolds :T 6d and T 6d
irred 5
2.2 Dimofte-Gaiotto-Gukov’s construction :TDGG 9
2.3 Relation between the two constructions 20
3 Symmetry enhancement 26
3.1 SO(3)/SU (2) enhancement 26
3.2 SU (3) enhancement 32
4 Dehn ﬁlling in 3d/3d correspondence 37
4.1 Dehn ﬁlling onT 6d
irred[N] 38
4.2 Small hyperbolic manifolds 40
5 3d N = 2 Dualities from Surgery calculus 42
A 3d indexI(A,B)
N (m,e ;x) andINpA+qB(x) 43
B T [SU (2)] and SU (2)/SO(3) types 48
B.1 Brief review ofT [SU (2)] 49
B.2 The global structure of the symmetries and ’t Hooft anomaly 50
B.3 S-transformation of 3d SCFT 51
B.4 SU (2)/SO(3) symmetry types of knots from six dimensions 52
1 Introduction and Summary
3-dimensional (3d) quantum ﬁeld theory exhibits several interesting aspects. Unlike higher
dimensional case, Abelian gauge interaction in 3d is strongly coupled at infrared (IR) and
gives non-trivial IR physics. Diﬀerent gauge theories at ultraviolet (UV) could end at
the same IR ﬁxed point along renormalization group (RG) and such phenomena is called
“duality”. Refer to [1–3] for examples of dualities among 3d gauge theories. There could be
enhanced symmetries in the IR ﬁxed point which is invisible in the UV gauge theory. From
purely ﬁeld theoretic viewpoint, these phenomena are not easy to understand or predict.
In this paper, we consider a certain subclass of 3d quantum ﬁeld theories withN = 2
(4 supercharges) supersymmetry which can be engineered by a twisted compactiﬁcation
of the 6d (2, 0)-superconformal ﬁeld theory (SCFT) ofA1 type. The 6d theory is the
simplest maximally supersymmetric conformal ﬁeld theory and describes the low energy
world volume theory of two coincident M5-branes in M-theory. The 6d theory hasSO(5)
– 1 –
R-symmetry and allows a 1/2 BPS regular co-dimension two defect. The concrete set-up
of this paper is as follows
6d A1 (2,0)-SCFT on R1,2×M with a partial topological twisting alongM
with a regular co-dimension two defect alongR1,2×K
compacitiﬁcation alongM
−−−−−−−−−−−−−−−−−−−→T 6d[M,K ] on R1,2.
(1.1)
HereM is a compact (closed) 3-manifold andK is a knot insideM.1 Using the vectorSO(3)
subgroup ofSO(5) R-symmetry, we perform a topological twisting alongM which preserves
1/4 supersymmetries. After the compactiﬁcation, we obtain a 3dN = 2 quantum ﬁeld
theory, sayT 6d[M,K ], determined by the topological choice ofM and K. These theories
are 3d analogy of 4dN = 2 theories of class S [4, 5]. In the analogy, closed Riemann surface
corresponds toM and a regular puncture on the surface corresponds toK. The 6d picture
predicts the existence ofsu(2) ﬂavor symmetry associated to the knot in the resulting 3d
gauge theory.
One non-trivial task is ﬁnding ﬁeld theoretical description of the 3d theoryT 6d[M,K ].
A hint comes from so called 3d/3d relations [6–10] which says that the partition functions
of theT 6d[M,K ] theory on supersymmetric curved backgrounds are equal to the partition
functions of purely bosonicSL(2, C) Chern-Simons (CS) theories onM with a monodromy
defect alongK. State-integral models [9, 11–14] give integral expressions for complex CS
partition functions while localization techniques [15–18] give similar integral expressions for
the supersymmetric partition functions of 3d ﬁeld theories.
Base on the technical developments, ﬁeld theoretic algorithm of constructing 3d gauge
theoryTDGG[M,K ] labelled by the choice of(M,K ) is proposed by Dimoft-Gaiotto-Gukov
[19]. Their construction guarantees that the localization integrals of theTDGG[M,K ] the-
ory are identical to the corresponding state-integral models. In the original paper, the 3d
gauge theoryTDGG[N,XA] is actually labelled by a choice of a knot complementN and a
primitive boundary cycleA∈H1(∂N, Z). But there is a one-to-one map between the two
topological choices, (M,K ) and (N,A ), and we can labell them by the choice of(M,K )
which has more clear meaning in the 6d compactiﬁcation (1.1). The explicit map between
two topological choices is explained around Figure 1. From the non-trivial match of super-
symmetric partition functions, it is tempting to conclude that theTDGG[M,K ] is actually
T 6d[M,K ]. However, there are two manifest diﬀerences between two theories. Firstly, only
some subset of irreducible ﬂatSL(2, C) connections on the knot complementN := M\K
appears as vacua onR2×S1 ofTDGG[M,K ] theory while all ﬂat connections are expected
to appear as the vacua ofT 6d[M,K ] theory. This point was already emphasized in [20]. Sec-
ondly, theTDGG[M,K ] theory generically hasU(1) ﬂavor symmetry, denoted asU(1)XA,
associated to the knotK while T 6d[M,K ] has asu(2) ﬂavor symmetry. Motivated from
the similarity and diﬀerences of two theories, we propose the precise relation (2.84) between
1The system can be generalized to the case when a knotK is replaced by a linkL with several compo-
nents. We use the letterK for knot andL for link.
– 2 –
them, which we reproduce here:
T 6d on a vacuumPSCFT
−−−−−−−−−−−−−−−→T 6d
irred
deformed byδW =µ3
− −−−−−−−−−−−−−−−− →TDGG (1.2)
Here µ = (µ1,µ 2,µ 3) is a chiral operator in the triplet representation ofsu(2), and this
operator is associated the co-dimension two defect alongK. Each of the arrows in the
above equation are nontrivial RG ﬂows which are explained below.
The proposed relation explains why theTDGG[M,K ] theory generically has onlyU(1)
symmetry associated to the knot whileT 6d[M,K ] has su(2) ﬂavor symmetry. Thesu(2)
symmetry of T 6d[M,K ] is broken by the superpotential deformationδW = µ3 in (1.2)
which is typically a relevant deformation in the RG sense. After S1-reduction, the 6d
theory becomes 5d maximally supersymmetricsu(2) Yang-mills theory (SYM) and the co-
dimension two defect in 6d theory is realized by coupling a copy of the 3dN = 4T [SU (2)]
theory [21] to the 5d theory. Thenµ is thesu(2) moment map operator of the 3dN = 4
T [SU (2)] theory.
As an intermediate step, we introduce a 3d SCFTT 6d
irred[M,K ] appearing in (1.2) which
is the IR ﬁxed point ofT 6d[M,K ] on a particular pointPSCFT of the vacuum moduli space.
Unlike T 6d[M,K ], T 6d
irred[M,K ] might not contain thesu(2) moment map operatorµ af-
ter taking the IR limit. In that case, the superpotential deformation is not possible (or
more precisely, it is irrelevant) and thus theTDGG[M,K ] still has thesu(2) symmetry. By
carefully analyzing the coupled system, 5d SYM+3dT [SU (2)], we ﬁnd a topological condi-
tion on (N,A ) which guarantees the absence of moment map operator and thus thesu(2)
symmetry in TDGG[N,XA] theory. The topological condition is summarized in Table 1.
For example, we expectsu(2) symmetry enhancement whenM is a Lens-space and do not
expect the enhancement whenM is hyperbolic.
Asanapplicationofthesymmetryenhancementcriterion, weshowthatthe TDGG[M =
S3,K ] theory for all hyperbolic twist knotsK has a surprising SU (3) symmetry. As a
simplest example, we claim that the following 3dN = 2 theory hasSU (3) symmetry.
TDGG[M =S3,K = ﬁgure-eight knot]
= A U(1)0 vector multiplet coupled to two chiral multiplets of charge +1.
(1.3)
The theory only has manifestSU (2)×U(1) symmetry where theSU (2) rotates the two
chirals and theU(1) comes from the topological symmetry of the dynamical abelian gauge
ﬁeld. TheU(1)XA symmetry associated to the knot is a linear combination of two Cartans
of theSU (2)×U(1) which is expected to be enhanced toSO(3) according to the criterion
in Table 1. From a group theoretical analysis, the enhancement implies that theSU (2)×
U(1) should be enhanced toSU (3). We checked the symmetry enhancement by explicitly
constructing the corresponding conserved current multiplet.
Base on the proposed relation betweenT 6d[M,K ] and TDGG[M,K ], we identify the
ﬁeld theoretical operation onTDGG[M,K ] corresponding to Dehn ﬁlling operation on the
knot complementN = M\K. The operation is only possible when theTDGG[M,K ] has
su(2) ﬂavor symmetry. The Dehn ﬁlling operation is analogous to closing of punctures on
Riemann surface in 4d/2d correspondence [22]. By applying the Dehn ﬁlling operation, we
– 3 –
can extend the DGG’s construction to 3d gauge theories labelled by a closed 3-manifold
M. The theory is denoted asT 6d
irred[M] and has similar 6d interpretation asT 6d
irred[M,K ].
As concrete examples, ﬁeld theoretic descriptions ofT 6d
irred[M] for three smallest hyperbolic
3-manifolds are given in [23]. One interesting aspect of our construction ofT 6d
irred[M] is
that we can relate surgery calculus in knot theory to 3dN = 2 dualities. One way of
representing closed 3-manifold is using so called Dehn surgery representation. A closed 3-
manifoldM has inﬁnitely many diﬀerent surgery descriptions and surgery calculus tell when
two surgery descriptions give the same 3-manifold. Diﬀerent surgery representations of a
closed 3-manifold give diﬀerent ﬁeld theoretical descriptions ofT 6d
irred[M] which are related
by 3d dualities. One illustrative example is given around eq. (5.2). Since the 3d theory
depends on only the topology of the 3-manifold, every physical quantities of the theory are
topological invariants of the 3-manifold. As an example, we introduce a new 3-manifold
invariant called “3d index” which is nothing but the superconformal index of theT 6d
irred[M].
The paper is organized as follows. In section 2, we introduce two ways of associating
the choice of 3-manifoldM and a knotK inside it with a 3d gauge theoryT [M,K ]. One
is through the construction by Dimofte-Gaiotto-Gukov [19] (DGG) and the corresponding
gauge theory is denoted asTDGG[M,K ]. The other is through a twisted compactiﬁcation of
6dA1 (2,0) theory onM with a regular co-dimension two defect alongK. The resulting 3d
gauge theory is denoted asT 6d[M,K ]. After explaining the two constructions in detail, we
propose a precise relation (2.84) between two constructions. Base on the proposed relation,
in section 3, we give a topological criterion on(M,K ) which determines when theU(1)XA
symmetryTDGG[M,K ] theory is enhanced toSU (2) orSO(3). The criterion is summarized
in Table 1. In section 4, we identify ﬁeld theoretic operation corresponding to Dehn ﬁlling
operation in 3-manifold side in 3d/3d correspondence. It allows us to extend the DGG’s
construction to the case when the knot is absent. In section 5, we discuss how the surgery
calculus in knot theory predicts inﬁnitely many 3dN = 2 dualities.
2 3d N = 2 Superconformal ﬁeld theories labelled by 3-manifolds
In this section, we introduce two ways of associating a 3-manifoldM with a knotK in it
to a 3dN = 2 gauge theoryT [M,K ].
(M,K ) ↝ (a 3dN = 2 gauge theoryT [M,K ]), where
M is a closed 3-manifold, K ⊂M is a knot inM .
(2.1)
One way is through a twisted compactiﬁcation of a 6dN = (2, 0) theory ofA1 type on a
closed 3-manifoldM with a regular co-dimension two defect along a knotK on M. The
other way is using the construction by Dimofte-Gaiotto-Gukov [19] (DGG) based on an
ideal triangulation of the knot complementM\K. These two theories are argued to be
related [19], and we will propose the more precise relation between them with supporting
evidences. We describe the relation after reviewing basic aspects of two approaches.
Before going to detailed analysis, let us ﬁrst introduce an alternative labelling for the
topological choice, (M and K), which will be used throughout the paper. The choice can
– 4 –
(M,K)(N,A)MKN=M\KA
Figure 1. The choice of a knotK inside a closed 3-manifoldM can be alternatively described by
a choice of knot complementN and a boundary cycleA∈H1(∂N, Z).
be replaced by
(M,K )↔ (N,A ), where
N is a knot complement andA∈H1(∂N, Z) is a primitive boundary cycle .
(2.2)
For a given(M,K ), the corresponding(N,A ) is given by
N =M\K :=M−NK , (NK : Tubular neighborhood of a knotK)
A : A primitive boundary cycle around the knotK.
(i.e. the contractible cycle in the removed tubular neighborhoodNK)
(2.3)
For given(N,A ), on the other hand,(M,K ) is determined by
M =NA := (A closed 3-manifold obtained fromN by closing a cycleA in ∂N )
:= (N∪ (D2×S1))/∼ with A∼ (contractible boundary cycle ofD2×S1)
K :={p}× S1⊂D2×S1, where p∈D2 is the origin ofD2.
(2.4)
Using the map, we can use two choices interchangeably. For example,
T [N,A ] =T [M,K ]. (2.5)
In most part of this paper, we assume thatN is a knot complement with one torus boundary
but our discussion can be easily generalized to the case whenN is a link complement with
several torus boundaries.
2.1 6d A1 (2,0) theory on 3-manifolds :T 6d and T 6d
irred
We deﬁne
T 6d[M,K ] = (Twisted compactiﬁcation of 6d (2,0)A1 theory onM
with a regular co-dimension two defect alongK⊂M).
(2.6)
T 6d
irred[M,K ] = (The low energy limit ofT 6d[M,K ]
on a particular pointPSCFT on the moduli space of vacua).
(2.7)
– 5 –
Asasimplerset-up, wecanalsoconsider the casewhenthedefect isabsent. Inthatcase, the
resulting 3d theory is denoted asT 6d[M] and T 6d
irred[M], respectively. For theT 6d
irred[M,K ]
to be deﬁned, we assume thatN =M\K is a hyperbolicknot complement.
The reason that we considerT 6d
irred[M,K ] is as follows. The moduli space of vacua of
T 6d[M,K ] in general contains several diﬀerent connected components. Then, we have to
decide which point of the moduli space we consider before taking the low energy limit. The
typical distances between diﬀerent components of the moduli space are of the order of the
compactiﬁcation scale onM, which set the cutoﬀ scale of the low energy eﬀective 3d theory.
Therefore, we cannot expect that there is a single eﬀective 3d theory which describes the
entire moduli space of vacua. Only after specifying a point on the moduli space, we can
obtain a low energy eﬀective ﬁeld theory which describes the physics near that point.2
In other words,T 6d[M,K ] is not a genuine 3d theory, but should be considered more
appropriately as the 6d theory compactiﬁed onM. However, we will be sometimes sloppy
and call it a 3d theory in this paper.
InT 6d
irred[M,K ], we pick up a point and take the low energy limit. The low energy limit
may be described by a 3d SCFT (which can be empty or a topological theory). Below we
will specify which point on the moduli space of vacua we take, by using reduction to 5d
SYM.
T 6d on R2×S1 via 5d SYM The structure of the moduli space of vacua becomes simpler
if we compactify the 3d spacetime toR2×S1. This is because we can use the 5 dimensional
maximally supersymmetric Yang-Mills (5d SYM) theory description. The set-up is3
6dN = (2, 0) on R2×S1×M
 ++
5dN = 2 SYM on R2×M // theory T 6d[M] on R2×S1
(2.8)
The bosonic components of the 5d SYM theory are gauge ﬁeldsAI (I = 0,··· , 4) and scalar
ﬁeldsφk (k = 0,··· , 4). After compactiﬁcation onM, the supersymmetry is deﬁned onR2,
and we split these ﬁelds as
(AI=0,1,2,3,4,φk=1,2,3,4,5)→ (Aµ=0,1,φk=0,1)⊕ (Ai :=Ai +iφi)i=2,3,4 (2.9)
From the point of view of the super-algebra onR2, theV = (Aµ=0,1,φk=0,1) is the vector
multiplet andAi =Ai +iφi (i = 2, 3, 4) are twisted chiral ﬁelds. The reason that we regard
2 A simple example which illustrates the point is theT 2 compactiﬁcation of the 6dN = (2, 0)A1 theory
on T 2. The moduli space of this theory is[R5×S1]/Z2, whereS1 comes from the integral of the 2-form
ﬁeld onT 2. On the other hand, the moduli space of 4dN = 4 SYM is R6/Z2. Only after picking a point
on [R5×S1]/Z2 and taking the low energy limit, the 6dN = (2, 0) theory onT 2 becomes the 4dN = 4
SYM. In this case the moduli space is connected, but still there is no single 4d eﬀective theory describing
the whole moduli space of vacua.
3On general grounds, one may only expect that 5d SYM describes the moduli space only in the limit
of very small radius ofS1. However, somewhat miraculously, it is believed that 5d SYM describes even a
ﬁnite radius ofS1.
– 6 –
A as twisted chiral ﬁelds rather than chiral ﬁelds is that the relation between 5d SYM and
T 6d[M] is a kind of mirror symmetry analogous to the case of 4d class S theories.
The twisted superpotential is given by complex Chern-Simons action as
~WYM = 1
g2
YM
CS[A] := 1
g2
YM
∫
M
1
2Tr
(
AdA + 2
3A3
)
. (2.10)
where g2
YM is the gauge coupling of 5d SYM which is related to the radiusR of S1 as
1
g2
YM
= 1
8π2R. (2.11)
This is the results in [6–8] in the limitS2→ R2. This twisted superpotential corresponds
to the twisted superpotential obtained in DGG’s construction discussed in Sec. 2.2
The regular co-dimension two defect along a knotK⊂M can be realized as coupling
the 3d T [SU (2)] theory [21] to the ﬁelds of 5d SYM [24–28]. The theoryT [SU (2)] is
reviewed in Appendix B.1. This is a 3d N = 4 SCFT given byU(1) vector multiplet
coupled two fundamental hypermultiplets(Ea, ˜Ea)a=1,2. The theory hassu(2)H×su(2)C
ﬂavor symmetry and let
~µ := holomorphic moment map operator ofsu(2)C ,
~ν := holomorphic moment map operator ofsu(2)H .
(2.12)
Then the twisted superpotential coupling of theT [SU (2)] and the 5d SYM is given by
~WYM-defect =
∫
K
tr(~νA). (2.13)
This means that we integrate the one-form tr(~νAi)dyi overK.4
We can also include (complexiﬁed) mass terms to the defect as
~Wmass =
∫
K
ds tr(m~µ) (2.14)
whereds is the line element onK, andm is the mass. The mass of defect is related to the
eigenvalues of~ν:
Eigenvalues of~ν ={m,−m}. (2.15)
See [28] for detailed explanations of the coupling of 5d SYM toT [SU (2)] in the context of
4d class S theories. The analysis there may be extended to the 3d/3d case, but we do not
perform a detailed analysis.
4 The gauge invariance is preserved as follows. The supersymmetry is considered in the two dimensional
space R2, and hence the direction along the knotK is considered as a kind of “internal manifold”. Lett be
the coordinate alongK. Then, the kinetic term along this direction comes not from the Kahler potential,
but from the twisted superpotential as~W ⊃ ˜E∂tE. This term combines with (2.13) to form a covariant
derivative ˜E(∂t +A)E, where we have used~µ∼E ˜E (see Appendix B.1).
– 7 –
By solving F-term equations for the twisted superpotenal in (2.10) and (2.13), a part
of the moduli space of vacua5 on R2×S1 with mass parameterm is given by
Mvacua(T 6d[M,K ] on R2×S1)
={A :dA +A∧A =~νδ(K), eigenvalues of~ν ={m,−m}}/G .
(2.16)
where δ(K) is the delta function localized onK, andG is the group ofPSL (2, C) gauge
transformations on M. This is the space of ﬂat connections of the complexiﬁeld gauge
group PSL (2, C) with the holonomye~ν around K.
ρhol(A) := (PSL (2, C) holonomy matrix alongA-cycle) =e~ν . (2.17)
Notice that the eigenvalues ofe~ν are determined by the mass parameterm.
Now we can specify the pointPSCFT on the moduli space of vacua which is taken in
the deﬁnition (2.7). First, let us consider more generally. For simplicity we assume that the
moduli space of vacua onR3,Mvacua(T 6d[M,K ] on R3), is a discrete set. Let us take an
arbitary pointP ∈M vacua(T 6d[M,K ] on R3 ). Then, if we compactify the theory onS1
with a radius which is large enough compared to potential barriers between diﬀerent points
onMvacua(T 6d[M,K ] on R3), then the pointP goes to a subsetM(P ) of the moduli space
of vacua onR2×S1 denoted asMvacua(T 6d[M,K ] on R2×S1),
P→M (P )⊂M vacua(T 6d[M,K ] on R2×S1). (2.18)
ThisM(P ) need not be a single point, but may have several points whose number is related
to the Witten index of the 3d eﬀective theory onP. Because of the supersymmetry, the
condition that the radius ofS1 is large may be dropped since there is no phase transition
under change of the radius.
The explicit forms ofMvacua(T 6d[M,K ] on R3) andM(P ) are not known and they are
deﬁned just by the abstract ﬁeld theoretical considerations as above. However, later we will
propose howM(PSCFT) may be given concretely in terms of ﬂatPSL (2, C) connections.
To consider a superconformal point, we set the massm to be zero. Then the point
PSCFT is deﬁned as follows. After compactiﬁcation onS1, the moduli space of vacua
of the theory on PSCFT becomes a subsetM(PSCFT) of the moduli space of vacua on
R2×S1. Then, the point PSCFT is deﬁned by the condition thatM(PSCFT) contains
the connectionAhyp∈M vacua(T 6d[M,K ] on R2×S1) which is determined by the unique
complete hyperbolic metric onN = M\K. More explicitly, using the spin-connectionω
and dreibeine of the complete hyperbolic metric, the ﬂat connection can be expressed as
Ahyp =ω−ie. (2.19)
This ﬂat connection has the greatest value of Im(CS[Aα]) among all ﬂat connectionsAα
with parabolic boundary holonomy and is conjectured to be the only vacua contributing
5When the connectionA is reducible, we can turn on the expectation values of the vector multiplets
V = (Aµ=0,1,φk=0,1). These branches are very important in 4d class S theories [28, 29]. However, in the 3d
theories considered in this paper, we only consider points on the moduli space on whichA is irreducible.
Therefore, we can neglect those branches.
– 8 –
to a squashed 3-sphere partition function [30] ofT 6d
irred[M,K ]. Refer to [13, 31–34] for
discussions on the conjecture from various respects, state-integral model of the complex
CS theory, holographic principal and resurgent analysis. To other physical quantities of
T 6d
irred[M,K ] such as superconformal index, on the other hand, other ﬂat connections in
M(PSCFT) may contributes.
Now we give a conjecture about howM(PSCFT) is given concretely in terms of ﬂat
connections. First we consider the case where a knotK exists. For this purpose, we deﬁne
M(PSCFT) even for nonzero massm by continuity fromm = 0. Namely, M(PSCFT) is
just the set of vacua of the 3d eﬀective theory nearPSCFT with mass m. We make the
dependence onm explicit by writing it asM(PSCFT,m ). We also deﬁneχ(N) as
χ(N) =
⋃
m
{A :dA +A∧A =~νδ(K), eigenvalues of~ν ={m,−m}}/G (2.20)
This means that we consider all ﬂat connections with varying holonomy around the knot.
Then we propose
⋃
m
M(PSCFT,m ) = {the connected component ofχ(N) containingAhyp}
:=χ0(N). (2.21)
In [35], the component is calledDehn surgery component. Another way of representing the
above equation isM(PSCFT,m ) =χ0(N)∩{eigenvalues ofν ={m,−m}}.
Next, consider the case where there is no knot on M. If the closed 3-manifold is
represented by a Dehn ﬁlling operation on a hyperbolic knot complementN = M\K for
some K along a boundary cycleA,
M =NA (2.22)
we propose that theM(PSCFT) is given by
M(PSCFT) of the closed manifoldM
=χ0(N)∩{ρhol(A) = 1} (2.23)
Thedeﬁnitionoftherighthandsidecontainsaknot K, butweassumethatitisindependent
of the choiceK⊂M. Notice thatρhol(A) = 1 is stronger thanm = 0, since we could have
a nonzero upper-right component ofν even if its eigenvalues are zero.
2.2 Dimofte-Gaiotto-Gukov’s construction :TDGG
In [19], a combinatorial way of constructing a 3d SCFT, which we denoteTDGG[N,XA], for
given choice of(N,A ) is proposed. Empirically, the theory associated to non-hyperbolicN
is a trivial theory only with topological degrees of freedom. In this subsection we focus on
the case whenN is hyperbolic. Here we give a summary of the DGG’s construction with a
modiﬁcation on superpotential deformation associated to ‘hard’ internal edges (see (2.47))
which play a crucial role in the symmetry enhancement of the theory.
– 9 –
Mechanics of ideal triangualtion The construction is based on a choice of an ideal
triangulationT of N.
T : N =
( k⋃
i=1
∆i
)
/∼ . (2.24)
Here ∆i denote the i-th tetrahedron in the triangulation. Ideal tetrahedron can be em-
bedded into a hyperbolic upper half planeH3 in a way that all vertices are located on the
boundary of H3 and both of edges and faces are geodesics. Hyperbolic structures on an
ideal tetrahedron can be parameterized by a complex parameterz (with 0 < Im[Z] < π,
Z := logz), which is the cross-ratio of the positions of its vertices on∂H3. We assign edge
parameters (z,z′,z′′) to each pair of edges of ideal tetrahedron as in the ﬁgure below.
w=zw=0w=1zz'z''z''z'
z
zz'z''
z' z''
z
Figure 2 . Edge parameters (z,z′,z′′) of an ideal tetrahedron. Left: ideal tetrahedron in
H3 ={(y,w ) : y ∈ R+,w ∈ C} with metric ds2(H3) = dy2+dwd ¯w
y2 . Using the isometry of H3,
PSL (2, C), four asymptotic vertices can be placed at(y,w ) = (0, 0), (0, 1), (0,z ) and (∞,·). Right:
topologically, ideal tetrahedron is a tetrahedron with truncated vertices.
Geometrically, these edge parameters correspond to
{Z,Z′,Z′′} :={logz, logz′, logz′′}
=i(dihedral angle between two faces meeting on the edge) + (torsion). (2.25)
Here “torsion” is a quantity which measures the twisting of hyperbolic metric around the
edge. For an ideal tetrahedron inH3, these parameters satisfy
Zi +Z′
i +Z′′
i =iπ (sum of angles in small boundary triangle equals toπ),
e−Zi +eZ′′
i = 1.
(2.26)
The second equation follows directly from the geometric deﬁnition of(z,z′,z′′) as equivalent
cross-ratios. These constraints are compatible with the following cyclic symmetry of ideal
tetrahedron:
Z3 : (Z,Z′,Z′′)→ (Z′,Z′′,Z )→ (Z′′,Z,Z ′). (2.27)
An hyperbolic structure on a knot complementN can be obtained by gluing the hy-
perbolic structure on each tetrahedron in a smooth way. For the smooth gluing, we need
– 10 –
to impose the following conditions
CI := (sum of all logarithmic edge variables associated to
edges meeting at theI-th internal edge in the gluing)
=
k∑
i=1
(GIiZi +G′
IiZ′
i +G′′
IiZ′′
i ), G Ii,G′
Ii,G′′
Ii∈{ 0, 1, 2}.
= 2πi.
(2.28)
There arek-internal edges in an ideal triangulation withk ideal tetrahedra. A solution to
these gluing equations (2.26) and (2.28) with conditions0 < Im[Zi] < πfor alli gives a
hyperbolic (generally incomplete) structure onN.
M(PSCFT ) from ideal triangulation More generally, a solution to the exponentiated
gluing equations gives an irreducible ﬂatPSL (2, C) = SL(2, C)/⟨±1⟩ connections onN.
Consider the algebraic varietyD[N,T ] determined by gluing equations of an ideal triangu-
lationT ,
D[N,T ] :={zi,z′
i,z′′
i ∈ C\{0, 1} :ziz′
iz′′
i =−1,z−1
i +z′′
i− 1 = 0,
k∏
i=1
zGIi
i (z′
i)G′
Ii(z′′
i )G′′
Ii = 1}.
(2.29)
The variety is called adeformation variety. A point inD[N,T ] gives an irreducible ﬂat-
connection via a mapχT
χT : D[N,T ]→χ(N) :={ρhol∈ Hom
[
π1(N)→PSL (2, C)
]
/(conj)}. (2.30)
where the deﬁnition ofχ(N) here is equivalent to that in (2.20). The mapχT is injective
but not surjective. Using the map, holonomy matrix along a primitive boundary cycle
A∈ H1(∂N, Z) = π1(∂N )⊂ π1(N) can be written as linear combinations of logarithmic
edge parameters
ρhol(A) =
(
ea/2 0
∗ e−a/2
)
where a =
k∑
i=1
(αiZi +α′′
iZ′′
i ) +iπϵ
with integer coeﬃcients(αi,α′′
i,ϵ ).
(2.31)
Dependence on{Z′
i} was eliminated using the linear relations in (2.26). The algebraic
variety depends on the choice of an ideal triangulationT of N. But it is known that
the Dehn surgery componentχ0(N) =⋃
mM(PSCFT ,m ) in (2.21) is always contained in
D[N,T ] for anyT except exotic cases whenD[N,T ] is empty [35],
χ0(N) = the connected component ofD[N,T ] for non-exoticT
containing a solution of gluing eqns corresponding toAhyp.
(2.32)
We currently do not have the ﬁeld theoretic understanding of the exotic case and will always
work with non-exotic triangulations.
– 11 –
SU (2)/SO(3)-type of boundary cycleA For later use, we classify a primitive boundary
cycle A into two types, SU (2) or SO(3), depending on evenness/oddness of the linear
coeﬃcients (αi,α′′
i ).
A is of
{
SU (2)-type, if all (αi,α′′
i ) can be chosen as even-integers
SO(3)-type, otherwise
(2.33)
Note that the linear coeﬃcients are deﬁned modulo the following shifts due to the last
gluing equations in (2.29)
(
αi,α′′
i
)
→
(
αi +
k∑
i=1
cIi(GIi−G′
Ii),α′′
i +
k∑
i=1
cIi(G′′
Ii−G′
Ii)
)
with some integerscIi ,
and A is SU (2)-type if there is a choice ofcIi which makes all(αi,α′′
i ) even-integers. An
alternative deﬁnition ofSO(3)/SU (2) type without relying an ideal triangulation is
A is of
{
SU (2)-type, A∈ Ker
(
i∗ :H1(∂N, Z)→H1(N, Z2)
)
SO(3)-type, otherwise
(2.34)
Two deﬁnitions, (2.33) and (2.34), are equivalent [36]. An explanation ofSU (2)/SO(3)
types from the 6dN = (2, 0) theory point of view is discussed in Appendix B.
TDGG[N,XA] from symplectic gluing The gluing equations are known to have the
following symplectic structure [36, 37] which play a crucial role in the DGG’s construction.
Upon a skew-symmetric bilinear{ , } deﬁned by{Zi,Z′
j} ={Z′
i,Z′′
j} ={Z′′
i,Zj} = δij,
internal edge variables{CI} and the boundary holonomy variablea around A satisfy the
followings:
{CI,CJ} ={a,CI} = 0, for allI,J = 1,...,k (2.35)
Further we can choose a linearly independent primitive cycleB∈H1(∂N, Z) such that
{a,b} =−2, (2.36)
where b is related to the holonomy alongB as in eq. (2.31). The choice ofB is not unique
but have the following freedom of choice
B→B +kA, k ∈ Z. (2.37)
Using the freedom, we will always chooseB to have the properties that
B is of
{
SU (2) type, when A is ofSO(3) type ,
SO(3) type, when A is ofSU (2) type ,
(2.38)
where theSU (2)/SO(3) types ofB-cycle is deﬁned in the same way asA.
– 12 –
Amongk-internal edge variables in eq. (2.28), onlyk− 1 of them6 are linearly indepen-
dent modulo linear relations in (2.26). Let the linearly independent set as{CI}k−1
I=1. Then,
we introduce their conjugate variables{ΓI}k−1
I=1 satisfying
{CI, ΓJ} =δIJ , {a, ΓI} ={b, ΓI} = 0, I,J = 1,...,k − 1. (2.39)
From the choice of (A,B,{CI},{ΓI}), we associate a Sp(2k, Z) matrix gN and integer-
valued 2k-vectorν as follows


XA
C1
...
Ck−1
PB
Γ1
...
Γk−1


=gN·


Z1
Z2
...
Zk
Z′′
1
Z′′
2
...
Z′′
k


+iπνN , (2.40)
where
(XA,PB) =
{
(a
2,b ), when (A,B ) is of
(
SU (2),SO (3)
)
type
(a, b
2), when (A,B ) is of
(
SO(3),SU (2)
)
type
(2.41)
Notice that (XA,PB) are always linear combinations of Zi,Z′′
i with integer coeﬃcients
because of the even-ness condition (2.33).
Using the gluing data summarized in (gN,νN), we can construct the corresponding
TDGG theory. As a ﬁrst step, we preparek-copies of a free chiral theory
Tstep I =T⊗k
∆ =
k times
z }| {
T∆⊗... ⊗T∆,
T∆ := (a free theory of single chiral multipletΦ with CS level−1/2
for non-dynamical background gauge ﬁeld coupled toU(1) ﬂavor symmetry),
LTstep1(V1,...,V k) =
k∑
i=1
1
4π
∫
d4θ(−1
2ΣiVi) +
∫
d4θΦ†
ieViΦi,
(2.42)
where Σi is the ﬁeld strength of the vector multipletVi. The theoryTstep Ihasu(1)k ﬂavor
symmetry and{Vi} are background vector-multiplets coupled to the ﬂavor symmetries.
Using the symmetry, one can considerSp(2k, Z) action on the theory which is a gen-
eralization of Witten’sSL(2, Z) action [38] which corresponds tok = 1 case. To be more
explicit, one needs to decompose aSp(2k, Z) into products of “T-type (gt
K),” “S-type (gs
J),”
and “GL-type(ggl
U)”:
gt
K :=
(
I 0
K I
)
, g s
J :=
(
I−J −J
J I −J
)
, g gl
U :=
(
U 0
0 (U−1)t
)
. (2.43)
6More generally, for an ideal triangulation of a knot/link complementN with ♯T torus boundaries the
number of linearly independent internal edge variables arek−♯T.
– 13 –
Here J is a diagonal matrix whose diagonal entries are either 0 or 1. Let LT (⃗V :=
(V1,...,V k)) be a Lagrangian for a theoryT with U(1)k ﬂavor symmetry. Field theoretic
actions of the basic types are
Lgt
K·T (⃗V ) :=LT (⃗V ) + 1
4π
∫
d4θ⃗Σ·K⃗V ,
Lgs
J·T (⃗V ) :=LT ((I−J)⃗V +J⃗V′) + 1
2π
∫
d4θ⃗Σ·J⃗V′,
Lggl
U·T (⃗V ) :=LT (U−1·⃗V ),
(2.44)
where ⃗V′ only has components such thatJ⃗V′ = ⃗V′, and they are now dynamical ﬁelds. As
for theSL(2, Z) case, the ﬁnal theory does not depend on the decomposition and depends
only on theSp(2k, Z) element.
Now the second step of the construction is
Tstep II =gN·Tstep I, (2.45)
wheregN is the symplectic matrix in (2.40) obtained from an ideal triangulation ofN. The
gN-transformed theory still hasu(1)k ﬂavor symmetry
U(1)XA×U(1)C1×... ×U(1)Ck−1 , (2.46)
whose background gauge ﬁelds areVXA :=V1,...,V Ck−1 :=Vk in Tstep II.
As a ﬁnal step, we break theU(1)k to its subgroup by adding chiral operators to the
superpotential
LTDGG[N,XA] =LTstep II +
( ∑
‘easy’CI
∫
d2θOCI +c.c
)
. (2.47)
An internal edgeCI =∑k
i=1(GIiZi +G′
IiZ′
i +G′′
IiZ′′
i ) in (2.28) is called ‘easy’ [19] if at most
one ofGIi, G′
Ii and G′′
Ii is nonzero for eachi,
k∑
i=1
(GIiG′
Ii +G′
IiG′′
Ii +G′′
IiGIi) = 0 (2.48)
and ‘hard’ otherwise. This condition simply means that only one of edge parameters (Zi,Z′
i
andZ′′
i ) ofi-th tetrahedron appears inCI for alli = 1...k . Upon a proper choice of cyclic
relabeling (2.27) of edge parameters, we can make such an internal edgeCI as a linear
combination of onlyZis:
CI =
k∑
i=1
~GIiZi, G Ii∈{ 0, 1, 2}. (2.49)
Then, the gauge-invariant chiral primary operatorOCI in Tstep II is given by
OCI =
k∏
i=1
Φ
~GIi
i . (2.50)
– 14 –
As will be explained below, diﬀerent cyclic labelings give diﬀerent descriptions ofTstep II
which are related by a sequence of basic dualities in (2.56). Therefore for each easy internal
edgeCI, there is a chiral primary operatorOCI which can be written as the above form in
a duality frame. The operator is charged only underU(1)CI. For each hard internal edge,
on the other hand, there may only be a corresponding gauge invariant dyonic 1/4 BPS
operator with non-zero spin. There is no way to write down a supersymmetric deformation
using the dyonic local operators.
Hard internal edges and accidental symmetries In the original DGG’s construc-
tion [19], they proposed to use ideal triangulations with only easy internal edges. From
superﬁcial counting, we expect the resultingTDGG[N] has ﬂavor symmetry of rank1 whose
Cartan corresponds to theU(1)XA.
If allCI are easy, we superﬁcially expect that
U(1)XA×U(1)C1×... ×U(1)Ck−1 in Tstep II
Superpotential deformation in (2.47)
−−−−−−−−−−−−−−−−−−−−−−−−−→U(1)XA in TDGG[N,XA]
(2.51)
The counting sounds compatible with the 6d construction since the knot gives a ﬂavor
symmetry (su(2)) of rank 1. But the counting could be wrong as we will see below for the
case with an ideal triangulation ofN = (ﬁgure-eight knot complement) with 6-tetrahedra.
The correct rank is always equal or greater than the superﬁcial counting. In our modiﬁed
proposal (2.47), we can use any ideal triangulation and will argue that the resulting theory
is independent of the choice of ideal triangulation regardless of existence of hard edges.
One of the consequences is that rank of the ﬂavor symmetry could be larger than1 because
the number of independent easy edges could be less than(k− 1). From the counting of
linearly independent easy internal edges, we checked thatTDGG theories for most of knot
complements in SnapPy’s census have additional symmetries.
For example, we show theSU (3) symmetry for all hyperbolic twist knots in section
3.2. The additional symmetries are accidental and unexpected from 6d viewpoint. The
above DGG’s construction can be generalized to higherK (number of M5-branes) cases [9]
and there is no such an additional symmetry whenK is suﬃciently large. For higherK
one need to use a so-calledK-decomposition which replace a single tetrahedron in an ideal
triangulation into 1
6K(K2− 1) copies of ﬁner building blocks, octahedra. The construction
of the 3d theory for higherK is parallel to the construction forK = 2 case reviewed above
except tetrahedra in an ideal triangulation are replaced by octahedra in aK-decomposition.
We assign 3 complex parameters (z,z′,z′′) to each pair of two vertices of an octahedron
and their gluing equations in aK-decomposition also possess a symplectic structure. One
diﬀerence in higherK is that there are enough number of easy internal edges (better to call
internal vertices forK-decomposition case) to break allu(1) symmetries except the ones
expected from 6d viewpoint. 6d viewpoint expect that the 3d theory has a ﬂavor symmetry
of rank (K− 1). A hard internal edge appears when two edges of a single tetrahedron are
glued to the internal edges simultaneously. InK-decomposition, two diﬀerent vertices of a
single octahedron can not meet at an internal vertex possibly except when the octahedron
– 15 –
is located nearest to one of vertices of tetrahedrons. So the number of hard internal vertices
will be at most order ofk (the number of tetrahedrons in a triangulation) while there are
kK(K2−1)
6 internal vertices among which(K− 1) are linearly dependent. So the number of
easy internal vertices arek
(K(K2−1)
6 −o(1)
)
which is large enough to span the
(
kK(K2−1)
6 −
(K− 1)
)
-linearly independent internal vertices for suﬃciently largeK.
Topological invariance ofTDGG[N,XA] At ﬁrst glance, the above construction seems
to depend on the various choices other than(N,A ). For the construction, we choose an
ideal triangulation ofN. All diﬀerent ideal triangulations of a given 3-manifold are known
to be related by sequence of a basic local move called 2-3 Pachner move. In the DGG’s
construction, the geometric move corresponds to a mirror symmetry between a 3dN =
2 SQED with two chirals (ΦA, ΦB) of charge (+1,−1) and a free theory with 3 chirals
(M,Tp,Tm):
∫
d4θ
(
Φ†
AeV ΦA + Φ†
Be−V +UΦB + 1
4π (U + 2W )(ΣV− 1
2ΣU)
)
(V : dynamical)
≃
∫
d4θ
(
M†eUM + (Tp)†eWTp + (Tm)†e−U−WTm
)
+
(∫
d2θMTpTm +c.c
) (2.52)
Under the duality, gauge-invariant chiral operators are mapped as follows
ΦAΦB ↔ M
V+ (BPS monopole operator of magnetic ﬂux+1) ↔ Tp (2.53)
V− (BPS monopole operator of magnetic ﬂux−1) ↔ Tm
So the TDGG theory is invariant under the local 2-3 move and thus independent on the
choice ofT . For a given choice ofT , we still have freedoms of choosing cyclic labeling
(2.27) of edge parameters for each tetrahedron.
(
Z
Z′′
)
→
(
Z′
Z
)
=ST·
(
Z
Z′′
)
+iπ
(
1
0
)
,
S :=
(
0−1
1 0
)
, T :=
(
1 0
1 1
)
.
(2.54)
The invarianceTDGG theory under choice is guaranteed from a duality
T∆≃ (ST )·T∆. (2.55)
More explicitly, the duality is
∫
d4θ
(
Φ†eUΦ− 1
8πUΣU
)
≃
∫
d4θ
(
Φ†eV Φ + 1
8πV ΣV + 1
2πUΣV
)
, (V : dynamical).
(2.56)
– 16 –
In the construction ofTDGG theory, we also need to choose conjugate variables{PB, ΓI}.
But these choices only aﬀect the background Chern-Simons coupling coupled to ﬂavor sym-
metries. So modulo the background CS couplings, the theory only depends on the topolog-
ical choice(N,A ). To specify the background Chern-Simons coupling of theU(1)XA ﬂavor
symmetry associated to the knot, we sometimes specify the choice of boundary cycleB and
denote the theory by
TDGG[N,XA;PB]. (2.57)
Example :N =S3\41 =m004 with an ideal triangulation with 2 tetrahedraHere
41 is a simpliﬁed notation, called Alexander-Briggs notation, for ﬁgure-eight knot which is
depicted in ﬁg 3. The notation simply means that the ﬁgure-eight knot is the 1st (simplest)
knot with 4 crossings. The fundamental group of the knot complement is
π1(S3\41) =⟨α,β,γ :αγ−1βα−1γ =βγ−1β−1α = 1⟩. (2.58)
The group contains a peripheral subgroupZ× Z which can be identiﬁed as fundamental
group of boundary torus
π1
(
∂(S3\41)
)
=π1(T2) = Z× Z =⟨µ,ν⟩⊂ π1(S3\41) (2.59)
Canonical choice of the basis(µ,λ ) is (meridian, longitude). Upon the basis choice, the
embedding i :π1
(
∂(S3\41)
)
→π1(S3\41) is given by
i(µ) =α, i (ν) =αγ−1βγα−1β−1 (2.60)
The knot complement can be ideally triangulated by two tetrahedrons.
T : S3\41 = (∆1∪ ∆2)/∼ . (2.61)
See ﬁg. 3 below for the gluing rule∼. There are two internal edges in the triangulation
z1 z2
S3\=
Figure 3. The simplest ideal triangulation ofm004 =S3\41.
which are linearly dependent modulo the linear equations in (2.26).
C1 =Z′′
1 +Z′
2 + 2Z′
1 + 2Z2, C 2 =Z′′
1 +Z′
2 + 2Z1 + 2Z′′
2 . (2.62)
– 17 –
The deformation variety in this example is
D[S3\41,T ] ={z1,z′
1,z′′
1,z 2,z′
2,z′′
2 :z−1
i +z′′
i− 1 = 0, ziz′
iz′′
i =−1, z′′
1(z′
1)2z′
2z2
2 = 1}i=1,2.
(2.63)
Each point in the variety gives aPSL (2, C) = SL(2, C)/⟨±1⟩ ﬂat connection on the knot
complement. The holonomy matrices along the basis (α,β,γ ) of π1(S3\41) for the ﬂat
connections is
ρhol(α) =


√
z1
z2
0
−1+z1√z1z2
√
z2
z1

 ,
ρhol(β) =


√
z′
2
z′′
1
−
√
z′
2
z′′
1√
z′′
1z′
2 −
√
z′′
1
z′
2
(z′
2− 1)

 ,
ρhol(γ) =


z′
1+z′′
2−1√
z′
1z′′
2
1−z′
1√
z′
1z′′
2
z′′
2−1√
z′
1z′′
2
1√
z′
1z′′
2

 .
(2.64)
Boundary (meridian, longitudinal) holonomies are
ρhol(µ) = Hol(α) =
(
eaµ/2 0
∗ e−aµ/2
)
, a (µ) =Z1−Z2,
ρhol(ν) = Hol(αγ−1βγα−1β−1) =
(
ebλ/2 0
∗ e−bλ/2
)
, b λ = 2(Z1−Z′
1).
(2.65)
So, (µ,λ ) is of (SO(3),SU (2)) type and we choose
Xµ =aµ =Z1−Z2, P λ =bλ/2 =Z1−Z′
1. (2.66)
With the choices, theSp(4, Z) matrix gm004 in (2.40) is given by
gm004 =


1 −1 0 0
−2 1 −1−1
2 0 1 0
0 1 0 0

 , (2.67)
which can be decomposed intogm004 =gs
Jm004gt
Km004ggl
Um004 with (2.43)
Um004 =
(
1−1
0 1
)
, K m004 =
(
2 2
2 1
)
, J m004 =
(
0 0
0 1
)
. (2.68)
– 18 –
Following each steps in eq. (2.42),(2.45) and (2.47),TDGG[m004,Xµ;Pλ] is given by
LTstep1(V1,V 2) =LT⊗2
∆
= 1
4π
∫
d4θ(−1
2Σ1V1− 1
2Σ2V2) +
∫
d4θ(Φ†
1eV1Φ1 + Φ†
2eV2Φ2),
LTDGG[m004,Xµ;Pλ](VX,VC) =LTstep2(VX,VC)
= 1
4π
∫
d4θ
(
−1
2ΣCVX + Σ(2VC + 3VX)
)
+
∫
d4θ
(
Φ†
1eV +VX
2 Φ1 + Φ†
2eV−VX
2 Φ2
)
.
(2.69)
HereV (with Σ := ¯DDV ) is a dynamicalU(1) vector multiplet whileVX(ΣX) andVC(ΣC)
are background multiplets coupled to ﬂavor symmetries,U(1)XA and sayu(1)C respectively.
Note that both of C1 and C2 are hard internal edges and we can not break theu(1)C
associated to them.
Example :N =S3\41 =m004 with an ideal triangulation with 6 tetrahedraThe
absence of chiral primary operators corresponding to hard edges in the above construction
ofTDGG[m004,Xµ;Pλ] using 2 tetrahedra were already noticed in [19]. The interpretation
there was that this is due to the “bad" choice of triangulation, which contains hard internal
edges, and can be cured by choosing a proper ideal triangulation which does not have a
hard internal edge. As a “good" ideal triangulation form004, they propose the one using
six tetrahedra, ∆R,S,X,Y,Z,W . The internal edges in the triangulation are [19]
C1 =X +W + 2(R′ +S′ +Z′′), C 2 =R +Y + 2(Z′ +W′ +S′′),
C3 =S +W + 2(R′′ +X′′ +Y′), C 4 =R +Z + 2(Y′′ +W′′ +X′),
C5 =X +Y, C 6 =S +Z.
(2.70)
Note that there is no hard internal edges in the triangulation and 5 internal edges are
linearly independent. Superﬁcial counting suggests that the resulting theory have a ﬂavor
symmetry of rank6− 5 = 1, where ﬁveu(1)s are broken by superpotential operators.
Our interpretation on this problem is diﬀerent from [19]. We claim that the theory
realized by six tetrahedra is actually completely the same as the one realized by two tetra-
hedra in the low energy limit. Therefore, the theory constructed by six tetrahedra has a
hidden additional u(1) symmetry in the low energy limit which corresponds to the hard
edge in the triangulation with two tetrahedra.
To see it, let us focus on the two tetrahedra∆X and ∆Y, which are glued in such a
way that the system has the internal edgeC5 =X +Y. Then, this theory is described by
two chiral ﬁeldsΦX and ΦY with the Lagrangian
∫
d4θ(Φ†
XΦX + Φ†
Y ΦY ) +
∫
d2θΦXΦY + h.c., (2.71)
where we have neglected background ﬁelds. The superpotential is due to the presence of
the internal edge C5 = X +Y. Then it is clear that these ﬁelds ΦX and ΦY can be
integrated out and the theory becomes empty in the low energy limit. This means that
two tetrahedra ∆X and ∆Y are eliminated. Mathematically this corresponds to the 0-2
– 19 –
move. The invariance of a topological quantity called 3d index (see appendix A) under
the 0-2 move is proven in [39]. The deﬁnition of the topological quantity is based on ideal
triangulation and is equivalent to the localization expression for the superconformal index
ofTDGG theory. Intuitively, the constraints0< Im[X], Im[Y ]<π andC5 = 2πi mean that
Im[X], Im[Y ]→π, and hence these tetrahedra are squashed to be ﬂat. The same comment
also applies to∆S, ∆Z and C6 =S +Z.
At the level of edge variables, the process of integrating out the massive ﬁelds may be
done by eliminating the variables corresponding to the massive ﬁelds. More explicitly, we
deﬁne
C′
1 :=C3 +C4 + 2C5−C6− 4πi =W +R + 2W′′ + 2R′′ (2.72)
C′
2 :=C1 +C2−C5 + 2C6− 4πi =W +R + 2W′ + 2R′, (2.73)
After renamingW→Z′′
1, R→Z′
2 and so on, these variablesC′
1 and C′
2 become the same
as the ones in the triangulation with two tetrahedra.
