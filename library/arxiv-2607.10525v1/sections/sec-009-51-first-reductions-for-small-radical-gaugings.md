---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-009-51-first-reductions-for-small-radical-gaugings
section_title: "First reductions for small radical gaugings"
section_number: 5.1
pages: 21-33
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
---
scription to the small radical gaugings classified in [GN25]. Table 1, adapted from
[GN25, Table 3], records the non-pointed nondegenerate entries and the conclusions
proved below. We follow the notation and parameter conventions of that reference.
HereD r has order2r; the symbolse,h, andNdenote the elliptic, hyperbolic, and
norm forms, respectively; andp,rare distinct odd primes except in the final row.
Table 1: Non-pointed small radical gaugings from [GN25, Table 3].
FPdim mantleB G generator
action
description fiber functors
4 Iη 1 – Ising no
8 Iη ⊠C(C 2,qη4 ) 1 – Ising⊠pointed no
4r C(Cr,qµ) C2 x7→−x metaplectic no
16 Iη ⊠C(C 2
2,h) 1 – Ising⊠pointed no
16 Iη C2 trivial Ising⊠pointed no
16 C(C4,qξ) C2 x7→−x two Ising factors no
16 C(C2,qi)⊠2 C2 swap two Ising factors no
16 C(C 2
2,e) C2 swap two Ising factors no
16 C(C 2
2,h) C2 swap two Ising factors no
8r C(C2r,qiµ) C2 x7→−x metaplectic no
4r2 Veck Dr – Rep(Dω(Dr)),
ω|Cr̸= 1
no
4r2 C(C 2
r,h) C2 half-turn Rep(Dω(Dr)),
ω|Cr = 1
yes iff[ω] = 0
4r2 C(C 2
r,h) C2 signed swap Z(TY(A,χ,τ)) no
4r2 C(C 2
r,e) C2 half-turn elliptic gauging no
4r2 C(C 2
r,e) C2 signed swap elliptic gauging no
4pr C(Cpr,qζµ) C2 half-turn metaplectic no
4pr C(Cpr,qζµ) C2 mixed signs metaplectic⊠
pointed
no
p2r2,
p|
r−1
C(C 2
r,h) Cp order-p
rotation
Rep(Dω(Cr ⋊Cp)) yes for every
[ω]
22 C. GALINDO, C. GALLEGO, AND Y. MORALES
FPdim mantleB G generator
action
description fiber functors
p2r2,
p|
r+ 1
C(C 2
r,e) Cp order-p
rotation
elliptic prime-cyclic
gauging
no
36 C(C 2
2,e) C3 order-3
rotation
elliptic gauging no
We first exclude the rows whose non-integrality is immediate. If a fusion cate-
gory admits a fiber functor, finite Tannaka–Krein reconstruction identifies it with the
representation category of a semisimple Hopf algebra [EGNO15, Theorem 5.3.12];
hence Frobenius–Perron dimensions of simple objects are ordinary vector-space di-
mensions, and therefore integers. This excludes the rows containing an Ising factor,
the metaplectic rows, and the metaplectic-times-pointed rows.
Lemma 5.7.Let a finite groupGact on a fusion categoryC. If the equivariantization
CG is group-theoretical, thenCis group-theoretical.
Proof.The forgetful tensor functorCG→Cis dominant, and group-theoretical fusion
categories are stable under dominant tensor images [ENO05, Proposition 8.44].□
The same obstruction applies to the rows described as centersZ(TY(A,χ,τ)),
whereA≃C r andris an odd prime. Letmbe the non-invertible simple object of
TY(A,χ,τ). ThenFPdim(m) =
p
|A|= √r. The forgetful tensor functor
Z(TY(A,χ,τ))→TY(A,χ,τ)
is dominant, and tensor functors between fusion categories preserve Frobenius–Perron
dimensions. Hencemappearsasadirectsummandoftheimageofsomesimplecentral
objectZ. Writing the image ofZinTY(A,χ,τ)as a direct sum of invertible objects
and copies ofm, we get
FPdim(Z) =a+b √r
witha,b∈Z ≥0 andb >0. This number is not an integer. ThusZ(TY(A,χ,τ))is
itself non-integral.
Proposition 5.8.LetKbe a finite group. Letω∈Z 3(K,k×), and choose the group-
theoretical presentation
Z(Vecω
K)≃(Vec eω
K×K )∗
M(∆K,eµ),
where∆K⊂K×Kis the diagonal subgroup. Then fiber functors onZ(Vec ω
K)are
parameterized by conjugacy classes of pairs(L,ν), withνunderstood up to multipli-
cation by a2-coboundary, such that:
(1)L⊆K×Kis a subgroup with∆KL=K×K;
(2)ν∈C 2(L,k×)satisfiesdν=eω| L;
(3)the cocycle obtained fromeµν−1 on∆K∩Lis nondegenerate.
In this model the cohomology class ofeωispr∗
1[ω]−pr ∗
2[ω]. In particular, ifLis a
complement to∆K, the last condition is automatic.
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 23
This is the fiber-functor classification for group-theoretical fusion categories [Nik08,
Section 2], applied to Ostrik’s group-theoretical model of the center of a pointed
fusioncategory[Ost03, Theorem3.2, Proposition3.1, Corollary3.1andCorollary3.2].
Changingνby a2-coboundary gives an equivalent module category and does not
affect the nondegeneracy condition.
Forω= 1, the complementK×{e}gives the usual forgetful fiber functor on
Rep(D(K)). For non-trivialω, Proposition 5.8 reduces the question to the restriction
ofeωto subgroups transverse to∆K.
For the dihedral entries, write
Dr =⟨ρ,s|ρ r =s 2 =e, sρs=ρ −1⟩, R=⟨ρ⟩,
withran odd prime. The representatives in [CGR00, Section 6.3, Equation (6.20)]
identifyH 3(Dr,k×)∼= Z/2rZ; denote the class indexed byjby[αj]. Its restriction to
Rhas parameter−jmodr, while its restriction to any reflection subgroupC ∼= C2
is the classjmod 2. Hence the rowω| Cr = 1consists ofj= 0,r, and the other row
consists ofj̸≡0 (modr).
Lemma 5.9.LetG=D r, withran odd prime, and putR=⟨ρ⟩. IfL⊆G×Gis a
subgroup such that∆GL=G×G, then eitherL=G×HorL=H×Gfor some
subgroupH⊆G, or else
L=R×CorL=C×R
for a reflection subgroupC⊆G.
Proof.The condition∆GL=G×Gis equivalent to
G={a −1b|(a,b)∈L}.
LetA= pr 1(L)andB= pr 2(L). ThenAB=G. Sinceris prime, the subgroups
ofGare1,R, the reflection subgroups, andG. Hence either one ofA,BisG, or
{A,B}={R,C}for a reflection subgroupC.
In the second case Goursat’s lemma gives only the direct product, sinceRandC
have no non-trivial common quotient. ThusL=R×CorL=C×R.
Assume now thatA=G. If the quotient appearing in Goursat’s lemma is trivial,
thenL=G×B. Supposethatthisquotientisnon-trivial. Sincethenormalsubgroups
ofGare{e},R, andG, the only non-trivial quotients ofGareG/R ∼=C2 andG. In
the quotientG/R, the relation definingLgivesaR=bRfor every(a,b)∈L. In the
quotientGcase, necessarilyB=Gand the relation is the graph of an automorphism
ofG; every automorphism ofDr preservesRand induces the identity onG/R, whence
againaR=bR. Hencea −1b∈Rfor every(a,b)∈L, contradicting the displayed
equality above. Thus onlyL=G×Bcan occur. The caseB=Gis symmetric.□
Proposition 5.10.LetG=D r, withran odd prime, and letω=α j be one of the
cocycles above. ThenZ(Vecω
G)≃Rep(D ω(G))has a fiber functor if and only ifj= 0.
Proof.Forj= 0this is the ordinary double, and the usual forgetful functor is a fiber
functor.
24 C. GALINDO, C. GALLEGO, AND Y. MORALES
Assumej̸= 0and suppose that a fiber functor exists. By Proposition 5.8, there
is a subgroupL⊆G×Gwith∆GL=G×Gsuch thateω| L is a coboundary. By
Lemma 5.9, eitherL=G×HorL=H×G, orL=R×CorL=C×RwithCa
reflection subgroup.
In the first two cases,LcontainsG×{e}or{e}×G. Since[eω] = pr ∗
1[ω]−pr ∗
2[ω],
the restriction ofeωto one of these subgroups isωorω−1, which is non-trivial because
j̸= 0. This is impossible.
It remains to considerR×CandC×R. Ifj̸≡0 (modr), the restriction ofω
toRis non-trivial; henceeω| L cannot be a coboundary. Ifj≡0 (modr)andj̸= 0,
thenj=r; sinceris odd, the restriction ofωtoC ∼= C2 is the non-trivial class
(−1)ABC. Againeω|L cannot be a coboundary. Thus no non-trivial classjgives a
fiber functor.□
Lemma 5.11.LetBbe a nondegenerate braided fusion category, and let
E=
M
g∈G
Eg
be a faithfully graded braidedG-crossed extension ofB. WriteTg∈Aut br
⊗ (B)for the
crossed action ofg. Let
Φ : BrPic(B)
≃
−−→EqBr(Z(B))
be the canonical equivalence and let
ι:B⊠B rev ≃
−−→Z(B)
be the braided equivalence determined by the braiding ofB. Then the invertibleB-
bimodule categoryEg satisfies
(10)ι −1Φ([Eg])ι≃id B ⊠Tg.
Proof.By [ENO10, Theorem 7.12], the braidedG-crossed structure determines a
morphism of categorical2-groups
G−→Pic(B), g7−→[E g].
Recall that the alpha-induction homomorphism
∂: Pic(B)−→Aut br
⊗ (B)
is characterized byα−
M◦∂M≃α +
M for every invertibleB-module categoryM[ENO10,
Section 5.4]. ForX∈E g andY∈B, the composite of crossed braidings
Y⊗X
cY,X
− −−− →X⊗Y
cX,Y
−−−−→Tg(Y)⊗X
is a module-natural isomorphismα+
Eg(Y)≃α −
Eg(Tg(Y)); the crossed hexagon identities
give the module-functor compatibility. Hence
∂Eg =T g.
Equivalently, thisistherelationbetweenthecategorical2-groupmorphismin[ENO10,
Theorem 7.12] and the structural map of the Picard crossed module.
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 25
Under the Brauer–Picard equivalence, the image ofPic(B)consists of the braided
autoequivalences ofZ(B)that are trivializable on the first copy ofB, while the restric-
tion to the second copyBrev is the map∂; see [DN13, Lemma 4.4 and Corollary 4.9].
SinceBis nondegenerate, the inverse construction in [ENO10, Theorem 5.2] sends a
braided autoequivalenceTofBto the bimodule category whose center autoequiva-
lence isidB ⊠T. TakingT=T g proves (10).
Finally, in the extension classification of [ENO10, Theorems 1.3 and 8.9], the ho-
momorphism
c:G−→BrPic(B), c(g) = [E g],
is fixed before the finalH3(G,k×)-parameter is chosen. The latter changes the asso-
ciativity coherence but not the classes of the homogeneous components. This is also
the convention in [GPR24, Definition 2.1], where the crossed action is fixed first and
the parameterαlabels the remainingH 3-choices.□
Lemma 5.12.LetAbe a finite abelian group of odd order, letB=C(A,q), and let
E=
M
g∈G
Eg
be a braidedG-crossed extension ofB. Fixg∈G, and letθ∈O(A,q)be the auto-
morphism induced byg∗ onA= Inv(B). Then, for every simple objectX∈E g, the
following hold:
(1)Aacts transitively onIrr(E g)by left tensor product.
(2)The stabilizer ofXis
StA(X) :={a∈A|a⊗X≃X}= (1−θ)A.
(3)The assignment
a+ (1−θ)A7−→a⊗X
defines a bijection
A/(1−θ)A
≃
−−→Irr(Eg).
In particular,
# Irr(Eg) =|ker(1−θ)|.
(4)The Frobenius–Perron dimension ofXis
FPdim(X) =
p
|(1−θ)A|.
Proof.By [ENO10, Theorem 6.1],E g is an invertible, hence indecomposable,B-
module category. Since the simple objects ofBare the elements ofA, tensoring
by them permutesIrr(Eg). EachA-orbit spans aB-module direct summand, so inde-
composability implies that this action is transitive.
The crossed braiding gives, fora∈AandX∈E g, isomorphisms
a⊗X
ca,X
−−−→X⊗a
cX,a
−−−→θ(a)⊗X.
Tensoring on the left byθ(a)−1 shows that(a−θ(a))⊗X≃X. Hence
(1−θ)A⊆St A(X).
26 C. GALINDO, C. GALLEGO, AND Y. MORALES
It remains to compute the number of simple objects. Write
bq(a,b) =q(a+b)q(a) −1q(b)−1
for the symmetric bicharacter associated withq. Since|A|is odd, doubling is an
automorphism ofA; put
c(a,b) :=b q(a/2,b).
Thencis a nondegenerate symmetric bicharacter,c(a,a) =q(a), andθpreservesc.
Thus we may use the braided model in which the underlying fusion category ofBis
VecA and the braiding isc. Usecto identifybAwithA. Under the braided equivalence
B⊠B rev≃Z(Vec A),(x,y)7−→
 
