---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-118-18-rigid-noncommutative-dualizing-complexes
section_title: "Rigid Noncommutative Dualizing Complexes"
section_number: 18
pages: 411-418
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
In this section of the book we are going to work with noncommutative (namely
not necessarily commutative) rings. We shall often use the abbreviation “NC” for
“noncommutative”. The goal is to introduce rigid NC dualizing complexes in the
sense of M. Van den Bergh [153], and to prove their existence and uniqueness under
certain conditions.
18.1. Noncommutative Dualizing Complexes. Here we will deﬁne NC dual-
izing complexes over a NC ring A. The deﬁnition is almost identical to that in
the NC graded setting (see Subsection 17.1). We will prove that the NC dualizing
complexes over A are parameterized by the derived Picard group of A. The content
of this subsection is adapted from the paper [165].
Let K be a commutative ring. Recall (from Deﬁnition 1.2.1) that a central K-ring
is a ring A equipped with a ring homomorphism K →Cent(A), where Cent(A) is
the center of A. In more traditional texts, a central K-ring is called an associative
unital K-algebra. The category of central K-rings, with K-ring homomorphisms, is
denoted by Rng/c K.
Here is the convention that is in force throughout this section:
Convention 18.1.1. There is a base ﬁeld K. All rings are by default central K-
rings, and all homomorphisms between K-rings are over K; namely we work within
the category Rng/c K. All bimodules are K-central, and all additive functors are
K-linear. We use the notation ⊗for ⊗K. For a ring A we write Aen := A ⊗Aop,
the enveloping ring of A.
See Remark 18.1.30 regarding the assumption that the base ring K is a ﬁeld.
Recall that a NC ring A is called noetherian if it is both left noetherian and right
noetherian. See Remark 15.1.30 regarding the failure of the noetherian property to
be preserved under ﬁnitely generated ring extensions.
Let A be a ring. As before, M(A) is the category of left A-modules. The category
of right A-modules is M(Aop), and the category of A-bimodules is M(Aen). Given
another ring B, the category of A-B-bimodules is M(A ⊗Bop). These are K-linear
abelian categories.
The derived category of M(A) is D(A) := D(M(A)); its objects are the com-
plexes of (left) A-modules. The other derived categories are D(Aop) := D(M(Aop)),
D(Aen) := D(M(Aen)) and D(A ⊗Bop) := D(M(A ⊗Bop)).
Consider the canonical ring anti-automorphism op : B →Bop, that is the iden-
tity on the underlying K-module. There is a canonical ring isomorphism
(18.1.2)
A ⊗Bop
≃
−→Bop ⊗A,
a ⊗op(b) 7→op(b) ⊗a.
The
induced
isomorphism
on
the
bimodule
categories
M(A ⊗Bop)
≃
−→
M(Bop ⊗A) is the identity on the underlying K-modules. Indeed, for M ∈M(A ⊗
Bop), m ∈M and a ⊗op(b) ∈A ⊗Bop, we have (op(b) ⊗a)·m = a·m·b =
(a ⊗op(b))·m. Now take B = A in (18.1.2). Since (Aop)op = A, there is a canoni-
cal ring isomorphism
(18.1.3)
Aen = A ⊗Aop
≃
−→Aop ⊗A = (Aop)en
and an induced isomorphism on the bimodule categories
(18.1.4)
M(Aen)
≃
−→M((Aop)en).
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
411
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
All these categorical relations pass to derived categories.
The ring Aen is isomorphic to its opposite ring. There is a ring isomorphism
(18.1.5)
trop : Aen
≃
−→(Aen)op
with this formula: for a1, a2 ∈A it sends the element a1 ⊗op(a2) ∈Aen to
(18.1.6)
trop(a1 ⊗op(a2)) := op(a2 ⊗op(a1)) ∈(Aen)op.
On the underlying K-module A⊗A this is just the transposition a1 ⊗a2 7→a2 ⊗a1,
and hence the name “transpose opposite” and the acronym “trop”.
Usually an A-A-bimodule M is seen as a left Aen-module, with this action of an
element a1 ⊗op(a2) ∈Aen on an element m ∈M :
(18.1.7)
(a1 ⊗op(a2))·m = a1·m·a2.
But using the ring isomorphism trop from formula (18.1.5) we can also consider
M as a left (Aen)op-module, and thus as a right Aen-module. Explicitly, the right
action of an element a2 ⊗op(a1) ∈Aen on an element m ∈M is:
(18.1.8)
m·(a2 ⊗op(a1)) =♥op(a2 ⊗op(a1))·m
=† (a1 ⊗op(a2))·m =♦a1·m·a2.
In equality =♥we move from a right action by Aen to the left action by (Aen)op,
and in equality =† we made use of formula (18.1.6) to move from (Aen)op to Aen.
Finally, the equality =♦is formula (18.1.7). This game of musical chairs will be
played in Subsections 18.5 and 18.2.
Let A and B be rings. The canonical ring homomorphisms
A →A ⊗Bop ←Bop
induce restriction functors
(18.1.9)
D(A)
RestA
←−−−−D(A ⊗Bop)
RestBop
−−−−−→D(Bop).
See the commutative diagram 14.2.3. We shall usually keep these restriction func-
tors implicit, and instead use terminology like in Deﬁnition 14.2.18.
In Deﬁnition 12.5.1 we introduced this notation: for a ring A we denote by Mf(A)
the full subcategory of M(A) on the ﬁnite (i.e. ﬁnitely generated) A-modules. And
Df(A) is the full subcategory of D(A) on the complexes of A-modules M such that
Hi(M) ∈Mf(A) for every i.
If A is left noetherian, then Mf(A) is a thick abelian subcategory of M(A); and
hence Df(A) is a full triangulated subcategory of D(A). As usual we can combine
indicators: D⋆
f (A) := Df(A) ∩D⋆(A), where ⋆is some boundedness indicator (+,
−, b or ⟨empty⟩).
Now to ﬁniteness of A-B-bimodules. The expression M(f,..)(A ⊗Bop) denotes
the full subcategory of M(A ⊗Bop) on the bimodules that are ﬁnite over A; and
the expression M(..,f)(A ⊗Bop) denotes the full subcategory on the bimodules that
are ﬁnite over Bop. Of course we deﬁne
M(f,f)(A ⊗Bop) := M(f,..)(A ⊗Bop) ∩M(..,f)(A ⊗Bop).
The same notation shall apply to derived categories.
To a complex of bimodules M ∈D(A ⊗Bop) we associated two derived homo-
thety morphisms in Subsection 14.4. Let us recall them. The derived homothety
morphism through Bop is the morphism
(18.1.10)
hmR
M,Bop : B →RHomA(M, M)
in D(Ben); and the derived homothety morphism through A is the morphism
(18.1.11)
hmR
M,A : A →RHomBop(M, M)
412
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
in D(Aen). According to Deﬁnition 14.4.14, the complex M has the noncommuta-
tive derived Morita property on the A side (resp. on the Bop side) if the morphism
hmR
M,Bop (resp. hmR
M,A) is an isomorphism.
Deﬁnition 18.1.12 ([165]). Let A be a noetherian ring. A noncommutative du-
alizing complex over A is an object R ∈Db(Aen) satisfying the following three
conditions:
(i) For every p the A-bimodule Hp(R) is ﬁnite over A and over Aop.
(ii) The complex R has ﬁnite injective dimension over A and over Aop.
(iii) The complex of bimodules R has the noncommutative derived Morita prop-
erty on both sides.
Note that conditions (i) and (ii) are one-sided, namely they refer separately to
RestA(R) ∈D(A) and to RestAop(R) ∈D(Aop); whereas condition (iii) is more
complicated, and we will study it further in Lemma 18.1.21 below. Also note that
condition (i) can be stated as “R belongs to D(f,f)(Aen)”.
Before going on, we need to say something about the op-symmetry of Deﬁnition
18.1.12. Given a complex R ∈D(Aen), by formula (18.1.4) the complex R is also
an object of D((Aop)en), and we could ask whether R is a dualizing complex over
the ring Aop. The answer is positive of course, because all three conditions are
op-symmetric. We record this fact as the next proposition.
Proposition 18.1.13. If R is a NC dualizing complex over A, then R is also a
NC dualizing complex over Aop.
Example 18.1.14. A NC ring A is called regular if it has ﬁnite global cohomological
dimension on both sides. This is very similar to the graded deﬁnition (see Deﬁnition
15.4.1). Let us recall what it means: there is some natural number d such that
Exti
A(M, N) = 0 for all i > d and all M, N ∈M(A); and also Exti
Aop(M ′, N ′) = 0
for all i > d and all M ′, N ′ ∈M(Aop). The smallest such number d is the global
cohomological dimension of A.
Such rings are easy to ﬁnd; for instance, if K is a ﬁeld, and g is ﬁnite Lie
algebra over K, then the universal enveloping ring A := U(g) is regular; the global
cohomological dimension of A is d := rankK(g).
A weaker condition is this: A is called Gorenstein if A has ﬁnite injective dimen-
sion both as a left module and as a right module over itself. Namely there is some
natural number d such that Exti
A(M, A) = 0 for all i > d and all M ∈M(A); and
also Exti
Aop(M ′, A) = 0 for all i > d and all M ′ ∈M(Aop).
Assume A is Gorenstein. Then the complex of bimodules R := A satisﬁes con-
dition (ii) of Deﬁnition 18.1.12. Conditions (i) and (iii) of this deﬁnition are auto-
matically true. We conclude that R := A is a NC dualizing complex over itself.
Deﬁnition 18.1.15. Let A be a noetherian ring, let R be a NC dualizing complex
over A, and let B be a second ring. The duality functors associated to R are the
triangulated functors
DA : D(A ⊗Bop)op →D(B ⊗Aop),
DA := RHomA(−, R)
and
DAop : D(B ⊗Aop)op →D(A ⊗Bop),
DAop := RHomAop(−, R).
Notice that the expressions DA and DAop leave R and B implicit; this is because
the dualizing complex R is taken to be ﬁxed, and the second ring B is less important.
The NC derived Hom-evaluation morphisms were already discussed in Subsection
17.1, in the algebraically graded context. The nongraded deﬁnition is very similar.
Given a complex M ∈D(A ⊗Bop), there is a morphism
(18.1.16)
evR,R
M
: M →DAop(DA(M)) = RHomAop RHomA(M, R), R

