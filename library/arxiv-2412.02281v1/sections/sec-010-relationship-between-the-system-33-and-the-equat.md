---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-010-relationship-between-the-system-33-and-the-equat
section_title: "Relationship between the System (33) and the Equation (5)"
section_number: null
pages: 14-14
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
The computation of the connection matrix and q-Stokes matrix of (33) can be transformed into the connectio n
problem of the equation (5). In this subsection, we clarify t he relationship between the system (33) and the
equation (5).
From explicit expressions of fundamental solutions in Prop osition 3.6 and Proposition 3.7, one gets that:
• For 1 ≤i,k ≤n − 1, 1 ≤j ≤n, F (0)
q (z;Enn,A n−1)ij and F (∞)
q (z,λ ;Enn,A n−1)ik satisfy the equation
n∏
l=1
(z ·Dq −λ (n)
l )y(z) =
n−1∏
l=1
Ç
q−δliσq − 1
q − 1 −λ (n−1)
l
å
(z ·y(z)), (38)
whereδli is the Kronecker delta symbol. It follows that F (∞)
q (z,λ ;Enn,A n−1)in also satisﬁes (38), since
F (∞)
q (z,λ ;Enn,A n−1)in = F (0)
q (z;Enn,A n−1)ij
Uq(z,λ ;Enn,A n−1)nj
−
n−1∑
k=1
Uq(z,λ ;Enn,A n−1)kj
Uq(z,λ ;Enn,A n−1)nj
F (∞)
q (z,λ ;Enn,A n−1)ik,
which is a sum with pseudo-constant coeﬃcients. In fact, the function F (∞)
q (z,λ ;Enn,A n−1)inz−µ j
satisﬁes the equation (see νn in (34)):
(1 −q)z
n−1∏
l=1
(1 −q1+µ j −ν l−δliσq)y(z) = qν n (1 −σq)
n∏
l=1,l ⁄=j
Ä
1 −qµ j −µ lσq
ä
y(z),
which admits the unique convergent solution
ψ ij (z)zν n−µ j −1
(q−ν n (1−q)z;q)∞
, such that ψij(z) is a power series in the
variable 1/z , with the constant term 1. Then we have
F (∞)
q (z,λ ;Enn,A n−1)in = qa(n−1)
i ψij(z)zν n−1
(q−ν n(1 −q)z;q)∞
, (39)
by the direct computations involving recurrence relations of power series coeﬃcients of ψij(z) and
F (∞)
q (z,λ ;Enn,A n−1)in.
• For i = n, 1 ≤ k ≤ n − 1, 1 ≤ j ≤ n, F (0)
q (z;Enn,A n−1)nj and F (∞)
q (z,λ ;Enn,A n−1)nk satisfy the
equation
n∏
l=1
(z ·Dq −λ (n)
l )y(z) =
n−1∏
l=1
(z ·Dq −λ (n−1)
l )(z ·y(z)). (40)
It also follows that F (∞)
q (z,λ ;Enn,A n−1)nn satisﬁes (40) and
Fq(z,λ ;Enn,A n−1)nn = ψnj(z)zν n
(q−ν n (1 −q)z;q)∞
, (41)
given the power series ψnj(z) for the variable 1 /z , with the constant term 1, such that
ψ nj (z)zν n−µ j
(q−ν n (1−q)z;q)∞
satisﬁes the equation
(1 −q)z
n−1∏
l=1
(1 −q1+µ j −ν lσq)y(z) = qν n (1 −σq)
n∏
l=1,l ⁄=j
Ä
1 −qµ j −µ lσq
ä
y(z).
So the coeﬃcients of the connection formula of the equations (38), (40), which can be derived from Theorem
1.2 (or Theorem 2.26 equivalently), provide the entries of Uq(z,λ ;Enn,A n−1).
