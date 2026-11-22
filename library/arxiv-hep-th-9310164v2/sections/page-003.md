---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-003
section_title: "Page 3"
section_number: null
pages: 3-3
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
SPHERICAL CATEGORIES
3
set of conditions for coherence to hold.
In the following deﬁnition it is convenient to regard the distinguished object e as
a functor from the category with one morphism to C. Then λ and ρ can be deﬁned
to be natural transformations.
Deﬁnition 1.1. A monoidal category is a category, C, together with a functor
⊗: C × C →C an object e, and natural transformations
α: (⊗× 1)⊗→(1 × ⊗)⊗
λ: e ⊗1 →1
ρ: 1 ⊗e →1
Each component of each of the natural transformations α, λ and ρ is required to
be an isomorphism. This data is also required to be coherent which is equivalent to
requiring that α satisfy the pentagon identity and that ρ and λ satisfy a triangular
identity. Also, ρ(e) = λ(e): e ⊗e →e. These conditions are given in [MacLane
1971].
If each component of the natural transformations α, λ and ρ is the identity map
then the category is called strict monoidal.
If C is a category, then the opposite category C−is the category obtained by
reversing morphisms. If F: C →D is a functor, then F −: C−→D−is the corre-
sponding functor on the opposites. A functor C−→D is the same as a contravari-
ant functor C →D.
Deﬁnition 1.2. Let (C, ⊗, e, α, λ, ρ) be a monoidal category. Then the data needed
to make this a category with duals is a functor, ∗: C−→C, and natural transfor-
mations
(1) τ: 1 →∗∗,
(2) γ: (∗× ∗) ◦⊗→⊗op ◦∗
and an isomorphism ν: e →e∗.
Each component of the natural transformations τ and γ is required to be an
isomorphism. A category with data satisfying these conditions is called a category
with dual data.
Deﬁnition 1.3. A category with dual data is strict if each component of the
natural transformations γ and τ is the identity map and the map ν is the identity
map. In this case the category is called a category with strict dual data.
In the following deﬁnition, if α = (±, ±, . . . , ±) is an n-tuple of signs, then Cα
denotes the category C± × C± × . . . × C±, with C+ ≡C. Also, if 0 is the 0-tuple,
then C0 is the category with one morphism, so that e: C0 →C.
It is convenient to regard ν as a natural transformation from the functor e to
the functor e−◦∗.
Deﬁnition 1.4. The set of iterates of the functors ⊗, ∗and e is the smallest set
of functors F: Cα →C which satisﬁes the following conditions:
(1) The functor e: C0 →C is an iterate.
