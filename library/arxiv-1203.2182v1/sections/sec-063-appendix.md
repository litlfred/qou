---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-063-appendix
section_title: "Appendix"
section_number: null
pages: 68-69
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
A. Miscellaneous results on knot invariants
A1 Macdonald polynomials
Let pn be the power sum symmetric function in x = (x1,x 2,... ):
pn :=
∞∑
i=1
xn
i. (A1)
For any symmetric functions f and g, a scalar product is introduced as:
⟨f(p),g (p)⟩q1,q2 :=f(p∗)g(p)|constant part , p ∗
n :=n1 −qn
1
1 −qn
2
∂
∂pn
. (A2)
with p = (p1,p 2,... ) and p∗ = (p∗
1,p ∗
2,... ). The Macdonald function PR(x;q1,q 2) is uniquely
speciﬁed by the following orthogonality condition and norm alization:
⟨PR(x;q1,q 2),P Q(x;q1,q 2)⟩q1,q2 = 0, (R ⁄=Q) (A3)
PR(x;q1,q 2) =
∑
Q≤R
uRQ(q1,q 2)mR(x), u RR(q1,q 2) = 1 (A4)
where mR(x) is the monomial symmetric function:
mR(x) :=
∑
σ
x
Rσ(1)
1 x
Rσ(2)
2 · · ·, (A5)
and uRQ(q1,q 2) ∈ Q(q1,q 2). The dominance partial ordering R > Qdenotes the condition:
|R| = |Q| and R1 + · · · +Ri ≥Q1 + · · · +Qi for all i. The scalar product of the Macdonald
functions is given by
⟨PR(x;q1,q 2),P Q(x;q1,q 2)⟩q1,q2 =
∏
i,j
1 −qRi−j+1
1 q
Rt
j−i
2
1 −qRi−j
1 q
Rt
j−i+1
2
. (A6)
Explicit form of the Macdonald function PR(x;q1,q 2)
Using the deﬁnitions above, the Macdonald functions are det ermined explicitly. Up to r ≤ 3,
the Macdonald functions PSr+ℓ,r−ℓ(x;q1,q 2) and PΛ r+ℓ,r−ℓ(x;q1,q 2) are
PS1(x,q 1,q 2) = p1,
PS2(x,q 1,q 2) = (1 +q1)(1 −q2)
1 −q1q2
p2
1
2 + (1 −q1)(1 +q2)
1 −q1q2
p2
2 , P S1,1(x,q 1,q 2) = p2
1
2 − p2
2,
PS3(x;q1,q 2) = (1 +q1)(1 −q3
1)(1 −q2)2
(1 −q1)(1 −q1q2)(1 −q2
1q2)
p3
1
6 + (1 −q3
1)(1 −q2
2)
(1 −q1q2)(1 −q2
1q2)
p1p2
2
+ (1 −q1)(1 −q2
1)(1 −q3
2)
(1 −q2)(1 −q1q2)(1 −q2
1q2)
p3
3,
PS2,1(x;q1,q 2) = (1 −q2)(2 +q1 +q2 + 2q1q2)
1 −q1q2
2
p3
1
6 + (q2 −q1)(1 +q2)
1 −q1q2
2
p1p2
2
− (1 −q1)(1 −q3
2)
(1 −q2)(1 −q1q2
2)
p3
3,
– 67 –
PΛ 1(x,q 1,q 2) = p1,
PΛ 2(x,q 1,q 2) = PS1,1(x,q 1,q 2), P Λ 1,1(x,q 1,q 2) =PS2(x,q 1,q 2),
PΛ 3(x;q1,q 2) = p3
1
6 − p1p2
2 + p3
3,
PΛ 2,1(x;q1,q 2) = PS2,1(x;q1,q 2) (A7)
Using SF,16 we can generate the explicit expression of the Macdonald pol ynomials for more
examples.
Specialization MR(q̺
2;q1,q 2)
Specializingx =q̺
