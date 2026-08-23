---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: sec-008-10-john-w-barrett-bruce-w-westbury
section_title: "JOHN W. BARRETT & BRUCE W. WESTBURY"
section_number: 10
pages: 10-12
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where th e ten- sor product need not be commutative."
---
M
Figure 1
Deﬁnition 2.4. Let a be any object in a pivotal category. Then the monoid
End(a) has two trace maps, tr L, trR: End(a) → End(e). In a pivotal category
trL(f ) is deﬁned to be the composite
e
ǫ(a∗)
− − − →a∗ ⊗ a∗∗ 1⊗τ − 1(a)
− − − − − − →a∗ ⊗ a
1⊗f
− − →a∗ ⊗ a
τ (a∗)⊗τ (a)
− − − − − − − →
a∗∗∗ ⊗ a∗∗ γ(a∗∗,a∗)
− − − − − − →(a∗ ⊗ a∗∗)∗ ǫ∗(a∗)
− − − − →e∗ ν
− →e
and tr R(f ) is deﬁned to be the composite
e
ǫ(a)
− − →a ⊗ a∗ f ⊗1
− − →a ⊗ a∗ τ (a)⊗1
− − − − →a∗∗ ⊗ a∗ γ(a∗,a)
− − − − →(a ⊗ a∗)∗ ǫ∗(a)
− − − →e∗ ν
− →e
In a strict pivotal category these deﬁnitions simplify to:
trL(f ) = ǫ(a∗)(1 ⊗ f )ǫ(a∗)∗
trR(f ) = ǫ(a)(f ⊗ 1)ǫ(a)∗
These are called trace maps because they satisfy tr L(f g) = tr L(gf ) and tr R(f g) =
trR(gf ).
Deﬁnition 2.5. A pivotal category is spherical if, for all objects a and all mor-
phisms f : a → a,
trL(f ) = tr R(f ).
An equivalent condition is that trL(f ) = trL(f ∗), for all f : a → a. Also, in a
spherical category, tr L(f ⊗ g) = tr L(f ). trL(g) (where the product is in End( e)) for
all f : a → a and all g: b → b.
In the rest of this paper we study additive spherical categor ies. This means that
each Hom set is a ﬁnitely generated abelian group; and that th e data deﬁning the
spherical structure is compatible with the additive struct ure. This means that ⊗ is
Z-bilinear, that ∗ is Z-linear and all components of all the natural transformatio ns
in the pivotal data are multilinear over Z.
In any additive monoidal category End( e) is a commutative ring (see [Kelly and
Laplaza 1980]) and we denote this ring by F. In particular the trace map, tr L,
takes values in this ring. It follows that an additive monoid al category is F-linear,
by using the structure maps of λ and ρ, and that if the category is pivotal then the
data deﬁning the pivotal structure is F-linear.
The main examples of additive spherical categories arise as the category of rep-
resentations of a Hopf algebra with some additional structu re. This is discussed in
detail in the next section.
SPHERICAL CATEGORIES 11
Example 2.6. An example of an additive spherical category which cannot be
regarded as a category whose objects are ﬁnitely generated f ree modules is given
by taking the free Z[q, q−1, z]-linear category on the category of oriented tangles
and then taking the quotient by the well-known skein relatio n for the HOMFLY
polynomial. This is an additive spherical category and for e ach pair of objects a and
b, Hom( a, b) is a ﬁnitely generated free Z[q, q−1, z]-module. However the objects
cannot be taken to be ﬁnitely generated modules unless z is a quantum integer.
Deﬁnition 2.7. For any two objects a and b there is a bilinear pairing
Θ: Hom( a, b) × Hom(b, a) → F
deﬁned by Θ( f, g) = tr L(f g) = tr L(gf ).
Deﬁnition 2.8. A spherical category is non-degenerate if, for all objects a and b,
the pairing Θ is non-degenerate.
The next theorem shows that every additive spherical catego ry has a natural quo-
tient which is a non-degenerate spherical category. This co nstruction is mentioned
in [Turaev 1992].
Theorem 2.9. Let C be an additive spherical category. Deﬁne the subcategory J
to have the same set of objects and morphisms deﬁned by
HomJ (c1, c2) = {f ∈ HomC(c1, c2) : tr L(f g) = 0 for all g ∈ HomC(c2, c1)}
Then C/J is a non-degenerate additive spherical category.
Proof. It is clear that J is closed under composition on either side by arbitrary
morphisms in C. Hence the quotient is an additive category. It is also clear that
f ∈ J if and only if f ∗ ∈ J and so the functor ∗ is well-deﬁned on the quotient.
The functor ⊗ is well-deﬁned on the quotient since f ∈ J implies f ⊗ g1 ∈ J and
g2 ⊗ f ∈ J for arbitrary morphisms in C. This follows from the observation that
trL((f ⊗ g)h) can always be written as tr L(f h′) for a morphism h′, which can be
constructed from g and h.1
The structure maps of the natural transformations α, λ, ρ, γ, ν, τ and the
morphisms ǫ(a) are taken to be the images in the quotient of the given morphi sms
in C. The conditions on this structure which imply that this quot ient is spherical
follow from the same conditions in C.
Each pairing Θ is non-degenerate by construction.
3. Spherical Hopf algebras
In this section we introduce spherical Hopf algebras. These are deﬁned to be
Hopf algebras with some additional structure which implies that the category of
ﬁnitely generated modules is a spherical category.
1We thank Marco Mackaay for pointing out that this argument was g iven incorrectly in [Barrett
and Westbury 1996].
