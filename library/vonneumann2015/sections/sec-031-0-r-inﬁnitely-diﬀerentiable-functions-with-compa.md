---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-031-0-r-inﬁnitely-diﬀerentiable-functions-with-compa
section_title: "(R) (inﬁnitely diﬀerentiable functions with compact support), Sf = f ′. Show that S is preclosed."
section_number: 0
pages: 86-87
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
with compact support), Sf = f ′. Show that S is preclosed.
(ii) Deﬁne T from L2(R) to C by D(T) = L1(R) ∩L2(R), T(f) =
R
R f.
Show that T is not preclosed.
Deﬁnition 12.1.12. Suppose T is a closed operator. A core for T is a linear
subspace D0 ⊂D(T) such that T|D0 = T.
86
We can perform basic arithmetic operations with (unbounded) operators
as follows: S + T is the operator with domain D(S + T) = D(S) ∩D(T) and
(S + T)ξ = Sξ + Tξ. ST is the operator with domain D(ST) = {ξ ∈D(T) :
Tξ ∈D(S)} and (ST)ξ = S(Tξ). Of particular importance is the adjoint.
Deﬁnition 12.1.13. Let T be a densely deﬁned operator on H. Let
D(T ∗)
=
{η ∈H : ∃σ ∈H such that ⟨Tξ, η⟩= ⟨ξ, σ⟩∀ξ ∈D(T)}
=
{η ∈H : ∃C > 0 such that |⟨Tξ, η⟩| ≤C||ξ|| ∀ξ ∈D(T)}.
For ξ ∈D(T ∗) note that the element σ is unique (by the density of D(T))
and deﬁne T ∗ξ = η.
Remark 12.1.14. Note that if S ⊂T then T ∗⊂S∗.
Exercise 12.1.15. Give an example to show that the domain of the adjoint
need not be dense. [In fact it can be {0}].
Proposition 12.1.16. Let T be a densely deﬁned operator. Then
