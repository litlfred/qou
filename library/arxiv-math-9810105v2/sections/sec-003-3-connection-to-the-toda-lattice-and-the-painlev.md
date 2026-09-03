---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-003-3-connection-to-the-toda-lattice-and-the-painlev
section_title: "Connection to the Toda Lattice and the Painlev´e III Equation"
section_number: 3
pages: 16-16
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
---
In this Section, we discuss the connection of the RHP (1.26) for κ2
k and the
RHP for the Toda lattice and the Painlev´e III equation. In the RH context, the
connection results from the speciﬁc form of the weight, e
√
λ(z+z−1). Connections can
also be seen from the Toeplitz determinant/orthogonal polynomial point of view as
in [PS], [Hi] and [Wi]. The purpose of this short Section is purely to establish the
various connection, but we do not use the results in the sequel.
Write q = k + 1 in (1.26). We deﬁne
mT L(z; q) =








0 −1
1
0

Y (z; q)

z−qe
√
λz−1
0
0
zqe−
√
λz−1

0
1
−1 0

|z| > 1,

0 −1
1
0

Y (z; q)

e
√
λz
0
0
e−
√
λz

|z| < 1.
(3.1)
A simple calculation shows that mT L solves the following RHP,









mT L(z)
is analytic in
C −Σ,
mT L
+ (z) = mT L
−(z)
 
0
−z−qe−
√
λ(z−z−1)
zqe
√
λ(z−z−1)
1
!
mT L(z) →I
as
z →∞.
(3.2)
Once again, the RHP for Y is equivalent to the RHP for mT L in the sense that a
solution of one problem yields a solution of the other problem.
Recall that the RHP related to the Toda Lattice problem, for −∞< m < ∞,
dam
dt
= 2(b2
m −b2
m−1)
dbm
dt
= bm(am+1 −am),
(3.3)
under initial data decaying at inﬁnity is the following (see,e.g.,[Ka]). Suppose that
there are no solitons and denote the reﬂection coeﬃcient by r(z), z ∈Σ. Then we
ﬁnd Q(z) such that









Q(z)
is analytic in C −Σ
Q+(z) = Q−(z)
 
1 −|r(z)|2
−¯r(z)z2me−t(z−z−1)
r(z)z−2met(z−z−1)
1
!
Q(z) →I
as z →∞.
(3.4)
When q is even, if we set
√
λ = t and q = −2m in (3.2), then the RHP is identical
with the above RHP with r(z) ≡1.
For the connection to the Painlev´e III equation, deﬁne
mP III(z) =
(
(−1)qmT L(z)
|z| < 1,
mT L(z)
|z| > 1.
(3.5)
Note in (3.2),
(−1)q
 
0
−z−qe−
√
λ(z−z−1)
zqe
√
λ(z−z−1)
1
!
=(−1)qe−
√
λ