x+y,c(x−y,−)

,
the autoequivalenceidB ⊠Tθ is represented onA⊕ bA≃A⊕Aby
gθ = 1
2

1 +θ1−θ
1−θ1 +θ

,
where 1
2 denotes the inverse of doubling onA. Indeed, the coordinates(u,v) =
(x+y,x−y)are sent to(x+θ(y),x−θ(y)). By Lemma 5.11, the invertibleVec A-
bimodule category underlyingEg is the one represented byidB ⊠Tθ, and hence bygθ
in these coordinates. IfP:A⊕ bA→Ais the first projection, then
P gθ(0,v) = 1
2(1−θ)v.
Therefore [ENO10, Proposition 10.8] gives
# Irr(Eg) =

ker(Pg θ| bA)

 =|ker(1−θ)|=|A/(1−θ)A|.
Transitivity now yields
|A: St A(X)|=|ker(1−θ)|,
so
|StA(X)|= |A|
|ker(1−θ)| =|(1−θ)A|.
Together with the inclusion above, this provesStA(X) = (1−θ)Aand the asserted
parametrization of simple objects.
Finally, putI= (1−θ)A. Fora∈A, rigidity gives
HomB(a,X⊗X ∗)≃Hom Eg(a⊗X,X).
SinceXis simple, the latter space is one-dimensional fora∈Iand zero fora /∈I.
Therefore
X⊗X ∗≃
M
a∈I
a,
and hence
FPdim(X)2 =|I|=|(1−θ)A|.
□
Proposition 5.13.LetA=C 2
r, withran odd prime. The two rows of Table 1 with
mantleC(A,e)andG=C 2 admit no fiber functor.
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 27
Proof.We identifyAwith a two-dimensional vector space overF r and letθbe the
involution defining the action. Lemma 5.12 applies to the non-trivial homogeneous
component.
Ifθis one of the non-central involutions in the row(x,y)7→(±y,±x), then1−θ
has rank one overFr; hence(1−θ)Ahas orderr. The defect sector contains simple
objects of Frobenius–Perron dimension√r. A simple object in the equivariantiza-
tion lying over such a defect has dimension[C 2 : St C2(X)] dim(π)√r, whereπis
the corresponding irreducible projective representation of the stabilizer; this is the
orbit–stabilizer construction for simple equivariant objects recalled in [GP17, Subsec-
tion 7.5.1]. Thus its dimension is a positive integer multiple of√r, and the integrality
obstruction excludes this row.
It remains to consider the half-turnθ=−id A. In this case(1−θ)A=A, so
the non-trivial component has a unique simple objectmof dimensionr. Since the
grading group has order two,m∗ lies in the same component and hencem∗≃m.
Also, everya∈Afixesm. Frobenius reciprocity therefore gives
[m⊗m ∗ :a] = dim Hom(a⊗m,m) = 1 (a∈A).
Thus
m⊗m≃
M
a∈A
a,
so the crossed extension has the Tambara–Yamagami fusion rules and is a category
TY(A,χ,τ). Since the row has elliptic metric groupC(A,e), the associated symmetric
form has no Lagrangian; equivalently, the bilinear formχin this Tambara–Yamagami
category is elliptic. We apply Theorem 3.6 to the equivariantization by the induced
actionT−id A.
The subgroupH={e}would give a fiber functor onTY(A,χ,τ)itself, which is im-
possible by Tambara’s criterion [Tam00, Propositions 4.1 and 4.2], sinceχis elliptic.
Thus a fiber functor would have to come fromH=C2. SinceH 2(C2,k×) = 0, Corol-
lary 3.7 forces an equivariant rank-twoTY(A,χ,τ)-module category, indecomposable
as aTY(A,χ,τ)-module category, on which the non-trivial element acts freely on the
two simple objects.
To exclude this case, use the classification of module categories over Tambara–
Yamagami categories [MM12, Section 9]. In the form used in [Nik08, Lemma 4.3 and
Remark 4.5], such a module category restricts toVecA as
M(A,µ)⊕M(A,µ ′),
whereM(A,µ)is the pointedVec A-module category attached toµ,[µ]̸= 0in
H2(A,k×), andµ′ is determined byχandµ. By [MM12, Lemma 9.1], theσ-translate
ofM(H,ψ)isM(R ⊥,eψ), whereR= Rad(ψ),ξ ψ is the alternating bicharacter asso-
ciated withψ, and eψ(a,b) =ψ(t b,ta)for elementst a satisfyingξ ψ(ta,−) =χ(a,−).
Specializing this formula toH=AandR={0}, and writing the alternating form
Alt(µ)asλJandχas a symmetric matrixS, gives the matrix formula used in [Nik08,
28 C. GALINDO, C. GALLEGO, AND Y. MORALES
Remark 4.5]:
Alt(µ′) =−det(S)
λ J.
Since cohomology classes inH 2(A,k×)are determined by their alternating forms,
[µ] = [µ′]would implyλ 2 =−det(S). ThusM(A,µ)andM(A,µ ′)are equivalent
only if−det(S)is a square inF r, which is exactly the condition thatχbe hyperbolic
overF r. Sinceχis elliptic, the twoVec A-summands are not equivalent.
The automorphism−id A acts trivially onH2(A,k×). If aC2-equivariant structure
on the rank-two module category acted freely on simple objects, the corresponding
module equivalence
U:M→M T−id A
would interchange the two simple objects. After restriction toVecA, this would force
an equivalenceM(A,µ)≃M(A,µ ′), contradicting the preceding paragraph. Hence
no such equivariant structure can act transitively on the two simple objects. This
contradicts Corollary 3.7, and the half-turn row with elliptic mantle has no fiber
functor.□
Proposition 5.14.Letp,rbe odd primes withp|r−1, and let
K=⟨x,y|x r =y p =e, yxy−1 =x a⟩
whereahas orderpinF ×
r . ThenZ(Vec ω
K)≃Rep(D ω(K))admits a fiber functor for
everyω∈Z 3(K,k×).
Proof.LetR=⟨x⟩and letπ:K→P=K/R≃C p be the quotient map. Consider
the Lyndon–Hochschild–Serre spectral sequence
Es,t
2 =H s(P,H t(R,k×))⇒H s+t(K,k×).
Since|R|and|P|are coprime, andH t(R,k×)is finiter-primary fort>0, the mixed
termsE s,t
2 withs,t >0vanish. MoreoverE 0,3
2 =H 3(R,k×)P = 0, becausePacts
onH 3(R,k×)≃F r by multiplication bya2̸= 1. Hence the only contribution in total
degree3isE 3,0
2 =H 3(P,k×), and inflation gives
H3(K,k×)≃π ∗H3(P,k×).
Thus, after changingωwithin its cohomology class, which does not change the
monoidal equivalence class ofVecω
K, we may assumeω=π∗ηfor someη∈Z 3(P,k×).
Choose the subgroup⟨y⟩⊂Kas a section ofP, and letι:P→Pbe inversion.
Putf:K→Kfor the homomorphism obtained by composingπ,ι, and this section,
and set
L={(k,f(k))|k∈K}⊂K×K.
ThenLis a subgroup of order|K|. If(k,f(k))lies in∆K, thenk=f(k)belongs to
⟨y⟩and its image inPis fixed by inversion. Sincepis odd, this forcesk=e. Hence
L∩∆K={e}, and therefore∆KL=K×K.
By Proposition 5.8, it remains only to check thateω|L is cohomologically trivial. In
cohomology,
[eω]|L = (π◦pr 1|L)∗[η]−(π◦pr 2|L)∗[η] =π ∗[η]−(ι◦π) ∗[η].
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 29
The inversion automorphism ofP≃C p acts trivially onH3(P,k×): under the identi-
ficationH 3(P,k×)≃H 4(P,Z), inversion acts by multiplication by(−1)2 = 1. Hence
the displayed class vanishes; therefore there is a 2-cochainνonLwithdν=eω| L.
SinceL∩∆K={e}, the nondegeneracy condition in Proposition 5.8 is automatic.
Thus(L,ν)gives a fiber functor.□
Proposition 5.15.Letp,qbe odd primes withp|q+ 1. LetA=F q2, viewed as
a two-dimensional vector space overF q, and letN:A→F q be the norm form,
viewed through a fixed non-trivial additive character as ak×-valued quadratic form.
Forc∈ker(N)of orderpandα∈H 3(Cp,k×), let
Eα = Vecp,α
(A,N)
be the correspondingCp-crossed extension ofC(A,N). Then the gauging
Dα = (Eα)Cp
admits no fiber functor.
Proof.The fusion rules ofEα are recalled in [GPR24, Proposition 4.1]. Its trivial com-
ponent is the pointed categoryVecA, and the non-trivial homogeneous components
contain one simple object each. We write these non-invertible simples asXi,i∈C ×
p ,
with
a⊗X i =X i⊗a=X i, X i⊗Xj =



