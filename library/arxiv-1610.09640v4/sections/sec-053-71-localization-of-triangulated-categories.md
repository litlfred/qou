---
doc_id: arxiv-1610.09640v4
doc_title: "Derived Categories"
section_id: sec-053-71-localization-of-triangulated-categories
section_title: "Localization of Triangulated Categories"
section_number: 7.1
pages: 127-132
source_pdf: 1610.09640v4.pdf
source_sha256: db5e7a5c5e85f95f
toc_source: outline
doc_brief: "Derived Categories — This is the fourth (and last) prepublication version of a book on derived categories, that will be published by Cambridge University Press."
---
gory, with translation functor T. As we did in Section 6, we shall often write a ∈K
for a morphism a ∈K(M, N) = HomK(M, N), leaving the objects implicit.
Proposition 7.1.1. Suppose H : K →M is a cohomological functor, where M is
some abelian category. Let
S :=

s ∈K | H(Ti(s)) is invertible for all i ∈Z
	
.
Then S is a left and right denominator set in K.
Proof. It is clear that S is closed under composition and contains the identity
morphisms. So it is a multiplicatively closed set.
Let’s prove that condition (RD1) of Deﬁnition 6.2.14 holds. Suppose we are given
morphisms L
a−→N
s←−M with s ∈S. We need to ﬁnd morphisms L
t←−K
b−→M
with t ∈S and such that a ◦t = s ◦b.
Consider the solid commutative diagram
K
t
/
b

L
c◦a
/
a

P
/
=

T(K)
T(b)

M
s
/ N
c
/ P
/ T(M)
where the bottom row is a distinguished triangle built on M
s−→N, and and the top
row is a distinguished triangle built on L
c◦a
−−→P, then turned 120◦to the right.
By axiom (TR3) there is a morphism b making the diagram commutative. Thus
a◦t = s◦b. Since H(Ti(s)) are invertible for all i ∈Z, it follows that H(Ti(P)) = 0.
But then H(Ti(t)) are invertible for all i ∈Z, so t ∈S.
Next we prove condition (RD2) of Deﬁnition 6.2.14. Because we are in an addi-
tive category, this condition is simpliﬁed: given a ∈K and s ∈S satisfying s◦a = 0,
we have to ﬁnd t ∈S satisfying a ◦t = 0.
Say the objects involved are L
a−→M
s−→N. Take a distinguished triangle built
on s and then turned: P
b−→M
s−→N −→T(P). We get an exact sequence
HomK(L, P)
b ◦(−)
−−−−→HomK(L, M)
s ◦(−)
−−−−→HomK(L, N).
Since s◦a = 0, there is c : L →P s.t. a = b◦c. Now look at a distinguished triangle
built on c, and then turned: K
t−→L
c−→P −→T(K). We know that c ◦t = 0; hence
a ◦t = b ◦c ◦t = 0. But (s ∈S) ⇒(H(Ti(P)) = 0 for all i) ⇒(t ∈S).
The left versions (LD1) and (LD2) are proved the same way.
□
Deﬁnition 7.1.2. A denominator set of cohomological origin in K is a denominator
set S ⊆K that arises from a cohomological functor H, as in Proposition 7.1.1. The
morphisms in S are called quasi-isomorphisms relative to H.
This material will be published by Cambridge University Press as Derived Categories by Amnon
Yekutieli. This prepublication version is free to view and download for personal use only. Not for
redistribution, resale or use in derivative works. c⃝Amnon Yekutieli, 2019.
127
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Theorem 7.1.3. Let (K, T) be a triangulated category, let S be a denominator set
of cohomological origin in K, and let (Q, τ) : (K, T) →(KS, TS) be the T-additive
functor from Proposition 6.3.8. Then the T-additive category (KS, TS) has a unique
triangulated structure such that these two properties hold:
(i) The pair (Q, τ) is a triangulated functor.
(ii) Suppose (K′, T′) is another triangulated category, and (F, ν) : (K, T) →
(K′, T′) is a triangulated functor, such that F(s) is invertible for every
s ∈S. Let (FS, νS) : (KS, TS) →(K′, T′) be the T-additive functor from
Proposition 6.3.9. Then (FS, νS) is a triangulated functor.
This result is stated as [62, Proposition I.3.2] and as [75, Proposition 1.6.9]. Both
sources do not give proofs (just hints).
Proof. Since S is of cohomological origin we have T(S) = S. Recall that the trans-
lation isomorphism τ is the identity automorphism of the functor Q ◦T; see Propo-
sition 6.3.8. So we will ignore it.
Step 1. The distinguished triangles in KS are deﬁned to be those triangles that are
isomorphic to the images under Q of distinguished triangles in K. Let us verify the
axioms of triangulated category.
(TR1). By deﬁnition every triangle that’s isomorphic to a distinguished triangle is
distinguished; and the triangle M
idM
−−→M →0 →T(M) in KS is clearly distin-
guished.
Suppose we are given a morphism α : L →M in KS.
We have to build a
distinguished triangle on it. Choose a fraction presentation α = Q(a) ◦Q(s)−1.
Using condition (LD1) we can ﬁnd b ∈K and t ∈S such that t ◦a = b ◦s. These
ﬁt into the solid commutative diagram
L
α
$
b
%
K
s
o
a
/ M
t
y
˜K
in K. (The dashed arrow α is in KS.)
Consider the solid commutative diagram below, where the rows are distinguished
triangles built on a and b respectively.
(7.1.4)
K
a
/
s

