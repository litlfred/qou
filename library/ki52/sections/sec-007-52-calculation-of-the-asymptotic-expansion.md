---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-007-52-calculation-of-the-asymptotic-expansion
section_title: "Calculation of the asymptotic expansion"
section_number: 5.2
pages: 30-36
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Calculation of the asymptotic expansion
In this section, we show some lemmas used in the proof of Theorem 1.1.
Let (t0, s0) and (tc, sc) be the critical points of ˆV (t, s) and V (t, s) given in the previous
section. We put x0 = e2π√−1 ·t0, y0 = e2π√−1 ·s0 and xc = e2π√−1 ·tc, yc = e2π√−1 ·sc. In
order to show Lemma 5.2 below, we calculate (xc, yc) in terms of (x0, y0), as follows. We
show a proof of the following lemma in Appendix C.
Lemma 5.1. We can put xc = x0 + x1ℏ+ O(ℏ2) and yc = y0 + y1ℏ+ O(ℏ2) for some
x1, y1 ∈C in a suﬃciently small neighborhood of (x0, y0) (i.e., for suﬃciently large N).
Here, O(ℏ2) means that the absolute value of the error term is bounded by Cℏ2 with a
constant C which is independent of N.
We calculate x1 and y1, as follows. We put x = e2π√−1 ·t and y = e2π√−1 ·s. From the
deﬁnition of V (t, s) and Proposition A.1, we have that
∂
∂tV (t, s) = −log
(
1 −1
x
)
−2π
√
−1
(
t + s −1
2 −1
2N
)
+ O(ℏ2),
∂
∂sV (t, s) = −2 log
(
1 −1
y
)
−2π
√
−1
(
t + 2s −1 −1
2N
)
+ O(ℏ2).
(50)
Then, since (tc, sc) is a critical point of V (t, s), we have that







