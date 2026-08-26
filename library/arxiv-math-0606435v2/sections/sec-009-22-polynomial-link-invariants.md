---
doc_id: arxiv-math-0606435v2
doc_title: "PROPERTIES OF CLOSED 3-BRAIDS"
section_id: sec-009-22-polynomial-link-invariants
section_title: "Polynomial link invariants"
section_number: 2.2
pages: 6-7
source_pdf: 0606435v2 (1).pdf
source_sha256: 6dddaf838a19f0f5
doc_brief: "PROPERTIES OF CLOSED 3-BRAIDS — We show that 3-braid links with given (non-zero) Alexander o r Jones polynomial are ﬁnitely many, and can be effectively determined."
---
Let X ∈ Z[t,t−1]. The minimal or maximal degree mindeg X or maxdeg X is the minimal resp. maximal exponent of t
with non-zero coefﬁcient in X. Let spant X = maxdegt X − mindegt X. The coefﬁcient in degree d of t in X is denoted
[X]td or [X]d. The leading coefﬁcient maxcf X of X is its coefﬁcient in degree maxdeg X. If X ∈ Z[x±1
1 ,x±1
2 ], then
maxdeg x1 X denotes the maximal degree in x1. Minimal degree and coefﬁcients are deﬁned similarly, and o f course
[X]xk
1
is regarded as a polynomial in x±1
2 .
Let P(v,z) be the skein polynomial [F&, LM]. It is a Laurent polynomial in two variables of orien ted knots and links.
We use here the convention of [Mo], i.e. with the polynomial taking the value 1 on the unknot, having the variables v
and z and satisfying the skein relation
v−1 P
( )
− vP
( )
= zP
( )
.(2)
We will denote in each triple as in (2) the diagrams (from left to right) by D+, D− and D0. For a diagram D of a link
L, we will use all of the notations P(D) = PD = PD(l,m) = P(L) etc. for its skein polynomial, with the self-suggestive
meaning of indices and arguments. So we can rewrite (2) as
v−1P+(v,z) − vP−(v,z) = zP0(v,z) .(3)
The writhe is a number ( ±1), assigned to any crossing in a link diagram. A crossing as o n the left in (2) has writhe
1 and is called positive. A crossing as in the middle of (2) has writhe −1 and is called negative. The writhe of a link
diagram is the sum of writhes of all its crossings.
Let c±(D) be the number of positive, respectively negative crossings of a diagram D, so that c(D) = c+(D) +c−(D)
and w(D) = c+(D) − c−(D).
The Jones polynomial [J2] V, and (one variable) Alexander polynomial [Al] ∆ are obtained from P by variable substi-
tutions
∆(t) = P(1,t1/ 2 − t−1/ 2) ,(4)
and
V (t) = P(t,t1/ 2 − t−1/ 2) .(5)
Hence these polynomials also satisfy corresponding skein relations. (In algebraic topology, the Alexander polynomial
is usually deﬁned only up to units in Z[t,t−1]; the present normalization is so that ∆(t) = ∆(1/ t) and ∆(1) = 1.)
In very contrast to its relatives, the range of the Alexander polynomial (i.e., set of values it takes) is known. Let us
call a polynomial ∆ ∈ Z[t1/ 2,t−1/ 2] admissible if it satisﬁes for some natural number n ≥ 1 the three properties
(i) t(n−1)/ 2∆ ∈ Z[t±1],
(ii) ∆(t) = (−1)n−1∆(1/ t) and
(iii) (t1/ 2 − t−1/ 2)n−1 | ∆ for n > 1, or ∆(1) = 1 for n = 1.
It is well-known that these are exactly the polynomials that occur as (1-variable) Alexander polynomials of some
n-component link.
