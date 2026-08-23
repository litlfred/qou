---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: sec-005-4-john-w-barrett-bruce-w-westbury
section_title: "JOHN W. BARRETT & BRUCE W. WESTBURY"
section_number: 4
pages: 4-6
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where th e ten- sor product need not be commutative."
---
(2) The identity functor 1: C → C is an iterate.
(3) If F and G are iterates then the functor F ⊗ G = F × G ◦ ⊗ is an iterate.
(4) If F is an iterate then F ∗ = F − ◦ ∗ is an iterate.
The length of α is called the multiplicity of the iterated functor. There is a
category with objects the set of all iterates of ⊗, ∗ and e and morphisms all natural
transformations.
Deﬁnition 1.5. Let F , G and H be any three iterated functors. Then we have
natural transformations
α: (F ⊗ G) ⊗ H → F ⊗ (G ⊗ H)
λ: e ⊗ F → F
ρ: F ⊗ e → F
γ: (F ∗) ⊗ (G∗) → (G ⊗ F )∗
τ : F → F ∗∗
ν: e → e∗
Each of these is an isomorphism. Each of these and their inver ses are called in-
stances. More particularly, the ﬁrst one, for example, is ca lled an instance of α,
and its inverse an instance of the inverse of α.
Deﬁnition 1.6. The set of expansions is the smallest subset of the set of natu ral
transformations which satisﬁes the following:
(1) The identity functor, 1, is an expansion.
(2) Any instance is an expansion.
(3) If β is an expansion then β ⊗ 1 and 1 ⊗ β are expansions.
(4) If β is an expansion then β∗ is an expansion.
The smallest set which satisﬁes all but the last condition is the set of reduced
expansions.
Deﬁnition 1.7. The smallest subcategory which contains instances and whic h is
closed under ⊗ and ∗ is equal to the smallest subcategory which contains expansi ons.
This is called the category of iterates and any morphism in th is category is called
an iterated natural transformation.
The smallest subcategory of the category of iterates which c ontains instances and
which is closed under ⊗ is equal to the smallest subcategory of the category of
iterates which contains reduced expansions. Any morphism i n this category is
called a reduced iterated natural transformation.
Deﬁnition 1.8. Since every expansion is an isomorphism and the inverse of an y
expansion is an expansion it follows that every iterated nat ural transformation is
an isomorphism and that every inverse of an iterated natural transformation is an
iterated natural transformation. The category C with dual data is coherent if any
two iterated natural transformations between the same two i terated functors are
equal. Equivalently, the dual data is coherent if any diagra m with vertices iterated
functors and arrows expansions commutes.
SPHERICAL CATEGORIES 5
A category with dual data which is coherent is called a catego ry with duals.
The following is a coherence theorem, in the sense that this i s a ﬁnite set of
conditions on the data which are necessary and suﬃcient for t he data to be coherent.
Theorem 1.9. A category C with dual data is coherent if, and only if, the following
conditions are satisﬁed:
(1) τ (e) is the composite
e
ν
− →e∗ ν ∗−1
− − − →e∗∗
(2) For each object c, τ (c∗) and τ (c)∗ are inverse isomorphisms.
(3) For any object a, the following diagram commutes
a∗ ⊗ e
1⊗ν
− − − − →a∗ ⊗ e∗
ρ(a∗)


↓


↓ γ(a,e)
a∗ − − − − →
λ∗(a)
(e ⊗ a)∗
(4) For any object a, the following diagram commutes
e ⊗ a∗ ν⊗1
− − − − →e∗ ⊗ a∗
λ(a∗)


↓


↓ γ(e,a)
a∗ − − − − →
ρ∗(a)
(a ⊗ e)∗
(5) For all objects a, b and c, the following diagram commutes
(c∗ ⊗ b∗) ⊗ a∗ γ(c,b)⊗1
− − − − − →(b ⊗ c)∗ ⊗ a∗ γ(b⊗c,a)
− − − − − →(a ⊗ (b ⊗ c))∗
α(c∗,b∗,a∗)


↓


↓ α∗(a,b,c)
c∗ ⊗ (b∗ ⊗ a∗)
1⊗γ(b,a)
− − − − − →c∗ ⊗ (a ⊗ b)∗ γ(c,a⊗b)
− − − − − →((a ⊗ b) ⊗ c)∗
(6) For all objects a and b the following diagram commutes
a ⊗ b − − − − →
τ (a⊗b)
(a ⊗ b)∗∗
τ (a)⊗τ (b)


↓


↓ γ∗(b,a)
a∗∗ ⊗ b∗∗ γ(a∗,b∗)
− − − − − →(b∗ ⊗ a∗)∗
