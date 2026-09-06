---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI"
section_id: sec-047-71-localization-of-triangulated-categories
section_title: "Localization of Triangulated Categories"
section_number: 7.1
pages: 127-139
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
doc_brief: "Derived Categories | Amnon Yekutieli | 14 Apr 2019 DERIVED CATEGORIES AMNON YEKUTIELI — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by"
---
gory, with translation functorT. As we did in Section 6, we shall often writea∈K
for a morphisma∈K(M,N ) = HomK(M,N ), leaving the objects implicit.
Proposition 7.1.1. Suppose H : K→M is a cohomological functor, whereM is
some abelian category. Let
S :=
{
s∈K|H(Ti(s)) is invertible for alli∈Z
}
.
Then S is a left and right denominator set inK.
Proof. It is clear that S is closed under composition and contains the identity
morphisms. So it is a multiplicatively closed set.
Let’s prove that condition (RD1) of Deﬁnition 6.2.14 holds. Suppose we are given
morphisms L
a
− →N
s
← −M with s∈S. We need to ﬁnd morphismsL
t
← −K
b
− →M
with t∈S and such thata◦t =s◦b.
Consider the solid commutative diagram
K t //
b

L c◦a //
a

P //
=

T(K)
T(b)

M s //N c //P // T(M)
where the bottom row is a distinguished triangle built onM
s
− →N, and and the top
row is a distinguished triangle built onL
c◦a
−−→P, then turned 120◦to the right.
By axiom (TR3) there is a morphismb making the diagram commutative. Thus
a◦t =s◦b. SinceH(Ti(s)) are invertible for alli∈Z, it follows thatH(Ti(P )) = 0.
But thenH(Ti(t)) are invertible for alli∈Z, sot∈S.
Next we prove condition (RD2) of Deﬁnition 6.2.14. Because we are in an addi-
tive category, this condition is simpliﬁed: givena∈K ands∈S satisfyings◦a = 0,
we have to ﬁndt∈S satisfying a◦t = 0.
Say the objects involved areL
a
− →M
s
− →N. Take a distinguished triangle built
on s and then turned:P
b
− →M
s
− →N− →T(P ). We get an exact sequence
HomK(L,P )
b◦(−)
−−−−→HomK(L,M )
s◦(−)
−−−−→HomK(L,N ).
Sinces◦a = 0, there isc :L→P s.t.a =b◦c. Now look at a distinguished triangle
built onc, and then turned:K
t
− →L
c
− →P− →T(K). We know thatc◦t = 0; hence
a◦t =b◦c◦t = 0. But (s∈S)⇒(H(Ti(P )) = 0 for alli)⇒(t∈S).
The left versions (LD1) and (LD2) are proved the same way. □
Deﬁnition 7.1.2.Adenominator set of cohomological originin K is a denominator
set S⊆K that arises from a cohomological functorH, as in Proposition 7.1.1. The
morphisms in S are calledquasi-isomorphisms relative toH.
ThismaterialwillbepublishedbyCambridgeUniversityPressas Derived CategoriesbyAmnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works.c© Amnon Yekutieli, 2019.
127
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Theorem 7.1.3. Let (K, T) be a triangulated category, letS be a denominator set
of cohomological origin inK, and let (Q,τ) : ( K, T)→(KS, TS) be the T-additive
functor from Proposition6.3.8. Then the T-additive category(KS, TS) has a unique
triangulated structure such that these two properties hold:
(i) The pair (Q,τ) is a triangulated functor.
(ii) Suppose (K′, T′) is another triangulated category, and (F,ν) : ( K, T) →
(K′, T′) is a triangulated functor, such that F (s) is invertible for every
s∈S. Let (FS,νS) : ( KS, TS)→(K′, T′) be the T-additive functor from
Proposition 6.3.9. Then (FS,νS) is a triangulated functor.
This result is stated as [62, Proposition I.3.2] and as [75, Proposition 1.6.9]. Both
sources do not give proofs (just hints).
Proof. Since S is of cohomological origin we haveT(S) = S. Recall that the trans-
lation isomorphismτis the identity automorphism of the functorQ◦T; see Propo-
sition 6.3.8. So we will ignore it.
Step 1. The distinguished triangles inKS are deﬁned to be those triangles that are
isomorphic to the images underQ of distinguished triangles inK. Let us verify the
axioms of triangulated category.
(TR1). By deﬁnition every triangle that’s isomorphic to a distinguished triangle is
distinguished; and the triangleM
idM
−−→M →0→T(M) in KS is clearly distin-
guished.
Suppose we are given a morphism α: L →M in KS. We have to build a
distinguished triangle on it. Choose a fraction presentationα= Q(a)◦Q(s)−1.
Using condition (LD1) we can ﬁndb∈K and t∈S such thatt◦a =b◦s. These
ﬁt into the solid commutative diagram
L
α
$$
b %%
Ksoo a //M
tyy˜K
in K. (The dashed arrowαis in KS.)
Consider the solid commutative diagram below, where the rows are distinguished
triangles built ona and b respectively.
(7.1.4) K a //
s

M e //
t

N c //
u

T(K)
T(s)

L b // ˜K //P d // T(L)
By (TR3) there is a morphism u that makes the whole diagram commutative.
Sinces,t∈S andH is a cohomological functor, it follows thatu∈S. Applying the
functor Q to (7.1.4), and using the isomorphismQ(t) :M→˜K to replace ˜K with
M, we get the commutative diagram
K
Q(a) //
Q(s)

M
Q(e) //
Q(idM)

N
Q(c) //
Q(u)

T(K)
T(Q(s))

L α //M
Q(u◦e) //P
Q(d) // T(L)
128
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in KS. The top row is a distinguished triangle, and the vertical arrows are isomor-
phisms. So the bottom row is a distinguished triangle. This is the triangle we were
looking for.
(TR2). Turning: this is trivial.
(TR3). We are given the solid commutative diagram inKS, where the rows are
distinguished triangles:
(7.1.5) L α //
φ

M
β //
ψ

N
γ //
χ

T(L)
T(φ)

L′ α′
//M′ β′
//N′ γ′
// T(L′)
and we have to ﬁndχto complete the diagram.
By replacing the rows with isomorphic triangles, we can assume they come from
K. Thus we can replace (7.1.5) with this diagram:
(7.1.6) L
Q(α) //
φ

M
Q(β) //
ψ

N
Q(γ) //
χ

T(L)
T(φ)

L′Q(α′) //M′Q(β′) //N′Q(γ′) // T(L′)
in whichα,β,γ,α′,β′,γ′are morphisms inK. It is a commutative diagram. Let us
choose fraction presentationsφ= Q(a)◦Q(s)−1 and ψ= Q(b)◦Q(t)−1. Then the
solid diagram (7.1.6) comes from applyingQ to the diagram
(7.1.7) L α //M
β //N
γ // T(L)
˜L
a

s
OO
˜M
b

t
OO
T(˜L)
T(a)

T(s)
OO
L′ α′
//M′ β′
//N′ γ′
// T(L′)
in K. Here the rows are distinguished triangles inK; but the diagram might fail to
be commutative.
By axiom (RO3) we can ﬁndc∈K and u∈S s.t. Q(t)−1◦Q(α)◦Q(s) =
Q(c)◦Q(u)−1. This is the solid diagram below:
L α //M
˜L′′u′
// ˜L′ u //
c
;;˜L
a

s
OO
˜M
b

t
OO
L′ α′
//M′
Thus Q(α◦s◦u) = Q(t◦c). By (RO4) there is a morphismu′∈S s.t. (α◦s◦u)◦u′=
(t◦c)◦u′. We get
φ= Q(a)◦Q(s)−1 = Q(a◦u◦u′)◦Q(s◦u◦u′)−1
129
Derived Categories | Amnon Yekutieli | 14 Apr 2019
in KS. Thus, after substituting˜L := ˜L′′,s :=s◦u◦u′,a :=a◦u◦u′andc :=c◦u′,
we get a new diagram
(7.1.8) L α //M
β //N
γ // T(L)
˜L c //
a

s
OO
˜M
b

t
OO
T(˜L)
T(a)

T(s)
OO
L′ α′
//M′ β′
//N′ γ′
// T(L′)
in K instead of (7.1.7). In this new diagram the top left square is commutative; but
maybe the bottom left square is not commutative.
When we apply Q to the diagram (7.1.8), the whole diagram, including the
bottom left square, becomes commutative, since (7.1.6) is commutative. Again
using condition (RO4), there isv∈S s.t. (α′◦a)◦v = (b◦c)◦v. In a diagram:
L α //M
˜L′ v // ˜L
a

s
OO
c // ˜M
b

t
OO
L′ α′
//M′
Performing the replacements ˜L := ˜L′, s :=s◦v, c :=c◦v and a :=a◦v we now
have a commutative square also at the bottom left of (7.1.8). Sinceγ◦β= 0 and
γ′◦β′= 0, in fact the whole diagram (7.1.8) inK is now commutative.
Now by (TR1) we can embed the morphismc in a distinguished triangle. We
get the solid diagram
(7.1.9) L α //M
β //N
γ // T(L)
˜L c //
a

s
OO
˜M
˜β //
b

t
OO
˜N
˜γ //
d

w
OO
T(˜L)
T(a)