M
e
/
t

N
c
/
u

T(K)
T(s)

L
b
/ ˜K
/ P
d
/ T(L)
By (TR3) there is a morphism u that makes the whole diagram commutative.
Since s, t ∈S and H is a cohomological functor, it follows that u ∈S. Applying the
functor Q to (7.1.4), and using the isomorphism Q(t) : M →˜K to replace ˜K with
M, we get the commutative diagram
K
Q(a)
/
Q(s)

M
Q(e)
/
Q(idM)

N
Q(c) /
Q(u)

T(K)
T(Q(s))

L
α
/ M
Q(u◦e) / P
Q(d) / T(L)
128
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
in KS. The top row is a distinguished triangle, and the vertical arrows are isomor-
phisms. So the bottom row is a distinguished triangle. This is the triangle we were
looking for.
(TR2). Turning: this is trivial.
(TR3). We are given the solid commutative diagram in KS, where the rows are
distinguished triangles:
(7.1.5)
L
α
/
φ

M
β
/
ψ

N
γ
/
χ

T(L)
T(φ)

L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′)
and we have to ﬁnd χ to complete the diagram.
By replacing the rows with isomorphic triangles, we can assume they come from
K. Thus we can replace (7.1.5) with this diagram:
(7.1.6)
L
Q(α)
/
φ

M
Q(β)
/
ψ

N
Q(γ) /
χ

T(L)
T(φ)

L′
Q(α′) / M ′
Q(β′) / N ′
Q(γ′) / T(L′)
in which α, β, γ, α′, β′, γ′ are morphisms in K. It is a commutative diagram. Let us
choose fraction presentations φ = Q(a) ◦Q(s)−1 and ψ = Q(b) ◦Q(t)−1. Then the
solid diagram (7.1.6) comes from applying Q to the diagram
(7.1.7)
L
α
/ M
β
/ N
γ
/ T(L)
˜L
a

s
O
˜
M
b

t
O
T(˜L)
T(a)

T(s)
O
L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′)
in K. Here the rows are distinguished triangles in K; but the diagram might fail to
be commutative.
By axiom (RO3) we can ﬁnd c ∈K and u ∈S s.t. Q(t)−1 ◦Q(α) ◦Q(s) =
Q(c) ◦Q(u)−1. This is the solid diagram below:
L
α
/ M
˜L′′
u′
/ ˜L′
u
/
c
;
˜L
a

s
O
˜
M
b

t
O
L′
α′
/ M ′
Thus Q(α◦s◦u) = Q(t◦c). By (RO4) there is a morphism u′ ∈S s.t. (α◦s◦u)◦u′ =
(t ◦c) ◦u′. We get
φ = Q(a) ◦Q(s)−1 = Q(a ◦u ◦u′) ◦Q(s ◦u ◦u′)−1
129
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
in KS. Thus, after substituting ˜L := ˜L′′, s := s◦u◦u′, a := a◦u◦u′ and c := c◦u′,
we get a new diagram
(7.1.8)
L
α
/ M
β
/ N
γ
/ T(L)
˜L
c
/
a

