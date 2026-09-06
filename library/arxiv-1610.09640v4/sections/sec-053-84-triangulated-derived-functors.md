---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-053-84-triangulated-derived-functors
section_title: "Triangulated Derived Functors"
section_number: 8.4
pages: 155-162
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
nitions and results of the previous subsection to the case of triangulated functors
between triangulated categories. There is a ﬁxed nonzero commutative base ring
K, and all categories and functors here areK-linear.
Triangulated functors and morphisms between them were introduced in Deﬁni-
tion 5.2.1. Recall that a triangulated functor is a pair(F,τ), consisting of a linear
functorF and a translation isomorphismτ, that respect the distinguished triangles.
Here is the triangulated version of Deﬁnition 8.2.1.
Deﬁnition 8.4.1.Let K and L be triangulated categories. We deﬁneTrFun(K, L)
to be the category whose objects are the triangulated functors (F,τ) : K→L.
Given objects (F,τ) and (G,ν) of TrFun(K, L), the morphismsα: (F,τ)⇒(G,ν)
in TrFun(K, L) are the morphisms of triangulated functors.
155
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Lemma 8.4.2. Let (F,τ) : ( K, TK)→(L, TL) be a triangulated functor between
triangulated categories. AssumeF is an equivalence(of abstract categories), with
quasi-inverse G : L→K, and with adjunction isomorphismsα:G◦F
≃
=⇒IdK and
β:F◦G
≃
=⇒IdL. Then there is an isomorphism of functorsν:G◦TL
≃
=⇒TK◦G
such that (G,ν) : ( L, TL)→(K, TK) is a triangulated functor, andαand βare
isomorphisms of triangulated functors.
Proof. It is well-known thatG is additive (or in our case,K-linear); but since the
proof is so easy, we shall reproduce it. Take any pair of objectsM,N ∈L. We have
to prove that the bijection
GM,N : HomL(M,N )→HomK
(
G(M),G (N)
{
is linear. But
GM,N = (FG(M),G(N))−1◦HomL(βM,β−1
N )
asbijections(ofsets)betweenthesemodules. Since HomL(βM,β−1
N )andF−1
G(M),G(N)
areK-linear, so isGM,N.
We deﬁne the isomorphism of functorsνby the formula
ν:= (α◦idTK◦G)∗(idG◦τ◦idG)−1∗(idG◦TL◦β)−1,
in terms of the2-categorical notation. This gives rise to a commutative diagram of
isomorphisms
G◦TL◦F◦G
id◦β


G◦F◦TK◦Gid◦τ◦idks
α◦id


G◦TL
ν +3 TK◦G
of additive functorsL→K. So the pair(G,ν) is a T-additive functor.
Theveriﬁcationthat (G,ν)preservestriangles(inthesenseofDeﬁnition5.2.1(1))
is done like the proof of the additivity ofG, but now using axiom (TR1)(a) from
Deﬁnition 5.1.10. Alsoαandβare morphisms of triangulated functors (Deﬁnitions
5.2.1(2) and 5.1.5). We leave these veriﬁcations as an exercise. □
Exercise 8.4.3. Finish the proof above (the last assertions).
From here on in this subsection we shall usually keep the translation isomor-
phisms (such asτand νabove) implicit.
Suppose we are given triangulated functorsU : K′→K and V : L→L′. There
is an induced functor
TrFun(U,V ) : TrFun(K, L)→TrFun(K′, L′);
the formula is the same as in (8.2.2).
Lemma 8.4.4. If U and V are equivalences, then the functorTrFun(U,V ) is an
equivalence.
Proof. Use Proposition 8.2.3 and Lemma 8.4.2. □
Deﬁnition 8.4.5.Let K and L be triangulated categories, and let S⊆K be a
denominator set of cohomological origin. We deﬁne TrFunS(K, L) to be the full
subcategory of TrFun(K, L) whose objects are the functors that are localizable toS,
in the sense of Deﬁnition 8.2.5.
We know that the localization functor Q : K →KS is a left and right Ore
localization.
156
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Lemma 8.4.6. Let K and E be triangulated categories, and letS⊆K be a denom-
inator set of cohomological origin. Then the functor
TrFun(Q, IdE) : TrFun(KS, E)→TrFunS(K, E)
is an isomorphism of categories.
Proof. Use Proposition 8.2.6 and Theorem 7.1.3. □
Here is the triangulated version of Deﬁnition 8.3.1.
Deﬁnition 8.4.7.Let F : K→E be a triangulated functor between triangulated
categories, and let S⊆K be a denominator set of cohomological origin. A tri-
angulated right derived functor ofF with respect to S is a triangulated functor
RF : KS→E, together with a morphismηR :F⇒RF◦Q of triangulated functors
K→E. The pair(RF,ηR) must have this universal property:
(R) Given any pair (G,θ), consisting of a triangulated functorG : KS →E
and a morphism of triangulated functorsθ:F⇒G◦Q, there is a unique
morphism of triangulated functorsµ: RF⇒G such thatθ= (µ◦idQ)∗ηR.
Proposition 8.4.8. If a triangulated right derived functor(RF,ηR) exists, then
it is unique, up to a unique isomorphism. Namely, if (G,θ) is another triangu-
lated right derived functor ofF, then there is a unique isomorphism of triangulated
functors µ: RF
≃
=⇒G such thatθ= (µ◦idQ)∗ηR.
The proof is the same as that of Proposition 8.3.2. Now for the triangulated
version of Theorem 8.3.3.
Theorem 8.4.9. In the situation of Deﬁnition8.4.7, assume there is a full trian-
gulated subcategoryJ⊆K with these two properties:
(a) Every objectM∈K admits a morphismρ:M→I in S with targetI∈J.
(b) If ψis a morphism inJ∩S, thenF (ψ) is an isomorphism inE.
Then the triangulated right derived functor(RF,ηR) : KS→E of F with respect to
S exists. Moreover, for every objectI∈J the morphismηR
I :F (I)→RF (I) in E
is an isomorphism.
Proof. It will be convenient to change notation to that used in the proof of Theorem
8.3.3. Let’s deﬁneK′:= J, S′:= K′∩S and D′:= K′
S′. The localization functor of
K′is Q′: K′→D′. The inclusion functor isU : K′→K, and its localization is the
functor V : D′→D. We have this commutative diagram of triangulated functors
between triangulated categories:
(8.4.10) K′U //
Q′

K
Q

D′V // D
The functorU is fully faithful. By Lemma 8.3.8 the functorV is an equivalence.
Diagram (8.4.10) induces a commutative diagram of linear categories:
(8.4.11) TrFun(K′, E) TrFun(K, E)
Fun(U,Id)oo
TrFunS′(K′, E)
f.f.emb
OO
TrFunS(K, E)
f.f.emb
OO
equiv
Fun(U,Id)oo
TrFun(D′, E)
Fun(Q′,Id) isom
OO
TrFun(D, E)
Fun(V,Id)
equiv
oo
Fun(Q,Id)isom
OO
157
Derived Categories | Amnon Yekutieli | 14 Apr 2019
By deﬁnition the arrows marked “f.f. emb” are fully faithful embeddings. According
to Lemma 8.4.6 the arrowsFun(Q, Id) and Fun(Q′, Id) are isomorphisms of cate-
gories. By Lemma 8.4.4 the arrowFun(V, Id) is an equivalence. It follows that the
arrow Fun(U, Id) in the middle row is an equivalence too.
We know thatS⊆K is a left denominator set. Condition (b) of the theorem
says that F sends morphisms in S′to isomorphisms in E. Condition (a) there
says that there are enough rightK′-resolutions in K. Thus we are in a position
to use the abstract Theorem 8.3.3. It says that there is an abstract right derived
functor (RF,ηR) : D = KS→E of F with respect to S. However, going over the
proof of Theorem 8.3.3, we see that all constructions there can be made within
the triangulated setting, namely in diagram (8.4.11) instead of in diagram (8.3.11).
Therefore RF is an object of the category in the bottom right corner of (8.4.11),
and the morphismηR : F⇒RF◦Q is in the category in the top right corner of
(8.4.11). The triangulated variant of step 4 in the proof of Theorem 8.3.3 shows
that (RF,ηR) satisﬁes condition (R) of Deﬁnition 8.4.7. □
By slight abuse of notation, in the situation of Deﬁnition 8.4.7 we sometimes
refer to the triangulated right derived functorRF just as “the right derived functor
of F”. As the next corollary shows, this does really cause a problem.
Corollary 8.4.12.In the situation of Theorem8.4.9, the triangulated right derived
functor (RF,ηR) is also an abstract right derived functor ofF with respect toS, in
the sense of Deﬁnition8.3.1.
Proof. This is seen in the proof of Theorem 8.4.9. □
In the situation of Theorem 8.4.9, letK⋆be a full triangulated subcategory of
K. Deﬁne S⋆:= K⋆∩S and J⋆:= K⋆∩J. Denote by W : K⋆→K the inclusion
functor, and byWS⋆: K⋆
S⋆→KS its localization. Warning: the functorWS⋆is not
necessarily fully faithful; cf. Proposition 7.1.13.
Proposition 8.4.13. Assume that every objectM ∈K⋆admits a morphismρ:
M→I in S⋆with targetI∈J⋆. Then the pair(R⋆F,η⋆) := (RF◦WS⋆,ηR◦idW )
is a right derived functor ofF⋆:=F◦W : K⋆→E.
Exercise 8.4.14. Prove the last proposition. (Hint: Start by choosing a system
of right J⋆-resolutions in K⋆. Then extend it to a system of rightJ-resolutions in
K. Now follow the proofs of Theorems 8.4.9 and 8.3.3.)
Here is the specialization of Deﬁnition 8.4.7 to categories of DG modules. First:
Setup 8.4.15. We are given a DG ringA, an abelian category M, and a full
triangulated subcategory K⊆K(A, M). We write S := K∩S(A, M), the set of
quasi-isomorphisms in K, and D := KS, the derived category ofK.
Deﬁnition 8.4.16.Under Setup 8.4.15, letE be a triangulated category, and let
F : K→E be a triangulated functor. Atriangulated right derived functorofF is a
triangulated right derived functor(RF,ηR) : D→E of F with respect toS, in the
sense of Deﬁnition 8.4.7.
Example 8.4.17.Suppose we start from an additive functorF 0 : M→N between
abelian categories. We know how to extend it to a DG functor
C+(F 0) : C+(M)→C+(N),
and this induces a triangulated functor
K+(F 0) : K+(M)→K+(N).
158
Derived Categories | Amnon Yekutieli | 14 Apr 2019
By composing with the localization functorQ+
N : K+(N)→D+(N) we get a trian-
gulated functor
(8.4.18) F := Q+
N◦K+(F 0) : K+(M)→D+(N).
DeﬁneK := K+(M), S := S+(M) and E := D+(N), so in this notation we have a
triangulated functorF : K→E, and we are in the situation of Deﬁnition 8.4.16.
Note that the restriction ofF to the full subcategoryM⊆K+(M) coincides with
the original functorF 0.
Assume that the abelian categoryM has enough injectives; namely that every
object M∈M admits a monomorphism to an injective object. LetJ be the full
subcategory of K on the bounded below complexes of injective objects. We will
prove later (see Corollary 10.1.19 and Theorem 11.5.8) that properties (a) and (b)
of Theorem 8.4.9 hold for thisJ, regardless whatF is. Therefore the triangulated
right derived functor
(8.4.19) (R+F,η+) : D+(M)→D+(N)
exists, and for every complexI∈J the morphism
(8.4.20) η+
I :F (I)→R+F (I)
in D+(N) is an isomorphism.
Now assume the original functorF 0 : M→N is left exact. For each q ≥0
we have the classical right derived functor RqF 0 : M →N, and R0F 0 ∼= F 0.
Formula (8.4.20) shows that for everyM∈M and q≥0 there is an isomorphism
RqF 0(M)∼= Hq(R+F (M)) in N. As the object M ∈M moves, this becomes an
isomorphism RqF 0∼= Hq◦R+F of additive functorsM→N.
In this example we were careful to use distinct notations for the functorF 0 be-
tween abelian categories, and the induced triangulated functorF = Q+
N◦K+(F 0).
Later we will use the same notation forF 0 and F.
Our treatment of triangulated left derived functors will be brief: we will state
the deﬁnitions and the main results, but won’t give proofs, beyond a hint here and
there on the passage from right to left derived functors.
Deﬁnition 8.4.21.Let F : K→E be triangulated functor between triangulated
categories, and let S⊆K be a denominator set of cohomological origin. A tri-
angulated left derived functor of F with respect to S is a triangulated functor
LF : KS→E, together with a morphismηL : LF◦Q⇒F of triangulated functors
K→E. The pair(LF,ηL) must have this universal property:
(L) Given any pair (G,θ), consisting of a triangulated functorG : KS →E
and a morphism of triangulated functorsθ:G◦Q⇒F, there is a unique
morphism of triangulated functorsµ:G⇒LF such thatθ=ηL∗(µ◦idQ).
Proposition 8.4.22. If a triangulated left derived functor(LF,ηL) exists, then it
is unique, up to a unique isomorphism. Namely, if(G,θ) is another triangulated left
derived functor ofF, then there is a unique isomorphism of triangulated functors
µ:G
≃
=⇒LF such thatθ=ηL∗(µ◦idQ).
The proof is the same as that of Proposition 8.4.8, with direction of arrows inE
reversed.
Theorem 8.4.23. In the situation of Deﬁnition8.4.21, assume there is a full
triangulated subcategoryP⊆K with these two properties:
(a) Every objectM∈K admits a morphismρ:P→M in S with sourceP∈P.
(b) If ψis a morphism inP∩S, thenF (ψ) is an isomorphism inE.
159
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Then the triangulated left derived functor(LF,ηL) : KS→E of F with respect to
S exists. Moreover, for every objectP∈P the morphismηL
P : LF (P )→F (P ) in E
is an isomorphism.
The proof is the same as that of Theorem 8.4.9, with direction of arrows inE
reversed.
Corollary 8.4.24.In the situation of Theorem8.4.23, the triangulated left derived
functor (LF,ηL) is also an abstract left derived functor ofF with respect toS, in
the sense of Deﬁnition8.3.28.
The proof is the same as that of Corollary 8.4.12, with direction of arrows inE
reversed.
In the situation of Theorem 8.4.23, letK⋆be a full triangulated subcategory of
K. DeﬁneS⋆:= K⋆∩S and P⋆:= K⋆∩P. Denote by W : K⋆→K the inclusion
functor, and byWS⋆: K⋆
S⋆→KS its localization.
Proposition 8.4.25. Assume that everyM∈K⋆admits a morphismρ:P→M
in S⋆with sourceP ∈P⋆. Then the pair (L⋆,η⋆) := (L F◦WS⋆,ηL◦idW ) is a
triangulated left derived functor ofF⋆:=F◦W : K⋆→E.
The proof is just like that of Proposition 8.4.13 (which was an exercise).
Here is the specialization of Deﬁnition 8.4.21 to categories of DG modules.
Deﬁnition 8.4.26.Under Setup 8.4.15, letE be a triangulated category, and let
F : K→E be a triangulated functor. Atriangulated left derived functor of F is
a triangulated left derived functor(LF,ηL) : D→E of F with respect toS, in the
sense of Deﬁnition 8.4.21.
Example 8.4.27.This is analogous to Example 8.4.17. We start with an additive
functor F 0 : M→N between abelian categories. We know how to extend it to a
DG functor
C−(F 0) : C−(M)→C−(N),
and this induces a triangulated functor
K−(F 0) : K−(M)→K−(N).
By composing withQ−
N we get a triangulated functor
(8.4.28) F := Q−
N◦K−(F 0) : K−(M)→D−(N).
DeﬁningK := K−(M), S := S+(M) and E := D−(N), we have a triangulated functor
F : K→E, and the situation is that of Deﬁnition 8.4.26.
Assume that the abelian category M has enough projectives. Deﬁne P to be
the full subcategory of K on the bounded above complexes of projective objects.
We will prove later (in Corollary 10.2.14 and Theorem 11.3.6) that properties (a)
and (b) of Theorem 8.4.23 hold in this situation. Therefore we have a left derived
functor
(8.4.29) (L−F,η−) : D−(M)→D−(N).
For anyP∈P the morphism
(8.4.30) η−
P : L−F (P )→F (P )
in E is an isomorphism.
Now assume the functorF 0 is right exact. ThenF 0 has the classical left derived
functors LqF 0 : M→N for allq≥0, andL0F 0∼=F 0. Formula (8.4.30) shows that
for everyM∈M there is an isomorphismLqF 0(M)∼= H−q(L−F (M)) in N. AsM
moves there is an isomorphismLqF 0∼= H−q◦L−F of additive functorsM→N.
160
Derived Categories | Amnon Yekutieli | 14 Apr 2019
In this example, as in Example 8.4.14, we were careful to use distinct notations
for the functorF 0 between abelian categories, and the induced triangulated functor
F = Q−
N◦K−(F 0). Later we will use the same notation forF 0 and F.
Remark 8.4.31. The reader might ask the following question at this point: Sup-
pose we are given additive functors
(8.4.32) L
F
− →M
G
− →N
between abelian categories, and the categoriesM and N have enough injectives, so
that the right derived functors
(8.4.33) D+(L) R+F //
R+(G◦F)
((
D+(M) R+G // D+(N)
exist (see Example 8.4.17 above). Does this diagram commute (up to an isomor-
phism of triangulated functors)? Similar questions can be asked about left derived
functors, etc.
Here is an answer. Assume thatF sends injectives inL to rightG-acyclic objects
of M. See Deﬁnition 16.1.3 (that talks about categories of graded modules, but
the ideas are the same). By Lemma 16.1.5 we know that for each bounded below
complex of rightG-acyclic objectsJ, the canonical morphismG(J)→R+G(J) in
D+(M)isanisomorphism. Therefore, foreveryboundedbelowcomplexofinjectives
I∈C(L), lettingJ :=F (I), we haveJ∼= R+F (I), and hence
R+(G◦F )(I)∼= (G◦F )(I) =G(F (I)) =G(J)∼= R+G(J)∼= R+G(R+F (I)).
Thus there is an isomorphism of triangulated functors
(8.4.34) R+(G◦F )∼= R+G◦R+F : D+(L)→D+(N).
The original application of the isomorphism (8.4.34), in [62, Proposition II.5.1],
was this: given morphisms of schemes X
f
− →Y
g
− →Z, the derived pushforward
functors satisfy
(8.4.35) R+(g∗◦f∗)∼= R+g∗◦R+f∗
as functors D+(X)→D+(Z). This is true because the functorf∗sends injective
OX-modules to ﬂasqueOY-modules.
This pleasant phenomenon seems to fail in some important situations that we
study in our book. For instance, take a noncommutative ringA and A-bimodules
S,T that are tilting complexes but not invertible bimodules (see Subsection 14.5).
Consider the abelian categories L = M = N := M(A) and the functors F :=
HomA(T,−) andG := HomA(S,−). It is quite likely that the functorsR+G◦R+F
and R+(G◦F ) are not isomorphic. A concrete instance in which this can be tested
is the ringA from Example 18.6.24, and the bimodulesS =T :=A∗there.
Remark 8.4.36. The composition of derived functors explained in the previous
remark is also related tospectral sequences. Given the input (8.4.32), in classical
homological algebra it was impossible to ask for something like the commutative
diagram (8.4.33). The best approximation was to have aconvergent spectral se-
quence
(8.4.37) Ei,j
k = RjG◦RiF⇒Rn(G◦F ).
Indeed, underthe assumption in theprevious remark (namely thatF sends injective
objects to rightG-acyclic objects), such a convergent spectral sequence does exist;
see [101, Chapters XI-XII], [129, Section 11] or [158, Section 5.7]. In the geometric
161
Derived Categories | Amnon Yekutieli | 14 Apr 2019
example above, for which the isomorphism (8.4.35) holds, this is theLeray spectral
sequence.
There are several kinds of spectral sequences, but basically they are all of the
same nature, i.e. approximations of the composition of derived functors.
Mosttraditionalapplicationsofspectralsequencesareperformedmoreeﬀectively
byﬁltrationsandtruncationsofcomplexes, ascanbeseeninSection12ofthisbook.
Still, there are a few instances in which spectral sequences cannot be left out, such
as theniveau spectral sequencein algebraic geometry (see [62, Chapter IV]), or its
noncommutative relative, thedouble Ext spectral sequencefor Auslander dualizing
complexes (see Remark 18.5.13 and the paper [183]).
