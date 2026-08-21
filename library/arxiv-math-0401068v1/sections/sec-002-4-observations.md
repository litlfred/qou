---
doc_id: arxiv-math-0401068v1
doc_title: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS"
section_id: sec-002-4-observations
section_title: "Observations"
section_number: 4
pages: 6-11
source_pdf: 0401068v1.pdf
source_sha256: 8168d7e7f6069978
doc_brief: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS — @We show that for a twist knot, the A-polynomial can be obtained fr om recur- rences for the summand in Masbaum’s formula of the"
---
We start with reviewing Wilf-Zeilberger’s algorithm. For more details, w e refer to [4] and
[3]. A disctrete function F (n, k) is called proper q-hypergeometric if it is one of the form
F (n, k) =
∏
s(As; q)asn+bs·k+cs∏
t(Bt; q)utn+vt·k+wt
qA(n, k)ξk,
where k = ( k1, . . . , k r), As, B t ∈ Q(q), as, ut are integers, bs, ks are vectors of r integers,
A(n, k) is a quadratic form, cs, wt are variables and ξ is an r vector of elements in Q(q), and
for k ≥ 0,
(A, q )k :=
{
(1 − A)(1 − Aq) · · ·(1 − Aqk−1) if k > 0,
1 if k = 0.
In [4], Garoufalidis and Le proved that the colored Jones polynomial JK(n) can be written
as a multisum
JK(n) =
∞∑
k=0
F (n, k 1, . . . , k r)
of a proper q-hypergeometric function F (n, k 1, . . . , k r), where only ﬁnitely many terms in the
right hand side are nonzero. Consider the operators E, Ei, Q and Qj, (1 ≤ i, j ≤ r) acting on
a discrete function f : Nr → Z[q±] by
(Ef )(n, k 1, . . . , k r) = f (n + 1, k 1, . . . , k r),
(Eif )(n, k 1, . . . , k r) = f (n, k 1, . . . , k i−1, k i + 1, k i+1, . . . , k r),
(Qf )(n, k 1, . . . , k r) = qnf (n, k 1, . . . , k r),
(Qjf )(n, k 1, . . . , k r) = qkj f (n, k 1, . . . , k r).
Then, they satisfy the relations
QQi = QiQ, Q iQj = QjQi, EE i = EiE, E iEj = EjEi,
QiE = EQi, Q iEj = EjQi for i ⁄= j, EQ = qQE, E iQi = qQiEi,
which are denoted by ( Relq). The q-Weyl algebra A is deﬁned to be a noncomutative algebra
with presentation
A = Z[q±]⟨Q, Q 1, . . . , Q r, E, E 1, . . . , E r⟩
(Relq) .
Wilf and Zeilberger proved that
6
Theorem 4.1. [15] Every proper q-hypergeometric function F (n, k) satisﬁes a k-free recur-
rence
(13)
∑
i, j∈S
σi, j(qn)F (n + i, k + j) = 0 ,
where S is a ﬁnite set, k = ( k1, . . . , k r), j = ( j1, . . . , j r), and σi, j(qn) are polynomials in qn
with coeﬃcients in Q(q).
Putting
P = P (E, Q, E 1, . . . , E r) =
∑
i, j∈S
σi, j(Q)EiEj,
where Ej = E1
j1 · · ·Er
jr, the recurrence (13) can be written in operator notation as P F = 0.
Moreover, they showed that any k-free recurrence can be transformed to
P = P (E, Q, 1, . . . , 1) +
r∑
i=1
(Ei − 1)Ri(E, Q, E 1, . . . , E r).
Applying it to F (n, k 1, . . . , k r) and summing over k ≥ 0 give us
P (E, Q, 1, . . . , 1)JK(n) = error(n),
where error(n) is a sum of a multisum of proper q-hypergeometric function with r−1 variables.
So, repeating the process, we arrive at a homogeneous recursive relation of JK(n)
P1(E, Q )P (E, Q, 1, . . . , 1)JK(n) = 0 ,
where P1(E, Q ) is a polynomial in E with coeﬃcients in Q(q)[Q].
On the other hand, from the fact that F (n, k 1, . . . , k r) is proper q-hypergeometric, we can
write EF/F = A/B and EiF/F = Ai/B i for polynomials A, B, A i, B i ∈ Q(q)[qn, q k1, . . . , q kr].
Then, putting Q = qn and Qi = qki, it follows that ( BE − A)F = 0, ( BiEi − Ai)F = 0 and
that BE − A, BiEi − Ai generate the annihilation ideal of F in A. From these generators, the
Wilf-Zeilberger’s algorithm ﬁnds a k-free recurrence of F (n, k) and then a recursive relation
of the sum of ∑
k F (n, k).
Now, we apply the above algorithm to JKp(n). From the equations (3), (4) and (5), setting
B = (1 − q−n−1)(1 − q−n+k), A = qk(1 − q−n−k−1)(1 − q−n),
B1 = (1 − qk+l+2)(1 − qk−l+1), A 1 = −qk+n+2(1 − q−n−k−1)(1 − q−n+k+1)(1 − qk),
B2 = (q2l+1 − 1)(1 − qk+l+2), A 2 = q(2p+1)l+2p(q2(l+1)+1 − 1)(1 − qk−l),
we have ( BE − A)F = 0, ( BiEi − Ai)F = 0 for i = 1 , 2, with Q = qn, Q1 = qk and Q2 = ql.
Identifying Q with m2, E with l, Q1 with x, Q2 with y, from the deﬁnition of fi for i = 0, 1, 2
in Section 2, we observe that ε(BE −A) corresponds to f0(1, m 2, x, y )−l and that ε(BiEi −Ai)
with Ei = 1 corresponds to fi(1, m 2, x, y ) − 1 for i = 1 , 2, where ε is the evaluation map at
q = 1 deﬁned in [3]. So, our result may support the AJ conjecture.
Nextly, we will present the usage of the mathematica package qMultiSum.m with the above
theorical background, which is developed by A. Riese [13], to obtain in homogeneous recur-
rences of the colored Jones polynomial of the knots 5 2 and 6 1. We will also relate them to the
A-polynomial.
7
The formula in [8] allows us to write
(14) J52(n) =
∞∑
k=0
k∑
l=0
(−1)k+1q(3k2+5k)/ 2qnk (q−1)n+k(q−1)n−1
(q−1)n(q−1)n−k−1
q−l(k+1) (q−1)k
(q−1)l(q−1)k−l
.
We denote the summand by F (n, k, l ). Then, the mathematica program soft qMultiSum.m
computes the k-free recurrence of F (n, k, l )
−q4+7n (q − qn)
(
q2 − qn) (
q5 − qn)
(q + qn)
(
q2 + qn) (
q − q2n) (
q3 − q2n)
F (−5 + n, k, l )
+q1+3n (q − qn)
(
q2 − qn) (
q4 − qn) 2
(q + qn)
(
q2 + qn) (
q4 + qn) (
q − q2n) (
q3 − q2n)
×
(
q9 − q2n) (
q4 − qn − q1+n)
F (−4 + n, −1 + k, −1 + l)
−q9+2n (q − qn)
(
q2 − qn) (
q4 − qn) 2
(q + qn)
(
q2 + qn) (
q4 + qn) (
q − q2n)
×
(
q3 − q2n) (
q9 − q2n)
F (−4 + n, −1 + k, l )
−q5+6n (
1 + q + q2 + q3 + q4)
(q − qn)
(
q4 − qn) 2
(q + qn)
(
q4 + qn) (
q − q2n)
×
(
q3 − q2n)
F (−4 + n, k, l )
+ (q − qn)
(
q2 − qn) (
q3 − qn) 3 (
q4 − qn)
(q + qn)
(
q2 + qn) (
q3 + qn) (
q4 + qn) (
q − q2n)
×
(
q3 − q2n) (
q7 − q2n) (
q9 − q2n)
F (−3 + n, −2 + k, −2 + l)
+q2+2n (q − qn)
(
q3 − qn) 2 (
q4 − qn)
(q + qn)
(
q3 + qn) (
q4 + qn) (
q − q2n) (
q3 − q2n)
×
(
q9 − q2n) (
q5 + q6 + q2n − q1+n − 2q2+n − 2q3+n − q4+n)
F (−3 + n, −1 + k, −1 + l)
−q5+n (q − qn)
(
q3 − qn) 2 (
q4 − qn)
(q + qn)
(
q3 + qn) (
q4 + qn) (
q − q2n) (
q3 − q2n)
×
(
q9 − q2n) (
q6 + q2n + q1+2n)
F (−3 + n, −1 + k, l )
−q6+5n (
1 + q2) (
1 + q + q2 + q3 + q4)
(q − qn)
(
q3 − qn) 2
(q + qn)
(
q3 + qn) (
q − q2n)
×
(
q9 − q2n)
F (−3 + n, k, l )
−q (q − qn)
(
q2 − qn) 3 (
q3 − qn) (
q4 − qn)
(q + qn)
(
q2 + qn) (
q3 + qn) (
q4 + qn)
×
(
q − q2n) (
q3 − q2n) (
q7 − q2n) (
q9 − q2n)
F (−2 + n, −2 + k, −2 + l)
+q4+n (q − qn)
(
q2 − qn) 2 (
q4 − qn)
(q + qn)
(
q2 + qn) (
q4 + qn) (
q − q2n) (
q7 − q2n)
×
(
q9 − q2n) (
q5 + q2n − q1+n − 2q2+n − 2q3+n − q4+n + q1+2n)
F (−2 + n, −1 + k, −1 + l)
−q3+2n (q − qn)
(
q2 − qn) 2 (
q4 − qn)
(q + qn)
(
q2 + qn) (
q4 + qn) (
q − q2n) (
q7 − q2n)
×
(
q9 − q2n) (
q4 + q5 + q2n)
F (−2 + n, −1 + k, l )
−q7+4n (
1 + q2) (
1 + q + q2 + q3 + q4) (
q2 − qn) 2 (
q4 − qn) (
q2 + qn) (
q4 + qn) (
q − q2n)
×
(
q9 − q2n)
F (−2 + n, k, l )
−q6+n(q − qn)2 (
q + q2 − qn) (
q3 − qn) (
q4 − qn)
(q + qn)
(
q3 + qn) (
q4 + qn) (
q − q2n)
×
(
q7 − q2n) (
q9 − q2n)
F (−1 + n, −1 + k, −1 + l)
−q5+3n(q − qn)2 (
q3 − qn) (
q4 − qn)
(q + qn)
(
q3 + qn) (
q4 + qn) (
q − q2n) (
q7 − q2n)
×
(
q9 − q2n)
F (−1 + n, −1 + k, l )
−q8+3n (
1 + q + q2 + q3 + q4)
(q − qn)2 (
q4 − qn)
(q + qn)
(
q4 + qn) (
q7 − q2n)
8
×
(
q9 − q2n)
F (−1 + n, k, l )
+q9+2n (
q3 − qn) (
q4 − qn)
(−1 + qn)
(
q3 + qn) (
q4 + qn) (
q7 − q2n)
×
(
q9 − q2n)
F (n, k, l ) = 0 .
Moreover, it can be converted into the inhomogeneous recursive r elation of the colored Jones
polynomial of the knot 5 2
q9+7nJ52(n)
+ (−1 + q1+n)2 (1 + q1+n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) ×
q5+2n (
1 − q1+n − q1+2n + q2+2n + q3+2n − q6+2n + q2+3n + q7+3n + q5+4n + q6+4n + 2q7+4n
−q8+4n − q9+4n − q8+5n + q9+6n + q10+6n)
J52(1 + n)
+ (−1 + q2+n)2 (1 + q2+n) (−1 + q1+2n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) (−1 + q7+2n) ×
q
(
−1 + 2q2+n + q2+2n − q4+2n + q6+2n + q7+2n − q4+3n + q5+3n + 3q6+3n + 2q7+3n − q8+3n
−2q9+3n + q6+4n − 2q8+4n − 2q9+4n + q11+4n − q13+4n − q8+5n + 3q10+5n + 3q11+5n
−3q13+5n − 2q14+5n + q15+5n + q10+6n + q11+6n − q13+6n + 2q15+6n + q16+6n + q14+7n
+3q15+7n + 2q16+7n − q17+7n − q18+7n − q17+8n − q18+8n + q20+9n)
J52(2 + n)
−(−1 + q1+n) (1 + q1+n) (−1 + q3+n) (−1 + q1+2n)
(1 + qn) (−1 + q4+n) (1 + q4+n) (−1 + q7+2n) ×
(
−1 + q2+n + q3+n − q4+2n − 3q5+2n − 2q6+2n + q7+2n + q8+2n − q5+3n − q6+3n + q8+3n
−2q10+3n − q11+3n + q8+4n − 3q10+4n − 3q11+4n + 3q13+4n + 2q14+4n − q15+4n − q11+5n
+2q13+5n + 2q14+5n − q16+5n + q18+5n + q14+6n − q15+6n − 3q16+6n − 2q17+6n + q18+6n
+2q19+6n − q17+7n + q19+7n − q21+7n − q22+7n − 2q22+8n + q25+9n)
J52(3 + n)
+ (−1 + q1+n) (1 + q1+n) (−1 + q4+n) (−1 + q1+2n) (−1 + q3+2n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) (−1 + q7+2n) (−1 + q9+2n) ×
q1+n (
1 + q − q4+n + q6+2n + q7+2n + 2q8+2n − q9+2n − q10+2n + q8+3n + q13+3n
−q12+4n + q13+4n + q14+4n − q17+4n − q17+5n + q21+6n)
J52(4 + n)
+ (−1 + q1+n) (1 + q1+n) (−1 + q2+n) (1 + q2+n) (−1 + q5+n) (−1 + q1+2n) (−1 + q3+2n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) (−1 + q4+n) (1 + q4+n) (−1 + q7+2n) (−1 + q9+2n) ×
q4+2nJ52(5 + n) = G(n),
where G(n) is a sum of sums of proper q-hypergeometric function. Setting q = 1, and replacing
J52(i + n) by li and qn by m2, the denominators cancell, the left hand side is changed to
(1 + m2l)2 ×
{m14 + l(m4 − m6 + 2m10 + 2m12 − m14) − l2(−1 + 2m2 + 2m4 − m8 + m10) + l3},
and the second factor is equal to the A-polynomial of the knot 5 2. So, this supports the AJ
conjecture for the knot 5 2.
9
Furthermore, the colored Jones polynomial of the knot 6 1 can be written
(15) J61(n) =
∞∑
k=0
k∑
l=0
q−k2−kqnk (q−1)n+k(q−1)n−1
(q−1)n(q−1)n−k−1
ql(k+1) (q)k
(q)l(q)k−l
.
Using qMultiSum.m again, we can obtain the inhomogeneous recursive relation of J61(n)
q8+4nJ61(n)
− (−1 + q1+n)2 (1 + q1+n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) ×
q5+2n (
1 + q − 2q2+n − q3+n − q1+2n − q2+2n + q3+2n − q6+2n − q7+2n + q3+3n − q5+3n
−q6+3n − q7+3n + q8+3n − q4+4n + q7+4n + q8+4n − q9+4n − q9+5n + q10+6n)
J61(1 + n)
− (−1 + q2+n)2 (1 + q2+n) (−1 + q1+2n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) (−1 + q7+2n) ×
q
(
−1 + 2q2+n + q3+n + q2+2n + q3+2n − q4+2n − 2q5+2n + q6+2n + q7+2n − 2q4+3n − q5+3n
+2q6+3n + 3q7+3n − 2q9+3n − q10+3n − q5+4n + q6+4n + q7+4n − 2q8+4n − 5q9+4n − 3q10+4n
+q12+4n − q13+4n − 2q8+5n − 3q9+5n + 3q11+5n + q12+5n − 2q13+5n − 3q14+5n + 2q11+6n
+q12+6n − 2q13+6n − 2q14+6n + 2q16+6n − q13+7n + 2q15+7n + 3q16+7n − q18+7n
−2q18+8n + q20+9n)
J61(2 + n)
+ (−1 + q1+n) (1 + q1+n) (−1 + q3+n) (−1 + q1+2n)
(−1 + qn) (−1 + q4+n) (1 + q4+n) (−1 + q7+2n) ×
(
−1 + 2q3+n + q3+2n − 2q5+2n − 3q6+2n + q8+2n − 2q6+3n − q7+3n + 2q8+3n + 2q9+3n
−2q11+3n + 2q8+4n + 3q9+4n − 3q11+4n − q12+4n + 2q13+4n + 3q14+4n + q10+5n − q11+5n
−q12+5n + 2q13+5n + 5q14+5n + 3q15+5n − q17+5n + q18+5n + 2q14+6n + q15+6n − 2q16+6n
−3q17+6n + 2q19+6n + q20+6n − q17+7n − q18+7n + q19+7n + 2q20+7n − q21+7n − q22+7n
−2q22+8n − q23+8n + q25+9n)
J61(3 + n)
−(−1 + q1+n) (1 + q1+n) (−1 + q4+n) (−1 + q1+2n) (−1 + q3+2n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) (−1 + q7+2n) (−1 + q9+2n) ×
q2+n (
1 − q4+n − q4+2n + q7+2n + q8+2n − q9+2n + q8+3n − q10+3n − q11+3n − q12+3n
+q13+3n − q11+4n − q12+4n + q13+4n − q16+4n − q17+4n − 2q17+5n − q18+5n
+q20+6n + q21+6n)
J61(4 + n)
+ (−1 + q1+n) (1 + q1+n) (−1 + q2+n) (1 + q2+n) (−1 + q5+n) (−1 + q1+2n) (−1 + q3+2n)
(−1 + qn) (−1 + q3+n) (1 + q3+n) (−1 + q4+n) (1 + q4+n) (−1 + q7+2n) (−1 + q9+2n) ×
q18+5nJ61(5 + n) = G′(n),
where G′(n) is a sum of sums of proper q-hypergeometric function. Setting q = 1, and replacing
J61(i + n) by li and qn by m2, the left hand side is changed to
(1 + m2l){m8 + l(−2m4 + 3m6 + 3m8 + 2m14 − m16)
+l2(1 − 3m2 − m4 + 3m6 + 6m8 + 3m10 − m12 − 3m14 + m16)
+l3(−1 + m2 + m4 + 3m10 + 3m12 − 2m14) + m8l4},
10
and the second factor coincides with the A-polynomial of the knot 6 1.
Finally, we discuss our result in terms of Volume conjecture due to Kashaev, H.Murakami
and J.Murakami. (see [7],[10]). Let K be a hyperbolic knot in S3 and MK the complement of
K. We write ˆJK(n) for JK(n) evaluated at q = exp 2π √−1
n . Then, Volume conjecture is
Conjecture 4.2.
2π lim
n→∞
log | ˆJK(n)|
n = V ol(MK),
where V ol(MK) is the hyperbolic volume of MK.
From the formula of JKp(n) given by Masbaum, we have
(16) ˆJKp(n) =
∞∑
k=0
k∑
l=0
(−1)k+lqk(k+3)/ 2(q)k(q−1)kql(l+1)p+l(l−1)/ 2 (q)2l+1
(q)2l
(q)k
(q)k+l+1(q)k−l
.
Computing the optimistic limit [9] of ˆJK(n), it is conjectured that there exists a solution
(x0, y 0) to the two equations
(17) f1(1, 1, x, y ) = 1 , f 2(1, 1, x, y ) = 1
such that
V ol(MK) = 3 D(x0) − D(x0y0) − D( x0
y0
),
where fi is the same notation as in Section 2, and D(z) = Im(Li 2(z)) + log |z| arg(1 − z) with
Li2(z) = −
∫ z
0
log(1−w)
w dw. By using Mathematica 4 and Maple V, we can numerically see that
for p = −1, 2, −2, this conjecture is true.
In [16], Y.Yokota introduced a way to construct an ideal triangulatio n of the complement
MK of K associated to Kashaev’s R-matrices, and gave a sketch proof of Volume conjecture.
Moreover, in [17], he explained a method to calculate the A-polynomial of K from the trian-
gulation of ∂MK in [16]. We hope to ﬁnd a geometrical interpretation of our method to obtain
the A-polynomial, comparing with Yokota’s method.
