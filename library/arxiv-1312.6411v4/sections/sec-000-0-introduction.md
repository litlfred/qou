---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-000-0-introduction
section_title: "Introduction"
section_number: 0
pages: 1-7
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
1. DG Modules and their Resolutions 7
2. Cohomological Dimension 11
3. Reduction and Lifting 16
4. Localization of Commutative DG Rings 19
5. Perfect DG Modules 24
6. Tilting DG Modules 30
7. Dualizing DG Modules 35
8. Cohen-Macaulay DG Modules 43
Date: 22 March 2016.
Key words and phrases.DG rings, DG modules, derived categories.
Mathematics Subject Classiﬁcation2000. Primary: 13D09; Secondary: 13D07, 18G10, 16E45.
Grants: Supported by Israel Science Foundation grant no. 253/13.
Notice regarding publication: The author has decided not to submit the present version of the paper
toapeerreviewedjournal. Thisdecisionisbasedonfrustratingexperiencewithsubmissionsofearlier
versions.
1
arXiv:1312.6411v4  [math.AG]  22 Mar 2016
2 AMNON YEKUTIELI
9. Rigid DG Modules 47
References 51
0. Introduction
In this paper we are interested incommutative DG rings. This is an abbreviation
for strongly commutative nonpositive associative unital diﬀerential graded alge-
bras overZ. Thus a commutative DG ring is a graded ringA =⨁
i≤0 Ai, together
with a diﬀerentiald of degree 1, that satisﬁes the graded Leibniz rule. The mul-
tiplication satisﬁesb· a = (−1)ij· a· b for alla∈ Ai and b∈ Aj, and a· a = 0 if i
is odd. By default, the DG rings in the Introduction are commutative. Rings are
viewed as DG rings concentrated in degree0 (so they are commutative by default
throughout the Introduction).
CommutativeDGringscomeupinthefoundationsof derivedalgebraicgeometry ,
as developed by Toën-Vezzosi [TV]. Indeed, aderived stackis a stack of groupoids
on the site of commutative DG rings (with its étale topology). Some precursors
of this point of view are the papers [Hi2], [Ke2], [KoSo] and [Be]. Another role
of commutative DG rings is asresolutions of commutative rings. We shall say more
on this role below, since it was the immediate motivation for writing the present
paper.
Inourpaperwestudy perfect,tilting,dualizing,Cohen-MacaulayandrigidDGmod-
ules over commutative DG rings. We give deﬁnitions that generalize the familiar
deﬁnitions for rings. Many of the results that hold for rings, continue to hold in
the much more complicated DG setting. Later in the Introduction we discuss the
main deﬁnitions and results of the paper, and a couple of conjectures.
ButﬁrstletusexplaintheproblemthatmotivatedourworkoncommutativeDG
rings. Rigiddualizingcomplexes overnoetheriancommutativeringsarethefounda-
tionofanewapproachtoGrothendieckDualityonschemesandDeligne-Mumford
stacks. See the papers [YZ1], [YZ2], [Ye3], [Ye6], [Ye8] and [Ye9]. Rigid dualizing
complexes were introduced by Van den Bergh in the context of noncommutative
rings over a base ﬁeldK; see [VdB]. But for the new approach to Grothendieck
Duality in algebraic geometry, that should apply also to the arithmetic setup, we
are interested in commutative rings over a base commutative ringK that isnot a
ﬁeld.
In this context, the deﬁnition of a rigid complex relies on the more primitive
notionofthe squareofacomplex . Givenacommutative K-ring A,wechoosea K-ﬂat
commutative DG ring resolution˜A→ A relative K. Such resolutions exist, because
we work with strongly commutative DG rings (see Remark 4.3 for a discussion
of this issue). For any complex ofA-modules M, its square is the complex ofA-
modules
(0.1) SqA/K(M) := RHom ˜A⊗K ˜A(A, M⊗L
K M).
The question of independence ofSqA/K(M) of the choice of resolution˜A is very
subtle; and in fact there was a mistake in the original proof in [YZ1] (which has
since been corrected; see [Ye5]). A rigid dualizing complex overA relative toK is
a pair (R, ρ), consisting of a dualizing complexR, and an isomorphismρ : R ≃− →
SqA/K(R) in the derived categoryD(A).
In the course of writing the new paper [Ye7] – which corrects further mistakes
in the earlier paper [YZ1], and extends it – we realized that we need Theorem 0.8,
that deals with Cohen-Macaulay DG modules. This is explained in Remark 8.9.
COMMUTATIVE DG RINGS 3
The parts of the present paper leading to Section 8 set the stage for the deﬁnition
of Cohen-Macaulay DG modules and the proof of Theorem 0.8.
Fromawiderperspective,weexpectthattheresultsinthispapershallﬁndfur-
ther applications in algebra and geometry. One such possible application would
be the development of a theory ofrigid dualizing complexes in derived algebraic ge-
ometry (of either ﬂavor: Lurie’s or Toën’s). Indeed, a commutative DG ring is an
aﬃne derived scheme; so what is needed is a way to sheaﬁfy our constructions.
That should be facilitated by theétale descentand étale codescentproperties ofrigid
residue complexes(see [Ye6]).
Ourworkinthepresentpapershouldbeeasilyaccessibletoanyonewithawork-
ing knowledge of the derived category of modules over a ring (e.g. from the book
[We]). This is because the methods we use are basically the same; there are only
slight modiﬁcations. The necessary tools to upgrade from rings to DG rings (such
as K-injective resolutions in place of injective resolutions) are recalled in Section
1 of our paper. We do not resort at all to the daunting technicalities ofE∞ rings.
Likewise, we do not touch simplicial methods or Quillen model structures.
Let us now describe the work in this paper. Consider a commutative DG ring
A =⨁
i≤0 Ai. Its cohomologyH(A) = ⨁
i≤0 Hi(A) is a commutative graded ring.
Weusethenotation ¯A := H0(A). ThereisacanonicalhomomorphismofDGrings
A→ ¯A. Wesaythat Aiscohomologicallypseudo-noetherian if ¯Aisanoetherianring,
and Hi(A) is a ﬁnite (i.e. ﬁnitely generated)¯A-module for everyi. (Note that this
is weaker than the condition that the ringH(A) is noetherian.)
The category of DGA-modules is denoted byC(A). It is a DG category, and
its derived category, gotten by inverting the quasi-isomorphisms, is denoted by
D(A). Therearefulltriangulatedsubcategories D+(A), D−(A)and Db(A)of D(A),
madeupoftheDGmodules Mwithboundedbelow,boundedaboveandbounded
cohomologies, respectively. The full subcategory ofD(A) on the DG modulesM,
whose cohomology modulesHi(M) are ﬁnite over¯A, is denoted byDf(A). As
usual, for any boundedness condition⋆ we letD⋆
f (A) := Df(A)∩ D⋆(A). If A is
cohomologically pseudo-noetherian, then the categoriesD⋆
f (A) are triangulated,
and A∈ D−
f (A). In caseA is a ring, thenD(A) = D(Mod A), the derived category
of A-modules.
In Section 1 we recall some facts on DG modules. We mention several kinds of
resolutions of DG modules, and special attention is paid to semi-free resolutions.
Section 2 is about various notions of cohomological dimension for DG modules
and derived functors. For instance, in Deﬁnition 2.4 we introduce the projective
and injective dimensions of a DGA-module M relative to a subcategoryE⊆ D(A).
In Section 3 we study the reduction functorD(A)→ D( ¯A), M↦→ ¯A⊗L
A M. We
show that projective¯A-modules can be lifted to DGA-modules.
In Section 4 we discuss localization of a commutative DG ringA on Spec ¯A.
We introduce theČech resolutionC(M; a) of a DG A-module M, associated to a
covering sequencea = ( a1, . . . , an) of ¯A. In case there is a decompositionSpec ¯A =
∐n
i=1 Spec ¯Ai into open-closed subsets, we show that there are canonically deﬁned
DG rings A1, . . . , An, and a DG ring quasi-isomorphismA→ ∏n
i=1 Ai, that inH0
recovers the decomposition¯A∼= ∏n
i=1 ¯Ai.
The topic of Section 5 isperfect DG modules. A DGA-module P is calledgeo-
metrically perfectif locally onSpec ¯A it is isomorphic, in the derived category, to a
ﬁnite semi-free DG module. See Deﬁnition 5.4 for the precise formulation. This
deﬁnition appears to be completely new for DG rings. WhenA is a ring (so that
A = A0 = ¯A), this deﬁnition coincides with the one in [SGA 6, Exposé I], since
4 AMNON YEKUTIELI
a ﬁnite semi-free DG module over a ring is just a bounded complex of ﬁnite free
modules.
A DG A-module P is calledalgebraically perfectif it can be ﬁnitely built fromA
by shifts, direct summands and cones. In other words, ifP belongs to the epaisse
subcategoryof D(A)classicallygeneratedby A,inthesenseof[BV]. Thisdeﬁnition
(without the qualiﬁcation “algebraically”) was already used in [ABIM].
When Aisaring,itisknownthatgeometricallyperfectcomplexesarethesame
as algebraically perfect complexes; see [SGA 6, Exposé I]. Therefore they are just
called “perfect complexes”.
Here is the main result Section 5. It is a combination of Theorem 5.11, Theorem
5.20 and Corollary 5.21.
Theorem 0.2. Let A be a commutative DG ring, and letP be a DG A-module. The
following four conditions are equivalent:
(i) The DGA-module P is geometrically perfect.
(ii) TheDG A-module Pisin D−(A),andtheDG ¯A-module ¯A⊗L
A Pisgeometrically
perfect.
(iii) For anyM, N∈ D(A), the canonical morphism
RHomA(P, M)⊗L
A N→ RHomA(P, M⊗L
A N)
in D(A) is an isomorphism.
(iv) The DGA-module P is algebraically perfect.
If Aiscohomologicallypseudo-noetherian,thenthefourconditionsaboveareequivalentto :
(v) The DG A-module P is inD−
f (A), and it has ﬁnite projective dimension relative
to D(A).
When A is a commutative ring, conditions (i) and (ii) are essentially the same;
and (as already mentioned above) the equivalence of conditions (i) and (iv) was
proved in [SGA 6]. But for DG rings this is a new result. In light of Theorem 0.2
we can unambiguously talk about “perfect DG modules”.
Section 6 is abouttilting DG modules. A DGA-module P is said to be tilting if
there is some DG moduleQ such thatP⊗L
A Q∼= A in D(A). The DG moduleQ is
called a quasi-inverse ofP. The next theorem is repeated as Theorem 6.5.
Theorem 0.3. Let A be a commutative DG ring, and letP be a DG A-module. The
following four conditions are equivalent:
(i) The DGA-module P is tilting .
(ii) The functorP⊗L
A− is an equivalence ofD(A).
(ii) The functorRHomA(P,−) is an equivalence ofD(A).
(iv) TheDG A-module Pisperfect,andtheadjunctionmorphism A→ RHomA(P, P)
in D(A) is an isomorphism.
A combination of Theorems 0.3 and 0.2 implies that the DGA-module Q :=
RHomA(P, A) is a quasi-inverse of the tilting DG moduleP.
As in [Ye2], we deﬁne thecommutative derived Picard groupDPic(A) to be the
group whose elements are the isomorphism classes of tilting DGA-modules, and
the multiplication is induced by−⊗ L
A−.
If A→ B is a homomorphism of DG rings, then the operationP↦→ B⊗L
A P
inducesagrouphomomorphism DPic(A)→ DPic(B). ThenextresultisTheorem
6.14 in the body of the paper.
Theorem 0.4. Let A be a commutative DG ring. The canonical group homomorphism
DPic(A)→ DPic( ¯A)
is bijective.
COMMUTATIVE DG RINGS 5
In an earlier version of the paper we had a ﬁniteness condition: we required
Spec ¯A to have ﬁnitely many connected components. But, as noticed by Negron
[Ng], this condition is superﬂuous.
It is known that the commutative derived Picard group of the ring¯A has this
structure:
DPic( ¯A)∼= Pic( ¯A)× Flc(Spec ¯A, Z) .
Here Flc(Spec ¯A, Z) is the group of locally constant functionsSpec ¯A→ Z, and
Pic( ¯A)istheusual(commutative)Picardgroup. SeeTheorem6.13,duetoNegron,
that reﬁnes earlier results in [Ye2], [RZ] and [Ye4].
In Section 7 we talk aboutdualizing DG modules. HereA is a cohomologically
pseudo-noetherian commutative DG ring. A DGA-module R∈ D+
f (A) is called
dualizing if it has ﬁnite injective dimension relative toD(A), and the adjunction
morphism A→ RHomA(R, R) is an isomorphism. Note that whenA is a ring,
this is precisely the original deﬁnition found in [RD]; but for a DG ring there are
severalpossiblenotionsofinjectivedimension, andthecorrectonehastobeused.
See Deﬁnition 2.4(2) and Remark 2.9. Note also thatR need not have bounded
cohomology – see Corollary 7.3 and Example 7.26. For comparisons to dualizing
DG modules, as deﬁned previously in [Hi1], [FIJ] and [Lu2], see Example 7.23,
Proposition 7.17 and Remark 7.27 respectively.
A DG ringA is calledtractable if it is cohomologically pseudo-noetherian, and
there is a homomorphismK→ A from a ﬁnite dimensional regular noetherian
commutative ringK, such that the induced homomorphismK→ ¯A is essentially
ﬁnite type. Such a homomorphismK→ A is called atractionfor A.
The next result is a combination of Theorem 7.9 and Corollary 7.11. WhenA is
a ring, this was proved by Grothendieck [RD, Sections V.3 and V.10].
Theorem 0.5. Let A be a tractable commutative DG ring. Then:
(1) A has a dualizing DG module.
(2) The operation(P, R)↦→ P⊗L
A R, for a tilting DG moduleP and a dualizing DG
module R, induces a simply transitive action of the groupDPic(A) on the set of
isomorphism classes of dualizing DGA-modules.
In particular, if ¯A is a local ring, then by Theorems 0.4 and 6.13 we have
DPic(A)∼= Z. Thus any two dualizing DGA-modules R, R′ satisfy R′ ∼= R[m]
for an integerm.
A combination of Theorems 0.4 and 0.5 yields (see Corollary 7.12):
Corollary 0.6. If A is a tractable commutative DG ring, then the operationR ↦→
RHomA( ¯A, R) induces a bijection
{dualizing DGA-modules}
isomorphism
≃− →{dualizing DG ¯A-modules}
isomorphism .
Here is a result that is quite surprising. It relies on a theorem of Jørgensen [Jo],
who proved it in the local case (i.e. when¯A is a local ring).
Theorem0.7. Let AbeacohomologicallyboundedtractablecommutativeDGring. If ¯Ais
aperfectDG A-module,thenthecanonicalhomomorphism A→ ¯Aisaquasi-isomorphism.
This is repeated (in slightly stronger form) as Theorem 7.21 in the body of the
paper. See Remark 7.25 for an interpretation of this theorem.
Section8ofthepaperisabout Cohen-MacaulayDGmodules. Thedeﬁnitiondoes
not involve regular sequences of course; nor does it involve vanishing of local co-
homologies as in [RD] (even though it could probably be stated in this language).
Instead we use a fact discovered in [YZ3]: for a noetherian schemeX with dual-
izing complexR, a complexM∈ Db
c (ModOX) is CM (in the sense of [RD], for
6 AMNON YEKUTIELI
the dimension function determined byR) iﬀRHomOX (M,R) is (isomorphic to) a
coherent sheaf. In [YZ3] the CM complexes insideDb
c (ModOX) were also called
perverse coherent sheaves.
With the explanation above, the next deﬁnition makes sense. LetR be a dual-
izing DG A-module. A DG moduleM∈ Db
f (A) is calledCM with respect toR if
RHomA(M, R)∈ D0
f (A). HereD0
f (A)is thefull subcategory ofD(A)consisting of
DG modules with ﬁnite cohomology concentrated in degree0; and we know that
it is equivalent to the categoryModf ¯A of ﬁnite¯A-modules.
The next theorem is repeated, in slightly greater generality, as Theorem 8.7.
Theorem 0.8. Let f : A→ B be a homomorphism between tractable commutative DG
rings, such thatH0( f ) : ¯A→ ¯B is surjective. LetRB be a dualizing DGB-module, and
let M, N∈ Db
f (B).
(1) If M is CM w.r.t.RB, and there is an isomorphismrest f (M) ∼= rest f (N) in
D(A), thenN is also CM w.r.t.RB.
(2) If M and N are both CM w.r.t.RB, then the homomorphism
rest f : Hom D(B)(M, N)→ HomD(A)
(
rest f (M), restf (N)
)
is bijective.
In the theorem, rest f : D(B) → D(A) is the restriction functor. As already
mentioned, Theorem 0.8 is needed in [Ye7].
Inourpaper[Ye5]weintroducethe squaringoperation forcommutativeDGrings.
Theconstructiongoeslikethis. Theinputisahomomorphism A→ Bofcommuta-
tive DG rings. To this datum we associate a functorSqB/A from D(B) to itself. The
formula is a bit more general than (0.1): we choose any K-ﬂat DG ring resolution
˜A→ ˜B of A→ B (see Section 9), and we deﬁne
(0.9) SqB/A(M) := RHom ˜B⊗ ˜A ˜B(B, M⊗L
˜A M)∈ D(B).
The proof that this deﬁnition does not depend on the resolution˜A→ ˜B is quite
diﬃcult.
A rigid DG moduleover B relative to A is a pair(M, ρ), consisting of a DGB-
module M, and arigidifying isomorphism ρ : M ≃− →SqB/A(M) in D(B). There is a
notionofrigidmorphismbetweenrigidDGmodules(Deﬁnition9.3). Hereareour
results on rigid DG modules. The ﬁrst is a DG version of [YZ1, Theorem 0.2], and
it is repeated as Theorem 9.4.
Theorem0.10. Let A→ BbeahomomorphismofcommutativeDGrings,andlet (M, ρ)
be a rigid DG module overB relative toA. Assume that the adjunction morphismB→
RHomB(M, M)in D(B)isanisomorphism. Thentheonlyrigidautomorphismof (M, ρ)
is the identity.
Next is a DG version of the uniqueness in [YZ2, Theorem 1.1](1). It is repeated
as Theorem 9.7.
Theorem 0.11. Let A be a tractable commutative DG ring, with tractionK→ A. Sup-
pose (R, ρ) and (R′, ρ′) are rigid dualizing DG modules overA relative toK. Then there
is a unique rigid isomorphism(R, ρ)∼= (R′, ρ′).
Thus we can call(R, ρ) therigid dualizing DG module ofA relative toK.
Conjecture 0.12.In the situation of Theorem 0.11, the rigid dualizing DG module
over A relative toK exists.
COMMUTATIVE DG RINGS 7
Indeed, we give more detailed conjectures in Section 9, that would imply Con-
jecture0.12. When Aisaring,theseassertionswerealreadyprovedin[YZ1](with
some corrections in [Ye7]). In caseA has bounded cohomology, Conjecture 0.12
was very recently proved by Shaul [Sh2].
We end the Introduction with another conjecture on rigid DG modules.
Conjecture0.13. InthesituationofTheorem 0.11,let (M, ρ)bearigidDGmodule
over A relative toK. Assume that M∈ D+
f (A), and thatM is nonzero on each
connected component ofSpec ¯A. Then M is a dualizing DGA-module.
When Aisaringand M∈ Db
f (A),thiswasprovedin[YZ2]and[AIL]. Moreon
this conjecture in Remark 9.9.
Acknowledgments. I wish to thank Peter Jørgensen, Bernhard Keller, Vladimir
Hinich,LiranShaul,JamesZhang,AmnonNeeman,DennisGaitsgory,RishiVyas,
Matan Prasma, Jacob Lurie, Benjamin Antieau, John Palmieri, Pieter Belmans,
Michel Vaquié, Joseph Lipman, Srikanth Iyengar and Cris Negron for helpful dis-
cussions.
