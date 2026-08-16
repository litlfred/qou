---
doc_id: arxiv-0905.0228v4
doc_title: "A CURIOUS q-ANALOGUE OF HERMITE POL YNOMIALS"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-7
source_pdf: 0905.0228v4.pdf
source_sha256: 1744545d0f210949
doc_brief: "A CURIOUS q-ANALOGUE OF HERMITE POLYNOMIALS — Two well-known q-Hermite polynomials are the continuous and discrete q-Hermite polynomials."
---
2. The q-Hermite polynomials Hn(x, s |q) 4
3. The rescaled discrete q-Hermite polynomials II 7
4. Connection with q-Fibonacci polynomials and q-Lucas polynomials 12
5. Appendix 16
5.1. Some well-known facts 16
5.2. A second proof of Proposition 14 17
Acknowledgement 19
References 19
1. Introduction
There are many ways to construct Hermite polynomials. For ex ample, the normalized
Hermite polynomials Hn(x, s ) = sn/ 2Hn(x/ √s, 1) ( n ≥ 0) may be deﬁned by the recurrence
relation:
Hn+1(x, s ) = xHn(x, s ) − nsHn−1(x, s ), (1.1)
with initial values H0(x, s ) = 1 and H−1(x, s ) = 0. By induction, we have
Hn(x, s ) = ( x − sD)n · 1, (1.2)
where D = d
dx denotes the diﬀerentiation operator. It follows that
D Hn(x, s ) = nHn−1(x, s ). (1.3)
2000 Mathematics Subject Classiﬁcation. Primary 05A05, 05A15, 33C45; Secondary 05A10, 05A18, 34B24 .
Key words and phrases. Hermite polynomials, q-Hermite polynomials, Al-Salam-Chihara polynomials, Han -
kel determinants, Catalan numbers, matchings, Touchard-R iordan.
October 25, 2018.
1
They have the explicit formula (see [1, Chapter 6])
Hn(x, s ) =
n∑
k=0
( n
2k
)
(−s)k(2k − 1)!!xn−2k.
The ﬁrst terms are
1, x, −s + x2, −3sx + x3, 3s2 − 6sx2 + x4, 15s2x − 10sx3 + x5.
The Hermite polynomials are orthogonal with respect to the t he linear functional deﬁned by
the moments
µ n = 1√
2π
∫ ∞
−∞
xne−x2/ 2dx =
{
(n − 1)!! if n is even ,
0 otherwise .
In other words, the n-th moment µ n of the measure of the Hermite polynomials is the number
of the complete matchings on [ n] := {1, . . . , n }, i.e., µ 2n = (2n − 1)!! and µ 2n+1 = 0.
Consider the rescaled Hermite polynomials pn(z, x, s ) = Hn(z − x, −s) deﬁned by
pn+1(z, x, s ) = ( z − x)pn(z, x, s ) + snpn−1(z, x, s ) (1.4)
with initial values p0(z, x, s ) = 1 and p−1(z, x, s ) = 0. Let F be the linear functional on the
polynomials in z deﬁned by F(pn(z, x, s )) = δn, 0. Then, the moments F(zn) are again the
Hermite polynomials
F(zn) = (
√
−s)n
n∑
k=0
( n
k
)
(x/
√
−s)n−kµ k = Hn(x, s ). (1.5)
This is equivalent to say that the generating function of the Hermite polynomials Hn(x, s ) has
the following continued fraction expansion:
H(z, x, s ) =
∑
n≥0
Hn(x, s )zn = 1
1 − xz + sz2
1 − xz + 2sz2
1 − xz + 3sz2
. . .
. (1.6)
Several q-Hermite polynomials were introduced in the literature (se e [13, 9]). Two important
classes of orthogonal q-analogues of Hn(x, s ) are the continuous and the discrete q-Hermite I
polynomials, which are special cases of the Al-Salam-Chiha ra polynomials.
We ﬁrst introduce some standard q-notations. For n ≥ 1 let
[n] := [ n]q = 1 − qn
1 − q , [n]q! =
n∏
k=1
[k]q, [2n − 1]q!! =
n∏
k=1
[2k − 1]q,
and ( a; q)n = (1 − a)(1 − aq) · · · (1 − aqn−1) with ( a; q)0 = 1. The q-binomial coeﬃcient is
deﬁned by [ n
k
]
:=
[ n
k
]
q
= (q; q)n
(q; q)k(q; q)n−k
for 0 ≤ k ≤ n and zero otherwise.
2
Recall [8] that the Al-Salam-Chihara polynomials Pn(x; a, b, c ) satisfy the three term recur-
rence:
Pn+1(x; a, b, c ) = ( x − aqn)Pn(x; a, b, c ) − (c + bqn−1)[n]qPn−1(x; a, b, c ) (1.7)
with initial values P−1(x; a, b, c ) = 0 and P0(x; a, b, c ) = 1.
Deﬁnition 1. Let Fa,b,c be the linear functional on the polynomials in z which satisfy
Fa,b,c (Pn(z; a, b, c )) = δn, 0. (1.8)
Note that the continuous q-Hermite polynomials are
˜Hn(x, s |q) = Pn(x; 0, 0, s ) (1.9)
and are also the moments (see [8] and Proposition 16):
˜Hn(x, s |q) = Fx, −s, 0(zn). (1.10)
The discrete q-Hermite polynomials I are
˜hn(x, s ; q) = Pn(x; 0, (1 − q)s, 0). (1.11)
The discrete q-Hermite polynomials II are
˜
hn(x; q) = ( −i)n˜hn(ix, 1; q−1). (1.12)
Besides, as we will see in Section 4, the polynomials
hn(x, s ; q) := Pn(0; −x, 0, s ) (1.13)
are actually a rescaled version of ˜hn(x; q). The main purpose of this paper is to study another
q-analogue of Hermite polynomials.
Deﬁnition 2. The new q-Hermite polynomials are deﬁned by
Hn(x, s |q) := Fx, 0, −s(zn). (1.14)
The q-Hermite polynomials ˜Hn(x, s |q) have, amongst other facts,
(1) orthogonality with an explicit measure,
(2) an explicit 3-term recurrence relation,
(3) explicit expressions,
(4) a combinatorial model using matchings,
(5) are moments for other orthogonal polynomials,
(6) evaluable Hankel determinants because of (5),
(7) Jacobi continued fractions as generating functions bec ause of (5).
The new q-Hermite polynomials Hn(x, s |q) are not orthogonal, i.e., they do not have (1)
and (2). Instead they have a nice q-analogue of the operator formula (1.2) for the ordinary
Hermite polynomials (see Theorem 4), the coeﬃcients in Hn(x, s |q) appear in the inverse
matrix of the coeﬃcients in the continuous q-Hermite polynomials (cf. Theorem 5), they have
simple connection coeﬃcients with q-Lucas and q-Fibonacci polynomials (cf. Theorem 11). The
discrete q-Hermite polynomials hn(x, s ; q) also have (1)-(4), and we will show in Theorem 6 that
they are also moments. Moreover, the quotients of two consec utive polynomials hn(x, s ; q) (see
Eq.(3.21)) appear as coeﬃcients in the expansion of the S-co ntinued fraction of the generating
function of Hn(x, s |q)’s, which leads to a second proof of Theorem 4.
3
This paper is organized as follows: we prove the main propert ies of Hn(x, s |q) and hn(x, s ; q)
in Section 2 and Section 3, respectively. In Section 4 we shal l establish the connection of our
new q-Hermite polynomials with the q-Fibonacci and q-Lucas polynomials. This yields, in
particular, a generalization of Touchard-Riordan’s formu la for the moments of continuous q-
Hermite polynomials (cf. Proposition 14), ﬁrst obtained by Josuat-Verg` es [10]. Finally, in
Section 5, we recall some well-known facts about the general theory of orthogonal polynomials
and give another proof of the generalized Touchard-Riordan formula by using the orthogonality
of continuous q-Hermite polynomials.
2. The q-Hermite polynomials Hn(x, s |q)
By (1.8) the q-Hermite polynomials Hn(x, s |q) are the moments of the measure of the or-
thogonal polynomials Pn(z) satisfying the recurrence:
Pn+1(z) = ( z − xqn)Pn(z) + s[n]qPn−1(z). (2.1)
Recall [13, p.80] that the Al-Salam-Chihara polynomials Qn(x) := Qn(x; α, β ) satisfy the three
term recurrence:
Qn+1(x) = (2 x − (α + β )qn)Qn(x) − (1 − qn)(1 − αβq n−1)Qn−1(x), (2.2)
with Q0(x) = 1 and Q−1(x) = 0. They have the following explicit formulas:
Qn(x; α, β |q) = ( αe iθ; q)ne−iθ2φ 1
(
q−n, βe −iθ
α −1q−n+1e−iθ |q; α −1qeiθ
)
, (2.3)
where x = cos θ.
Comparing (2.1) and (2.2) we have Pn(z) = 1
(2a)n Qn(az; α, 0) with
a = 1
2
√
q − 1
s and α = x
√
q − 1
s . (2.4)
Using the known formula for Al-Salam-Chihara polynomials w e obtain
Pn(z) = 1
(2aα )n
n∑
k=0
(q−n; q)k
(q; q)k
qk
k−1∏
i=0
(1 + α 2q2i − 2qiaαz )
=
( s
x(q − 1)
) n n∑
k=0
(q−n; q)k
(q; q)k
( −q
s
) k k−1∏
i=0
(
(q − 1)qixz − s − (q − 1)q2ix2)
. (2.5)
The ﬁrst values of these polynomials are
P1(z) = z − x,
P2(z) = z2 − x(1 + q)z + (s + qx2),
P3(z) = z3 − x[3]qz2 + (2s + qs + q[3]qx2)z − (s + qs + q2s + q3x2)x.
A matching m of {1, 2, . . . , n } is a set of pairs ( i, j ) such that i < j and i, j ∈ [n]. Each pair
(i, j ) is called an edge of the matching. Let ed( m) be the number of edges of m, so n − 2ed(m)
is the number of unmatched vertices. Two edges ( i, j ) and ( k, l ) have a crossing if i < k < j < l
or k < i < l < j . Let cr( m) be the number of crossing numbers in the matching m. Using the
combinatorial theory of Viennot [17], Ismail and Stanton [8 , Theorem 6] gave a combinatorial
4
interpretation of the moments of Al-Salam-Chihara polynom ials. In particular we derive the
following result from [8, Theorem 6].
Lemma 3. The moments of the measure of the orthogonal polynomials {Pn(x)} are the gen-
erating functions for all matchings m of [n]:
Fx, 0, −s(zn) =
∑
m
xn−2ed(m)(−s)ed(m)q( ¸m)+cr(m), (2.6)
where c(m) = ∑
a−vertices |{edges i < j : i < a < j }| and the sum extends over all matchings
m of [n].
Let M (n, k ) be the set of matchings of {1, . . . , n } with k unmatched vertices. Then
Fx, 0, −s(zn) =
∑
k
c(n, k, q )xk(−s)
n−k
2 , (2.7)
where
c(n, k, q ) =
∑
m∈M (n,k )
qc(m)+cr(m). (2.8)
It is easy to verify that
c(n, k, q ) = c(n − 1, k − 1, q ) + [k + 1]qc(n − 1, k + 1, q ) (2.9)
with c(0, k, q ) = δk, 0 and c(n, 0, q ) = c(n − 1, 1, q ).
Indeed, if n is an unmatched vertex then for the restriction m0 of m to [ n − 1] we get
c(m0) = c(m) and cr( m0) = cr( m). If n is matched with m(n), such that there are i unmatched
vertices and j endpoints of edges which cross the edge ( m(n), n ) between m(n) and n, then
c(m) = c(m0) + i − j and cr( m) = cr( m0) + j. Thus c(m) + cr(m) = c(m0) + cr(m0) + i. Since
each i with 0 ≤ i ≤ k can occur we get (2.9).
Let now Dq be the q-derivative operator deﬁned by
Dqf (z) = f (z) − f (qz)
(1 − q)z .
We have then the following q-analogue of (1.2).
Theorem 4. The q-Hermite polynomials Hn(x, s |q), deﬁned as moments Fx, 0, −s(zn), have the
following operator formula:
Hn(x, s |q) = ( x − sDq)n1. (2.10)
Proof. We know that
Hn(x, s |q) =
∑
k
c(n, k, q )xk(−s)
n−k
2 , (2.11)
where c(n, k, q ) satisﬁes (2.9). Therefore
Hn(x, s |q) =
∑
k
c(n − 1, k − 1, q )xk(−s)
n−k
2 +
∑
k
[k + 1]qc(n − 1, k + 1, q )xk(−s)
n−k
2
= xHn−1(x, s |q) − sDqHn−1(x, s |q).
The result follows then by induction on n.
5
Remark. It should be noted that the method of Varvak [16] (see also [10 ]) can also be applied
to prove Theorem 4. In fact her method proves ﬁrst that ( x − sDq)n1 is a generating function
of some rook placements, which is then shown to count involut ions with respect to the statistic
( ¸m) + cr(m) (see [16, Theorem 6.4]). We will give another proof of (2.10 ) by using continued
fraction, see the remark after Theorem 8.
The ﬁrst terms of the sequence Hn(x, s |q) are
1, x, −s + x2, x (−(2 + q)s + x2), (2 + q)s2 − (3 + 2q + q2)sx2 + x4,
x((5 + 6q + 3q2 + q3)s2 − (4 + 3q + 2q2 + q3)sx2 + x4), . . .
Let
˜Hn(x, s |q) =
∑
k
b(n, k, q )xk(−s)
n−k
2 . (2.12)
Theorem 5. The matrices (c(i, j, q ))n−1
i,j =0 and (b(i, j, q )(−1)
i−j
2 )n−1
i,j =0 are mutually inverse.
Proof. We ﬁrst show by induction that
˜Hn(x + sDq, s |q)1 = xn. (2.13)
For this is obvious for n = 0. If it is already shown for n we get
˜Hn+1(x + sDq, s |q)1 = ( x + sDq) ˜Hn(x + sDq, s |q)1 − s[n]q ˜Hn−1(x + sDq, s |q)1
= (x + sDq)xn − s[n]qxn−1 = xn+1.
On the other hand we have
˜Hn(x + sDq, s |q)1 =
n∑
k=0
b(n, k, q )(−s)
n−k
2 (x + sDq)k1
=
n∑
k=0
b(n, k, q )(−s)
n−k
2
k∑
j=0
c(k, j, q )s
k−j
2 xj
=
n∑
j=0
s
n−j
2 xj
n∑
k=j
b(n, k, q )(−1)
n−k
2 c(k, j, q ). (2.14)
The result follows then by comparing (2.13) and (2.14).
Remark. If we set q = 0 then (2.9) reduces to the well-known Catalan triangle (se e [2, Chap.
7]), which implies
c(2n, 0, 0) = Cn = 1
n + 1
( 2n
n
)
,
c(2n, 2k, 0) = 2k + 1
n + k + 1
( 2n
n − k
)
=
( 2n
n − k
)
−
( 2n
n − k − 1
)
,
c(2n + 1, 2k + 1, 0) = 2k + 2
n + k + 2
( 2n + 1
n − k
)
=
( 2n + 1
n − k
)
−
( 2n + 1
n − k − 1
)
.
6
We shall use the standard q-notations in [6]. The recurrence (2.1) implies that the Han kel
determinants of Hn(x, s |q) are
det(Hi+j(x, s |q))n−1
i,j = (−s)(n
2)
n−1∏
j=0
[j]q! (2.15)
and
det(Hi+j+1(x, s ; q))n−1
i,j = hn(x, −s; q)(−s)(n
2)
n−1∏
j=0
[j]q!, (2.16)
where
hn(x, −s; q) = ( −1)nPn(0) =
( s
x(1 − q)
) n n∑
k=0
(q−n; q)k
(q; q)k
qk
k−1∏
i=0
(1 + x2(q − 1)q2i/s ).
