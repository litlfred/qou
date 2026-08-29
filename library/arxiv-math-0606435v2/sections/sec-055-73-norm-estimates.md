---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-055-73-norm-estimates
section_title: "Norm estimates"
section_number: 7.3
pages: 50-51
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
The Jones polynomial V can be speciﬁed, for our purposes, by V (t) = X(t,t). In the following, which root of complex
numbers is taken is irrelevant, important is though that it be kept ﬁxed in subsequent calculations. By ℜ we denote the
real part of a complex number.
Theorem 7.3 If |t| = 1, ℜ t > 0 and β is a 4-braid, then
⏐⏐Vˆβ(t)
⏐⏐ ≤ (2ℜ √t)3. If β is a 3-braid and ℜ t > −1/ 2, then⏐⏐Vˆβ(t)
⏐⏐ ≤ (2ℜ √t)2.
Proof. We have from [J] that if β ∈ B4 with [β] = e, then
Vˆβ(t) =
(
−
√
t
) e−3
[ t(1 − t3)
1 − t2 tr ψ 3 + t2
1 + t tr ¯ψ 2 + 1 − t5
1 − t2
]
,(56)
where ¯ψ 2 is the composition of ψ 2 with¯ : B4 → B3. Taking norms and using that ¯ψ 2 and ψ 3 are unitary, we ﬁnd
⏐⏐V (t)
⏐⏐ ≤ 3
⏐⏐⏐⏐
1 − t3
1 − t2
⏐⏐⏐⏐ + 2
|1 + t| +
⏐⏐⏐⏐
1 − t5
1 − t2
⏐⏐⏐⏐ .(57)
It is now a routine (but somewhat tedious) calculation to verify that the r.h.s. is equal to (2ℜ √t)3 for |t| = 1, ℜ t > 0.
For β ∈ B3 we have similarly
Vˆβ(t) =
(
−
√
t
) e−2 [
t · tr ψ 2 + (1 + t2)
]
,(58)
and the result follows using |tr ψ 2| ≤ 2. ✷
This theorem generalizes Jones’s result [J, proposition 15 .3] for n ≤ 4, where he considers t = e2πi/ k, k ≥ 5. In fact
the comparison to (and established coincidence with) Jones’s estimate led to the simpliﬁcation of the r.h.s. of (57). In
[St3] we noted that Jones’s estimate can be better than MWF when MWF = 3, but by connected sum one can give an
example for MW F = 4. Again it appears that for β ∈ B4 and t ⁄= e±πi/ 3 the set { |Vˆβ(t)| } is dense in [0,(2ℜ √t)3], and
similarly it is in [0,(2ℜ √t)2] for β ∈ B3 and t ⁄= e±πi/ 3,e±πi/ 5. (See also the remarks at the end of §12 in [J].)
Conjecture 7.2 If β ∈ Bn and |t| = 1 with |argt| < 2π/ n then |V (t)| ≤ (2ℜ √t)n−1.
In the case of the Alexander polynomial ∆(t) = X(t,1/ t), we can say something on general braids.
Theorem 7.4 For each n ≥ 2, if |t| = 1 and |argt| ≤ 2π/ n and β ∈ Bn then
⏐⏐∆ ˆβ(t)
⏐⏐ ≤ 2n−1|1 − t|
|1 − tn| .
Proof. J0 is positive deﬁnite when |t| = 1 and |argt| < 2π/ n. Then
⏐⏐∆ ˆβ(t)
⏐⏐ |1 − t|
|1 − tn| =
⏐⏐det(1 − ψ n−1(β))
⏐⏐ ,
and all eigenvalues of 1− ψ n−1 have norm ≤ 2. The case |argt| = 2π/ n follows by continuity. ✷
