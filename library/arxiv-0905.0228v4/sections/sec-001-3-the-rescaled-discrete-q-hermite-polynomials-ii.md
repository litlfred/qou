---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POL YNOMIALS"
section_id: sec-001-3-the-rescaled-discrete-q-hermite-polynomials-ii
section_title: "The rescaled discrete q-Hermite polynomials II"
section_number: 3
pages: 7-12
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
By deﬁnition (1.13) and (1.7) we have
hn+1(x, s ; q) = qnxhn(x, s ; q) − [n]qshn−1(x, s ; q). (3.1)
We derive then
hn(x, s ; q) = q(n
2)√
sn˜hn
( x√s ; q
)
(3.2)
=
n∑
k=0
q(n−2k
2 )
[ n
2k
]
[2k − 1]q!!(−s)kxn−2k, (3.3)
where ˜hn(x; q) are the discrete q-Hermite polynomials II, see (1.13).
Since Dq(f g) = Dq(f )g + f (qx)Dq(g) and Dq(x) = 1, we see that
Dq(hn+1(x)) = qnxDq(hn(x)) + qnhn(qx) − [n]qsDq(hn−1(x)).
We derive by induction on n that
Dqhn(x, s ; q) = [ n]qhn−1(qx, s ; q). (3.4)
The ﬁrst terms of these polynomials are
1, x, qx 2 − s, q 3x3 − s[3]qx, q 6x4 − s(q5 + q4 + 2q3 + q2 + q)x2 + s2[3]q.
The following result shows that the polynomials hn(x, s ; q) are moments of some orthogonal
polynomials.
Theorem 6. The generating function of hn(x, s ; q) has the continued fraction expansion:
∑
m≥0
hn(x, s ; q)tn = 1
1 − b0t − λ 1t2
1 − b1t − λ 2t2
1 − b2t − λ 3t2
1 − . . .
,
7
with
bn = qn−1(qn + qn+1 − 1)x and λ n = −qn−1[n]q(s + q2n−2(1 − q)x2). (3.5)
Proof. To prove this it suﬃces to show that the Stieltjes tableau (5. 3) is satisﬁed with
a(n, k ) =
[ n
k
]
hn−k(qkx, s ; q).
This is easily veriﬁed.
This implies that their Hankel determinants are
det(hi+j(x, s ; q))n−1
i,j = (−1)(n
2)q(n
3)
n−1∏
j=0
(
[j]q!(s + q2j(1 − q)x2)n−1−j)
(3.6)
and
det(hi+j+1(x, s ; q))n−1
i,j
det(hi+j(x, s ; q))n−1
i,j
= w(n), (3.7)
where w(n) satisﬁes
w(n + 1) = qn−1(qn + qn+1 − 1)xw(n) + qn−1[n]q(s + q2n−2(1 − q)x2)w(n − 1).
It is easily veriﬁed that
w(n) =
n∑
k=0
q2(n−k
2 )
[ n
2k
]
[2k − 1]q!!skxn−2k (3.8)
satisﬁes the same recurrence with the same initial values.
Lemma 7. Let Ln(x) := hn(x, (1 − q)s; q). Then
sLn(x) + xLn+1(x) = ( x2 + s)Ln(qx). (3.9)
Proof. First we note that the constant terms of both sides of (3.9) ar e equal to sLn(0). So it
suﬃces to show that the derivatives of the two sides are equal . Applying Dq to (3.9) and using
(3.4) we obtain, after replacing x by x/q ,
s[n]Ln−1(x) + xq[n − 1]Ln(x) + Ln+1(x) = ( x2 + s)q[n]Ln−1(qx).
Since Ln+1(x) = qnxLn(x) − (1 − qn)sLn−1(x), we can rewrite the above equation as follows:
sLn−1(x) + xLn(x) = ( x2 + s)Ln−1(qx). (3.10)
The proof is thus completed by induction on n.
We shall prove the following Jacobi continued fraction expa nsion for the generating function
of ( x + (1 − q)sDq)n · 1. This is equivalent to Theorem 4.
8
Theorem 8. Let Tn(x, s ) = ( x + (1 − q)sDq)n · 1. Then
∑
n≥0
Tn(x, s )tn = 1
1 − b0t − λ 1t2
1 − b1t − λ 2t2
1 − . . .
, (3.11)
where the coeﬃcients are
bn = qnx, for n ≥ 0; and λ n = (1 − qn)s, for n ≥ 1. (3.12)
Proof. Since Tn(x, s ) = ( x + (1 − q)sDq)Tn−1(x, s ), we have
Tn(x, s ) = ( x + s
x )Tn−1(x, s ) − s
x Tn−1(qx, s ).
Equivalently the generating function G(x, t ) = ∑
n≥0 Tn(x, s )tn satisﬁes the functional equa-
tion: (
1 − x2 + s
x t
)
G(x, t ) = 1 − s
x tG(qx, t ). (3.13)
Suppose that
G(x, t ) = 1
1 − c1t
1 − c2t
1 − c3t
1 − . . .
, (3.14)
where cn = (gn − 1)gn−1A with A := A(x) = − x2+s
x and gi := gi(x).
Substituting (3.14) in (3.13) and then replacing t by t/A we obtain
1 + t
1 − (g1 − 1)t
1 − (g2 − 1)g1t
1 − (g3 − 1)g2t
1 − (g4 − 1)g3t
1 − . . .
= 1 +
s
x2+s t
1 − (g′
1 − 1) A′
A t
1 − (g′
2 − 1)g′
1
A′
A t
1 − (g′
3 − 1)g′
2
A′
A t
1 − . . .
, (3.15)
where A′ := A(qx) and g′
i := gi(qx). Comparing this with Wall’s formula (see [12]):
1 + z
1 − (g1 − 1)z
1 − (g2 − 1)g1z
1 − (g3 − 1)g2z
1 − (g4 − 1)g3z
1 − . . .
= 1 + g1z
1 − (g1 − 1)g2z
1 − (g2 − 1)g3z
1 − (g3 − 1)g4z
1 − . . .
, (3.16)
9
we derive that g0 = 1 and for n ≥ 1,







