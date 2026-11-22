---
doc_id: arxiv-hep-th-9310164v2
doc_title: "SPHERICAL CATEGORIES"
section_id: page-006
section_title: "Page 6"
section_number: null
pages: 6-6
source_pdf: 9310164v2.pdf
source_sha256: e0972e04667ccc47
toc_source: undetermined
doc_brief: "SPHERICAL CATEGORIES — This paper is a study of monoidal categories with duals where the ten- sor product need not be commutative."
---
6
JOHN W. BARRETT & BRUCE W. WESTBURY
Note that the following diagram shows that τ(a)∗∗= τ(a∗∗) for any object a
follows from the condition that τ is a natural transformation with each component
an isomorphism.
a
τ(a)
−−−−→
a∗∗
τ(a)
y
yτ ∗∗(a)
a∗∗−−−−→
τ(a∗∗)
a∗∗∗∗
This is implied by condition (2) but not conversely.
It is trivial that if the natural transformations are coherent then each of these
diagrams commutes. It remains to prove the converse.
Lemma 1.10. Any iterated natural transformation is equal to a reduced iterated
natural transformation.
Proof. There are six natural transformations α, λ, ρ, γ, τ and ν and six condi-
tions above.
Furthermore each condition has exactly one instance which is not
reduced and for each natural transformation there is exactly one condition which
contains an instance of that natural transformation which is not reduced. Hence,
by applications of these diagrams and their images by ∗, any instance is equal to
a reduced iterated natural transformation and it follows that any iterated natural
transformation is equal to a reduced iterated natural transformation.
This shows that it is suﬃcient to prove the coherence theorem for reduced iter-
ated natural transformations. Any reduced iterate of (α, λ, ρ) and their inverses is
called a central iterate. Maclane proves the coherence theorem for central iterates
in [MacLane 1963].
Lemma 1.11. Any expansion of an instance of γ, τ, or ν (but not their inverses)
composed with a central iterate is equal to a central iterate composed with a expan-
sion of an instance of γ, τ, or ν.
Proof. This follows from the condition that the central iterate is a natural transfor-
mation and that each component of the expansion is a morphism. The commutative
square which contains both of these provides the proof.
An example is provided by the following commutative diagram:
((F ∗⊗G∗) ⊗H) ⊗J
α(F ∗⊗G,H,J)
−−−−−−−−−→
(F ∗⊗G∗) ⊗(H ⊗J)
(γ(F,G)⊗1H)⊗1J
y
yγ(F,G)⊗1H⊗J
((G ⊗F)∗⊗H) ⊗J
−−−−−−−−−−→
α((G⊗F )∗,H,J)
(G ⊗F)∗⊗(H ⊗J)
Deﬁnition 1.12. The set of standard iterated functors is the smallest set of iter-
ated functors which satisﬁes:
(1) The iterates e, 1 and ∗are standard.
(2) If F̸ = e is standard then F ⊗1 and F ⊗∗are standard.
