---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-057-92-triangulated-bifunctors
section_title: "Triangulated Bifunctors"
section_number: 9.2
pages: 167-171
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
were deﬁned in Section 5.
Suppose (K1, T1)and (K2, T2)are T-additive categories (linear over the base ring
K). There are two induced translation automorphisms on the categoryK1×K2 :
(9.2.1) T1(M1,M 2) :=
(
T1(M1),M 2
{
and
(9.2.2) T2(M1,M 2) :=
(
M1, T2(M2)
{
.
These two functors commute:T2◦T1 = T1◦T2.
167
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Deﬁnition 9.2.3.Let (K1, T1), (K2, T2) and (L, T) be T-additive categories. A
T-additive bifunctor
(F,τ1,τ2) : (K1, T1)×(K2, T2)→(L, T)
is made up of an additive bifunctorF : K1×K2→L, as in Deﬁnition 9.1.2, together
with isomorphismsτi :F◦Ti
≃
− →T◦F of bifunctors K1×K2→L. The condition
is that
(†) τ1◦τ2 =−τ2◦τ1
as isomorphisms of bifunctors
F◦T2◦T1 =F◦T1◦T2
≃
=⇒T◦T◦F.
The reason for the sign appearing in condition (†) will become clear in the proof
of Lemma 9.2.14.
Let (F,τ1,τ2) be a T-additive bifunctor as in Deﬁnition 9.2.3. If we ﬁx an object
M1∈K1, then (
F (M1,−),τ2
{
: (K2, T2)→(L, T)
is a T-additive functor. Similarly if we ﬁx the second argument ofF.
In the next exercises we let the reader establish several operations on T-additive
bifunctors.
Exercise 9.2.4. In the situation of Deﬁnition 9.2.3, suppose(G,τ) : ( L, T)→
(L′, T′) is a T-additive functor into a fourth T-additive category(L′, T′). Write the
explicit formula for the T-additive bifunctor
(G,τ)◦(F,τ1,τ2) : (K1, T1)×(K2, T2)→(L′, T′).
This should be compared to Deﬁnition 5.1.4.
Exercise 9.2.5. In the situation of Deﬁnition 9.2.3, suppose
(F′,τ′
1,τ′
2) : (K1, T1)×(K2, T2)→(L, T)
is another T-additive bifunctor. Write the deﬁnition of a morphism of T-additive
bifunctors ζ: (F,τ1,τ2)→(F′,τ′
1,τ′
2). Use Deﬁnition 5.1.4 as a template.
Exercise 9.2.6. Give a deﬁnition of a T-additive trifunctor. Show that ifF and
G are T-additive bifunctors, thenG(−,F (−,−)) andG(F (−,−),−) are T-additive
trifunctors (whenever these compositions makes sense).
We now move to triangulated categories.
Deﬁnition 9.2.7.Let (K1, T1), (K2, T2) and (L, T) be triangulated categories. A
triangulated bifunctor
(F,τ1,τ2) : (K1, T1)×(K2, T2)→(L, T)
is a T-additive bifunctor that respects the triangulated structure in each argument.
Namely, for every distinguished triangle
L1
α1
−→M1
β1
−→N1
γ1
−→T1(L1)
in K1, and every objectL2∈K2, the triangle
F (L1,L 2)
F(α1,id)
−−−−−→F (M1,L 2)
F(β1,id)
−−−−−→F (N1,L 2)
τ1◦F(γ1,id)
−−−−−−−→T(F (L1,L 2))
in L is distinguished; and the same for distinguished triangles in the second argu-
ment.
168
Derived Categories | Amnon Yekutieli | 14 Apr 2019
The operations on triangulated bifunctors are the same as those on T-additive
bifunctors (see exercises above).
We now discuss triangulated bifunctors in our favorite setup: DG modules in
abelian categories. This is done both in the covariant and in the contravariant di-
rection, in either argument. Recall that the opposite homotopy categoryK(A, M)op
was given a canonical triangulated structure in Subsection 5.6.
Setup 9.2.8. We are given this data:
•DG ringsA1 and A2, and abelian categoriesM1 and M2.
•Direction indicators}1 and}2, that are either⟨empty⟩or op.
•Full subcategories Ci ⊆C(Ai, Mi), whose homotopy categories Ki :=
Ho(Ci)⊆K(Ai, Mi) are such that K♦i
i is a triangulated subcategory of
K(Ai, Mi)♦i.
The translation functor of the category K(Ai, Mi) is denoted by Ti, and the
translation functor of the categoryK(Ai, Mi)♦i is denoted byT♦i
i .
Deﬁnition 9.2.9.Under Setup 9.2.8, let L be another triangulated category. A
triangulated bifunctor from (K1, K2) to L that is contravariant in the ﬁrst or the
second argumentis, by deﬁnition, a triangulated bifunctor
(F,τ1,τ2) : (K♦1
1 , T♦1
1 )×(K♦2
2 , T♦2
2 )→(L, T)
as in Deﬁnition 9.2.7, where the contravariance is according to the direction indi-
cators}1 and}2.
Next we explain how to obtain triangulated bifunctors from DG bifunctors. This
is done in the following setup:
Setup 9.2.10. In addition to the data from Setup 9.2.8, we are given:
•A DG ringB and an abelian categoryN.
•A DG bifunctorF : C♦1
1 ×C♦2
2 →C(B, N).
The translation functor of the category K(B, N) is denoted by T. For every
object (M1,M 2)∈C1×C2 there are isomorphisms
(9.2.11) τi,M1,M2 :F (Ti(M1,M 2))
≃
− →T(F (M1,M 2))
in C(B, N), arising from Deﬁnition 4.4.1. Let us make this explicit (only fori = 2,
since the case i = 1 is similar). Fixing the object M1 we obtain a DG functor
G : C2→C(B, N), G(M2) :=F (M1,M 2). The isomorphism
τ2,M1,M2 :G(T2(M2))
≃
− →T(G(M2))
is then
(9.2.12) τ2,M1,M2 = tG(M2)◦G(tM2)−1.
We are using the little t operator here.
Lemma 9.2.13. Under Setups9.2.8 and 9.2.10, assume that the direction indica-
tors}1 and}2 are both⟨empty⟩. Fix i∈{1, 2}. Letting the object (M1,M 2) in
(9.2.11) vary, we get an isomorphismτi : F◦Ti
≃
− →T◦F of additive bifunctors
Str(C1)×Str(C2)→Cstr(B, N).
Proof. This is an almost immediate consequence of the fact that the little t opera-
tors are morphisms of functors (see Theorem 4.1.8(2)), □
According to Proposition 9.1.6, the DG bifunctorF induces an additive bifunctor
F : K♦1
1 ×K♦2
2 →K(B, N) on the homotopy categories.
169
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(9.2.15)
F (T1(M1), T2(M2))
F(t−1
M1
,id)
))
F(id,t−1
M2
)
uu
F (T1(M1),M 2)
tF(T1(M1),M2)