(
1 −1
xc
)
(−q−1/2xcyc) = 1 + O(ℏ2),
(
1 −1
yc
)2q−1/2xcy2
c = 1 + O(ℏ2).
These are rewritten,
{
(1 −xc)yc = q1/2 + O(ℏ2),
q1/2yc = (yc −1)2(yc −q1/2) + O(ℏ2).
Hence, putting xc = x0 + x1ℏ+ O(ℏ2) and yc = y0 + y1ℏ+ O(ℏ2) by Lemma 5.1, we have
that



x0 = 1 −1
y0
,
y0 = (y0 −1)3,





−
x1
1 −x0
+ y1
y0
= 1
2 ,
y1 + 1
2y0 = (y0 −1)2(
3y1 −1
2
)
.
Therefore, we obtain that
y1 =
y2
0
2(2y0 + 1),
x1 = −
y0 + 1
2y0(2y0 + 1).
30
Further, in order to show Lemmas 5.2, 5.3 and 5.4 below, we calculate the expansion
(48) concretely, as follows. Putting ˇt = t −tc, we expand φ(1 −t)/N at tc as follows,
φ(1−t)
N
= φ(1−tc)
N
−φ′(1−tc)
N
ˇt+1
2
φ′′(1−tc)
N
ˇt2−1
6
φ(3)(1−tc)
N
ˇt3+ 1
24
φ(4)(1−tc)
N
ˇt4+· · · ,
where we can calculate φ(k)(1 −tc)/N concretely by Proposition A.1. Hence, putting
ˇt = t −tc and ˇs = s −sc, we can show by concrete calculation that V (t, s) is expanded at
a critical point (tc, sc) in the following form,
V (t, s) = V (tc, sc)+(degree 2 part)+(degree 3 part)+(degree 4 part)+(degree ≥5 part),
(51)
where
(degree 2 part) = 2π
√
−1
( ˇt2
2
1
1 −xc
+ ˇs2
2
1 + yc
1 −yc
−(ˇt + ˇs)2
2
)
+ O(ℏ2),
(52)
(degree 3 part) = (2π
√
−1)2 (y0 −1)
( ˇt3
6 · y0 + ˇs3
6 · 2
)
+ O(ℏ),
(53)
(degree 4 part) = (2π
√
−1)3( ˇt4
24 (x2
0 + x0)y3
0 −ˇs4
24 2(y0 + 1)
)
+ O(ℏ).
(54)
Now, we show lemmas used in the proof of Theorem 1.1.
Lemma 5.2. Under the notation in the proof of Theorem 1.1,
exp
(
N V (tc, sc)
)
= eNς e−π√−1/4(
1 −y0
)1/2(
1 + (C1 + C2)ℏ+ O(ℏ2)
)
,
where we put
C1 =
1
184(−16y2
0 + 33y0 + 9),
C2 =
1
24(2y2
0 −5y0).
Proof. We put tc = t0 +t1/N +· · · and sc = s0 +s1/N +· · · . Recalling that xc = e2π√−1 ·tc
and yc = e2π√−1 ·sc, we have that
t1 = x1
x0
= −
y0 + 1
2(y0 −1)(2y0 + 1),
s1 = y1
y0
=
y0
2(2y0 + 1).
Putting ˇt = −t1/N and ˇs = −s1/N in the degree 2 part (52) of the expansion (51), we
have that
V (t0, s0) = V (tc, sc) + 2π
√
−1
( t2
1
2N 2
1
1 −x0
+ s2
1
2N 2
1 + y0
1 −y0
−(t1 + s1)2
2N 2
)
+ O(ℏ3).
Hence,
N V (tc, sc) = N V (t0, s0) + C1ℏ+ O(ℏ2),
31
where we put
C1 = −1
2
(
t2
1
1
1 −x0
+ s2
1
1 + y0
1 −y0
−(t1 + s1)2)
=
1
184(−16y2
0 + 33y0 + 9).
Hence,
exp
(
N V (tc, sc)
)
= exp
(
N V (t0, s0)
)
·
(
1 + C1ℏ+ O(ℏ2)
)
.
(55)
Further, we calculate V (t0, s0), as follows. From the deﬁnition of V (t, s), we have that
V (t0, s0) =
1
N
(
−φ(1 −t0) −2 φ(1 −s0)
)
−
1
2π√−1
π2
6
−2π
√
−1
(1
2
(
t0 + s0 −1
2N
)2 + 1
2s2
0 −1
2t0 −s0 + 1
6
)
−3π√−1
4N
+ π√−1
4N 2 .
Since this goes to ˆV (t0, s0) as N →∞, we have that
ˆV (t0, s0) =
1
2π√−1
(
−Li2
( 1
x0
)
−2 Li2
( 1
y0
)
−π2
6
)
−2π
√
−1
(1
2(t0 + s0)2 + 1
2s2
0 −1
2t0 −s0 + 1
6
)
=
1
2π√−1
(
Li2(x0y0) + Li2
( 1
x0y0
)
+ Li2(y0) −Li2
( 1
y0
)
−Li2
( 1
x0
)
−π2
6
)
= ς.
Hence, by Proposition A.1,
V (t0, s0) = ς + 2π
√
−1 t0 + s0
2N
−3π√−1
4N
+ 2π√−1
N 2
(
1
24(x0−1) +
1
12(y0−1)
)
+ O
( 1
N 3
)
.
Therefore,
exp
(
N V (t0, s0)
)
= eNςe−3
4 π√−1 (
x0y0
)1/2(
1 + C2ℏ+ O(ℏ2)
)
= eNςe−π√−1/4 (
1 −y0
)1/2(
1 + C2ℏ+ O(ℏ2)
)
,
where we put
C2 =
1
24(x0 −1) +
1
12(y0 −1) =
1
24(2y2
0 −5y0).
Hence, from the above formula and (55), we obtain the required formula.
Lemma 5.3. Under the notation in the proof of Theorem 1.1,
VttVss −V 2
ts = −4π2(−2y0 −1)
(
1 −2C3ℏ+ O(ℏ2)
)
,
(VttVss −V 2
ts)−1/2 =
1
2π√−1
(
−2y0 −1
)−1/2(
1 + C3ℏ+ O(ℏ2)
)
,
where we put
C3 =
1
46
(
8y2
0 −17y0 + 9
)
.
32
Proof. From the degree 2 part (52) of the expansion (51), we have that
Vtt = ∂2V
∂t2 (tc, sc) = 2π
√
−1
(
1
1 −xc
−1
)
+ O(ℏ2) = 2π
√
−1 ·
xc
1 −xc
+ O(ℏ2),
Vts =
∂2V
∂t ∂s(tc, sc) = −2π
√
−1 + O(ℏ2),
Vss = ∂2V
∂s2 (tc, sc) = 2π
√
−1
(1 + yc
1 −yc
−1
)
+ O(ℏ2) = 2π
√
−1 ·
2yc
1 −yc
+ O(ℏ2)
Hence,
VttVss −V 2
ts = −4π2(
xc
1 −xc
·
2yc
1 −yc
−1
)
+ O(ℏ2)
= −4π2(2q−1/2xcy2
c
1 −yc
−1
)
+ O(ℏ2)
= −4π2(
−2yc · 1 −q−1/2yc
1 −yc
−1
)
+ O(ℏ2)
= −4π2(
−yc
(
2 +
y0
1 −y0
ℏ
)
−1
)
+ O(ℏ2)
= −4π2(−2y0 −1)
(
1 −
y2
0(y0 + 2)
(y0 −1)(2y0 + 1)2 ℏ
)
+ O(ℏ2)
= −4π2(−2y0 −1)
(
1 −2C3ℏ
)
+ O(ℏ2),
where
C3 =
y2
0(y0 + 2)
2(y0 −1)(2y0 + 1)2 =
1
46
(
8y2
0 −17y0 + 9
)
.
Therefore, we obtain the required formulas.
Lemma 5.4. Under the notation in the proof of Theorem 1.1,
λ1 = C4 + C5 ,
where we put
C4 =
1
92(2y2
0 + 15y0),
C5 = −
1
3174(197y2
0 + 127y0 + 227).
Proof. We show the lemma by using Proposition 3.5. As shown in Proposition 3.5, λ1
consists of two contributions from the degree 3 part and the degree 4 part of the expansion
(51).
We calculate the contribution from the degree 4 part of the expansion (51), as follows.
As in (54), the degree 4 part of this expansion is given by
(2π
√
−1)3( ˇt4
24 (x2
0 + x0)y3
0 −ˇs4
24 2(y0 + 1)
)
+ O(ℏ).
(56)
33
As explained in Proposition 3.5, the contribution from ˇt4 is calculated as
N ·
( ∂
∂u1
)4 exp
(
−1
4N
(
u1
u2
)T
A−1
(
u1
u2
) )

u1=u2=0
= 1
2N ·
( ∂
∂u1
)4
(
−1
2N
(
u1
u2
)T(
Vtt
Vts
Vts
Vss
)−1 (
u1
u2
) )2
=
1
8N (VttVss −V 2
ts)2
( ∂
∂u1
)4(
Vssu2
1 −2Vtsu1u2 + Vttu2
2
)2
=
1
8N (VttVss −V 2
ts)2 · 4! · V 2
ss
=
4!
8N (2π√−1)2 (2y0 + 1)2
( 2y0
1 −y0
)2 + O(ℏ),
by using Lemma 5.3 and formulas in the proof of Lemma 5.3. Similarly, the contribution
from ˇs4 is calculated as
1
8N (VttVss −V 2
ts)2
( ∂
∂u2
)4(
Vssu2
1 −2Vtsu1u2 + Vttu2
2
)2
=
1
8N (VttVss −V 2
ts)2 · 4! · V 2
tt
=
4!
8N (2π√−1)2 (2y0 + 1)2
(
x0
1 −x0
)2 + O(ℏ).
Hence, the contribution from (56) is equal to
2π√−1
8N (2y0 + 1)2
(
(x2
0 + x0)y3
0
( 2y0
1 −y0
)2 −2(y0 + 1)
(
x0
1 −x0
)2)
= C4ℏ,
where we put
C4 =
1
8(2y0 + 1)2
(
(x2
0 + x0)y3
0
( 2y0
1 −y0
)2 −2(y0 + 1)
(
x0
1 −x0
)2)
=
1
92(2y2
0 + 15y0).
We calculate the contribution from the degree 3 part of the expansion (51), as follows.
As in (53), the degree 3 part of this expansion is given by
(2π
√
−1)2 (y0 −1)
( ˇt3
6 · y0 + ˇs3
6 · 2
)
+ O(ℏ),
and, hence, the corresponding degree 6 part is given by
1
2 (2π
√
−1)4 (y0 −1)2( ˇt3
6 · y0 + ˇs3
6 · 2
)2
+ O(ℏ)
= 1
2 (2π
√
−1)4 (y0 −1)2( ˇt6
62 · y2
0 + ˇs6
62 · 4 +
ˇt3ˇs3
62 · 4y0
)
+ O(ℏ).
(57)
34
The contribution from ˇt6 is calculated as
N 2 ·
( ∂
∂u1
)6 exp
(
−1
4N
(
u1
u2
)T
A−1
(
u1
u2
) )

u1=u2=0
= 1
6N 2 ·
( ∂
∂u1
)6
(
−1
2N
(
u1
u2
)T(
Vtt
Vts
Vts
Vss
)−1 (
u1
u2
) )3
=
−1
48N (VttVss −V 2
ts)3
( ∂
∂u1
)6(
Vssu2
1 −2Vtsu1u2 + Vttu2
2
)3
=
−1
48N (VttVss −V 2
ts)3 · 6! · V 3
ss
=
6!
48N (2π√−1)3 (2y0 + 1)3
( 2y0
1 −y0
)3 + O(ℏ),
by using Lemma 5.3 and formulas in the proof of Lemma 5.3. Similarly, the contribution
from ˇs6 is calculated as
−1
48N (VttVss −V 2
ts)3
( ∂
∂u2
)6(
Vssu2
1 −2Vtsu1u2 + Vttu2
2
)3
=
−1
48N (VttVss −V 2
ts)3 · 6! · V 3
tt
=
6!
48N (2π√−1)3 (2y0 + 1)3
(
x0
1 −x0
)3 + O(ℏ).
Similarly, the contribution from ˇt3ˇs3 is calculated as
−1
48N (VttVss −V 2
ts)3
( ∂
∂u1
)3( ∂
∂u2
)3(
Vssu2
1 −2Vtsu1u2 + Vttu2
2
)3
=
−1
48N (VttVss −V 2
ts)3 · 6! ·
(2
5(−Vts)3 + 3
5VttVss(−Vts)
)
+ O(ℏ)
=
6!
48N (2π√−1)3 (2y0 + 1)3
(2
5 + 3
5
x0
1 −x0
2y0
1 −y0
)
,
by using Lemma 5.3 and formulas in the proof of Lemma 5.3. Hence, the contribution
from (57) is equal to
5 · 2π√−1 (y0 −1)2
24N (2y0 + 1)3
(
y2
0
( 2y0
1 −y0
)3 + 4
(
x0
1 −x0
)3 + 4y0
(2
5 + 3
5
x0
1 −x0
2y0
1 −y0
))
= C5ℏ
where we put
C5 =
5(y0 −1)2
24(2y0 + 1)3
(
y2
0
( 2y0
1 −y0
)3 + 4
(
x0
1 −x0
)3 + 4y0
(2
5 + 3
5
x0
1 −x0
2y0
1 −y0
))
= −
1
3174(197y2
0 + 127y0 + 227).
Therefore, we obtain the required formula of the lemma.
35
