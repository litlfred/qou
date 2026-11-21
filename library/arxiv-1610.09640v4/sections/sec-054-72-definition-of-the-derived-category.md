---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-054-72-definition-of-the-derived-category
section_title: "Definition of the Derived Category"
section_number: 7.2
pages: 132-135
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
category K = K(A, M), for a central DG K-ring A and a K-linear abelian category
M.
Recall the cohomology functor H : Cstr(A, M) →Gstr(M) from Deﬁnition 3.2.4.
Lemma 7.2.1. Suppose φ, ψ : M →N are morphisms in Cstr(A, M) such that
ψ −φ is a coboundary in HomA,M(M, N).
Then H(φ) = H(ψ), as morphisms
H(M) →H(N) in Gstr(M).
Exercise 7.2.2. Prove the lemma.
It follows that there is an induced functor
(7.2.3)
H : K(A, M) →Gstr(M).
We shall be interested in its degree 0 component H0. Of course all other components
can be recovered from H0 by the translation functor: Hi = H0 ◦Ti.
Proposition 7.2.4. Let M be an abelian category and let A be a DG ring. Then
the functor H0 : K(A, M) →M is cohomological.
Proof. Clearly H0 is additive. Consider a distinguished triangle
(7.2.5)
L
α−→M
β−→N
γ−→T(L)
in K(A, M). We must prove that
H0(L)
H0(α)
−−−−→H0(M)
H0(β)
−−−−→H0(N)
132
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
is an exact sequence in M.
By Deﬁnition 5.4.2 we can assume that the distinguished triangle (7.2.5) is the
image of a standard triangle in C(A, M). Namely that N = Cone(α), the standard
cone associated to α, and the morphisms are β = eα and γ = pα; see Deﬁnitions
4.2.1 and 4.2.5. To be explicit, in matrix notation we have N =
h
M
T(L)
i
, dN =

dM α◦t−1
L
0
dT(L)

and β =
h
idM
0
i
.
Let us use the abbreviations ¯β := H0(β) and ¯α := H0(α).
By Proposition
5.3.1 we know that β ◦α = 0, and hence ¯β ◦¯α = 0. It remains to prove that
the morphism ¯α : H0(L) →Ker(¯β) in M is an epimorphism. This will be done
using the ﬁrst sheaf trick (Proposition 2.4.9(3)): we will prove that given a section
¯m ∈Γ(U, Ker(¯β)) on an open set U ∈M, there is a reﬁnement V ′ ↠U and a
section ¯l ∈Γ(V ′, H0(L)) such that ¯α(¯l) = ¯m in Γ(V ′, Ker(¯β)). See Subsection 2.4
for the “geometric” terminology that’s used in the sheaf tricks.
Take some section ¯m ∈Γ(U, Ker(¯β)) on an open set U ∈M. This means that
¯m ∈Γ(U, H0(M)) and ¯β( ¯m) = 0.
There is a covering V ↠U and a section
m ∈Γ(V, Z0(M)) such that πM(m) = ¯m. Now
β(m) =
m
0

∈Γ(V, Z0(N)) ⊆Γ(V, N 0) =
Γ(V, M 0)
Γ(V, L1)

in column notation. The vanishing of ¯β( ¯m) = πN(β(m)) in Γ(V, H0(N)) means that
there is a covering V ′ ↠V and a section n ∈Γ(V ′, N −1) such that dN(n) = β(m).
In column notation we have n =
 m′
l

, with m′ ∈Γ(V ′, M −1) and l ∈Γ(V ′, L0).
The equality β(m) = dN(n) becomes the matrix equality
m
0

=
dM
α
0
−dL

·
m′
l

=
dM(m′) + α(l)
−dL(l)

.
We see that l ∈Γ(V ′, Z0(L)). Then the cohomology class ¯l := πL(l) ∈Γ(V ′, H0(L))
satisﬁes
¯α(¯l) = πM(α(l)) = πM(dM(m′) + α(l)) = πM(m) = ¯m
in Γ(V ′, H0(M)), as required.
□
Deﬁnition 7.2.6. A morphism φ in K(A, M) is called a quasi-isomorphism if the
morphisms Hi(φ) in M are isomorphisms for all i. The set of quasi-isomorphisms
in K(A, M) is denoted by S(A, M).
By Proposition 7.2.4 the functor H0 is cohomological. According to Proposition
7.1.1, S(A, M) is a denominator set of cohomological origin; so Theorem 7.1.3 applies
to it, and the next deﬁnition makes sense.
Deﬁnition 7.2.7. Let M be a K-linear abelian category and A a central DG K-ring.
The derived category of DG A-modules in M is the K-linear triangulated category
D(A, M) := K(A, M)S(A,M).
The corresponding triangulated localization functor is
Q : K(A, M) →D(A, M).
We also have the additive functor P : Cstr(A, M) →K(A, M) which sends a strict
morphism of DG modules to its homotopy class.
Deﬁnition 7.2.8. Let M be an abelian category and let A be a DG ring. Deﬁne
the functor
˜Q := Q ◦P : Cstr(A, M) →D(A, M).
133
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
We thus get a commutative diagram of additive functors
(7.2.9)
Cstr(A, M)
P
/
˜Q

