---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-009-54-verifying-the-assumption-of-the-poisson-summa
section_title: "Verifying the assumption of the Poisson summation formula"
section_number: 5.4
pages: 39-48
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Verifying the assumption of the Poisson summation formula
In this section, in Lemma 5.8, we verify the assumption of the Poisson summation formula
(Proposition 4.6, see also Remark 4.8 and Appendix B) when we apply Proposition 4.6
and Remark 4.8 to (14). As in the previous section, we consider ˆV (t, s) instead of V (t, s)
in this section.
We calculate a critical point (tr, sr) ∈∆′ of Re ˆV (t, s), as follows. Putting x = e2π√−1 ·t
and y = e2π√−1 ·s, we have that
∂
∂t Re ˆV (t, s) = Re
(
−log
(
1 −1
x
))
,
∂
∂s Re ˆV (t, s) = Re
(
−2 log
(
1 −1
y
))
,
since t, s ∈R. Hence, putting xr = e2π√−1 ·tr and yr = e2π√−1 ·sr,

 xr −1

 =

 yr −1

 = 1,
39
noting that |xr| = |yr| = 1. Therefore, xr = yr = e2π√−1/3, and Re V (t, s) has a unique
maximal point (1
6, 1
6) on ∆′. Its maximal value is given by
Re ˆV
(1
6, 1
6
)
−ςR = Re
1
2π√−1
(
Li2(eπ√−1/3) −2 Li2(e−π√−1/3)
)
−ςR
= 0.03448931080... .
Hence,
Re ˆV (t, s) −ςR ≤0.03448931080... ,
(63)
for any (t, s) ∈∆′.
Lemma 5.8. When we apply Proposition 4.6 to (14), the assumptions of Proposition 4.6
hold.
Proof. We verify the assumptions (41) and (42) for i = 1 in Lemmas 5.9 and 5.10 be-
low, and verify the assumptions for i = 2 in Lemmas 5.11 and 5.12 below. The other
assumptions of Proposition 4.6 can be veriﬁed easily.
Lemma 5.9. The assumption (41) holds for i = 1.
Proof. As for the assumption (41) for i = 1, we show that ∂∆′ is null-homotopic in
{
(t + δ
√
−1, s) ∈C2 

 (t, s) ∈∆′, δ ≥0, Re V (t + δ
√
−1, s) < ςR + 2πδ
}
.
To show it, we show that the following disk bounds ∂∆′ in the above domain,
{
(t + δ0
√
−1, s) ∈C2 

 (t, s) ∈∆′}