413
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
in D(A ⊗Bop), which is functorial in M. If we choose a K-injective resolution
R →I in D(Aen), then we have an isomorphism
DAop(DA(M)) ∼= HomAop HomA(M, I), I

in D(A ⊗Bop), and the morphism evR,R
M
is represented by the Hom-evaluation
homomorphism
evM,I : M →HomAop HomA(M, I), I

in Cstr(A⊗Bop). For this we use the results of Subsection 14.3, that apply because
A and B are ﬂat over K.
In the special case when B = A and M = A, the morphism evR,R
A
recovers the
derived homothety morphism through A, see (18.1.11); i.e.
(18.1.17)
hmR
R,A = evR,R
A
: A →RHomAop(R, R)
in D(Aen). This formula makes implicit use of the left co-unitor isomorphism lcu :
RHomA(A, R)
≃
−→R in D(Aen). Likewise for the homothety morphism hmR
R,Aop.
Theorem 18.1.18. Let A be a noetherian ring, let R be a NC dualizing complex
over A, let B be a second ring, and let DA and DAop be the duality functors asso-
ciated to R. Let ⋆be a boundedness indicator, and let M ∈D⋆
(f,..)(A ⊗Bop). Then
the following hold:
(1) The complex DA(M) belongs to D−⋆
(..,f)(B ⊗Aop), where −⋆is the reversed
boundedness indicator.
(2) The derived Hom-evaluation morphism evR,R
M
: M →DAop(DA(M)) in
D(A ⊗Bop) is an isomorphism.
Proof. The proof is the same as that of Theorem 17.1.6, with the obvious modiﬁ-
cations (i.e. neglecting the algebraic grading). It all boils down to Theorems 12.5.7
and 12.5.2.
□
Corollary 18.1.19. Under the assumptions of Theorem 18.1.18, the functor
DA : D⋆
(f,..)(A ⊗Bop)op →D−⋆
(..,f)(B ⊗Aop)
is an equivalence of triangulated categories, with quasi-inverse DAop.
Proof. First we note that the op-symmetry (Proposition 18.1.13) implies that The-
orem 18.1.18 is true after exchanging A with Aop. Thus evR,R
N
: N →DA(DAop(N))
is an isomorphism for every N ∈D−⋆
(..,f)(B ⊗Aop). Now the assertion is clear.
□
We need a better understanding of the derived homothety morphisms. Suppose
M ∈C(A⊗Bop). The right action of B on M is the homothety ring homomorphism
through Bop, hmM,Bop : Bop →EndCstr(A)(M). Namely for elements b ∈B and
m ∈M i we have hmM,Bop(op(b))(m) = m·b ∈M i. By composing hmM,Bop with
the localization functor Q : Cstr(A) →D(A) we obtain the ring homomorphism
(18.1.20)
hmD
M,Bop := Q ◦hmM,Bop : Bop →EndD(A)(M).
Lemma 18.1.21. Let M ∈D(A⊗Bop). The three conditions below are equivalent.
(i) M has the derived Morita property on the A side, i.e. (18.1.10) is an iso-
morphism.
(ii) For every p̸ = 0 the module HomD(A)(M, M[p]) is zero, and the ring homo-
morphism hmD
M,Bop : Bop →EndD(A)(M) is bijective.
(iii) For every p̸ = 0 the module Hp RHomA(M, M)

