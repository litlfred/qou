---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-086-144-tilting-dg-bimodules
section_title: "Tilting DG Bimodules"
section_number: 14.4
pages: 308-314
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
all DG rings are K-ﬂat central over the base ringK,⊗=⊗K, andAen =A⊗Aop
for a DG ringA.
Deﬁnition 14.4.1.Let A and B be DG rings. An object T ∈D(B⊗Aop) is
called atilting DGB-A-bimodule if there exists some objectS∈D(A⊗Bop), and
isomorphisms S⊗L
BT∼=A in D(Aen) and T⊗L
AS∼=B in D(Ben).
When B = A, so thatB⊗Aop = Aen, we use the termtilting DGA-bimodule
as an abbreviation for the term tilting DGA-A-bimodule.
It is clear from the symmetry of the deﬁnition that the objectS∈D(A⊗Bop)
is a tilting DGA-B-bimodule.
Lemma 14.4.2. LetT∈D(B⊗Aop) and S,S′∈D(A⊗Bop) satisfy S⊗L
BT∼=A
in D(Aen) and T⊗L
AS′∼=B in D(Ben). ThenS′∼=S in D(A⊗Bop). ThereforeT
is a tilting DGB-A-bimodule, andS is a tilting DGA-B-bimodule.
Proof. Using the associativity of derived tensor products from Proposition
14.3.13(4) we have isomorphisms
S∼=S⊗L
BB∼=S⊗L
B (T⊗L
AS′)∼= (S⊗L
BT )⊗L
AS′∼=A⊗L
AS′∼=S′
in D(A⊗Bop). □
The lemma implies that the tilting DGA-B-bimodule S in Deﬁnition 14.4.1 is
unique up to isomorphism.
Deﬁnition 14.4.3.The tilting DGA-B-bimodule S in Deﬁnition 14.4.1 is called
the quasi-inverse ofT.
Here are some general properties of tilting DG bimodules.
Proposition 14.4.4.LetA,B,C be DG rings, letT be a tilting DGB-A-bimodule,
and letS be a tilting DGC-B-bimodule. ThenS⊗L
BT is a tiltingC-A-bimodule.
Proof. LetT∨be the quasi-inverse ofT, and letS∨be the quasi-inverse ofS. Then
(T∨⊗L
BS∨)⊗L
C (S⊗L
BT )∼=T∨⊗L
B (S∨⊗L
CS)⊗L
BT
∼=T∨⊗L
BB⊗L
BT∼=A
in D(Aen). Likewise
(S⊗L
BT )⊗L
A (T∨⊗L
BS∨)∼=C
in D(Cen). □
308
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 14.4.5. SupposeT is a tilting DGB-A-bimodule, andS is a tilting
DG A-B-bimodule. Then the triangulated functor
GT,S : D(Aen)→D(Ben)
with formulaGT,S (M) :=T⊗L
AM⊗L
AS is an equivalence.
Proposition 14.4.6. SupposeT is a tilting DGB-A-bimodule, with quasi-inverse
T∨. Fix an isomorphism T∨⊗L
B T
≃
− →A in D(Aen). Then for every M1,M 2∈
D(Aen) there is an isomorphism
GT,T∨(M1⊗L
AM2)
≃
− →GT,T∨(M1)⊗L
BGT,T∨(M2)
in D(Ben). This isomorphism is bifunctorial in(M1,M 2).
Exercise 14.4.7. Prove Propositions 14.4.5 and 14.4.6.
Deﬁnition 14.4.8.Let A be a K-ﬂat central DGK-ring. The noncommutative
derived Picard group ofA relative toK is the groupDPicK(A), whose elements are
the isomorphism classes inD(Aen) of the tilting DGA-bimodules. The multiplica-
tion in this group is induced from(−⊗L
A−), and the unit element is the class of
the DG bimoduleA.
This deﬁnition is valid by Proposition 14.4.4. Propositions 14.4.5 and 14.4.6 say
that:
Corollary 14.4.9. A tilting DGB-A-bimodule T, with quasi-inverseT∨, and an
isomorphism T∨⊗L
BT∼=A in D(Aen), induce a group isomorphism
DPicK(A)
≃
− →DPicK(B).
We don’t know much about the structure of the derived Picard groupDPicK(A)
in general. However, whenA is either a ring or a commutative DG ring, there are
a few strong structural results – see next subsection.
Remark 14.4.10. IfA is not K-ﬂat over the base ringK, then the derived Picard
group should be deﬁned using a K-ﬂat resolution˜A→A, as explained in Remark
14.3.24. Namely DPicK(A) is the group whose elements are the isomorphism classes
in D( ˜Aen) of the tilting DG ˜A-bimodules, etc. This group is independent, up to a
canonical group isomorphism, of the resolution˜A→A.
The derived homothety morphism in the commutative setting, and the related
derived Morita property, were deﬁned in subsection 13.1. In the current noncom-
mutative setting these notions become more involved, as we shall now see.
Given a DG bimoduleM∈C(B⊗KAop), there are DG ring homomorphisms
hmM,Aop :Aop→EndB(M) = HomB(M,M )
and
hmM,B :B→EndAop(M) = HomAop(M,M )
that we call the noncommutative homothety homomorphisms through Aop and
through B respectively. When we forget the ring structures, these become ho-
momorphisms
(14.4.11) hmM,Aop :A→HomB(M,M )
and
(14.4.12) hmM,B :B→HomAop(M,M )
in Cstr(Aen) and Cstr(Ben) respectively.
Deﬁnition 14.4.13.Let M∈D(B⊗Aop).
309
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) The noncommutative derived homothety morphism ofM throughAop is the
morphism
hmR
M,Aop :=ηR
M,M◦Q(hmM,Aop) :A→RHomB(M,M )
in D(Aen).
(2) The noncommutative derived homothety morphism ofM through B is the
morphism
hmR
M,B :=ηR
M,M◦Q(hmM,B) :B→RHomAop(M,M )
in D(Ben).
Here is a commutative diagram inD(Aen) depicting the noncommutative derived
homothety morphism throughAop.
A
Q(hmM,Aop)