F(t−1
M1
,id)
))
F (M1, T2(M2))
tF(M1,T2(M2))

F(id,t−1
M2
)
uu
T(F (T1(M1),M 2))
T(F(t−1
M1
,id))

F (M1,M 2)
tF(M1,M2)
uu
tF(M1,M2)
))
T(F (M1, T2(M2))
T(F(id,t−1
M2
))

T(F (M1,M 2))
T(tF(M1,M2))
))
T(F (M1,M 2))
T(tF(M1,M2))
uu
T(T(F (M1,M 2)))
Lemma 9.2.14. Under Setups9.2.8 and 9.2.10, assume that the direction indica-
tors}1 and}2 are both⟨empty⟩. Then
(F,τ1,τ2) : K1×K2→K(B, N)
is a triangulated bifunctor.
Proof. The only challenge is to prove that(F,τ1,τ2) is a T-additive bifunctor; and
in that, all we have to prove is that condition (†) in Deﬁnition 9.2.2 holds, namely
that τ1◦τ2 =−τ2◦τ1. The rest hinges on single-argument considerations, that
were already handled in Theorems 4.4.3 and 5.5.1.
So let us prove the equality (†). Choose a pair of objects (M1,M 2). We have
diagram (9.2.15) in the categoryC(B, N). Going from top to bottom on the left
edge is the morphismτ1◦τ2, and going on the right edge is the morphismτ2◦τ1.
The bottom diamond is trivially commutative. The two triangles, with common
vertex atF (M1,M 2), are (−1)-commutative, because t : Id →T is a degree−1
morphism of DG functors. Since they occur on both sides, these signs cancel each
other. Finally, the top diamond is(−1)-commutative, because
(t−1
M1, id)◦(id, t−1
M2) = (t−1
M1, t−1
M2) =−(id, t−1
M2)◦(t−1
M1, id). □
Theorem 9.2.16. Under Setups 9.2.8 and 9.2.10, there are canonical translation
isomorphisms τ1 and τ2 such that
(F,τ1,τ2) : (K♦1
1 , T♦1
1 )×(K♦2
2 , T♦2
2 )→(K(B, N), T)
is a triangulated bifunctor.
Proof. Fori = 1, 2 let us deﬁne the indicator
♥i :=
{
ﬂip if}i = op,
⟨empty⟩if}i =⟨empty⟩.
We get DG categoriesC♥i
i : if }i =⟨empty⟩then C♥i
i = Ci⊆C(Ai, Mi), and if
}i = op then
C♥i
i = Cﬂip
i = Flip(Cop
i )⊆C(Ai, Mi)ﬂip = C(Aop
i , Mop
i ),
as in the proof of Theorem 5.6.10. Likewise there are triangulated categoriesK♥i
i .
170
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We start by composingF with the isomorphism of DG categoriesFlip−1 from
Theorem 3.9.16, in each coordinatei for which}i = op. This gives a new DG
bifunctor
F′: C♥1
1 ×C♥2
2 →C(B, N).
Now we can apply Lemma 9.2.14, to get a triangulated bifunctor
F′: K♥1
1 ×K♥2
2 →K(B, N).
Speciﬁcally, this means that we have a pair of translations (τ′
1,τ′
2) such that
(F′,τ′
1,τ′
2) is a triangulated bifunctor.
Finally we composeF′with the isomorphism of triangulated categoriesFlip from
formula (5.6.6), in each coordinatei for which}i = op. This recovers the original
bifunctor F on K♦1
1 ×K♦2
2 . There are translations τi, that are gotten from the
translations τ′
i like in the proof of Theorem 5.6.10. □
