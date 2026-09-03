---
doc_id: arxiv-1912.10638v2
doc_title: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG"
section_id: sec-007-15-acknowledgements
section_title: "Acknowledgements"
section_number: 1.5
pages: 7-13
source_pdf: 1912.10638v2.pdf
source_sha256: 612e44871d91d2e2
doc_brief: "Asymptotics of some quantum invariants of the Whitehead chains Ka Ho WONG — In this paper, we study the asymptotics of the colored Jones polynomials of the Whitehead chains with one belt colored by"
---
The author would like to thank Tian Yang for the valuable comments and suggestions to this work.
2 Asymptotics of JM1,M2(W L, e
2πi
N+ 1
2 )
2.1 Potential functions of JM1,M2(W L, e
2πi
N + 1
2 )
In this section, we compute the potential function of the ( M1,M 2)-th unnormalized colored Jones poly-
nomials for the Whitehead link WL , where M1,M 2 are sequences of positive integers in N. First of all,
the formula of the ( M1,M 2)-th unnormalized colored Jones polynomials of the Whitehead link is given
by [25]
JM1,M2(WL,t ) =t
M 2
2−1
2 (t
1
2−t− 1
2 )−1
M2−1∑
n=0
(t
M1 (2n+1)
2 −t−M1 (2n+1)
2 )· ˜C(n,t ;M2),
where
˜C(n,t ;M2) =t
M2 (M2−1)
2
M2−1−n∑
l=0
t−M2(l+n)
n∏
j=1
(1−tM2−l−j)(1−tl+j)
1−tj .
Put t =e
2πi
N + 1
2 . By direct computation, we have
(t
1
2−t− 1
2 )−1 = 1
2i sin
(
π
N+ 1
2
) (6)
t
M1 (2n+1)
2 −t−M1 (2n+1)
2 =t
(N + 1
2 )(2n+1)
2 +
(M1−(N + 1
2 ))(2n+1)
2 −t−
(N + 1
2 )(2n+1)
2 −
(M1−(N + 1
2 ))(2n+1)
2
=−
[
e
2πi( M1
N + 1
2
−1)(n+ 1
2 )
−e
−2πi( M1
N + 1
2
−1)(n+ 1
2 )
]
=−
[
e
πi
(
M1
N + 1
2
−1
)
e
2πi
(
M1
N + 1
2
−1
)
(n)
−e
−πi
(
M1
N + 1
2
−1
)
e
−2πi
(
M1
N + 1
2
−1
)
(n)
]
= (−1)M1−Ni
[
e
πi
(
M1
N + 1
2
−1
)
e
N + 1
2
2πi
[
(2πi)
(
M1
N + 1
2
−1
)][
2πi
(
n
N + 1
2
− 1
2
)]
+e
−πi
(
M1
N + 1
2
−1
)
e
−
N + 1
2
2πi
[
(2πi)
(
M1
N + 1
2
−1
)][
2πi
(
n
N + 1
2
− 1
2
)]]
(7)
7
Besides,
t
M 2
2−1
2 +M2 (M2−1)
2 =e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
(8)
t−M2(l+n) =e
−2πi( M2
N + 1
2
−1)(l+n)
=e
−
N + 1
2
2πi
[
2πi
(
M2
N + 1
2
−1
)[
2πi
(
l
N + 1
2
)
+2πi
(
n
N + 1
2
)]]
(9)
Next, for any odd integer r = 2N + 1≥ 3, we consider the following version of the quantum dilogarithm
function ϕr(z) (see [6, 7], or Section 2.3 in [24] for a review of its properties) deﬁned by
ϕr(z) = 4πi
r
∫
Ω
e(2z−π)x
4x sinh(πx) sinh(2πx
r )dx,
where
Ω = (−∞,−ϵ]∪{z∈ C||z| =ϵ, Imz >0}∪ [ϵ,∞)
for some ϵ∈ (0, 1) and
z∈
{
z∈ C
⏐⏐⏐⏐− π
2N + 1 < Rez <π + π
2N + 1
}
For any z∈ C with 0 < Rez < π, the quantum dilogarithm function satisﬁes the functional equation
(Lemma 2.1)1) in [24])
1−e2iz = exp
(N + 1
2
2πi
(
ϕr
(
z− π
2N + 1
)
−ϕr
(
z + π
2N + 1
)))
(10)
Furthermore, let Li2 : C\(1,∞)→ C be the dilogartihm function deﬁned by
Li2(z) =−
∫ z
0
log(1−u)
u du
For anyz with 0 < Rez <π, the quantum dilogarithm function satisﬁes (Lemma 2.3 in [24])
ϕr(z) = Li2(e2iz) + 2π2e2iz
3(1−e2iz)
1
(2N + 1)2 +O
( 1
(N + 1
2)3
)
, (11)
and asN→∞ ,ϕr(z) uniformly converges to Li2(e2iz) on any compact subset of{z∈ C| 0< Rez <π}.
Using the functional equation of the quantum dilogarithm function, we have
n∏
j=1
(1−tM2−l−j) =
n∏
j=1
(
1−e
2πi
(
M2
N + 1
2
− l
N + 1
2
− j
N + 1
2
))
= exp

