---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-060-4-comparison-between-equations-on-integrals-and
section_title: "Comparison between equations on integrals and equations on series"
section_number: 4
pages: 73-74
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
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
