---
doc_id: arxiv-2412.02281v1
doc_title: "u + A"
section_id: sec-012-explicit-evaluation-of-connection-matrix-and-q-s
section_title: "Explicit Evaluation of Connection Matrix and q-Stokes Matrix of (2)"
section_number: null
pages: 17-18
source_pdf: 2412.02281v1.pdf
source_sha256: ac4127cf4994b2ba
doc_brief: "Explicit evaluation of the q-Stokes matrices for certain confluent hypergeometric q-difference equations — We prove a connection formula for the basic hypergeomtric fu nction nϕn−1 (a1,...,a n−1"
---
Since the matrices Enn and diag (Pn−1, 1) commute with each other, we get
Proposition 3.11. Under the condition (3) (with the condition (30) included), the nonresonant condition
(4), and condition (31), for λ ∈ C∗\ ∪1≤l≤n−1 [−(1 −q)/q ν l ;q], we have
F (∞)
q (z,λ ;Enn,A ) = diag (Pn−1, 1)Fq (z,λ ;Enn,A n−1) diag
Ä
P −1
n−1, 1
ä
,
F (0)
q (z;Enn,A ) = diag (Pn−1, 1)F (0)
q (z;Enn,A n−1).
Moreover, the connection matrix and q-Stokes matrices of the systems (2) and (33) are related by
Sq (z,λ,µ ;Enn,A ) = diag (Pn−1, 1)Sq (z,λ,µ ;En,A n−1) diag
Ä
P −1
n−1, 1
ä
,
Uq (z,λ ;Enn,A ) = diag (Pn−1, 1)Uq (z,λ ;Enn,A n−1).
Following Proposition 3.11, the explicit expression of the q-Stokes matrix of (2) is given below and the
connection matrix of (2) can be determined in a similar manne r.
Theorem 3.12. Under the condition (42), and for z,λ,µ such that
λ,µ ∈ C∗, λ,µ / ∈ − 1 −q
qν l
qZ, for 1 ≤l ≤n − 1, µ /∈λq Z, and z ∈ C∗, z /∈ − 1
µqZ, z /∈ − 1
λqZ,
17
the q-Stokes matrix Sq (z,λ,µ ;Enn,A ) of the system (2) takes the block matrix form
Sq (z,λ,µ ;Enn,A ) =
Å Idn−1 0
bq 1
ã
,
wherebq =
(
(bq)1,..., (bq)n−1
)
with
(bq)k =
n−1∑
j=1
(− 1)n+k∆ 1,...,n −2,n
1,...,n −1
Ä
A − λ (n−1)
j · Idn
ä
∆ 1,..., ˆk,...,n −1
1,...,n −2
Ä
A − λ (n−1)
j · Idn
ä
∏ n−1
l=1,l ⁄=j
Ä
λ (n−1)
l − λ (n−1)
j
ä ∏ n−2
l=1
Ä
λ (n−2)
l − λ (n−1)
j
ä
n∑
s=1
∏ n−1
l=1 (q1+µ s −ν l ;q)∞∏ n
l=1,l ⁄=s(q1+µ s−µ l ;q)∞
∏ n
l=1,l ⁄=sθq((1 −q)q1−µ l/λ )
∏ n−1
l=1 θq((1 −q)q1−ν l/λ )
θq
( qµ s−ν nλz)
θq(λz )
×
∏ n
l=1,l ⁄=s(q1+µ l−ν j ;q)∞
∏ n−1
l=1,l ⁄=j(qν l−µ s ;q)∞
∏ n−1
l=1,l ⁄=j(q1+ν l−ν j ;q)∞
∏ n
l=1,l ⁄=s(qµ l −µ s ;q)∞
θq
(
qν j −µ s −1µz
)
θq (µz )
θq (µqµ s/ (1 −q))
θq (µqν j −1/ (1 −q))
zν j
zν n+1.
Proof. The expression of diag ( Pn−1, 1)Sq (z,λ,µ ;En,A n−1) diag( P −1
n−1, 1) tells us that
(bq)k = −
n−1∑
j=1
b(n−1)
j
Ä
P −1
n−1
ä
jk
n∑
s=1
∏ n−1
l=1 (q1+µ s −ν l ;q)∞∏ n
l=1,l ⁄=s(q1+µ s−µ l ;q)∞
∏ n
l=1,l ⁄=sθq((1 −q)q1−µ l/λ )
∏ n−1
l=1 θq((1 −q)q1−ν l/λ )
θq
(
qµ s−ν nλz
)
θq(λz )
×
∏ n
l=1,l ⁄=s(q1+µ l−ν j ;q)∞
∏ n−1
l=1,l ⁄=j (qν l−µ s ;q)∞
∏ n−1
l=1,l ⁄=j(q1+ν l−ν j ;q)∞
∏ n
l=1,l ⁄=s(qµ l−µ s ;q)∞
θq
( qν j −µ s−1µz)
θq (µz )
θq (µqµ s/ (1 −q))
θq (µqν j −1/ (1 −q))
zν j
zν n+1. (50)
Using Proposition 3.4, the identity (50) can be rewritten as the form in this theorem.
Like Remark 2.28, we have
Remark 3.13. We can use the connection formula of nϕn(a1,...,a n;b1,...,b n;z) to derive the q-Stokes matrix
of the system
DqFq(z) =
Å
Ennσq + A
z
ã
Fq(z).
