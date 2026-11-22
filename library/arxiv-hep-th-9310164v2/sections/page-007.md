---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-007
section_title: "Page 7"
section_number: null
pages: 7-7
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
SPHERICAL CATEGORIES
7
Deﬁnition 1.13. The set of reduced iterated functors is the smallest set of iterated
functors which satisﬁes:
(1) The iterates e, 1 and ∗are reduced.
(2) If F and G are reduced then F ⊗G is reduced.
Deﬁne two iterated functors, F and G, to be equivalent if there is an iterated
natural transformation from F to G. This is obviously an equivalence relation.
Deﬁnition 1.14. The rank r and luminosity, l, of an iterated functor are deﬁned
recursively as follows:
(1) r(e) = 1 and r(1) = 1
(2) r(F ⊗G) = r(F) + r(G) + 1
(3) r(F ∗) = r(F)
(1) l(e) = 0 and l(1) = 0.
(2) l(F ⊗G) = l(F) + l(G).
(3) l(F ∗) = l(F) + r(F).
The rank is a modiﬁed multiplicity, and the luminosity is a measure of the number
of stars. The luminosity is unaﬀected by central iterated natural transformations,
but is increased by instances of γ, τ and ν.
Lemma 1.15. For any iterated functor F, there is a unique reduced iterated functor
R and a unique natural transformation R →F which is an iterate of instances of
γ, τ and ν.
Proof. The proof is by induction on the sum of the luminosity and the rank of F.
Any iterated functor is of the form
(1) F ∗∗.
(2) (F ⊗G)∗.
(3) e∗
(4) F ⊗G.
(5) 1, ∗, or e.
and the only instances of γ, τ and ν which have these as range are
(1) τ: F →F ∗∗
(2) γ: (G∗) ⊗(F ∗) →(F ⊗G)∗
(3) ν: e →e∗
(4) A ⊗1 or 1 ⊗B
(5) none.
In the ﬁrst three cases, the conclusion follows from the induction hypothesis applied
to the domain of the natural transformation, which has the same rank and lower
luminosity. In (4), the induction hypothesis can be applied to F and G separately,
which have lower rank and luminosity which is no greater. The conclusion follows
as the natural transformations A ⊗1 and 1 ⊗B commute. The functors in (5) are
reduced iterated functors, and F = R.