is zero, and the Bop-
module H0 RHomA(M, M)

is free, with basis the element idM.
414
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. This is clear from the canonical isomorphisms
HomD(A)
 M, M[p]
 ∼= Hp RHomA(M, M)

of Corollary 12.2.8.
□
Lemma 18.1.22. Let T ∈D(Aen), and consider the triangulated functor
G := T ⊗L
A (−) : D(A ⊗Bop) →D(A ⊗Bop).
For every M ∈D(A ⊗Bop) the diagram
Bop
hmD
M,Bop
/
hmD
G(M),Bop
(
EndD(A)(M)
G

EndD(A)(G(M))
of ring homomorphisms is commutative.
Proof. This is because the action of Bop on M is categorical, i.e. by endomorphisms
in D(A).
□
Lemma 18.1.23. Let R ∈D(Aen), and consider the triangulated functor
D := RHomA(−, R) : D(A ⊗Bop)op →D(B ⊗Aop).
For every M ∈D(A ⊗Bop) the diagram
Bop
hmD
M,Bop
/
Op(hmD
D(M),B)
)
EndD(A)(M)
D

EndD(Aop)(D(M))op
of ring homomorphisms is commutative.
Proof. Same as the previous lemma, only here D is contravariant.
□
Tilting DG bimodules were deﬁned in Deﬁnition 14.4.1. Here we call them tilting
complexes. Given a tilting complex T ∈D(Aen), we know that its quasi-inverse T ∨
satisﬁes T ∨∼= RHomA(T, A) ∼= RHomAop(T, A) in D(Aen). See Corollary 14.4.27
with B = A, and use the ring isomorphism (18.1.3).
Lemma 18.1.24. Let T be a tilting complex complex over A, with quasi-inverse
T ∨. Then there is an isomorphism T ⊗L
A (−) ∼= RHomA(T ∨, −) of triangulated
functors from D(A ⊗Bop) to itself.
Proof. Let’s write S := T ∨. Then T ∼= S∨∼= RHomA(S, A). We know that S is
perfect on the A side (see Corollary 14.4.28), so by Theorem 14.1.22 we have
T ⊗L
A M ∼= RHomA(S, A) ⊗L
A M
∼= RHomA(S, A ⊗L
A M) ∼= RHomA(T ∨, M).
□
Theorem 18.1.25 ([165]). Let A be a noetherian ring, and let R be a NC dualizing
complex over A.
(1) Given a tilting complex T over A, the complex R′ := T ⊗L
A R is also a NC
dualizing complex over A.
(2) Given a second NC dualizing complex R′ over A, the complex T
:=
RHomA(R, R′) is a tilting complex over A, and R′ ∼= T ⊗L
A R in D(Aen).
(3) If T is a tilting complex over A, and if T ⊗L
A R ∼= R in D(Aen), then T ∼= A
in D(Aen).
415
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof.
(1) We need to verify that R′ satisﬁes conditions (i)-(iii) of Deﬁnition 18.1.12.
Consider the equivalence of triangulated categories G := T ⊗L
A (−) : D(A) →
D(A). The functor G has ﬁnite cohomological dimension (see Theorem 14.1.22,
Corollary 14.4.28 and Proposition 14.1.5). Now G(A) = T, and T ∈Db
f (A) by
Theorem 14.1.26, so Theorem 12.5.8 tells us that G(M) ∈Db
f (A) for every M ∈
Db
f (A). Taking M := R we see that R′ = G(R) ∈Db
f (A).
Let T ∨be the quasi-inverse of T. By Lemma 18.1.24, with B = A, we see that
(18.1.26)
R′ = T ⊗L
A R ∼= RHomA(T ∨, R) = DA(T ∨)
in D(Aen). The tilting complex T ∨belongs to Db
f (A), so according to Theorem
18.1.18(1) with B = K, we see that DA(T ∨) ∈Db
f (Aop). Thus R′ ∈Db
f (Aop). We
have now veriﬁed condition (i) of Deﬁnition 18.1.12 for R′.
To prove that R′ has ﬁnite injective dimension over A, we need to ﬁnd a uniform
bound on the cohomology of RHomA(M, R′), for all M ∈M(A). This is the same
as ﬁnding a natural number d such that HomD(A)(M, R′[i]) = 0 for all M ∈M(A)
and |i| > d. We shall use the equivalence of triangulated categories
G∨:= T ∨⊗L
A (−) ∼= RHomA(T, −) : D(A) →D(A).
Since R ∼= G∨(R′), we obtain a K-module isomorphism
G∨: HomD(A)
 M, R′[i]
 ≃
