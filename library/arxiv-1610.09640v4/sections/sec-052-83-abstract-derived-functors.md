---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-052-83-abstract-derived-functors
section_title: "Abstract Derived Functors"
section_number: 8.3
pages: 147-155
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
tors in an abstract setup (as opposed to the triangulated setup).
Deﬁnition 8.3.1(Right Derived Functor). Consider a category K and a multi-
plicatively closed set of morphismsS⊆K, with localization functorQ : K→KS.
LetF : K→E be a functor. Aright derived functor ofF with respect toS is a pair
(RF,ηR), where
RF : KS→E
is a functor, and
ηR :F⇒RF◦Q
is a morphism of functors, such that the following universal property holds:
(R) Given any pair(G,θ), consisting of a functorG : KS→Eand a morphism of
functorsθ:F⇒G◦Q, there is a unique morphism of functorsµ: RF⇒G
such thatθ= (µ◦idQ)∗ηR.
Pictorially: there is a2-diagram
K F //
Q

E
KS
RF
;;
ηR


For any other pair(G,θ) there is a unique morphismµthat sits in this2-diagram
K F //
Q

E
KS
;;
ηR


G
MM
θ

µ ’
such that the diagram of2-morphisms (with∗composition)
F
ηR


θ
"*
RF◦Q µ◦idQ
+3G◦Q
is commutative.
Proposition 8.3.2. If a right derived functor(RF,ηR) exists, then it is unique,
up to a unique isomorphism. Namely, if (G,θ) is another right derived functor
of F, then there is a unique isomorphism of functorsµ: RF
≃
=⇒G such that
θ= (µ◦idQ)∗ηR.
147
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. Despite the apparent complication of the situation, the usual argument for
uniqueness of universals applies. To be explicit, given another right derived functor
(G,θ), let µ: RF ⇒G be the unique morphism that’s guaranteed by property
(R) of the pair(RF,ηR). Then let ν: G⇒RF be the unique morphism that’s
guaranteed by property (R) of the pair(G,θ). Then the morphisms idRF,ν∗µ:
RF⇒RF satisfy
(idRF◦idQ)∗µ=µ= ((ν∗µ)◦idQ)∗µ.
The uniqueness in property (R) of the pair(RF,ηR) implies that idRF = ν∗µ.
Likewise idG =µ∗ν. Henceµis an isomorphism of functors. □
Here is a rather general existence result. Left denominator sets were introduced
in Deﬁnition 6.2.16.
Theorem 8.3.3 (Existence of Right Derived Functor). In the situation of Def-
inition 8.3.1, assume there is a full subcategory J⊆K such the following three
conditions hold:
(a) The multiplicatively closed setS is a left denominator set inK.
(b) For every objectM∈K there is a morphismρ: M→I in S, with target
I∈J.
(c) If ψis a morphism inS∩J, thenF (ψ) is an isomorphism inE.
Then the right derived functor
(RF,ηR) : KS→E
exists. Moreover, for every objectI∈J the morphism
ηR
I :F (I)→RF (I)
in E is an isomorphism.
Condition (b) says that K has enough right J-resolutions. Condition (c) says
that J is anF-acyclic category.
Theorem 8.3.3 is [76, Proposition 7.3.2]. However their notation is diﬀerent:
what we call “left denominator set”, they call “right multiplicative system”.
We need a deﬁnition and a few lemmas before giving the proof of the theorem.
In them we assume the situation of the theorem.
Deﬁnition 8.3.4.In the situation of Theorem 8.3.3, by a system of right J-
resolutions we mean a pair (I,ρ), where I : Ob( K)→Ob(J) is a function, and
ρ={ρM}M∈Ob(K) is a collection of morphismsρM :M→I(M) in S. Moreover, if
M∈Ob(J), thenI(M) =M and ρM = idM.
Since here K has enough right J-resolutions, it follows that systems of right
J-resolutions (I,ρ) exist.
Let us introduce some new notation that will make the proofs more readable:
(8.3.5) K′:= J, S′:= J∩S, D := KS and D′:= K′
S′.
The inclusion functor isU : K′→K, and its localization isV : D′→D. These sit
in a commutative diagram
(8.3.6) K′U //
Q′

K
Q