s
O
˜
M
b

t
O
T(˜L)
T(a)

T(s)
O
L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′)
in K instead of (7.1.7). In this new diagram the top left square is commutative; but
maybe the bottom left square is not commutative.
When we apply Q to the diagram (7.1.8), the whole diagram, including the
bottom left square, becomes commutative, since (7.1.6) is commutative.
Again
using condition (RO4), there is v ∈S s.t. (α′ ◦a) ◦v = (b ◦c) ◦v. In a diagram:
L
α
/ M
˜L′
v
/ ˜L
a

s
O
c
/ ˜
M
b

t
O
L′
α′
/ M ′
Performing the replacements ˜L := ˜L′, s := s ◦v, c := c ◦v and a := a ◦v we now
have a commutative square also at the bottom left of (7.1.8). Since γ ◦β = 0 and
γ′ ◦β′ = 0, in fact the whole diagram (7.1.8) in K is now commutative.
Now by (TR1) we can embed the morphism c in a distinguished triangle. We
get the solid diagram
(7.1.9)
L
α
/ M
β
/ N
γ
/ T(L)
˜L
c
/
a

s
O
˜
M
˜β
/
b

t
O
˜N
˜γ
/
d

w
O
T(˜L)
T(a)

T(s)
O
L′
α′
/ M ′
β′
/ N ′
γ′
/ T(L′)
in K. The rows are distinguished triangles. Since ˜γ ◦˜β = 0, the solid diagram is
commutative. By (TR3) there are morphisms w and d that make the whole diagram
commutative. Now by the long exact cohomology sequence (see Theorem 3.7.10)
the morphism w belongs to S. The morphism χ := Q(d) ◦Q(w)−1 : N →N ′ solves
the problem.
(TR4). We will not give any details, as this axiom is not an important feature for
us (see Remark 5.1.13). A proof can be found as part of the proof of [113, Theorem
2.1.8, page 97], where this axiom is called (TR4′).
Step 2. Suppose (F, ν) is a triangulated functor as in condition (ii). By Proposition
6.3.9 this extends uniquely to a T-additive functor (FS, νS). The construction of the
triangulated structure on (KS, TS) in the previous steps, and the deﬁning property
of the translation isomorphism νS in Proposition 6.3.9, show that (FS, νS) is a
triangulated functor.
130
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Step 3. At this point (KS, TS) is a triangulated category, and conditions (i)-(ii) of the
theorem are satisﬁed. We need to prove the uniqueness of the triangulated structure
on (KS, TS). Condition (i) says that we can’t have less distinguished triangles than
those we declared. We can’t have more distinguished triangles, because of condition
(ii).
□
Proposition 7.1.10. Consider the situation of Proposition 7.1.1 and Theorem
7.1.3.
(1) The cohomological functor H : K →M factors into H = HS ◦Q, where
HS : KS →M is a cohomological functor.
(2) Let M be an object of K. The object Q(M) is zero in KS iﬀthe objects
H(Ti((M)) are zero in M for all i.
Proof.
(1) The existence and uniqueness of the functor HS are by the universal prop-
erty (Loc3) in Deﬁnition 6.1.2. We leave it as an exercise to show that HS is a
cohomological functor.
(2) Since HS is an additive functor, if Q(M) = 0, then so is H(M) = HS(Q(M)).
And of course Q(M) = 0 iﬀQ(Ti(M)) = 0 for all i.
For the converse, let φ : 0 →M be the zero morphism in K. If H(Ti(M)) = 0
for all i, then H(Ti(φ)) : 0 →H(Ti(M)) are isomorphisms for all i. Then φ ∈S,
and so Q(φ) : 0 →Q(M) is an isomorphism in KS.
□
Proposition 7.1.11. Let K be a triangulated category, let S be a denominator set
of cohomological origin in K, and let K′ be a full triangulated subcategory of K. Then
S′ := K′ ∩S is a denominator set of cohomological origin in K′, the Ore localization
K′
S′ exists, and K′
S′ is a triangulated category.
Proof. Let H : K →M be a cohomological functor that determines S. The functor
H|K′ : K′ →M is also cohomological, and the set of morphisms S′ satisﬁes
S′ =

s ∈K′ | H|K′(Ti(s)) is an isomorphism for all i
	
.
Hence Proposition 7.1.1 and Theorem 7.1.3 apply.
□
In the situation of the proposition, the localization functor is denoted by Q′ :
K′ →K′
S′.
Proposition 7.1.12. In the situation of Proposition 7.1.11, let F : K′ →E be a
triangulated functor into some triangulated category E. Assume that for every s ∈
S′, the morphism F(s) is an isomorphism in E. Then there is a unique triangulated
functor FS′ : K′
S′ →E that extends F; Namely FS′ ◦Q′ = F as functors K′ →E.
Proof. This is part of Theorem 7.1.3.
□
In particular we can look at the functor F : K′
inc
−−→K
Q
−→KS, and its extension
FS′ : K′
S′ →KS. We are interested in suﬃcient conditions for the functor FS′ to be
fully faithful.
Proposition 7.1.13. Let K be a triangulated category, let S be a denominator set
of cohomological origin in K, and let K′ ⊆K be a full triangulated subcategory.
Deﬁne S′ := K′ ∩S. Assume either of these conditions holds:
(r) Let M ∈Ob(K). If there exists a morphism s : M →L in S with L ∈
Ob(K′), there exists a morphism t : K →M in S with K ∈Ob(K′).
(l) Let M ∈Ob(K). If there exists a morphism s : L →M in S with L ∈
Ob(K′), there exists a morphism t : M →K in S with K ∈Ob(K′).
Then the functor FS′ : K′
S′ →KS is fully faithful.
131
Derived Categories
|
Amnon Yekutieli
|
14 Apr 2019
Proof. By Proposition 7.1.11, S′ is a multiplicatively closed set of cohomological
origin. So by Proposition 7.1.1 it is a right and left denominator set in K′. According
to Proposition 6.2.34, under condition (r) the functor FS′ is fully faithful.
For condition (l) we pass to the opposite categories, using Proposition 6.2.17.
□
Remark 7.1.14. Let K be a triangulated category, and let N ⊆K be a full trian-
gulated subcategory. Deﬁne S to be the set of morphisms s in K such that the cone
of s (see Deﬁnition 5.3.7) is isomorphic to an object of N. It turns out that S is a
left and right denominator set in K. We call S the denominator set associated to N.
The localization KS is a triangulated category, and it is called the Verdier quotient
of K by N, with notation K/N := KS. See [156, Chapter 2] or [75, Section 1.6].
We want to relate this to Remark 5.3.25. Let ˜S be a left and right denominator
set in K. A morphism s in K is called a divisor of ˜S if there exist morphisms u, v ∈K
such that u ◦s and s ◦v belong to ˜S. We call ˜S a saturated denominator set if it
contains all its divisors.
Let N ⊆K be a full triangulated subcategory, and let S be the associated de-
nominator set, as in the ﬁrst paragraph. Let ˜N be the saturated full triangulated
subcategory of K generated by N, in the sense of Deﬁnition 5.3.20. Let ˜S be the
set of morphisms gotten by adjoining to S all its divisors. Then ˜S is a saturated
left and right denominator set of morphisms in K, the canonical functor KS →K˜S
is an isomorphism, the kernel of the localization functor Q : K →KS (see Corollary
5.3.23) is ˜N, and ˜S is the denominator set associated to ˜N. This is proved in [156,
Chapter 2] and [76, Proposition 7.1.20].
An important example of a Verdier quotient is the passage from the homotopy
category K(A, M) to the derived category D(A, M), that we shall study in Sub-
section 7.2 below. Indeed, the set of quasi-isomorphisms S(A, M) in K(A, M) can
be described as the denominator set associated to the full subcategory N(A, M) ⊆
K(A, M) on the acyclic complexes, which is a saturated full triangulated subcate-
gory.
