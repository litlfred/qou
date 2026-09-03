---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-063-76-mahler-measures
section_title: "Mahler measures"
section_number: 7.6
pages: 56-57
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
7.6.1. 3-braids
The material in section 7 originated from a question of S. Kamada whether the Alexander polynomial Mahler measure
M(∆) is bounded on closed 3-braids.
Deﬁnition 7.1 For a Laurent polynomial p ∈ Z[t±1], and n ∈ N+, we deﬁne the n-norm of p by
||p||n := n
√
∞
∑
k=−∞
(
[p]k
) n ,
and its Mahler measure by
M(p) := ∏
|t|≥1, p(t)=0
|t| .
This is extended to p ∈ Z[t±1/ 2] in the obvious way. See [SSW, CK].
Kamada’s question is related to controlling|V (t)| and |∆(t)| for t ∈ S1, since the 2-norm || .||2 and the Mahler measure
M of polynomials have circle integral formulas (see (64) and ( 65)). One can thus ask whether ||∆ ·Wn||2 is bounded
for proper Wn ∈ Z[t,1/ t], or (weaker) whether M(∆) is bounded (and similarly M(V ) and ||V ·Wn||2) for braid index
≤ n.
For values of t where J0 is not deﬁnite, however, there seems little one can say on the range (on closed 3-braids) of
|V (t)| or |∆(t)|. Likely they are dense in R+. We can conclude boundedness properties in special cases wh ere the
indeﬁnite J0 values of t are controllable. For example the following can be proved ea sily. (Note that for polynomials
with integer coefﬁcients the properties a set of polynomial s to have bounded 2-norms, or ﬁnitely many distinct 2-
norms, are equivalent, and also equivalent to the same two properties for the 1-norm.)
Proposition 7.5 The set
{ ||(1 − t2n)∆ ˆβ(t)||2 : β ∈ B2n, ∆ ˆβ ∈ Z[t±n] }
is ﬁnite for any n ≥ 2.
Proof. We have
||X||2
2 =
Z 1
0
⏐⏐X(e2πis)
⏐⏐2 ds .(64)
If ∆ ∈ Z[t±n], then this integral for
X = (1 − t2n)∆(t)
1 − t = det(1 − ψ 2n−1)
is controlled from its part over 0 < s < 1
2n, and this in turn is controlled by the unitarity of ψ 2n−1. To eliminate the
denominator, observe that the norm in (64) is just the one in L2(S1), and so ||P · Q||2 ≤ ||P||2 · ||Q||2. ✷
However, in general a bound on the Mahler measure of arbitrar y polynomials of closed n-braids does not exist even
for n = 3.
Proposition 7.6 The Mahler measure of ∆ and V is unbounded on closed 3-braids.
Proof. In the following x ≤ O(y) means limsup |x/ y| < ∞ (the limit following from the context), x ≥ O(y) means
liminf |x/ y| > 0 and x = O(y) means both x ≤ O(y) and x ≥ O(y). The quantities C and C′ will stand for real constants,
with C being positive. They are understood to be independent on the indices of the terms in the formula they occur in,
but may vary between the various inequalities.
