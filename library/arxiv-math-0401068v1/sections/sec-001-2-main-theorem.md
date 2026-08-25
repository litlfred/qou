---
doc_id: arxiv-math-0401068v1
doc_title: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS"
section_id: sec-001-2-main-theorem
section_title: "Main Theorem"
section_number: 2
pages: 2-6
source_pdf: 0401068v1.pdf
source_sha256: 8168d7e7f6069978
doc_brief: "THE COLORED JONES POLYNOMIAL AND THE A-POLYNOMIAL FOR TWIST KNOTS — @We show that for a twist knot, the A-polynomial can be obtained fr om recur- rences for the summand in Masbaum’s formula of the"
---
prove Theorem 2.2. In Section 4, we relate our result to the AJ conj ecture and give a result
about recursive relations of the Jones polynomials for the knots 5 2 and 6 1.
The author would like to thank Y. Yokota for helpful conversation.
2. Main Theorem
We start with the review of the deﬁnition of the A-polynomial of a knot K in S3 (see [1] ). Let
MK be the complement of K and R(MK) the set of all representations of π1(MK) into SL(2, C).
The set R(MK) is an aﬃne algebraic variety. Noting that SL(2, C) acts on representations by
conjugation, we restrict our attention to the subset RU of R(MK) consisting of a represetation
ρ satisfying that ρ(µ) and ρ(λ) are upper triangular matirices for the meridian µ and the
preferred longitude λ of K. We can deﬁne a projection ξ from RU to C2 by ξ(ρ) = ( l, m ) for
ρ ∈ R(MK) with
ρ(µ) =
(
m ∗
0 m−1
)
, ρ (λ) =
(
l ∗
0 l−1
)
.
The Zariski closure of ξ(RU ) has a structure of an algebraic variety in C2 and each of its
irreducible complex-dimension-one components is a curve, which is de ﬁned by a polynomial
with integer coeﬃcients in l and m. The A-polynomial is the product of those deﬁning poly-
nomials. We note that the A-polynomial of K has a factor l − 1, which correponds to abelian
representations. So, we denote by AK(l, m ) the A-polynomial divided by l − 1.
Nextly, we recall Masbaum’s formula of the colored Jones polynomial for a twist knot. Some
notations are ﬁxed.
{n} = sn − s−n, s 2 = q,
{n}! = {n}{n − 1} · · · {1}, (q)n = (1 − q)(1 − q2) · · · (1 − qn).
Let JK(n) be the colored Jones polynomial of a 0-framing knot K colored with the n-
dimensional irreducible representation of sl2(C), where JK(n) is normalized by J© (n) = 1
for the trivial knot © . ( J ′
K(n) in [8] is equal to JK(n) in this paper.)
Let Kp be the twist knot drawn in ﬁgure 1. In [8], Masbaum obtained the follow ing formula
for the colored Jones polynomial of the twist knot Kp.
Theorem 2.1. [8] The colored Jones polynomial of the twist knot Kp is given by
(1) JKp(n) =
∞∑
k=0
CKp(k) {n − k}{n − k + 1} · · · {n + k}
{n} ,
where
(2) CKp(k) = ( −1)k+1sk(k+3)/ 2
k∑
l=0
(−1)lql(l+1)p{2l + 1} {k}!
{k + l + 1}!{k − l}! .
2
We make use of the rearranged Masbaum’s formula ([4])
JKp(n) =
∞∑
k=0
k∑
l=0
(−1)k+1qk(k+3)/ 2qnk (q−1)n+k(q−1)n−1
(q−1)n(q−1)n−k−1
×(−1)lql(l+1)p+l(l−1)/ 2(q2l+1 − 1) (q)k
(q)k+l+1(q)k−l
.
Let us put
F (n, k, l )
= (−1)k+1qk(k+3)/ 2qnk (q−1)n+k(q−1)n−1
(q−1)n(q−1)n−k−1
(−1)lql(l+1)p+l(l−1)/ 2(q2l+1 − 1) (q)k
(q)k+l+1(q)k−l
.
Then, it easily follows that
f0(q, q n, q k, q l) := F (n + 1, k, l )
F (n, k, l ) = qk (1 − q−n−k−1)(1 − q−n)
(1 − q−n−1)(1 − q−n+k) ,(3)
f1(q, q n, q k, q l) := F (n, k + 1, l )
F (n, k, l ) = −qk+n+2 (1 − q−n−k−1)(1 − q−n+k+1)(1 − qk)
(1 − qk+l+2)(1 − qk−l+1) ,(4)
f2(q, q n, q k, q l) := F (n, k, l + 1)
F (n, k, l ) = −q(2p+1)l+2p (q2(l+1)+1 − 1)(1 − qk−l)
(q2l+1 − 1)(1 − qk+l+2) .(5)
We obtain the following result.
Theorem 2.2. From the three equations
f0(1, m 2, x, y ) = l, f 1(1, m 2, x, y ) = 1 , f 2(1, m 2, x, y ) = 1 ,
we can obtain
x = lm2 + 1
m2 + l , (y + 1)(1 − x)yphp(m, x ) = 0 ,
where hp(m, x ) is an element in Z[m±1, x ] and satisﬁes that if we put
BKp(l, m ) :=
{
(m2 + l)2p−1(m2)php(m, lm2+1
m2+l ), p > 0,
(m2 + l)2|p|(m2)|p|hp(m, lm2+1
m2+l ), p ≤ 0,
then, BKp(l, m ) = AKp(l, m ).
3. Proof of Theorem 2.2
Let Kp be the twist knot pictured in Figure 1. To prove Theorem 2.2, we use t he following
formula for the A-polynomial of the twist knot Kp due to Hoste and Shanahan in [5].
Theorem 3.1. (Hoste-Shanahan [5]) For p ⁄= −1, 0, 1, 2, AKp(l, m ) is given recusively by
(6) AKp(l, m ) =
{
cAKp− 1(l, m ) − dAKp− 2(l, m ), p > 0,
cAKp+1(l, m ) − dAKp+2(l, m ), p < 0,
where
c = −l + l2 + 2lm2 + m4 + 2lm4 + l2m4 + 2lm6 + m8 − lm8,
d = m4(l + m2)4,
3
p full twists
Figure 1
and with initial conditions
AK2(l, m ) = −l2 + l3 + 2l2m2 + lm4 + 2l2m4 − lm6 − l2m8
+2lm10 + l2m10 + 2lm12 + m14 − lm14,
AK1(l, m ) = l + m6,
AK0(l, m ) = 1 ,
AK− 1(l, m ) = −l + lm2 + m4 + 2lm4 + l2m4 + lm6 − lm8.
Now, we give a proof of Theorem 2.2.
Proof of Theorem 2.2 From the ﬁrst equation
f0(1, m 2, x, y ) = x(1 − 1
xm2 )
(1 − x
m2 ) = l,
we get
x = lm2 + 1
m2 + l .
Moreover, the second equation
f1(1, m 2, x, y ) = −xm2 (1 − 1
xm2 )(1 − x
m2 )(1 − x)
(1 − xy)(1 − x
y ) = 1
gives
(7) y2 + 1 = y
m2 (m4 − xm4 + x2m2 + m2 + 1 − x).
It is clear that the claim for p = 0 holds. We consider the case p > 0. The third equation
f2(1, m 2, x, y ) = −y2p+1 (1 − x
y )
(1 − xy) = 1
implies that
(8) y2p+1 + 1 − y2px − xy = 0,
which can be changed to
0 = ( y + 1)(y2p − y2p−1 + y2p−2 − · · · + 1 − xy(y2p−2 − y2p−3 + · · · + 1))
= ( y + 1){(y2 + 1 − (1 + x)y)(y2(p−1) + y2(p−2) + · · · + y2 + 1)
4
−(1 − x)(y2(p−1) + y2(p−2) + · · · + y2)}.
From the equation (7), we can get
(9) ( y + 1)(1 − x)Hp(m, x, y ) = 0 ,
where H0(m, x, y ) = 1 and for p ≥ 1,
Hp(m, x, y )
= y
m2 (m4 − xm2 + 1)(y2(p−1) + y2(p−2) + · · · + y2 + 1) − (y2(p−1) + y2(p−2) + · · · + y2).
To prove the theorem for p > 0, we need
Lemma 3.2. We have Hp(m, x, y ) = yphp(m, x ), where for p ≥ 2, hp(m, x ) is given recursively
by
(10) hp(m, x ) = a
m2 hp−1(m, x ) − hp−2(m, x )
with a = m4 − xm4 + x2m2 + m2 + 1 − x, h0(m, x ) = 1 , h1(m, x ) = b
m2 , and b = m4 − xm2 + 1.
Proof of lemma 3.2 We show by induction on p. When p = 1, it follows that H1(m, x, y ) =
y
m2 (m4 − xm2 + 1) = yh1(m, x ). In the case p = 2, we obtain that
H2(m, x, y ) = H1(m, x, y ) + yb
m2 y2 − y2
= yh1(m, x ) + y3h1(m, x ) − y2
= y(h1(m, x )(y2 + 1) − y)
= y( ay
m2 h1(m, x ) − y)
= y2( a
m2 h1(m, x ) − 1)
= y2( a
m2 h1(m, x ) − h0(m, x )).
Here we used the equation (7) in the fourth equality. Suppose that it holds for p ≤ n. By
hypothesis of induction and the deﬁnition of Hp(m, x, y ), we can obtain
Hn+1(m, x, y ) = Hn(m, x, y ) + yb
m2 y2n − y2n
= ynhn(m, x, y ) + y2( yb
m2 y2(n−1) − y2(n−1))
= ynhn(m, x, y ) + y2(Hn(m, x, y ) − Hn−1(m, x, y ))
= ynhn(m, x, y ) + y2(yn(hn(m, x, y ) − yn−1hn−1(m, x, y ))
= yn((y2 + 1)hn(m, x, y ) − yhn−1(m, x, y ))
= yn( a
m2 yhn(m, x, y ) − yhn−1(m, x, y ))
= yn+1( a
m2 hn(m, x, y ) − hn−1(m, x, y )).
This completes the proof. □
5
Let us go back to the proof of the theorem. From Lemma 3.2, it is clea r that hp(m, x ) is in
Z[m±1, x ]. We put
(11) BKp(l, m ) := ( m2 + l)2p−1(m2)php(m, lm2 + 1
m2 + l ),
and then, it is easy to see that BKp(l, m ) satisﬁes the recursive relation
(12) BKp(l, m ) = a(m2 + l)2BKp− 1(l, m ) − m4(m2 + l)4BKp− 2(l, m ).
By comparing it with the recursive relation (6) of AKp(l, m ) by Hoste and Shanahan, and by
noting that a(m2 + l)2 = −l + l2 + 2lm2 + m4 + 2lm4 + l2m4 + 2lm6 + m8 − lm8 = c and
d = m4(m2 + l)4, it is shown that BKp(l, m ) = AKp(l, m ) for p ≥ 0. In a similar way to the
case p ≥ 0, we can prove the theorem in the case p < 0. □