qXi+j, i+j̸= 0,M
a∈A
a, i+j= 0.
Lemma 5.7 shows that ifDα were group-theoretical, then its de-equivariantizationEα
would be group-theoretical. Thus the non-group-theoreticality ofDα already follows
from [GPR24, Theorem 4.4]. The fiber-functor assertion is stronger: non-group-
theoretical Hopf representation categories can still admit fiber functors. We therefore
apply Corollary 5.5.
First suppose that the subgroupHin Corollary 5.5 is trivial. Then a fiber functor
onD α would come from a fiber functor onEα. By reconstruction, this would giveEα≃
Rep(H0)for a semisimple Hopf algebraH0 of dimensionpq2. By [JL09, Corollary 1.2],
all semisimple Hopf algebras of dimensionpq2 have group-theoretical representation
categories. This contradicts [GPR24, Theorem 4.4], where these elliptic categoriesEα
are shown to be non-group-theoretical.
It remains to exclude the caseH=C p. In the subcaseS=C p of Corollary 5.5,
the Clifford datum has anE α-module category eNwhose restriction toVec A is an
indecomposable module categoryN. The number of simple objects is intrinsic to the
underlying abelian category; hence# Irr( eN) = # Irr(N). By the pointed module-
category classification [Nik08, Section 2], suchVecA-module categories are indexed by
pairs(L,[µ]), whereL⊆Aand[µ]∈H 2(L,k×), and have rank[A:L]. Hence their
ranks are1,q, orq 2, neverp. Thus this subcase cannot produce a rank-pmodule
category.
30 C. GALINDO, C. GALLEGO, AND Y. MORALES
Consider now the subcaseS={e}, and suppose that it produces a fiber functor.
Put
M=E α ⊠VecAN,M t :=E α,t ⊠VecAN(t∈C p),
whereE α,t denotes the homogeneous component of degreet. By Corollary 5.5,Mhas
rankp. ThepsubcategoriesM t arenon-zeroindecomposableVec A-modulecategories,
so each one has rank one. Letmt be the unique simple object ofMt; in particular,
M0 =Nand its unique simple object ism 0.
Let
U:M−→M τ
be the module equivalence attached to a generatorτ∈C p, and writeU(m 0)≃m s.
RestrictingUtoN=M 0 and using the conventionX⊗τM=ρ τ(X)⊗Mgives an
equivalence ofVecA-module categories
(11)N τ−1
≃M s≃E α,s ⊠VecAN.
Indeed, the module-functor constraint forUreads
U(a⊗M)≃ρ τ(a)⊗U(M), a∈A,
which is preciselyVecA-linearity after twisting the source byτ−1.
By the classification of indecomposable module categories overVecA, the rank-one
categoryNis determined by a class[µ]∈H 2(A,k×). The restriction ofρ τ toA
is multiplication byc[GPR24, Definition 3.1 and the proof of Proposition 4.2], so
twisting byτ−1 pulls this class back along multiplication byc−1. Sincek× is divisible,
H2(A,k×)≃Hom(∧ 2A,k×),
and multiplication bycacts on∧ 2Aby
det
Fq
(c) =N(c) = 1.
ThereforeN τ−1
≃N, and (11) yields
Eα,s ⊠VecAN≃N.
Ifs̸= 0, thensgeneratesC p. Iterating the relative tensor product and using the
gradedmultiplicationequivalencesshowsthatthesameequivalenceholdsforeveryho-
mogeneous component. Moreover, becauseAis abelian, every rank-oneVecA-module
category is pointed. Indeed, a simpleVecA-module endofunctor has the identity as its
underlying functor, and its module structure is a character ofA; hence the simple ob-
jects of the dual category are indexed bybAand are invertible. The group-theoretical
criterion [MM12, Theorem 16] would then imply thatEα is group-theoretical, contra-
dicting [GPR24, Theorem 4.4]. Hences= 0andU(m 0)≃m 0.
Finally, for eachi∈C ×
p , the non-zero objectX i⊗m0 belongs to the rank-one
componentM i. Thus
Xi⊗m0≃n imi
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 31
for some integerni >0. The crossed action preserves the grading and the non-trivial
component of degreeihas the unique simple objectX i, soρ τ(Xi)≃X i. Applying
the module-functor constraint gives
niU(mi)≃U(X i⊗m0)≃ρ τ(Xi)⊗U(m 0)≃X i⊗m0≃n imi.
Semisimplicity impliesU(m i)≃m i for everyi. Hence the generator fixes all simple
objects ofMand cannot act as ap-cycle. This rules out the last subcase and proves
the proposition.□
Lemma 5.16.LetA=F 4 and letN:A→F 2 be the norm form, composed with the
non-trivial additive character ofF2. For everyα∈H 3(C3,k×), the crossed extension
Eα = Vec3,α
(A,N)
is non-group-theoretical.
Proof.Writeq(a) = (−1) N(a) andB=C(A,q), so that the underlying fusion category
ofBisVec A. Thus
q(0) = 1, q(a) =−1 (a̸= 0).
LetT c be the braided autoequivalence induced by multiplication by an elementc∈F×
4
of order three. By [GPR24, Definition 2.1 and Example 3.3(1)], the categoryEα is
the braidedC 3-crossed extension whose crossed action is generated byTc. There is
no additionalH 2-choice here: multiplication by3is an automorphism of the2-group
A, soH 2(C3,A) = 0for this action.
By Lemma 5.11, under the braided equivalence
ι:B⊠B rev ≃
−−→Z(VecA),
the Brauer–Picard class of the degree-one component satisfies
(12)ι −1Φ([Eα,1])ι≃id B ⊠Tc.
This formula is independent ofα: the parameterαchanges the final associativity co-
herence of the extension, but not the homomorphismC3→BrPic(VecA)represented
by its homogeneous components.
The group-theoretical criterion for graded extensions [MM12, Theorem 16 and Re-
mark 17] now says thatEα is group-theoretical if and only if a Lagrangian subcategory
ofZ(Vec A)is stable under the autoequivalence in (12).
The metric group ofB⊠B rev isA⊕Awith quadratic form
Q(x,y) =q(x)q(y) −1.
A Lagrangian subgroupL⊆A⊕Ahas order four and satisfiesQ| L = 1. If(x,0)∈L
withx̸= 0, thenQ(x,0) =−1, a contradiction; similarly,Lcontains no non-zero
element of the form(0,y). Hence both coordinate projectionsL→Aare injective.
Since|L|=|A|, there is an automorphismf∈Aut(A)such that
L= Γ f :={(x,f(x)) :x∈A}.
Conversely, every such graph is Lagrangian, becauseqtakes the same value on every
non-zero element ofA.
32 C. GALINDO, C. GALLEGO, AND Y. MORALES
IfΓ f were invariant underidA⊕Tc, then
(x,cf(x))∈Γ f (x∈A).
Comparison of the first coordinates givescf(x) =f(x)for allx. Sincefis surjective,
this would forcec= 1, contrary to the choice ofc. Thus no Lagrangian subcategory is
C3-stable, and the criterion cited above proves thatEα is non-group-theoretical.□
Proposition 5.17.LetA=F 4, viewed as an additive group, and letN:A→F 2 be
the norm form, viewed through a fixed non-trivial additive character as ak×-valued
quadratic form. For everyα∈H 3(C3,k×), the dimension36gauging
Dα =

