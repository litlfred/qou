---
doc_id: arxiv-hep-th-9310164v2
doc_title: ""
section_id: sec-004-2-spherical-categories
section_title: "Spherical categories"
section_number: 2
pages: 1-4
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
doc_brief: "This paper is a study of monoidal categories with duals where th e ten- sor product need not be commutative. The motivating examples are categories of representations of Hopf algebras."
---
3. Spherical Hopf algebras
0. Introduction
In this paper we introduce the notion of a spherical category . The motivation
for this and the main application is to generalise the Turaev -Viro state sum model
invariant of a closed piecewise-linear 3-manifold. This ap plication is discussed sep-
arately in [Barrett and Westbury 1996].
A spherical category is deﬁned to be a pivotal category which satisﬁes an extra
condition, which states that two trace maps are equal. The un iversal strict pivotal
category has an interpretation in terms of planar graphs. A n umber of authors have
introduced categories whose morphisms are deﬁned in terms o f diagrams and which
have applications to low dimensional topology (for example , [Freyd and Yetter
1989], [Joyal and Street 1991], [Reshetikhin and Turaev 199 0]). The main diﬀerence
between pivotal and spherical categories and these categor ies is that pivotal and
spherical categories are not required to be braided. Howeve r, any braided pivotal
category satisﬁes the extra spherical condition. The geome trical interpretation of
the extra condition, and the reason for the terminology, is t hat in a pivotal category
Typeset by AMS-TEX
1
2 JOHN W. BARRETT & BRUCE W. WESTBURY
planar graphs are equivalent under isotopies of the plane wh ereas in a spherical
category closed planar graphs are equivalent under isotopi es of the 2-sphere.
The ﬁrst part of the paper gives the deﬁnition of a monoidal ca tegory with duals
and the proof of a coherence theorem. The proof follows the pr oof of the coherence
theorem for monoidal categories in [MacLane 1963]. A monoid al category with duals
can be thought of as an abstraction of the category of represe ntations of a Hopf
algebra, except that we require each object to be reﬂexive. A coherence theorem
for categories with duals is given in [Kelly and Laplaza 1980 ]. The diﬀerences
between this result and ours are that we do not assume that the monoidal category
is symmetric but we do assume that all objects are reﬂexive. T he diﬀerence between
their proof and ours is that they emphasise the adjunctions i nvolving Hom and ⊗
whereas we emphasise the contravariant duality functor (following [Freyd and Yetter
1989]). The reason we need this result is that the category of representations of a
Hopf algebra is not strict.
The main sources of spherical categories are categories of r epresentations of Hopf
algebras with a distinguished element satisfying conditio ns. These are called spher-
ical Hopf algebras. The two main examples of such Hopf algebr as are involutory
Hopf algebras and ribbon Hopf algebras (such as quantised en veloping algebras).
The reason we consider the more general notion of a spherical category instead
of spherical Hopf algebras is that in the applications to 3-m anifold invariants it is
necessary to pass to a quotient. This quotient is not the cate gory of representations
of a Hopf algebra. The deﬁnition of this quotient applies to a ny additive spherical
category.
In the last section we show that the quotient of the category o f representations
of a spherical Hopf algebra is semisimple. This is the main re sult in the paper. The
proof uses properties of the matrix trace and does not apply t o the quotient of an
arbitrary additive spherical category. Although this quot ient is semisimple the set
of isomorphism classes of simple objects may be inﬁnite even if the original Hopf
algebra is ﬁnite dimensional. The construction of 3-manifo ld invariants depends on
ﬁnding a spherical subcategory such that, in the semisimple quotient of this subcat-
egory, the set of isomorphism classes of simple objects is ﬁn ite. For each quantised
enveloping algebra at a root of unity such a subcategory can b e constructed using
the results in [Andersen 1992] and [Andersen and Paradowski 1995].
1. Monoidal categories with duals
In this section we study monoidal categories with duals. Exa mples are ﬁnitely
generated free modules over a commutative ring. In these exa mples the tensor
product is commutative, but we do not require this. The motiv ating examples
of monoidal categories with duals are the categories of repr esentations of Hopf
algebras. These categories have a contravariant functor gi ven by the contragradient
dual but are not categories with duals, in general, as we requ ire that each object
be reﬂexive.
The only result in this section is a coherence theorem. The pr oof follows the
coherence theorem for monoidal categories in [MacLane 1963 ]. The deﬁnition of
coherence involves an inﬁnite set of diagrams. A coherence t heorem gives a ﬁnite
SPHERICAL CATEGORIES 3
set of conditions for coherence to hold.
In the following deﬁnition it is convenient to regard the dis tinguished object e as
a functor from the category with one morphism to C. Then λ and ρ can be deﬁned
to be natural transformations.
Deﬁnition 1.1. A monoidal category is a category, C, together with a functor
⊗: C × C → C an object e, and natural transformations
α: (⊗ × 1)⊗ → (1 × ⊗)⊗
λ: e ⊗ 1 → 1
ρ: 1 ⊗ e → 1
Each component of each of the natural transformations α, λ and ρ is required to
be an isomorphism. This data is also required to be coherent w hich is equivalent to
requiring that α satisfy the pentagon identity and that ρ and λ satisfy a triangular
identity. Also, ρ(e) = λ(e): e ⊗ e → e. These conditions are given in [MacLane
1971].
If each component of the natural transformations α, λ and ρ is the identity map
then the category is called strict monoidal.
If C is a category, then the opposite category C− is the category obtained by
reversing morphisms. If F : C → D is a functor, then F −: C− → D− is the corre-
sponding functor on the opposites. A functor C− → D is the same as a contravari-
ant functor C → D.
Deﬁnition 1.2. Let (C, ⊗, e, α, λ, ρ) be a monoidal category. Then the data needed
to make this a category with duals is a functor, ∗: C− → C , and natural transfor-
mations
(1) τ : 1 → ∗∗,
(2) γ: (∗ × ∗) ◦ ⊗ → ⊗ op ◦ ∗
and an isomorphism ν: e → e∗.
Each component of the natural transformations τ and γ is required to be an
isomorphism. A category with data satisfying these conditi ons is called a category
with dual data.
Deﬁnition 1.3. A category with dual data is strict if each component of the
natural transformations γ and τ is the identity map and the map ν is the identity
map. In this case the category is called a category with stric t dual data.
In the following deﬁnition, if α = ( ±, ±, . . . , ±) is an n-tuple of signs, then Cα
denotes the category C± × C ± × . . . × C ±, with C+ ≡ C . Also, if 0 is the 0-tuple,
then C0 is the category with one morphism, so that e: C0 → C .
It is convenient to regard ν as a natural transformation from the functor e to
the functor e− ◦ ∗.
Deﬁnition 1.4. The set of iterates of the functors ⊗, ∗ and e is the smallest set
of functors F : Cα → C which satisﬁes the following conditions:
(1) The functor e: C0 → C is an iterate.
