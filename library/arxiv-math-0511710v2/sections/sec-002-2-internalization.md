---
doc_id: arxiv-math-0511710v2
doc_title: "Higher Gauge Theory John Baez Department of Mathematics University of California"
section_id: sec-002-2-internalization
section_title: "Internalization"
section_number: 2
pages: 8-9
source_pdf: 0511710v2.pdf
source_sha256: f88f50d459080490
doc_brief: "Higher Gauge Theory John Baez Department of Mathematics University of California — Just as gauge theory describes the parallel transport of poi nt particles using connections on bundles, higher gauge"
---
The idea of internalization is simple: given a mathematical concept X deﬁned
solely in terms of sets, functions and commutative diagrams involving these, and
given some category K, one obtains the concept of an ‘ X in K’ by replacing
all these sets, functions and commutative diagrams by corre sponding objects,
morphisms, and commutative diagrams in K.
The case we need here is when X is the concept of ‘category’:
Deﬁnition 1. Let K be a category. An internal category in K, or simply
category in K, say C, consists of:
• an object Ob(C) ∈ K,
• an object Mor(C) ∈ K,
• source and target morphisms s, t: Mor(C) → Ob(C),
• an identity-assigning morphism i: Ob(C) → Mor(C),
• a composition morphism ◦: Mor(C)s×tMor(C) → Mor(C)
satisfying the usual rules of a category expressed in terms o f commutative dia-
grams.
Here Mor(C)s×tMor(C) is deﬁned using a pullback: if K is the category of sets,
it is the set of composable pairs of morphisms in C. Inherent in the deﬁnition is
the assumption that this pullback exist, along with the othe r pullbacks needed
to write the rules of a category as commutative diagrams.
We can similarly deﬁne a functor in K and a natural transformation
in K; details can be found in Borceux’s handbook [32]. There is a 2 -category
KCat whose objects, morphisms and 2-morphisms are categorie s, functors and
natural transformations in K. To study symmetries in higher gauge theory, we
need these examples:
Deﬁnition 2. Let LieGrp be the category whose objects are Lie groups and
whose morphisms are Lie group homomorphisms. Then the objec ts, morphisms
and 2-morphisms of LieGrpCat are called Lie 2-groups , Lie 2-group homo-
morphisms, and Lie 2-group 2-homomorphisms , respectively.
8
Deﬁnition 3. Let LieAlg be the category whose objects are Lie algebras and
whose morphisms are Lie algebra homomorphisms. Then the obj ects, morphisms
and 2-morphisms of LieAlgCat are called Lie 2-algebras , Lie 2-algebra ho-
momorphisms, and Lie 2-algebra 2-homomorphisms , respectively.
For the beneﬁt of experts, we should admit that we are only deﬁ ning ‘strict’
Lie 2-groups and Lie 2-algebras, where all the usual laws hol d as equations. We
rarely need any other kind in this paper, but there are more ge neral Lie 2-groups
and Lie 2-algebras where the usual laws hold only up to isomor phism [12, 13].
We could also consider categories in Diﬀ, the category whose objects are
ﬁnite-dimensional smooth manifolds and whose morphisms ar e smooth maps.
Ehresmann [33] introduced these in the late 1950’s under the name of ‘diﬀer-
entiable categories’. However, these are not quite what we w ant here, for two
reasons. First, unlike LieGrp and LieAlg, Diﬀ does not have p ullbacks in gen-
eral. This means that when we try to deﬁne a category in Diﬀ, th e set of
composable pairs of morphisms is not automatically a smooth manifold. Sec-
ond, the space of smooth paths in a smooth manifold is not agai n a smooth
manifold. This is an annoyance when studying connections on bundles.
To solve these problems, we want a category of ‘smooth spaces ’ that has
pullbacks and includes path spaces. Various categories of t his sort have been
proposed. It is unclear which one is best, but we shall use the last of several
variants proposed by Chen [34, 35]. In what follows, we use convex set to mean
a convex subset of Rn, where n is arbitrary (not ﬁxed). Any convex set inherits
a topology from its inclusion in Rn. We say a map f between convex sets is
smooth if arbitrarily high derivatives of f exist and are continuous, using the
usual deﬁnition of derivative as a limit of a quotient.
Deﬁnition 4. A smooth space is a set X equipped with, for each convex set
C, a collection of functions φ: C → X called plots in X, such that:
