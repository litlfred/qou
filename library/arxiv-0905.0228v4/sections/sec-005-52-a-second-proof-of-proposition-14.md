---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POL YNOMIALS"
section_id: sec-005-52-a-second-proof-of-proposition-14
section_title: "A second proof of Proposition 14"
section_number: 5.2
pages: 17-19
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
Theorem 5 and the orthogonality of the continuous q-Hermite polynomials. Clearly Theorem 5
is equivalent to
xn =
∑
k≡n (mod 2)
c(n, k, q )s(n−k)/ 2 ˜Hk(x, s |q). (5.14)
To compute c(n, k, q ) we can take s = 1 and let ˜Hn(x|q) = ˜Hn(x, s |q). It is known (see [9])
that the continuous q-Hermite polynomials ( ˜Hn(x|q)) are orthogonal with respect to the linear
functional ϕ deﬁned by
ϕ (xn) =
∫ 2/ √1−q
−2/ √1−q
xnv(x, q )dx, (5.15)
where
v(x, q ) =
√
(1 − q)(q)∞√
1 − (1 − q)x2/ 44π
∞∏
k=0
{1 + (2 − (1 − q)x2)qk + q2k}.
17
Since ϕ (( ˜Hk(x|q))2) = [ k]q!, it follows from (5.14) that, for k ≡ n (mod 2),
c(n, k, q ) = 1
[k]q! ϕ (xn ˜Hk(x|q)). (5.16)
Recall the well-known formula (see [9])
x2n =
n∑
j=−n
( 2n
n + j
)
T2j(x/ 2), (5.17)
where Tn(cos θ) = cos( nθ) = T−n(cos θ) is the nth Chybeshev polynomial of the ﬁrst kind. By
using the Jacobi triple product formula and the terminating q-binomial formula, we can prove
(see [7, p. 307]) that, for any integer j and a = √1 − q,
ϕ (Tn−2j(ax/ 2) ˜Hn(x|q)) = (−1)n+j
2an q(n−j
2 ){(q−n+j+1; q)n + qn−j(q−n+j; q)n}. (5.18)
It follows from (5.16), (5.17) and (5.18) that
c(2n, 2k, q ) = a−2n
[2k]q!
n∑
j=−n
( 2n
n + j
)
ϕ (T2j (ax/ 2) ˜H2k(x|q))
= (1 − q)−(n−k)
(q; q)2k
n∑
j=−n
( 2n
n + j
) (−1)k+j
2 q(k+j
2 ){(q−k−j+1; q)2k + qk+j(q−k−j; q)2k}
(5.19)
Since ( q−k−j+1; q)2k is zero if j ⁄= −n, . . . , −k and j ⁄= k + 1, . . . , n , and ( q−k−j; q)2k is zero if
j ⁄= −n, . . . , −k − 1 or j ⁄= k, . . . , n , we can split the last summation into the following four
summations:
S1 =
−k∑
j=−n
( 2n
n + j
) (−1)k+j
2 q(k+j
2 )(q−k−j+1; q)2k,
S2 =
n∑
j=k+1
( 2n
n + j
) (−1)k+j
2 q(k+j
2 )(q−k−j+1; q)2k,
S3 =
−k−1∑
j=−n
( 2n
n + j
) (−1)k+j
2 q(k+j
2 )qk+j(q−k−j; q)2k,
S4 =
n∑
j=k
( 2n
n + j
) (−1)k+j
2 q(k+j
2 )qk+j(q−k−j; q)2k.
It is readily seen, by replacing j by −j in S1 and S3, that S1 = S4 and S2 = S3. Therefore,
c(2n, 2k, q ) = (1 − q)−(n−k)
(q; q)2k
(S2 + S4)
= (1 − q)−(n−k) ∑
j≥0
( 2n
n + k + j
)
(−1)j q(j
2) [2k + 2j]
[2k + j]
[ 2k + j
j
]
. (5.20)
18
This corresponds to (4.21) for even indices. To derive the fo rmula for odd indices we can use
(2.9) to get
c(2n + 1, 2k + 1, q ) = [2 k + 2]qc(2n, 2k + 2, q ) + c(2n, 2k, q ),
and then apply (5.20).
