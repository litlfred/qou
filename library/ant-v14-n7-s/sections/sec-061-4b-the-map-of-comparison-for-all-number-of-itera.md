---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-061-4b-the-map-of-comparison-for-all-number-of-itera
section_title: "4B. The map of comparison for all number of iterations"
section_number: null
pages: 74-75
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
deﬁned the map of comparison, from integrals to series, comp6∫: K⟨⟨e0∪µN⟩⟩N
o(1)→ K⟨⟨e0∪µN⟩⟩har,o(1), by
(comp6∫((gξ)ξ∈µN(K)))[eξd+1end−1
0 eξd··· en1−1
0 eξ1]
=(−1)d ∑
ξ∈µN(K)
ξ−pα
gξ
[ 1
1− e0
eξd+1end−1
0 eξd··· en1−1
0 eξ1
]
.
In the context of this paper, it is natural to deﬁne a variant of the map of comparison from integral
to series, which takes into account the properties of the iterated Frobenius viewed as a function of its
number of iterations, and which has the additional advantage of being injective.
Deﬁnition 4B.1. Let the map comp6∫
iter : Ad˜51,0(K)o(1)(e1)→ (K⟨⟨e0∪µN⟩⟩
∫1,0
har)q N∗
be deﬁned by f ↦→
(τ(q˜α)( f)◦
∫1,0
har comp6∫ f)˜α∈N∗.
Equation (0-3) can be restated as
comp6∫
iter(Ad8q,−∞(e1))=(harq,˜α)α∈N∗.
The key property of comp6∫
iter , which a priori does not hold for comp6∫, is the following:
Proposition 4B.2. comp6∫
iter is injective.
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1741
Proof. Let a word w= eξd+1end−1
0 eξd··· en1−1
0 eξ1. For n> weight(w), let us consider the coefﬁcient
of(qa)n in comp6∫,iter( f)[w]. It is equal to f[en−(n1+···+nd)
0 eξd+1end−1
0 eξd··· en1−1
0 eξ1] + terms of lower
depth, where the depth is the one of coefﬁcients of f . This gives the result by an induction on the
depth. □
5. Iteration of the Frobenius on P1 \ ⋃
ξ B(ξ, 1)
In the previous sections, we considered the Frobenius of π un,crys
1 (P1\{ 0,µ N,∞}) at base-points(1, 0)
and the harmonic Frobenius. We now consider the Frobenius of π un,crys
1 (P1\{ 0,µ N,∞}) on the afﬁnoid
subspace U an= P1,an\⋃
ξ N=1 B(ξ, 1) of P1,an over K , where B(ξ, 1) is the open ball of center ξ and
of radius 1. As in Section 2, we will have a ﬁxed-point equation (Section 5A) and an iteration equation
(Section 5B). Additionally, we will have a third equation coming from the study of regularized iterated
integrals in [Jarossay 2019, Section 5.3].
