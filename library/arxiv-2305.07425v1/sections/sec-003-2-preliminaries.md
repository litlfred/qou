---
doc_id: arxiv-2305.07425v1
doc_title: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS"
section_id: sec-003-2-preliminaries
section_title: "Preliminaries"
section_number: 2
pages: 4-5
source_pdf: 2305.07425v1.pdf
source_sha256: 2f7d2ac5818b6af4
toc_source: outline
doc_brief: "LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS — The set of equivalence classes of cobounded actions of a group G on diﬀerent hyperbolic metric spaces carries a natural partial order."
---
2. Preliminaries
2.1. H–accessibility. In this section, we review the partial order on cobounded group actions
introduced in [ABO19]. Fix a group G. If G acts coboundedly on two metric spaces X and Y ,
we say G ↷X is dominated by G ↷Y , written G ↷X ⪯G ↷Y , if there exists a coarsely
G–equivariant coarsely Lipschitz map Y →X. The preorder ⪯induces an equivalence relation
G ↷X ∼G ↷Y if and only if G ↷X ⪯G ↷Y and G ↷Y ⪯G ↷X. It descends to a
partial order ≼on the set of equivalence classes. We denote the equivalence class of an action
by [G ↷X].
Deﬁnition 2.1. Given a group G, the poset of hyperbolic structures on G is deﬁned to be
H(G) := {[G ↷X] | G ↷X is cobounded and X is hyperbolic},
equipped with the partial order ≼.
By [ABO19, Proposition 3.12], this is equivalent to the original deﬁnition of H(G) in terms
of generating sets. We say that an element of a poset is largest when it is greater than or
equal to every other element of the poset. Such an element is unique.
Deﬁnition 2.2. A group G is H–accessible if the poset H(G) has a largest element. Otherwise,
it is H–inaccesible.
The following lemma gives a simple criterion to check if a group is H–inaccessible.
Lemma 2.3 ([AR19, Lemma 1.4]). Let G be a group. Suppose that there are commuting
elements a, b ∈G and hyperbolic actions G ↷X and G ↷Y such that
(1) a acts loxodromically and b acts elliptically in the action G ↷X; and
(2) b acts loxodromically in the action G ↷Y .
Then there does not exist a hyperbolic action G ↷Z such that G ↷X ⪯G ↷Z and
G ↷Y ⪯G ↷Z.
We will typically apply this lemma to spaces X and Y that are quasi-isometric to lines.
These actions on quasi-lines will be constructed using quasimorphisms, which, in turn, will
be constructed using hyperbolic actions of G with very weak proper discontinuity properties
(see [BBF15]).
Deﬁnition 2.4. Let G ↷X be a hyperbolic action and g ∈G be loxodromic with ﬁxed
points {g±} ⊂∂X. The element g is WWPD if the orbit of the pair (g+, g−) is discrete in the
space ∂X × ∂X \ ∆, where ∆= {(x, x) | x ∈∂X} is the diagonal subset. A WWPD element
g is WWPD+ if any h ∈G that stabilizes {g±} as a set also ﬁxes {g±} pointwise.
The following proposition follows from [BBF16, Corollary 3.2].
Proposition 2.5. Suppose that G ↷X is a hyperbolic action with a WWPD+ element g ∈G.
There is a homogeneous quasimorphism q: G →R such that q(g)̸ = 0 and q(h) = 0 for any
element h ∈G that acts elliptically on X.
Homogeneous quasimorphisms, in turn, give rise to actions on quasi-lines.
Proposition 2.6 ([ABO19, Lemma 4.15]). Let q: G →R be a non-zero homogeneous quasi-
morphism. Then there is an action of G on a quasi-line L such that q(g)̸ = 0 if and only if g
acts loxodromically on L.
LARGEST HYPERBOLIC ACTIONS OF 3–MANIFOLD GROUPS