hmR
M,Aop
))
HomB(M,M )
ηR
M,M // RHomB(M,M )
Themorphism ηR
M,M ispartoftherightderivedbifunctor RHomB(−,−); seePropo-
sition 14.3.15.
Deﬁnition 14.4.14.LetA andB be DG rings, and letM be an object ofD(B⊗
Aop).
(1) We say thatM has thenoncommutative derived Morita property on theB
side if the derived homothety morphism
hmR
M,Aop :A→RHomB(M,M )
in D(Aen) is an isomorphism.
(2) We say thatM has the noncommutative derived Morita property on the
Aop side if the derived homothety morphism
hmR
M,B :B→RHomAop(M,M )
in D(Ben) is an isomorphism.
(3) We say thatM has the noncommutative derived Morita property on both
sides if it has the noncommutative derived Morita property on theB side
and on theAop side.
Recall the restriction functors from diagram (14.2.3). Compact generators were
introduced in Deﬁnition 14.2.20(3). The next deﬁnition resembles Deﬁnition
14.2.24.
Deﬁnition 14.4.15.Let A and B be DG rings, and letT be an object ofD(B⊗
Aop).
(1) We say thatT is acompact generator ofD(B), or acompact generator on
the B side, if RestB(T )∈D(B) is a compact generator.
(2) We say thatT is a compact generator ofD(Aop), or acompact generator
on theAop side, if RestAop(T )∈D(Aop) is a compact generator.
(3) We say that T is a compact generator on both sides if it is a compact
generator on theB side and on theAop side.
The next theorem is similar to results appearing in [127] and [84]. It is a derived
version of the classical result for invertible bimodules over a ring (see Example
14.2.36 or [130, Section 4.1]).
In Deﬁnition 14.2.16 we introduced the notion of pretilting DG bimodules, and
in Deﬁnition 14.4.1 we introduced tilting DG bimodules.
310
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Theorem 14.4.16.LetA andB be K-ﬂat DG centralK-rings. The following three
conditions are equivalent for an objectT∈D(B⊗Aop).
(i) The DGB-A-bimoduleT is tilting.
(ii) The DGB-A-bimoduleT is pretilting.
(iii) The DGB-A-bimoduleT is a compact generator on theB side, and it has
the noncommutative derived Morita property on theB side.
Proof.
(i)⇒(ii): LetS∈D(A⊗Bop) be the quasi-inverse ofT. The functor
(14.4.17) GT :=T⊗L
A (−) : D(A)→D(B)
has a quasi-inverse
(14.4.18) GS :=S⊗L
B (−) : D(B)→D(A).
So GT is an equivalence, and the DG bimoduleT is pretilting.
(ii)⇒(iii): By deﬁnition, the functorGT from formula (14.4.17) is an equivalence
of triangulated categories. Also GT (A)∼= T in D(B). Because A is a compact
generator of D(A), Proposition 14.1.8 says thatT is a compact generator ofD(B).
Next we shall prove thatT has the noncommutative derived Morita property on
the B side, namely that the derived homothety morphism
(14.4.19) hmR
M,Aop :A→RHomB(T,T )
in D(Aen) is an isomorphism. According to Proposition 14.3.10 the restriction func-
tor RestA : D(Aen)→D(A) is conservative. Therefore, to prove that the morphism
hmR
M,Aop is an isomorphism in D(Aen), we can forget theAop-module structures
on the DG bimodulesA and RHomB(T,T ), and just prove thatRestA(hmR
M,Aop)
is an isomorphism inD(A).
According to Proposition 14.2.15 the functor
(14.4.20) FT := RHomB(T,−) : D(B)→D(A),
which is the right adjoint ofGT, is an equivalence. So there is an isomorphism of
triangulated functorsζ: IdD(A)
≃
− →FT◦GT from D(A) to itself. There is a diagram
A
RestA(hmR
M,Aop)

