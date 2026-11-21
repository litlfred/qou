---
doc_id: arxiv-2412.02281v1
doc_title: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations"
section_id: sec-010-relationship-between-the-system-33-and-the-equat
section_title: "Relationship between the System (33) and the Equation (5)"
section_number: null
pages: 14-14
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
toc_source: outline
doc_brief: "Explicit evaluation of the q -Stokes matrices for certain conﬂuent hypergeometric q -diﬀerence equations — We prove a connection formula for the basic hypergeomtric function nϕn−1 (a1, ..., an−1, 0"
---
Relationship between the System (33) and the Equation (5)
The computation of the connection matrix and q-Stokes matrix of (33) can be transformed into the connection
problem of the equation (5). In this subsection, we clarify the relationship between the system (33) and the
equation (5).
From explicit expressions of fundamental solutions in Proposition 3.6 and Proposition 3.7, one gets that:
• For 1 ≤i, k ≤n −1, 1 ≤j ≤n, F (0)
q
(z; Enn, An−1)ij and F (∞)
q
(z, λ; Enn, An−1)ik satisfy the equation
n
Y
l=1
(z · Dq −λ(n)
l
)y(z) =
n−1
Y
l=1
Ç
q−δliσq −1
q −1
−λ(n−1)
l
å
(z · y(z)),
(38)
where δli is the Kronecker delta symbol. It follows that F (∞)
q
(z, λ; Enn, An−1)in also satisﬁes (38), since
F (∞)
q
(z, λ; Enn, An−1)in = F (0)
q
(z; Enn, An−1)ij
Uq(z, λ; Enn, An−1)nj −
n−1
X
k=1
Uq(z, λ; Enn, An−1)kj
Uq(z, λ; Enn, An−1)nj F (∞)
q
(z, λ; Enn, An−1)ik,
which is a sum with pseudo-constant coeﬃcients.
In fact, the function F (∞)
q
(z, λ; Enn, An−1)inz−µj
satisﬁes the equation (see νn in (34)):
(1 −q)z
n−1
Y
l=1
(1 −q1+µj −νl−δliσq)y(z) = qνn(1 −σq)
n
Y
l=1,l̸=j
Ä
1 −qµj −µlσq
ä
y(z),
which admits the unique convergent solution
ψij(z)zνn−µj −1
(q−νn (1−q)z;q)∞
, such that ψij(z) is a power series in the
variable 1/z, with the constant term 1. Then we have
F (∞)
q
(z, λ; Enn, An−1)in = qa(n−1)
i
ψij(z)zνn−1
(q−νn(1 −q)z; q)∞
,
(39)
by the direct computations involving recurrence relations of power series coeﬃcients of ψij(z) and
F (∞)
q
(z, λ; Enn, An−1)in.
• For i = n, 1 ≤k ≤n −1, 1 ≤j ≤n, F (0)
q
(z; Enn, An−1)nj and F (∞)
q
(z, λ; Enn, An−1)nk satisfy the
equation
n
Y
l=1
(z · Dq −λ(n)
l
)y(z) =
n−1
Y
l=1
(z · Dq −λ(n−1)
l
)(z · y(z)).
(40)
It also follows that F (∞)
q
(z, λ; Enn, An−1)nn satisﬁes (40) and
Fq(z, λ; Enn, An−1)nn =
ψnj(z)zνn
(q−νn(1 −q)z; q)∞
,
(41)
given the power series ψnj(z) for the variable 1/z, with the constant term 1, such that
ψnj(z)zνn−µj
(q−νn (1−q)z;q)∞
satisﬁes the equation
(1 −q)z
n−1
Y
l=1
(1 −q1+µj−νlσq)y(z) = qνn(1 −σq)
n
Y
l=1,l̸=j
Ä
1 −qµj−µlσq
ä
y(z).
So the coeﬃcients of the connection formula of the equations (38), (40), which can be derived from Theorem
1.2 (or Theorem 2.26 equivalently), provide the entries of Uq(z, λ; Enn, An−1).