−→HomD(A)
 G∨(M), R[i]

for every i. The functor G∨has ﬁnite cohomological dimension, and R has ﬁnite
injective dimension; their sum d serves as the required bound.
Now let us prove that R′ has ﬁnite injective dimension over Aop. Take a module
M ∈M(Aop). We have these isomorphisms for every integer i :
Hi RHomAop(M, R′)
 ∼=1 HomD(Aop)
 M, R′[i]

∼=2 HomD(Aop)
 M, DA(T ∨)[i]

∼=3 HomD(A)
 T ∨, DAop(M)[i]

∼=4 Hi RHomA
 T ∨, RHomAop(M, R)

∼=5 Hi T ⊗L
A RHomAop(M, R)

= Hi (G ◦DAop)(M)

.
The justiﬁcations are as follows:
∼=1 : This is by Corollary 12.2.8.
∼=2 : This is by formula (18.1.26).
∼=3 : This relies on Corollary 18.1.19.
∼=4 : Again we use Corollary 12.2.8.
∼=5 : It is due to Lemma 18.1.24.
The functors G and DAop have ﬁnite cohomological dimensions, so we have a uni-
form bound on the cohomology of (G ◦DAop)(M). This completes the proof that
R′ satisﬁes condition (ii) of Deﬁnition 18.1.12.
To prove that R′ has the derived Morita property on the A side we use the
fact that R has the derived Morita property on the A side, and we invoke Lemma
18.1.21 with B := A and M := R. Since R′ = G(R), for every i ∈Z we have an
isomorphism of K-modules
G : HomD(A)
 R, R[i]
 ≃