N + 1
2
2πi
n∑
j=1
(
ϕr
( M2π
N + 1
2
− lπ
N + 1
2
− (j + 1
2)π
N + 1
2
)
−ϕr
( M2π
N + 1
2
− lπ
N + 1
2
− (j− 1
2)π
N + 1
2
)))
= exp
(N + 1
2
2πi
(
ϕr
( M2π
N + 1
2
− lπ
N + 1
2
− nπ
N + 1
2
− π
2N + 1
)
−ϕr
( M2π
N + 1
2
− lπ
N + 1
2
− π
2N + 1
)))
(12)
8
n∏
j=1
(1−tl+j) =
n∏
j=1
(
1−e
2πi
(
l
N + 1
2
+ j
N + 1
2
))
= exp

N + 1
2
2πi
n∑
j=1
(
ϕr
( lπ
N + 1
2
+ (j− 1
2)π
N + 1
2
)
−ϕr
( lπ
N + 1
2
+ (j + 1
2)π
N + 1
2
))

= exp
(N + 1
2
2πi
(
ϕr
( lπ
N + 1
2
+ π
2N + 1
)
−ϕr
( lπ
N + 1
2
+ nπ
N + 1
2
+ π
2N + 1
)))
(13)
n∏
j=1
(1−tj) =
n∏
j=1
(
1−e
2πi
(
j
N + 1
2
))
= exp

N + 1
2
2πi


n∑
j=1
(
ϕr
((j− 1
2)π
N + 1
2
)
−ϕr
((j + 1
2)π
N + 1
2
))