∪
{
(t + δ
√
−1, s) ∈C2 

 (t, s) ∈∂∆′, δ ∈[0, δ0]
}
.
We put
Ft,s(δ) = Re V (t + δ
√
−1, s) −ςR −2πδ
in this proof. Then, it is suﬃcient to show that
Ft,s(δ0) < 0
for any (t, s) ∈∆′, and
(64)
Ft,s(δ) < 0
for any (t, s) ∈∂∆′ and δ ∈[0, δ0],
(65)
for some δ0 > 0.
To show these, we estimate the diﬀerential of Ft,s(δ), as follows. The diﬀerential of
Ft,s(δ) is given by
d
dδFt,s(δ) = Re
(√
−1 ∂
∂t
ˆV (t + δ
√
−1, s)
)
−2π
= −Im
(
−log
(
1 −1
x
)
−2π
√
−1
(
t + s −1
2
))
−2π
= Arg
(
1 −1
x
)
+ 2π
(
t + s −3
2
)
,
where we put x = e2π√−1(t+δ√−1). Since 0.04 ≤t ≤0.4, it is shown that Arg (1 −1
x) is in
the following range,
0 < Arg
(
1 −1
x
)
< π.
40
Therefore, since t + s ≤0.6,
d
dδFt,s(δ) < 2π
(1
2 + 0.6 −3
2
)
= −2π · 0.4.
We show (64), as follows. We have that
Ft,s(δ0) = Ft,s(0) +
∫δ0
0
d
dδFt,s(δ) dδ < Ft,s(0) −2π · 0.4 · δ0 .
Further, by (63),
Ft,s(0) = Re ˆV (t, s) −ςR ≤0.03448931080... .
Hence, (64) is satisﬁed for a suﬃciently large δ0.
We show (65), as follows. From the deﬁnition of ∆′, we have that Ft,s(0) < 0 for any
(t, s) ∈∂∆′. Since
d
dδFt,s(δ) < 0 as shown above, it is shown similarly as above that
Ft,s(δ) < 0 for any δ ≥0. Hence, (65) is satisﬁed.
Lemma 5.10. The assumption (42) holds for i = 1.
Proof. We put
Ft,s(δ) = Re V (t −δ
√
−1, s) −ςR −2πδ
in this proof. Similarly as the proof of Lemma 5.9, it is suﬃcient to show that there exists
ε > 0 such that
d
dδFt,s(δ) < −ε,
(66)
for any (t, s) ∈∆′.
We calculate this as
d
dδFt,s(δ) = Re
(
−
√
−1 ∂
∂t
ˆV (t −δ
√
−1, s)
)
−2π
= Im
(
−log
(
1 −1
x
)
−2π
√
−1
(
t + s −1
2
))
−2π
= −Arg
(
1 −1
x
)
−2π
(
t + s + 1
2
)
,
where we put x = e2π√−1(t−δ√−1). Since 0.04 ≤t ≤0.4, it is shown that Arg (1 −1
x) is in
the following range,
0 < Arg
(
1 −1
x
)
< π .
Therefore, since t + s ≥0.09,
d
dδFt,s(δ) < −2π
(
0.09 + 1
2
)
= −2π · 0.59,
and (66) is satisﬁed.
Lemma 5.11. The assumption (41) holds for i = 2.
41
Proof. We put
Ft,s(δ) = Re V (t, s + δ
√
−1) −ςR −2πδ
in this proof. Similarly as the proof of Lemma 5.9, it is suﬃcient to show that there exists
ε > 0 such that
d
dδFt,s(δ) < −ε,
(67)
for any (t, s) ∈∆′.
To show these, we calculate the diﬀerential of Ft,s(δ) as
d
dδFt,s(δ) = Re
(√
−1 ∂
∂sV (t, s + δ
√
−1)
)
−2π
= −Im
(
−2 log
(
1 −1
y
)
−2π
√
−1
(
t + 2s −1
))
−2π
= 2 Arg
(
1 −1
y
)
+ 2π
(
t + 2s −2
)
,
where we put y = e2π√−1(s+δ√−1). Since 0.05 ≤s ≤0.4, it is shown that Arg (1 −1
y) is in
the following range,
0 < Arg
(
1 −1
y
)
< 2π
(1
2 −s
)
.
Therefore, since t ≤0.4,
d
dδFt,s(δ) < 2 · 2π
(1
2 −s
)
+ 2π
(
t + 2s −2
)
= 2π(t −1) ≤−2π · 0.6,
and (67) is satisﬁed.
Lemma 5.12. The assumption (42) holds for i = 2.
Proof. We put
Ft,s(δ) = Re V (t, s −δ
√
−1) −ςR −2πδ
in this proof. Similarly as the proof of Lemma 5.9, it is suﬃcient to show that there exists
ε > 0 such that
d
dδFt,s(δ) < −ε,
(68)
for any (t, s) ∈∆′.
We calculate this as
d
dδFt,s(δ) = Re
(
−
√
−1 ∂
∂sV (t, s −δ
√
−1)
)
−2π
= Im
(
−2 log
(
1 −1
y
)
−2π
√
−1
(
t + 2s −1
))
−2π
= −2 Arg
(
1 −1
y
)
−2π
(
t + 2s
)
,
42
where we put y = e2π√−1(s−δ√−1). Since 0.05 ≤s ≤0.4, it is shown that Arg (1 −1
y) is in
the following range,
0 < Arg
(
1 −1
y
)
< π .
Therefore, since t + s ≥0.09 and s ≥0.05,
d
dδFt,s(δ) < −2π
(
0.09 + 0.05
)
= −2π · 0.14,
and (68) is satisﬁed.
A
Properties of φ(t)
In this appendix, we review some basic properties of φ(t).
We put ℏ= 2π√−1/N, and put
Φd(z) = Li2
(
z
)
+
∑
1≤k≤d
ℏ2kc2k ·
(
z d
dz
)2k−2
z
1 −z ,
where we deﬁne c2k by
y/2
sinh(y/2) =
∑
k≥0
c2k y2k.
Proposition A.1. We ﬁx any suﬃciently small δ > 0 and any M > 0. Let d be any
non-negative integer. Then, in the domain
{
t ∈C

 δ ≤Re t ≤1 −δ,
|Im t| ≤M
}
,
(69)
φ(t) and φ(k)(t) are presented by
φ(t) =
N
2π√−1 Φd(e2π√−1 t) + O
(
1
N 2d+1
)
,
(70)
φ(k)(t) =
N
2π√−1
( d
dt
)kΦd(e2π√−1 t) + O
(
1
N 2d+1
)
,
(71)
for each k > 0, where O(1/N 2d+1) means the error term whose absolute value is bounded
by C/N 2d+1 for some C > 0, which is independent of t (but possibly dependent on δ).
In particular,
1
N φ(t) uniformly converges to
1
2π√−1Li2(e2π√−1 t) in the domain (69), and
1
N φ′(t) uniformly converges to −log(1 −e2π√−1 t) in the domain (69).
Proof. We show (70). We have that
φ(t) =
∫∞
−∞
Ne(2t−1)x
4x2 sinh x ·
x/N
sinh(x/N) dx =
∫∞
−∞
Ne(2t−1)x
4x2 sinh x
∑
k≥0
c2k
(2x
N
)2kdx.
(72)
43
We put the “k=0” part of (72) to be
f(t) =
∫∞
−∞
Ne(2t−1)x
4x2 sinh x dx.
To calculate f(t), we consider the following contour,
[
−(m + 1
2)π, −1
]
∪
{
z ∈C

 |z| = 1, Im z ≥0}
