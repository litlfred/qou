---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-026-85-proof-of-theorem-113
section_title: "Proof of Theorem 1.13"
section_number: 8.5
pages: 22-23
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
Each summand F (n, k) is the product of R-matrices (which are weights of crossing points) and weights of
extreme points (which have absolute value 1). There are c + 2 crossing points, but the weights of the two
boundary crossing have absolute value 1. Hence
|JK,n (e2πi/n )| ≤ nc
(
max
a,b,k
|evn(R±(n; a, b, k))|
) c
.
From the growth rate of max a,b,k |evn(R±(n; a, b, k))| given by Corollary 8.10 we get the theorem.
9. The generalized volume conjecture near α = 2πi
In this section we will prove Theorems 1.10 and 1.11 which are concerned with the Generalized Volume
Conjecture near 2πi. Our proofs use crucially the well-known symmetry principle, see [ KM91, Le00]: Suppose
m, m′ and n are positive integers with m ≡ ±m′ mod n, then
(44) JK,m (e2πi/n ) = JK,m ′(e2πi/n ).
Note that this fact is also a consequence of the existence of the cy clotomic expansion. However, the case of
higher rank Lie algebra requires results from canonical basis theor y, see [ Le00].
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 23
Proof. (of Theorem 1.10) The symmetry principle implies that for all n > m > 0, we have:
JK,n ±m(e2πi/n ) = JK,m (e2πi/n )
which implies that
lim
n→∞
JK,n ±m(e2πi/n ) = lim
n→∞
JK,m (e2πi/n ) = JK,m (1) = 1 ,
from which Theorem 1.10 follows easily. □
Proof. (of Theorem 1.11) Fix a knot K and consider the neighborhood UK of 0 as in Theorem 1.3. Deﬁne
VK = 1 + UK.
Let us suppose that α/(2πi) ∈ VK is a rational number not equal to 1. Assume that α = 2 πip/m with
p, m unequal coprime positive integers. Let N = np. Then, the symmetry principle implies that
fK,N (α) = JK,N (eα/N )
= JK,np (e2πi/ (nm))
= JK,n |p−m|(e2πi/ (nm)).
Since n|p − m|/(nm) = |p/m − 1| ∈ UK, Theorem 1.3 implies that
lim
n→∞
JK,n |p−m|(e2πi/ (nm)) = 1
∆( e2πi (|p/m −1|) .
In other words,
lim
n→∞
fK,np (α) = 1
∆( e2πi (|p/m −1|)
is bounded. The result follows. □
