---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-046-63-localization-of-linear-categories
section_title: "Localization of Linear Categories"
section_number: 6.3
pages: 123-127
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
rings as examples (see Examples 6.3.6 and 6.3.5). And in Section 7 we study
localization of triangulated categories. Here is a nonlinear example.
Example 6.2.35. Fix a base commutative ringK and a topological space (or,
more generally, a site)X. LetKX be the constant sheaf of ringsK onX. Consider
the category DGRng≤0
sc /KX of sheaves of commutative DGKX-rings on X (see
Deﬁnition 3.3.4 and Remark 12.8.22). For the sake of brevity let us just write
DGRngX := DGRng≤0
sc /KX.
The localization ofDGRngX with respect to the quasi-isomorphisms in it is called
thederived category of commutative DGKX-rings, and the notation isD(DGRngX).
The categorical localization functor isQ : DGRngX→D(DGRngX), and it is the
identity on objects. (The unfortunate tradition in homotopy theory is to call such
a localization the “homotopy category”, and to denote it by “Ho(DGRngX)”.)
As explained in the lecture notes [179], every DGKX-ringA admits a semi-
pseudo-free resolution ˜A→Ain DGRngX. The semi-pseudo-free DGKX-rings have
goodliftingproperties. Indeed, theybehavelikecoﬁbrantobjectsinaQuillenmodel
structure (even though there does not seems to be such a structure onDGRngX,
except whenX is a discrete space).
There is a congruence on the categoryDGRngX, called thequasi-homotopy re-
lation. (It turns out that this idea was already known to some homotopy theorists,
see Remark 6.2.37 below.) Let us denote byK(DGRngX) the homotopy category,
which is the quotient ofDGRngX modulo this congruence. So there is a functor
P : DGRngX→K(DGRngX), which is the identity on objects, and it sends a DG
ring homomorphism to its quasi-homotopy class.
The functors Q and P ﬁt into this commutative diagram:
(6.2.36) DGRngX
P //
Q

K(DGRngX)
¯Q // D(DGRngX)
The functor ¯Q is a faithful right Ore localization. The proof relies on the lifting
properties of semi-pseudo-free DGKX-rings. See Remark 12.8.22 for related mate-
rial.
Remark 6.2.37. Suppose C is a category, with a given multiplicatively closed set
of morphisms S⊆C. If C admits a Quillen model structure for which S is the
set ofweak equivalences, then there is automatically acalculus of fractionsfor the
localization functor Q : C→CS.
For instance, suppose that all objects ofC are ﬁbrant. In this case C is called
a category of ﬁbrant objects. Then there is a congruence relation H on C, and a
commutative diagram
C P //
Q

