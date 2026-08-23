---
doc_id: arxiv-1004.1533v3
doc_title: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT"
section_id: sec-002-1-preliminaries-i-spherical-categories
section_title: "Preliminaries I: spherical categories"
section_number: 1
pages: 2-6
source_pdf: 1004.1533v3.pdf
source_sha256: 95c1544431e6bf37
doc_brief: "TURAEV-VIRO INVARIANTS AS AN EXTENDED TQFT — In this paper we show how one can extend Turaev-Viro invarian ts, deﬁned for an arbitrary spherical fusion category C, to 3-manifolds with cor- ners."
---
In this section we collect notation and some facts about spherical c ategories.
We ﬁx an algebraically closed ﬁeld k of characteristic 0 and denote by Vec the
category of ﬁnite-dimensional vector spaces over k.
Throughout the paper, C will denote a spherical fusion category over k. We
refer the reader to the paper [DGNO] for the deﬁnitions and prop erties of such
categories. Note that we are not requiring a braiding on C.
In particular, C is semisimple with ﬁnitely many isomorphism classes of simple
objects. We will denote by Irr( C) the set of isomorphism classes of simple objects.
We will also denote by 1 the unit object in C (which is simple).
Two main examples of spherical categories are the category VecG of ﬁnite-
dimensional G-graded vector spaces (where G is a ﬁnite group) and the category
Rep(Uqg) which is the semisimple part of the category of representations of a quan-
tum group Uqg at a root of unity; this last category is actually modular, but we
will not be using this.
To simplify the notation, we will assume that C is a strict pivotal category, i.e.
that V ∗∗ = V . As is well-known, this is not really a restriction, since any pivotal
category is equivalent to a strict pivotal category.
We will denote, for an object X of C, by
dX = dimX ∈ k
its categorical dimension; it is known that for simple X, dX is non-zero. We will
ﬁx, for any simple object Xi ∈ C , a choice of square root √
dX so that for X = 1,√d1 = 1 and that for any simple X, √dX = √dX ∗ .
We will also denote
(1.1) D =
√ ∑
x∈Irr(C)
d2
X
(throughout the paper, we ﬁx a choice of the square root). Note that by results of
[ENO2005], D ⁄= 0.
We deﬁne the functor C⊠n → Vec by
(1.2) ⟨V1,...,V n⟩ = Hom C(1,V 1 ⊗ · · · ⊗Vn)
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 3
for any collection V1,...,V n of objects of C. Note that pivotal structure gives
functorial isomorphisms
(1.3) z : ⟨V1,...,V n⟩ ≃ ⟨Vn,V 1,...,V n−1⟩
such that zn = id (see [BK2001, Section 5.3]); thus, up to a canonical isomorphism,
the space ⟨V1,...,V n⟩ only depends on the cyclic order of V1,...,V n.
We have a natural composition map
(1.4)
⟨V1,...,V n,X ⟩ ⊗ ⟨X ∗,W 1,...,W m⟩ → ⟨V1,...,V n,W 1,...,W m⟩
ϕ ⊗ψ ↦→ϕ ◦
X
ψ = ev X ◦(ϕ ⊗ψ )
where ev X : X ⊗X ∗ → 1 is the evaluation morphism. It follows from semisimplicity
of C that direct sum of these composition maps gives a functorial isomor phism
(1.5)
⨁
X∈Irr(C)
⟨V1,...,V n,X ⟩ ⊗ ⟨X ∗,W 1,...,W m⟩ ≃ ⟨V1,...,V n,W 1,...,W m⟩.
Note that for any objects A,B ∈ Obj C, we have a non-degenerate pairing
HomC(A,B ) ⊗ HomC(A∗,B ∗) → k deﬁned by
(1.6) ( ϕ,ϕ ′) = ( 1
coevA
− − − − →A ⊗A∗ ϕ ⊗ϕ ′
− − − →B ⊗B∗ evB
− − →1)
In particular, this gives us a non-degenerate pairing ⟨V1,...,V n⟩⊗⟨V ∗
n,...,V ∗
1 ⟩ → k
and thus, functorial isomorphisms
(1.7) ⟨V1,...,V n⟩∗ ≃ ⟨V ∗
n,...,V ∗
1 ⟩
compatible with the cyclic permutations (1.3).
We will frequently use graphical representations of morphisms in th e category
C, using tangle diagrams as in [Tur1994] or [BK2001]. However, our con vention
is that of [BK2001]: a tangle with k strands labeled V1,...,V k at the bottom
and n strands labeled W1,...,W n at the top is considered as a morphism from
V1 ⊗ · · · ⊗Vk →W1 ⊗ · · · ⊗Wn. As usual, by default all strands are oriented going
from the bottom to top. Note that since C is assumed to be a spherical category
and not a braided one, no crossings are allowed in the diagrams.
For technical reasons, it is convenient to extend the graphical ca lculus by allow-
ing, in addition to rectangular coupons, also circular coupons labeled with mor-
phisms ϕ ∈ ⟨V, 1...,V n⟩. This is easily seen to be equivalent to the original for-
malism: every such circular coupon can be replaced by the usual rec tangular one
as shown in Figure 1.
ϕ
V1 Vn
= ϕ
V1 Vn
Figure 1. Round coupons
We will also use the following convention: if a ﬁgure contains a pair of cir cular
coupons, one with outgoing edges labeled V1,...,V n and the other with edges la-
beled V ∗
n,...,V ∗
1 , and the coupons are labeled by pair of letters ϕ,ϕ ∗ (or ψ,ψ ∗,
4 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
or . . . ) it will stand for summation over the dual bases:
(1.8)
ϕ
V1 Vn
ϕ ∗
V ∗
n V ∗
1
=
∑
α
ϕ α
V1 Vn
ϕ α
V ∗
n V ∗
1
where ϕ α ∈ ⟨V1,...,V n⟩, ϕ α ∈ ⟨V ∗
n,...,V ∗
1 ⟩ are dual bases with respect to pairing
(1.6).
The following lemma, proof of which is left to the reader, lists some pro perties
of this pairing and its relation with the composition maps (1.4).
Lemma 1.1.
(1) If X is simple and ϕ ∈ ⟨X,A ⟩, ϕ ′ ∈ ⟨A∗,X ∗⟩ then
ϕ ′
ϕ
X A X ∗A∗
= (ϕ,ϕ ′)
dX
X X ∗
(2)
∑
i∈Irr(C)
di ϕ ϕ ∗
... ...
V1 Vn Vn V1
Xi
=
... ...
V1
Vn
(we use here convention (1.8)).
(3) If X is simple, ϕ ∈ ⟨A,X ⟩, ϕ ′ ∈ ⟨X ∗,A ∗⟩, ψ ∈ ⟨X ∗,B ⟩, ψ ′ ∈ ⟨B∗,X ⟩,
then
(1.9) ( ϕ ◦
X
ψ,ψ ′ ◦
X ∗ϕ ′) = 1
dX
(ϕ,ϕ ′)(ψ ′,ψ )
(see Figure 2).
ϕ ψ ′ψ ϕ ′
A BX X ∗
= (ϕ,ϕ ′)
dX
ϕ ϕ ′
A X
= (ϕ,ϕ ′)(ψ ′,ψ )
dX
Figure 2. Compatibility of pairing with composition.
Corollary 1.2. LetX be a simple object. Deﬁne the rescaled composition map
(1.10)
⟨V1,...,V n,X ⟩ ⊗ ⟨X ∗,W 1,...,W m⟩ → ⟨V1,...,V n,W 1,...,W m⟩
ϕ ⊗ψ ↦→ϕ •
X
ψ =
√
dX evX ◦(ϕ ⊗ψ )
TURAEV-VIRO INV ARIANTS AS AN EXTENDED TQFT 5
Then the rescaled composition map agrees with the pairing:
(ϕ •
X
ψ,ψ ′ •
X ∗ϕ ′) = (ϕ,ϕ ′)(ψ ′,ψ )
(same notation as in (1.9)).
The following result, which easily follows from Lemma 1.1, will also be very
useful.
Lemma 1.3. If the subgraphs A, B are not connected, then
A
ϕ ϕ ∗
BV1
Vn
V1
Vn
=
A B
V1
Vn
Finally, we will need the following result, which is the motivation for the n ame
“spherical category”.
Let Γ be an oriented graph embedded in the sphere S2, where each edge e
is colored by an object V (e) ∈ C , and each vertex v is colored by a morphism
ϕ v ∈ ⟨V (e1)±,...V (en)±⟩, where e1,...,e n are the edges adjacent to vertex v,
taken in clockwise order, and V (ei)± =V (ei) if ei is outgoing edge, and V ∗(ei) if
ei is the incoming edge.
By removing a point from S2 and identifying S2 \pt ≃ R2, we can consider Γ as
a planar graph. Replacing each vertex v by a circular coupon labeled by morphism
ϕ v as shown in Figure 3, we get a graph of the type discussed above and which
therefore deﬁnes a number ZRT (Γ) ∈ k (see, e.g., [BK2001] or [Tur1994]).
C
A B
D E
F
Figure 3. Graph on a sphere and its “ﬂattening” to the plane
Theorem 1.4. [BW1996] The number ZRT (Γ) ∈ k does not depend on the choice
of a point to remove from S2 or on the choice of order of edges at vertices compatible
with the given cyclic order and thus deﬁnes an invariant of co lored graphs on the
sphere.
6 BENJAMIN BALSAM AND ALEXANDER KIRILLOV, JR.
