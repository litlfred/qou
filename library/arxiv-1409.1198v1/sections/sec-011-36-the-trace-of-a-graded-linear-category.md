---
doc_id: arxiv-1409.1198v1
doc_title: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR"
section_id: sec-011-36-the-trace-of-a-graded-linear-category
section_title: "The trace of a graded linear category"
section_number: 3.6
pages: 18-19
source_pdf: 1409.1198v1.pdf
source_sha256: 13ecb6c28bab6744
doc_brief: "TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR — Categoriﬁcation is a process of lifting structures to a high er categorical level."
---
an auto-equivalence ⟨1⟩. We denote by ⟨t⟩ the auto-equivalence obtained by applying ⟨1⟩t times. Thus,
given any object x ∈ Ob(C), there exists an object x⟨t⟩ ∈ Ob(C) for all t. Likewise, given any morphism
f : x → y in C, there is a morphism f ⟨t⟩: x⟨t⟩ → y⟨t⟩. This equips Hom-sets with the structure of
/CI -graded abelian groups in which composition maps are grading preser ving.
Given a graded linear category C, its Grothendieck group K0(C) is a /CI [q,q −1]-module with [x⟨t⟩]∼= :=
qt[x]. Likewise, the trace Tr( C) is /CI [q,q −1]-module with [f ⟨t⟩] = qt[f ] for an endomorphism f : x →x
in C. In this case, the generalized Chern character map
K0(C) → Tr(C)
is a homomorphism of /CI [q,q −1]-modules.
A graded linear category C is said to admit a translation if for every object x in C and integer t ∈ /CI ,
there is an isomorphism x → x⟨t⟩. Given any graded linear category C, we can form a graded linear
category C∗ that admits translations by declaring that Ob( C) = Ob( C∗) and setting
C∗(x,y ) :=
⨁
t∈ /CI
C(x,y ⟨t⟩),
for all objects x,y ∈ Ob(C). The translations x →x⟨t⟩ is given by 1 x in C∗ since
1x ∈ C (x,x ⟨0⟩) = C (x, (x⟨t⟩) ⟨−t⟩) ⊂ C ∗(x,x ⟨t⟩),
has inverse
1x⟨t⟩ ∈ C (x⟨t⟩,x ⟨t⟩) = C(x⟨t⟩, (x⟨0⟩)⟨t⟩) ⊂ C ∗(x⟨t⟩,x ).
By enlarging the hom spaces by adding isomorphisms x →x⟨t⟩, the Grothendieck group of graded
linear category with translation C∗ is only a /CI -module rather than a /CI [q,q −1]-module since [x⟨t⟩]∼= =
[x]∼=. However, the trace Tr( C∗) changes more drastically because, rather than only considering d egree
TRACE AS AN ALTERNATIVE DECATEGORIFICATION FUNCTOR 19
preserving endomorphisms f : x → x in C, we can now consider arbitrary degree maps x → x⟨t⟩ and
compose with the translation map from x⟨t⟩ →x to get a new endomorphism. Furthermore, using the
translationsx ∼=x⟨t⟩, it is not hard to see that given any endomorphism f : x →x, we have [f ⟨t⟩] = [f ]
in Tr(C∗), so that the graded version of the trace Tr( C∗) is also just a /CI -module.
As explained at the beginning of section 3.1, any ring with unit can be vie wed as a linear category
with one object ∗. A graded ring R = ⊕n∈ /CI
Rn can be viewed as a graded category whose objects are
indexed by the integers n = ∗⟨n⟩ for n ∈ /CI . The morphisms from n to m are given by the abelian
group Rm−n. Composition is given by the grading preserving multiplication in R. Example 7 can be
generalized to show that the generalized Chern character map K0(R) → Tr(R0) is an isomorphism
wheneverR is a graded local ring, so that the trace of the degree zero part of the ring is isomorphic to
the Grothendieck ring.
Exercise 13. If C denotes the graded linear category associated to a graded ri ng R, then the graded
linear category with translation C∗ is equivalent as a category to the linear category with one ob ject ∗
obtained by forgetting the grading on R.
Example 11. The nilHecke algebra NH n is a graded algebra with deg( xi) = 2 and deg( ∂i) = −2.
Recall that the nilHecke ring NH n is isomorphic as a graded algebra to the matrix ring Mat((n)!
q2 ; Symn)
of n! ×n! matrices with coeﬃcients in the ring Sym n = /CI [x1,...,x n]Sn of symmetric functions in n
variables. Here we write ( n)!
q2 := (1 −q2n)/(1 −q2) for the non-symmetrized quantum integers and
each variable of Sym n has degree 2.
To compute the trace of NH n regarded as a graded category C, observe that Tr( C) = Tr(Sym) and
that Sym is positively graded and one dimensional in degree zero, in pa rticular it is graded local, so
that the graded trace of Tr( C) ∼= K0(NHn) ∼=
/CI . Compare this result with section 2.2.2 where we
showed Tr(NHn) ∼= Symn. Exercise 13 shows that by enlarging the graded category C to C∗, we again
have Tr(C∗) = Sym n.
