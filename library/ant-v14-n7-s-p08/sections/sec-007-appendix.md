---
doc_id: ant-v14-n7-s-p08
doc_title: "Burgess bounds for short character sums evaluated at forms"
section_id: sec-007-appendix
section_title: "Appendix"
section_number: null
pages: 36-39
source_pdf: ant-v14-n7-s-p08.pdf
source_sha256: 81b8f00fe5fbd0f6
toc_source: inferred
doc_brief: "Burgess bounds for short character sums evaluated at forms — 11 sections: Front matter; Introduction; Method of proof: an overview"
---
A.1. The role of the stratiﬁcation. It is useful to remark on the crucial role that the stratiﬁcation plays
in obtaining our main theorem. Suppose that instead of Theorem A we only gained information about X1,
without any further stratiﬁcation into X2, . . . , Xn. Then for those (x(1), . . . , x(2r)) ∈A2nr
Fq \ X1(Fq), we
would have
|S(x(1), . . . , x(2r))| ≤Cqn/2,
but for those (x(1), . . . , x(2r)) ∈X1(Fq) we could have an upper bound as bad as the trivial (#Fq)n. We
would then have only the instance j = 1 of Theorem 4.4, namely
#

{x} ∈(0, k]2r :

X
m (mod q)
χ(F{x}(m))

 > Cqn/2

≤C′′∥k∥2rk−θ1
1
.
In place of (6-1) and Lemma 6.1 we would now have
X
m (mod q)
|S(F; m, k)|2r ≤
X
{x}∈(0,k]2r
{x}∈X0\X1

X
m (mod q)
χ(F{x}(m))

 +
X
{x}∈(0,k]2r
{x}∈X1

X
m (mod q)
χ(F{x}(m))

≪∥k∥2rCqn/2 + C′′∥k∥2rqnk−θ1
1
.
The second term has the worst growth qn appearing in (6-2) combined with the least savings k−θ1
1
=
Bn,r(1; k)−1. Proceeding with Menshov–Rademacher and the remaining argument, we would obtain
|S(F; N, H)|2r ≪(log q)2r(n+1)∥H∥2r−1P−1qn/2(1 + qn/2eBn,r(1; H/P)−1).
Burgess bounds for short character sums evaluated at forms
1947
The last factor is 1 + qn/2(H1/P)−θ1, which we balance by choosing P = H1q−n/(2θ1). This is a smaller
choice than (7-4), hence provides smaller savings; ultimately this yields the bound
|S(F; N, H)| ≪∥H∥1−1/2r H−1/2r
1
q(nθ1+n)/4rθ1(log q)n+1.
(A-1)
This is worse than our main theorem by a factor of q(n−1)/4rθ1.
A.2. Conditional results: assuming a stronger stratiﬁcation result. In our Theorem 1.1, the larger
2 = 2n,r is as a function of r, the better the bound is asymptotically in n. We brieﬂy explore how one
could hope to increase the value of 2n,r. The key is to improve Theorem A, and hence Theorem 4.4, by
obtaining larger values for the codimensions θ j.
At present, Theorem 4.4 holds with θ0 = 0 and θn = nr; for the intermediate values 1 ≤j ≤n −1, we
currently obtain values
θ j = j
j r −1
n−1
k
≈j
r −1
n−1

.
(A-2)
However, suppose that in the stratiﬁcation result of Theorem A (and hence in Theorem 4.1 and its
corollaries under the modiﬁed hypotheses), we were able to take the larger values
θ♯
j = jr,
1 ≤j ≤n.
(A-3)
This is a natural hypothesis since it is the linear interpolation between θ0 = 0 and θn = nr. In fact, note
from the deﬁnition (A-2) that we very nearly achieve (A-3) in the case of n = 2.
Supposing that we can take θ♯
j as large as in (A-3) in Theorem A, we could deduce that the statement
of Theorem 4.4 would hold with the function Bn,r( j; k) replaced by the modiﬁed function B♯
n,r( j; k)
deﬁned for 0 ≤j ≤n and k = (k1, . . . , kn) with k1 ≤k2 ≤· · · ≤kn by
B♯
n,r( j; k) =



1
if j = 0,
(k1 · · · k j/2)2r
if j ≥1 is even,
(k1 · · · k( j−1)/2)2rkr
( j+1)/2
if j ≥1 is odd.
Proceeding through the Burgess argument in this paper with the function Bn,r( j; k) replaced in each
instance by B♯
n,r( j; k), we would arrive at the analogue of (7-1), which now takes the form
|S(F; N, H)|2r ≪n,r,1,D (log q)2r(n+1)∥H∥2r−1P−1qn/2
n
X
j=0
q j/2eB♯
n,r( j; H/P)−1,
(A-4)
in which for any k with k1 ≤k2 ≤· · · ≤kn we deﬁne
eB♯
n,r( j; k) =



1
if j = 0,
(k1 · · · k j/2)2r−1
if j ≥1 is even,
(k1 · · · k( j−1)/2)2r−1kr
( j+1)/2
if j ≥1 is odd.
1948
Lillian B. Pierce and Junyan Xu
Recall that we assume H1 ≤H2 ≤· · · ≤Hn. We choose (cf. (7-2) and (7-4)) P to be an integer such that
H1
2q1/(2r−1) ≤P ≤
H1
q1/(2r−1)
which balances the j = 0 and j = 2 contributions. Under this choice, a simple computation shows that
for each j = 0, . . . , n we can verify that
q j/2eB♯
n,r( j; H/P)−1 ≤1,
upon using the fact that H1 ≤H2 ≤. . . ≤Hn and the deﬁnition of the function eB♯
n,r( · , · ) given above.
Applying this in (A-4) would give
|S(F; N, H)| ≪n,r,1,D ∥H∥1−(1/2r)H−1/2r
1
q(n2♯+1)/4r2♯(log q)n+1
with the deﬁnition
2♯= 2r −1
2
= r −1
2.
We can compute that this is nontrivial for H satisfying the analogues of (1-6) or (1-8) with 2♯in place
of 2; in the limit as n →∞we quantify the strength of the bound near the threshold βn = 1
2 −1/(2(n+1)).
Letting β = βn + κ, then our bound is of the form ∥H∥q−δ, where
δ = n + 1
2r
κ −
1
4r2♯≈n + 1
2r
κ −1
4r2 .
The maximum
δ ≈(n + 1)2
4
κ2
is achieved when r is the nearest integer to
r ≈
1
κ(n + 1).
Thus this conjectural improvement to the stratiﬁcation would yield a stronger savings near the threshold βn,
but would not alter the fundamental threshold βn. Similar computations to those above show that even if
we could conjecturally improve the θ j values to the strongest possible values θ♭
j = nr for 1 ≤j ≤n, this
bound will not be improved substantially, and the threshold βn will not change.
A.3. Fourier methods for incomplete sums that are not short. Roughly speaking, the threshold Hi ≤q1/2
appears as a natural constraint of the ranges for which our main results hold. This is not a deﬁcit, for
recall that on the other side of this threshold, different methods, which also rely on Weil bounds, become
feasible, for appropriate F. To bound S(F; N, H) in cases where Hi ≫q1/2, an advantageous strategy is
to “complete the sum,” writing
S(F; N, H) =
X
a=(a1,...,an)
ai (mod q)
χ(F(a))
X
x∈Zn
xi∈(Ni,Ni+Hi]
1x≡a (mod q).
Burgess bounds for short character sums evaluated at forms
1949
One then expands the sum over x using
1x≡a (mod q) = 1
qn
X
k (mod q)
eq(k · (x −a))
so that
S(F; N, H) = 1
qn
X
k (mod q)
X
a (mod q)
χ(F(a))eq(−k · a)41(a1/q) · · · 4n(an/q),
in which 4(α) = min{Hi, ∥α∥−1}, where ∥α∥denotes the distance from α to the nearest integer. One then
aims to show that under appropriate assumptions on the smoothness of F ∈Fq[x1, . . . , xn], for generic k
a Weil bound applies so that the internal sum over a is O(qn/2). (Note that this does require the deep
input of a Weil-strength bound for a multi-dimensional mixed character sum; see, e.g., [Katz 2006].) The
resulting sum over k is then expected to be roughly on the order of O(q−n/2∥H∥+qn/2(log q)n), which is
o(∥H∥) in the case that Hi ≫q1/2 log q for each i = 1, . . . , n, that is, the setting that is complementary to
that of this paper. In a hybrid case, in which some Hi are smaller than q1/2 and some are larger, one could
adopt a hybrid strategy; this regime is closely related to [Pierce 2006; Heath-Brown and Pierce 2012].
