---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-002-21-b-framings
section_title: "B-framings"
section_number: 2.1
pages: 6-9
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
We use this to consider the tangent classiﬁer, which thereafter oﬀ ers the notion of a B-framing on
an n-manifold, as well as an ∞-category of such.
Deﬁnition 2.1. Mﬂdn is the symmetric monoidal topological category for which an object is
a topological n-manifold that admits a ﬁnite good cover, which is to say a ﬁnite open cover by
Euclidean spaces with the property that each non-empty intersec tion of terms in the cover is itself
homeomorphic to a Euclidean space. The morphism spaces are space s of embeddings, endowed with
the compact-open topology. The symmetric monoidal structure is disjoint union. 3
In particular, the mapping space is MapMﬂdn (M, N ) = Emb(M, N ), the space of embeddings of
M into N equipped with the compact-open topology. Note that disjoint union is not the coproduct;
Mﬂdn has almost no nontrivial colimits.
We will be particularly interested in n-manifolds equipped with some extra structure such as
an orientation or a framing. Structure of this sort can be swiftly ac commodated by way of the
tangent classiﬁer : each n-manifold M has a tangent microbundle, and it is classiﬁed by a map
τM : M→ BTop(n) to the classifying space of the topological group Top(n) of self-homeomorphisms
3Thus, any M ∈ Mﬂd n has ﬁnitely many connected components, each of which is the i nterior of a compact
manifold with (possibly empty) boundary. This size restric tion is not an essential requirement; since all noncompact
manifolds are built as sequential colimits of such smaller m anifolds, this smallness condition could be removed and
one could instead add to Deﬁnition 3.15 the requirement that a homology theory preserves sequential colimits.
6
of Rn; see [MS]. For B→ BTop(n) a map of spaces, a B-framing on M is a homotopy commutative
diagram among spaces
B
/d15/d15
M τM
/d47/d47
g
/d54/d54♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠♠ BTop(n).
Example 2.2. Consider the composite continuous homomorphism
Top(n)
(−)+
−−−−→Aut∗(Sn)
π0
− −− →Z/2Z
given by applying 1-point compactiﬁcation to obtain based homotopy automorphisms of a sphere
followed by taking path components. For STop(n)⊂ Top(n) the kernel of this homomorphism, a
BSTop(n)-framing on a topological n-manifold is precisely an orientation.
Toward formulating an ∞-category of B-framed n-manifolds, we next explain how to make the
tangent classiﬁer continuously functorial among open embeddings . We will make ongoing use of the
following result of Kister and Mazur.
Theorem 2.3 ([Ki]). The continuous homomorphism of topological monoids Top(n)→ Emb(Rn, Rn)
is a homotopy equivalence.
Now, temporarily consider the full ∞-subcategory Eucn⊂ Mﬂdn consisting solely of Rn; this ∞-
category is that associated to the topological monoid Emb(Rn, Rn) of self-embeddings of Rn. We
draw an immediate consequence of the Kister–Mazur Theorem.
Corollary 2.4. The canonical functor
BTop(n)−→ Eucn
is an equivalence of ∞-categories. In particular, there is a preferred equivalen ce of∞-categories
PShv(Eucn) ≃ Spaces/ BTop(n)
between space-valued presheaves on Eucn and spaces over BTop(n).
After Corollary 2.4 we have a tangent classiﬁer, functorial in a cohe rent homotopy sense, given
by the restricted Yoneda functor:
(1) τ : Mﬂdn−→ PShv(Mﬂdn)−→ PShv(Eucn) ≃
Cor 2.4
Spaces/ BTop(n) .
We will postpone to Corollary 2.13 justiﬁcation for this terminology. T o deﬁne the ∞-category
of B-framed n-manifolds as it is equipped with a symmetric monoidal structure, we r ecord a few
standard facts about ∞-categories together with an observation about the functor τ .
Lemma 2.5. Let S be an∞-category and let S∈ S be an object.
(1) For each morphism S′→ S in S, the canonical functor among over∞-categories (S/S)/(S′→S)→
S/S′ is an equivalence.
(2) Should S admit ﬁnite coproducts, the over ∞-category S/S admits ﬁnite coproducts and they
are preserved by the projection functor S/S→ S.
In addition, the ∞-category of symmetric monoidal ∞-categories Cat⊗
∞ admits limits and they are
preserved by the forgetful functor Cat⊗
∞→ Cat∞.
Proof. Through the deﬁning adjunctions for over ∞-categories, the ﬁrst assertion follows because,
for each∞-category K, the canonical diagram among ∞-categories
{0} /d47/d47
/d15/d15
{0 < 1}
/d15/d15
K ⋆{0} /d47/d47 K ⋆{0 < 1}
7
is a pushout; here, for K and J∞-categories,
K ⋆ I := K
∐
K×{0}×I
K×{ 0 < 1}× I
∐
K×{1}×I
I
denotes the join of ∞-categories. The second assertion follows directly from the univer sal property
of coproducts. The ﬁnal assertion follows from Proposition 3.2.2.1 o f [Lu2], which in particular gives
that, for each Cartesian closed presentable ∞-category C, the forgetful functor from commutative
algebras AlgCom(C×)→ C preserves and creates limits. Apply this result to the case C = Cat∞.
□
Observation 2.6. Because Rn is connected, this tangent classiﬁer τ : Mﬂdn→ Spaces/ BTop(n) is
symmetric monoidal with respect to coproducts in the codomain. In other words, τ carries ﬁnite
disjoint unions to ﬁnite coproducts over BTop(n).
Deﬁnition 2.7. The symmetric monoidal ∞-category MﬂdB
n of B-framed topological n-manifolds
is the limit in the following diagram:
MﬂdB
n /d47/d47
/d15/d15
Spaces/B
/d15/d15
Mﬂdn
τ /d47/d47 Spaces/ BTop(n) .
Since passage from ∞-categories to their spaces of morphisms preserves limits, there is a cor-
responding expression for mapping spaces: for two B-framed manifolds, M and N , the space of
B-framed embeddings of M to N is the homotopy pullback
EmbB(M, N ) /d47/d47
/d15/d15
Map/B(M, N )
/d15/d15
Emb(M, N ) /d47/d47 Map/BTop(n)(M, N ),
where Map/X (M, N ) is the space of maps of M to N over X, a point of which can be taken to be
a map M→ N and a homotopy between the two resulting maps from M to X.
The following assures us that these spaces of B-framed embeddings have tractable homotopy
types.
Lemma 2.8. A B-framing g of Rn determines a homotopy equivalence EmbB(Rn, Rn)≃ Ω gB of
topological monoids, where Ω gB is the loop space of B based at the homotopy point g : Rn→ B.
Proof. By deﬁnition, the space EmbB(Rn, Rn) sits in a homotopy pullback square:
EmbB(Rn, Rn) /d47/d47
/d15/d15
Map/ B(Rn, Rn)
/d15/d15
Emb(Rn, Rn) /d47/d47 Map/ BTop(n)(Rn, Rn).
There are evident equivalences of spaces Map/ BTop(n)(Rn, Rn)≃ Ω BTop(n)≃ Top(n) and likewise
Map/ B(Rn, Rn)≃ Ω gB. It is standard that the the composite map of spaces
Top(n)−→ Emb(Rn, Rn)−→ Map/ BTop(n)(Rn, Rn)≃ Ω BTop(n)
is an equivalence. By Kister–Mazur, Theorem 2.3, the ﬁrst map includ ing Top(n) into Emb(Rn, Rn)
is a homotopy equivalence. It follows that the middle map in the above d isplay is also an equivalence
of spaces. We conclude that the bottom horizontal map in the abov e homotopy pullback square is
an equivalence of spaces. This implies the top horizontal map too is an equivalence of spaces.
□
8
