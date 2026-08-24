---
doc_id: ant-v14-n7-s-p02
doc_title: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values"
section_id: sec-023-4-comparison-between-equations-on-integrals-and
section_title: "Comparison between equations on integrals and equations on series"
section_number: 4
pages: 29-31
source_pdf: ant-v14-n7-s-p02.pdf
source_sha256: fd2121feb180b282
doc_brief: "Pro-unipotent harmonic actions and dynamical properties of p-adic cyclotomic multiple zeta values — 33 sections: Introduction 1711; Preliminaries 1716; Iteration of the harmonic Frobeniu"
---
We prove (0-6) and we discuss more generally the comparison between integrals and series.
4A. Uniqueness of the expansion of harq ˜α as a function of ˜α and q ˜α.
Proposition 4A.1. Let δ∈ N∗, and a map S: N∗∩[δ,+∞[→ K such that we have , for all a∈
N∗∩[δ,+∞[, S(a)=∑
n∈N
∑M
m=0 cn,m(qa)nam, where M∈ N∗, and(cl,m)0⩽n, 0⩽m⩽M∈ K N×{0,...,M}
such that∑
n∈N
∑M
m=0|cn,mqn|p<∞. If S(a)= 0 for all a∈ N∗∩[δ,+∞[, then we have cn,m= 0 for
all(n, m)∈ N×{ 0,..., M}.
Proof. Let a0∈ N∗∩[δ,+∞[ and u∈ N. By taking a=a0+pu in the equation∑
n∈N
∑M
m=0cn,m(qa)nam=0
and by taking the limit u→∞ , we get∑M
m=0 c0,mam
0= 0. Since this is true for inﬁnitely many a0, we
get c0,m= 0 for all m. This implies that, for all a,
∑
n>1
M∑
m=0
cn,m(qa)nam= qa
(∑
n>1
M∑
m=0
cn,m(qa)n−1am
)
= 0,
thus
∑
n∈N
M∑
m=0
cn+1,m(qa)nam= 0.
Whence the result: by induction on n, we have a contradiction if there exists(n, m) such that cn,m⁄= 0. □
Let us now prove (0 -6). By [Jarossay 2019], we have 8q,˜α∈ K⟨⟨e0∪µN⟩⟩o(1) for any ˜α∈ N∗. By
Corollary 2B.2, this implies that|8|q=∑
w word on e0∪µN
sup˜α∈Z∪{±∞}\{0}|8q,˜α[w]|pw is a well-deﬁned
element of K⟨⟨e0∪µN⟩⟩o(1). We have a similar bound for the coefﬁcients of the expansion of each harq,˜α[w]
obtained in Section 3C. Thus we can apply Proposition 4A.1 to the power series expansion of each
harq,˜α[w] in (0-3), (0-4), (0-5) to deduce that they are the same.
Example 4A.2. The term of depth one ( d= 1), in the case of P1\{ 0, 1,∞} (i.e., in the case N= 1) for
which p= q,˜α=α and˜α0=α0, of the equations of the theorem is the following, respectively (with
BL+b
b = 1/(L+ b+ 1)
(L+b+1
L
)
BL+1 for 1⩽ b⩽ L+ 1):
1740 David Jarossay
• The ﬁxed point equation of the harmonic Frobenius of integrals at (1, 0) (equation (0-3)):
harpα(n)=
∞∑
b=1
(pα)b+n Ad8p,−∞(e1)[eb
0e1en−1
0 e1]+ Ad8p,∞(e1)
[ 1
1− e0
e1en−1
0 e1
]
. (4-1)
• The relation of iteration of the harmonic Frobenius of integrals at (1, 0) (equation (0-4)):
harpα(n)=
∞∑
b=1
(pα)n(pα0)b
pα0− 1 Ad8p,α0(e1)[eb
0e1en−1
0 e1]− (pα)n
pα0− 1 Ad8p,α0(e1)
[ 1
1− e0
e1en−1
0 e1
]
. (4-2)
• The relation of iteration of the harmonic Frobenius of series (0-5):
harpα(n)=
∞∑
b=1
pα(n+b)− 1
pα0(n+b)− 1
∞∑
L=−1
BL+b
b harpα0(n+ b+ L). (4-3)
• The comparison between these three expressions: (0-6)
(pα0)b
pα0− 1 Ad8p,α0(e1)[eb
0e1en−1
0 e1]= Ad8p,∞(e1)[eb
0e1en−1
0 e1]
= 1
pα0(n+b)− 1
∞∑
L=−1
BL+b
b harpα0(n+ b+ L). (4-4)
Generalizing this example to higher depths gives a new way to compute p-adic cyclotomic multiple
zeta values.
4B. The map of comparison for all number of iterations. In [Jarossay 2015, Deﬁnition 5.1.3] we have
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