ζA
∼=
((
RHomB(T,T )
∼= // RHomB(T,T ⊗L
AA)
∼= // (FT◦GT )(A)
in D(A), and a calculation (with elements, using a K-ﬂat resolutionP →T in
Cstr(B⊗Aop)) shows that it is commutative. BecauseζA is an isomorphism, we
conclude that RestA(hmR
M,Aop) is an isomorphism.
(iii)⇒(ii): Choose a resolutionT→I in C(B⊗Aop) such thatI is K-injective
overB; this is possible by Lemma 14.3.11(2). (IfA is K-projective overK then we
can also choose a resolutionP→T in C(B⊗Aop) such thatP is K-projective over
B; and then the proof can proceed withP instead ofI.) Then the noncommutative
derivedhomothetymorphism hmR
T,Aop in D(Aen)isrepresentedbythecanonicalDG
ring homomorphismg : A→AI, whereAI := EndB(I)op. The noncommutative
derived Morita property on theB side says thatg is a quasi-isomorphism. Hence,
by Theorem 12.7.2, the restriction functorRestg : D(AI)→D(A) is an equivalence.
Because I∼= T is a compact generator ofD(B), according to Theorem 14.2.29
we know that the functorFI := RHomB(I,−) : D(B)→D(AI) is an equivalence.
311
Derived Categories | Amnon Yekutieli | 14 Apr 2019
TakingFT to be the functor from (14.4.20), we have a diagram of functors
D(B)
FI

FT
%%
D(AI)
Restg // D(A)
that is commutative up to isomorphism (cf. Theorem 12.7.2(3)). ThereforeFT is
an equivalence, and thusT is pretilting.
(ii)⇒(i): We assume thatT is a pretilting DGB-A-bimodule, i.e. the functors
GT and FT, from (14.4.17) and (14.4.20) respectively, are equivalences. Deﬁne the
DG bimodule
(14.4.21) S := RHomB(T,B )∈D(A⊗Bop).
Consider the tensor-evaluation morphism
(14.4.22) evR,L
T,B,T : RHomB(T,B )⊗L
BT→RHomB(T,B ⊗L
BT )
in D(Aen) from Proposition 14.3.19. Because the restriction functor RestK :
D(Aen)→D(K) is conservative, to prove thatevR,L
T,B,T is an isomorphism inD(Aen),
it suﬃces to prove it forRestK(evR,L
T,B,T ). But by Proposition 14.2.19 the DG mod-
ule T is algebraically perfect on theB side; so by Theorem 14.1.22, the morphism
RestK(evR,L
T,B,T ) is an isomorphism. Thus we get these isomorphisms
(14.4.23)
S⊗L
BT = RHomB(T,B )⊗L
BT
evR,L
T,B,T
−−−−−→RHomB(T,B ⊗L
BT )∼= RHomB(T,T )
in D(Aen). On the other hand, in the proof of “(ii)⇒(iii)” above we already
showed (formula (14.4.19)) thatA∼= RHomB(T,T ) in D(Aen). Combining this
with (14.4.23) we deduce that
(14.4.24) S⊗L
BT∼=A in D(Aen).
Next, consider the functorGS from formula (14.4.18), where nowS is the DG
bimodule from (14.4.21). The same arguments as above – those used forevR,L
T,B,T –
show that for everyN∈D(B) the morphism
evR,L
T,B,N : RHomB(T,B )⊗L
BN→RHomB(T,B ⊗L
BN)
in D(B) is an isomorphism. So, like (14.4.23), we get isomorphisms
(14.4.25)
GS(N) =S⊗L
BN = RHomB(T,B )⊗L
BN
evR,L
T,B,N
−−−−−→RHomB(T,B ⊗L
BN)∼= RHomB(T,N ) =FT (N)
in D(A). Since these isomorphisms are functorial inN, we see thatGS∼= FT as
functors. ThereforeGS is an equivalence, andS is a pretilting DGA-B-bimodule.
The same proof, but now for the pretilting DGA-B-bimodule S instead of for
T, shows that the DGB-A-bimodule
(14.4.26) T′:= RHomA(S,A )∈D(B⊗Aop)
satisﬁes the corresponding version of (14.4.24), i.e.T′⊗L
AS∼= B in D(Ben). By
Lemma 14.4.2 the DGB-A-bimodule T∼=T′is tilting. □
Corollary 14.4.27. Let T be a tilting DGB-A-bimodule. Then its quasi-inverse
is the DGA-B-bimoduleS := RHomB(T,B ).
Proof. This was shown in the proof of the implication “(ii)⇒(i)” above. □
312
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Corollary 14.4.28. Let T be a tilting DGB-A-bimodule. Then T is a compact
generator on both sides, and it has the noncommutative derived Morita property on
both sides.
Proof. By Theorem 14.4.16,T is a compact generator on theB side, and it has the
noncommutative derived Morita property on theB side.
Using the DG ring isomorphismAop⊗B
≃
− →B⊗Aop of (14.2.7), we can also view
T as an object ofD(Aop⊗B). And as such,T is a tilting DGAop-Bop-bimodule.
Now Theorem 14.4.16 tells us thatT is a compact generator on theAop side, and
it has the noncommutative derived Morita property on theAop side. □
The example of classical Morita Theory was already given; see Example 14.2.36.
Next is an example that goes in another direction altogether.
Example 14.4.29. Suppose f : A→B is a quasi-isomorphism in DGRng/fcK.
Then T :=B∈D(B⊗Aop) is a tilting DGB-A-bimodule. The equivalence
FT := RHomB(T,−) : D(B)→D(A)
is just the restriction functorRestf; and the equivalence
GT :=T⊗L
A (−) : D(A)→D(B)
is just the derived induction functorLIndf.
Theorem 14.4.30 (Rickard-Keller). Let A and B be K-ﬂat DG centralK-rings.
Assume that there exists a K-linear equivalence of triangulated categories F :
D(A) →D(B), and that Hi(A) = 0 for all i ⁄= 0. Then there exists a tilting
DG B-A-bimoduleT.
This theorem is very similar to J. Rickard’s [127, Theorem 6.4] and to B. Keller’s
[79, Corollary 9.2]. See Remark 14.4.35 for a brief discussion.
Proof. We begin with a warning: in the proof we will construct some new DG rings,
and they might fail to be K-ﬂat overK, thus violating Convention 14.3.8.
Consider the objectL :=F (A)∈D(B). It is a compact generator, by Proposi-
tions 14.1.8 and 14.2.23. Let us choose a K-projective resolutionP→L in Cstr(B),
and deﬁne the DG ring˜A := EndB(P )op. SoP∈D(B⊗K ˜Aop).
Because F is an equivalence, we get ring isomorphisms
(14.4.31) H0(A)∼= EndD(A)(A)op F
− →EndD(B)(L)op∼= EndD(B)(P )op∼= H0( ˜A).
For the same reason we haveHi( ˜A)∼= Hi(A) = 0 for alli⁄= 0. Deﬁne the DG rings
A1 := smt≤0(A) and ˜A1 := smt≤0( ˜A), and the ringsA2 := H0(A) and ˜A2 := H0( ˜A).
There are canonical quasi-isomorphismsA1→A,A1→A2, ˜A1→˜A and ˜A1→˜A2
in DGRng/cK. Equation (14.4.31) produces an isomorphismA2∼= ˜A2 in Rng/cK.
Now the DG ringB is K-ﬂat overK, so we have induced quasi-isomorphisms
B⊗Aop←B⊗Aop
1 →B⊗Aop
2 ∼=B⊗˜Aop
2 ←B⊗˜Aop
1 →B⊗˜Aop
in DGRng/cK. According to Theorem 12.7.2 we getK-linear equivalences of trian-
gulated categories
D(B⊗Aop)→D(B⊗Aop
1 )→D(B⊗Aop
2 )
→D(B⊗˜Aop
2 )→D(B⊗˜Aop
1 )→D(B⊗˜Aop).
There is an objectT ∈D(B⊗Aop) that corresponds toP ∈D(B⊗˜Aop) under
this chain of equivalences. All these equivalence restrict to the identity functor of
D(B), and hence there is an isomorphism
(14.4.32) RestB(T )∼= RestB(P )∼=L
313
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in D(B).
Since L is a compact generator on theB side, the same is true forT. Finally,
by equation (14.4.32), and using the equivalenceF, we know that
(14.4.33) Hi(
RHomB(T,T )
{∼= Hi(
RHomB(L,L )
{∼= Hi(
RHomA(A,A )
{
= 0
for alli⁄= 0. By equation (14.4.31) we know that
(14.4.34) H0(
RHomB(T,T )
{∼= EndD(B)(L)∼= EndD(A)(A)∼= H0(A)
as H0(A)-bimodules. Once we trace the various morphisms, formulas (14.4.33) and
(14.4.34) imply that the derived homothety morphism hmR
T,Aop : A →
RHomB(T,T ) in D(Aen) is an isomorphism. So T has the derived Morita prop-
erty on theB side. By Theorem 14.4.16,T is a tilting DGB-A-bimodule. □
Remark 14.4.35.J. Rickard, in [126, Theorem 6.4], considers ringsA andB, and
he does not assume that they are ﬂat over a base ringK. So instead of producing
a tilting complexT, as we do in Theorem 14.4.30 above, he actually produces a
pretilting complex. Another diﬀerence is that Rickard considers an equivalence
F : Db(A)→Db(B), whereas we look at the unbounded derived categories.
B. Keller, in [79, Corollary 9.2], works in much greater generality than we do:
instead of DG ringsA andB, he looks at DG categoriesA and B. Also he does not
require A to be K-ﬂat overK.
The apparent ﬂatness limitation in our Theorem 14.4.30 can be eﬀectively over-
come using K-ﬂat resolutions˜A→A and ˜B→B in DGRng/cK, as explained in
Remark 14.3.24. Since the restriction functorsD(A)→D( ˜A) and D(B)→D( ˜B)
are equivalences, we get an equivalence˜F : D( ˜A)→D( ˜B). Theorem 14.4.30 pro-
duces a tilting DG bimoduleT∈D( ˜B⊗˜Aop).
Remark 14.4.36. In the situation of Theorem 14.4.30, it is not known whether
one can ﬁnd a tilting DGB-A-bimodule T such thatF∼=T⊗L
A (−) as triangulated
functors. This question was already raised by Rickard in [126], and still remains
open, except for a few special cases (see [109] for hereditary rings, and [40] for
triangular rings).
If we drop the condition that the cohomology ofA is concentrated in degree
0, then there is a counterexample to the assertion of Theorem 14.4.30, due to
B. Shipley [140, Section 5], based on her joint work with D. Dugger [45]. Here
is its translation to our terminology. She considers the DG ring A = Z[¯x] :=
Z⟨x⟩/(x4), where x is a variable of degree−1, and d(¯x) := 2 . (Note that A is
weakly commutative but not strongly commutative, since¯x2⁄= 0.) The second DG
ring is H(A). A calculation shows thatH(A)∼=F2[¯y] := F2⟨y⟩/(y2), wherey is a
variable of degree−2, and d(¯y) := 0. For the base ring we takeK :=Z. Because
H(A) is not K-ﬂat overK, we choose a K-ﬂat resolutionB→H(A) overK.
Shipley asserts that on the one hand there is an equivalence of triangulated cat-
egories D(A)→D(B), and on the other hand there does not exist a DG bimodule
T∈D(B⊗Aop) that is a compact generator on theB side, and has the noncommu-
tative derived Morita property on theB side (condition (iii) of Theorem 14.4.16).
Thus there does not exist a tilting DGB-A-bimodule.
Remark 14.4.37.In algebraic geometry the role of tensoring with tilting bimodule
complexes is played byFourier-Mukai transforms. This theory is at the core of
contemporary birational geometry. See the survey [64] or the book [70].
