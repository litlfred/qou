---
doc_id: arxiv-0908.4305v3
doc_title: "Higher Dimensional Algebra VII: Groupoidification"
section_id: sec-008-61-scalar-multiplication
section_title: "Scalar Multiplication"
section_number: 6.1
pages: 52-56
source_pdf: 0908.4305v3.pdf
source_sha256: ab8d2b335b026a36
doc_brief: "Higher Dimensional Algebra VII: Groupoidification — Groupoidiﬁcation is a form of categoriﬁcation in which vect or spaces are replaced by groupoids and linear operators are replaced by spans of"
---
is a functor. Finally, we prove the results about inner products and adjoints.
6.1 Scalar Multiplication
To prove facts about scalar multiplication, we use the following lemma:
Lemma 38. Given a groupoid Λ and a functor between groupoids p : X →Y ,
then the functor c ×p : Λ ×Y → 1 ×X (wherec : Λ → 1 is the unique morphism
from Λ to the terminal groupoid 1) satisﬁes:
|(c ×p)−1(1,x )| = |Λ | |p−1(x)|
for all x ∈X.
Proof. By the deﬁnition of full inverse image we have
(c ×p)−1(1,x ) ∼= Λ ×p−1(x).
In the product Λ ×p−1(x), an automorphism of an object ( λ,y ) is an automor-
phism of λ together with an automorphism of y. We thus obtain
|(c ×p)−1(1,x )| =
∑
[λ ]∈Λ
∑
[y]∈p−1(x)
1
|Aut(λ)|
1
|Aut(y)|
which is equal to |Λ | |p−1(x)|, as desired.
Proposition 39. Given a groupoid Λ and a groupoid over X, say v : Ψ →X,
the groupoid Λ × Ψ over X satisﬁes
Λ × Ψ
~
= |Λ |Ψ
~
.
Proof. This follows from Lemma 38.
Proposition 40. Given a tame groupoid Λ and a tame span
S
/d127/d127/d127/d127/d127/d127/d127/d127/d127
/d31/d31/d64/d64/d64/d64/d64/d64/d64
Y X
52
then Λ ×S is tame and
Λ ×S
~
= |Λ |S
~
.
Proof. This follows from Lemma 38.
6.2 Functoriality of Degroupoidiﬁcation
In this section we prove that our process of turning groupoids into vector spaces
and spans of groupoids into linear operators is indeed a functor. We ﬁrst show
that the process preserves identities, then show associativity of composition,
from which many other things follow, including the preservation of co mposition.
The lemmas in this section add up to a proof of the following theorem:
Theorem 41. Degroupoidiﬁcation is a functor from the category of groupo ids
and equivalence classes of tame spans to the category of real vector spaces and
linear operators.
Proof. As mentioned above, the proof follows from Lemmas 42 and 44.
Lemma 42. Degroupoidiﬁcation preserves identities, i.e., given a gr oupoidX,
1X
~
= 1 R
X
~
, where 1X is the identity span from X to X and 1R
X
~
is the identity
operator on RX
~ .
Proof. This follows from the explicit formula given in Theorem 36.
We now want to prove the associativity of composition of tame spans. Amongst
the consequences of this proposition we can derive the preservat ion of composi-
tion under degroupoidiﬁcation. Given a triple of composable spans:
T
qT
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pT
/d31/d31/d64/d64/d64/d64/d64/d64/d64 S
qS
/d127/d127/d127/d127/d127/d127/d127/d127/d127 pS
/d31/d31/d64/d64/d64/d64/d64/d64/d64 R
qR
/d126/d126/d126 /d126/d126 /d126 /d126/d126 /d126 pR
/d32/d32/d65/d65/d65/d65/d65/d65/d65/d65
Z Y X W
we want to show that composing in the two possible orders— T (SR) or (TS )R—
will provide equivalent spans of groupoids. In fact, since groupoids , spans of
groupoids, and isomorphism classes of maps between spans of grou poids natu-
rally form a bicategory, there exists a natural isomorphism called th e associa-
tor. This tells us that the spans T (SR) and (TS )R are in fact equivalent. But
since we have not constructed this bicategory, we will instead give a n explicit
construction of the equivalence T (SR)
∼
→ (TS )R.
Proposition 43. Given a composable triple of tame spans, the operation of
composition of tame spans by weak pullback is associative up to equivalence of
spans of groupoids.
53
Proof. We consider the above triple of spans in order to construct the afo re-
mentioned equivalence. The equivalence is simple to describe if we ﬁrst take
a close look at the groupoids T (SR) and ( TS )R. The composite T (SR) has
objects (t, (s,r,α ),β ) such that r ∈ R, s ∈ S, t ∈ T , α : qR(r) → pS(s), and
β : qS(s) →pT (t), and morphisms f : (t, (s,r,α ),β ) → (t′, (s′,r ′,α ′),β ′), which
consist of a map g : (s,r,α ) → (s′,r ′,α ′) in SR and a map h : t →t′ such that
the following diagram commutes:
qSπs((s,r,α ))
β /d47/d47
qS π S(g)
/d15/d15
pT (t)
pT (h)
/d15/d15
qSπs((s′,r ′,α ′))
β ′
/d47/d47pT (t′)
where πS maps the composite SR to S. Further, g consists of a pair of maps
k : r →r′ and j :s →s′ such that the following diagram commutes:
qR(r) α /d47/d47
qS (k)
/d15/d15
pS(s)
pS (j)
/d15/d15
qR(r′)
α ′
/d47/d47pS(s′)
The groupoid (TS )R has objects ((t,s,α ),r,β ) such thatr ∈R,s ∈S,t ∈T ,
α : qS(s) → pT (t), and β : qR(r) → pS(s), and morphisms f : ((t,s,α ),r,β ) →
((t′,s ′,α ′),r ′,β ′), which consist of a map g : (t,s,α ) → (t′,s ′,α ′) in TS and a
map h : r →r′ such that the following diagram commutes:
pR(r)
pR(h)
/d15/d15
β /d47/d47pSπs((t,s,α ))
pS π S(g)
/d15/d15
pR(r′)
β ′
/d47/d47pSπs((t′,s ′,α ′))
Further, g consists of a pair of maps k : s → s′ and j : t → t′ such that the
following diagram commutes:
qS(s) α /d47/d47
qS (k)
/d15/d15
pT (t)
pT (j)
/d15/d15
qS(s′)
α ′
/d47/d47pT (t′)
We can now write down a functor F :T (SR) → (TS )R:
(t, (s,r,α ),β ) ↦→((t,s,β ),r,α )
54
Again, a morphismf : (t, (s,r,α ),β ) → (t′, (s′,r ′,α ′),β ′) consists of mapsk :r →
r′, j : s → s′, and h : t → t′. We need to deﬁne F (f ) : ((t,s,β ),r,α ) →
((t′,s ′,β ′),r ′,α ′). The ﬁrst component g′ : (t,s,β ) → (t′,s ′,β ′) consists of the
maps j : s →s′ and h : t →t′, and the following diagram commutes:
qS(s)
β /d47/d47
qS (j)
/d15/d15
pT (t)
pT (h)
/d15/d15
qS(s′)
β ′
/d47/d47pT (t′)
The other component map of F (f ) is k : r → r′ and we see that the following
diagram also commutes:
pR(r)
pR(k)
/d15/d15
α /d47/d47pSπs((t,s,β ))
pS π S (g′)
/d15/d15
pR(r′)
α ′
/d47/d47pSπs((t′,s ′,β ′))
thus, deﬁning a morphism in ( TS )R.
We now just need to check that F preserves identities and composition and
that it is indeed an isomorphism. We will then have shown that the apex es of the
two spans are isomorphic. First, given an identity morphism 1 : ( t, (s,r,α ),β ) →
(t, (s,r,α ),β ), then F (1) is the identity morphism on (( t,s,β ),r,α ). The com-
ponents of the identity morphism are the respective identity morph isms on the
objects r,s, and t. By the construction of F , it is clear that F (1) will then be
an identity morphism.
Given a pair of composable maps f : (t, (s,r,α ),β ) → (t′, (s′,r ′,α ′),β ′) and
f ′ : (t′, (s′,r ′,α ′),β ′) → (t′′, (s′′,r ′′,α ′′),β ′′) in T (SR), the composite is a map
f ′f with components g′g : (s,r,α ) → (s′′,r ′′,α ′′) and h′h : t →t′′. Further, g′g
has component morphisms k′k : r →r′′ andj′j : s →s′. It is then easy to check
that under the image of F this composition is preserved.
The construction of the inverse of F is implicit in the construction of F , and
it is easy to verify that each composite FF −1 andF −1F is an identity functor.
Further, the natural isomorphisms required for an equivalence of spans can each
be taken to be the identity.
It follows from the associativity of composition that degroupoidiﬁca tion pre-
serves composition:
Lemma 44. Degroupoidiﬁcation preserves composition. That is, given a pair
of composable tame spans:
T
/d31/d31/d64/d64/d64/d64/d64/d64/d64
/d127/d127/d127/d127/d127/d127/d127/d127/d127 S
/d31/d31/d64/d64/d64/d64/d64/d64/d64
/d127/d127/d127/d127/d127/d127/d127/d127/d127
Z Y X
55
we have
T
~
S
~
=TS
~
.
Proof. Consider the composable pair of spans above along with a groupoid Ψ
overX:
T
/d31/d31/d64/d64/d64/d64/d64/d64/d64
/d127/d127/d127/d127/d127/d127/d127/d127/d127 S
/d31/d31/d64/d64/d64/d64/d64/d64/d64
/d127/d127/d127/d127/d127/d127/d127/d127/d127 Ψ
/d31/d31/d63/d63/d63/d63/d63/d63/d63/d63
/d126/d126/d126 /d126/d126 /d126 /d126/d126 /d126
Z Y X 1
We can consider the groupoid over X as a span by taking the right leg to be the
unique map to the terminal groupoid. We can compose this triple of sp ans in
two ways; either T (SΨ) or ( TS )Ψ. By the Proposition 43 stated above, these
spans are equivalent. By Theorem 35, degroupoidiﬁcation produce s the same
linear operators. Thus, composition is preserved. That is,
T
~
S
~
Ψ
~
=TS
~
Ψ
~
.
