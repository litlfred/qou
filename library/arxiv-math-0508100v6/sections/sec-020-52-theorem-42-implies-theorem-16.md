---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-020-52-theorem-42-implies-theorem-16
section_title: "Theorem 4.2 implies Theorem 1.6"
section_number: 5.2
pages: 13-14
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
toc_source: outline
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent polynomials, whose nth term is the nth colored Jones polynomial."
---
(20)
f [N]
K,n(z) := JK,n(ez/n) −
N−1
X
k=0
PK,k(ez)
∆K(ez)2k+1
 z
n
k
.
Theorem 1.6 follows from Theorem 1.5, Lemma 2.1 and the following uniform bound.
Theorem 5.3. For every knot K there exists an open neighborhood ˜UK of 0 ∈C such that for every N ≥0
there exists a positive number MN such that for α ∈˜UK, and all n ≥0, we have:

n
α
N
f (N)
K,n(α)

 < MN.
Proof. (of Theorem 5.3, assuming Theorem 4.2) We have the following identities, where the second follows
from (14) and (15):
f [N]
K,n(α) = fK,n(α) −
N−1
X
p=0
RK,p(α)
α
n
p
=
∞
X
k=0
hK,k(α, α
n) −
N−1
X
p=0
 ∞
X
k=0
dk,p(α)
! α
n
p
=
∞
X
k=0
"
hK,k(α, α
n) −
N−1
X
p=0
dk,p(α)
α
n
p
#
Using the estimate in Corollary 5.2, we see that
14
STAVROS GAROUFALIDIS AND THANG TQ LˆE

n
α
N
f [N]
K,n(α)

 < 1
N!
∞
X
k=0
|αA4|k−N (A5k2)N.
If |αA4| < 1, the series of the right hand side is absolutely convergent. It is enough to take ˜UK to be the
disk centered at 0 with radius 1/(2A4 + 1). This proves Theorem 5.3, assuming Theorem 4.2.
□
