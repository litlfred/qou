---
doc_id: arxiv-1312.6411v4
doc_title: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-001-1-dg-modules-and-their-resolutions
section_title: "DG Modules and their Resolutions"
section_number: 1
pages: 7-11
source_pdf: 1312.6411v4.pdf
source_sha256: ceac22eb8ffe87e6
doc_brief: "DUALITY AND TILTING FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — We consider commutative DG rings (better known as nonpositive stronglycommutativeassociativeunitalDGalgebras)."
---
A DG ring(usually called an associative unital DG algebra overZ) is a graded
ring A = ⨁
i∈Z Ai, with diﬀerentiald of degree 1, satisfying the graded Leibniz
rule
d(a· b) = d(a)· b + (−1)i· a· d(b)
for a∈ Ai and b∈ Aj. AhomomorphismofDGringsisadegree 0ringhomomor-
phismthatcommuteswiththediﬀerentials. Inthiswaywegetacategory,denoted
by DGR. Rings are viewed as DG rings concentrated in degree0. For a DG ringA,
the cohomologyH(A) = ⨁
i∈Z Hi(A) is a graded ring.
The opposite of the DG ringA is the DG ringAop, which is the same graded
abelian group as A, with the same diﬀerential, but the multiplication· op is re-
versedinthegradedsense. Namely, forelements a∈ Ai and b∈ Aj, theirproduct
in Aop is
a· op b := (−1)ij· b· a.
A left DGA-module is a graded leftA-module M =⨁
i∈Z Mi, with diﬀerential
d satisfying the graded Leibniz rule. IfM is a left DGA-module then H(M) =⨁
i∈Z Hi(M) is a graded leftH(A)-module. Note that a right DGA-module is the
same as a left DGAop-module.
Convention 1.1.By default, in this paper all DG modules are left DG modules.
From Section 4 onwards our DG rings will be commutative, and for them the
distinction between left and right DG modules becomes negligible.
Deﬁnition 1.2.Let A be a DG ring. The category of (left) DGA-modules, withA-
linearhomomorphismsofdegree 0thatcommutewithdiﬀerentials,isdenotedby
DGMod A,orbyitsabbreviation C(A). Thederivedcategory,gottenfrom DGMod A
by inverting quasi-isomorphisms, is denoted byD(DGMod A), or by the abbrevia-
tion D(A).
For information onD(A) see [BL, Section 10], [Ke1, Section 2] or [SP, Section
09KV]. If A is a ring, thenC(A) = C(Mod A), the category of complexes ofA-
modules; and D(A) = D(Mod A), the usual derived category of the abelian cate-
gory Mod A.
Deﬁnition 1.3.Let A =⨁
i∈Z Ai be a DG ring.
8 AMNON YEKUTIELI
(1) We say thatA is a nonpositive DG ringif Ai = 0 for alli > 0.
(2) If A is nonpositive DG ring, then we write¯A := H0(A), which is a ring.
There is a canonical DG ring homomorphismA→ ¯A.
Thefullsubcategoryof DGRonthenonpositiveDGringsisdenotedby DGR≤0.
Convention1.4. Bydefault,inthispaperallDGringsarenonpositive;i.e.wework
inside DGR≤0.
OneoftheimportantadvantagesofnonpositiveDGringsisthatthediﬀerential
dofanyDG A-module Mis A0-linear. Thisimpliesthatthetwosmarttruncations
(1.5) smt≥i(M) :=
(
···→ 0→ Coker(d|Mi−1 )→ Mi+1→ Mi+2→···
)
and
(1.6) smt≤i(M) :=
(
···→ Mi−2→ Mi−1→ Ker(d|Mi )→ 0→···
)
remain within C(A); and there are functorial homomorphismsM→ smt≥i(M)
and smt≤i(M)→ Min C(A),inducingisomorphismsin H≥i and H≤i respectively.
Note that these are the truncationsτ≤n and τ≥n from [SP, Section 0118], that are
variants of the truncationsσ>n and σ≤n from [RD, Section I.7, page 69]. Warn-
ing: thetwostupidtruncationsmightfailtoworkinthiscontext–thesetruncated
complexes of abelian groups might not be DGA-modules.
Recall that for a subsetS ⊆ Z, its inﬁmum isinf(S) ∈ Z∪{± ∞}, where
inf(S) = + ∞ iﬀS = ∅. Likewise the supremum issup(S)∈ Z∪{± ∞}, where
sup(S) =−∞ iﬀS = ∅. For i, j∈ Z∪{ ∞}, the expressionsi + j and−i− j have
obviousvaluesin Z∪{± ∞}. Andfor i, j∈ Z∪{± ∞},theexpression i≤ jhasan
obvious meaning.
Let M =⨁
i∈Z Mi be a graded abelian group. We write
(1.7) inf(M) := inf{i| Mi⁄= 0} and sup(M) := sup{i| Mi⁄= 0}.
The amplitude ofM is
(1.8) amp(M) := sup(M)− inf(M)∈ N∪{± ∞}.
(For M = 0 this readsinf(M) = ∞, sup(M) =−∞ and amp(M) =−∞.) Thus M
is bounded (resp. bounded above, resp. bounded below) iﬀamp(M) < ∞ (resp.
sup(M) < ∞, resp.inf(M) >−∞).
Given i0≤ i1 in Z∪{± ∞}, theinteger intervalwith these endpoints is the set of
integers
(1.9) [i0, i1] :={i∈ Z| i0≤ i≤ i1}.
The integer interval [i0, i1] is said to be bounded (resp. bounded above, resp.
bounded below) ifi0, i1∈ Z (resp. i1∈ Z, resp.i0∈ Z). Thelengthof this interval
is i1− i0∈ N∪{ ∞}. Of course the interval has ﬁnite length iﬀ it is bounded. We
write−[i0, i1] := [−i1,−i0]. Given a second integer interval[j0, j1], we let
[i0, i1] + [j0, j1] := [ i0 + j0, i1 + j1].
For the empty interval∅, the sum is[i0, i1] + ∅ := ∅.
Deﬁnition 1.10.Let M =⨁
i∈Z Mi be a graded abelian group.
(1) We say thatM is concentrated in an integer interval[i0, i1] if
{i∈ Z| Mi⁄= 0}⊆ [i0, i1].
(2) The concentrationof M is the smallest integer intervalcon(M) in whichM
is concentrated.
COMMUTATIVE DG RINGS 9
In other words, ifi0 = inf(M)≤ i1 = sup(M), then the concentration ofM is
theinterval con(M) = [ i0, i1],andtheamplitude amp(M)isthelengthof con(M).
Furthermore, con(M) = ∅ iﬀM = 0.
Given an integer interval[i0, i1], we denote byD[i0,i1](A) the full subcategory
of D(A) consisting of the DG modulesM whose cohomologiesH(M) are concen-
trated in this interval; namelycon(H(M))⊆ [i0, i1]. For i∈ Z we writeDi(A) :=
D[i,i](A). Thesubcategory D[i0,i1](A)isadditive,butnottriangulated. Similarlywe
have the subcategoryC[i0,i1](A)⊆ C(A), consisting of the DG modulesM that are
concentrated in the integer interval[i0, i1]; namelycon(M)⊆ [i0, i1].
Deﬁnition 1.11.Let A be a DG ring.
(1) A DG A-module M is said to becohomologically bounded(resp. cohomologi-
cally bounded above, resp.cohomologically bounded below) if the graded mod-
ule H(M) is bounded (resp. bounded above, resp. bounded below). We
denote byDb(A), D−(A) and D+(A) the corresponding full subcategories
of D(A).
(2) The full subcategory ofD(A) consisting of the DG modulesM, whose co-
homology modulesHi(M) are ﬁnite over¯A, is denoted byDf(A).
(3) For any boundedness condition⋆ we writeD⋆
f (A) := Df(A)∩ D⋆(A).
Thus we have
Db(A) =
⋃
−∞<i0≤i1<∞
D[i0,i1](A) ,
etc. Thecategories Db(A), D−(A)and D+(A)aretriangulated. If ¯Aisleftnoether-
ian, then the categoriesDb
f (A), D−
f (A) and D+
f (A) are also triangulated.
GivenaDG A-module M,itsshiftbyaninteger iistheDGmodule M[i],whose
j-th graded component isM[i]j := Mi+j. Elements of M[i]j are denoted bym[i],
with m∈ Mi+j. The diﬀerential ofM[i] is dM[i](m[i]) := (−1)i· dM(m)[i]. The left
actionof Aon M[i]isalsotwistedby ±1,asfollows: a· m[i] := (−1)ki· (a· m)[i]for
a∈ Ak. The right action remains untwisted:m[i]· a := ( m· a)[i]. See [Ye5, Section
1] for a detailed study of the shift operation, including an explanation of the sign
that appears in the left action.
We now recall some resolutions of DGA-modules. A DG moduleN is called
acyclicif H(N) = 0. ADG A-module Miscalled K-projective(resp.K-injective),iffor
anyacyclicDG A-module N,theDG Z-module HomA(M, N)(resp. HomA(N, M))
is also acyclic. The DG A-module M is called K-ﬂatif for any acyclic DGAop-
module N, the DGZ-module N⊗A M is acyclic. It is easy to see that K-projective
implies K-ﬂat. More information about the operationsHomA(−,−) and−⊗ A−,
and the various resolutions, see [Ye5, Section 1].
Foracardinalnumber r(possiblyinﬁnite)wedenoteby M⊕r thedirectsumof r
copiesof M. RecallthataDG A-module Pisa freeDGmodule if P∼=
⨁
i∈Z A[−i]⊕ri,
where ri are cardinal numbers. We say thatP is aﬁnite free DG moduleif ∑i ri < ∞
(for some such isomorphism).
Deﬁnition1.12. Let PbeaDG A-module. Asemi-freeﬁltrationof Pisanascending
ﬁltration{νj(P)}j∈Z by DGA-submodules νj(P)⊆ P, such thatν−1(P) = 0, P =⋃
j νj(P), and eachgrν
j (P) := νj(P)/νj−1(P) is a free DGA-module.
Deﬁnition 1.13.Let P be a DGA-module, with semi-free ﬁltration{νj(P)}j∈Z.
(1) The ﬁltration{νj(P)}j∈Z is said to have lengthl if
l = inf{j∈ N| νj(P) = P}∈ N∪{ ∞}.
10 AMNON YEKUTIELI
(2) The ﬁltration{νj(P)}j∈Z is calledpseudo-ﬁniteif each free DGA-module
grν
j (P) is ﬁnite, andlimj→∞ sup(grν
j (P)) =−∞.
(3) The ﬁltration{νj(P)}j∈Z on P is calledﬁniteif it is pseudo-ﬁnite and has
ﬁnite length.
Deﬁnition1.14. ADG A-module Piscalleda semi-free(resp.pseudo-ﬁnitesemi-free,
resp. ﬁnite semi-free) DG moduleif it admits a semi-free (resp. pseudo-ﬁnite semi-
free, resp. ﬁnite semi-free) ﬁltration. Thesemi-free lengthof P is deﬁned to be the
minimum of the lengths of its semi-free ﬁltrations.
Notethatasemi-freeDGmoduleneednotbeboundedabove. If Pisasemi-free
DG module then it is K-projective; see [Ke1, Section 3.1].
Recall that our DG rings are always nonpositive. The next proposition gives
another characterization of pseudo-ﬁnite semi-free DG modules. The graded ring
gotten from A by forgetting the diﬀerential is denoted byA♮. Likewise for DG
modules.
Proposition 1.15. Let P be a DGA-module.
(1) P is pseudo-ﬁnite semi-free iﬀ there arei1 ∈ Z and ri ∈ N, such thatP♮ ∼=⨁
i≤i1 A♮[−i]⊕ri as gradedA♮-modules.
(2) Pisﬁnitesemi-freeiﬀthereisanisomorphismofgraded A♮-modulesasinitem (1)
above, andi0∈ Z, such thatri = 0 for alli < i0.
Proof. Given an isomorphismP♮∼=
⨁
i≤i1 A♮[−i]⊕ri, deﬁne
νj(P) :=
⨁
i1−j≤i≤i1
A[−i]⊕ri⊆ P.
Thisisapseudo-ﬁnitesemi-freeﬁltration,oflength ≤ i1− i0 intheﬁnitecase. The
converse is clear, and so is item (2). □
Deﬁnition 1.16.Let [i0, i1] be an integer interval (possibly unbounded).
(1) Let P be a free gradedA♮-module. We say thatP has abasis concentrated in
[i0, i1] if there is an isomorphism of gradedA♮-modules
P∼=
⨁
i∈[i0,i1]
A♮[−i]⊕ri
for some cardinal numbersri.
(2) A DG A-module M is said to begenerated in the integer interval[i0, i1] if
there is a surjection of gradedA♮-modules P → M♮, where P is a free
graded A♮-module with a basis concentrated in[i0, i1].
Proposition 1.17. Let M be a DGA-module generated in the integer interval[i0, i1].
(1) If N∈ C[j0,j1](Aop), then
N⊗A M∈ C[j0,j1]+[i0,i1](Z) = C[j0+i0,j1+i1](Z).
(2) If N∈ C[j0,j1](A), then
HomA(M, N)∈ C[j0,j1]−[i0,i1](Z) = C[j0−i1,j1−i0](Z).
The easy proof is left to the reader.
Deﬁnition 1.18.Let A be a DG ring.
(1) Aiscalled cohomologicallyleftnoetherian ifthegradedring H(A)isleftnoe-
therian.
(2) A is calledcohomologically left pseudo-noetherianif it satisﬁes these two con-
ditions:
COMMUTATIVE DG RINGS 11
(i) The ring ¯A = H0(A) is left noetherian.
(ii) For everyi the left ¯A-module Hi(A) is ﬁnite (i.e. ﬁnitely generated).
We shall be mostly interested in cohomologically left pseudo-noetherian DG
rings. Of course ifA is cohomologically left noetherian, then it is cohomologically
left pseudo-noetherian. These conditions are equivalent whenA is cohomologi-
cally bounded.
Asusual,byasemi-freeresolutionofaDGmodule Mwemeanaquasi-isomor-
phism P→ M in C(A), where P is semi-free. Likewise we talk about K-injective
resolutions M→ I.
Proposition 1.19. Let M be a DGA-module.
(1) There is a semi-free resolutionP→ M such thatsup(P) = sup(H(M)).
(2) If the DG ringA is cohomologically left pseudo-noetherian, and ifM∈ D−
f (A),
then there is a pseudo-ﬁnite semi-free resolutionP→ M such that sup(P) =
sup(H(M)).
(3) There is a K-injective resolutionM→ I such thatinf(I) = inf(H(M)).
Proof. (1) See [Ke1, Theorem 3.1], [AFH], or [SP, Section 09KK], noting that
sup(A) = 0 (if A is nonzero).
(2) In this case the construction in item (1) can be made with ﬁnitely many basis
elements in each degree. See [Ke1, Theorem 3.1] or [AFH].
(3) See [Ke1, Theorem 3.2], [AFH], or [SP, Section 09KQ]. The point is that any DG
A-module can be embedded in a product of shifts of the DG A-module
HomZ(A, Q/Z). □
Remark1.20. Suppose Aisaring. ADG A-module Pispseudo-ﬁnitesemi-freeiﬀ
itisaboundedabovecomplexofﬁnitefree A-modules. Nowaccordingto[SGA 6]
or[SP,Deﬁnition064Q],aDG A-module Miscalledpseudo-coherentifitisquasi-
isomorphictosomepseudo-ﬁnitesemi-freeDGmodule P. Thisexplainsthechoice
of the name “pseudo-ﬁnite semi-free DG module”.
Thename“pseudo-noetherianDGring”waschosenduetothecloserelationto
pseudo-ﬁnite semi-free resolutions; see Proposition 1.19(2).
