---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from Quantum Geometry"
section_id: sec-007-iv-the-entropy-calcula-tions
section_title: "THE ENTROPY CALCULA TIONS"
section_number: IV
pages: 9-12
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
doc_brief: "Black hole entropy from Quantum Geometry — Quantum Geometry (the modern Loop Quantum Gravity using gra phs and spin-networks instead of the loops) provides microscopic d egrees of freedom that"
---
To ﬁnd an upper bound for the number N(a) introduced in the previous section (recall
that a = 4 πγℓ 2
Plk, and k ∈ N), consider the set M +
k of all the ﬁnite sequences ( m1, ..., mn)
of non-zero elements of 1
2Z which satisfy the inequality in (34), but do not necessarily sum
to zero,that is,
M +
k := {(m1, ..., mn)
⏐
⏐
⏐ n ∈ N, 0 ⁄= m1, ..., mn ∈ 1
2 Z,
n∑
i=1
|mi| ≤ k
2 } . (37)
Let N +
k be the number of elements of M +
k plus 1 (the empty sequence). Certainly,
N(a) ≤ N +
k (38)
Next, since k is arbitrarily ﬁxed integer, let it become a variable of the s e-
quence ( N +
0 , N +
1 , ..., N+
k , ...). To establish a recurrence relation satisﬁed by the
sequence ( N +
0 , N +
1 , ..., N+
k , ...), notice that if ( m1, ..., mn) ∈ M +
k−1, then both
(m1, ..., mn, 1
2 ), (m1, ..., mn, − 1
2 ) ∈ M +
k . In the same way, for arbitrary natural 0 < l ≤ k,
(m1, ..., mn) ∈ M +
k−l ⇒ (m1, ..., mn, ±1
2 l) ∈ M +
k . (39)
9
Obviously, if we consider all 0 < l ≤ k, and all the sequences ( m1, ..., mn) ∈ M +
k−l, then the
resulting ( m1, ..., mn, ± 1
2 l) form the entire set M +
k . Also, for two diﬀerent l ⁄= l′,
(m1, ..., mn, ±1
2 l) ⁄= ( m1, ..., mn, ±1
2 l′). (40)
This proves the following recurrence relation,
N +
k = 2 N +
k−1 + ... + 2N +
0 + 1. (41)
The (unique) solution is
N +
k = 3 k. (42)
In conclusion,
N(a) ≤ 3k . (43)
To ﬁnd a lower bound for N(a), we use the inequality
√
|mi|(|mi| + 1) ≤ | mi| + 1
2 , (44)
and consider the number N −
k equal to 1 plus the number of elements in the set
M −
k := {(m1, ..., mn)
⏐
⏐
⏐ n ∈ N, 0 ⁄= m1, ..., mn ∈ 1
2Z,
n∑
i=1
(|mi| + 1
2 ) ≤ k
2 } (45)
Notice that this time, ignoring the constraint that the elem ents mi of each sequence sum to
zero (34) makes an in-equivalence relation between N(a) and N −
k a priori not known. But
let us postpone this problem for a moment. Using the same cons truction as above, we ﬁnd
the recurrence relation satisﬁed by N −
k ,
N −
k = 2 N −
k−2 + ... + 2N −
0 + 1. (46)
The unique solution is
N −
k = 2
3 2k + (−1)k
3 . (47)
A lower bound for N(a) is the number N ′−
k of the elements of M −
k which additionally satisfy
m1 + ... + mn = 0,
N ′−
k ≤ N(a). (48)
A statistical physics argument giving the value of the desir ed number N ′−
k is as follows (this
argument is due to Meissner, who also provided an exact proof in [11]). We can think of
each sequence ( m1, ..., mn) as of a sequence of random steps on a line. The total length of
10
each path is bounded by k owing to the inequality in the deﬁnition of the set M −
k . The
number of sequences in M −
k of a given, ﬁxed value of the sum
m1 + ... + mn = δ (49)
depends on δ. The average value of δ is ¯δ = 0. For large values of k, the number of the
paths corresponding to the random walk distance δ should be given by the Gaussian function
C√
k e− δ 2
βk N −
k . In particular, the value
N ′−
k = C
√
k
N −
k (50)
corresponds to δ = 0.
Summarizing,
C√
k
N −
k ≤ N(a) ≤ N +
k , (51)
where the numbers N −
k and N +
k were calculated in (43, 47). Therefore the entropy is
bounded in the following way
ln 2
4πγℓ 2
Pl
a + o(a) ≤ S(a) ≤ ln 3
4πγℓ 2
Pl
a. (52)
We are in a position now, to compare our results with those of [ 8]. The mistake made in [8]
in the combinatorial formulation (see (44) in that paper) is an assumption, that one can order
the ji labels in (23) such that j1 ≤ ... ≤ jn, and impose this as a constraint on ‘admissible’
states we count. As a consequence, the number of the states co ntributing to the entropy
was underestimated: the analysis of [8] implied that for lar ge a the leading contribution to
the number of sequences comes only from the sequences ( m1, ..., mn) = ( ± 1
2, ..., ± 1
2 ). The
resulting number SABCK(a) proposed for the value of the entropy was
SABCK(a) = ln 2
4π
√
3γℓ2
Pl
a + O(a). (53)
The comparison with our (52) shows that the contribution from the higher half integers
|mi| > 1
2 can not be neglected.
The next consequence of the estimate (52) is a necessary cond ition for the agreement
of the entropy S(a) with the Bekenstein-Hawking entropy a / 4ℓ2
Pl; the condition is that the
value of the Barbero-Immirzi parameter γ is bounded in the following way,
ln 2
π ≤ γ ≤ ln 3
π . (54)
On the other hand, the value proposed for the Barbero-Immirz i parameter by counting the
sequences ( ±1/2, ..., ±1/2) was
γABCK = ln 2
π
√
3
. (55)
11
In the accompanying paper [11] the recurrence relations (46 ,41) are generalized to an
appropriate generalized recurrence relation satisﬁed by t he desired number N(a) itself. Next,
the combinatorial problem formulated in the previous secti on is solved completely. The
method is remarkably powerful. The result of [11] is
S(a) = γM
γ
a
4ℓ2
Pl
− 1
2 ln a + O(1), (56)
where γM is a constant deﬁned by the following equation
1
2 −
∑
0⁄=j∈ 1
2 N
e−2πγM
√
j(j+1) = 0. (57)
The numerical value of γM is calculated in [11].
An interesting historical remark is (it has been unraveled t o us recently, after our results
were derived) that before coming to their ﬁnal result (53, 55 ), Ashtekar, Baez and Krasnov
had established certain estimate. The inequality had been
Sbh(a) ≤ γ0
γ
a
4ℓ2
Pl
+ O(a) (58)
where the constant γ0 had been deﬁned by the same equation as as γM above. But since this
result emerged as an upper bound only, ﬁnally it was replaced by the improper one (53,55).