Vec3,α
(A,N)
C3
admits no fiber functor.
Proof.PutE α = Vec3,α
(A,N). We examine the alternatives in Corollary 5.5.
First suppose thatH=C 3. IfS=C 3, the Clifford datum contains anE α-
module category eNwhose restriction toVec A is an indecomposable module category
N. These categories have the same underlying abelian category and therefore the
same rank. Indecomposable module categories overVecA are parameterized by pairs
(L,[µ]), whereL⊆Aand[µ]∈H 2(L,k×), and their rank is[A:L][Nik08, Sec-
tion 2]. SinceA≃C 2
2, the possible ranks are1,2, and4, never3. Hence this subcase
is impossible.
Assume next thatS={e}. Then
M=E α ⊠VecAN=
M
t∈C3
Mt,M t =E α,t ⊠VecAN.
If this datum produced a fiber functor, Corollary 5.5 would force everyMt to have
rank one. In particular,N=M 0 has rank one. Such module categories are parame-
terized by
H2(A,k×)≃Hom(∧ 2A,k×)≃C 2,
where the first isomorphism uses the divisibility ofk×. Thus there are exactly two
equivalence classes of rank-oneVecA-module categories.
The homogeneous components ofEα act on equivalence classes of indecomposable
VecA-module categories by
[N]7−→[E α,t ⊠VecAN].
The three classes[Mt]form theC 3-orbit of[N], and all of them have rank one. This
orbit is therefore contained in a set of two elements. Since aC3-orbit has cardinality
one or three, the orbit must have cardinality one. Consequently,
Eα,t ⊠VecAN≃N(t∈C 3),
soNisC 3-stable.
Moreover, every rank-oneVecA-module category is pointed. Indeed, its underlying
semisimple category has one simple object, and its simpleVecA-module endofunctors
are indexed by the characters ofA; all of them are invertible. The criterion [MM12,
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 33
Theorem 16] would therefore makeEα group-theoretical, contradicting Lemma 5.16.
Thus the subcaseS={e}is also impossible.
It remains to considerH={e}. Corollary 5.5 then requires a fiber functor onEα
itself. By reconstruction, this would give a semisimple Hopf algebraH1 of dimension
12withE α ≃Rep(H 1). Every semisimple Hopf algebra of dimensionpq 2, and in
particular of dimension3·2 2, has a group-theoretical representation category [JL09,
Corollary 1.2]. This again contradicts Lemma 5.16. ThereforeD α admits no fiber
functor.□
Corollary 5.18.Among the non-pointed nondegenerate braided fusion categories in
Table 1, the categories admitting a realization asRep(H)for a finite-dimensional
semisimple factorizable Hopf algebraHare exactly:
(1)the ordinary dihedral doublesRep(D(Dr));
(2)the hyperbolic prime-cyclic twisted doublesRep(Dω(Cr ⋊Cp)), withp|r−1,
for every[ω]∈H 3(Cr ⋊Cp,k×).
All other non-pointed entries in the table admit no fiber functor.
Proof.The fiber-functor conclusions are assembled in Table 1 from the integrality
obstruction and Propositions 5.10, 5.13, 5.14, 5.15, and 5.17. Finite Tannaka–Krein
reconstruction turns fiber functors into semisimple Hopf realizations [EGNO15, The-
orem 5.3.12]; for a nondegenerate braided representation category, the corresponding
quasitriangular Hopf algebra is factorizable [Kas95, Chapter VIII].□