g2n = A′
A
g′
2n−1 − 1
g2n−1 − 1 g′
2n−2,
g2n+1 = A′
A
g′
2n − 1
g2n − 1 g′
2n−1.
(3.17)
For example,
g1 = s
x2 + s , g 3 = A′
A
g′
2 − 1
g2 − 1 g′
1 = s
x2 + s
1
q ,
g2 = A′
A
g′
1 − 1
g1 − 1 = q, g 4 = A′
A
g′
3 − 1
g3 − 1 g′
2 = −s + qs + q3x2
−s + qs + qx2 .
In general we have the following result.







g2n = sLn(x) + xLn+1(x)
(x2 + s)Ln(x) ,
g2n+1 = sLn(x)
sLn(x) + xLn+1(x) .
(n ≥ 0). (3.18)
This can be veriﬁed by induction on n. Suppose that the formula (3.18) is true for n ≥ 0. We
prove that the formula holds for n + 1. By (3.17) we have
g2n+2 = A′
A
g′
2n+1 − 1
g2n+1 − 1 g′
2n = sLn(x) + xLn+1(x)
(x2 + s)Ln+1(x)
Ln+1(qx)
Ln(qx) .
It follows from Lemma 1 that
g2n+2 = sLn+1(x) + xLn+2(x)
(x2 + s)Ln+1(x) . (3.19)
Since
Ln+1(x) − xLn(x) = ( qn − 1)(xLn(x) + sLn−1(x)), (3.20)
the veriﬁcation for g2n+3 is then straightforward. We derive from (3.14) and (3.18) th at







c2n = (g2n − 1)g2n−1A = (1 − qn)s Ln−1(x)
Ln(x) , for n ≥ 1;
c2n+1 = (g2n+1 − 1)g2nA = Ln+1(x)
Ln(x) , for n ≥ 0.
(3.21)
Invoking the contraction formula (see [19]), which transforms a S-continued fraction to a J-
continued fraction,
1
1 − c1z
1 − c2z
1 − c3z
1 − c4z
. . .
= 1
1 − c1z − c1c2z2
1 − (c2 + c3)z − c3c4z2
. . .
, (3.22)
10
we obtain






bn = hn+1(x, (1 − q)s; q)
hn(x, (1 − q)s; q) + (1 − qn)s hn−1(x, (1 − q)s; q)
hn(x, (1 − q)s; q) = qnx,
λ n = hn(x, (1 − q)s; ; q)
hn−1(x, (1 − q)s; q) · (1 − qn)s hn−1(x, (1 − q)s; ; q)
hn(x, (1 − q)s; ; q) = (1 − qn)s.
(3.23)
This completes the proof.
Remark. Instead of the contraction formula (3.22), we can also proce ed as follows. Deﬁne a
table ( A(n, k ))n,k ≥0 by
A(0, k ) = δk, 0,
A(n, 0) = c1A(n − 1, 1), (3.24)
A(n, k ) = A(n − 1, k − 1) + ck+1A(n − 1, k + 1).
In this case A(2n, 2k + 1) = A(2n + 1, 2k) = 0 for all n, k . If we deﬁne
a(n, k ) = A(2n, 2k),
then it is easily veriﬁed that a(n, k ) satisfy (5.3) with
b0 = c1, b n = c2n + c2n+1, λ n = c2nc2n−1. (3.25)
Substituting the values in (3.21) for cn we obtain (3.23). Therefore
∑
n
A(2n, 0)tn =
∑
n
a(n, 0)tn =
∑
n
Tn(x, s )tn.
As another application of this remark we prove the following result.
Proposition 9. Let wn(m, q ) = q
n((2m+1)n+1)
2 . Then
∑
m≥0
wn(m, q )tn = 1
1 − b0t − λ 1t2
1 − b1t − λ 2t2
1 − b2t − λ 3t2
1 − . . .
,
where
bn = q(2m+1)n−m(q(2m+1)n − 1) + q(2m+1)(2n+1)−m,
λ n = q(2m+1)(3n−1)−2m(q(2m+1)n − 1).
Proof. Let
A(2n, 2k) = wn(m, q )
wk(m, q )
[ n
k
]
q2m+1
and A(2n + 1, 2k + 1) = wn+1(m, q )
wk+1(m, q )
[ n
k
]
q2m+1
.
Then it is easily veriﬁed that the table (3.24) holds with c2n = q(2m+1)n−m(q(2m+1)n − 1) and
c2n+1 = q(2m+1)(2n+1)−m. Therefore
∑
n
A(2n, 0)tn =
∑
n
a(n, 0)tn =
∑
n
wn(m, q )tn.
11