D′V // D
Lemma 8.3.7. The multiplicatively closed setS′is a left denominator set inK′.
148
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. We need to verify conditions (LD1) and (LD2) in Deﬁnition 6.2.16.
(LD1): Given morphismsa′:L′→N′in K′and s′:L′→M′in S′, we must ﬁnd
morphisms b′: M′→K′in K′and t′: N′→K′in S′, such thatt′◦a′= b′◦s′.
Because S⊆K satisﬁes this condition, we can ﬁnd morphismsb : M′→K in K
and t : N′→K in S such thatt◦a′= b◦s′. There is a morphismρ: K→K′
in S with targetK′∈K′. Then the morphismst′:= ρ◦t and b′:= ρ◦b satisfy
t′◦a′=b′◦s′, andt′∈S′.
(LD2): Given morphismsa′,b′:M′→N′in K′ands′:L′→M′in S′, that satisfy
a′◦s′=b′◦s′, we must ﬁnd a morphismt′:N′→K′in S′such thatt′◦a′=t′◦b′.
Because S⊆K satisﬁes this condition, we can ﬁnd a morphismt : N′→K in S
such thatt◦a′=t◦b′. There is a morphismρ:K→K′in S with targetK′∈K′.
Then the morphismt′:=ρ◦t has the required property. □
Lemma 8.3.8. The functorV : D′→D is an equivalence.
Proof. Condition (b) of the theorem implies that V is essentially surjective on
objects. We need to prove thatV is fully faithful. We shall use the left version
of Proposition 6.2.34, namelyS and S′are left denominator sets, and in condition
(ii) the morphisms ares : L′→M and t : M →K′. (See Remark 6.2.3 and
Propositions 6.1.5 and 6.2.17 regarding side changes.) By Lemma 8.3.7 the left
version of condition (i) of Proposition 6.2.34 holds. Condition (b) of the theorem
implies the left version of condition (ii) of Proposition 6.2.34. Then the left version
of Proposition 6.2.34 says thatV is fully faithful. □
Lemma 8.3.9. Suppose a system of right K′-resolutions (I,ρ) has been chosen.
Then the functionI : Ob(K)→Ob(K′) extends uniquely to a functorI : D→D′,
such that I◦V = Id D′, and Q(ρ) : Id D⇒V◦I is an isomorphism of functors.
Therefore the functorI is a a quasi-inverse ofV.
The relevant2-diagram is this:
K′ Q′
//
U