∪
[
1, (m + 1
2)π
]
∪
{
z ∈C

 |z| = m + 1
2, Im z ≥0
}
.
Then, the integrand has poles at nπ√−1 (n = 1, 2, · · · , m) in the region bounded by the
contour. Hence,
f(t) =
lim
m→∞
m
∑
n=1
2π
√
−1
Res
x=nπ√−1
Ne(2t−1)x
4x2 sinh x
= 2π
√
−1
∞
∑
n=1
−N
4π2
(e2π√−1 t)n
n2
=
N
2π√−1 Li2(e2π√−1 t).
Further, for general k > 0, the “k” part of (72) is calculated as
c2k
N 2k f (2k)(t) =
N
2π√−1 · c2k
N 2k
( d
dt
)2kLi2(e2π√−1 t) =
N
2π√−1 · ℏ2kc2k
(
z d
dz
)2k−2
z
1 −z.
Therefore, we can put
φ(t) =
N
2π√−1 Φd(e2π√−1 t) + Rd,
where Rd is the error term. We estimate it, as follows. Since |(y/2)/ sinh(y/2)| is bounded
for y ∈R, there exists M0 > 0 such that

1
y2d+2
(
y/2
sinh y/2 −
d
∑
k=0
c2ky2k) 

 ≤M0
for any y ∈R. Hence, putting y = 2x/N,
|Rd| =

 φ(t) −
N
2π√−1 Φd(e2π√−1 t)

=

∫∞
−∞
Ne(2t−1)x
4x2 sinh x
(
x/N
sinh(x/N) −
d
∑
k=0
c2k
(2x
N
)2k)
dx

≤
∫∞
−∞

 Ne(2t−1)x
4x2 sinh x

 · M0

2x
N