= exp
(N + 1
2
2πi
(
ϕr
( π
2N + 1
)
−ϕr
( nπ
N + 1
2
+ π
2N + 1
)))
(14)
Altogether, by (6) - (14), we have
JM1,M2(WL,e
2πi
N + 1
2 )
= (−1)(M1−N)e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
2 sin( π
N+ 1
2
)
×
M2−1∑
n=0
[
e
πi
(
M1
N + 1
2
−1
)
e
N + 1
2
2πi
[
(2πi)
(
M1
N + 1
2
−1
)][
2πi
(
n
N + 1
2
− 1
2
)]
+e
−πi
(
M1
N + 1
2
−1
)
e
−
N + 1
2
2πi
[
(2πi)
(
M1
N + 1
2
−1
)][
2πi
(
n
N + 1
2
− 1
2
)]]
×
M2−1−n∑
l=0
e
−
N + 1
2
2πi
[
2πi
(
M2
N + 1
2
−1
)[
2πi
(
l
N + 1
2
)
+2πi
(
n
N + 1
2
)]]
× exp
(N + 1
2
2πi
(
ϕr
( M2π
N + 1
2
− lπ
N + 1
2
− nπ
N + 1
2
− π
2N + 1
)
−ϕr
( M2π
N + 1
2
− lπ
N + 1
2
− π
2N + 1
)
+ϕr
( lπ
N + 1
2
+ π
2N + 1
)
−ϕr
( lπ
N + 1
2
+ nπ
N + 1
2
+ π
2N + 1
)
−ϕr
( π
2N + 1
)
+ϕr
( nπ
N + 1
2
+ π
N + 1
2
)))
(15)
Deﬁne the limiting ratio s1 and s2 by
s1 = lim
N→∞
M1
N + 1
2
and s2 = lim
N→∞
M1
N + 1
2
,
Then we have
JM1,M2(WL,e
2πi
N + 1
2 ) = (−1)(M1−N)e
2πi
N + 1
2
(M 2
2−M2
2 − 1
2 )
2 sin( π
N+ 1
2
) exp
(
−ϕr
( π
2N + 1
))
(I+ +I−) (16)
where
I± =e
±πi
(
M2
N + 1
2
−1
)M2−1∑
n=0
M2−1−n∑
l=0
exp
((
N + 1
2
)
Φ±(s1,s2)
M1,M2
( n
N + 1
2
, l
N + 1
2
))
(17)
9
with
Φ±(s1,s2)
M1,M2 (z1,z 2) = 1
2πi
{
±
(
2πi
( M1
N + 1
2
− 1
))(
2πi
(
z1− 1
2
))
−
(
2πi
( M2
N + 1
2
− 1
))
(2πiz1 + 2πiz2)
+
[
ϕr
( M2π
N + 1
2
−πz1−πz2− π
2N + 1
)
−ϕr
( M2π
N + 1
2
−πz2− π
2N + 1
)
+ϕr
(
πz2 + π
2N + 1
)
−ϕr
(
πz1 +πz2 + π
2N + 1
)
+ϕr
(
πz1 + π
2N + 1
)]}
(18)
deﬁned on
{
(z1,z 2)∈ C| 0≤ Rez1, Rez2≤π, Rez1 + Rez2 < M2
N+ 1
2
}
. Take N → ∞, we obtain the
potential functions
Φ±(s1,s2)(z1,z 2) = 1
2πi
[
± (2πi (s1− 1))
(
2πi
(
z1− 1
2
))
− (2πi(s2− 1))(2πiz1 + 2πiz2)
+ Li2
(
e2πi(s2−1)−2πiz1−2πiz2
)
− Li2
(
e2πi(s2−1)−2πiz2
)
+ Li2
(
e2πiz2
)
− Li2
(
e2πiz1+2πiz2
)
+ Li2
(
e2πiz1
)]
deﬁned on{(z1,z 2)∈ C| Rez1, Rez2 > 0, Rez1 + Rez2 <s 2}.
The following lemma estimates the diﬀerence between Φ±(s1,s2)
M1,M2 (z1,z 2) and Φ
±
(
M1
N + 1
2
, M2
N + 1
2
)
(z1,z 2).
Lemma 2. On any compact subset of {(z1,z 2)∈ C| Rez1, Rez2 > 0, Rez1 + Rez2 <s 2},
Φ±(s1,s2)
M1,M2 (z1,z 2) = Φ
±
(
M1
N + 1
2
, M2
N + 1
2
)
(z1,z 2) + 1
N + 1
2
EM2(z1,z 2) +O
(
1
(
N + 1
2
)2
)
, (19)
where
EM2(z1,z 2) = 1
2
[
log
(
1−e
2πi
(
M2
N + 1
2
−1
)
−2πiz1−2πiz2
)
− log
(
1−e
2πi
(
M2
N + 1
2
−1
)
−2πiz2
)
− log
(
1−e2πiz2
)
+ log
(
1−e2πiz1+2πiz2
)
− log
(
1−e2πiz1
)]
(20)
Proof. From (11), we have
Φ+(s1,s2)
M1,M2 (z1,z 2)
= 1
2πi
[
±
(
2πi
( M1
N + 1
2
− 1
))(
2πi
(
z1− 1
2
))
−
(
2πi
( M2
N + 1
2
− 1
))
(2πiz1 + 2πiz2)
+ Li2
(
e
2πi
(
M2
N + 1
2
−1
)
−2πiz1−2πiz2− πi
N + 1
2
)
− Li2
(
e
2πi
(
M2
N + 1
2
−1
)
−2πiz2− πi
N + 1
2
)
+ Li2
(
e
2πiz2+ πi
N + 1
2
)
− Li2
(
e
2πiz1+2πiz2+ πi
N + 1
2
)
+ Li2
(
e
2πiz1+ πi
N + 1
2
)]
+O
( 1
(N + 1
2)2
)
(21)
By considering the Talyor series expansion of Li 2
(
e
2πi
(
M2
N + 1
2
−1
)
−2πiz1−2πiz2+v
)
with respect to v, we
have
Li2
(
e
2πi
(
M2
N + 1
2
−1
)
−2πiz1−2πiz2− πi
N + 1
2
)
= Li2
(
e
2πi
(
M2
N + 1
2
−1
)
−2πiz1−2πiz2
)
+ πi
N + 1
2
log
(
1−e
2πi
(
M2
N + 1
2
−1
)
−2πiz1−2πiz2
)
+O
( 1
(N + 1
2)2
)
(22)
10
The result follows by applying the same argument to all the dilogarithm terms.
2.2 The asymptotics expansion formula for JN,N (W L, e
2πi
N + 1
2 )
Next, we consider the ( N,N )-th colored Jones polynomials for the Whitehead Link. Note that in this
case, (7) and (9) can be simpliﬁed as
t
N (2n+1)
2 −t−N (2n+1)
2 = 2i sin
(π(n + 1
2)
N + 1
2
)
t−N(l+n) =e
πi
(
l
N + 1
2
+ n
N + 1
2
)
Deﬁne
˜Φ(1,1)
N,N (z1,z 2) = 1
2πi
[
ϕr
( Nπ
N + 1
2
−πz1−πz2− π
2N + 1
)
−ϕr
( Nπ
N + 1
2
−πz2− π
2N + 1
)
+ϕr
(
πz2 + π
2N + 1
)
−ϕr
(
πz1 +πz2 + π
2N + 1
)
+ϕr
(
πz1 + π
2N + 1
)]
(23)
We can see that
lim
N→∞
˜Φ(1,1)
N,N (z1,z 2)
= Φ±(1,1)(z1,z 2)
= 1
2πi
[
Li2
(
e−2πiz1−2πiz2
)
− Li2
(
e−2πiz2
)
+ Li2
(
e2πiz2
)
− Li2
(
e2πiz1+2πiz2
)
+ Li2
(
e2πiz1
)]
Since Φ +(1,1)(z1,z 2) and Φ−(1,1)(z1,z 2) are the same, for simplicity we use Φ (1,1)(z1,z 2) to denote
Φ±(1,1)(z1,z 2). Recall that for θ∈ (0,π ), we have
Li2(e2iθ) = Li2(1) +θ(π−θ) + 2iΛ(θ),
where Λ is the Lobachevsky function deﬁned by
Λ(θ) =−
∫ θ
0
log|2 sint|dt
Also, the Lobachevsky function Λ is an odd function. Let
∆ ={(x,y )∈ [0, 1]2|x +y≤ 1}
Then for (z1,z 2)∈ ∆, the real part of Φ (1,1)(x1,x 2) is given by
Re Φ(1,1)(x1,x 2) = 1
π [Λ (−πz1−πz2)− Λ (−πz2) + Λ (πz2)− Λ (πz1 +πz2) + Λ (πz1)]
= 1
π [−2Λ(πx1 +πx2) + 2Λ(πx2) + Λ(πx1)]
= 1
πf(x1,x 2)
Note that this function f(x1,x 2) is the function appeared in Equation (3.22) of [25]. In particular,
the real part of Φ (1,1)(x1,x 2) has a unique maximum at ( 1
2, 1
4) in the ∆, with maximum value
Re Φ(1,1)
(1
2, 1
4
)
= 1
πf
(1
2, 1
4
)
= 1
2π
[
8Λ
(π
4
)]
= 1
2πv8 = 1
2π Vol(WL )
11
Furthermore, the critical point equations of the potential function are given by



