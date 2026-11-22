---
doc_id: arxiv-math-9201302v1
doc_title: "The Quantum G 2 Link Invariant"
section_id: sec-008-31-invariants-of-colored-ribbon-graphs
section_title: "Invariants of colored ribbon graphs"
section_number: 3.1
pages: 12-14
source_pdf: 9201302v1.pdf
source_sha256: 67987dd432f58488
toc_source: inferred
doc_brief: "The Quantum G_2 Link Invariant — We derive an inductive, combinatorial deﬁnition of a polynomial-valued regular isotopy invariant of links and tangled graphs."
---
Invariants of colored ribbon graphs
We begin with a summary of Reshetikhin and Turaev’s deﬁnition and some basic properties.
We review some of the theory of ﬁnite-dimensional left modules, or representations, of a Hopf algebra H.
If we have two representations V and W, the tensor product V ⊗W is also a representation by the coalgebra
structure of H. There is a trivial representation I such that I ⊗V ∼= V ⊗I ∼= V canonically. However, there
is no canonical isomorphism between V ⊗W and W ⊗V as representation of H, and indeed the two modules
need not be isomorphic at all. In particular, the switching map, which takes x ⊗y to y ⊗x, is in general not
a module homomorphism. On the other hand, we do have U ⊗(V ⊗W) ∼= (U ⊗V ) ⊗W, and it is still true
that if A and B are morphisms between representations, A⊗B is also. Also, for each representation V there
is a representation V ∗and a canonical identiﬁcation of Hom(U ⊗V ∗, W) and Hom(U, W ⊗V ). There is
also a representation V ◦with a canonical identiﬁcation of Hom(V ◦⊗U, W) with Hom(U, V ⊗W). Although
there are canonical isomorphisms V ◦∗∼= V ∗◦∼= V , V ∗∗need not be isomorphic to V . Finally, we deﬁne
Inv(V ) = Hom(I, V ) by analogy with the case when H is a group algebra.
There is a visual notation for morphisms in the category of H-modules and their compositions. If f is a
morphism from V1 ⊗. . . ⊗Vn to W1 ⊗. . . Wn, we can represent f by a diagram with one vertex:
(Figure 30)
Similarly for compositions of morphisms.
For example, if f : V1 →V3 ⊗V4, g : V4 ⊗V2 →V5, and
h : V3 ⊗V5 →V6 ⊗V7 are morphisms, then we can express h ◦(I ⊗g) ◦(f ⊗I) by the diagram:
(Figure 31)
Note that the facts stated in the previous paragraph allow us to erase internal edges labeled with the
representation I; by a slight abuse of notation we may, for example, draw a morphism f : I →V ⊗W as:
(Figure 32)
In general these diagrams must be planar graphs in which none of the edges pass through a slope of
zero. However, it is sometimes possible to augment the structure of a Hopf algebra to obtain a ribbon Hopf
algebra, in which the graphs can have edges that bend arbitrarily and can have edges that cross each other,
provided one arm of each crossing is labeled “over” and the other “under”. First, there is a distinguished
element R of H ⊗H which we can use to construct, for each V and W, an isomorphism ˘R : V ⊗W →W ⊗V
which is denoted by a right-handed crossing:
(Figure 33)
The inverse ˘R−1, which need not equal ˘R, is denoted by a left-handed crossing:
(Figure 34)
Second, there is a distinguished element K of H which we can use to construct an isomorphism ˘K : V ∗∗→V .
It follows that there exist canonical morphisms which can be denoted as follows:
(Figure 34)
In light of the existence of these morphisms and the identiﬁcation of V ∗and V ◦, we can orient the edges of
the diagrams and declare that an edge labeled with V ∗is equivalent to an oppositely oriented edge labeled
with V . In a ribbon Hopf algebra the elements R and K must satisfy certain axioms which can be translated
to various identities for the corresponding morphisms. Here are some of these identities:
(Figure 35)
These identities allow us to interpret the ﬁnite-dimensional representation theory of a given ribbon Hopf
algebra H as an invariant of colored ribbon graphs, where each edge is colored by a representation of H
and each vertex is colored by an element of Inv(V1 ⊗V2 ⊗. . . Vn), where V1, . . . , Vn are the colors of the
incoming edges going clockwise around the vertex. (The vertex must also be marked to identify which edge
corresponds to the ﬁrst factor in the tensor product; however there is an identiﬁcation between the sets of
colors allowed for two diﬀerent markings. Although there is no single preferred isomorphism between V ⊗W
and W ⊗V , there is such an isomorphism between Inv(V ⊗W) and Inv(W ⊗V ). It is constructed from the
˘K morphisms.) We may interpret the value of a ribbon graph with no endpoints as a morphism from I to
I, i.e. as a scalar invariant. But the invariant is also a linearly recurrent invariant; the spanning space of
endpoints colored with V1, . . . , Vn is again Inv(V1 ⊗V2 ⊗. . . Vn). This invariant of colored ribbon graphs is
the Reshetikhin-Turaev invariant corresponding to the ribbon Hopf algebra H.
We remark that for a ﬁxed graph, the invariant is multilinear under direct sums, and more generally
under extensions, of the colors of the edges, so it suﬃces to consider irreducible representations as colors.
We also consider the consequences of an irreducible representation V being self-dual. If V is symmetrically
self-dual, i.e. there is an element B of Inv(V ⊗V ) which is invariant under the switching map, then we can
allow an unoriented edge colored by V by interpreting it as two oriented edges using B:
(Figure 36)
On the other hand, if V is anti-symmetrically self-dual, i.e. the invariant tensor B negates under the switching
map, then this construction has a sign ambiguity. But suppose that all representations of H are self-dual,
some of them anti-symmetrically self-dual.
Then we may resolve the ambiguity by observing that the
Reshetikhin-Turaev theory works equally well for Hopf superalgebras. If we reinterpret anti-symmetrically
self-dual representations as being negatively graded, they become supersymmetric. It is possible to replace
the Hopf algebra H with a Hopf superalgebra H′ for which these are the natural gradings.
The other essential ingredient in the Reshetikhin-Turaev theory is a collection of examples of ribbon Hopf
algebras. For each simple Lie algebra g there is a Hopf algebra Uq(g), the quantized universal enveloping
algebra of g, over the ﬁeld C(q, q1/2, q1/3, . . . ) (see [2]). The representation ring of this Hopf algebra is the
same as that of g or U(g). Consequently we will refer to the irreducible representations Uq(g) as Vλ, where λ
is the highest weight of the corresponding representation of g. However, the calculus of morphisms between
the representations is only the same as that for g at the specialization q = 1. We denote the corresponding
ribbon graph invariant by RTg.
The most important ﬁrst case of the ribbon graph invariants is their value on the untwisted unknot
colored with some Vλ. The value of RTg for this graph is known as the quantum dimension of Vλ and equals
the trace of the element K. This element is a member of the subalgebra of Uq(g) generated by the Cartan
subalgebra of g, and this subalgebra is the same as the corresponding subalgebra of a certain completion
U(g), the ordinary universal enveloping algebra. If ρ is half of the sum of the positive roots of the root
system of g and Hρ is the corresponding element of the Cartan subalgebra, then K = qHρ. The upshot is
that the trace of K on Vλ is P
α m(α)q(ρ,α), where α runs over the weights of Vλ and m(α) is the multiplicity
of α. Another formula for the quantum dimension is the quantum Weyl dimension formula:
dimq Vλ =
Q
α≻0 [(λ + ρ, α)]
Q
α≻0 [(ρ, α)]
,
where [n] = qn/2−q−n/2
q1/2−q−1/2 is a “quantum integer” (see [1, ch. 6, p. 151] for a proof that this is the trace of K).
For example, when g = G2, we obtain:
dimq V1,0 = q5 + q4 + q + 1 + q−1 + q−4 + q−5 = [7][12][2]
[6][4]
as the quantum dimension of the smallest non-trivial irreducible representation. Note, however, that when
we perform a supersymmetric conversion of a ribbon Hopf algebra H as described above, the quantum
dimension of a negatively graded representation negates.
The next most important computation is the evaluation of a right-handed twist:
(Figure 37)
where c(Vλ) is the Casimir number for Vλ. A derivation of this equation is given in [10].
3.2
Comparison with ⟨·⟩g
We restrict our attention to the exceptional simple Lie algebra G2. All representations of G2 are symmetri-
cally self-dual. The vector space Inv(V ⊗3
1,0 ) is 1-dimensional; let us choose some element T in it. We interpret
a G2 freeway as a colored ribbon graph by coloring all edges with the 7-dimensional representation V1,0 and
all vertices with T . In this way we obtain a value of RTG2 for G2 freeways.
We can verify by a computation with weight diagrams that dim Inv(V ⊗n
1,0 ) is 1,0,1,1,4, and 10 as n ranges
from 0 to 5 (see [4]). A lengthier calculation shows that the values of RTG2 on acyclic graphs with n endpoints
are indeed a basis for n < 5 and q = 1 (and therefore also for q an indeterminate). The author and Rena
Zieve performed this calculation explicitly. The tensor T was chosen as a trilinear form T (a, b, c) on V1,0. It
is well-known that for the compact real Lie group G2, V1,0 can be interpreted as the imaginary octonions, or
Cayley numbers, which are equipped with a positive-deﬁnite inner product and a cross product, a bilinear
function “×” with the property that if a and b are orthogonal unit vectors, a × b is a unit vector which is
orthogonal to both a and b. We deﬁne T (a, b, c) = (a × b) · c.
The conclusion is that the invariant RTG2 satisﬁes the 1,0,1,1,4,10 Ansatz. It remains only to show that
the parameter q in RTG2 agrees with the parameter q in ⟨·⟩G2. To do this we ﬁrst check that the quantum
dimension of V1,0 equals the constant a in the recurrence relation of ⟨·⟩G2, and we compute the factor gained
by a right-hand twist:
(Figure 38)
We verify that c(V1,0) = 6. Thus, the two parameterizations are the same, up to a constant factor in the
choice of T . (The choice of T above for the explicit q = 1 computation agrees with the right choice for
⟨·⟩G2.) Notice in particular that the Casimir element is always positive, which assures us that the ambiguity
between q and q−1 has been resolved in agreement with convention.
By similar but simpler reasoning we can show that ⟨·⟩A2 = RTA2, where all edges of an A2 freeway are
colored with the 3-dimensional representation V1,0, whose dual is V0,1. The orientations of the edges are
needed because V1,0 is not self-dual. The colors for the vertices can be recognized as the determinant, or the
usual 3-dimensional cross product.
We also have ⟨·⟩C2 = RTC2, where the single edges are colored with the 4-dimensional representation
V1,0 and the double edges are colored with the 5-dimensional representation V0,1. The representation V1,0
is the canonical representation of sp(4) ∼= C2. Note that it is anti-symmetrically self-dual. To convert from
⟨·⟩C2, where edges are not oriented, we must use the Hopf superalgebra Uq(sp(4))′ instead of Uq(sp(4)).
This superalgebra can also be thought of as Uq(sp(0, 4)), where osp(0, 4) is an orthosymplectic Lie super-
algebra. (Similarly, the Kauﬀman bracket ⟨·⟩A1 more properly describes invariants from the representation
theory of sp(0, 2) rather than the theory of sl(2) = sp(2).) Finally, the representation V0,1 is the canonical
representation of so(5) ∼= B2 ∼= C2.
