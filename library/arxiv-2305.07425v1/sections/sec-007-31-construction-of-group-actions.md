---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-007-31-construction-of-group-actions
section_title: "Construction of group actions"
section_number: 3.1
pages: 8-10
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a grou p G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
≤ 2 subgroup G′. For each vertex v in the Bass-Serre tree T , let Lv be the quasi-line from
Deﬁnition 2.14. Recall that gLv =Lgv for any group element g in G.
Let L1 be the collection of quasi-lines {Lv}v∈V1 and L2 be the collection of quasi-lines
{Lv}v∈V2. We deﬁne a projection of Lv to Lv′ in Li as follows.
Deﬁnition 3.2 (Projection maps in Li). For any two distinct verticesv,v ′ ∈ V i, let e′ = [w,u ]
and e = [u,v ] denote the last two (oriented) edges in [ v′,v ]. The projection from Lv′ into Lv
is
Π Lv (Lv′ ) :=ψe(projℓ¯e(ℓe′)),
where ψe : ℓ¯e →Lv and proj ℓ¯e : Hu →ℓ¯e are the maps introduced in Section 2.
The fact that d(v,v ′) is even is not necessary for Deﬁnition 3.2, only that d(v,v ′) ≥ 2.
We will verify that the Li with these projection maps satisfy the projection axioms (s ee Def-
inition 2.7) for i = 1, 2. Let dLa(Lb,L c) be the projection distance diam
(
Π La(Lb) ∪ Π La (Lb)
)
.
Lemma 3.3. There exists a constant λ >0 such that diam(Π Lv (Lv′ )) ≤ λ for any distinct
v,v ′ ∈ V i for i = 1, 2. Moreover, if a,b,c ∈ V i are distinct vertices with dT (a, [b,c ]) ≥ 2, then
Π La(Lc) = Π La(Lb).
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 9
Proof. By Remark 2.16, there is a uniform bound on the diameter of pro jℓ¯e(ℓe′). Combined
with the fact that ψe is uniformly coarsely Lipschitz, this gives the constant λ. Considering the
convex hull of {a} ∪[b,c ], we see that, orienting [ c,a ] and [b,a ] towardsa, the last two edges of
[c,a ] are the same as the last two edges of [ b,a ]. Hence by deﬁnition, Π La(Lc) = Π La (Lb). □
Let v be a vertex of the Bass-Serre tree T . By Remark 2.16, the collection {ℓf =
iv(τf (Xf )) |f ∈ E(T ) such that f + = v} satisﬁes the projection axioms with a constant ξ0.
Let dℓ denote the projection distances with respect to proj ℓ. The following lemma follows
immediately from Lemma 2.18 and the deﬁnitions of dℓe and dLv .
Lemma 3.4. There exists a constant λ > 0 such that the following holds. Let u,v,w be
distinct vertices in V1 contained in Lk(o) for some vertex o in V2. Let e = [w,o ], e1 = [u,o ],
and e2 = [v,o ]. Then
1
λdℓe(ℓe1,ℓ e2) −λ ≤dLw (Lu,L v) ≤λdℓe(ℓe1,ℓ e2) +λ.
We are now ready to verify the projection axioms.
Proposition 3.5. There exists ξ > 0 such that for each i ∈ { 1, 2}, Li together with the
projection maps projℓ satisﬁes the projection axioms.
Proof. We verify the projection axioms for L1. The case for L2 is identical. The constant ξ
will be deﬁned explicitly during the proof.
Axiom 1: This follows from Lemma 3.3.
Axiom 2: Letu,v,w be distinct vertices in V1. In the course of the proof, we will compute
a constant ξ >0 such that if dLw (Lu,L v)>ξ , then dLu (Lw,L v) ≤ξ.
SincedLw (Lu,L v)> 0, it follows from Lemma 3.3 that either w lies on [u,v ] ordT (w, [u,v ]) =
1. If w lies on [u,v ], then since u,w,v ∈ V 1, we have dT (u, [w,v ]) ≥ 2 and dT (v, [u,w ]) ≥ 2.
Axiom 2 thus follows from Lemma 3.3.
On the other hand, suppose that d(w, [u,v ]) = 1. Let o ∈ [u,v ] be adjacent to w and con-
sider the vertices u′,v ′ ∈ Lk(o) ∩ [u,v ] which lie in [u,o ] and [o,v ], respectively. If u ⁄=u′, then
dLu(Lw,L v) = 0, and so we may assume without loss of generality that u =u′. Furthermore,
πLu(Lv) = πLu(Lv′ ) by deﬁnition. Thus to prove the upper bound on dLu(Lw,L v), it suﬃces
to assume that v =v′, in which case u,v,w all lie in Lk( o), where o ∈ V 2.
Let e = [w,o ], e1 = [u,o ], and e2 = [v,o ]. It follows from Lemma 3.4 that
1
λdℓe(ℓe1,ℓ e2) −λ ≤dLw (Lu,L v) ≤λdℓe(ℓe1,ℓ e2) +λ.
Again applying Lemma 3.4 with the roles of u,v,w exchanged, we have that
1
λdℓe1 (ℓe,ℓ e2) −λ ≤dLu(Lw,L v) ≤λdℓe1 (ℓe,ℓ e2) +λ.
Since {ℓf |f ∈E(T ) and f + =o} satisﬁes the projection axioms with constant ξ0, it follows
that dℓe(ℓe1,ℓ e2) > ξ0 implies that dℓe1 (ℓe,ℓ e2) ≤ ξ0. Since there are ﬁnitely many choices
for o up to the action G′, the constant ξ0 may be chosen independently of o. Thus, setting
ξ =λξ0 +λ, the above inequalities show that dLW (Lu,L v)>ξ implies that dLu (Lw,L v) ≤ξ.
This veriﬁes Axiom 2.
Axiom 3: For distinct u,v ∈ V 1, we will prove the set
{w ∈ V 1 |dLw (Lu,L v)>ξ }
is ﬁnite. By Lemma 3.3, any such vertex w is either contained in the interior of [ u,v ] or
satisﬁes d(w, [u,v ]) = 1. The ﬁrst case yields at most d(u,v ) − 1 choices for w.
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 10
Suppose d(w, [u,v ]) = 1. As in the proof of Axiom 2, we can assume that u,v,w lie in
Lk(o) for some vertex o in V2. Let e1 = [u,o ],e 2 = [v,o ], and e = [w,o ]. By Lemma 3.4, we
havedLw (Lu,L v) ≤λdℓe(ℓe1,ℓ e2) +λ. Since ξ =λξ0 +λ, it follows that
{w ∈ Lk(o)
⏐⏐dLw (Lu,L v)>ξ } ⊂ {w ∈ Lk(o)
⏐⏐dℓe(ℓe1,ℓ e2)>ξ 0}.
The projection axioms for {ℓf |f ∈ E(T ) and f + = v} imply that the latter set is ﬁnite,
and so the former set must also be ﬁnite. Since there are ﬁnite ly many possibilities for o, this
veriﬁes Axiom 3. □
Lemma 3.6. For each i = 1, 2, the action of G =π1(G) on the collection Li = {Lv |v ∈ V i}
satisﬁes
Π gLv (gLu) = gΠ Lv (Lu)
for any v ∈ V i and any g ∈G.
Proof. This follows immediately from the deﬁnition of Π and the fact that the maps proj and
ψ are G–equivariant in the sense that proj ge(ℓgf ) = g · proj ¯e(ℓf ) and ψge(gx) = gψe(x). □
We are now ready to prove Theorem 1.4.
Proof of Theorem 1.4. Let G′ be the ﬁnite index subgroup of G given by Lemma 3.1, which
is also a Croke-Kleiner admissible group. Without loss of ge nerality, we replace G by G′ for
the rest of the proof.
By Proposition 3.5, the collection of quasi-lines Li = {Lv |v ∈ V i} satisﬁes the projection
axioms with a constant ξ for i = 1, 2. Fix K > 4ξ. The unbounded quasi-trees of metric
spaces CK (L1) and CK (L2) are themselves quasi-trees, and they admit unbounded isom etric
actions G ↷ CK(L1) and G ↷ CK(L2).
Since the underlying graph of G is bipartite, we can choose an edge ˇ e in Γ which is not a
loop. Choosing the orientation of ˇe correctly,µ = ˇe− andω = ˇe+ have lifts in T belonging to
V1 and V2 respectively. By construction, elements of Zµ and Zω are loxodromic and elliptic
in the action on CK(L1), respectively, and elliptic and loxodromic in the action o n CK(L2),
respectively. By Lemma 2.3, we conclude that the group G is H–inaccessible. □
Every graph manifold has a ﬁnite cover that is a graph manifol d N containing at least
two Seifert ﬁbered spaces such that each Seifert ﬁbered piec e has orientable, hyperbolic base
orbifold. We call such a graph manifold non-elementary in Section 4. Since π1(N ) is a
Croke-Kleiner admissible group, the following corollary i s immediate from Theorem 1.4.
Corollary 3.7. Every graph manifold has a ﬁnite cover whose fundamental gro up is H–
inaccessible.
It is still unknown whether H–inaccessibility of a ﬁnite index normal subgroup of G passes to
H–inaccessibility of the ambient group G. Thus it is natural to ask whether the “ﬁnite cover”
condition in Corollary 3.7 can be removed. We will address th is question in the following
section.
