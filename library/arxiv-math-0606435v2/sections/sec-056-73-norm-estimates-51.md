---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-056-73-norm-estimates-51
section_title: "Norm estimates 51"
section_number: 7.3
pages: 51-52
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Corollary 7.2 For all n,k the set {
∆(ˆβ) : β ∈ Bn , deg∆ ≤ k
}
is ﬁnite. That is, among closed braids of given number of stra nds only ﬁnitely many Alexander polynomials of given
degree occur.
Proof. ∆ is determined by ∆(ti) for k different ti with |ti| = 1, 0 < argti < 2π/ n, by means of a linear transformation
using the (regular Vandermonde) matrixM = (t j
i )n
i,j=1. So ||[∆(t)]t j || ≤ || M−1|| · ||∆(ti)|| . ✷
This result should be put in contrast to the various construc tions of knots with any given Alexander polynomial. For
example a recent construction of Nakamura [Na2] allows to re alize the degree of the polynomial by the (actually
braidzel) genus of the knot. (We were subsequently independ ently able to further specialize this result to canonical
genus.) A different construction of Fujii [Fu] shows that kn ots with 3 bridges admit all Alexander polynomials. So
the situation between braid and plat closures is completely different.
Compare also Birman-Menasco’s result in [BM3], mentioned ( for knots) in remark 6.1, that there are only ﬁnitely
many closed braids of given number of strands with given genu s. Note that we do not claim that only ﬁnitely many
closed braids of given number of strands with given Alexander polynomial (degree) occur. For 3-braids it is true, but
from 5-braids on the non-faithfulness of the Burau representation should (in principle, modulo the evaluability of an-
other invariant) make it possible to construct inﬁnite families of links with the same (for example, trivial) polynomial.
It makes some sense to ask about the status of 4-braids.
Question 7.1 Are there only ﬁnitely many closed 4-braids of given Alexander polynomial (degree)?
When working with ∆, for 3- and 4-braids we can be more explicit.
Corollary 7.3 If β ∈ B4, then
⏐⏐ ∆ ˆβ(t)
⏐⏐ ≤ 8 |1 − t|
|1 − t4| ,(59)
when |t| = 1 and ℜ t > 0. If β ∈ B3 and ℜ t > −1/ 2, then
⏐⏐ ∆ ˆβ(t)
⏐⏐ ≤ 4 |1 − t|
|1 − t3| . ✷
Putting t = e2πi/ 5 in (59) we have
⏐⏐ ∆(e2πi/ 5)
⏐⏐ ≤ 8 . This improves the bound 10 .47 . . .in [St3] suggested to replace
Jones’s (incorrect) value 6.5 in [J2]. For 3-braid knots Jones gives in [J, proposition 15.2] the better bound 3 when
t = i, using the property V (i) = ±1.
Example 7.1 The simplest knots with MWF = 4 which can be excluded from being a 4-braid using corollary 7.3 are
138385 (where one can use t = e2πi/ 9) and 1437492 (with t = e2πi/ 8). For 3-braids we can deal with the known examples
942 and 949. (This gives now an alternative proof that there are no 3-bra id knots with such Alexander polynomial, as
we explained in example 4.2.)
If we know the exponent sum of β we can do better.
Proposition 7.2 If β ∈ B4, e = [β] and t as before, then
⏐⏐⏐⏐
(
−
√
t
) e−3
∆ ˆβ(t)1 − t4
1 − t − 1 + (−t)e
⏐⏐⏐⏐ ≤ 6.
If β ∈ B3 and ℜ t > −1/ 2, then ⏐⏐⏐⏐
(
−
√
t
) e−2
∆ ˆβ(t)1 − t3
1 − t − 1 − (−t)e
⏐⏐⏐⏐ ≤ 2 . ✷
52 7 Applications of the representation theory
~W1111 = 1
[2][3][4] × ~W211 = q
[2][1][4]× ~W22 = q2
[2][2][3]× ~W31 = q3
[2][1][4] × ~W4 = q6
[2][3][4]×
1 1 1 1 1 1
−λ q2 + q3 + q4 1 + q2 + q3 1 + q + q2 1 + 1/ q + q2 1 + 1/ q + 1/ q2
λ2 q5 + q6 + q7 q3 + q2 + q5 q + q2 + q3 1/ q + q + q2 1/ q + 1/ q2 + 1/ q3
−λ3 q9 q5 q3 q 1/ q3
Table 3: The weights of the traces contributing to the λ-coefﬁcients of X for a 4-braid.
Each table entry must be multiplied with the factor on the rig ht in the ﬁrst row to obtain
the contribution of the corresponding trace to −
√
λ
e−3
times the power of −λ in the ﬁrst
column. In the ﬁrst row the symbol [i] denotes 1 − qi.
Example 7.2 Since one can determine the possible e via MWF from P, one can apply proposition 7.2 for given P. In
the 3-braid case we can exclude 10 150 this way. The remaining two 10 crossing knots with unsharp MW F, 10132 and