D′
V
""
Id // D′
K
Q // D
I
OO
Id
//
Q(ρ)
KS
D
I
OO
Recall that in a2-diagram, an empty polygon means it is commutative, namely it
can be ﬁlled with
id
=⇒.
Proof. Consider a morphismψ:M→N in D. SinceV : D′→D is an equivalence,
and since V (I(M)) = I(M) and V (I(N)) = I(N), there is a unique morphism
I(ψ) :I(M)→I(N) in D′satisfying
(8.3.10) V (I(ψ)) := Q(ρN)◦ψ◦Q(ρM)−1.
in D.
Let us check thatI : D→D′is really a functor. Suppose φ: L→M and
ψ:M→N are morphisms inD. Then
V
(
I(ψ)◦I(φ)
{
=V (I(ψ))◦V (I(φ))
=
(
Q(ρN)◦ψ◦Q(ρM)−1{
◦
(
Q(ρM)◦φ◦Q(ρL)−1{
= Q(ρN)◦(ψ◦φ)◦Q(ρL)−1 =V
(
I(ψ◦φ)
{
.
Since V is an equivalence, it follows thatI(ψ)◦I(φ) =I(ψ◦φ).
149
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Because ρM′: M′→I(M′) is the identity for any objectM′∈K′, we see that
there is equalityI◦V = IdD′. By the deﬁning formula (8.3.10) ofI(ψ) we have a
commutative diagram
V (I(M))
V (I(ψ)) //V (I(N))
M
ψ //
Q(ρM)
OO
N
Q(ρN)
OO
in D. Hence Q(ρ) : IdD⇒V◦I is an isomorphism of functors. □
Diagram (8.3.6) induces a commutative diagram of categories:
(8.3.11) Fun(K′, E) Fun(K, E)
Fun(U,Id)oo
FunS′(K′, E)
f.f.emb
OO
FunS(K, E)
f.f.emb
OO
equiv
Fun(U,Id)oo
Fun(D′, E)
Fun(Q′,Id) isom
OO
Fun(D, E)
Fun(V,Id)
equiv
oo
Fun(Q,Id)isom
OO
The vertical arrows marked “f.f. emb” are fully faithful embeddings by deﬁnition.
According to Proposition 8.2.6 the vertical arrows marked “isom” are isomorphisms
of categories. And by Lemma 8.3.8 and Proposition 8.2.3 the arrowFun(V, Id) in
the bottom row is an equivalence. As a consequence, the arrowFun(U, Id) in the
middle row is also an equivalence.
Let’s introduce the notationF′:= F◦U : K′→E. This functor is an object
of the category in the middle left of diagram (8.3.11), since, by condition (c) of
Theorem 8.3.3, it invertsS′.
Lemma 8.3.12.LetG : D→E be a functor. Given a morphismθ′:F′⇒G◦Q◦U
of functors K′→E, there is a unique morphismθ:F⇒G◦Q of functors K→E
s.t. θ′=θ◦idU.
Note thatG is an object in the category in the bottom right of diagram (8.3.11).
The morphismsθ′and θare in the middle left and top right respectively of this
diagram.
Proof. For every objectM∈K there is a morphismρ: M→I in S with target
I∈K′. A morphism of functorsθsatisfying θ′= θ◦idU will make this diagram
commutative:
(8.3.13) F (M)
θM //
F(ρ)

(G◦Q)(M)
(G◦Q)(ρ)∼=

F (I)
θ′
I // (G◦Q)(I)
We are using the facts thatI =U(I) and thatQ(ρ) is an isomorphism. This proves
the uniqueness ofθ.
For existence, let us choose a system of rightK′-resolutions (I,ρ), and deﬁne
θ={θM}using (8.3.13), namely
(8.3.14) θM := (G◦Q)(ρM)−1◦θ′
I(M)◦F (ρM).
150
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We must prove that this is indeed a morphism of functorsK→E. Namely, for a
given morphismφ:M→N in K, we have to prove that the diagram
(8.3.15) F (M)
θM //
F(φ)

(G◦Q)(M)
(G◦Q)(φ)

F (N)
θN // (G◦Q)(N)
in E is commutative.
Lemma 8.3.7 tells us that the morphismI(Q(φ)) in D′can be written as a left
fraction
(8.3.16) I(Q(φ)) = Q′(ψ1)−1◦Q′(ψ0)
of morphismsψ0∈K′and ψ1∈S′. We get these diagrams:
(8.3.17) M
φ //
ρM

N
ρN

I(M)
ψ0 
I(N)
ψ1
J
M
Q(φ) //
Q(ρM)

N
Q(ρN)

I(M)
V (I(Q(φ))) //
Q(ψ0)   
I(N)
Q(ψ1)~~
J
The ﬁrst diagram is in the categoryK, and it might fail to be commutative. The
second diagram is in the categoryD, and it is commutative: the bottom triangle
commutes by formula (8.3.16) and the equalityV◦Q′= Q; and the top square
commutes by formula (8.3.10). By condition (LO4) of the left Ore localization
Q : K→D, there is a morphismψ:J→L in S such thatψ◦ψ0◦ρM =ψ◦ψ1◦ρN◦φ
in K. There is the morphismρL :L→I(L) in S, whose targetI(L) belongs to K′.
Thus, after replacing the objectJ withI(L), the morphismψ0 byρL◦ψ◦ψ0, and
the morphismψ1 byρL◦ψ◦ψ1, and noting that the latter is a morphism inS′, we
can now assume that the ﬁrst diagram in (8.3.17) commutative too.
Now we embed (8.3.15) in the bigger diagram (8.3.18) inE. Since ρN∈S and
ψ1∈S′, the morphisms (G◦Q)(ρN), (G◦Q)(ψ1) and F (ψ1) are isomorphisms.
The top and bottom squares in (8.3.18) are commutative by the deﬁnition ofθM
and θN, see formula (8.3.14). The left and right rounded shapes (those involving
J) are commutative because the ﬁrst diagram in (8.3.17) is commutative.
(8.3.18) F (I(M))
θ′
I(M)
//
F(ψ0)

(G◦Q)(I(M))
(G◦Q)(ψ0)

F (M)
F(ρM)
OO
θM //
F(φ)

(G◦Q)(M)
(G◦Q)(ρM)∼=
OO
(G◦Q)(φ)

F (J) F (N)
θN //
F(ρN)

(G◦Q)(N)
(G◦Q)(ρN)∼=

(G◦Q)(J)
F (I(N))F(ψ1)
∼=
QQ
θ′
I(N)
// (G◦Q)(I(N)) (G◦Q)(ψ1)
∼=
KK
151
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Since θ′: F′⇒G◦Q◦U is a morphism of functors, we have a commutative
diagram
(8.3.19) F (I(M))
θ′
I(M)
//
F(ψ0)

(G◦Q)(I(M))
(G◦Q)(ψ0)

F (J)
θ′
J // (G◦Q)(J)
F (I(N))
F(ψ1)
OO
θ′
I(N)
// (G◦Q)(I(N))
(G◦Q)(ψ1)
OO
When we erase the arrowθ′
J from diagram (8.3.19), we obtain the outer boundary
of diagram (8.3.18). Therefore diagram (8.3.18) is commutative. In particular,
the middle square of diagram (8.3.18) is commutative, and it is precisely diagram
(8.3.15). □
Proof of Theorem8.3.3. The proof is divided into four steps.
Step 1. Recall that the functorF′=F◦U lives in the middle left term in diagram
(8.3.11). Because the arrowFun(Q′, Id) is an isomorphism, there is a unique functor
RF′living in the bottom left term of diagram (8.3.11) that satisﬁesRF′◦Q′=F′.
See next commutative diagram.
(8.3.20) K′ F′
//
Q′

E
D′
RF′
::
Letη′:= idF′. We claim that the pair(RF′,η′) is a right derived functor ofF′.
Indeed, suppose we are given a pair(G′,θ′), whereG′is a functor in the bottom
left corner of diagram (8.3.11), andθ′:F′⇒G′◦Q′is a morphism in the top left
corner of that diagram. See the2-diagram (8.3.22). Because the function
(8.3.21) HomFun(D′,E)(RF′,G′)→HomFun(K′,E)(F′,G′◦Q′)
is bijective – this is the left edge of diagram (8.3.11) – there is a unique morphism
µ′: RF′⇒G′that goes toθ′under (8.3.21).
(8.3.22) K′ F′
//
Q′

E
D′
RF′
;;
η′


G′
MM
θ′

µ′’
Step 2. Now we choose a system of right K′-resolutions (I,ρ), in the sense of
Deﬁnition 8.3.4. By Lemma 8.3.9 we get an equivalence of categoriesI : D→D′,
that is a quasi-inverse toV, and an isomorphism of functorsQ(ρ) : Id D
≃
− →V◦I.
152
Derived Categories | Amnon Yekutieli | 14 Apr 2019
See the following2-diagram (the solid arrows).
(8.3.23) K′ Q′
//
U

F′

D′
V
""
Id // D′ RF′
// E
K Q
// D
I
OO
Id
//
Q(ρ)
KS
D
I
OO
RF
<<
Deﬁne the functor
(8.3.24) RF := RF′◦I : D→E.
It is the dashed arrow in diagram (8.3.23). So the functorRF lives in the bottom
right corner of (8.3.11), andRF′= RF◦V.
Step 3. Consider Lemma 8.3.12, with the functorG := RF, and the morphism of
functors
η′= idF′:F′⇒RF′◦Q′= RF◦Q◦U.
The lemma says that there is a unique morphism of functorsηR :F⇒RF◦Q s.t.
ηR◦idU =η′.
We can give an explicit formula for the morphism of functorsηR. Take an object
M∈K. Then the morphismηR
M :F (M)→RF (M) =F (I(M)) in E is nothing but
(8.3.25) ηR
M :=F (ρM).
Here is the calculation. By formula (8.3.14) we have
ηR
M = (RF◦Q)(ρM)−1◦η′
I(M)◦F (ρM).
But η′
I(M) = idF(I(M)),
I(Q(ρM)) = Q(ρI(M))◦Q(ρM)◦Q(ρM)−1 = idI(M)
by (8.3.10), and
(RF◦Q)(ρM) = (RF′◦I◦Q)(ρM) = RF′(idI(M)) = idF(I(M)).
So everything else gets canceled, and we are left with (8.3.25).
Step 4. It remains to prove that the pair(RF,ηR) is a right derived functor ofF.
Suppose (G,θ) is a pair, whereG is a functor in the category in the bottom right
corner of diagram (8.3.11), andθ:F⇒G◦Q is a morphism in the top right corner
of the diagram. We are looking for a morphismµ: RF⇒G in the bottom right
category in diagram (8.3.11) for whichθ= (µ◦idQ)∗ηR. LetG′:=G◦V, and let
θ′:F′⇒G′◦Q′be the morphism in the top left corner of (8.3.11) corresponding
toθ. Because of the equivalenceFun(V, Id), ﬁnding suchµis the same as ﬁnding a
morphismµ′: RF′⇒G′in the bottom left category in diagram (8.3.11), satisfying
(8.3.26) θ′= (µ′◦idQ′)∗η′.
Finally, by step 1 the pair(RF′,η′) is a right derived functor ofF′. This says
that there is a unique morphismµ′satisfying (8.3.26). □
Deﬁnition 8.3.27.The construction of the right derived functor(RF,ηR) in the
proof of Theorem 8.3.3, and speciﬁcally formulas (8.3.24) and (8.3.25), is called a
presentation of (RF,ηR) by the system of rightJ-resolutions (I,ρ).
153
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Of course any other right derived functor ofF (perhaps presented by another
system of rightJ-resolutions) is uniquely isomorphic to(RF,ηR). This is according
to Proposition 8.4.8. In Sections 10 and 11 we shall give several existence results
for right resolutions by suitable acyclic objects.
Now to left derived functors.
Deﬁnition 8.3.28(Left Derived Functor). Consider a category K and a multi-
plicatively closed set of morphismsS⊆K, with localization functorQ : K→KS.
Let F : K→E be a functor. Aleft derived functor ofF with respect toS is a pair
(LF,ηL), where
LF : KS→E
is a functor, and
ηL : LF◦Q⇒F
is a morphism of functors, such that the following universal property holds:
(L) Given any pair(G,θ), consisting of a functorG : KS→Eand a morphism of
functorsθ:G◦Q⇒F, there is a unique morphism of functorsµ:G⇒LF
such thatθ=ηL∗(µ◦idQ).
Pictorially: there is a2-diagram
K F //
Q

E
KS
LF
;;
ηL
KS
For any other pair(G,θ) there is a unique morphismµthat sits in this2-diagram
K F //
Q

E
KS
;;
ηL
KS
G
MM
θ
QY
µ
_g
such that the diagram of2-morphisms (with∗composition)
F
LF◦Q
ηL
KS
G◦Q
θ
bj
µ◦idQ
ks
is commutative.
We see that a left derived functor with target E amounts to a right derived
functor with targetEop. It means that new proofs are not needed.
Proposition 8.3.29. If a left derived functor(LF,ηL) exists, then it is unique, up
to a unique isomorphism. Namely, if(G,θ) is another left derived functor ofF, then
there is a unique isomorphism of functorsµ:G
≃
=⇒LF such thatθ=ηL∗(µ◦idQ).
The proof is the same as that of Proposition 8.3.2, only some arrows have to be
reversed.
Theorem 8.3.30 (Existence of Left Derived Functor). In the situation of Deﬁ-
nition 8.3.28, assume there is a full subcategoryP⊆K such the following three
conditions hold:
(a) The multiplicatively closed setS is a right denominator set inK.
154
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(b) For every objectM∈K there is a morphismρ:P→M in S, with source
P∈P.
(c) If ψis a morphism inP∩S, thenF (ψ) is an isomorphism inE.
Then the left derived functor
(LF,ηL) : KS→E
exists. Moreover, for every objectP∈P the morphism
ηL
P : LF (P )→F (P )
in E is an isomorphism.
Condition (b) says thatK has enough leftP-resolutions. Condition (c) says that
P is anF-acyclic category.
The proof is the same as that of Theorem 8.3.3, only some arrows have to be
reversed. We leave this as an exercise.
Exercise 8.3.31.Prove Theorem 8.3.30, including the lemmas leading to it. (Hint:
replace E with Eop.)
For reference we give the next deﬁnition.
Deﬁnition 8.3.32.In the situation of Theorem 8.3.30, by a system of left P-
resolutions we mean a pair(P,ρ), where P : Ob( K)→Ob(P) is a function, and
ρ={ρM}M∈Ob(K) is a collection of morphismsρM :P (M)→M in S. Moreover, if
M∈Ob(P), thenP (M) =M and ρM = idM.
When K has enough leftP-resolutions, there exists a system of leftP-resolutions
(P,ρ) .
Deﬁnition 8.3.33.The construction of the left derived functor(LF,ηL) in the
proof of Theorem 8.3.30 – i.e. the left variant of the proof of Theorem 8.3.3, and
speciﬁcally the left versions of formulas (8.3.24) and (8.3.25) – is called apresenta-
tion of (LF,ηL) by the system of leftP-resolutions (P,ρ).
Of course any other left derived functor ofF (perhaps presented by another
system of leftP-resolutions) is uniquely isomorphic to(LF,ηL). This is according
to Proposition 8.3.29. In Sections 10 and 11 we shall give several existence results
for left resolutions by suitable acyclic objects.
Remark 8.3.34. The right derived functorRF from Deﬁnition 8.3.1 is aleft Kan
extension ofF along Q. Likewise, the left derived functorLF from Deﬁnition 8.3.28
is aright Kan extensionof F along Q. See [102, Chapter X].