K(A, M)
Q
/ D(A, M)
that are all the identity on objects.
It is sometimes convenient to describe morphisms in D(A, M) in terms of the
functor ˜Q. A morphism s ∈Cstr(A, M) is called a quasi-isomorphism if P(s) is a
quasi-isomorphism in K(A, M); i.e. if H(s) is an isomorphism in Gstr(M).
Proposition 7.2.10.
(1) Every morphism φ in D(A, M) can be written as a right fraction φ = ˜Q(a)◦
˜Q(s)−1 where a, s ∈Cstr(A, M) and s is a quasi-isomorphism.
(2) Let a ∈Cstr(A, M). Then ˜Q(a) = 0 in D(A, M) iﬀthere exists a quasi-
isomorphism s in Cstr(A, M) such that a ◦s is a coboundary in C(A, M).
Proof.
(1) This is because of property (RO3) of Deﬁnition 6.2.1 and the fact that P is full.
(2) Let us write ¯a := P(a) ∈K(A, M). Since Q(¯a) = 0, by Property (RO4) of
Deﬁnition 6.2.1 there is a quasi-isomorphism ¯s ∈K(A, M) such that ¯a ◦¯s = 0 in
K(A, M). Choose a quasi-isomorphism s ∈Cstr(A, M) such that ¯s = P(s). Then
P(a ◦s) = 0, and this means that a ◦s is a coboundary.
□
Of course there is a left version of this proposition. The next deﬁnition is about
arbitrary (not necessarily linear) categories.
Deﬁnition 7.2.11. A functor F : C →D between categories is called conserva-
tive if for every morphism φ in C, φ is an isomorphism if and only if F(φ) is an
isomorphism.
By Proposition 7.1.10 the cohomology functor (7.2.3) extends uniquely to a func-
tor
(7.2.12)
H : D(A, M) →Gstr(M).
Corollary 7.2.13. The functor H in (7.2.12) is conservative.
Proof. One implication is trivial. For the other implication, assume that φ is a
morphism in D(A, M) such that H(φ) is an isomorphism.
We can write φ as a
right fraction: φ = Q(a) ◦Q(s)−1, where a ∈K(A, M) and s ∈S(A, M). Then
H(φ) = H(Q(a)) ◦H(Q(s))−1, and we see that H(Q(a)) is an isomorphism. But
H(a) = H(Q(a)), so in fact a ∈S(A, M) too. Therefore Q(a) is an isomorphism in
D(A, M). It follows that φ is an isomorphism in D(A, M).
□
Exercise 7.2.14. Here M = M(K), so K(A, M) = K(A). Show that the functor
H0 : K(A) →M(K) is corepresentable by the object A ∈K(A) (see Subsection 1.7).
Remark 7.2.15. This is a continuation of Remarks 3.8.22 and 6.2.38 on strictly
unital A∞categories. The base ring K is a ﬁeld. The references are [83] and [37].
Recall that if A is an A∞category and B is a DG category, then A∞Fun(A, B) is a
DG category.
Consider the special case is when B = C(K), the DG category of complexes of
K-modules. An A∞functor M : A →C(K) is called an A∞A-module. The A∞
A-modules are the objects of the DG category C∞(A) := A∞Fun(A, C(K)). The
strict subcategory Str(C∞(A)), in the sense of Deﬁnition 3.4.6(1), is what most
texts call the category of A∞A-modules.
134
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
A morphism φ : M →N in Str(C∞(A)) is called a quasi-isomorphism if for
every object x ∈Ob(A) the morphism φ(x) : M(x) →N(x) in Str(C(K)) =
Cstr(K) is a quasi-isomorphism. The localization of Str(C∞(A)) w.r.t. the quasi-
isomorphisms is the derived category of A∞A-modules, denoted by D∞(A). (As
usual, the tradition is to call D∞(A) the “homotopy category” of C∞(A), and to
denote it by Ho(C∞(A)).) There is a localization functor Q : Str(C∞(A)) →D∞(A).
We can also consider the category K∞(A) := H0(C∞(A)), see Deﬁnition 3.4.6(2).
There is a full functor P : Str(C∞(A)) →K∞(A), and a commutative diagram
(7.2.16)
Str(C∞(A))
P
/
Q

K∞(A)
¯Q
/ D∞(A)
All three functors are the identity on objects. The categories K∞(A) and D∞(A)
are triangulated, and the functor ¯Q is an isomorphism of triangulated categories.
Finally, let A be a DG category. Then the DG category C(A) of DG A-modules
embeds faithfully (but not fully) into the DG category C∞(A). The induced trian-
gulated functor D(A) →D∞(A) is an equivalence.
