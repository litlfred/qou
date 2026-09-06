---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-008-4-haccessibility-of-3-manifold-groups
section_title: "H–accessibility of 3-manifold groups"
section_number: 4
pages: 10-12
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a grou p G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
The goal of this section is to prove Theorem 1.1, which gives c onditions under which the
fundamental group of a non-geometric 3–manifold is H–inaccessible.
We begin by recalling some deﬁnitions and facts about 3-mani folds. Let M be a compact,
connected, orientable, irreducible 3-manifold with empty or toroidal boundary. By the ge-
ometrization theorem for 3-manifolds of Perelman ([Perel1 ], [Perel2], [Perel3]) and Thurston,
either
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 11
(1) the manifold M is geometric, in the sense that its interior admits one of the following
geometries: S3, E3, H3, S2 × R, H2 × R, ~SL(2, R), Nil, and Sol; or
(2) the manifold M is non-geometric. In this case, the torus decomposition of 3-manifolds
yields a nonempty minimal union T ⊂ M of disjoint essential tori, unique up to iso-
topy, such that each component of M \T is either a Seifert ﬁbered piece or a hyperbolic
piece.
We refer the reader to [Scott] for background on geometric st ructures on 3-manifolds. A
Seifert ﬁbered piece is called non-elementary if its base orbifold is orientable and hyperbolic,
and it is called isolated if it is not glued to any other Seifert ﬁbered piece.
The manifold M is called a graph manifold if all the pieces of M \T are Seifert ﬁbered.
A graph manifold is non-elementary if it contains at least two pieces and all pieces are non-
elementary. In other words, a non-elementary graph manifol d is obtained by gluing at least
two and at most ﬁnitely many non-elementary Seifert ﬁbered m anifolds, where the gluing maps
between the Seifert components do not identify (unoriented ) Seifert ﬁbers up to homotopy.
We will call a non-geometric manifold M a mixed manifold if it is not a graph manifold. If
there is a subcollection T ′ of T and a connected component of M \T ′ that is a graph manifold,
then this connected component is called a graph manifold component of the mixed manifold
M . A graph manifold component is maximal if it is not properly contained in another graph
manifold component. A mixed manifold is non-elementary if all maximal graph manifold
components and Seifert ﬁbered pieces are non-elementary.
Remark 4.1. Every graph (respectively, mixed) manifold is ﬁnitely covered by a non-elementary
graph (respectively, mixed) manifold (see, for example, [P W14, Lemma 3.1], [KL98, Lemma 2.1]).
Our starting point for proving Theorem 1.1 is the following l emma, which describes when
π1(M ) is relatively hyperbolic.
Lemma 4.2 ([Dah03, BW13]) . Let M1,...,M k be the maximal graph manifold components
and Seifert ﬁbered pieces of the torus decomposition of M . Let S1,...,S ℓ be the tori in the
boundary of M that bound a hyperbolic piece, and let T1,...,T m be the tori in the torus de-
composition of M that separate two hyperbolic components. Then π1(M ) is hyperbolic relative
to
P = {π1(Mp)}k
p=1 ∪ {π1(Sq)}ℓ
q=1 ∪ {π1(Tr)}m
r=1.
This relatively hyperbolic structure on π1(M ) is useful because of the following result,
which gives a criterion for relatively hyperbolic groups to be H–inaccessible.
Lemma 4.3. Let (G, P) be a relatively hyperbolic group. If there is a peripheral sub group
P ∈ P that satisﬁes the hypotheses of Lemma 2.3, then G is H–inaccessible.
Before proving the lemma, we state an immediate corollary, w hich gives a diﬀerent proof
of [AR19, Theorem 6.2].
Corollary 4.4 ([AR19, Theorem 6.2]) . The fundamental group of a ﬁnite-volume cusped
hyperbolic 3-manifold is H–inaccessible.
We now turn to the proof of Lemma 4.3.
Proof of Lemma 4.3. To see that H(G) does not contain a largest element, we will construct
two actions of G on hyperbolic spaces with commuting elements a,b ∈ G that satisfy the
hypotheses of Lemma 2.3. To do this, we will apply the machine ry of induced actions from
[AHO].
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS 12
Since P satisﬁes the hypotheses of Lemma 2.3 by assumption, there ar e commuting ele-
ments a,b ∈ P and isometric actions P ↷ X and P ↷ Y on hyperbolic spaces such that
a and b act loxodromically and elliptically, respectively, in the action P ↷ X, and b acts
loxodromically in the action P ↷ Y . For all Q ∈ P \ {P }, ﬁx the trivial action of Q on a
point. By [AHO, Corollary 4.11(a)], there exist hyperbolic spaces ZX,Z Y on which G acts
by isometries, associated to the collection of actions {Q ↷ ∗ | Q ∈ P \ {P }} ∪ {P ↷ X} and
the collection of actions {Q ↷ ∗ | Q ∈ P \ {P }} ∪ {P ↷ Y }, respectively. Moreover, there
are coarsely P –equivariant quasi-isometric embeddings X →ZX and Y →ZY . Therefore, a
acts loxodromically and b acts elliptically in the action G ↷ ZX , while b acts loxodromically
in the action G ↷ ZY . This completes the proof. □
In light of Lemmas 4.2 and 4.3, to prove the H–inaccessibility of π1(M ), it suﬃces to
understand its peripheral subgroups. In Section 4.1, we ana lyze the fundamental groups of
the Seifert ﬁbered pieces. The more diﬃcult subgroups to und erstand are the fundamental
groups of the maximal graph manifold components. We conside r these in Section 4.2 and
give conditions under which they satisfy Lemma 2.3; see Prop osition 4.8. In Section 4.3, we
put these results together and prove Theorem 1.1. Up to this p oint, we have been assuming
thatM has empty or toroidal boundary. Finally, in Section 4.4, we c onsider 3-manifolds with
higher genus boundary components.
4.1. Seifert ﬁbered manifolds. In this section, we analyze Seifert ﬁbered pieces.
Lemma 4.5. Let 1 → Z i− →G π− →H → 1 be a short exact sequence where Z is central in G
and H is a non-elementary hyperbolic group. Then G is H–inaccessible.
Proof. Choose a ﬁnite generating set J ofH and consider the hyperbolic action G ↷ Cay(H,J ).
Leta be a generator of the group Z, and let b be an element of G such that π(b) is loxodromic
in H ↷ Cay(H,J ). The element b is thus loxodromic in the action G ↷ Cay(H,J ), as well,
while the element a is elliptic (in fact, trivial) in this action.
Since every integral cohomology class of a hyperbolic group is bounded (see [Min01]),
the central extension Z → G → H corresponds to a bounded element of H 2(H, Z). Hence
[HRSS22, Lemma 4.1] provides a quasi-morphism φ : G → Z which is unbounded on i(Z). By
[ABO19, Lemma 4.15], there exists a generating set S for G such that L := Cay(G,S ) is a
quasi-line and the inclusion Z →L induced by i is a Z–equivariant quasi-isometry. We thus
obtain a hyperbolic action G ↷ L for which a is loxodromic. Since a ∈Z(G), the elements a
and b commute. By Lemma 2.3, G is H–inaccessible. □
Corollary 4.6. Let M be a non-elementary Seifert ﬁbered manifold. Then π1(M ) is H–
inaccessible.
Proof. Let ϕ : M → Σ be a Seifert ﬁbration. Since S1 → M → Σ is a circle bundle over Σ,
there is a short exact sequence
1 → Z →π1(M ) →π1(Σ) → 1,
where Z is the normal cyclic subgroup of π1(M ) generated by a ﬁber. The group Z is central
inπ1(M ) since Σ is orientable (see, e.g., [Mar, Proposition 10.4.4 ]). By Lemma 4.5, the group
π1(M ) is H–inaccessible. □
