---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POL YNOMIALS"
section_id: sec-002-4-connection-with-q-fibonacci-polynomials-and-q
section_title: "Connection with q-Fibonacci polynomials and q-Lucas polynomials"
section_number: 4
pages: 12-16
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
We deﬁne the Lucas polynomials by
ln(x, s ) = xln−1(x, s ) + sln−2(x, s ) for n > 2,
with initial values l1(x, s ) = x and l2(x, s ) = x2 + 2s. They have the explicit formula
ln(x, s ) =
∑
2k≤n
n
n − k
( n − k
k
)
skxn−2k (n > 0). (4.1)
Furthermore we deﬁne l0(x, s ) = 1. Note that this deﬁnition diﬀers from the usual one in
which l0(x, s ) = 2.
The Fibonacci polynomials are deﬁned by
fn(x, s ) = xfn−1(x, s ) + sfn−2(x, s )
with f0(x, s ) = 0 and f1(x, s ) = 1. They have the explicit formula
fn(x, s ) =
⌊ n−1
2 ⌋∑
k=0
( n − 1 − k
k
)
skxn−1−2k. (4.2)
We ﬁrst establish the following inversion of (4.1) and (4.2) .
Lemma 10.
xn =
∑
2k≤n
( n
k
)
skln−2k(x, −s), (4.3)
xn =
∑
2k≤n+1
(( n
k
)
−
( n
k − 1
))
skfn+1−2k(x, −s). (4.4)
Proof. Recall the Tchebyshev inverse relations [15, p. 54-62]:
bn =
⌊ n
2 ⌋∑
k=0
(−1)k n
n − k
( n − k
k
)
an−2k ⇐ ⇒an =
⌊ n
2 ⌋∑
k=0
( n
k
)
bn−2k, (4.5)
where a0 = b0 = 1, and
bn =
⌊ n
2 ⌋∑
k=0
(−1)k
( n − k
k
)
an−2k ⇐ ⇒an =
⌊ n
2 ⌋∑
k=0
[( n
k
)
−
( n
k − 1
)]
bn−2k. (4.6)
We derive immediately (4.3) from (4.1) and (4.5). Clearly (4 .2) is equivalent to the left identity
in (4.6) with an =
(
x√s
) n
and bn = fn+1(x, −s)
(√s)n . By inversion we ﬁnd
xn =
⌊ n
2 ⌋∑
k=0
(( n
k
)
−
( n
k − 1
))
skfn+1−2k(x, −s). (4.7)
To see the equivalence of (4.4) and (4.7) we notice that
12
• if n is odd, then
( n
k
)
=
( n
k−1
)
for k =
⌊ n+1
2
⌋
,
• if n is even, then
⌊ n+1
2
⌋
=
⌊ n
2
⌋
.
Deﬁne the q-Lucas and q-Fibonacci polynomials by
Ln(x, s ) = ln(x + (q − 1)sDq, s ) · 1, (4.8)
Fn(x, s ) = fn(x + (q − 1)sDq, s ) · 1. (4.9)
It is known (see [3] and [4] ) that they have the explicit formu lae
Ln(x, s ) =
⌊ n
2 ⌋∑
k=0
q(k
2) [n]
[n − k]
[ n − k
k
]
skxn−2k, (4.10)
Fn(x, s ) =
⌊ n−1
2 ⌋∑
k=0
q(k+1
2 )
[ n − 1 − k
k
]
skxn−1−2k, (4.11)
for n > 0, with L0(x, s ) = 1 and F0(x, s ) = 0.
Theorem 11. We have
Hn(x, (q − 1)s|q) =
⌊ n
2 ⌋∑
k=0
( n
k
)
skLn−2k(x, −s) (4.12)
=
⌊ n+1
2 ⌋∑
k=0
(( n
k
)
−
( n
k − 1
))
skFn+1−2k(x, −s). (4.13)
Proof. Since
Ln(x, −s) = ln(x − (q − 1)sDq, s ) · 1,
Fn(x, −s) = fn(x − (q − 1)sDq, s ) · 1,
the theorem follows by applying the homomorphism x ↦→x − (q − 1)sDq to (4.3) and (4.4).
We derive some consequences of the formula (4.13).
Corollary 12. We have
Hn(1, q − 1|q) =
n∑
k=−n
(−1)kq
k(3k+1)
2
( n⌊ n−3k
2
⌋
)
=
n∑
k=0
(−1)kq
k(3k+1)
2
( n⌊ n−3k
2
⌋
)
+
n∑
k=1
(−1)kq
k(3k−1)
2
( n⌊ n−3k+1
2
⌋
)
.
(4.14)
Proof. Let r(k) = k(3k+1)
2 . Then, it follows from [3] that
F3n(1, −1) =
n−1∑
k=−n
(−1)kqr(k), F 3n+1(1, −1) = F3n+2(1, −1) =
n∑
k=−n
(−1)kqr(k),
13
or
Fn(1, −1) =
∑
−n≤3j≤n−1
(−1)jq
j(3j+1)
2 . (4.15)
Let w(n) = ∑ ⌊ n+1
2 ⌋
k=0
( ( n
k
)
−
( n
k−1
) )
Fn+1−2k(1, −1). Consider a ﬁxed term ( −1)jqr(j). This
term occurs in Fn(1, −1) if − n
3 ≤ j ≤ n−1
3 . We are looking for all k, such that this term
occurs in Fn+1−2k(1, −1). For j ≥ 0 the largest such number is k0 =
⌊
n−3j
2
⌋
. For j ≤ n−2k
3 is
equivalent with k ≤ k0. Therefore the coeﬃcient of ( −1)jqr(j) in w(n) is ∑ k0
k=0
( ( n
k
)
−
( n
k−1
) )
=
( n
k0
)
. For j < 0 we have − n+1−2k
3 ≤ j is equivalent with k ≤ ⌊ n+1−3j
2 ⌋. This gives the last sum
in (4.14).
Corollary 13. We have
H2n
(
1, q − 1
q |q
)
= q−n
n∑
j=−n
(( 2n
n − 3j
)
−
( 2n
n − 3j − 1
))
q2j(3j+1), (4.16)
and
H2n+1(1, q − 1
q |q) = q−n
n∑
j=−n
(( 2n + 1
n − 3j
)
−
( 2n + 1
n − 3j − 1
))
q2j(3j+2). (4.17)
Proof. Note that
H2n(1, q − 1
q |q) = 1
qn
n∑
k=0
(( 2n
n − k
)
−
( 2n
n − k − 1
))
qkF2k+1(1, − 1
q ), (4.18)
H2n+1(1, q − 1
q |q) = 1
qn
n+1∑
k=0
(( 2n + 1
n + 1 − k
)
−
( 2n + 1
n − k
))
qk−1F2k(1, − 1
q ). (4.19)
Recall (see [3]) that
F3n(1, − 1
q ) = 0 , F 3n+1(1, − 1
q ) = ( −1)nqr(n), F 3n+2(1, − 1
q ) = ( −1)nqr(−n). (4.20)
Hence
• if k = 3j then 2 k + 1 = 6 j + 1 and qkF2k+1(1, − 1
q ) = q3jF6j+1(1, − 1
q ) = q2j(3j+1).
• if k = 3j + 1 then 2 k + 1 = 6 j + 3 and qkF2k+1(1, − 1
q ) = 0.
• If k = 3j + 2 then 2 k + 1 = 6 j + 5 and qkF2k+1(1, − 1
q ) = q3j+2.
• if k = 3j then 2 k = 6j and qk−1F2k(1, − 1
q ) = 0.
• if k = 3j + 1 then 2 k = 6j + 2 and qk−1F2k(1, − 1
q ) = q2j(3j+2).
• If . k = 3j + 2 then 2 k = 6j + 4 and qk−1F2k(1, − 1
q ) = −q(3j+1)(2j+2).
Substituting the above values into (4.18) and (4.19) yields (4.16) and (4.17).
Finally, from (4.12) and (2.8) we derive two explicit formul ae for the coeﬃcient c(n, k, q ).
14
Proposition 14. If k ≡ n (mod 2) then
c(n, k, q ) =
∑
m∈M (n,k )
qc(m)+cr(m)
= (1 − q)− n−k
2
∑
j≥0
( n
n−k−2j
2
)
(−1)j q(j
2) [k + 2j]
[k + j]
[ k + j
j
]
(4.21)
= (1 − q)− n−k
2
∑
j≥0
(( n
n−k−2j
2
)
−
( n
n−k−2j−2
2
))
(−1)jq(j+1
2 )
[ k + j
k
]
. (4.22)
In the next section we shall give another proof by using the or thogonality of the continuous
q-Hermite polynomials. Some remarks about the above formula are in order.
(a) Formula (4.22) has been obtained with diﬀerent means by Jo suat-Verg` es [10, Propo-
sition 12] and is also used in [5]. It is easy to see that (4.21) and (4.22) are equal by
writing
[k + 2j]
[k + j] = qj + [j]
[k + j] .
(b) When k = 0, we recover a formula of Touchard-Riordan (see [2, 9, 14]) :
c(2n, 0, q ) =
∑
m∈M (2n, 0)
qcr(m) = 1
(1 − q)n
n∑
j=−n
( 2n
n + j
)
(−1)j q(j
2). (4.23)
(c) Notice that H2n(0, −1|q) = c(2n, 0, q ) and H2n+1(0, −1|q) = c(2n + 1, 0, q ) = 0. Hence
∑
n≥0
c(n, 0, q )tn = 1
1 − t2
1 − [2]qt2
1 − [3]qt2
1 − · · ·
.
We derive then a known result (see [9]): the coeﬃcient c(n, 0, q ) coincides with the n-th
moment of the continuous q-Hermite polynomials ˜H(x, 1|q), i.e.,
F(zn) = c(n, 0, q ),
where F is the linear functional on the polynomials in z deﬁned by F( ˜Hn(x, 1|q)) = δn, 0.
As in [11] we can derive another double sum expression for Hn(x, s |q). We omit the proof.
Proposition 15. We have
Hn(x, s |q) =
n∑
k=0
(−1)kq−(k
2)
k∑
i=0
( s
x(q − 1) q−i + xqi
) n
×
k∏
j=0,j ⁄=i
1
q−i − q−j + x2 q−1
s (qi − qj)
. (4.24)
15
