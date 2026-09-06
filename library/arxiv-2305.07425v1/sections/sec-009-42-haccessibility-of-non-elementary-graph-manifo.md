---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-009-42-haccessibility-of-non-elementary-graph-manifo
section_title: "H–accessibility of non-elementary graph manifolds"
section_number: 4.2
pages: 12-16
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a grou p G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
non-elementary graph manifold with Seifert ﬁbered pieces M1,...,M k in its torus decompo-
sition. There is an induced graph-of-groups structure G on π1(M ) with underlying graph Γ
as follows. There is a vertex of Γ for each Mi, with vertex group π1(Mi). Each edge group is
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 13
Z2, the fundamental group of a torus in the decomposition. The e dge monomorphisms come
from the two diﬀerent gluings of the torus into the two adjacen t Seifert ﬁbered components.
With this graph of groups structure, π1(M ) is a Croke-Kleiner admissible group.
The universal cover ~M of M is tiled by a countable collection of copies of the universal
covers ~M1,..., ~Mk. We call these subsets vertex spaces. We refer to boundary components of
vertex spaces as edge spaces. Two vertex spaces are either disjoint or intersect along an edge
space. Let T be the Bass-Serre tree of G.
Applying Theorem 1.4 to the Croke-Kleiner admissible group π1(M ), we obtain a cover
M ′ → M of degree 2 such that π1(M ′) is not H–accessible. However, this is not enough to
conclude H–inaccessibility of π1(M ), as it is unknown whether H–inaccessibility of a ﬁnite
index subgroup passes to the ambient group. In this section, we will show that π1(M ) itself
is H–inaccessible; see Proposition 4.8.
We begin with a lemma. Let πα(β) be the closest point projection of a line β to a line α
in a hyperbolic space. Let dα(·, ·) be in the resulting projection distances.
Lemma 4.7. LetF be a 2-dimensional hyperbolic orbifold with nonempty bound ary and uni-
versal cover ~F , and let L be the collection of boundary lines of ~F . For any α ∈ L and any
loxodromicγ ∈π1(F ) whose axis in ~F is also a line in L, the following holds. There exists a
constantλ> 0 such that for any n ∈ Z and any line β ∈ L \ {α,γ n(α)}, we have
dβ(α,γ n(α)) ≤λ.
The proof of this lemma is very similar to that of [AR19, Lemma 5.6]. We refer the reader to
that paper for some ﬁgures that may be helpful; see in particu lar [AR19, Figure 8].
Proof of Lemma 4.7. Since L is a π1(F )–invariant collection of axes in the hyperbolic plane
H2, it follows from Example 2.8 that ( L,π ℓ) satisﬁes the projection axioms for some constant
ξ. In particular, there exists a constant ξ >1 such that diam(πℓ(ℓ′)) ≤ξ for distinct elements
ℓ and ℓ′ in L. Let
λ = max{ξ,d (α,γ (α)) + 2ξ,d (α,γ 2(α)) + 2ξ}.
Let ℓ ∈ L denote the axis of γ in ~F . If ℓ =α, then
dβ(α,γ n(α)) = dβ(α,α ) ≤ξ ≤λ,
and the result holds. For the remainder of the proof, we assum eℓ ⁄=α and consider two cases.
Case 1 : β /∈ {γk(α) |k ∈ Z}
In this case, there exists a unique k0 ∈ Z such thatβ lies betweenγk0(α) andγk0+1(α). That
is, ∂H2 minus the endpoints of γk0(α) and γk0+1(α) consists of four intervals, one containing
the endpoints of β, one containing the endpoints of all γi(α) for i /∈ {k0,k 0 + 1}, and the
other two disjoint from all endpoints of lines in L. Fixing an appropriate orientation on β,
we partially order sub-intervals I = [x,y ] and J = [z,w ] of β (with x ≤y and z ≤ w in the
orientation) by I ≤ J if x ≤ z and y ≤ w. Then the projections of the lines γk(α) onto β
occur in the following order
πβ(γk0(α))<π β(γk0−1(α))<π β(γk0−2(α))<...<π β(ℓ)
and
πβ(ℓ)<...<π β(γk0+3(α))<π β(γk0+2(α))<π β(γk0+1(α)).
Thus
dβ(α,γ n(α)) ≤dβ(γk0(α),γ k0+1(α)) ≤d(γk0(α),γ k0+1(α)) + 2ξ,
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 14
whered(γk0(α),γ k0+1(α)) denotes the distance between γk0(α) andγk0+1(α) in the hyperbolic
plane. The ﬁnal inequality follows from the fact that the nea rest point projection is a 1–
Lipschitz map and that πℓ(ℓ′) has diameter at most ξ for any distinct lines ℓ,ℓ ′ ∈ L. Since
d(γk0(α),γ k0+1(α))) = d(α,γ (α)), it follows that
dβ(α,γ n(α)) ≤d(α,γ (α)) + 2ξ ≤λ.
Case 2 : β =γk(α) for some integer k ⁄= 0,n . Using an analogous argument to Case 1, we see
that dβ(α,γ n(α)) is bounded above by
dβ(γk−1(α),γ k+1(α)) ≤d(α,γ 2(α)) + 2ξ ≤λ. □
Proposition 4.8. The fundamental group of a non-elementary graph manifold is H–inaccessible.
Proof. Let G be the graph-of-groups structure on π1(M ) with underlying graph Γ described at
the beginning of this section. The assumption that the graph manifold M is non-elementary
ensures that there are at least two vertices in the graph Γ. We divide the proof into two cases,
depending on the location of loops in Γ.
Fix an edge α in Γ that is not a loop, and label the vertex α− byµ and the vertex α+ by
ω. Let Tα be the torus in M associated to the edge α. Let v and w be two adjacent vertices
in the tree T such that ~Mv and ~Mw are the universal covers of the Seifert pieces Mµ andMω,
respectively. Let zµ and zω be the generators of Zµ and Zω, respectively.
Case 1: Suppose there is no loop in Γ based at the vertex µ. Let
Wµ :=
{
Lv
⏐⏐ ~Mv is a lift of the Seifert ﬁbered piece Mµ
}
If Lv and Lv′ are two distinct elements in Wµ, then d(v,v ′) ≥ 2 (though they are not
necessarily an even distance apart). In this case, the techn iques in Section 3 apply to show
that there is a cobounded action π1(M ) ↷ CK (Wµ) such that zµ is loxodromic and zω is
elliptic.
Case 2: Suppose there is a loop in Γ based at the vertex µ.
As in Section 3, we partition the vertex set T 0 into two disjoint collections of vertices V1
and V2 such that if z and z′ both lie in Vi then d(z,z ′) is even. Applying Theorem 1.4 to
the Croke-Kleiner admissible group π1(M ), we obtain a degree 2 cover M ′ → M such that
π1(M ′) is H–inaccessible and π1(M ′) preserves V1 and V2.
Assume without loss of generality that v is in V1 and w is in V2. Let
Qµ :=
{
Lu
⏐⏐u ∈ V1 and ~Mu is a lift of Mµ}
The results in Section 3 still hold for Qµ, and thus we obtain quasi-trees of spaces CK (Qµ) for
suﬃciently large K. Since π1(M ′) preserves Qµ, we obtain an action π1(M ′) ↷ CK(Qµ) as in
Section 3.
Passing to a power of two if necessary, we may assume that zµ,z ω ∈ π1(M ′). As shown
in the proof of Theorem 1.4, the element zµ acts loxodromically on CK(Qµ), while zω acts
elliptically on CK(Qµ). By the construction of CK(Qµ), and since vertex groups are central
extensions of Z, the element zµ is a WWPD + element in the action π1(M ′) ↷ CK(Qµ).
Hence Proposition 2.5 provides a homogeneous quasimorphis m qK : π1(M ′) → R satisfying
qK(zω) = 0 and qK(zµ) ⁄= 0.
Our goal is to extend qK to a homogeneous quasimorphism π1(M ) → R while ensuring
that zω and zµ still have trivial and non-trivial image, respectively. Le t h ∈ π1(M ) be a
representative of the non-trivial coset of π1(M ′) in π1(M ). Deﬁne a function q′
K : π1(M ′) → R
by
q′
K(x) :=qK(x) +qK(hxh−1).
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 15
Note that q′
K is constant on conjugacy classes of π1(M ), i.e., q′
K(yxy −1) = q′
K(x) for any
y ∈π1(M ) and x ∈π1(M ′)). Hence it follows from the proof of [BF09, Lemma 7.2] that q′
K
extends to a homogeneous quasimorphism ρK : π1(M ) → R deﬁned by ρK (x) :=q′
K(x2)
/
2 for
eachx ∈π1(M ).
Lemma 4.9. Suppose there is a loop in Γ based atµ. For K large enough, we have ρK(zω) = 0
and ρK (zµ) ⁄= 0.
We defer the proof of the lemma for the moment and assume this r esult to complete the
proof Proposition 4.8. Since ρK : π1(M ) → R is a nonzero homogeneuous quasimorphism, we
obtain from Proposition 2.6 an action π1(M ) ↷ L on a quasi-line. Moreover, since ρK(zµ) ⁄= 0
and ρK (zω) = 0, the element zµ is loxodromic while zω is elliptic in this action.
Now, consider the other endpoint ω ofα. Suppose ﬁrst there is not a loop in Γ based at ω.
Interchanging the roles of µ andω in Case 1 above produces an action π1(M ) ↷ CK(Wω) such
thatzµ is elliptic and zω is loxodromic. On the other hand, if there is a loop in Γ based a tω,
then interchanging the roles of µ andω in Case 2 above produces an action π1(M ) ↷ L′ on a
quasi-line in which (after possibly passing to a power of 2) zµ is elliptic and zω is loxodromic.
Regardless of which combination of cases holds for the verti cesµ andω, we have produced
two actions on hyperbolic spaces and two commuting elements zµ and zω which satisfy the
conditions of Lemma 2.3, which concludes the proof. □
We now prove Lemma 4.9.
Proof of Lemma 4.9. Recall that v ∈ V 1. As h ∈π1(M ) is a representative of the non-trivial
coset of π1(M ′) in π1(M ), we have hv ∈ V 2. Note that ~Mhv is also a lift of Mµ, even though
hv is not in V1. Fix a vertex v0 adjacent to hv such that ~Mv0 is a lift of Mµ in ~M . This
ensures that Lv0 is in Q1. Let l ∈ Lhv be the boundary line of ~Fhv corresponding to the edge
[v0,hv ].
We will ﬁrst show that ρK(zω) = 0. Since qK is a homogeneous quasimorphism and
zω ∈π1(M ′), we have that
ρK(zω) = q′
K(zω) = qK(zω) +qK(hzωh−1) = 0 + qK(hzωh−1).
By Proposition 2.5, to show ρK(zω) = qK(hzωh−1) = 0, it suﬃces to show that hzωh−1 is
elliptic in the action π1(M ′) ↷ CK(Q1). Let ξ >0 be the projection constant of the projection
complexes Q1 and Q2. Since Mhv is a Seifert ﬁbered piece, we have ~Mhv = ~Fhv × R, where
Fhv is the base orbifold of Mhv. Applying Lemma 4.7 to the space Fhv, the collection of
boundary lines of ~Fhv, the ﬁxed boundary line l, and the chosen element γ = hzωh−1, we
obtain a constant λ> 0. We further enlarge λ so that it satisﬁes Lemma 3.4.
ChooseK >4ξ + 4 + 2λ +λ2 large enough to apply Proposition 2.9, and let y0 be a point in
the projection of Lhzω h−1v0 toLv0. We will show that dCK (Q1)(y0,γ n(y0)) ≤ 6K for all n ∈ Z,
which will imply that γ is elliptic in the action π1(M ′) ↷ CK (Q1), as desired.
Fix n ∈ Z. By Proposition 2.9, we have
(2) dCK (Q1)(y0,γ n(y0)) ≤ 4
∑
u∈V1
Lu ∈ Q1
[dLu (y0,γ n(y0))]K + 6K.
Thus it suﬃces to show that dLu (y0,γ n(y0)) < K for all u ∈ V 1 such that Lu ∈ Q1. Since
Lu ∈ Q1, ~Mu is a lift of Mµ.
We divide the proof into several cases, depending on the loca tion of the vertex u.
Case 1: u ∈ {v0,γ n(v0)}. We assume that u =v0 as the case u =γn(v0) is proved similarly.
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 16
By assumption, y0 ∈Lv0, and so γn(y0) ∈Lγn(y0). By deﬁnition,
dLv0 (y0,γ n(y0)) = diam( {y0} ∪ Π Lv0 (Lγn(v0)))
and
dLv0 (Lγ(v0),L γn(v0)) = diam
(
Π Lv0 (Lγ(v0)) ∪ Π Lv0 (Lγn(v0))
)
.
As y0 ∈ Π Lv0 (Lγ(v0)) and the diameter of Π Lv0 (Lγ(v0)) is no more than ξ, it follows that
(3)
⏐⏐dLv0 (y0,γ n(y0)) −dLv0 (Lγ(v0),L γn(v0))
⏐⏐ ≤ 2ξ.
The line l is the boundary line of ~Fhv associated to the edge [ v0,hv ]. Recall that zω is an
element of the edge group G[v,w], and so it ﬁxes the vertex v. Thus γ(hv) = hzωh−1(hv) =
hzω(v) = hv, and so the lines γ(l) and γn(l) are the boundary lines in ~Fhv associated to the
edges [hv,γ (v0)] and [hv,γ n(v0)], respectively.
Combining (3) with Lemmas 3.4 and 4.7 implies that
dLv0 (y0,γ n(y0)) ≤dLv0 (Lγ(v0),L γn(v0)) + 2ξ
≤λdl(γ(l),γ n(l)) +λ + 2ξ
=λd γ−1(l)(l,γ n−1(l)) +λ + 2ξ ≤λ2 +λ + 2ξ <K.
Case 2: u ∈ Lk(hv) but u ⁄∈ {v0,γ n(v0)}. Let b be the boundary line of ~Fhv corresponding
to the edge [ u,hv ], so that b /∈ {l,γ n(l)}. By Lemma 4.7, we have that db(l,γ n(l)) ≤ λ. It
follows from Lemma 3.4 that
dLu (y0,γ n(y0)) = dLu(Lv0,L γn(v0))
≤λd b(l,γ n(l)) +λ
≤λ2 +λ<K.
Case 3: u ⁄∈Lk(hv). In this case, d(u, [v0,γ n(v0)]) ≥ 2, and so
dLu(y0,γ ny0) = dLu(Lv0,L γn(v0)) ≤λ<K.
We have shown that dLu(y0,γ n(y0)) < K for all u ∈ V 1 such that Lu ∈ Q1. Therefore
(2) shows that dCK (Q1)(y0,γ n(y0)) ≤ 6K for all n. It follows that γ is elliptic in the action
π1(M ′) ↷ CK (Q1), and so q(zω) = 0.
To complete the proof, we need to verify that
ρK (zµ) = q′
K(zµ) = qK(zµ) +qK(hzµh−1) ⁄= 0.
Since hzµh−1 is a central element in Ghv = Stab G(hv), it follows from Remark 2.13 that
hzµh−1 acts elliptically on Lv0, and thus also on CK (Q1). By Proposition 2.5, we have
qK(hzµh−1) = 0. Since qK(zµ) ⁄= 0, it follows that ρK(zµ) ⁄= 0. □
Theorem 1.3 now follows immediately from Corollary 4.6 and P roposition 4.8.
