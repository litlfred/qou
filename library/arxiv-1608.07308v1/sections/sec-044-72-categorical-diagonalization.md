---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-044-72-categorical-diagonalization
section_title: "Categorical diagonalization"
section_number: 7.2
pages: 53-53
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
egorical diagonalization, which we will now recall. Assume we are given an equivariant
monoidal categoryT ↷C, which can be taken to be triangulated or dg.
Deﬁnition 7.6. ([23]) Fix an objectF∈Kb(C). An arrow:
(7.1) λ· 1
α
−→F
is called an eigenmap ofF , and the grading shiftλ∈T∨ is called an eigenvalue ofF .
Deﬁnition 7.7. ([23]) An object F ∈ Kb(C) is called diagonalizable if it has a collection of
eigenvaluesλ0,...,λ n∈T∨ and eigenmaps:
{
λi· 1
αi
→F
}
i∈{0,...,n}
such that⊗n
i=0Cone(αi)≃ 0.
The intuition behind the above terminology comes about by considering the Grothendieck
group [C], which is an algebra because the categoryC is monoidal. Multiplication by the class
of the object [F ] induces an operator on [C], and the datum of Deﬁnition 7.7 amounts to:
(7.2)
n∏
i=0
([F ]−λi) = 0
In other words, the condition that the product of the cones of the eigenmaps is 0 amounts to
requiring the operator∗↝∗· [F ] to solve its characteristic polynomial. In Lemma 7.8, we
establish the fact that categorical diagonalization is universally represented by the category:
D =Db(CohT (Pn
A))
whereA is any commutative ring andT ↷ Pn
A acts via:
(7.3) t· [z0 :... :zn]↦→
[ z0
λ0(t) :... : zn
λn(t)
]
whereλ0,...,λ n∈T∨. An immediate generalization of Example 4.13 yields the following:
Lemma 7.8. The datum of a diagonalizable object F∈C as in Deﬁnition 7.7 is equivalent to
the existence of aT –equivariant map:
ι :C→ Pn
A
such thatF =ι∗ (O(1)), whereA = EndC(1).
