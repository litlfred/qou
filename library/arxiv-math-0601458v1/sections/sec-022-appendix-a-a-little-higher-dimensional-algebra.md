---
doc_id: arxiv-math-0601458v1
doc_title: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS"
section_id: sec-022-appendix-a-a-little-higher-dimensional-algebra
section_title: "Appendix A. A Little Higher-Dimensional Algebra"
section_number: null
pages: 61-62
source_pdf: 0601458v1.pdf
source_sha256: ef34611620cfd0bd
toc_source: outline
doc_brief: "CATEGORIFIED ALGEBRA AND QUANTUM MECHANICS — Interest in combinatorial interpretations of mathematical entities stems from the convenience of the concrete models they provide."
---
Appendix A. A Little Higher-Dimensional Algebra
Deﬁnition 34. A rig, or semiring, is a set R with two operations, which we cus-
tomarily denote by + and ·, referred to as addition and multiplication respectively,
such that (R, +) is a commutative monoid with identity 0, (R, ·) is a monoid with
identitiy 1. We also require that multiplication distributes over addition on the left
and right, and 0 is ﬁxed under multiplication by any a ∈R.
Deﬁnition 35. A monoidal category Mis a category equipped with a functor
⊗: M × M →M, a unit object 1 ∈M, and natural isomorphisms α, λ, ρ with
components αA,B,C : (A ⊗B) ⊗C →A ⊗(B ⊗C) (the associator), λA : 1 ⊗A →
A (the left unit), and ρA : A ⊗1 →A (the right unit), satisfying coherence
conditions6. A 2-rig is a monoidal cocomplete category: a monoidal category C
which has all colimits, such that the functors X ⊗−: C →C and −⊗X : C →C
preserve colimits for all objects X ∈C.
Theorem 13. The category Set[Z] is a 2-rig whose monoidal operation ⊗is the
product · of structure types.
Proof. To see that · is a monoidal operation, note that the unit object is 1, which
can only be put on the empty set, in exactly one way. Putting a (1 · F)-structure
or (F · 1)-structure on a set S means taking S = S ⊎{}, putting an F-structure on
S and a 1-structure on {}. This is equivalent to putting an F-structure on S, so we
have left and right units. The associator αF,F ′,F ′′ : (F · F ′) · F ′′ →F · (F ′ · F ′′) is
the natural isomorphism induced by the set isomorphism between (A + B) + Cand
A + (B + C). Splitting S into A + B + C in these two ways, and putting an F-
structure on A, F ′-structure on B and F ′′-structure on C can been seen as a way
of putting an (F + F ′)-structure on (A + B) and an F ′′-structure on C, but also as
putting an F-structure on A and an (F ′ + F ′′)-structure on (B + C). In fact this
α is a natural isomorphism, so · is indeed a monoidal operation.
To see that Set[Z] is cocomplete - contains all colimits - note that Set is co-
complete. Moreover, by taking colimits of the sets of structures on each n, we can
ﬁnd arbitrary colimits of objects of Set[Z].
To see that Set[Z] is monoidal cocomplete, we now only have to have that the
multiplication functors F · −and −· F preserve colimits for all structure types F
(i.e. the “product” distributes over “sum”).
□
6See, for instance, MacLane [13]. This deﬁnition includes slightly more than the deﬁnition of
a rig because we here explain the generalization of associativity for the monoidal operation. Also,
we extend the “addition” operation to general colimits - of which coproducts, the equivalent of
binary sums, are an example. Otherwise, the two defenitions have the same form.
62 JEFFREY MORTON
