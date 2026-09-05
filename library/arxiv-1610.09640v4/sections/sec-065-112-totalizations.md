---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-065-112-totalizations
section_title: "Totalizations"
section_number: 11.2
pages: 187-200
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
(11.2.1) (M,∂) =
(
···→M−1 ∂−1
−−→M0 ∂0
−→M1→···
{
with entries in the abelian categoryCstr(A, M). This means that for eachi∈Z
there is a DG module(Mi, dMi)∈C(A, M), and a morphism∂i : Mi→Mi+1 in
Cstr(A, M), such that∂i+1◦∂i = 0. Recall that the strictness of∂i says that it has
degree 0, and that
(11.2.2) ∂i◦dMi = dMi+1◦∂i.
In terms of our symbolic notation, (M,∂) is an object of the DG category
C(Cstr(A, M)).
Each DG module(Mi, dMi) has its own internal structure:
(11.2.3) (Mi, dMi) =
(
{Mi,j}j∈Z,{dj
Mi}j∈Z
{
.
Here Mi,j ∈M, dj
Mi : Mi,j →Mi,j+1 is a morphism in M, and the relation
dj+1
Mi ◦dj
Mi = 0 holds. There is an action of the DG ringA onMi, prescribed by a
DGK-ring homomorphismfMi :A→EndM(Mi).
187
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Sometimes we viewM as a double complex, and then we refer to its rows and
columns: Mi is thei-th column ofM, and{Mi,j}i∈Z is itsj-th row. See diagram
(11.2.4).
(11.2.4) ... ... ...
···//M−1,1 ∂−1
//
OO
M0,1 ∂0
//
OO
M1,1 //
OO
···
···//M−1,0 ∂−1
//
d0
M−1
OO
M0,0 ∂0
//
d0
M0
OO
M1,0 //
d0
M1
OO
···
...
OO
...
OO
...
OO
As explained in Proposition 11.1.1, if the abelian categoryMhas countable direct
sums, then so doesCstr(A, M). Recall thatA♮is the underlying graded ring of the
DG ringA.
Deﬁnition 11.2.5.Assume that M has countable direct sums. Given a complex
(M,∂) with entries inCstr(A, M), with notation as in (11.2.1), itsdirect sum total-
ization is the object
Tot⊕(M,∂) =
(
Tot⊕(M), dTot
{
∈C(A, M)
deﬁned as follows, in four stages.
(1) There is a graded object
Tot⊕(M) :=
⨁
i∈Z
T−i(Mi)∈G(A♮, M).
(2) On each summand T−i(Mi) of Tot⊕(M) there is a diﬀerentialdT−i(Mi),
and we deﬁne the degree1 operator dM :=⨁
i∈Z dT−i(Mi) on Tot⊕(M).
(3) For eachi let
tot(∂)i := t−1
T−(i+1)(Mi+1)◦T−i(∂i) : T−i(Mi)→T−(i+1)(Mi+1).
We deﬁne the degree1 operator tot(∂) := ⨁
i∈Z tot(∂)i on the graded
object Tot⊕(M).
(4) The diﬀerentialdTot on the graded objectTot⊕(M) is dTot := dM + tot(∂).
For the deﬁnition to be valid we need to verify something:
Lemma 11.2.6. The degree1 operator dTot makes the pair
(
Tot⊕(M), dTot
{
into
an object ofC(A, M).
Proof. We have to check thatdTot◦dTot = 0 and thattot(∂) isA-linear. Below we
shall verify the ﬁrst condition; the second veriﬁcation is similar, and is left to the
reader.
For a giveni∈Z consider the composed morphism starting at the summand
T−i(Mi) of the total DG module:
T−i(Mi)
dTot
−−−→T−i(Mi)⊕T−(i+1)(Mi+1)
dTot
−−−→T−i(Mi)⊕T−(i+1)(Mi+1)⊕T−(i+2)(Mi+2).
188
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Let us view these direct sums as columns, with matrices of operators acting on
them from the left. So we have to calculate the matrix product
)
]
dT−i(Mi) 0
t−1◦T−i(∂i) d T−(i+1)(Mi+1)
0 t −1◦T−(i+1)(∂i+1)

[◦
)
dT−i(Mi)
t−1◦T−i(∂i)
[
The resulting column of operators hasdT−i(Mi)◦dT−i(Mi) = 0 in the ﬁrst position.
In the second position we have
(11.2.7) t−1◦T−i(∂i)◦dT−i(Mi) + dT−(i+1)(Mi+1)◦t−1◦T−i(∂i).
Using Proposition 4.1.12 we have
dT−(i+1)(Mi+1)◦t−1 =−t−1◦dT−i(Mi+1) =−t−1◦T−i(dMi+1).
Therefore (11.2.7) equals
t−1◦T−i(
∂i◦dMi−dMi+1◦∂i{
,
which is zero by (11.2.2). In the bottom of the column we have
(11.2.8) t−1◦T−(i+1)(∂i+1)◦t−1◦T−i(∂i).
According to Deﬁnition 4.1.6 we know that
T−(i+1)(∂i+1)◦t−1 = t−1◦T(T−(i+1)(∂i+1)) = t−1◦T−i(∂i+1)).
Therefore (11.2.8) equalst−1◦T−i(
∂i+1◦∂i{
= 0. □
Exercise 11.2.9. Finish the proof of the lemma (theA-linearity of tot(∂)).
Example 11.2.10. If Mi = 0 for i⁄=−1, 0, then
Tot⊕(M,∂) = Cone(∂−1 :M−1→M0),
the standard cone from Deﬁnition 4.2.1. In Proposition 11.2.13 there is a more
general statement.
In Deﬁnition 7.3.6 we talked about smart truncations of DG modules. Here is
another sort of truncations.
Deﬁnition 11.2.11.Let N be an abelian category. For a complexN∈C(N) its
stupid truncationsat an integerq are
stt≤q(N) :=
(
···→Nq−1→Nq→0→0→···
{
and
stt≥q(N) :=
(
···→0→0→Nq→Nq+1→···
{
.
These truncations ﬁt into a short exact sequence
(11.2.12) 0→stt≥q(N)→N→stt≤q−1(N)→0
in Cstr(N).
Warning: The stupid truncations do not apply to DG modulesN ∈C(B, N),
unless the DG ring B is a ring. However, in what follows we will use stupid
truncations in C(N), where N is the abelian category Cstr(A, M). This could be
a bit confusing.
Proposition 11.2.13. Let
(M,∂) =
(
···→M−1 ∂−1
−−→M0 ∂0
−→M1→0→···
{
be a complex with entries in the abelian categoryCstr(A, M), let
(M′,∂) :=
(
···→M−1 ∂−1
−−→M0→0→···
{
,
189
Derived Categories | Amnon Yekutieli | 14 Apr 2019
namely the stupid truncation ofM below 0, and letρ: Tot⊕(M′,∂)→M1 be the
morphism in Cstr(A, M) induced by∂0 :M0→M1. Then there is an isomorphism
(†) T
(
Tot⊕(M,∂)
{∼= Cone
(
−ρ: Tot⊕(M′,∂)→M1{
in Cstr(A, M).
Proof. By comparing translations we see that the objects on both sides of (†) match
ineachdegree. Likewiseforallthediﬀerentialsthatdonotinvolve ∂0. Acalculation
similar to that in the proof of Lemma 11.2.6 shows that there is a sign change there,
and this is why we need−ρon the right side of (†). □
Corollary 11.2.14. If, in the situation of Proposition 11.2.13, the DG module
Tot⊕(M,∂) is acyclic, thenρ: Tot⊕(M′,∂)→M1 is a quasi-isomorphism.
Proof. If Tot⊕(M,∂) is acyclic then so isT
(
Tot⊕(M,∂)
{
. The proposition implies
that−ρis a quasi-isomorphism. Thereforeρis a quasi-isomorphism. □
Deﬁnition 11.2.15.Let M∈C(A, M).
(1) A ﬁltrationon M is a direct system{Fj(M)}j≥−1 in Cstr(A, M) consisting
of subobjectsFj(M)⊆M, indexed by the interval[−1,∞]⊆Z.
(2) We say thatM = limj→Fj(M) if the direct limit exists, and the canonical
morphism limj→Fj(M)→M in Cstr(A, M) is an isomorphism.
(3) The ﬁltrationF induces, for eachj≥0, the subquotient
GrF
j (M) :=Fj(M)/Fj−1(M)∈C(A, M).
Our ﬁltrations will always be ascending. But sometimes they will be indexed by
a subinterval [j0,j 1] of [−1,∞]; and in this caseGrF
j (M) will be deﬁned only for
j∈[j0 + 1,j 1].
In the next proposition we takeM = M(K); but really all we need is thatM has
exact countable direct limits.
Recall that for a DGA-module M we denote byZ(M) the object of cocycles of
M. It is an object ofG(K).
Proposition 11.2.16.Let (M,∂) be a complex with entries in the abelian category
Cstr(A), with internal structure(11.2.3). Assume that the two conditions below hold:
(i) For everyj∈Z the complex
(
···→M−1,j ∂−1
−−→M0,j ∂0
−→M1,j→···
{
with entries inM(K) is acyclic.
(ii) There is somej1∈Z such that for allj≥j1 the complex
(
···→Zj(M−1)
∂−1
−−→Zj(M0)
∂0
−→Zj(M1)→···
{
with entries inM(K) is acyclic.
Then the DGA-module Tot⊕(M,∂) is acyclic.
Proof. The proof is done in two steps.
Step 1. Let us replace condition (ii) by the stronger condition:
(ii′) There is somej′
1∈Z such thatMi,j = 0 for allj >j′
1.
For everyi we introduce a ﬁltration{Fq(Mi)}q≥−1 on the DGK-module Mi as
follows:
Fq(Mi) := stt≥j′
1−q(Mi) =
(
···→0→Mi,j′
1−q dMi
− −− →Mi,j′
1−q+1→···
{
,
the stupid truncation abovej′
1−q. These ﬁltrations induces a ﬁltration on the DG
K-module Tot⊕(M,∂) :
Fq
(
Tot⊕(M)
{
:= Tot⊕(
···→Fq(M−1)
∂−1
−−→Fq(M0)
∂0
−→Fq(M1)→···
{
.
190
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We note thatF−1
(
Tot⊕(M)
{
= 0, and
(11.2.17)

q≥−1
Fq
(
Tot⊕(M)
{
= Tot⊕(M).
For everyq≥0 the DGK-module GrF
q
(
Tot⊕(M)
{
is isomorphic inCstr(K), up
to signs of diﬀerentials, to the complex in condition (i) with indexj =j′
1−q, so it
is acyclic. Forq =−1 we trivially have an acyclic DGK-module F−1
(
Tot⊕(M)
{
.
For everyq≥0 there is an exact sequence
0→Fq−1
(
Tot⊕(M)
{
→Fq
(
Tot⊕(M)
{
→GrF
q
(
Tot⊕(M)
{
→0
in Cstr(K). By induction onq we conclude thatFq
(
Tot⊕(M)
{
is acyclic. Finally,
by (11.2.17), and the fact that cohomology commutes with direct limits inCstr(K),
we see that the DG moduleTot⊕(M,∂) is acyclic.
Step 2. Now we assume conditions (i) and (ii). For eachi we introduce a ﬁltration
{Gq(Mi)}q≥0 on the DGK-module Mi as follows:
Gq(Mi) := smt≤j1+q(Mi) =
(
···→Mi,j1+q−1 dMi
− −− →Zj1+q(Mi)→0→···
{
,
the smart truncation belowj1 +q.
For every value ofq the complex
Gq(M) :=
(
···→Gq(M−1)
∂−1
−−→Gq(M0)
∂0
−→Gq(M1)→···
{
satisﬁes conditions (i) and (ii′), withj′
1 := j1 +q. Indeed, forj < j1 +q the j-th
row ofGq(M) is
(
···→M−1,j ∂−1
−−→M0,j ∂0
−→M1,j→···
{
,
and it is exact by condition (i). Forj =j1 +q its j-th row is
(
···→Zj(M−1)
∂−1
−−→Z(M0)
∂0
−→Zj(M1)→···
{
,
and it is exact by condition (ii). And forj >j1 +q thej-th row ofGq(M) is zero.
Therefore, by step 1, the DG moduleGq
(
Tot⊕(M)
{
:= Tot⊕(
Gq(M)
{
is acyclic.
Finally, sinceM = limq→Gq(M), it follows that
Tot⊕(M) = lim
q→
Gq
(
Tot⊕(M)
{
.
So Tot⊕(M) is acyclic. □
The second half of this subsection deals with products instead of direct sums. As
explained in Proposition 11.1.1, if the abelian categoryM has countable products,
then so doesCstr(A, M).
Deﬁnition 11.2.18.Assume that M has countable products. Given a complex
(M,∂) with entries inCstr(A, M), with notation as in (11.2.1), itsproduct totaliza-
tion is the object
TotΠ (M,∂) =
(
TotΠ (M), dTot
{
∈C(A, M)
deﬁned as follows, in four stages.
(1) There is a graded object
TotΠ (M) :=

i∈Z
T−i(Mi)∈G(A♮, M).
(2) On each factor T−i(Mi) of TotΠ (M) there is a diﬀerentialdT−i(Mi), and
we let dM :=∏
i∈Z dT−i(Mi), which is a diﬀerential onTotΠ (M).
191
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(3) For eachi let
tot(∂)i := t−1
T−(i+1)(Mi+1)◦T−i(∂i) : T−i(Mi)→T−(i+1)(Mi+1).
Wedeﬁnethedegree 1operator tot(∂) :=∏
i∈Z tot(∂)i onthegradedobject
TotΠ (M).
(4) The diﬀerentialdTot on the graded objectTotΠ (M) is dTot := dM + tot(∂).
Note that (ifM also has countable direct sums) there is a canonical embedding
(11.2.19) Tot⊕(M)⊆TotΠ (M)
in Cstr(A, M). In caseMi = 0 for|i|≫0, then this is an equality.
For Deﬁnition 11.2.18 to be valid we need to verify something:
Lemma 11.2.20.The degree1 operator dTot makes the pair
(
TotΠ (M), dTot
{
into
an object ofC(A, M).
Proof. This is the same calculation as in the proof of Lemma 11.2.6, heuristically
using the inclusion (11.2.19). □
Proposition 11.2.21. Let
(M,∂) =
(
···→0→M−1 ∂−1
−−→M0 ∂0
−→M1→···
{
be a complex with entries in the abelian categoryCstr(A, M), let
(M′,∂) :=
(
···→0→M0 ∂0
−→M1→···
{
,
namely the stupid truncation ofM above 0, and let ρ: M−1→TotΠ (M′,∂) be
the morphism in Cstr(A, M) induced by ∂−1 : M−1 →M0. Then there is an
isomorphism
TotΠ (M,∂)∼= Cone
(
ρ:M−1→TotΠ (M′,∂)
{
in Cstr(A, M).
Proof. Like the proof of Proposition 11.2.13, only now there are no sign issues.□
This directly implies:
Corollary 11.2.22. If, in the situation of Proposition 11.2.21, the DG module
TotΠ (M,∂) is acyclic, thenρ:M−1→TotΠ (M′,∂) is a quasi-isomorphism.
In Subsection 1.3 we discussed quotients in categories. They are dual to subob-
jects. Similarly, we now introduce a notion dual to a ﬁltration of an object.
Deﬁnition 11.2.23.Let M∈C(A, M).
(1) A coﬁltrationon M is an inverse system{Fj(M)}j≥−1 in Cstr(A, M) con-
sisting of quotientsM↠Fj(M), indexed by the interval[−1,∞]⊆Z.
(2) We say thatM = lim←jFj(M) if the inverse limit exists, and the canonical
morphism M→lim←jFj(M) in Cstr(A, M) is an isomorphism.
(3) The coﬁltrationF gives rise to the subquotients
GrF
j (M) := Ker
(
Fj(M)→Fj−1(M)
{
∈C(A, M).
Recall that for a DGA-module M we denote by Y(M) := M/ B(M); this is
the object of decocycles ofM, and it belongs to G(K). See Deﬁnition 3.2.4 and
equation 3.8.8.
Proposition 11.2.24.Let (M,∂) be a complex with entries in the abelian category
Cstr(A), with internal structure(11.2.3). Assume that the two conditions below hold:
192
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(i) For everyj∈Z the complex
(
···→M−1,j ∂−1
−−→M0,j ∂0
−→M1,j→···
{
with entries inM(K) is acyclic.
(ii) There is somej0∈Z such that for allj≤j0 the complex
(
···→Yj(M−1)
Yj(∂−1)
−−−−−→Yj(M0)
Yj(∂0)
−−−−→Yj(M1)→···
{
with entries inM(K) is acyclic.
Then the DGA-module TotΠ (M,∂) is acyclic.
Proof. The proof is divided into two steps.
Step 1. We replace condition (ii) by the stronger condition:
(ii′) There is somej′
0∈Z such thatMi,j = 0 for allj <j′
0.
For everyi we introduce a coﬁltration{Fq(Mi)}q≥−1 on the DGK-module Mi
as follows: Fq(Mi) := stt≤j′
0+q(Mi), the stupid truncation belowj′
0 +q. These
coﬁltrations induce a coﬁltration on the DGK-module TotΠ (M,∂) :
Fq
(
TotΠ (M)
{
:= TotΠ(
···→Fq(M−1)
∂−1
−−→Fq(M0)
∂0
−→Fq(M1)→···
{
.
We note thatF−1
(
TotΠ (M)
{
= 0, and
(11.2.25) lim
←q
Fq
(
TotΠ (M)
{
= TotΠ (M).
For everyq≥0 the DGK-module GrF
q
(
TotΠ (M)
{
is isomorphic in Cstr(K) to
the complex in condition (i) with indexj = j′
0 +q (up to a sign change of the
diﬀerentials), so it is acyclic. Forq =−1 we trivially have an acyclic DGK-module
F−1
(
TotΠ (M)
{
. For everyq≥0 there is an exact sequence
0→GrF
q
(
TotΠ (M)
{
→Fq
(
TotΠ (M)
{
→Fq−1
(
TotΠ (M)
{
→0
in Cstr(K). By induction onq we conclude thatFq
(
TotΠ (M)
{
is acyclic. Finally,
because the inverse system of complexes ofK-modules (11.2.25) has surjective tran-
sitions, the Mittag-Leﬄer argument (see Corollary 11.1.8) says that the DG module
TotΠ (M,∂) is acyclic.
Step 2. Here we assume conditions (i) and (ii). For eachiwe introduce a coﬁltration
{Gq(Mi)}q≥0 on the DGK-module Mi as follows:
Gq(Mi) := smt≥j0−q(Mi) =
(
···→0→Yj0−q(Mi)
dMi
− −− →Mi,j0−q+1→···
{
,
the smart truncation abovej0−q.
For eachq the complex
Gq(M) :=
(
···→Gq(M−1)
Gq(∂−1)
−−−−−→Gq(M0)
Gq(∂0)
−−−−→Gq(M1)→···
{
satisﬁes conditions (i) and (ii′), withj′
0 :=j0−q. Indeed, itsj-th row is
(
···→M−1,j ∂−1
−−→M0,j ∂0
−→M1,j→···
{
for j >j0−q; it is
(
···→Yj(M−1)
Yj(∂−1)
−−−−−→Y(M0)
Yj(∂0)
−−−−→Yj(M1)→···
{
forj =j0−q; and it is zero forj <j0−q. All these rows are exact. Therefore, by
step 1, the DG moduleGq
(
TotΠ (M)
{
:= TotΠ(
Gq(M)
{
is acyclic.
Finally, sinceM = lim←q Gq(M), it follows that
TotΠ (M) = lim
←q
Gq
(
TotΠ (M)
{
.
193
Derived Categories | Amnon Yekutieli | 14 Apr 2019
This is an inverse system of complexes ofK-modules with surjective transitions.
According to the Mittag-Leﬄer argument the limitTotΠ (M) is acyclic. □
11.3. K-Projective Resolutions inC−(M). Recall that M is aK-linear abelian
category, and C(M) is the DG category of complexes inM. The strict category
Cstr(M) is abelian.
The next deﬁnition is inspired by the work of B. Keller [79, Section 3.1].
Deﬁnition 11.3.1.Let P be an object ofC(M).
(1) A semi-projective ﬁltrationon P is a ﬁltrationF ={Fj(P )}j≥−1 on P as
an object ofCstr(M), such that:
•F−1(P ) = 0.
•Each GrF
j (P ) is a complex of projective objects ofM with zero diﬀer-
ential.
•P = limj→Fj(P ) in Cstr(M).
(2) The complexP is called asemi-projective complexif it admits some semi-
projective ﬁltration.
K-projective objects inC(M) were introduced in Deﬁnition 10.2.1.
Theorem 11.3.2. Let M be an abelian category, and letP be a semi-projective
complex in C(M). ThenP is K-projective.
Proof. The proof is in four steps.
Step 1. We start by proving that ifP = Tk(Q), the translation of a projective
object Q∈M, then P is K-projective. This is easy: given an acyclic complex
N∈C(M), we have
HomM(P,N ) = HomM
(
Tk(Q),N
{∼= T−k(
HomM(Q,N )
{
in Cstr(K). But HomM(Q,−) is an exact functorM→M(K), so HomM(Q,N ) is
an acyclic complex.
Step 2. NowP is a complex of projective objects ofM with zero diﬀerential. This
means thatP∼=⨁
k∈Z Tk(Qk) in Cstr(M), where eachQk is a projective object in
M. But then
HomM(P,N )∼=

k∈Z
HomM
(
Tk(Qk),N
{
in Cstr(K). This is an easy case of Proposition 1.8.6. By step 1 and the fact
that a product of acyclic complexes inCstr(K) is acyclic (itself an easy case of the
Mittag-Leﬄer argument), we conclude thatHomM(P,N ) is acyclic.
Step 3. Fix a semi-projective ﬁltrationF ={Fj(P )}j≥−1 on P. Here we prove
that for everyj the complexFj(P ) is K-projective. This is done by induction on
j≥−1. Forj =−1 it is trivial. Forj≥0 there is an exact sequence
(11.3.3) 0→Fj−1(P )→Fj(P )→GrF
j (P )→0
in Cstr(M). In each degreei∈Z the exact sequence
0→Fj−1(P )i→Fj(P )i→GrF
j (P )i→0
in Msplits, becauseGrF
j (P )i isaprojectiveobject. Thustheexactsequence(11.3.3)
is split exact in the abelian categoryGstr(M) of graded objects inM.
LetN∈C(M) be an acyclic complex. Applying the functorHomM(−,N ) to the
sequence of complexes (11.3.3) we obtain a sequence
(11.3.4)
0→HomM
(
GrF
j (P ),N
{
→HomM
(
Fj(P ),N
{
→HomM
(
Fj−1(P ),N
{
→0
194
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in Cstr(K). Because (11.3.3) is split exact inGstr(M), the sequence (11.3.4) is split
exact in Gstr(K). Therefore (11.3.4) is exact inCstr(K).
By the induction hypothesis the complexHomM
(
Fj−1(P ),N
{
is acyclic. By step
2 the complexHomM
(
GrF
j (P ),N
{
is acyclic. The long exact cohomology sequence
associated to (11.3.4) shows that the complexHomM
(
Fj(P ),N
{
is acyclic too.
Step 4. We keep the semi-projective ﬁltrationF ={Fj(P )}j≥−1 from step 3. Take
any acyclic complexN∈C(M). By Proposition 1.8.6 we know that
HomM(P,N )∼= lim
←j
HomM
(
Fj(P ),N
{
in Cstr(K). According to step 3 the complexesHomM
(
Fj(P ),N
{
are all acyclic. The
exactness of the sequences (11.3.4) implies that the inverse system{
HomM
(
Fj(P ),N
{}
j≥−1 in Cstr(K) has surjective transitions. Now the Mittag-
Leﬄer argument (Corollary 11.1.8) says that the inverse limit complexHomM(P,N )
is acyclic. □
Proposition 11.3.5. Let M be an abelian category. IfP ∈C(M) is a bounded
above complex of projectives, thenP is a semi-projective complex.
Proof. Say P is nonzero and sup(P ) = i1 ∈Z. For j ≥ −1 deﬁneFj(P ) :=
stt≥i1−j(P ), the stupid truncation above i1−j from Deﬁnition 11.2.11. Then
{Fj(P )}j≥−1 is a semi-projective ﬁltration onP. □
The next theorem is dual to [62, Lemma I.4.6(1)], in the sense of changing
direction of arrows. We give a detailed proof.
Theorem 11.3.6.Let M be an abelian category, and letP⊆M be a full subcategory
such that every objectM∈M admits an epimorphismP ↠ M from some object
P∈P. Then every complexM∈C−(M) admits a quasi-isomorphismρ:P→M
in C−
str(M), such thatsup(P ) = sup(M), and eachPi is an object ofP.
Proof. This is divided into steps.
Step 1. We can assume thatM ⁄= 0. After translating M, we can assume that
sup(M) = 0.
Step 2. Say the diﬀerential of the complex M is di
M : Mi →Mi+1. Let us
choose an epimorphismρ0 : P 0↠ M0 in M from some objectP 0∈P. We get
a morphism δ0 : M−1⊕P 0 →M0 whose components are d−1
M and−ρ0. Thus
Ker(δ0) = M−1×M0 P 0, the ﬁbered product. Next we choose an epimorphism
ψ−1 :P−1↠ Ker(δ0) from some objectP−1∈P. So there is an exact sequence
(11.3.7) P−1 ψ−1
− −− →M−1⊕P 0 δ0
−→M0→0.
The components ofψ−1 are denoted byρ−1 : P−1→M−1 and d−1
P : P−1→P 0.
We have this commutative diagram
(11.3.8) P−1
ρ−1

d−1
P //P 0
ρ0

// 0
M−2 d−2
M //M−1 d−1
M //M0 // 0
in M.
195
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Step 3. This is the inductive step. Here i≤−1, and we already have objects
Pi,...,P 0 in P, and morphismsρi,...,ρ0 and di
P,..., d−1
P , that ﬁt into this com-
mutative diagram
(11.3.9) Pi
ρi

di
P //Pi+1
ρi+1

//···
d−1
P //P 0
ρ0

// 0
Mi−1 di−1
M //Mi di
M //Mi+1 //···
d−1
M //M0 // 0
in M. Also dj+1
P ◦dj
P = 0 for allj in the interval[i,−1]
Deﬁne the morphismδi :Mi−1⊕Pi→Mi⊕Pi+1 to be the one with components
di−1
M ,−ρi and−di
P. Expressing direct sums of objects as columns, and letting
matrices of morphisms act on them from the left, we have this matrix representation
of δi :
(11.3.10) δi =
)
di−1
M −ρi
0 −di
P
[
.
So Ker(δi) =Mi−1×(Mi⊕Pi+1)Pi, the ﬁbered product.
Let us choose an epimorphismψi−1 :Pi−1↠ Ker(δi) from an objectPi−1∈P.
We get an exact sequence
(11.3.11) Pi−1 ψi−1
−−−→Mi−1⊕Pi δi
−→Mi⊕Pi+1.
The components of the morphismψi−1 are denoted byρi−1 : Pi−1→Mi−1 and
di−1
P :Pi−1→Pi. In matrix representation is
(11.3.12) ψi−1 =
)
ρi−1
di−1
P
[
.
In this way we obtain the slightly bigger diagram than (11.3.9):
(11.3.13) Pi−1
ρi−1

di−1
P //Pi
ρi

di
P //Pi+1
ρi+1

//···//P 0
ρ0

// 0
Mi−1 di−1
M //Mi di
M //Mi+1 //···//M0 // 0
Because δi◦ψi−1 = 0 in (11.3.11), it follows thatdi
P◦di−1
P = 0, and also
(11.3.14) ρi◦di−1
P = di−1
M ◦ρi−1,
showing that diagram (11.3.13) is commutative.
Step 4. We carry out the construction in step 3 inductively for alli≤−1, thus
obtaining a diagram like (11.3.13) that goes inﬁnitely to the left.
Letting Pi := 0 for positivei, the collectionP :={Pi}i∈Z becomes a complex,
with diﬀerentialdP :={di
P}i∈Z. By equation (11.3.14), the collectionρ:={ρi}i∈Z
is a strict morphism of complexesρ:P→M.
Step 5. It remains to prove thatρis a quasi-isomorphism.
Take anyi≤0. Let us examine this diagram:
(11.3.15) Pi−1 −ψi−1
//
(0,id)

Mi−1⊕Pi δi
//
id

Mi⊕Pi+1
id

Mi−2⊕Pi−1 δi−1
//Mi−1⊕Pi δi
//Mi⊕Pi+1
196
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Comparing the formula forδi−1 in (11.3.10) to the formula for−ψi−1 in (11.3.12),
we see that this diagram is commutative. An easy calculation using (11.3.14) shows
that δi◦δi−1 = 0. The top row is exact, because (up to signs) fori = 0 it is part
of the exact sequence (11.3.7), and fori≤−1 it is the exact sequence (11.3.11). It
follows that the bottom row is also exact.
Let N ={Ni}i∈Z be the complex with componentsNi := Mi−1⊕Pi for all
i. The diﬀerentialdN ={di
N}i∈Z is di
N :=−δi : Ni→Ni+1. We haveNi = 0
for i≥2. The exactness of the sequence (11.3.7) says thatH1(N) = 0, and the
exactness of the second row in (11.3.15) says thatHi(N) = 0 for i≤0. Hence
the complexN is acyclic. On the other hand, by the deﬁnition of the morphisms
δi in (11.3.10), we see thatN is just the standard cone on the strict morphism of
complexes T−1(ρ) : T−1(P )→T−1(M). See Deﬁnition 4.2.1. ThereforeT−1(ρ) is
a quasi-isomorphism, and so isρ. □
Example 11.3.16. Let (X,A) be a ringed space. Usually there aren’t enough
projective objects in the abelian categoryM(A) = ModA of sheaves ofA-modules
on X; but there are always enough ﬂat objects. A general method to produce ﬂat
sheaves is as follows. Given an open setU⊆X with inclusion mapg :U→X, the
extension by zero sheafg!(A|U) is a ﬂatA-module. Let us callg!(A|U) a pseudo-free
A-module of pseudo-rank1 and pseudo-supportU . Apseudo-freeA-module is, by
deﬁnition, a sheafP which is a direct sum of rank1 pseudo-freeA-modules (with
varying pseudo-supports). A pseudo-freeA-module is ﬂat, and everyA-moduleM
admits an epimorphismP↠M from some pseudo-freeA-moduleP. More on this
in [62, Proposition II.1.2] or [75, Proposition 2.4.12]. (Warning: in case(X,OX) is
a scheme, the pseudo-freeOX-modules are usually not quasi-coherent.)
Now letC(A) = C(ModA) be the category of complexes ofA-modules. Because
M(A) has enough ﬂat objects, Theorem 11.3.6 tells us that every complexM∈
C−(A) admits a quasi-isomorphismP→Mfrom a bounded above complex of ﬂat
A-modulesP. Similarly to Proposition 11.3.5 and Theorem 11.3.2, one can show
that such a complexP is K-ﬂat. The conclusion is that the subcategoryC−(A) has
enough K-ﬂat objects.
But in fact more is true: the category of unbounded complexesC(A) also has
enough K-ﬂat objects; see [143]. For an even more general statement see Remark
11.4.45 below.
Deﬁnition 11.3.17.Let M be an abelian category, and let M′⊆M be a full
abelian subcategory. We say thatM′has enough projectives relative toM if every
object M∈M′admits an epimorphismP↠M, whereP is an object ofM′that is
projective in the bigger categoryM.
Of course, ifM′has enough projectives relative toM then M′itself has enough
projectives.
Thick abelian categories were deﬁned in Deﬁnition 7.4.1. The next theorem is
the opposite of [62, Lemma I.4.6(3)].
Theorem 11.3.18.Let M be an abelian category, and letM′⊆M be a thick abelian
subcategory that has enough projectives relative toM. LetM∈C(M) be a complex
with bounded above cohomology, such thatHi(M)∈M′for all i. Then there is a
quasi-isomorphismρ:P→M in Cstr(M), whereP∈C−(M′), eachPi is projective
in M, and sup(P ) = sup(H(M)).
197
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. The proof of Theorem 11.5.8, reversed, works here. (Despite being located
later in the book, Theorem 11.5.8 is not logically dependent on the current the-
orem.) To be explicit, let us take N := Mop and N′:= M′op. Since monomor-
phisms in M become epimorphisms in N, and projective objects inM become in-
jective objects in N, the full abelian subcategoryN′⊆N satisﬁes assumptions of
Theorem 11.5.8. By Theorem 3.9.16 we have a canonical isomorphism of cate-
gories C+
str(N)
≃
− →C−
str(M)op that respects the cohomology functor. Thus a quasi-
isomorphism N →J in C+
str(N) gives rise to a quasi-isomorphism P →M in
C−
str(M). □
Corollary 11.3.19. If M is an abelian category with enough projectives, then
C−(M) has enough K-projectives.
Proof. According to either Theorem 11.3.6 or Theorem 11.3.18, everyM∈C−(M)
admits a quasi-isomorphismP→M from a bounded above complex of projectives
P. Now use Proposition 11.3.5 and Theorem 11.3.2. □
Corollary 11.3.20. Let M be an abelian category with enough projectives, and
let M ∈C(M) be a complex with bounded above cohomology. ThenM has a K-
projective resolutionP→M, such thatsup(P ) = sup(H(M)), and everyPi is an
projective object ofM.
Proof. We may assume that H(M) is not zero. Let i := sup(H(M))∈Z, and
take N := smt≤i(M), the smart truncation from Deﬁnition 7.3.6. ThenN→M
is a quasi-isomorphism and sup(N) = i. According to either Theorem 11.3.6 or
Theorem 11.3.18, there is a quasi-isomorphismP →N, whereP is a complex of
projectives andsup(P ) =i. By Proposition 11.3.5 and Theorem 11.3.2 the complex
P is K-projective. The composed quasi-isomorphismP→M is what we are looking
for. □
Corollary 11.3.21. Under the assumptions of Theorem 11.3.18, the canonical
functor D−(M′)→D−
M′(M) is an equivalence.
Proof. Consider the commutative diagram
K−(M′)M-prj F

Q

D−(M′) G // D−
M′(M) f.f. // D(M)
where K−(M′)M-prj is the homotopy category of bounded above complexes of objects
of M′that are projective in M. Since these are K-projective complexes inK(M),
the functorsF and Q are fully faithful, by Corollary 10.2.10. The functor marked
“f.f.” is the fully faithful inclusion of this full subcategory. We conclude that the
functor G is also fully faithful. The theorem tells us that the essential image ofG
is D−
M′(M). □
Here is an important instance where Theorem 11.3.18 and Corollary 11.3.21
apply.
Example 11.3.22.LetA be a left noetherian ring. Consider the abelian category
M := M(A) = ModA, and the thick abelian subcategoryM′:= Mf(A) = ModfA of
ﬁnitely generated modules. ThenM′has enough projectives relative toM. Theorem
11.3.18 tells us that ifM∈C(M) is a complex such that the modulesHi(M) are
all ﬁnitely generated, andHi(M) = 0 fori≫0, then there is a resolutionP→M,
198
Derived Categories | Amnon Yekutieli | 14 Apr 2019
where P is a bounded above complex of ﬁnitely generated projective modules.
Corollary 11.3.21 says that the canonical functor
D−(Mf(A)) = D−(M′)→D−
M′(M) = D−
f (M(A)) = D−
f (A)
is an equivalence. See Example 11.4.44 for another approach to this problem.
We end this subsection with a result on K-ﬂat complexes over rings.
Proposition 11.3.23. Let A be a ring andP a bounded above complex of ﬂat
A-modules. ThenP is a K-ﬂat complex.
Exercise 11.3.24. Prove this proposition. (Hint: see the proofs of Proposition
11.3.5 and Theorem 11.3.2.)
199
Derived Categories | Amnon Yekutieli | 14 Apr 2019
