---
doc_id: arxiv-hep-th-9310164v2
doc_title: ""
section_id: sec-006-6-john-w-barrett-bruce-w-westbury
section_title: "JOHN W. BARRETT & BRUCE W. WESTBURY"
section_number: 6
pages: 6-8
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
doc_brief: "This paper is a study of monoidal categories with duals where th e ten- sor product need not be commutative. The motivating examples are categories of representations of Hopf algebras."
---
Note that the following diagram shows that τ (a)∗∗ = τ (a∗∗) for any object a
follows from the condition that τ is a natural transformation with each component
an isomorphism.
a
τ (a)
− − − − →a∗∗
τ (a)


↓


↓ τ ∗∗(a)
a∗∗ − − − − →
τ (a∗∗)
a∗∗∗∗
This is implied by condition (2) but not conversely.
It is trivial that if the natural transformations are cohere nt then each of these
diagrams commutes. It remains to prove the converse.
Lemma 1.10. Any iterated natural transformation is equal to a reduced it erated
natural transformation.
Proof. There are six natural transformations α, λ, ρ, γ, τ and ν and six condi-
tions above. Furthermore each condition has exactly one ins tance which is not
reduced and for each natural transformation there is exactl y one condition which
contains an instance of that natural transformation which i s not reduced. Hence,
by applications of these diagrams and their images by ∗, any instance is equal to
a reduced iterated natural transformation and it follows th at any iterated natural
transformation is equal to a reduced iterated natural trans formation.
This shows that it is suﬃcient to prove the coherence theorem for reduced iter-
ated natural transformations. Any reduced iterate of ( α, λ, ρ) and their inverses is
called a central iterate. Maclane proves the coherence theo rem for central iterates
in [MacLane 1963].
Lemma 1.11. Any expansion of an instance of γ, τ , or ν (but not their inverses)
composed with a central iterate is equal to a central iterate composed with a expan-
sion of an instance of γ, τ , or ν.
Proof. This follows from the condition that the central iterate is a natural transfor-
mation and that each component of the expansion is a morphism . The commutative
square which contains both of these provides the proof.
An example is provided by the following commutative diagram :
((F ∗ ⊗ G∗) ⊗ H) ⊗ J
α(F ∗⊗G,H,J )
− − − − − − − − − →(F ∗ ⊗ G∗) ⊗ (H ⊗ J)
(γ(F,G)⊗1H )⊗1J


↓


↓ γ(F,G)⊗1H⊗ J
((G ⊗ F )∗ ⊗ H) ⊗ J − − − − − − − − − − →
α((G⊗F )∗,H,J )
(G ⊗ F )∗ ⊗ (H ⊗ J)
Deﬁnition 1.12. The set of standard iterated functors is the smallest set of i ter-
ated functors which satisﬁes:
(1) The iterates e, 1 and ∗ are standard.
(2) If F ⁄= e is standard then F ⊗ 1 and F ⊗ ∗ are standard.
SPHERICAL CATEGORIES 7
Deﬁnition 1.13. The set of reduced iterated functors is the smallest set of it erated
functors which satisﬁes:
(1) The iterates e, 1 and ∗ are reduced.
(2) If F and G are reduced then F ⊗ G is reduced.
Deﬁne two iterated functors, F and G, to be equivalent if there is an iterated
natural transformation from F to G. This is obviously an equivalence relation.
Deﬁnition 1.14. The rank r and luminosity, l, of an iterated functor are deﬁned
recursively as follows:
(1) r(e) = 1 and r(1) = 1
(2) r(F ⊗ G) = r(F ) + r(G) + 1
(3) r(F ∗) = r(F )
(1) l(e) = 0 and l(1) = 0.
(2) l(F ⊗ G) = l(F ) + l(G).
(3) l(F ∗) = l(F ) + r(F ).
The rank is a modiﬁed multiplicity, and the luminosity is a me asure of the number
of stars. The luminosity is unaﬀected by central iterated na tural transformations,
but is increased by instances of γ, τ and ν.
Lemma 1.15. For any iterated functor F , there is a unique reduced iterated functor
R and a unique natural transformation R → F which is an iterate of instances of
γ, τ and ν.
Proof. The proof is by induction on the sum of the luminosity and the r ank of F .
Any iterated functor is of the form
(1) F ∗∗.
(2) ( F ⊗ G)∗.
(3) e∗
(4) F ⊗ G.
(5) 1, ∗, or e.
and the only instances of γ, τ and ν which have these as range are
(1) τ : F → F ∗∗
(2) γ: (G∗) ⊗ (F ∗) → (F ⊗ G)∗
(3) ν: e → e∗
(4) A ⊗ 1 or 1 ⊗ B
(5) none.
In the ﬁrst three cases, the conclusion follows from the indu ction hypothesis applied
to the domain of the natural transformation, which has the sa me rank and lower
luminosity. In (4), the induction hypothesis can be applied to F and G separately,
which have lower rank and luminosity which is no greater. The conclusion follows
as the natural transformations A ⊗ 1 and 1 ⊗ B commute. The functors in (5) are
reduced iterated functors, and F = R.