C/ H
¯Q // CS
in which, like in (6.2.36), the functorP is full, and the functor ¯Q is a right Ore
localization. These facts are explained in [115] (search for the emphasized text in
this remark).
123
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Remark 6.2.38. This is a continuation of Remark 3.8.22 on strictly unitalA∞
categories, and it is related to Example 6.2.35 and Remark 6.2.37 above, and to
Remark 12.8.21 below. The references are [83] and [37]. Recall that the base ring
K is a ﬁeld.
Let A and B be A∞categories, i.e. objects of the category A∞Cat. An A∞
functor F : A→B is called a quasi-equivalence if H(F ) : H( A)→H(B) is an
equivalence of graded categories. Thederived categoryof A∞Cat is the localization
D(A∞Cat) of A∞Cat with respect to the quasi-equivalences. (As mentioned above,
the tradition is to callD(A∞Cat) the “homotopy category” ofA∞Cat, and to denote
it by “Ho(A∞Cat)”.) There is a localization functorQ : A∞Cat→D(A∞Cat), which
is the identity on objects.
Suppose F,F′: A →B are A∞functors. So F and F′are objects of the
A∞category A∞Fun(A, B). We say thatF and F′are A∞homotopic if they are
isomorphic in the category H0(
A∞Fun(A, B)
{
, in which case we write F ≈F′.
DeﬁneK(A∞Cat) to be the quotient of A∞Cat modulo the relation≈. There is
a full functor P : A∞Cat→K(A∞Cat), which is the identity on objects. AnA∞
functorF : A→B is called anA∞equivalenceif it is an isomorphism inK(A∞Cat).
This means that there is anA∞functor G : B→A, such thatG◦F ≈IdA and
F◦G≈IdB. There is a commutative diagram
(6.2.39) A∞Cat P //
Q

K(A∞Cat)
¯Q // D(A∞Cat)
An important theorem (see [94, Theorem 9.2.0.4 ]) says that anA∞functor F
is a quasi-equivalence iﬀ it is anA∞equivalence. This implies that the functor¯Q
in diagram (6.2.39) is an isomorphism of categories.
It is worthwhile to mention that the categoryA∞Cat does not have a Quillen
model structure (for which the weak equivalences are the quasi-equivalences).
Let DGCat be the category of K-linear DG categories, where the morphisms
are the DG functors (see Deﬁnition 3.5.1). There is a fully faithful embedding
DGRng/cK →DGCat, since the DG rings (see Deﬁnition 3.3.2) are the single-
object DG categories. Because anA∞category whose higher operations vanish is
a DG category, there is a faithful (but not full) embeddingDGCat→A∞Cat. The
derived categoryof DGCat is the localization D(DGCat) of DGCat with respect to
the quasi-equivalences in it. (Once more, the traditional notation forD(DGCat) is
“Ho(DGCat)”.) The embedding ofDGCat into A∞Cat induces a functorD(DGCat)
→D(A∞Cat), and this is an equivalence. Together with the equivalence¯Q from
(6.2.39), this implies that every morphismF : A→B in D(DGCat) can be repre-
sented by anA∞functor ˜F : A→B, which is unique up to a unique isomorphism
in K(A∞Cat).
Moreover, the categoryD(DGCat) is symmetric monoidal, with tensor operation
A⊗B. It turns out that the DG categoryA∞Fun(A, B) is theinternal Hom object,
making D(DGCat) into aclosed monoidal category.
6.3. Localization of Linear Categories.Until now in this section we dealt with
arbitrary categories. In this subsection our categories will be linear over the com-
mutative base ringK (which will be implicit most of the time). See Convention
1.2.4.
For convenience we only talk about right denominator sets here. All the state-
ments hold equally for left denominator sets; cf. Remark 6.2.3 and Proposition
6.2.4.
124
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Theorem 6.3.1. Let A be aK-linear category, letS be a right denominator set in
A, and let(AS, Q) be the right Ore localization.
(1) The category AS has a uniqueK-linear structure, such thatQ : A→AS is
aK-linear functor.
(2) Suppose B is another K-linear category, and F : A →B is a K-linear
functor s.t. F (s) is invertible for everys∈S. Let FS : AS →B be the
localization ofF. ThenFS is aK-linear functor.
(3) If A is an additive category, then so isAS.
Proof.
(1) Letq1,q 2 : M→N be morphisms in AS. Choose common denominator pre-
sentations qi = Q(ai)◦Q(s)−1. Since Q must be an additive functor, we have to
deﬁne
(6.3.2) Q(a1) + Q(a2) := Q(a1 +a2).
By the distributive law (bilinearity of composition) we must deﬁneq1 + q2 :=
Q(a1 +a2)◦Q(s)−1. And forλ∈K we must deﬁneλ·qi := Q(λ·ai)◦Q(s)−1.
The usual tricks are then used to prove independence of representatives. For
instance, to prove that (6.3.2) is independent of choices, suppose thatQ(a1) =
Q(a′
1) and Q(a2) = Q(a′
2). Then, by (RO4), there aret1,t 2∈S such thata1◦t1 =
a′
1◦t1 anda2◦t2 =a′
2◦t2. By(RD1)thereexist b∈Aandv∈Ss.t.t1◦b =t2◦v. Let
t3 :=t2◦v∈S. Then (a1+a2)◦t3 = (a′
1+a′
2)◦t3, and henceQ(a1+a2) = Q(a′
1+a′
2).
In this wayAS is aK-linear category, andQ is aK-linear functor.
(2) The only option forFS is FS(qi) := F (ai)◦F (s)−1. The usual tricks are used
to prove independence of representatives.
(3) Clear from Propositions 2.5.2 and 2.5.7. □
Exercise 6.3.3. Finish the proofs of items (1) and (2) of the theorem.
Remark 6.3.4. Let A be a ring, which we can think of as a one-object linear
category A. In this context, Theorem 6.3.1 is one of the most important results in
noncommutative ring theory. See the books [106], [130] or [148].
Here are somewhat concrete examples.
Example6.3.5. SupposeAisanoncommutativering(i.e.itisnotnecessarilycom-
mutative), andS is a central multiplicatively closed set inA(i.e.S⊆Cent(A)). Be-
cause the elements ofS commute with all elements ofA, the denominator conditions
hold automatically. We get a left and right Ore localization of ringsQ :A→AS.
Note that ifS contains a nilpotent element, then the ringAS is trivial.
The last observation should serve as a warning: localization can sometimes kill
everything. Fortunately, the localization procedure that gives rise to the derived
category does not cause any catastrophe, as we shall see in Proposition 7.1.10.
Example 6.3.6. Suppose A is a noncommutative ring that is both noetherian
and an integral domain (i.e. the only zero-divisor inA is 0). Let S be the set of
nonzero elements ofA. ThenS is both a left and a right denominator set. See [106,
Theorem 2.1.15].
Remark 6.3.7. Suppose A is a ring andS is a right denominator set in it. Then
the right Ore localizationAS is ﬂatas leftA-module. See [130, Theorem 3.1.20].
We have no idea if something like this is true for linear categories with more than
one object.
Proposition 6.3.8. Let (K, T) be a T-additive category, letS be a right denomi-
nator set inK such that T(S) = S, and letQ : K→KS be the localization functor.
125
Derived Categories | Amnon Yekutieli | 14 Apr 2019
(1) There is a unique additive automorphismTS of the categoryKS, such that
TS◦Q = Q◦T as functors K→KS.
(2) Let τbe the identity automorphism of the functor Q◦T. Then (Q,τ) :
(K, T)→(KS, TS) is a T-additive functor.
Proof.
(1) By the assumption the functor Q◦T : K →KS sends the morphisms in S
to isomorphisms. By the property (Loc3) of localization in Deﬁnition 6.1.2, the
functor TS : KS→KS satisfying TS◦Q = Q◦T exists and is unique. Similarly,
there is a unique functorT−1
S : KS→KS satisfying T−1
S ◦Q = Q◦T−1. An easy
calculation shows thatT−1
S ◦TS = Id = T S◦T−1
S . Hence TS is an automorphism
of KS. By Theorem 6.3.1 the functorTS is additive.
(2) This is clear. □
The composition of T-additive functors was deﬁned in Deﬁnition 5.1.4.
Proposition 6.3.9. In the situation of Proposition6.3.8, suppose (K′, T′) is an-
other T-additive category, and(F,ν) : ( K, T)→(K′, T′) is a T-additive functor,
such thatF (s) is invertible for everys∈S. LetFS : KS→K′be the localized func-
tor. Then there is a unique isomorphismνS :FS◦TS
≃
− →T′◦FS of functorsKS→K′,
such that (F,ν) = (FS,νS)◦(Q,τ) as T-additive functors(K, T)→(K′, T′).
Exercise 6.3.10. Prove Proposition 6.3.9.
126
Derived Categories | Amnon Yekutieli | 14 Apr 2019
7. The Derived Category D(A, M)
In this section we introduce the main mathematical concept of the book: the
derived category D(A, M) of DG A-modules in M. Here A is a central DG K-
ring, and M is aK-linear abelian category. The base ringK can be any nonzero
commutative ring, and it will remain implicit most of the time.
