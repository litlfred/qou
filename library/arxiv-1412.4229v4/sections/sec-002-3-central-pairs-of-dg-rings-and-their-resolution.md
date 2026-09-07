---
doc_id: arxiv-1412.4229v4
doc_title: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI"
section_id: sec-002-3-central-pairs-of-dg-rings-and-their-resolution
section_title: "Central Pairs of DG Rings and their Resolutions"
section_number: 3
pages: 16-23
source_pdf: 1412.4229v4.pdf
source_sha256: 248d6a1e28a76a94
doc_brief: "THE SQUARING OPERATION FOR COMMUTATIVE DG RINGS AMNON YEKUTIELI — Let A → B be a homomorphism of commutative rings."
---
In this section we introduce several special kinds of DG rings and homomor-
phisms. Recall that DGR is the category of DG rings.
Deﬁnition 3.1.A DG ringA = ⨁
i∈ZAi is called nonpositive if Ai = 0 for all
i >0. The full subcategory ofDGR consisting of nonpositive DG rings is denoted
by DGR≤0.
Deﬁnition 3.2.A DG ring A = ⨁
i∈ZAi is called strongly commutative if it
satisﬁes these two conditions:
(i) A is weakly commutative (Deﬁnition 1.6(2)), namelyb·a = (−1)ij·a·b for
all a∈Ai and b∈Aj.
(ii) a·a = 0 for alla∈Ai and i odd.
We denote byDGRsc the full subcategory ofDGR on the strongly commutative DG
rings.
THE SQUARING OPERATION 17
Deﬁnition 3.3.A DG ringA is called acommutative DG ringif it is both non-
positive and strongly commutative. The full subcategory of DGR consisting of
commutative DG rings is denoted byDGR≤0
sc .
In other words,
DGR≤0
sc = DGR≤0∩DGRsc.
Example 3.4. A commutative DG ringA concentrated in degree0 (i.e. A =A0)
is just a commutative ring.
Remark 3.5.The name “strongly commutative DG ring” was suggested to us by J.
Palmieri. In an earlier version of this paper we used the name “strictly commutative
DG ring”, following [ML]; and in [YZ2] it was “super-commutative DG algebra”.
The name “weakly commutative DG ring” is “commutative DG algebra” in [ML],
and “graded-commutative DG algebra” in [AILN].
Of course when the number2 is invertible inA0 (e.g. ifA0 contains Q), then
condition (i) of Deﬁnition 3.2 implies condition (ii), so that the distinction between
weak and strong commutativity disappears. See also Remark 3.14.
Central homomorphisms were introduced in Deﬁnition 1.6(3).
Deﬁnition 3.6.A central pair of DG ringsis a central homomorphismu :A→B
in DGR, where the DG ringA is commutative. We usually denote this pair byB/A,
keepingu implicit.
Suppose A
u
− →B and A′u′
−→B′are central pairs of DG rings. Amorphism of
central pairsw/v : B′/A′→B/A consists of homomorphisms v : A′→A and
w :B′→B in DGR, such thatu◦v =w◦u′. The resulting category is called the
category of central pairs of DG rings, and is denoted byPDGR.
A morphismw/v in PDGR is shown in diagram (0.2.1). We do not require the
homomorphism w : B′→B to be central. The homomorphism v : A′→A is
automatically central, becauseA is commutative.
Deﬁnition 3.7.
(1) A nonpositive central pairis a central pairB/A such that bothA and B
are nonpositive DG rings. The full subcategory of nonpositive central pairs
is denoted byPDGR≤0.
(2) A commutative central pairis a central pairB/A such that the DG ringB
is also commutative. The full subcategory of commutative central pairs is
denoted by PDGR≤0
sc .
(3) A morphismw/v : B′/A′→B/A in PDGR is called central if the homo-
morphism w :B′→B is central. The subcategory ofPDGR on all objects,
but only with central homomorphisms, is denoted byPDGR⃗ce.
(4) A morphismw/v : B′/A′→B/A in PDGR is called aquasi-isomorphism
if the homomorphisms v : A′→A and w : B′→B are both quasi-
isomorphisms.
Deﬁnition 3.8.Let B/A be a central pair of DG rings. Aresolution of B/A is a
morphism s/r : ˜B/ ˜A→B/A in PDGR, such that:
•r : ˜A→A is a quasi-isomorphism.
•s : ˜B→B is a surjective quasi-isomorphism.
The resolution is calledstrict if ˜A =A and r = idA, the identity automorphism
of A.
See diagram (0.2.2) for an illustration.
18 AMNON YEKUTIELI
Deﬁnition 3.9.Letw/v :B′/A′→B/Abe a morphism inPDGR, lets/r : ˜B/ ˜A→
B/A be a resolution ofB/A, and lets′/r′: ˜B′/ ˜A′→B′/A′be a resolution ofB′/A′.
A morphism ˜w/˜v : ˜B′/ ˜A′→˜B/ ˜A in PDGR is said to bemorphism of resolutions
abovew/v if
(w/v)◦(s′/r′) = (s/r)◦( ˜w/˜v)
in PDGR. In this case, we also say that˜w/˜v is aresolution ofw/v.
IfB′/A′=B/A andw/v is the identity automorphism, then we say that˜w/˜v is
a morphism of resolutions ofB/A.
A morphism ˜w/˜v is shown in diagram (0.2.3).
By graded setwe mean a setX with a partitionX =∐
i∈ZXi; the elements of
Xi are said to have degreei. We say thatX is anonpositive graded setif Xi = ∅
for alli >0. A ﬁltered graded setis a graded setX, with an ascending ﬁltration
F ={Fj(X)}j∈Z by graded subsets, such thatX =⋃
jFj(X) and F−1(X) = ∅.
LetAbeaDGring. Wedenoteby A♮thegradedringgottenfrom Abyforgetting
the diﬀerential. The same for DG modules. When talking about free modules, we
assume the DG ringA is nonzero (to avoid nonsense).
For a variablex of degreei, we letA⊗x := A[−i], the shift by−i of the DG
A-module A. For any element a∈Aj we denote bya⊗x or a·x the element
t−i(a)∈A[−i]j+i; cf. (1.18). Note that d(x) = 0, and d(a·x) = d(a)·x for any
a∈A. Now consider a graded set of variablesX. The free DGA-module onX is
A⊗X :=
⨁
x∈X
A⊗x.
A free DGA-module is a DGA-module P that is isomorphic toA⊗X for some
graded set of variablesX. The image ofX in P is called abasis of P.
Let P be a DGA-module. A semi-free ﬁltrationon P is an ascending ﬁltration
F ={Fj(P )}j∈Z of P by DG submodules, such thatP =⋃
jFj(P ), F−1(P ) = 0,
and each grF
j (P ) := Fj(P )/Fj−1(P ) is a free DGA-module. We say thatP is a
semi-free DGA-module if it admits some semi-free ﬁltration. See [AFH] and [Hi].
A semi-free DG module is K-projective, and hence also K-ﬂat.
Let P be a semi-free DGA-module, with semi-free ﬁltrationF. For eachj≥0
choose a graded subsetYj⊆Fj(P ) whose image ¯Yj in grF
j (P ) is a basis of this free
DG A-module. The graded set X := ∐
i∈Z Yj is ﬁltered byFj(X) := ⋃
j′≤jYj′.
Such a ﬁltered graded set is called asemi-basis ofP. Note that for everyj there is
an isomorphism of gradedA♮-modules A♮⊗Fj(X)∼=Fj(P )♮; and soA♮⊗X∼=P♮.
For any elementy∈Yj, its image ¯y∈¯Yj⊆grF
j (P ) satisﬁesd(¯y) = 0; and hence
d(y)∈Fj−1(X). We see thatd(Fj(X))⊆Fj−1(X).
Given a graded set of variablesX, we can form the noncommutative polynomial
ring Z⟨X⟩over Z, which is the freeZ-module on the set of monomialsx1···xm in
the elements ofX, and with the obvious multiplication and grading.
The next deﬁnition is not standard. Its ﬁrst occurrence seems to have been in
[YZ2].
Deﬁnition 3.10.Let X = ∐
i∈ZXi be a graded set of variables. The strongly
commutative polynomial ringZ[X] is the quotient ofZ⟨X⟩by the two-sided ideal
generated by the elementsy·x−(−1)ij·x·y and z2, for allx∈Xi, y∈Xj and
z∈Xk, withi,j,k ∈Z and k odd.
Deﬁnition 3.11.Consider a nonpositive central pair of DG ringsA
u
− →B.
(1) We say thatB is a commutative semi-free DG ring overA, that u is a
commutative semi-free DG ring homomorphism, and thatB/A is a com-
mutative semi-free pair of DG rings, if there is an isomorphism of graded
THE SQUARING OPERATION 19
A♮-rings B♮∼=A♮⊗Z Z[X], whereX is a nonpositive graded set, andZ[X]
is the strongly commutative polynomial ring. Such a graded setX is called
a set of commutative semi-free ring generatorsof B overA.
(2) We say thatB is a noncommutative semi-free DG ring overA, thatu is
a noncommutative semi-free DG ring homomorphism, and thatB/A is a
noncommutative semi-free pair of DG rings, if there is an isomorphism of
graded A♮-rings B♮∼= A♮⊗Z Z⟨X⟩, whereX is a nonpositive graded set,
and Z⟨X⟩is the noncommutative polynomial ring. Such a graded setX is
called aset of noncommutative semi-free ring generatorsof B overA.
(3) We say thatB is a K-ﬂat DG ring overA, that u is a K-ﬂat DG ring
homomorphism, and thatB/A is aK-ﬂat pair of DG rings, ifB is K-ﬂat
as a DGA-module (left or right – it does not matter).
Proposition 3.12. Let u : A→B a nonpositive central pair of DG rings, which
is either commutative semi-free or a noncommutative semi-free. Thenu : A→B
is K-ﬂat.
Proof. In the noncommutative case, letX be a set of noncommutative semi-free
ring generators ofB overA. Then the monomialsx1···xm, withx1,...,xm∈X,
are a semi-basis for the DGA-module B. We are using the fact that the graded
set X is nonpositive.
In the commutative case, letX be a set of commutative semi-free ring generators
of B overA. Choose some ordering of the setX. Then the monomialsx1···xm,
with x1≤···≤xm in X, andxi < xi+1 if xi is odd, are a semi-basis for the DG
A-module B. Again, we are using the fact that the graded setX is nonpositive.
We see that in both casesB is a semi-free DGA-module, and thus it is K-ﬂat.□
Example 3.13. Let A be a commutative ring, and let a = (a1,...,an) be a
sequence of elements inA. The Koszul complexB := K(A;a) associated to this
sequence is a commutative semi-free DG ring overA. It has a set of commutative
semi-free ring generatorsX ={x1,...,xn}of degree−1, such thatdB(xi) =ai.
Remark 3.14. The strongly commutative polynomial ringZ[X] is a free graded
Z-module. This is what makes Proposition 3.12 work.
The “weakly commutative polynomial ring”, which is the quotient ofZ⟨X⟩by
the two-sided ideal generated by the elementsy·x−(−1)ij·x·y for allx∈Xi and
y∈Xj, is not ﬂat overZ. Indeed, for any odd elementz∈X we havez2⁄= 0 but
2·z2 = 0.
Deﬁnition 3.15.LetB/A be a central pair of DG rings, and lets/r : ˜B/ ˜A→B/A
be a resolution ofB/A (Deﬁnition 3.8).
(1) Assume B/A is a commutative pair. We say that˜B/ ˜A is a commutative
semi-free resolutionofB/A if the pair ˜B/ ˜A is commutative semi-free (Def-
inition 3.11(1)).
(2) We say that ˜B/ ˜A is a noncommutative semi-free resolutionof B/A if the
pair ˜B/ ˜A is noncommutative semi-free (Deﬁnition 3.11(2)).
(3) We say that ˜B/ ˜A is a K-ﬂat resolutionof B/A if the pair ˜B/ ˜A is K-ﬂat
(Deﬁnition 3.11(3)).
Example 3.16.IfB is K-ﬂat overA, thenB/A is a K-ﬂat ring resolution of itself.
It is terminal among all K-ﬂat ring resolutions ofB/A.
Example 3.17. Let u : A→B be a surjective homomorphism of commutative
rings, and leta = (a1,...,an) be a sequence of elements ofA that generates the
ideal Ker(u). Assume that the sequencea is regular. Deﬁne ˜B := K(A;a), the
Koszul complex. Then ˜B/A is a strict commutative semi-free DG ring resolution
of B/A.
20 AMNON YEKUTIELI
Remark 3.18. In [YZ2] we did not require the quasi-isomorphismw to be surjec-
tive. That omission was not signiﬁcant there, because we were mostly concerned
with the case whenB is a ring (cf. [YZ2, Proposition 1.8]). WhenB has nonzero
negative components, the surjectivity is needed (cf. proof of Theorem 3.21 below).
The next results in this section are enhanced versions of [YZ2, Propositions 1.7
and 1.8]. The categoryDGR≤0/ceA was introduced in Deﬁnition 1.6(4).
Lemma 3.19. Let A be a commutative DG ring, and letB,B′∈DGR≤0/ceA.
Assume either of these two conditions holds:
(i) B is commutative, andB′is commutative semi-free overA, with commu-
tative semi-free ring generating setX.
(ii) B′is noncommutative semi-free overA, with noncommutative semi-free
ring generating setX.
Letw :X→B be a degree0 function. Then:
(1) The function w extends uniquely to a gradedA♮-ring homomorphism w :
B′♮→B♮.
(2) The graded ring homomorphismw :B′♮→B♮extends to a DG ring homo-
morphism w :B′→B iﬀd(w(x)) =w(d(x)) for allx∈X.
Proof. This is an easy exercise. □
Lemma 3.20. LetX be a nonpositive graded set, and letA be a commutative DG
ring. Consider the graded ringB :=A♮⊗Z Z[X] or B :=A♮⊗Z Z⟨X⟩.
(1) Let dX :X→B be a degree1 function. The function dX extends uniquely
to a degree1 derivation dB :B→B, such thatdB|A = dA, the diﬀerential
of A.
(2) The derivationdB is a diﬀerential onB, i.e.dB◦dB = 0, iﬀ(dB◦dB)(x) =
0 for allx∈X.
Proof. (1) Take elementsxj∈Xnj for j = 1,...,m, and consider the monomial
x1···xm∈Z[X] (resp. in Z⟨X⟩). We let
dB(x1···xm) :=
m∑
j=1
(−1)n1+···nj−1·x1···xj−1·dX(xj)·xj+1···xm∈B.
This is well-deﬁned in the commutative case (and there is nothing to check in
the noncommutative case). Extending it additively we obtain a degree1 Z-linear
homomorphism Z[X]→B (resp. Z⟨X⟩→B). This extends to a degree1 A-linear
homomorphism dB :B→B that satisﬁes the graded Leibniz rule.
(2) This is an easy exercise. □
For a DG ringA we denote by Z(A) = ⨁
i Zi(A) the set of cocycles, and by
B(A) =⨁
i Bi(A) the set of coboundaries (i.e. the kernel and image ofdA, respec-
tively). So Z(A) a DG subring ofA (with zero diﬀerential of course), andB(A) is
a two-sided graded ideal ofZ(A).
Theorem 3.21. LetA
u
− →B be a nonpositive central pair of DG rings.
(1) If B is commutative, then there exists a strict commutative semi-free DG
ring resolutionA
˜u
− →˜B of A
u
− →B.
(2) There exists a strict noncommutative semi-free DG ring resolutionA
˜u
− →˜B
of A
u
− →B.
THE SQUARING OPERATION 21
Proof. (1) We are looking for a commutative semi-free DGA-ring ˜B, with a quasi-
isomorphism v : ˜B→B in DGR≤0
sc /A. We shall construct an increasing sequence
of commutative DGA-rings F0( ˜B)⊆F1( ˜B)⊆···. The diﬀerential ofFi( ˜B) will
be denoted bydi. At the same time we shall construct an increasing sequence of
graded sets F0(X)⊆F1(X)⊆···, with a compatible sequence of isomorphisms
Fi( ˜B)♮∼= A♮⊗Z Z[Fi(X)]. We shall also construct a compatible sequence of DG
ring homomorphisms vi : Fi( ˜B)→B. The DG A-ring ˜B := ⋃
iFi( ˜B) and the
homomorphism v := limi→vi will have the desired properties.
The construction is by recursion oni∈N. Moreover, for everyi the following
conditions will hold:
(i) The homomorphisms vi : Fi( ˜B) →B, B(vi) : B( Fi( ˜B)) →B(B) and
H(vi) : H(Fi( ˜B))→H(B) are surjective in degrees≥−i.
(ii) The homomorphism H(vi) : H( Fi( ˜B))→H(B) is bijective in degrees≥
−i + 1.
We start by choosing a setZ′′
0 of degree−1 elements, and a functionv0 :Z′′
0→
B−1, such that the setdB(v0(Z′′
0 )) generates B0(B) as anA0-module. LetY′′
0 be a
set of degree0 elements, with a bijectiond0 :Z′′
0→Y′′
0 . Let v0 :Y′′
0 →B0 be the
unique function such thatv0(d0(z)) = dB(v0(z)) for allz∈Z′′
0.
Choose a setY′
0 of degree 0 elements, and a functionv0 : Y′
0→B0, such that
the setv0(Y′
0⊔Y′′
0 ) generates B0 as anA0-ring.
Deﬁne the graded setF0(X) := Y′
0⊔Y′′
0 ⊔Z′′
0, and the graded ringF0( ˜B)♮:=
A♮⊗Z Z[F0(X)]. Setting d0(y) := 0 for y ∈Y′
0⊔Y′′
0 gives a degree 1 function
d0 : F0(X)→F0( ˜B)♮. According to Lemma 3.20 we get a diﬀerentiald0 on the
graded ringF0( ˜B)♮, and it becomes the DGA-ring F0( ˜B). Lemma 3.19 says that
the function v0 : F0(X)→B extends uniquely to a DGA-ring homomorphism
v0 :F0( ˜B)→B. Condition (i) holds, and condition (ii) holds trivially, fori = 0.
Now take anyi≥0, and assume thatvi : Fi( ˜B)→B is already deﬁned, and
it satisﬁes conditions (i)-(ii). Choose a graded setY′
i+1 of degree−i−1 elements,
and a functionvi+1 : Y′
i+1→Z−i−1(B), such that the cohomology classes of the
elements of vi+1(Y′
i+1) generate H−i−1(B) as H0(A)-module. For y ∈Y′
i+1 let
di+1(y) := 0∈Fi( ˜B).
Consider theA0-module
Ji+1 :=
{
b∈Z−i(Fi( ˜B))|H−i(vi)(b) = 0
}
.
Choose a graded setY′′′
i+1 of degree−i−1 elements, and a functiondi+1 :Y′′′
i+1→
Ji+1, such that the cohomology classes of the elements ofdi+1(Y′′′
i+1) generate the
H0(A)-module
Ker
(
H−i(vi) : H−i(Fi( ˜B))→H−i(B)
{
.
For anyy∈Y′′′
i+1 there exists someb∈B−i−1 such thatvi(di+1(y)) = d(b), and we
let vi+1(y) :=b.
Choose a graded setZ′′
i+1 of degree−i−2 elements, and a functionvi+1 :Z′′
i+1→
B−i−2, such that the setdB(vi+1(Z′′
i+1)) generates B−i−1(B) as A0-module. Let
Y′′
i+1 be a set of degree−i−1 elements, with a bijectiondi+1 :Z′′
i+1→Y′′
i+1. Let
vi+1 :Y′′
i+1→B−i−1 be the unique function such thatvi+1(di+1(z)) = dB(vi+1(z))
for allz∈Z′′
i+1. Fory∈Y′′
i+1 we deﬁnedi+1(y) := 0.
Lastly choose a graded setY′
i+1 of degree−i−1 elements, and a functionvi+1 :
Y′
i+1→B−i−1, such that, letting
Yi+1 :=Y′
i+1⊔Y′′
i+1⊔Y′′′
i+1,
22 AMNON YEKUTIELI
the set vi+1(Yi+1) generates B−i−1 as an A0-module. Since vi : B−i(Fi( ˜B))→
B−i(B) is surjective, for anyy∈Y′
i+1 there existsb∈Fi( ˜B)−i such thatvi(b) =
dB(vi+1(y)), and we deﬁnedi+1(y) :=b.
Deﬁne the graded set
Fi+1(X) :=Fi(X)⊔Yi+1⊔Z′′
i+1
and the commutative graded ring
Fi+1( ˜B)♮:=A♮⊗Z Z[Fi+1(X)].
There is a degree1 function di+1 : Fi+1(X)→Fi+1( ˜B)♮such that di+1|Fi(X) =
di. According to Lemma 3.20 the function di+1 induces a diﬀerentialdi+1 on
Fi+1( ˜B)♮; so we get a DG ringFi+1( ˜B). Likewise we have a degree0 functionvi+1 :
Fi+1(X)→B such thatvi+1|Fi(X) =vi|Fi(X). By Lemma 3.19 there is an induced
DG A-ring homomorphismvi+1 :Fi+1( ˜B)→B, and it satisﬁesvi+1|Fi( ˜B) =vi.
(2) Here we are looking for a noncommutative semi-free DGA-ring ˜B, with a quasi-
isomorphism v : ˜B→B in DGR≤0/ceA. The proof here is the same as in part (1),
except that we now replaceZ[Fi(X)] with Z⟨Fi(X)⟩everywhere. □
Theorem 3.22.LetA
u
− →B be a central pair of nonpositive DG rings. Suppose we
are given two factorizationsA
˜u
− →˜B
v
− →B and A
˜u′
−→˜B′v′
−→B of u in DGR≤0/ceA,
such that v is a surjective quasi-isomorphism, and either of these two conditions
holds:
(i) The DG ring ˜B is commutative, and the DG ring˜B′is commutative semi-
free overA.
(ii) The DG ring ˜B′is noncommutative semi-free overA.
Then there exists a homomorphismw : ˜B′→˜B in DGR≤0/ceA such thatw◦˜u′= ˜u
and v◦w =v′.
The situation is shown in this commutative diagram inDGR/ceA below.
(3.23) ˜B′
v′
  
A u //
˜u′
>>
˜u   
semi-free
B
˜B
v
>>
surj qu-isom
˜B′
v′
  
w

A
˜u′
>>
˜u   
B
˜B
v
>>
Proof. The proof is similar to that of [YZ2, Proposition 1.8]. LetX = ∐
i≤0Xi
be a set of commutative (resp. noncommutative) semi-free DGA-ring generators
of ˜B′over A. Deﬁne Fi(X) := ⋃
−i≤j≤0Xi, and let Fi( ˜B′) be the A-subring
of ˜B′generated by the setFi(X). So Fi( ˜B′) is a DGA-ring, Fi( ˜B′)♮∼= A♮⊗Z
Z[Fi(X)] (resp.Fi( ˜B′)♮∼=A♮⊗Z Z⟨Fi(X)⟩), and ˜B′=⋃
iFi( ˜B′). We will construct
aconsistentsequenceofhomomorphisms wi :Fi( ˜B′)→˜B in DGR≤0/ceA, satisfying
wi◦˜u′= ˜u and v◦wi = v′. The construction is by recursion oni∈N. Then
w := limi→wi will have the required properties.
We start with i = 0. Take any x ∈X0. Since v is surjective, there exists
b∈˜B0 such thatv(b) = v′(x) in B0. We letw0(x) := b. The resulting function
w0 : X0→˜B extends uniquely to a DGA-ring homomorphismw0 : Fi( ˜B′)→˜B,
by Lemma 3.19.
THE SQUARING OPERATION 23
Next consider anyi∈N, and assume a DGA-ring homomorphismwi :Fi( ˜B′)→
˜B is deﬁned, satisfying the required conditions. Take any elementx∈X−i−1.
Since v is surjective, there exists b ∈˜B−i−1 such that v(b) = v′(x) in B−i−1.
Now d(x)∈Fi( ˜B′)−i is a cocycle inFi( ˜B′), sowi(d(x))∈˜B−i is a cocycle. Let
c :=wi(d(x))−d(b)∈˜B−i, which is also a cocycle. We have
v(c) =v(wi(d(x))−v(d(b)) =v′(d(x))−v(d(b)) = d(v′(x)−v(b)) = 0.
Thus the cohomology class [c] satisﬁesH(v)([c]) = [ v(c)] = 0 . Because H(v) is
bijective we conclude that[c] = 0 in H−i( ˜B). Hence there is someb′∈˜B−i−1 such
that d(b′) =c. We deﬁnewi+1(x) :=b +b′. Then
(3.24) d(wi+1(x)) = d(b +b′) = d(b) +c =wi(d(x)).
In this way we obtain a functionwi+1 :Fi+1(X)→˜B that extendswi. Accord-
ing to Lemma 3.19(1), the functionwi+1 extends uniquely to a homomorphism of
graded A♮-rings Fi+1(w) : Fi+1( ˜B′)♮→˜B♮. Equation (3.24) and Lemma 3.19(2)
imply thatwi+1 :Fi+1( ˜B′)→˜B is in fact a homomorphism of DG rings. □
Corollary 3.25.
(1) Any objectB/A of PDGR≤0 admits a nonpositive K-ﬂat resolution˜B/ ˜A.
(2) Any morphismw/v :B′/A′→B/A in PDGR≤0 admits a nonpositive K-ﬂat
resolution ˜w/˜v.
Proof. (1) Let ˜B be a noncommutative semi-free DG ring resolution ofB overA.
See Theorem 3.21. Then ˜B/A is strict nonpositive K-ﬂat resolution ofB/A.
(2) Let ˜B′be a noncommutative semi-free DG ring resolution ofB′over A′, and
let ˜A be a commutative semi-free DG ring resolution of A over A′. Next, let
˜B be a noncommutative semi-free DG ring resolution ofB over ˜A. So ˜B′/A′is
a K-ﬂat resolution ofB′/A′, and ˜B/ ˜A is a K-ﬂat resolution ofB/A. Also, we
have a homomorphism ˜v : A′→˜A above v : A′→A. Finally, according to
Theorem 3.22, we can ﬁnd a homomorphism˜w : ˜B′→˜B that respects all other
homomorphisms. □
