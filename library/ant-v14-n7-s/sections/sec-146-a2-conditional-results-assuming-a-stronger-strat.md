---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-146-a2-conditional-results-assuming-a-stronger-strat
section_title: "A.2. Conditional results: assuming a stronger stratification result"
section_number: null
pages: 281-282
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
2=2n,r is as a function of r, the better the bound is asymptotically in n. We brieﬂy explore how one
could hope to increase the value of 2n,r. The key is to improve Theorem A, and hence Theorem 4.4, by
obtaining larger values for the codimensionsθ j.
At present, Theorem 4.4 holds with θ0= 0 andθn= nr ; for the intermediate values 1≤ j≤ n− 1, we
currently obtain values
θ j= j
⌊ r−1
n−1
⌋
≈ j
( r−1
n−1
)
. (A-2)
However, suppose that in the stratiﬁcation result of Theorem A (and hence in Theorem 4.1 and its
corollaries under the modiﬁed hypotheses), we were able to take the larger values
θ♯
j= jr, 1≤ j≤ n. (A-3)
This is a natural hypothesis since it is the linear interpolation between θ0= 0 andθn= nr . In fact, note
from the deﬁnition (A-2) that we very nearly achieve (A-3) in the case of n= 2.
Supposing that we can take θ♯
j as large as in (A-3) in Theorem A, we could deduce that the statement
of Theorem 4.4 would hold with the function Bn,r( j; k) replaced by the modiﬁed function B♯
n,r( j; k)
deﬁned for 0≤ j≤ n and k=(k1,..., kn) with k1≤ k2≤···≤ kn by
B♯
n,r( j; k)=



1 if j= 0,
(k1··· k j/2)2r if j≥ 1 is even,
(k1··· k( j−1)/2)2rkr
( j+1)/2 if j≥ 1 is odd.
Proceeding through the Burgess argument in this paper with the function Bn,r( j; k) replaced in each
instance by B♯
n,r( j; k), we would arrive at the analogue of (7-1), which now takes the form
|S(F; N, H)|2r≪n,r,1, D(log q)2r(n+1)‖H‖2r−1 P−1qn/2
n∑
j=0
q j/2~B♯
n,r( j; H/P)−1, (A-4)
in which for any k with k1≤ k2≤···≤ kn we deﬁne
~B♯
n,r( j; k)=



1 if j= 0,
(k1··· k j/2)2r−1 if j≥ 1 is even,
(k1··· k( j−1)/2)2r−1kr
( j+1)/2 if j≥ 1 is odd.
1948 Lillian B. Pierce and Junyan Xu
Recall that we assume H1≤ H2≤···≤ Hn. We choose (cf. (7 -2) and (7-4)) P to be an integer such that
H1
2q1/(2r−1)≤ P≤ H1
q1/(2r−1)
which balances the j= 0 and j= 2 contributions. Under this choice, a simple computation shows that
for each j= 0,..., n we can verify that
q j/2~B♯
n,r( j; H/P)−1≤ 1,
upon using the fact that H1≤ H2≤... ≤ Hn and the deﬁnition of the function ~B♯
n,r(·,·) given above.
Applying this in (A-4) would give
|S(F; N, H)|≪ n,r,1, D‖H‖1−(1/2r)H−1/2r
1 q(n2♯+1)/4r2♯
(log q)n+1
with the deﬁnition
2♯= 2r−1
2 = r− 1
2.
We can compute that this is nontrivial for H satisfying the analogues of (1-6) or (1-8) with2♯ in place
of2; in the limit as n→∞ we quantify the strength of the bound near the thresholdβn= 1
2−1/(2(n+1)).
Lettingβ=βn+κ, then our bound is of the form‖H‖q−δ, where
δ= n+ 1
2r κ− 1
4r2♯≈ n+ 1
2r κ− 1
4r 2.
The maximum
δ≈(n+ 1)2
4 κ2
is achieved when r is the nearest integer to
r≈ 1
κ(n+ 1).
Thus this conjectural improvement to the stratiﬁcation would yield a stronger savings near the thresholdβn,
but would not alter the fundamental threshold βn. Similar computations to those above show that even if
we could conjecturally improve the θ j values to the strongest possible values θ♭
j= nr for 1≤ j≤ n, this
bound will not be improved substantially, and the threshold βn will not change.
