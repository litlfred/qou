---
doc_id: arxiv-1206.5522v6
doc_title: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS"
section_id: sec-008-33-homology-theories
section_title: "Homology theories"
section_number: 3.3
pages: 18-19
source_pdf: 1206.5522v6.pdf
source_sha256: 6e992242435b5e9f
doc_brief: "FACTORIZATION HOMOLOGY OF TOPOLOGICAL MANIFOLDS — Factorization homology theories of topological manifolds , after Beilinson, Drinfeld and Lurie, are homology-type theories for topological"
---
theory. First, note that taking products of manifolds deﬁnes a fu nctor MﬂdB
n−1× Mﬂdor
1 → MﬂdB
n ,
where Mﬂdor
1 is oriented 1-manifolds and
MﬂdB
n−1 := Mﬂdn−1 ×
Spaces/BT op(n)
Spaces/B
is the ∞-category of ( n− 1)-manifolds with a B-framing on the product of their tangent bundle
product with a trivial line bundle. Consequently, any B-framed n-manifold of the form M0× R,
where M0 is an ( n− 1)-manifold, can be given the structure of a Diskor
1 -algebra in MﬂdB
n , since R
has the structure of a Diskor
1 -algebra in Mﬂdor
1 .
Deﬁnition 3.13 (Collar-gluing). A collar-gluing among B-framed n-manifolds is a continuous map
f : M→ [−1, 1]
to the closed interval for which the restriction f| : M|(−1,1)→ (−1, 1) is a manifold bundle. We will
often denote a collar-gluing M
f
− →[−1, 1] simply as the open cover
M ′ ⋃
M0×R
M ′′ ∼= M
where M ′ = f −1[−1, 1) and M ′′ = f −1(−1, 1] and M0 = f −1{0}.
Remark 3.14. We ﬁnd it useful to think of a collar-gluing as the data of a manifold M together
with a codimension-1 properly embedded submanifold M0⊂ M that splits the manifold M into
two disconnected parts, M ′ and M ′′. Such data is aﬀorded by gluing two manifolds with boundary
along a common boundary. The actual data of a collar-gluing speciﬁe s that named just above, in
addition to a bi-collaring M0× R֒→M of M0⊂ M .
Construction 2.21 oﬀers, for each collar-gluing M
f
− →[−1, 1] among B-framed n-manifolds, a
monoidal functor
f −1 : Disk∂,or
1/[−1,1]−→ MﬂdB
n/M .
In particular, for each symmetric monoidal functor MﬂdB
n
F
− →V with⊗-presentable codomain, there
is a canonical morphism in V:
(6) F(M ′)
⨂
F(M0×R)
F(M ′′) ≃
Cor 3.12
∫
[−1,1]
F◦ f −1 −→ F(M ) .
Deﬁnition 3.15. A symmetric monoidal functor F : MﬂdB
n → V satisﬁes⊗-excision if, for each
collar-gluing M ′ ⋃
M0×R
M ′′∼= M among B-framed n-manifolds, the canonical morphism (6)
F(M ′)
⨂
F(M0×R)
F(M ′′)
≃
−−→F(M )
is an equivalence in V. The ∞-category of homology theories for B-framed n-manifolds valued in V
is the full ∞-subcategory
H(MﬂdB
n , V) ⊂ Fun⊗(MﬂdB
n , V)
consisting of those symmetric monoidal functors that satisfy ⊗-excision.
18
Remark 3.16. The behavior of a homology theory with coeﬃcients in V depends critically on the
symmetric monoidal structure chosen on V. For instance, for the symmetric monoidal ∞-category
(Modk,⊕) of k-modules over a ﬁxed ﬁeld k with direct sum, a homology theory is forced to be
ordinary homology with coeﬃcients in k; while for ( Modk,⊗), a homology theories is typically not
a homotopy invariant of manifolds.
Remark 3.17. One can complete the ∞-category Mﬂdn as follows: ﬁrst, formally adjoin, for every
collar-gluing M ′ ⋃
M0×R
M ′′∼= M , the colimit of the simplicial object Bar•(M ′, M0× R, M ′′); second,
Dwyer-Kan localize by forcing the natural map from this new object |Bar•(M ′, M0× R, M ′′)|→ M
to be an equivalence. Denote this completion of the ∞-category of manifolds as ˆMﬂdn. The
completion functor Mﬂdn → ˆMﬂdn is the universal homology theory: that is, we now have the
suggestive equivalence ∫
M
Rn ≃ M
as objects of ˆMﬂdn (the lefthand side is not deﬁned in Mﬂdn). By this universal property, a ⊗-
excisive functor Mﬂdn→ V is equivalent to a symmetric monoidal functor ˆMﬂdn→ V that preserves
geometric realizations of simplicial objects.
