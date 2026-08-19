---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-022-8-growth-rates-of-r-matrices-and-the-lobachevsky
section_title: "Growth rates of R-matrices and the Lobachevsky function"
section_number: 8
pages: 18-19
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
8.1. The Lobachevsky function. In Section 6 we got a simple but crude estimate for the l1-norm of the
R-matrices, which are a ratio of ﬁve quantum factorials. In this large ly independent section we will give
reﬁned (and optimal) estimates for the growth rate of the R-matrices. These estimates reveal the close
relationship between hyperbolic geometry and the asymptotics of t he quantum factorials.
Recall that the Lobachevsky function is given by
Λ( z) = −
∫ z
0
log |2 sin x|dx = 1
2
∞∑
n=1
sin(2nz)
n2
The Lobachevsky function is an odd, periodic function with period π. Its graph for z ∈ [0, π] is:
0.5 1 1.5 2 2.5 3
-0.4
-0.2
0.2
0.4
Deﬁnition 8.1. If f (q) ∈ Z[q±1/ 4], let us denote by ev n(f ) the evaluation of f at q1/ 4 = eπi/ (2n).
For 0 ≤ k ≤ n we have
evn|{k}| = |ekπi/n − e−kπi/n | = 2 sin(kπ/n),
hence,
log(evn|({j}!|)|) =
j∑
k=1
log |2 sin(kπ/n)|,
which is very closely related to a Riemann sum of the integral in the deﬁ nition of the Lobachevsky function.
It is not surprising to have the following.
Proposition 8.2. For every α ∈ (0, 1) we have:
log |evn({⌊αn⌋}!)| = − n
π Λ( πα) + O(log n).
Here O(log n) is a term which is bounded by C log n for some constant C independent of α.
Remark 8.3. The proof reveals an asymptotic expansion of the form:
evn({⌊αn⌋}!) ∼ nθ exp
(
− n
π Λ( πα)
) (
C0 + C1
n + C2
n2 + . . .
)
for explicitly computable constants Ci and θ.
Proof. Recall the Euler-MacLaurin summation formula , with error term (see for example, [ Olv97, Chpt. 8]):
b∑
k=a
f (k) =
∫ b
a
f (x)dx + 1
2 f (a) + 1
2 f (b) +
m−1∑
k=1
B2k
(2k)! (f (2k−1)(b) − f (2k−1)(a)) + Rm(a, b, f)
where Bk is the kth Bernoulli number and the error term has an estimate
|Rm(a, b, f)| ≤ (2 − 21−2m) |B2m|
(2m)!
∫ b
a
|f (2m)(x)|dx.
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 19
Applying the above formula for m = 1 to f (x) = log(2 sin xπ/n), we have:
log(
⌊αn ⌋∏
k=1
2 sin(kπ/n)) = 1
2 (f (1) + f (⌊αn⌋)) +
∫ ⌊αn ⌋
1
log(2 sin(tπ/n))dt + R1(1, ⌊αn⌋, f)
= 1
2 (f (1) + f (αn) +
∫ αn
1
log(2 sin(tπ/n))dt + R1(1, ⌊αn⌋, f) + ǫ(α, n)
= 1
2 (f (1) + f (αn)) + n
π
∫ πα
π/n
log |2 sin(u)|u + R1(1, ⌊αn⌋, f) + ǫ(α, n)
= 1
2 (f (1) + f (αn)) + n
π
(
−Λ( πα) + Λ( π
n )
)
+ R1(1, ⌊αn⌋, f) + ǫ(α, n).
Here ǫ(α, n) comes from adjusting the boundary of integration and satisﬁes |ǫ(α, n)| = O(1). Note that
1
2 |f (1) + f (αn)| = O(log n).
Moreover, f ′′(x) = π 2
n2 (csc(πx/n))2 > 0. Hence
∫ ⌊αn ⌋
1
|f ′′(x)|dx =
∫ ⌊αn ⌋
1
f ′′(x)dx ≤
∫ αn
1
f ′′(x)dx = π
n
(
cot(απ) − cot
(π
n
))
.
It follows easily that
|R1(1, ⌊αn⌋, f)| = O(1).
Furthermore, using L’Hospital’s rule, one can see that
n
π
⏐
⏐
⏐Λ( π
n )
⏐
⏐
⏐ = O(log n).
The result follows. □
Corollary 8.4. For every α ∈ (0, 1) and any ﬁxed number d we have:
log |evn({⌊αn + d⌋}!)| = − n
π Λ( πα) + O(log n).
Proof. There is ε > 0 such that for big enough n, we have ε ≤ x/n ≤ 1 − ε for every integer x between
⌊αn⌋ and ⌊αn + d⌋. For such x, we have 0 < 2 sin επ < 2 sin(xπ/n) < 2, and hence there is a constant M
such that | log 2 sin(xπ/n)| < M . There are at most |d| + 1 such values of x. Hence the diﬀerence between
log |evn({⌊αn + d⌋}!)| and log |evn({⌊αn⌋}!)| by absolute value is less than ( |d|+ 1)M , a constant. The result
follows. □
