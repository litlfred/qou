---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-051-63-localization-of-linear-categories
section_title: "Localization of Linear Categories"
section_number: 6.3
pages: 124-127
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
arbitrary categories. In this subsection our categories will be linear over the com-
mutative base ring K (which will be implicit most of the time). See Convention
1.2.4.
For convenience we only talk about right denominator sets here. All the state-
ments hold equally for left denominator sets; cf. Remark 6.2.3 and Proposition
6.2.4.
124
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Theorem 6.3.1. Let A be a K-linear category, let S be a right denominator set in
A, and let (AS, Q) be the right Ore localization.
(1) The category AS has a unique K-linear structure, such that Q : A →AS is
a K-linear functor.
(2) Suppose B is another K-linear category, and F : A →B is a K-linear
functor s.t. F(s) is invertible for every s ∈S. Let FS : AS →B be the
localization of F. Then FS is a K-linear functor.
(3) If A is an additive category, then so is AS.
Proof.
(1) Let q1, q2 : M →N be morphisms in AS. Choose common denominator pre-
sentations qi = Q(ai) ◦Q(s)−1. Since Q must be an additive functor, we have to
deﬁne
(6.3.2)
Q(a1) + Q(a2) := Q(a1 + a2).
By the distributive law (bilinearity of composition) we must deﬁne q1 + q2 :=
Q(a1 + a2) ◦Q(s)−1. And for λ ∈K we must deﬁne λ · qi := Q(λ·ai) ◦Q(s)−1.
The usual tricks are then used to prove independence of representatives. For
instance, to prove that (6.3.2) is independent of choices, suppose that Q(a1) =
Q(a′
1) and Q(a2) = Q(a′
2). Then, by (RO4), there are t1, t2 ∈S such that a1 ◦t1 =
a′
1◦t1 and a2◦t2 = a′
2◦t2. By (RD1) there exist b ∈A and v ∈S s.t. t1◦b = t2◦v. Let
t3 := t2◦v ∈S. Then (a1+a2)◦t3 = (a′
1+a′
2)◦t3, and hence Q(a1+a2) = Q(a′
1+a′
2).
In this way AS is a K-linear category, and Q is a K-linear functor.
(2) The only option for FS is FS(qi) := F(ai) ◦F(s)−1. The usual tricks are used
to prove independence of representatives.
(3) Clear from Propositions 2.5.2 and 2.5.7.
□
Exercise 6.3.3. Finish the proofs of items (1) and (2) of the theorem.
Remark 6.3.4. Let A be a ring, which we can think of as a one-object linear
category A. In this context, Theorem 6.3.1 is one of the most important results in
noncommutative ring theory. See the books [106], [130] or [148].
Here are somewhat concrete examples.
Example 6.3.5. Suppose A is a noncommutative ring (i.e. it is not necessarily com-
mutative), and S is a central multiplicatively closed set in A (i.e. S ⊆Cent(A)). Be-
cause the elements of S commute with all elements of A, the denominator conditions
hold automatically. We get a left and right Ore localization of rings Q : A →AS.
Note that if S contains a nilpotent element, then the ring AS is trivial.
The last observation should serve as a warning: localization can sometimes kill
everything. Fortunately, the localization procedure that gives rise to the derived
category does not cause any catastrophe, as we shall see in Proposition 7.1.10.
Example 6.3.6. Suppose A is a noncommutative ring that is both noetherian
and an integral domain (i.e. the only zero-divisor in A is 0). Let S be the set of
nonzero elements of A. Then S is both a left and a right denominator set. See [106,
Theorem 2.1.15].
Remark 6.3.7. Suppose A is a ring and S is a right denominator set in it. Then
the right Ore localization AS is ﬂat as left A-module. See [130, Theorem 3.1.20].
We have no idea if something like this is true for linear categories with more than
one object.
Proposition 6.3.8. Let (K, T) be a T-additive category, let S be a right denomi-
nator set in K such that T(S) = S, and let Q : K →KS be the localization functor.
125
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
(1) There is a unique additive automorphism TS of the category KS, such that
TS ◦Q = Q ◦T as functors K →KS.
(2) Let τ be the identity automorphism of the functor Q ◦T. Then (Q, τ) :
(K, T) →(KS, TS) is a T-additive functor.
Proof.
(1) By the assumption the functor Q ◦T : K →KS sends the morphisms in S
to isomorphisms. By the property (Loc3) of localization in Deﬁnition 6.1.2, the
functor TS : KS →KS satisfying TS ◦Q = Q ◦T exists and is unique. Similarly,
there is a unique functor T−1
S
: KS →KS satisfying T−1
S
◦Q = Q ◦T−1. An easy
calculation shows that T−1
S
◦TS = Id = TS ◦T−1
S . Hence TS is an automorphism
of KS. By Theorem 6.3.1 the functor TS is additive.
(2) This is clear.
□
The composition of T-additive functors was deﬁned in Deﬁnition 5.1.4.
Proposition 6.3.9. In the situation of Proposition 6.3.8, suppose (K′, T′) is an-
other T-additive category, and (F, ν) : (K, T) →(K′, T′) is a T-additive functor,
such that F(s) is invertible for every s ∈S. Let FS : KS →K′ be the localized func-
tor. Then there is a unique isomorphism νS : FS◦TS
≃
−→T′ ◦FS of functors KS →K′,
such that (F, ν) = (FS, νS) ◦(Q, τ) as T-additive functors (K, T) →(K′, T′).
Exercise 6.3.10. Prove Proposition 6.3.9.
126
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