2d+2 dx
= 22dM0
N 2d+1
( ∫∞
1
e(2Re t−1)x
| sinh x| x2d dx +
∫−1
−∞
e(2Re t−1)x
| sinh x| x2d dx +
∫
|z|=1
Im z ≥0
eRe ((2t−1)z)
| sinh z| |dz|
)
.
(73)
44
For x ≥1, the integrand of (73) is bounded by M1e−2δxx2d for some M1 > 0. For x ≤−1,
the integrand of (73) is bounded by M2e2δxx2d for some M2 > 0. For |z| = 1, the integrand
of (73) is bounded by a constant. Hence, the values of the integrals of (73) is bounded by
a constant. Therefore, |Rd| is bounded by C/N 2d+1 for some C > 0, which is independent
of t. Hence, we obtain (70).
We obtain (71) by similar arguments for φ(k)(t).
Lemma A.2. For any t ∈C with 0 < Re t < 1,
φ(t) + φ(1 −t) = 2π
√
−1
(
−N
2
(
t2 −t + 1
6
)
+
1
24N
)
.
Proof. By deﬁnition,
φ(t) + φ(1 −t) =
∫
γ
e(2t−1)x + e(1−2t)x
4x sinh x sinh(x/N) dx.
Since this integrand is an odd function, if the contour was R, the integral would vanish.
In this case, since the contour γ avoids the pole at x = 0, the contribution from the
residue at this pole survives. By expanding the numerator and the denominator of the
integrand as power series of x concretely, we can calculate this residue, and obtain the
required formula.
Lemma A.3 (Kashaev).
φ
( 1
2N
)
=
N
2π√−1
π2
6 + 1
2 log N + π√−1
4
−π√−1
12N ,
φ
(
1 −1
2N
)
=
N
2π√−1
π2
6 −1
2 log N + π√−1
4
−π√−1
12N .
Proof. It is suﬃcient to show that
φ
( 1
2N
)
+ φ
(
1 −1
2N
)
= 2π
√
−1
(
−N
12 + 1
4 −
1
12N
)
,
(74)
φ
( 1
2N
)
−φ
(
1 −1
2N
)
= log N.
(75)
We obtain (74) from Lemma A.2 by putting t = 1/2N.
We show (75), as follows. By (3) and (8),
exp
(
φ
( 1
2N
)
−φ
(
1 −1
2N
))
= N.
(76)
Further, from the deﬁnition of φ(t),
φ
( 1
2N
)
−φ
(
1 −1
2N
)
=
∫
γ
e(1−1/N)x −e(1/N−1)x
4x sinh x sinh(x/N) dx.
By a similar argument as in the proof of Lemma A.2, we can see that the residue of this
integrand at 0 vanishes. Hence, the value of this integral is real, and we obtain (75) from
(76).
45
B
Convergence of V (t, s) to ˆV (t, s)
When we apply the saddle point method and the Poisson summation formula to V (t, s),
it is necessary to note how V (t, s) converges to ˆV (t, s) as N →∞. In this appendix, we
verify that this convergence is suitable in those applications.
We recall that in Section 2.2 we put V (t, s) and ˆV (t, s) by
V (t, s) =
1
N
(
−φ(1 −t) −2 φ(1 −s)
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
t + s −1
2N
)2 + 1
2s2 −1
2t −s + 1
6
)
−3π√−1
4N
+ π√−1
4N 2
and
ˆV (t, s) =
1
2π√−1
(
−Li2(e−2π√−1 t) −2 Li2(e−2π√−1 s) −π2
6
)
−2π
√
−1
(1
2t2 + s2 + ts −1
2t −s + 1
6
)
.
Lemma B.1. Let m be any non-negative integer. Then, in the domain ∆′′ of (12), V (t, s)
is presented by the following form
V (t, s) = ˆV (t, s) + V1(t, s) 1
N + V2(t, s) 1
N 2 + · · · + Vm(t, s) 1
N m + +Rm(t, s)
1
N m+1
where Vi(t, s)’s are holomorphic functions independent of N, and |Rm(t, s)| is bounded by
a constant which is independent of N.
In particular, V (t, s) uniformly converges to ˆV (t, s) in the domain ∆′′.
Proof. We obtain the required presentation by applying Proposition A.1 to V (t, s). In
particular, by Proposition A.1,
1
N φ(t) uniformly converges to
1
2π√−1Li2(e2π√−1 t) as N →
∞in the domain ∆′′. Hence, we obtain the lemma.
Lemma B.2. Let i and j be any non-negative integers.
Then, in the domain ∆′′,

 ∂i+j
∂it∂jsV (t, s)

 is bounded by a constant which is independent of N.
Proof. By Proposition A.1,

 ∂i+j
∂it∂jsV (t, s)

 uniformly converges to

 ∂i+j
∂it∂js ˆV (t, s)

 as N →∞
