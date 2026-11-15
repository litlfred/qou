---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-009-52-flows-on-gk-and-monomials-of-gbkm1mr
section_title: "Flows on GK and monomials of GB'K(m1,…mr)"
section_number: 5.2
pages: 8-9
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
toc_source: outline
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent polynomials that encodes the Jones polynomial of a knot and its parallels."
---
K(m1, . . . mr). We interpret each entry γij with no z indeter-
minate as arc (ij) of the arc-graph GK. Then each monomial in GB′
K(m1, . . . , mr) corresponds to a ﬂow
on GK with indeg(i) = outdeg(i) = mi, i = 1, . . . , r. If f is such a ﬂow, we denote by G(f) the sum of all
monomials of P GB′
K(m1, . . . , mr) corresponding to f. Summarizing we can write
Observation 1.
∞
X
m1,...,mr=0
GB′
K(m1, . . . , mr) =
X
f
G(f).
We denote by C(f) the canonical monomial of a product (in arbitrary order) of the entries of B′
K corre-
sponding to the edges of GK, where the entry corresponding to each edge e appears f(e) times.
Observation 2. Let C be a summand of Qr
i=1(P
j γijxj)mi, which contains mi indeterminates xi, i =
1, . . . , r and contributes to G(f). For 1 ≤v ≤r and 1 ≤j ≤f(er
v) let c(C, v, j) be the number of γebv’s which
need to be commuted through the j-th occurrence of γerv in order to get C(f) from C. Then
C = xm1
1 xm2
2
. . . xmr
r q−rot(f)C(f)qexc(f)
r
Y
v=1
f(er
v)
Y
j=1
qsign(v)c(C,v,j).
8
Proof. Let Xij = γijxj. Hence C is a summand of the coeﬃcient of xm1
1 xm2
2
. . . xmr
r
in Qr
i=1(P
j Xij)mi.
For each j ﬁxed the γij’s appear ordered in C. In each canonical monomial, the γij’s appear ordered by
the second coordinate, and then by the ﬁrst coordinate. Hence, in order to get a canonical monomial times
xm1
1 xm2
2
. . . xmr
r
from a summand of Qr
i=1(P
j Xij)mi, we only need to commute Xij’s so that they are ordered
by the second coordinate. This means: if ai appears in S before (after respectively) the block S(i) then ai
appears in C before (after respectively )the block S(i) BUT ai−1 appears in R after (before respectively) the
block T (i). Hence we need to commute
1. Each Xi−1,i through each Xj−1,j, j ∈S(i) and each Xk−1,i through each Xj−1,j, j, k ∈S(i), R(k) >
R(j). The commutation in B′
K is such that we acquire each time qsign(j−1). Hence we acquire in
total qexc(f) since we recall that exc(f) = P
v sign(v)f(eb
v) P
e<er
v f(e).
2. Each Xk−1,i through each Xk−1,k, k ∈S(i). The commutation in B′
K is such that we acquire in total
qsign(k−1)(c(C,k−1,1)+...c(C,k−1,f(er
k−1)).
3. The commutation in B′
K is such that if i < i′, j < j′ and Xi,j′, Xi′,j do not appear in one of the
previous two cases then Xi,j′, Xi′,j = Xi′,j, Xi,j′.
This ﬁnishes the proof.
□
Corollary 5.3.
G(f) = C(f)qδ(f)
r
Y
v=1
X
f(ebv)≥c1≥···≥cf(erv)≥0
qsign(v)(c1+...cf(erv)).
Since
X
f(ebv)≥c1≥···≥cf(erv)≥0
qsign(v)(c1+...cf(erv)) =
 f(v)
f(ebv)

qsign(v)
,
we have
Corollary 5.4.
G(f) = qδ(f)multq(f)C(f).
Proof. (of Theorem 2) Theorem 7 tells us that
Jn(K, q) = qδ(K,n)
X
f∈F(GK)
multt(f)tδ(f) Y
v∈VK
t−sign(v)nf(eb
v)
Y
ered;t(e)=v
f(e)−1
Y
j=0
(1−t−sign(s(e))(n−(P
e′<ve f(e))−j)).
Comparing this with the deﬁnition 1.2 of the n-evaluation and using Theorem 4, Observation 2 and Corollary
5.4, we can see that Theorem 2 follows.
□
