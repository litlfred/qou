---
doc_id: arxiv-1701.06567v2
doc_title: "BPS spectra and 3-manifold invariants"
section_id: sec-016-3-examples
section_title: "Examples"
section_number: 3
pages: 27-29
source_pdf: 1701.06567v2.pdf
source_sha256: c1610b50f5a7e22c
doc_brief: "BPS spectra and 3-manifold invariants — We provide a physical deﬁnition of new homological invariants Ha(M3) of 3- manifolds (possibly, with knots) labeled by abelian ﬂat connections."
---
In this section, we present many examples, illustrating the general proposal outlined in the
previous section. In particular, our goal is two-fold: ﬁrst, we wish to use the proposed physics
deﬁnition of the new homological invariants Ha[M3] to compute them in many concrete ex-
amples, to the extent that one can start exploring the structure of the results and explicitly
test the Conjectures 2.1 and 2.2, which is our second goal. We start with the simplest three-
manifold and gradually move to the study of more complex ones.
3.1 M3 =S3
For M3 = S3 and G = U(N), the 3d N = 2 theory T [S3] is a 3d N = 2 Chern-Simons
theory with gauge group U(N) at level 1 and an adjoint chiral multiplet φ, whose R-charge
is equal to 2 [54]. This theory is dual (the duality is usually referred to as the “duality
appetizer” [31, 62, 63]) to a system of N free chirals, making it simple to analyze. The R-
charges of the free chirals are given by R = 2, 4,..., 2N, and they have charges 1 , 2,...,N
under the U(1)β ﬂavor symmetry that rotates the original adjoint chiral φ by a phase.
As a result, the superconformal index of the theory T [S3] can be expressed a simple
product,
IU(N)(q,t ) =
N∏
i=1
(t−iq1−i;q)∞
(tiqi;q)∞
, (3.1)
where, as usual, the q-Pochhammer symbol is deﬁned as
(z;q)n =
n−1∏
j=0
(1−zqj). (3.2)
– 26 –
Since H1(S3) = 0, there is only one homological block ˆZ0(q,t ), realized as the S1×D2
partition function of the N free chirals with Neumann boundary conditions,
ˆZ0(q,t ) =
N∏
i=1
1
(tiqi;q)∞
. (3.3)
In the terminology of [27] this is an unreduced homological block.26 In order to relate it to the
WRT invariant of S3 as in Conjecture 2.1, before taking the unreﬁned limit t→ 1, one has
to divide by the contribution of the Cartan components of the adjoint chiral φ. The result
looks like
ˆZ0(q) = (tq;q)N
∞ˆZ0(q,t )
⏐⏐⏐
t→1
=
N−1∏
j=1
(1−qj)N−j. (3.4)
In the case of G = SU (2), the dual theory consists of just one free chiral multiplet with
R-charge 4 and U(1)β charge 2, whose index is
ISU (2)(q,t ) = (t−2q−1;q)∞
(t2q2;q)∞
. (3.5)
and we have
ˆZ0(q,t ) = 1
(t2q2;q)∞
, ˆZ0(q) = (1−q2). (3.6)
Using the standard prescription for extending the quantum dilogarithm outside |q|< 1,27
(x;q−1)∞∝ 1
(xq;q)∞
, (3.7)
we have, for G =U(N),28
ˆZ0(1/q, 1/t) =
N∏
i=1
1
(t−iq−i; 1/q)∞
= 1
N!
N∏
i=1
(t−iq1−i;q)∞. (3.9)
We see that the superconformal index ( 3.1) indeed admits a factorization ` a la(2.37),
I(q,t ) =|W0|ˆZ0(q,t )ˆZ0(q−1,t−1), (3.10)
with only one homological block in this case.
26Although the terminology “reduced” and “unreduced” here is very similar to the one used in knot homology,
there is no direct connection.
27Note that this is not an ordinary analytic continuation. The latter actually does not exists because |q| = 1
is a natural boundary.
28Note that there is an ambiguous overall constant in (3.7). We ﬁx it in (3.9) by requiring that the unreﬁned
quantities are related by the ordinary analytic continuation. Namely,
ˆZ0(1/q, 1/t)· (t−1q−1;q−1)N
∞
⏐⏐⏐
t→1
= ˆZ0(1/q, 1/t)· (1/t;q)−N
∞
⏐⏐⏐
t→1
= ˆZ0(1/q) =
N−1∏
j=1
(1−q−j)N−j. (3.8)
– 27 –