in the domain ∆′′. Since ∆′′ is compact,

 ∂i+j
∂it∂js ˆV (t, s)

 is bounded in ∆′′. Hence, we obtain
the lemma.
When we apply the saddle point method, we need to show that V (t, s) satisﬁes the
condition of Remark 3.6, noting that ˆV (t, s) satisﬁes the assumption of the saddle point
method as shown in Section 5.3. In fact, we can show the condition of Remark 3.6 for
V (t, s) by Lemma B.1.
When we apply the Poisson summation formula, we need to show that V (t, s) satisﬁes
the condition of Remark 4.8, noting that ˆV (t, s) satisﬁes the assumption of the Poisson
summation formula as shown in Section 5.4. In fact, we can show the condition of Remark
4.8 for V (t, s) by Lemmas B.1 and B.2.
46
C
Critical points of V (t, s) and ˆV (t, s)
In this appendix, we show a proof of Lemma 5.1.
We put ℏ= 2π√−1/N, and use the notation in Section 5.2. By Proposition A.1, we
can put
1
N φ′(1 −t) = −log(1 −e−2π√−1 t) + r(t, ℏ) ℏ2
for some smooth function r(t, ℏ) of t and ℏ. Then, from the deﬁnition of V (t, s), we have
that
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
+ r(t, ℏ) ℏ2,
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
+ 2 r(s, ℏ) ℏ2.
Hence, a critical point of V (t, s) is a solution of





(
1 −1
x
)
(−q−1/2xy) = er(t,ℏ) ℏ2,
(
1 −1
y
)2q−1/2xy2 = e2 r(s,ℏ) ℏ2.
This is rewritten as
{
(1 −x)y = q1/2er(t,ℏ) ℏ2,
x(y −1)2 = q1/2e2 r(s,ℏ) ℏ2.
Further, by putting
F(t, s, ℏ) = (1 −x)y −q1/2er(t,ℏ) ℏ2,
G(t, s, ℏ) = x(y −1)2 −q1/2e2 r(s,ℏ) ℏ2,
the above system of equations is rewritten as
{
F(t, s, ℏ) = 0,
G(t, s, ℏ) = 0.
(77)
We note that (t0, s0, 0) is a solution of (77).
Proof of Lemma 5.1. It is suﬃcient to show that there exists a smooth solution
(
f(ℏ), g(ℏ), ℏ
)
of (77) in a suﬃciently small neighborhood of (t0, s0, 0). Hence, by the implicit function
theorem, it is suﬃcient to show that
det
( ∂
∂tF(t0, s0, 0)
∂
∂sF(t0, s0, 0)
∂
∂tG(t0, s0, 0)
∂
∂sG(t0, s0, 0)
)̸
= 0.
(78)
Since x = e2π√−1 t,
d
dt = 2π√−1 x d
dx. Similarly,
d
ds = 2π√−1 y d
dy. Therefore, from the
deﬁnitions of F(t, s, ℏ) and G(t, s, ℏ), we have that
1
2π√−1
∂
∂tF(t0, s0, 0) = x ∂
∂x
(
(1 −x)y
)

ℏ=0 = −x0y0 ,
47
1
2π√−1
∂
∂sF(t0, s0, 0) = y ∂
∂y
(
(1 −x)y
)

ℏ=0 = (1 −x0)y0 ,
1
2π√−1
∂
∂tG(t0, s0, 0) = x ∂
∂x
(
x(y −1)2)

ℏ=0 = x0(y0 −1)2,
1
2π√−1
∂
∂sG(t0, s0, 0) = y ∂
∂y
(
x(y −1)2)

ℏ=0 = 2x0y0(y0 −1).
Hence, the determinant of (78) is calculated as
−4π2 · det
(
−x0y0
(1 −x0)y0
x0(y0 −1)2
2x0y0(y0 −1)
)
= 4π2 · x0y0(y0 −1)(x0y0 + x0 + y0 −1)
= 4π2 · (2y0 + 1)(y0 −1)3/y0 = 4π2 · (2y0 + 1)̸ = 0,
since x0 = 1 −1/y0 and (y0 −1)3 = y0. Therefore, we obtain (78), completing the proof
of the lemma.
