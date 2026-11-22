---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-033-38-the-dg-category-cam
section_title: "The DG Category C(A,M)"
section_number: 3.8
pages: 71-74
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
sections.
The concept introduced in the deﬁnition below is new.
It is the DG
version of Deﬁnition 3.1.45.
Conventions 1.2.4, 3.3.3, 3.4.3 and 3.5.2 are in place. Thus all linear structures
and operations are K-linear, and rings and bimodules are central over K.
Recall that given an abelian category M, the category of complexes C(M) is
a DG category.
For a complex M ∈C(M) we have the DG ring EndM(M) =
HomM(M, M). The multiplication in this ring is composition.
Deﬁnition 3.8.1. Let M be an abelian category, and let A be a DG ring. A DG
A-module in M is an object M ∈C(M), together with a DG ring homomorphism
f : A →EndM(M).
If M is a DG A-module in M, then after forgetting the diﬀerentials, M becomes
a graded A-module in M.
Deﬁnition 3.8.2. Let M be an abelian category, let A be a DG ring, and let M, N
be DG A-modules in M. In Deﬁnition 3.1.47 we introduced the graded K-module
HomA,M(M, N). This is made into a DG K-module with diﬀerential
d(φ) := dN ◦φ −(−1)i·φ ◦dM
for φ ∈HomA,M(M, N)i.
When we have to be speciﬁc, we denote the diﬀerential of HomA,M(M, N) by
dHom, dA,M, or some similar expression.
As we have seen before (in Lemmas 3.6.5 and 3.4.5), given morphisms
φk ∈HomA,M(Mk, Mk+1)ik
for k ∈{0, 1}, we have
φ1 ◦φ0 ∈HomA,M(M0, M2)i0+i1,
and
d(φ1 ◦φ0) = d(φ1) ◦φ0 + (−1)i1 ·φ1 ◦d(φ0).
Also the identity automorphism idM belongs to HomA,M(M, M)0, and d(idM) = 0.
Therefore the next deﬁnition is legitimate.
Deﬁnition 3.8.3. Let M be an abelian category, and let A be a DG ring. The
DG category of DG A-modules in M is denoted by C(A, M). The morphism DG
K-modules are
HomC(A,M)(M0, M1) := HomA,M(M0, M1)
from Deﬁnition 3.8.2. The composition is that of C(M).
Notice that forgetting the action of A is a faithful DG functor C(A, M) →C(M).
Example 3.8.4. If A = K, then C(A, M) = C(M); and if M = Mod K, then
C(A, M) = C(A) = DGMod A.
71
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Deﬁnition 3.8.5. In the situation of Deﬁnition 3.8.3:
(1) The strict category of C(A, M) (see Deﬁnition 3.4.6(1)) is denoted by
Cstr(A, M).
(2) The homotopy category of C(A, M) (see Deﬁnition 3.4.6(2)) is denoted by
K(A, M).
To say this in words: a morphism φ : M →N in C(A, M) is strict if and only if
it has degree 0 and φ ◦dM = dN ◦φ. The morphisms in K(A, M) are the homotopy
classes of strict morphisms.
An additive functor F : M →N between abelian categories is called faithfully
exact if for every sequence E in Cstr(A, M), the sequence E is exact if and only if
the sequence F(E) in N is exact.
Proposition 3.8.6. The category Cstr(A, M) is a K-linear abelian category, and
the forgetful functors
Cstr(A, M) −→Cstr(M)
Und
−−→Gstr(M)
are faithfully exact.
Exercise 3.8.7. Prove the proposition above.
Like Deﬁnition 3.2.4, given a DG module M ∈C(A, M) and an integer i, we can
consider the objects of degree i cocycles Zi(M), decocycles Yi(M), coboundaries
Bi(M) and cohomology Hi(M). These are all objects of M. As M varies we get
linear functors
(3.8.8)
Z, Y, B, H : Cstr(A, M) →Gstr(M).
These objects are related by the following exact sequences in M :
(3.8.9)
0 →Zi(M) →M i
di
M
−−→M i+1,
(3.8.10)
M i−1
di−1
M
−−−→M →Yi(M) →0,
(3.8.11)
0 →Bi(M) →Zi(M) →Hi(M) →0,
(3.8.12)
0 →Hi(M) →Yi(M) →Bi+1(M) →0.
Remark 3.8.13. Actually, the cohomology functor H from equation (3.8.8) factors
through the category Gstr(H(A), M). See formula (3.1.49). We will not need this
fact.
Proposition 3.8.14. The functor Z in equation (3.8.8) is left exact, and the func-
tor Y in equation (3.8.8) is right exact.
Proof. It is enough to consider each degree separately. And by Proposition 3.8.6
we may ignore the DG ring A. Let F i : Gstr(M) →M be the functor that sends a
graded module M to its degree i component M i. This is an exact functor.
Formula (3.8.9) exhibits Zi as the kernel of the homomorphism of functors di :
F i →F i+1. According to Proposition 2.5.18(2) the functor Zi is left exact.
Similarly, formula (3.8.10) exhibits Yi as the cokernel of the homomorphism of
functors di−1 : F i−1 →F i. According to Proposition 2.5.18(2) the functor Yi is
right exact.
□
Proposition 3.8.15. Let {Mx}x∈X be a collection of objects of C(A, M), indexed
by a set X. Assume that for every i ∈Z the direct sum M i := L
x∈X M i
x exists in
M. Then the graded object M := {M i}i∈Z ∈G(M) has a canonical structure of DG
A-module in M, and M is a direct sum of the collection {Mx}x∈X in Cstr(A, M).
72
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Exercise 3.8.16. Prove Proposition 3.8.15. (Hint: look at the proof of Theorem
3.9.16.)
Example 3.8.17. Since M(K) has inﬁnite direct sums, the proposition above shows
that Cstr(A) has inﬁnite direct sums.
Proposition 3.8.18. Given a DG ring A, let A♮be the graded ring gotten by
forgetting the diﬀerential. Consider the forgetful functor Und : C(A, M) →G(A♮, M)
that forgets the diﬀerentials of DG modules, i.e. Und(M, dM) := M.
(1) Und is a fully faithful graded functor.
(2) On the strict categories, Str(Und) : Cstr(A, M) →Gstr(A, M) is a faithfully
exact additive functor.
Exercise 3.8.19. Prove Proposition 3.8.18.
A graded object M = {M i}i∈Z in M is said to be bounded above if the set
{i | M i̸ = 0} is bounded above. Likewise we deﬁne bounded below and bounded
graded objects.
Deﬁnition 3.8.20. We deﬁne C−(A, M), C+(A, M) and Cb(A, M) to be the full
subcategories of C(A, M) consisting of bounded above, bounded below and bounded
DG modules respectively.
The symbols “−”, “+” and “b” and “⟨empty⟩” (the empty symbol) are called
boundedness indicators. We shall usually use the symbol “⋆” to denote an unspec-
iﬁed boundedness indicator. Thus the expression C⋆(A, M) can refer to any of the
four full subcategories of C(A, M) that are mentioned in the deﬁnition above.
Remark 3.8.21. Here is a generalization of Deﬁnition 3.8.3.
Instead of a DG
central K-ring A we can take a small K-linear DG category A. We then deﬁne the
K-linear DG category C(A, M) := DGFun(A, C(M)) as in Exercise 3.5.8.
This is indeed a generalization of Deﬁnition 3.8.3: when A has a single object x,
and we write A := EndA(x), then the functor M 7→M(x) is an isomorphism of DG
categories C(A, M)
≃
−→C(A, M).
In the special case of M = M(K) = Mod K, the DG category C(A, M) is what
Keller [79] calls the DG category of DG A-modules.
Almost everything we do in this book for C(A, M) holds in the more general
context of C(A, M). However, in the more general context a lot of the intuition
is lost, and some aspects become pretty cumbersome. This is the reason we have
decided to stick with the less general context.
Remark 3.8.22. The theory of DG categories has a generalization – this is the
theory of A∞categories, which will be outlined in this remark. All set theoretical
issues are going to be ignored.
The concept of an A∞algebra, namely a single-object A∞category, was intro-
duced by J. Stasheﬀ[146], [147] in the 1960’s, in relation with his work on higher
operations on H-spaces in topology.
A∞categories are at the core of Homological Mirror Symmetry, conceived by K.
Fukaya and M. Kontsevich during the 1990’s. Indeed, a symplectic manifold Y gives
rise to the Fukaya category F(Y ), which is an A∞category, and is a categoriﬁcation
of Floer cohomology. See [48], [86], [87], [141] and [88].
Further developments on A∞algebras and categories were made, among oth-
ers, by T.V. Kadeishvili [73], K. Lefèvre-Hasegawa [94], B. Keller [80], [83], and
Canonaco-Ornaghi-Stellari [37]. For the analogous theory of L∞algebras, general-
izing DG Lie algebras, see [169].
We shall only discuss strictly unital A∞categories, giving very few details (full
details can be found in [83] and [37]), and our notation deviates somewhat from
73
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
the references (because we want it to be compatible with the rest of the book).
The base ring K is assumed to be a ﬁeld. An A∞category A over K has a set
of objects Ob(A).
For each pair of objects x, y ∈Ob(A) there is a graded K-
module A(x, y) = HomA(x, y). For each x ∈Ob(A) there is a degree 0 element
idx ∈A(x, x). For each i ≥1 and each sequence x0, . . . , xi ∈Ob(A), there is a
degree 2 −i homomorphism
(3.8.23)
mi : A(xi−1, xi) ⊗· · · ⊗A(x0, x1) →A(x0, xi)
G(K). The operations mi satisfy certain relations. Roughly speaking, the operation
m1 is a diﬀerential, the operation m2 is a multiplication, the element idx is a unit
for the multiplication m2, the multiplication m2 is associative up to the hotomopy
m3, etc. The relations imply that the cohomology H(A), w.r.t. the diﬀerential m1,
is a graded category, in the sense of Deﬁnition 3.1.32. If the higher (i.e. i > 2)
operations mi vanish, then A is a DG category, in the sense of Deﬁnition 3.4.1.
Suppose A and B are A∞categories. An A∞functor F : A →B consists of a
function Fob : Ob(A) →Ob(B), and for each i ≥1 and each sequence x0, . . . , xi ∈
Ob(A), a degree 1 −i homomorphism
(3.8.24)
Fi : A(xi−1, xi) ⊗· · · ⊗A(x0, x1) →B
 Fob(x0), Fob(xi)

in G(K). There are relations that the Fi have to satisfy. Given another A∞functor
G : B →C, there is a composed A∞functor G◦F : A →C, which is hard to describe
directly (it is usually deﬁned in terms of cocategories, via the bar construction). We
denote by A∞Cat the category whose objects are the A∞categories and whose
morphisms are the A∞functors.
For a pair A, B ∈Ob(A∞Cat) we denote by A∞Fun(A, B) the set of A∞functors
from A to B, so that
(3.8.25)
HomA∞Cat(A, B) = A∞Fun(A, B).
An important fact is that A∞Fun(A, B) is itself the set of objects of an A∞category,
i.e. A∞Fun(A, B) ∈Ob(A∞Cat). If B is a DG category (i.e. its higher operations
vanish), then A∞Fun(A, B) is also a DG category.
We shall discuss more aspects of A∞categories in Remarks 6.2.38 and 7.2.15.
