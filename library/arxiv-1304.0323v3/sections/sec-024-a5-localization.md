---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-024-a5-localization
section_title: "A.5. Localization"
section_number: null
pages: 71-72
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
has a structure of a tensor category by F⊗G = F·G, the composition of functors.
Let{Φi}i∈I be a commuting family of objects of Fct( C,C). Then we can deﬁne Φ α∈
Fct(C,C) for α∈ Z⊕I
≥0 and Φ α· Φβ ∼−→Φα+β as in the preceding subsection.
72 S.-J. KANG, M. KASHIW ARA, M. KIM
We deﬁne the category ~C as follows. The objects of ~C are pairs (X,α ) of X∈C and
α∈ Z⊕I . The homomorphisms are deﬁned by
Hom ~C
(
(X,α ), (Y,β )
)
= lim−→
γ∈Z⊕I
≥0,
γ+α,γ +β∈Z⊕I
≥0
HomC(Φγ+α(X), Φγ+β(Y )).
Note that we have a well-deﬁned inductive system in the above deﬁnit ion, since
{Φi}i∈I is a commuting family.
The composition of morphisms in ~C is deﬁned in an evident way.
We deﬁne a functor Υ : C→ ~C by X↦→(X, 0). For α∈ Z⊕I, we deﬁne a functor
~Φα : ~C→ ~C by
(X,β )↦→(X,β +α).
Then all the functors ~Φα are auto-equivalences. Moreover, the diagram
C
Φ α
/d47/d47
/d15/d15
C
/d15/d15
~C
~Φ α
/d47/d47 ~C
is quasi-commutative for any α∈ Z⊕I
≥0. We call ~C the localization ofC by the commuting
family{Φi}i∈I and denote it by C[Φ−1
i |i∈I].
The following lemma can be easily veriﬁed.
Lemma A.5.1. Assume thatC is an abelian category and the Φi’s are exact functors.
Then
(i)C[Φ−1
i |i∈I] is an abelian category and the functor Υ : C→C [Φ−1
i |i∈I] is an
exact functor.
(ii) ForX∈C , Υ(X)≃ 0 if and only if there exists α∈ Z⊕I
≥0 such that Φα(X)≃ 0.