log(1−e−2πiz1−2πiz2) + log(1−e2πiz1+2πiz2)− log(1−e2πiz1) = 0
log(1−e−2πiz1−2πiz2) + log(1−e2πiz1+2πiz2)− log(1−e−2πiz2)− log(1−e2πiz2) = 0
(24)
(25)
Note that the point ( z1,z 2) =
( 1
2, 1
4
)
indeed solves the equations (24) and (25). Moreover, at this
critical point,
∂2
∂z2
1
Φ(1,1)
(1
2, 1
4
)
= (2πi)
( i
1−i− −i
1 +i +−1
2
)
= 2πi
(2i− 1
2
)
∂2
∂z2
2
Φ(1,1)
(1
2, 1
4
)
= (2πi)
( i
1−i− −i
1 +i− −i
1 +i + i
1−i
)
= 2πi(2i)
∂2
∂z1∂z2
Φ(1,1)
(1
2, 1
4
)
= (2πi)
( i
1−i− −i
1 +i
)
= 2πi(i)
As a result, since
− det(HessΦ(1,1))
(1
2, 1
4
)
=−4π2(1 +i)⁄= 0,
Φ(1,1)(z1,z 2) has a non-degenerate critical point at
( 1
2, 1
4
)
with critical value
Φ(1,1)
(1
2, 1
4
)
= 1
2πi [2 Li2(i)− 2 Li2(−i) + Li2(−1)]
= 1
2πi
[
2
(
Li2(1) +
(π
4
)(
π− π
4
)
+ 2iΛ
(π
4
))
− 2
(
Li2(1) +
(3π
4
)(
π− 3π
4
)
+ 2iΛ
(3π
4
))
− π2
12
]
= 1
2π
[
8Λ
(π
4
)
+ π2i
12
]
= 1
2π
[
Vol(S3\WL ) +π2i
12
]
(26)
We denote this non-degenerate critical point by z(1,1). Similarly, we let z(1,1)
N,N to be the critical point
of the function ˜Φ(1,1)
N,N (z1,z 2) with limN→∞ z(1,1)
N,N = ( 1
2, 1
4).
Next, we are going to study the asymptotic expansion formula for JN,N (WL,e
2πi
N + 1
2 ) and show that
the exponential growth is given by the critical value of Φ(1,1)(
z(1,1))
. From previous discussion, since the
critical value is the unique maximum of Re Φ(z1,z 2) on ∆, it suﬃcies to study the asymptotic expansion
formula near this critical point.
Since z(1,1) is a critical point, we can ﬁnd a 4 real dimension ball BR⊂ C2∼= R4 centred at the
non-degenerate critical point with radius R such that whenever (x1±ηi,x 2), (x1,x 2±ηi)∈BR. we have
⏐⏐⏐⏐
d
dη Re Φ(x1±ηi,x 2)
⏐⏐⏐⏐,
⏐⏐⏐⏐
d
dη Re Φ(x1,x 2±ηi)
⏐⏐⏐⏐<π (27)
In particular, we may choose R small enough such that the intersection ∂BR∩ ∆ is a circle centered at
the critical point. Let
S±
1 ={(x1±ηi,x 2)| (x1,x 2)∈∂BR∩ ∆,η∈ [0,R/ 2]}∪{ (x1± (R/2)i,x 2)| (x1,x 2)∈BR∩ ∆}
S±
2 ={(x1,x 2±ηi)| (x1,x 2)∈∂BR∩ ∆,η∈ [0,R/ 2]}∪{ (x1,x 2± (R/2)i)| (x1,x 2)∈BR∩ ∆}
For every points on S±
1 , we have
Re Φ(1,1)(x1±ηi,x 2)− Re Φ(1,1)(z(1,1))≤
[
Re Φ(1,1)(x1,x 2)− Re Φ(1,1)(z(1,1))
]
+πη <2πη (28)
Similarly, for every points on S±
2 , we have
Re Φ(1,1)(x1,x 2±ηi)− Re Φ(1,1)(z(1,1))≤
[
Re Φ(1,1)(x1,x 2)− Re Φ(1,1)(z(1,1))
]
+πη <2πη (29)
12
Thus, by the Poisson Summation Formula (Proposition 4.6, Remark 4.7 and 4.8 in [18]), we have
JN,N (WL,e
2πi
N + 1
2 )
= e
2πi
N + 1
2
(N 2−N
2− 1
2 )
sin( π
N+ 1
2
) exp
(
−ϕr
( π
2N + 1
))N−1∑
n=0
N−1−n∑
l=1
sin
(
π
( n
N + 1
2
)
+ π
2N + 1
)
e
πi
(
n
N + 1
2
+ l
N + 1
2
)
× exp
((
N + 1
2
)
˜Φ±(1,1)
N,N
( n
N + 1
2
, l
N + 1
2
))
∼
N→∞
e
2πi
N + 1
2
(N 2−N
2− 1
2 )
sin( π
N+ 1
2
) exp
(
−ϕr
( π
2N + 1
))(
N + 1
2
)2
×
∫ ∫
BR∩∆
sin
(
πz1 + π
2N + 1
)
eπi(z1+z2) exp
((
N + 1
2
)
˜Φ(1,1)
N,N (z1,z 2)
)
dz1dz2 (30)
Next, we want to apply the Saddle point approximation. A key observation is that we can choose r as
small as possible such that the assumption in Proposition 3.5 in [18] is automatically satisﬁed. Moreover,
by Lemma A.3 of [18], we have
exp
(
−ϕh
( π
2N + 1
))
= exp
(
−N + 1
2
2πi
π2
6 − 1
2 log(N + 1
2)− πi
4 + πi
12(N + 1
2)
)
∼
N→∞
e−πi
4 (N + 1
2)− 1
2 exp
((
N + 1
2
)πi
12
)
(31)
Altogether, by the saddle point approximation (Proposition 3.5 in [18]), we have
JN,N (WL,e
2πi
N + 1
2 )
∼
N→∞
−e−πi
4
(N + 1
2)
1
2
π exp
(N + 1
2
2π
π2i
6
)
(N + 1
2)2
∫ ∫
BR∩∆
sin
(
πz1 + π
2N + 1
)
eπi(z1+z2) exp
((
N + 1
2
)
˜Φ(1,1)
N,N (z1,z 2)
)
dz1dz2
∼
N→∞
π(N + 1
2)3/2
√
−4π2(1 +i)
× exp
((
N + 1
2
)(
˜Φ(1,1)
N,N (z(1,1)
N,N ) +πi
12
))(
1 +O
( 1
N
))
(32)
with
lim
N→∞
[
˜Φ(1,1)
N,N (z(1,1)
N,N ) +πi
12
]
= 1
2π
[
Vol(S3\WL ) +π2i
4
]
= 1
2π [Vol(S3\WL ) +i CS(S3\WL )] (33)
Remark 2. If we use the normalization in [25] and [22], then there will be an extra factor
t
1
2−t− 1
2
tN/2−t−N/2 =
2i sin
(
π( 1
N+ 1
2
)
)
2i sin
(
π( N
N+ 1
2
)
) ∼
N→∞
2
In particular, the exponent of (N + 1
2) is 3
2, which agrees with the result in [25] and [22].
