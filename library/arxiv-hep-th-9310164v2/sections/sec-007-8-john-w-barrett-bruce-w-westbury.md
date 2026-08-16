---
doc_id: arxiv-hep-th-9310164v2
doc_title: ""
section_id: sec-007-8-john-w-barrett-bruce-w-westbury
section_title: "JOHN W. BARRETT & BRUCE W. WESTBURY"
section_number: 8
pages: 8-10
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
doc_brief: "This paper is a study of monoidal categories with duals where th e ten- sor product need not be commutative. The motivating examples are categories of representations of Hopf algebras."
---
The proof of the coherence theorem 1.9 now follows. It is only necessary to con-
sider reduced iterated natural transformations. A reduced iterated natural transfor-
mation is said to be directed if it is the product of instances which do not include
the inverses of ( γ, τ, ν ). By the preceding lemma 1.15, each iterated functor is
equivalent to a reduced iterated functor, and hence to a stan dard iterated functor,
by a directed natural transformation.
By a standard argument (see [MacLane 1963]), it is suﬃcient t o prove the co-
herence result for directed natural transformations betwe en an iterated functor F
and a standard iterated functor S. According to lemma 1.11, any directed natural
transformation S → F can be written as a central iterate S → R followed by an
iterate of instances of ( γ, τ, ν ): R → F . By lemma 1.15, R and the second natural
transformation are unique, whilst the ﬁrst natural transfo rmation is unique by the
coherence of central iterates.
Deﬁnition 1.16. If C is a category with duals then deﬁne the category P C to have
objects of the form ( F, {a1, . . . , an}) where F is a standard iterated functor of mul-
tiplicity n and each ai is an object of C. The set of morphisms from ( F, {a1, . . . , an})
to (G, {a1, . . . , am}) is the set of morphisms in C from F (a1, . . . , an) to G(a1, . . . , am).
There is a functor i: C → P C deﬁned on objects by a ↦→(1, a). There is also
a functor π: P C → C deﬁned on objects by ( F, {a1, . . . , an}) ↦→F (a1, . . . , an). It
is trivial that the composite i ◦ π is the identity functor of C. It is also clear that
there is a canonical natural transformation from π ◦ i to the identity functor of P C.
Hence the categories P C and C are canonically equivalent.
The coherence theorem implies that the category P C is a strict monoidal cat-
egory with strict duals. The functor i has the universal property that if D is a
strict monoidal category with strict duals and F : C → D is a functor of monoidal
categories with duals then there is a unique functor G: P C → D of strict monoidal
categories with strict duals such that F = i ◦ G.
2. Spherical categories
In this section we introduce spherical categories. A pivota l category is a category
with duals and with some additional structure and a spherica l category is a pivotal
category in which the additional structure satisﬁes an extr a condition.
Strict pivotal categories are discussed in [Freyd and Yette r 1989], where it is
shown that the category of oriented planar graphs up to isoto py with labelled
edges and with a distinguished edge at each vertex is a strict pivotal category.
If the sphere S2 is regarded as the plane with the point at inﬁnity attached, t hen
a closed graph in the plane can be regarded as a closed graph on the sphere. There
is an isotopy of the sphere which takes a closed graph of the fo rm of Figure 1 to
the graph obtained by closing M in a loop to the left. This isotopy moves the loop
in Figure 1 past the point at inﬁnity. Taken together with pla nar isotopies, such
an operation on planar graphs generates all the isotopies on the sphere. It follows
that the evaluation in a spherical category of a closed graph with labelled edges and
with a distinguished edge at each vertex is invariant under i sotopies of the sphere
S2.
SPHERICAL CATEGORIES 9
Deﬁnition 2.1. A pivotal category is a category with duals together with a mo r-
phism ǫ(c): e → c ⊗ c∗ for each object c ∈ C .
The conditions on the components of ǫ are the following:
(1) For all morphisms, f : a → b, the following diagram commutes
e
ǫ(a)
− − − − →a ⊗ a∗
ǫ(b)


↓


↓ f ⊗1
b ⊗ b∗ − − − − →
1⊗f ∗
b ⊗ a∗
(2) For all objects a, the following composite is the identity map of a∗:
a∗ λ− 1(a∗)
− − − − − →e ⊗ a∗ ǫ(a∗)⊗1
− − − − − →(a∗ ⊗ a∗∗) ⊗ a∗ α(a∗,a∗∗,a∗)
− − − − − − − − →a∗ ⊗ (a∗∗ ⊗ a∗)
1⊗γ(a∗,a)
− − − − − − →
a∗ ⊗ (a ⊗ a∗)∗ 1⊗ǫ(a)∗
− − − − − →a∗ ⊗ e∗ 1⊗ν − 1
− − − − →a∗ ⊗ e
ρ(a∗)
− − − →a∗
(3) For all objects a and b the following composite is required to be ǫ(a ⊗ b):
e
ǫ(a)
− − →a ⊗ a∗ 1⊗λ− 1(a∗)
− − − − − − − →a ⊗ (e ⊗ a∗)
1⊗(ǫ(b)⊗1)
− − − − − − − →a ⊗ ((b ⊗ b∗) ⊗ a∗)
1⊗α(b,b∗,a∗)
− − − − − − − − →a ⊗ (b ⊗ (b∗ ⊗ a∗))
α− 1(a,b,b∗⊗a∗)
− − − − − − − − − − →(a ⊗ b) ⊗ (b∗ ⊗ a∗)
1⊗γ(b,a)
− − − − − →(a ⊗ b) ⊗ (a ⊗ b)∗
These conditions imply that the strict extension is a pivota l category in the
sense of [Freyd and Yetter 1989]. This is clear once it has bee n shown that ǫ is
well-deﬁned on the strict extension.
The functor ∗ and the maps ǫ are not independent. The maps ǫ determine ∗.
This observation is in [Kelly and Laplaza 1980] where the map s ǫ are taken as more
fundamental than ∗. In [Turaev 1992] it is noted that the maps ǫ also determine γ.
Lemma 2.2. In any pivotal category, for any morphism f : a → b the following
composite is f ∗:
b∗ ρ− 1(b∗)
− − − − − →b∗ ⊗ e
1⊗ǫ(a)
− − − − →b∗ ⊗ (a ⊗ a∗)
1⊗(f ⊗1)
− − − − − →b∗ ⊗ (b ⊗ a∗)
α− 1(b∗,b,a∗)
− − − − − − − − →(b∗ ⊗ b) ⊗ a∗ (τ (b∗)⊗τ (b))⊗1
− − − − − − − − − − →(b∗∗∗ ⊗ b∗∗) ⊗ a
γ(b∗∗,b∗)⊗1
− − − − − − − →(b∗ ⊗ b∗∗)∗ ⊗ a∗
ǫ∗(b∗)⊗1
− − − − − →e∗ ⊗ a∗ ν − 1⊗1
− − − − →e ⊗ a∗ λ(a∗)
− − − →a∗
Proof. This follows directly from conditions (1) and (2) of the prec eding deﬁnition.
Remark 2.3. Note also that a pivotal category is closed, in the sense that there are
natural isomorphisms, for all a, b and c;
Hom(a ⊗ b, c) ∼
= Hom(b, a∗ ⊗ c) Hom( a, b ⊗ c) ∼
= Hom(a ⊗ c∗, b)
Hom(a ⊗ b, c) ∼
= Hom(a, c ⊗ b∗) Hom( a, b ⊗ c) ∼
= Hom(b∗ ⊗ a, c)
