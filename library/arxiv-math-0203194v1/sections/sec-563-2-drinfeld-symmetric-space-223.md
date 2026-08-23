---
doc_id: arxiv-math-0203194v1
doc_title: "Period mappings and differential equations. From C to Cp"
section_id: sec-563-2-drinfeld-symmetric-space-223
section_title: "DRINFELD SYMMETRIC SPACE. 223"
section_number: 2
pages: 227-229
source_pdf: 0203194v1.pdf
source_sha256: 6f35e530f07116dc
doc_brief: "Period mappings and differential equations. From C to Cp — 580 sections: INTRODUCTION; INTRODUCTION; INTRODUCTION"
---
canonical isomorphism V∼
= P(M )⊗RK due to the canonical isomorphism
M⊗RK∼
=V . So we get a bijection:
∆ 0
∼−→
{
(P,φ )
P ∼→ Pn
R,
φ : P⊗RK ∼→ P(V )
}
/∼,
where ( P1,φ 1) ∼ (P2,φ 2) if and only if there exists an R-isomorphism
Φ : P1
∼→ P2 which makes the diagram
P1⊗RK
Φ⊗RK
−→ P2⊗RK
φ1↓ ↓ φ2
P(V ) = P(V )
commutative.
Next we consider two vertices Λ 1 and Λ 2 which are adjacent with each
other. The canonical isomorphism between the generic ﬁbers induce a nat-
ural birational map between P(Λ 1) and P(Λ 2). More explicitly, taking rep-
resentatives Mi ∈ Λ i (i = 1, 2) so that M1 ⊋ M2 ⊋ πM1, we have the
birational map from P(Λ 1) to P(Λ 2) induced by M2֒→M1. We deﬁne the
join P(Λ 1)∨ P(Λ 2) to be the closure of the graph in P(Λ 1)×R P(Λ 2) of this
rational map. It is easily seen that the join P(Λ 1)∨ P(Λ 2) is R-isomorphic
to the blow-up of P(Λ 1) at the closed subscheme Proj(Sym kM1/M2). In
particular, the closed ﬁber of P(Λ 1)∨ P(Λ 2) consists of two rational varieties
intersecting transversally.
Lemma 2.1. The operation∨ is associative and commutative.
The proof is straightforward, and left to the reader. By the l emma, we
can extend the construction to any ﬁnite subcomplex of ∆. Mor e precisely,
for a ﬁnite subcomplex S, we take the joins of all vertices in S; the resulting
R-scheme is denoted by P(S). The scheme P(S) is a regular projective scheme
overR having the following properties:
(i) The generic ﬁber is canonically isomorphic to P(V ).
(ii) The closed ﬁber is a reduced normal crossing of non-sing ular rational
varieties of which the dual graph coincides with S.
We want to do this for a general convex subcomplex of ∆; this ca nnot
be done in terms of schemes because we have to consider a limit of blow-up’s
of Pn
R centered in the closed ﬁber. But we can do this in terms of form al
schemes, or rigid analytic spaces. Let ∆ ∗ be a convex subcomplex of ∆. For
any ﬁnite subcomplex S of ∆ ∗ we deﬁne ˆΩ( S) to be the completion of P(S)
along the closed ﬁber. Consider the maximal Zariski open sub set ˆΩ( S)′ of
ˆΩ( S) such that, for any ﬁnite subcomplex T of ∆ ∗ containing S, the induced
morphismρT
S : ˆΩ( T )→ˆΩ( S) gives an isomorphism restricted to the pull-back
of ˆΩ( S)′.
Deﬁnition 2.2. For a convex subcomplex ∆ ∗ of ∆ we deﬁne
ˆΩ(∆ ∗) : =
⋃
S: ﬁnite
ˆΩ( S)′,
224 B. OVER VIEW OF THEORY OF p-ADIC UNIFORMIZATION.
where S runs through all ﬁnite subcomplex of ∆ ∗. The corresponding rigid
analytic space (Raynaud generic ﬁber) is denoted by Ω(∆ ∗). In case ∆ ∗ = ∆
we simply write ˆΩ = ˆΩ(∆) and Ω = Ω(∆). The rigid analytic space Ω is
called the Drinfeld symmetric space .
The formal scheme ˆΩ(∆ ∗) is formally locally of ﬁnite type, of which the
closed ﬁber is the normal crossings of non-singular rationa l varieties having
the dual graph isomorphic to ∆ ∗. By deﬁnition, the group PGL( n + 1,K )
naturally acts on ˆΩ, and hence Ω.
Example 2.3. Let us consider ˆΩ in n = 2. The closed ﬁber ˆΩ 0 consists
of countably many components which are all isomorphic to the surface B
considered in 1.3. In each component every k-rational line is a double curve
in ˆΩ 0, and every k-rational point is a triple point.
Structure of Ω . First we note that, as a point set, we have an equality
Ω = Pn,an
K \
⋃
H ∈H
H,
whereH is the set of all K-rational hyperplanes.
Here we do not attempt to give a proof of this fact, but rather g ive a
sketchy explanation in order to get a feeling. We limit ourse lves to n = 1
case just for simplicity. The formal scheme ˆΩ is, roughly speaking, the limit
of successive blow-up’s
···−→ Ui
ρi
−→Ui−1−→···−→ U0
with U0 = P1
R and ρi the blow-up centered at all the k-rational points in
the closed ﬁber of Ui−1. Let z be a point in the generic ﬁber P1
K of each
Ui. We consider the closure
z of z in each Ui. Since Ui is a regular scheme,
the section z intersects the closed ﬁber at a smooth point transversally. If
z is not a K-rational point, then for suﬃciently large N , z intersects the
closed ﬁber of Ui at a non- k-rational smooth point for i > N. But, if z is
K-rational,z intersects the closed ﬁber always at a k-rational point which is
in the next blow-up center. So if we consider the limit, such f ormal sections
determined by K-rational points does not exist any more, while those by
non-K-rational points certainly exist. This explains the above e quality in
n = 1. For higher n we can apply the similar argument.
Next we discuss the analytic structure of Ω; viz. we show how t o in-
troduce an admissible covering to Ω; since we have construct ed the rigid
analytic space Ω from the formal model, we must have one such c overing
such that the associated formal model recovers ˆΩ. This can be actually
described in an elegent way in terms of norms: A non-negative real valued
function α : V→ R≥0 is said to be a norm overK if it satisﬁes:
(i) α(x)> 0 whenever x⁄= 0.
(ii) For a∈K, α(ax) =|a|α(x).
(iii) α(x +y)≤ max{α(x),α (y)}.