−→HomD(A)
 R′, R′[i]

,
416
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
and this is zero when i̸ = 0. For i = 0 we use Lemma 18.1.22: there is a commutative
diagram of rings
Aop
hmD
Aop,R
∼
=
/
hmD
Aop,R′
(
EndD(A)(R)
G
∼
=

EndD(A)(R′)
and the vertical arrow G is an isomorphism. Therefore hmD
Aop,R′ is a ring isomor-
phism.
Finally, to prove that R′ has the derived Morita property on the Aop side we
use the fact that the tilting complex T ∨has the derived Morita property on the A
side (by Corollary 14.4.28), together with Lemma 18.1.21, applied to the complexes
T ∨∈M(A ⊗Aop) and R′ ∈M(Aop ⊗A). Recall from (18.1.26) that R′ ∼= DA(T ∨)
in D(Aen). By Corollary 18.1.19, for every i ∈Z we have an isomorphism of K-
modules
DA : HomD(A)
 T ∨, T ∨[i]
 ≃
−→HomD(Aop)
 R′, R′[i]

,
and this is zero when i̸ = 0. For i = 0 we use Lemma 18.1.23: there is a commutative
diagram of rings
Aop
hmD
Aop,T ∨
∼
=
/
Op(hmD
A,R′)
(
EndD(A)(T ∨)
DA
∼
=

EndD(Aop)(R′)op
It follows that hmD
A,R′ : A →EndD(Aop)(R′) is a ring isomorphism.
(2) The proof of this item is a minor modiﬁcation of the proof of Theorem 17.1.10.
Indeed, an ungraded version of Lemma 17.1.13 holds here, and we use Theorem
18.1.18 instead of Theorem 17.1.6.
(3) Assume that T ⊗L
A R ∼= R in D(Aen). Of course R = DA(A). Formula (18.1.26)
says that DA(A) ∼= DA(T ∨) in D(Aen). By Corollary 18.1.19 we conclude that
A ∼= T ∨in D(Aen). But then A ∼= T in D(Aen).
□
The op-symmetry that gave rise to Proposition 18.1.13 implies that several vari-
ations of Theorem 18.1.25 are true. We wish to write down only one of them, that
will be needed later.
Corollary 18.1.27. Let A be a noetherian ring, and let R and R′ be NC dualizing
complexes over A. Then there is a tilting complex T ′ such that R′ ∼= R ⊗L
A T ′ in
D(Aen).
Proof. This is a trivial (yet confusing) consequence of item (2) of Theorem 18.1.25,
when viewing R and R′ as NC dualizing complexes over the ring Aop.
□
Recall that a left action of a group G on a nonempty set X is called simply
transitive if there is one G-orbit in X, and the stabilizer of every point x ∈X is
trivial. I.e. for every (or equivalently, for some) point x ∈X the action function
G × {x} →X, (g, x) 7→g(x), is bijective.
Corollary 18.1.28. Let A be a ring, and assume it has at least one NC dualizing
complex.
Then the left action of the group DPicK(A) on the set of isomorphism
classes of NC dualizing complexes, induced by the bifunctor (T, R) 7→T ⊗L
A R, is
simply transitive.
417
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. By Theorem 18.1.25(1) this is a well-deﬁned action: T ⊗L
A R is a NC dual-
izing complex. The action is transitive by Theorem 18.1.25(2), and it has trivial
stabilizers by Theorem 18.1.25(3).
□
Remark 18.1.29. Suppose A is a noetherian commutative K-ring. A noncom-
mutative dualizing complex over A is not the same as a commutative dualizing
complex over A, in the sense of Deﬁnition 13.1.9. Indeed, there is a K-ring ho-
momorphism Aen →A, and this induces a restriction functor D(A) →D(Aen). If
R ∈D(A) is a commutative dualizing complex over A, then its image in D(Aen)
is a noncommutative dualizing complex over A. However, according to Theorem
18.1.25(1), given any tilting complex T over A, the complex R′ := T ⊗L
A R is also
a NC dualizing complex over A. And R′ can very easily fail to be in the essential
image of D(A); e.g. by taking T := A(ψ), the twist by an automorphism ψ of the
trivial bimodule A.
Remark 18.1.30. In case the base ring K is not a ﬁeld, but A is a ﬂat noetherian
K-ring, then the deﬁnitions and results in this subsection are still valid.
In case the ring A is noetherian, but is not ﬂat over the base ring K, we can
still deﬁne NC dualizing complexes over it. For that we choose a K-ﬂat DG ring
resolution ˜A →A over K; see Theorem 12.8.7 and Proposition 12.8.5.
A NC
dualizing complex over A is then a complex R ∈D( ˜Aen) that satisﬁes the three
conditions of Deﬁnition 18.1.12. As explained in Remark 14.3.24, the triangulated
category D( ˜Aen) is independent of the resolution ˜A, up to a canonical equivalence.
This means that the dualizing complex R is also independent of the resolution.
It is expected that Theorems 18.1.18 and 18.1.25 will still hold in this general
situation; but we did not verify this assertion.
However, ﬂatness alone is not suﬃcient for many of the results in the following
subsections (mainly in Subsection 18.5, in which we rely on results from Section
17, that assumed Convention 15.1.17.) Therefore we decided to assume K is a ﬁeld
in the current subsection as well.