T(s)
OO
L′ α′
//M′ β′
//N′ γ′
// T(L′)
in K. The rows are distinguished triangles. Since˜γ◦˜β= 0, the solid diagram is
commutative. By (TR3) there are morphismsw anddthat make the whole diagram
commutative. Now by the long exact cohomology sequence (see Theorem 3.7.10)
the morphismw belongs to S. The morphismχ:= Q(d)◦Q(w)−1 :N→N′solves
the problem.
(TR4). We will not give any details, as this axiom is not an important feature for
us (see Remark 5.1.13). A proof can be found as part of the proof of [113, Theorem
2.1.8, page 97], where this axiom is called (TR4′).
Step 2. Suppose(F,ν) is a triangulated functor as in condition (ii). By Proposition
6.3.9 this extends uniquely to a T-additive functor(FS,νS). The construction of the
triangulated structure on(KS, TS) in the previous steps, and the deﬁning property
of the translation isomorphism νS in Proposition 6.3.9, show that (FS,νS) is a
triangulated functor.
130
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Step3. Atthispoint (KS, TS)isatriangulatedcategory, andconditions(i)-(ii)ofthe
theorem are satisﬁed. We need to prove the uniqueness of the triangulated structure
on (KS, TS). Condition (i) says that we can’t have less distinguished triangles than
those we declared. We can’t have more distinguished triangles, because of condition
(ii). □
Proposition 7.1.10. Consider the situation of Proposition 7.1.1 and Theorem
7.1.3.
(1) The cohomological functorH : K→M factors into H = HS◦Q, where
HS : KS→M is a cohomological functor.
(2) Let M be an object of K. The object Q(M) is zero in KS iﬀ the objects
H(Ti((M)) are zero inM for alli.
Proof.
(1) The existence and uniqueness of the functorHS are by the universal prop-
erty (Loc3) in Deﬁnition 6.1.2. We leave it as an exercise to show thatHS is a
cohomological functor.
(2) SinceHS is an additive functor, ifQ(M) = 0, then so isH(M) = HS(Q(M)).
And of courseQ(M) = 0 iﬀQ(Ti(M)) = 0 for alli.
For the converse, letφ: 0→M be the zero morphism inK. If H(Ti(M)) = 0
for alli, thenH(Ti(φ)) : 0→H(Ti(M)) are isomorphisms for alli. Then φ∈S,
and so Q(φ) : 0→Q(M) is an isomorphism inKS. □
Proposition 7.1.11. Let K be a triangulated category, letS be a denominator set
of cohomological origin inK, and letK′be a full triangulated subcategory ofK. Then
S′:= K′∩S is a denominator set of cohomological origin inK′, the Ore localization
K′
S′exists, and K′
S′is a triangulated category.
Proof. Let H : K→M be a cohomological functor that determinesS. The functor
H|K′: K′→M is also cohomological, and the set of morphismsS′satisﬁes
S′=
{
s∈K′|H|K′(Ti(s)) is an isomorphism for alli
}
.
Hence Proposition 7.1.1 and Theorem 7.1.3 apply. □
In the situation of the proposition, the localization functor is denoted byQ′:
K′→K′
S′.
Proposition 7.1.12. In the situation of Proposition7.1.11, letF : K′→E be a
triangulated functor into some triangulated categoryE. Assume that for everys∈
S′, the morphismF (s) is an isomorphism inE. Then there is a unique triangulated
functor FS′: K′
S′→E that extendsF; Namely FS′◦Q′=F as functors K′→E.
Proof. This is part of Theorem 7.1.3. □
In particular we can look at the functorF : K′inc
−−→K
Q
− →KS, and its extension
FS′: K′
S′→KS. We are interested in suﬃcient conditions for the functorFS′to be
fully faithful.
Proposition 7.1.13. Let K be a triangulated category, letS be a denominator set
of cohomological origin in K, and let K′⊆K be a full triangulated subcategory.
DeﬁneS′:= K′∩S. Assume either of these conditions holds:
(r) Let M ∈Ob(K). If there exists a morphism s : M →L in S with L∈
Ob(K′), there exists a morphismt :K→M in S with K∈Ob(K′).
(l) Let M ∈Ob(K). If there exists a morphism s : L→M in S with L∈
Ob(K′), there exists a morphismt :M→K in S with K∈Ob(K′).
Then the functorFS′: K′
S′→KS is fully faithful.
131
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. By Proposition 7.1.11, S′is a multiplicatively closed set of cohomological
origin. SobyProposition7.1.1itisarightandleftdenominatorsetin K′. According
to Proposition 6.2.34, under condition (r) the functorFS′is fully faithful.
For condition (l) we pass to the opposite categories, using Proposition 6.2.17.□
Remark 7.1.14. Let K be a triangulated category, and letN⊆K be a full trian-
gulated subcategory. DeﬁneS to be the set of morphismss in K such that the cone
of s (see Deﬁnition 5.3.7) is isomorphic to an object ofN. It turns out thatS is a
left and right denominator set inK. We callS the denominator set associated toN.
The localization KS is a triangulated category, and it is called theVerdier quotient
of K by N, with notationK/N := KS. See [156, Chapter 2] or [75, Section 1.6].
We want to relate this to Remark 5.3.25. Let˜S be a left and right denominator
set inK. A morphisms in K is called adivisor of ˜S if there exist morphismsu,v∈K
such thatu◦s and s◦v belong to ˜S. We call ˜S a saturated denominator setif it
contains all its divisors.
Let N⊆K be a full triangulated subcategory, and letS be the associated de-
nominator set, as in the ﬁrst paragraph. Let˜N be the saturated full triangulated
subcategory of K generated by N, in the sense of Deﬁnition 5.3.20. Let˜S be the
set of morphisms gotten by adjoining toS all its divisors. Then ˜S is a saturated
left and right denominator set of morphisms inK, the canonical functorKS→K˜S
is an isomorphism, the kernel of the localization functorQ : K→KS (see Corollary
5.3.23) is ˜N, and ˜S is the denominator set associated to˜N. This is proved in [156,
Chapter 2] and [76, Proposition 7.1.20].
An important example of a Verdier quotient is the passage from the homotopy
category K(A, M) to the derived category D(A, M), that we shall study in Sub-
section 7.2 below. Indeed, the set of quasi-isomorphismsS(A, M) in K(A, M) can
be described as the denominator set associated to the full subcategoryN(A, M)⊆
K(A, M) on the acyclic complexes, which is a saturated full triangulated subcate-
gory.
7.2. DeﬁnitionoftheDerivedCategory. Wenowspecializetothetriangulated
category K = K(A, M), for a central DGK-ring A and aK-linear abelian category
M.
Recall the cohomology functorH : Cstr(A, M)→Gstr(M) from Deﬁnition 3.2.4.
Lemma 7.2.1. Suppose φ,ψ: M →N are morphisms in Cstr(A, M) such that
ψ−φis a coboundary in HomA,M(M,N ). Then H(φ) = H( ψ), as morphisms
H(M)→H(N) in Gstr(M).
Exercise 7.2.2. Prove the lemma.
It follows that there is an induced functor
(7.2.3) H : K(A, M)→Gstr(M).
We shall be interested in its degree0component H0. Of course all other components
can be recovered fromH0 by the translation functor:Hi = H0◦Ti.
Proposition 7.2.4. Let M be an abelian category and letA be a DG ring. Then
the functor H0 : K(A, M)→M is cohomological.
Proof. Clearly H0 is additive. Consider a distinguished triangle
(7.2.5) L
α
− →M
β
− →N
γ
− →T(L)
in K(A, M). We must prove that
H0(L)
H0(α)
−−−−→H0(M)
H0(β)
−−−−→H0(N)
132
Derived Categories | Amnon Yekutieli | 14 Apr 2019
is an exact sequence inM.
By Deﬁnition 5.4.2 we can assume that the distinguished triangle (7.2.5) is the
image of a standard triangle inC(A, M). Namely thatN = Cone(α), the standard
cone associated toα, and the morphisms areβ= eαand γ= pα; see Deﬁnitions
4.2.1 and 4.2.5. To be explicit, in matrix notation we haveN =

M
T(L)

, dN =
dM α◦t−1
L
0 d T(L)

and β=

idM
0

.
Let us use the abbreviations ¯β:= H 0(β) and ¯α:= H 0(α). By Proposition
5.3.1 we know thatβ◦α= 0, and hence ¯β◦¯α= 0. It remains to prove that
the morphism ¯α: H 0(L)→Ker( ¯β) in M is an epimorphism. This will be done
using the ﬁrst sheaf trick (Proposition 2.4.9(3)): we will prove that given a section
¯m∈Γ(U, Ker( ¯β)) on an open setU ∈M, there is a reﬁnementV′↠ U and a
section ¯l∈Γ(V′, H0(L)) such that ¯α(¯l) = ¯m in Γ(V′, Ker( ¯β)). See Subsection 2.4
for the “geometric” terminology that’s used in the sheaf tricks.
Take some section ¯m∈Γ(U, Ker( ¯β)) on an open setU∈M. This means that
¯m ∈Γ(U, H0(M)) and ¯β( ¯m) = 0 . There is a covering V ↠ U and a section
m∈Γ(V, Z0(M)) such thatπM(m) = ¯m. Now
β(m) =
m
0

∈Γ(V, Z0(N))⊆Γ(V,N 0) =
Γ(V,M 0)
Γ(V,L 1)

in column notation. The vanishing of¯β( ¯m) =πN(β(m)) in Γ(V, H0(N)) means that
there is a coveringV′↠V and a sectionn∈Γ(V′,N−1) such thatdN(n) =β(m).
In column notation we haven =
m′
l

, withm′∈Γ(V′,M−1) and l∈Γ(V′,L 0).
The equalityβ(m) = dN(n) becomes the matrix equality
m
0

=
dM α
0 −dL

·
m′
l

=
dM(m′) +α(l)
−dL(l)

.
We see thatl∈Γ(V′, Z0(L)). Then the cohomology class¯l :=πL(l)∈Γ(V′, H0(L))
satisﬁes
¯α(¯l) =πM(α(l)) =πM(dM(m′) +α(l)) =πM(m) = ¯m
in Γ(V′, H0(M)), as required. □
Deﬁnition 7.2.6.A morphismφin K(A, M) is called aquasi-isomorphism if the
morphisms Hi(φ) in M are isomorphisms for alli. The set of quasi-isomorphisms
in K(A, M) is denoted byS(A, M).
By Proposition 7.2.4 the functorH0 is cohomological. According to Proposition
7.1.1, S(A, M)isadenominatorsetofcohomologicalorigin; soTheorem7.1.3applies
to it, and the next deﬁnition makes sense.
Deﬁnition 7.2.7.Let Mbe aK-linear abelian category andAa central DGK-ring.
The derived category of DGA-modules in M is theK-linear triangulated category
D(A, M) := K(A, M)S(A,M).
The corresponding triangulated localization functor is
Q : K(A, M)→D(A, M).
We also have the additive functorP : Cstr(A, M)→K(A, M) which sends a strict
morphism of DG modules to its homotopy class.
Deﬁnition 7.2.8.Let M be an abelian category and letA be a DG ring. Deﬁne
the functor
˜Q := Q◦P : Cstr(A, M)→D(A, M).
133
Derived Categories | Amnon Yekutieli | 14 Apr 2019
We thus get a commutative diagram of additive functors
(7.2.9) Cstr(A, M) P //
˜Q

K(A, M)
Q // D(A, M)
that are all the identity on objects.
It is sometimes convenient to describe morphisms inD(A, M) in terms of the
functor ˜Q. A morphism s∈Cstr(A, M) is called a quasi-isomorphism ifP(s) is a
quasi-isomorphism in K(A, M); i.e. ifH(s) is an isomorphism inGstr(M).
Proposition 7.2.10.
(1) Every morphismφin D(A, M) can be written as a right fractionφ= ˜Q(a)◦
˜Q(s)−1 wherea,s∈Cstr(A, M) and s is a quasi-isomorphism.
(2) Let a∈Cstr(A, M). Then ˜Q(a) = 0 in D(A, M) iﬀ there exists a quasi-
isomorphism s in Cstr(A, M) such thata◦s is a coboundary inC(A, M).
Proof.
(1) This is because of property (RO3) of Deﬁnition 6.2.1 and the fact thatP is full.
(2) Let us write ¯a := P(a)∈K(A, M). Since Q(¯a) = 0 , by Property (RO4) of
Deﬁnition 6.2.1 there is a quasi-isomorphism¯s∈K(A, M) such that ¯a◦¯s = 0 in
K(A, M). Choose a quasi-isomorphism s∈Cstr(A, M) such that ¯s = P(s). Then
P(a◦s) = 0, and this means thata◦s is a coboundary. □
Of course there is a left version of this proposition. The next deﬁnition is about
arbitrary (not necessarily linear) categories.
Deﬁnition 7.2.11.A functorF : C→D between categories is calledconserva-
tive if for every morphismφin C, φis an isomorphism if and only ifF (φ) is an
isomorphism.
By Proposition 7.1.10 the cohomology functor (7.2.3) extends uniquely to a func-
tor
(7.2.12) H : D(A, M)→Gstr(M).
Corollary 7.2.13. The functor H in (7.2.12) is conservative.
Proof. One implication is trivial. For the other implication, assume thatφis a
morphism in D(A, M) such that H(φ) is an isomorphism. We can write φas a
right fraction: φ= Q(a)◦Q(s)−1, where a∈K(A, M) and s∈S(A, M). Then
H(φ) = H(Q(a))◦H(Q(s))−1, and we see thatH(Q(a)) is an isomorphism. But
H(a) = H(Q(a)), so in facta∈S(A, M) too. Therefore Q(a) is an isomorphism in
D(A, M). It follows thatφis an isomorphism inD(A, M). □
Exercise 7.2.14. Here M = M(K), so K(A, M) = K(A). Show that the functor
H0 : K(A)→M(K) is corepresentable by the objectA∈K(A) (see Subsection 1.7).
Remark 7.2.15. This is a continuation of Remarks 3.8.22 and 6.2.38 on strictly
unital A∞categories. The base ringK is a ﬁeld. The references are [83] and [37].
Recall that ifA is an A∞category and B is a DG category, thenA∞Fun(A, B) is a
DG category.
Consider the special case is whenB = C(K), the DG category of complexes of
K-modules. An A∞functor M : A→C(K) is called an A∞A-module. The A∞
A-modules are the objects of the DG categoryC∞(A) := A∞Fun(A, C(K)). The
strict subcategory Str(C∞(A)), in the sense of Deﬁnition 3.4.6(1), is what most
texts call thecategory ofA∞A-modules.
134
Derived Categories | Amnon Yekutieli | 14 Apr 2019
A morphism φ: M →N in Str(C∞(A)) is called a quasi-isomorphism if for
every object x ∈Ob(A) the morphism φ(x) : M(x) →N(x) in Str(C(K)) =
Cstr(K) is a quasi-isomorphism. The localization of Str(C∞(A)) w.r.t. the quasi-
isomorphisms is thederived category ofA∞A-modules, denoted by D∞(A). (As
usual, the tradition is to callD∞(A) the “homotopy category” ofC∞(A), and to
denoteitby Ho(C∞(A)).) Thereisalocalizationfunctor Q : Str(C∞(A))→D∞(A).
We can also consider the categoryK∞(A) := H0(C∞(A)), see Deﬁnition 3.4.6(2).
There is a full functorP : Str(C∞(A))→K∞(A), and a commutative diagram
(7.2.16) Str(C∞(A)) P //
Q

K∞(A)
¯Q // D∞(A)
All three functors are the identity on objects. The categoriesK∞(A) and D∞(A)
are triangulated, and the functor¯Q is an isomorphism of triangulated categories.
Finally, letA be a DG category. Then the DG categoryC(A) of DG A-modules
embeds faithfully (but not fully) into the DG categoryC∞(A). The induced trian-
gulated functor D(A)→D∞(A) is an equivalence.
7.3. Boundedness Conditions in K(A, M). We continue with a central DGK-
ringA and aK-linear abelian categoryM. Boundedness conditions inC(A, M) were
introduced in Deﬁnition 3.8.20. Similarly:
Deﬁnition 7.3.1.We deﬁneK−(A, M), K+(A, M) and Kb(A, M) to be the full
subcategories ofK(A, M) consisting of bounded above, bounded below and bounded
DG modules respectively.
Of course Kb(A, M) = K−(A, M)∩K+(A, M). The subcategories K⋆(A, M), for
⋆∈{−, +, b}, are full triangulated subcategories ofK(A, M); this is because the
operations of translation and cone preserve the various boundedness conditions.
Note that K⋆(A, M) = Ho
(
C⋆(A, M)
{
. As the next example shows, sometimes the
categories C⋆(A, M) and K⋆(A, M) can be very degenerate.
Example 7.3.2. Let A be the DG ringK[t,t−1], the ring of Laurent polynomials
in the variablet of degree1, with the zero diﬀerential. IfM ={Mi}i∈Z is a nonzero
object of C(A, M), thenMi⁄= 0 for alli. Therefore the categories C⋆(A, M) and
K⋆(A, M) are zero for⋆∈{−, +, b}.
Let S⋆(A, M) := K⋆(A, M)∩S(A, M), the category of quasi-isomorphisms in
K⋆(A, M). As already mentioned, Theorem 7.1.3 applies here, so we can localize.
Deﬁnition 7.3.3.For⋆∈{−, +, b}we deﬁne
D⋆(A, M) := K⋆(A, M)S⋆(A,M),
the Ore localization ofK⋆(A, M) with respect toS⋆(A, M).
Here is another kind of boundedness condition.
Deﬁnition 7.3.4.For⋆∈{−, +, b}we deﬁneD(A, M)⋆to be the full subcategory
of D(A, M) on the complexesM whose cohomology H(M) is of boundedness type
⋆.
Of course D(A, M)⋆is a full triangulated subcategory ofD(A, M). See Remark
7.3.13 regarding Deﬁnitions 7.3.3 and 7.3.4.
Handling boundedness conditions requires the use oftruncations. These will be
introduced after the next proposition.
135
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proposition 7.3.5. Let 0 →L
φ
− →M
ψ
− →N →0 be a short exact sequence
in Cstr(A, M). Then there is a morphism θ: N →T(L) in D(A, M) such that
L
Q(φ)
−−−→M
Q(ψ)
−−−→N
θ
− →T(L) is a distinguished triangle inD(A, M).
Proof. We are following the proof of [75, Proposition 1.7.5]. Let˜N be the standard
cone on φ. In matrix notation, as in Deﬁnition 4.2.1, we have˜N =

M
T(L)

and
d ˜N =

dM φ◦t−1
0 d T(L)

. The object ˜N sits inside the standard triangleL
φ
− →M
˜ψ
− →˜N
˜χ
− →
T(L) in Cstr(A, M), where ˜ψ:=
id
0

and ˜χ:= [ 0 id ] in matrix notation. Deﬁne
the morphismγ= ˜N→N to be the matrixγ:= [ ψ0 ]. We get a commutative
diagram
L
φ //M
˜ψ //
ψ
##
˜N
˜χ //
γ

T(L)
N
in Cstr(A, M). We shall prove below that γis a quasi-isomorphism. Then the
morphism θ:= Q(˜χ)◦Q(γ)−1 :N→T(L) will work.
Let ˜K be the standard cone onidL, and let˜β: ˜K→˜N be the matrix morphism
φ0
0 id

:

L
T(L)

→

M
T(L)

. This ﬁts into a short exact sequence0→˜K
˜β
− →˜N
γ
− →
N →0 in Cstr(A, M). But the DG module ˜K is acyclic, and therefore γis a
quasi-isomorphism, as claimed. □
Deﬁnition 7.3.6.Let M∈C(M) and i∈Z. The smart truncation ofM below i
is the complex
smt≤i(M) :=
(
···→Mi−2 d
− →Mi−1 d
− →Zi(M)→0→···
{
.
The smart truncation ofM abovei is the complex
smt≥i(M) :=
(
···→0→Yi(M)
d
− →Mi+1 d
− →Mi+2→···
{
.
In the deﬁnition we use the objects of cocyclesZi(M)and decocyclesYi(M)from
Deﬁnition 3.2.4. Note thatsmt≤i(M) is a subcomplex ofM, whereas smt≥i(M)
a quotient complex ofM. Denoting the inclusion and the projection bye and p
respectively, we get a diagram
(7.3.7) smt≤i(M)
e
− →M
p
− →smt≥i+1(M)
in Cstr(M). This diagram is functorial inM∈Cstr(M). But diagram (7.3.7) is not
an exact sequence in general – there is a defect in degreei.
Recall that a DG ringA is called nonpositive ifAi = 0 for alli> 0.
Proposition 7.3.8. AssumeA is a nonpositive DG ring.
(1) The diﬀerential of everyM∈Cstr(A, M) is A0-linear.
(2) The smart truncations from Deﬁnition7.3.6 are functors fromCstr(A, M)
to itself.
Exercise 7.3.9. Prove this proposition.
Proposition 7.3.10. Assume A is nonpositive. For everyM∈C(A, M) there is
a distinguished triangle
smt≤i(M)
e
− →M
p
− →smt≥i+1(M)
θ
− →T(smt≤i(M))
in D(A, M). Also, Hj(e) : Hj(smt≤i(M))→Hj(M) is an isomorphism in M for
all j≤i, and Hj(p) : Hj(M)→Hj(smt≥i+1(M)) is an isomorphism inM for all
j≥i + 1.
136
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Proof. The claims aboutHj(e) and Hj(p) are trivial to verify. Now there is a short
exact sequence
(7.3.11) 0→smt≤i(M)
e
− →M
p′
−→N→0
in Cstr(A, M), where
N :=
(
···→0→Mi/ Zi(M)
d
− →Mi+1 d
− →Mi+2→···
{
.
According to Proposition 7.3.5 we get a distinguished triangle
smt≤i(M)
e
− →M
p′
−→N
θ′
−→T(smt≤i(M))
in D(A, M). Next, there is an obvious quasi-isomorphismφ:N→smt≥i+1(M) in
Cstr(A, M) such thatp =φ◦p′. We deﬁne the morphism
θ:=θ′◦Q(φ)−1 : smt≥i+1(M)→T(smt≤i(M))
in D(A, M). □
Proposition 7.3.12. Assume A is nonpositive. For ⋆∈{−, +, b}the canonical
functor D⋆(A, M)→D(A, M)⋆is an equivalence of triangulated categories.
Proof. It is done in four steps.
Step 1. Here we prove that the functorF−: D−(A, M)→D(A, M) is fully faithful.
Let s : M→L be a quasi-isomorphism inK(A, M) with L∈K−(A, M). Say L is
concentrated in degrees≤i. Then Hj(M) = Hj(L) = 0 for allj > i. The smart
truncation smt≤i(M) belongs to K−(A, M), and the inclusiont : smt≤i(M)→M
is a quasi-isomorphism. According to Proposition 7.1.13, withK = K(A, M) and
K′= K−(A, M), and with condition (r), we see thatF−is fully faithful.
Step 2. Here we prove that the functorF + : D+(M)→D(M) is fully faithful.
Let s : L→M be a quasi-isomorphism inK(A, M) with L∈K+(A, M). Say L is
concentrated in degrees≥i. Then Hj(M) = Hj(L) = 0 for allj < i. The smart
truncation smt≥i(M) belongs to K+(A, M), and the projectiont :M→smt≥i(M)
is a quasi-isomorphism. According to Proposition 7.1.13, with condition (l), we see
that F + is fully faithful.
Step 3. The arguments in step 1 we show thatDb(A, M)→D+(A, M) is fully faith-
ful. And by step 2,D+(A, M)→D(A, M) is fully faithful. ThereforeDb(A, M)→
D(A, M) is fully faithful.
Step 4. Smart truncation shows that the functorD⋆(A, M)→D(A, M)⋆is essen-
tially surjective on objects. □
Remark 7.3.13. Deﬁnition 7.3.3 withA =K, namely D⋆(M), is standard usage
of this notation – starting from [62, Section I.4], all the way to the recent book [76,
Deﬁnition 13.1.2]. An exception is [144, Deﬁnition tag=05RU].
On the other hand, deﬁnition 7.3.4 withA =K, namely D(M)⋆, is almost never
used (an exception is [120]).
We are going to require both distinct concepts,D⋆(A, M) and D(A, M)⋆, until
the end of Section 11. Beginning with Section 12, in Deﬁnition 12.1.6, the notation
D(A, M)⋆will be eliminated, andD⋆(A, M) will be redeﬁned to replace it.
137
Derived Categories | Amnon Yekutieli | 14 Apr 2019
7.4. Thick Subcategories ofM. We begin by recalling a deﬁnition about abelian
categories.
Deﬁnition 7.4.1.Let M be an abelian category. Athick abelian subcategoryof M
is a full abelian subcategoryN that is closed under extensions. Namely if
0→M′→M→M′′→0
is a short exact sequence inM with M′,M′′∈N, thenM∈N too.
Proposition 7.4.2.Let M be an abelian category, and letM′⊆M be a thick abelian
subcategory. SupposeM1→M2→N→M3→M4 is an exact sequence inM, and
the objectsMi belong M′. ThenN∈M′too.
Exercise 7.4.3. Prove this proposition.
Deﬁnition 7.4.4.Let M be an abelian category andN⊆M a thick abelian subcat-
egory. We denote byDN(M) the full subcategory ofD(M) consisting of complexes
M such that Hi(M)∈N for everyi.
Given a boundedness condition ⋆, we write D⋆
N(M) := DN(M)∩D⋆(M) and
DN(M)⋆:= DN(M)∩D(M)⋆.
Proposition 7.4.5. If N is a thick abelian subcategory ofM then DN(M) is a full
triangulated subcategory ofD(M).
Proof. Clearly DN(M) is closed under translations. Now suppose M′→M →
M′′∆
−−→is a distinguished triangle inD(M) such thatM′,M ∈DN(M); we have to
show thatM′′is also inDN(M). Consider the exact sequenceHi(M′)→Hi(M)→
Hi(M′′)→Hi+1(M′)→Hi+1(M). The four outer objects belong to N. Since
N is a thick abelian subcategory of M it follows (using Proposition 7.4.2) that
Hi(M′′)∈N. □
Example 7.4.6. Let A be a noetherian commutative ring. The categoryModfA
of ﬁnitely generated modules is a thick abelian subcategory ofModA.
Example 7.4.7. Consider ModZ = Ab. As above we have the thick abelian
subcategory Abf = ModfZ of ﬁnitely generated abelian groups. There is also the
thick abelian subcategory Abtors of torsion abelian groups (every element has a
ﬁnite order). The intersection of Abtors and Abf is the category Abﬁn of ﬁnite
abelian groups. This is also thick.
Example 7.4.8. Let X be a noetherian scheme (e.g. an algebraic variety over an
algebraically closed ﬁeld). Consider the abelian categoryModOX ofOX-modules.
In it there is the thick abelian subcategoryQCohOX of quasi-coherent sheaves, and
in that there is the thick abelian subcategoryCohOX of coherent sheaves.
Passing to complexes, let us write C(X) := C(ModOX), the DG category of
unbounded complexes. Its strict subcategory is Cstr(X), and for each bounded-
ness condition⋆we have the full subcategoryC⋆
str(X)⊆Cstr(X). For the derived
category we write D(X) := D(ModOX). Inside it there are the full triangulated
subcategories
Dc(X) := DCohOX (ModOX)⊆Dqc(X) := DQCohOX (ModOX).
One can show (see [62, Corollary II.7.19]) that the canonical functor
D+(QCohOX) →D+
qc(X) is an equivalence. The proof is based on the deep
fact (see [62, Theorem II.7.18]) that QCohOX has enough injectives relative to
ModOX, in the sense of Deﬁnition 11.5.7. Then Theorem 11.5.8 says that every
complexM∈D+
qc(X) admits a quasi-isomorphismM→Iin Cstr(X), whereI is
a bounded below complex of injective quasi-coherentOX-modules.
138
Derived Categories | Amnon Yekutieli | 14 Apr 2019
Then, using smart truncations and the fact that every quasi-coherent sheaf on
X is the direct limit of its coherent subsheaves, one can show that the canonical
functor Db(CohOX)→Db
c(X) is an equivalence. See [70, Proposition 3.5]; when
X = Spec(A) is aﬃne see also Proposition 7.4.9 below. The categoryDb
c(X) is
the focus of a signiﬁcant part of the research in modern algebraic geometry (e.g.
birational geometry, see [70]).
A totally diﬀerent approach yields this result: ifX is separated and quasi-
compact, then the canonical functor D(QCohOX)→Dqc(X) is an equivalence.
See [23, Corollary 5.5].
For a left noetherian ringA we write Df(ModA) := DModfA(ModA).
Proposition 7.4.9. Let A be a left noetherian ring and⋆∈{−, b}. Then the
canonical functorD⋆(ModfA)→Df(ModA)⋆is an equivalence of triangulated cat-
egories.
Proof. Consider the functorF : D−(ModfA)→D(ModA). Suppose s : M→L
is a quasi-isomorphism in K(ModA), such that L ∈K−(ModfA). Then M ∈
Df(ModA)−. A bit later (in Theorem 11.4.40) we will prove thatM admits a free
resolution P→M, whereP is a bounded above complex of ﬁnitely generated free
modules. Thus we get a quasi-isomorphismt :P→M with P∈K−(ModfA). By
Proposition 7.1.13 with condition (r) we conclude thatF is fully faithful. This also
shows that the essential image ofF is Df(ModA)−.
Next consider the functorG : Db(ModfA)→D−(ModfA). Suppose s : L→
M is a quasi-isomorphism in K−(ModfA) with L ∈Kb(ModfA). Say H(L) is
concentrated in the integer interval [d0,d 1]. Then t : M →smt≥d0(M) is a
quasi-isomorphism, and smt≥d0(M)∈Kb(ModfA). By Proposition 7.1.13 with
condition (l) we conclude that G is fully faithful. Therefore the composition
F◦G : Db(ModfA)→D(ModA) is fully faithful. Suitable truncations (smt≥d0
and smt≤d1) show that the essential image ofF◦G is Df(ModA)b. □
