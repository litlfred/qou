---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-011
section_title: "Page 11"
section_number: null
pages: 11-11
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
SPHERICAL CATEGORIES
11
Example 2.6. An example of an additive spherical category which cannot be
regarded as a category whose objects are ﬁnitely generated free modules is given
by taking the free Z[q, q−1, z]-linear category on the category of oriented tangles
and then taking the quotient by the well-known skein relation for the HOMFLY
polynomial. This is an additive spherical category and for each pair of objects a and
b, Hom(a, b) is a ﬁnitely generated free Z[q, q−1, z]-module. However the objects
cannot be taken to be ﬁnitely generated modules unless z is a quantum integer.
Deﬁnition 2.7. For any two objects a and b there is a bilinear pairing
Θ: Hom(a, b) × Hom(b, a) →F
deﬁned by Θ(f, g) = trL(fg) = trL(gf).
Deﬁnition 2.8. A spherical category is non-degenerate if, for all objects a and b,
the pairing Θ is non-degenerate.
The next theorem shows that every additive spherical category has a natural quo-
tient which is a non-degenerate spherical category. This construction is mentioned
in [Turaev 1992].
Theorem 2.9. Let C be an additive spherical category. Deﬁne the subcategory J
to have the same set of objects and morphisms deﬁned by
HomJ (c1, c2) = {f ∈HomC(c1, c2) : trL(fg) = 0
for all g ∈HomC(c2, c1)}
Then C/J is a non-degenerate additive spherical category.
Proof. It is clear that J is closed under composition on either side by arbitrary
morphisms in C. Hence the quotient is an additive category. It is also clear that
f ∈J if and only if f ∗∈J and so the functor ∗is well-deﬁned on the quotient.
The functor ⊗is well-deﬁned on the quotient since f ∈J implies f ⊗g1 ∈J and
g2 ⊗f ∈J for arbitrary morphisms in C. This follows from the observation that
trL((f ⊗g)h) can always be written as trL(fh′) for a morphism h′, which can be
constructed from g and h.1
The structure maps of the natural transformations α, λ, ρ, γ, ν, τ and the
morphisms ǫ(a) are taken to be the images in the quotient of the given morphisms
in C. The conditions on this structure which imply that this quotient is spherical
follow from the same conditions in C.
Each pairing Θ is non-degenerate by construction.
3. Spherical Hopf algebras
In this section we introduce spherical Hopf algebras. These are deﬁned to be
Hopf algebras with some additional structure which implies that the category of
ﬁnitely generated modules is a spherical category.
1We thank Marco Mackaay for pointing out that this argument was given incorrectly in [Barrett
and Westbury 1996].
