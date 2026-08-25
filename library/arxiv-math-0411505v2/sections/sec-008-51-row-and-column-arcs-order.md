---
doc_id: arxiv-math-0411505v2
doc_title: "A NON-COMMUT A TIVE FORMULA FOR THE COLORED JONES FUNCTION"
section_id: sec-008-51-row-and-column-arcs-order
section_title: "Row and column arcs order"
section_number: 5.1
pages: 8-9
source_pdf: 0411505v2.pdf
source_sha256: a38cec365e0a227e
doc_brief: "A NON-COMMUTATIVE FORMULA FOR THE COLORED JONES FUNCTION — The colored Jones function of a knot is a sequence of Laurent p olynomials that encodes the Jones polynomial of a knot and its parallels."
---
with r + 1 crossings. We order the arcs of K so that they appear in increasing order as we walk in the
direction of the knot, and we denote by K the long knot obtained by breaking the arc ar+1. We also order
the crossings of K so that arc ai ends at the ith crossing, for i = 1, . . . , r.
Deﬁnition 5.1. (1) We deﬁne two permutations S, T on the set of the arcs of K as follows. For
arc ai of K let T (i) = T (i, 1), . . . , T(i, ki) ( S(i) = S(i, 1), . . . , S(i, ki) respectively) be the block
of arcs of K terminating at (starting from) ai and ordered along the orientation of ai. Let T
(S) be the permutation of the arcs of K deﬁned by T = T (1, 1), . . . , T(1, k1), . . . , T(r, kr) ( S =
S(r, kr), . . . , S(r, 1), . . . , S(1, 1)).
(2) We deﬁne permutation R of the arcs of K from T as follows: if ai appears in S before the block S(i)
then replace T (i, 1), . . . , T(i, ki) by T (i, ki), . . . , T(i, 1).
(3) Similarly we deﬁne permutation C of the arcs of K from S as follows: if ai appears in S after the
block S(i) then replace S(i, ki), . . . , S(i, 1) by S(i, 1), . . . , S(i, ki).
Deﬁnition 5.2. We deﬁne matrix B′
K = ( γij) to be obtained from BK by taking the rows in the R order
and the columns in the C order.
We consider the commutation relations between the variables appea ring in B′
K as in the Deﬁnition 1.1.
In particular, B′
K is right-quantum.
5.2. Flows on GK and monomials of GB′
K
(m1, . . . mr). We interpret each entry γij with no z indeter-
minate as arc ( ij) of the arc-graph GK . Then each monomial in GB′
K
(m1, . . . , mr) corresponds to a ﬂow
on GK with indeg(i) = outdeg(i) = mi, i = 1 , . . . , r. If f is such a ﬂow, we denote by G(f ) the sum of all
monomials of ∑ GB′
K
(m1, . . . , mr) corresponding to f . Summarizing we can write
Observation 1. ∞∑
m1,...,mr=0
GB′
K
(m1, . . . , mr) =
∑
f
G(f ).
We denote by C(f ) the canonical monomial of a product (in arbitrary order) of the e ntries of B′
K corre-
sponding to the edges of GK, where the entry corresponding to each edge e appears f (e) times.
Observation 2. Let C be a summand of ∏ r
i=1(∑
j γijxj )mi, which contains mi indeterminates xi, i =
1, . . . , r and contributes to G(f ). For 1≤ v≤ r and 1≤ j≤ f (er
v) let c(C, v, j) be the number of γeb
v
’s which
need to be commuted through the j-th occurrence of γer
v in order to get C(f ) from C. Then
C = xm1
1 xm2
2 . . . xmr
r q−rot(f )C(f )qexc(f )
r∏
v=1
f (er
v )∏
j=1
qsign(v)c(C,v,j).
8
Proof. Let Xij = γijxj. Hence C is a summand of the coeﬃcient of xm1
1 xm2
2 . . . xmr
r in ∏ r
i=1(∑
j Xij)mi .
For each j ﬁxed the γij’s appear ordered in C. In each canonical monomial, the γij’s appear ordered by
the second coordinate, and then by the ﬁrst coordinate. Hence, in order to get a canonical monomial times
xm1
1 xm2
2 . . . xmr
r from a summand of∏ r
i=1(∑
j Xij)mi, we only need to commute Xij’s so that they are ordered
by the second coordinate. This means: if ai appears in S before (after respectively) the block S(i) then ai
appears in C before (after respectively )the block S(i) BUT ai−1 appears in R after (before respectively) the
block T (i). Hence we need to commute
1. Each Xi−1,i through each Xj−1,j, j∈ S(i) and each Xk−1,i through each Xj−1,j, j, k∈ S(i), R(k) >
R(j). The commutation in B′
K is such that we acquire each time qsign(j−1). Hence we acquire in
total qexc(f ) since we recall that exc( f ) =∑
v sign(v)f (eb
v)∑
e<er
v
f (e).
2. Each Xk−1,i through each Xk−1,k, k∈ S(i). The commutation in B′
K is such that we acquire in total
qsign(k−1)(c(C,k−1,1)+...c(C,k−1,f (er
k−1)).
3. The commutation in B′
K is such that if i < i ′, j < j ′ and Xi,j′ , Xi′,j do not appear in one of the
previous two cases then Xi,j′ , Xi′,j = Xi′,j, Xi,j′ .
This ﬁnishes the proof. □
Corollary 5.3.
G(f ) = C(f )qδ(f )
r∏
v=1
∑
f (eb
v )≥c1≥···≥cf (er
v )≥0
qsign(v)(c1+...cf (er
v )).
Since ∑
f (eb
v )≥c1≥···≥cf (er
v )≥0
qsign(v)(c1+...cf (er
v )) =
( f (v)
f (eb
v)
)
qsign(v)
,
we have
Corollary 5.4.
G(f ) = qδ(f )multq(f )C(f ).
Proof. (of Theorem 2) Theorem 7 tells us that
Jn(K, q) = qδ(K,n) ∑
f ∈F (GK)
multt(f )tδ(f ) ∏
v∈VK
t−sign(v)nf (eb
v ) ∏
ered;t(e)=v
f (e)−1∏
j=0
(1−t−sign(s(e))(n−(∑
e′<v e f (e))−j)).
Comparing this with the deﬁnition 1.2 of the n-evaluation and using The orem 4, Observation 2 and Corollary
5.4, we can see that Theorem 2 follows. □
