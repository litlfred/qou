---
doc_id: arxiv-math-ph-0012035v3
doc_title: "Non-Abelian Stokes theorem in action Bogus/suppress law Broda1 Department of Theoretical Physics University of /suppress L´ od´ z Pomorska 149/153 PL 90–236 /suppress L´ od´ z Pola"
section_id: sec-008-212-ordering
section_title: "Ordering"
section_number: 2.1.2
pages: 10-11
source_pdf: 0012035v3.pdf
source_sha256: 06a4c8096c8ebb10
doc_brief: "Non-Abelian Stokes theorem in action Bogus/suppress law Broda1 Department of Theoretical Physics University of /suppress Lódź Pomorska 149/153 PL 90–236 /suppress Lódź Poland — In this short review"
---
There are a lot of diﬀerent ordering operators in our formulas which have been
collected in this section.
Dyson series We know from quantum theory that the path-ordered exponent
of an operator ˆA can be expressed by the power series called the Dyson series,
P exp
[
i
∫ t′′
t′
ˆA(t) dt
]
10
= P
[
1 +
∞∑
n=1
in
n!
∫ t′′
t′
dt1
∫ t′′
t′
dt2 . . .
∫ t′′
t′
dtn ˆA(t1) ˆA(t2) . . . ˆA(tn)
]
= 1 +
∞∑
n=1
in
n!
∫ t′′
t′
dt1
∫ t′′
t′
dt2 . . .
∫ t′′
t′
dtn P
[
ˆA(t1) ˆA(t2) . . . ˆA(tn)
]
= 1 +
∞∑
n=1
in
∫ t′′
t′
dt1
∫ t1
t′
dt2 . . .
∫ tn−1
t′
dtn ˆA(t1) ˆA(t2) . . . ˆA(tn),
where
P
[
ˆA1(t1) . . . ˆAn(tn)
] def
= ˆAσ(1)
(
tσ(1)
)
. . . ˆAσ(n)
(
tσ(n)
)
), t σ(1) ≥ . . . ≥ tσ(n).
For example, for two operators
P
[
ˆA1(t1) ˆA2(t2)
]
≡ θ (t1 − t2) ˆA1(t1) ˆA2(t2) + θ (t2 − t1) ˆA2(t2) ˆA1(t1),
where θ is the step function.
Conventions Since the operators/matrices appearing in our considerations
are, in general, non-commutative, we assume the following convent ions:
N∏
n=1
Xn
def
= XN XN −1 . . . X2X1, (12)
Pt (X1X2 . . . XN −1XN)
def
= XN XN −1 . . . X2X1, (13)
whereas for two parameters
Ps,t
N∏
m,n=1
Xm,n
def
=
N∏
n=1
N∏
m=1
Xm,n
≡ XN,N XN −1,N . . . X1,N XN,N −1 . . . X1,2XN,1 . . . X2,1X1,1.
