---
doc_id: arxiv-1102.3530v1
doc_title: "THE COLORED JONES POL YNOMIAL, THE CHERN–SIMONS"
section_id: sec-006-5-calculation-of-s
section_title: "Calculation of S"
section_number: 5
pages: 12-34
source_pdf: 1102.3530v1.pdf
source_sha256: ad3edab19f3dc404
doc_brief: "THE COLORED JONES POLYNOMIAL, THE CHERN–SIMONS — W e show that from the asymptotic behavior of an evaluation of the colored Jones polynomial of the ﬁgure-eight knot we can extr act the Chern– Simons"
---
In this section we ﬁrst show the analyticity of Sγ and then calculate its special
values.
Lemma 5.1. If a complex number γ has the positive real part, then Sγ (z) is an
analytic function in {z ∈ C | | Re(z)|<π + Re(γ)}.
Proof. Put
Lγ (t) := ezt
t sinh(πt) sinh(γt).
We will show that the improper integrals
∫ ∞
R Lγtdt and
∫ R
−∞Lγtdt converge.
Puttingz :=x + √−1y andγ :=a + √−1b for real numbers x,y,a,b witha> 0
we have
Re(Lγ (t)) = −2ext(
cosh(at) sin(bt) sin(ty) + sinh(at) cos(bt) cos(yt)
)
t sinh(πt)
(
cos(2bt) − cosh(2at)
)
and
Im(Lγ (t)) = 2ext(
cosh(at) sin(bt) cos(ty) − sinh(at) cos(bt) sin(yt)
)
t sinh(πt)
(
cos(2bt) − cosh(2at)
)
for t ∈ R.
If t is positive and suﬃciently large we have
| Re(Lγ (t))| ≤ 2exteat
t sinh(πt)(cosh(2at) − 1)
= 8e(x−π −a)t
t(1 −e−2πt )(1 +e−4at − 2e−2at)
and similarly we have
| Im(Lγ (t))| ≤ 8e(x−π −a)t
t(1 −e−2πt )(1 +e−4at − 2e−2at).
Therefore the integral
∫ ∞
R Lγtdt converges since x<π +a.
If t is negative and |t| is suﬃciently large we have
| Re(Lγ (t))| ≤ 2e(x−a)t
t sinh(πt)(cosh(2at) − 1)
= 8e(x+π +a)t
t(e2πt − 1)(e4at + 1 − 2e2at)
and similarly we have
| Im(Lγ (t))| ≤ 8e(x+π +a)t
t(e2πt − 1)(e4at + 1 − 2e2at).
Therefore the integral
∫ R
−∞Lγtdt converges since x> −π −a. □
Next we prove Lemma 3.5.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 13
Proof of Lemma 3.5. By the deﬁnition we have
Sγ (−π − √−1u +γ)
Sγ (π − √−1u −γ)
= exp
(
1
4
∫
CR
(
e(−π −√−1u+γ )t
sinh(πt) sinh(γt) − e(π −√−1u−γ )t
sinh(πt) sinh(γt)
)
dt
t
)
= exp
( 1
2
∫
CR
e−√−1ut sinh(−πt +γt)
sinh(πt) sinh(γt)
dt
t
)
= exp
(
1
2
∫
CR
e−√−1ut coth(πt)
t dt − 1
2
∫
CR
e−√−1ut coth(γt)
t dt
)
.
We will calculate the integral
∫
CR
e−√−1ut coth(κt)/tdt for a complex number κ
with Re(κ)> 0 and Im(κ) ≤ 0.
Put κ :=α −β√−1 with α >0 and β ≥ 0. For a positive number r, let U1 be
the segment connecting r and r +r′β/α −r′√−1, U2 be the segment connecting
r +r′β/α −r′√−1 and −r +r′β/α −r′√−1, and U3 be the segment connecting
−r +r′β/α −r′√−1 and −r withr′ := (n + 1/2)πα/|κ|2, where n := ⌊r|κ|2/(πα)⌋.
Here ⌊x⌋ is the largest integer that does not exceed x. Note that r −πα/(2|κ|2)<
r′ ≤r +πα/(2|κ|2). We use r′ instead of r just to avoid the poles of coth( κt). Then
we have
⏐
⏐
⏐
⏐
⏐
∫
U1
e−√
−1ut
t coth(κt)dt
⏐
⏐
⏐
⏐
⏐
≤
∫ r′
0
⏐
⏐
⏐
⏐
⏐
e−√
−1u(r+sβ/α −s√−1)
r +sβ/α −s√−1
⏐
⏐
⏐
⏐
⏐
⏐
⏐coth
(
(α −β
√
−1)(r +sβ/α −s
√
−1)
) ⏐
⏐ds
≤ 1
r
∫ r′
0
e−us⏐
⏐coth
(
rα −
√
−1(sα +rβ +sβ2/α)
) ⏐
⏐ds
≤ 1
r
∫ r′
0
e−usds
= 1
ur (1 −e−ur′
)
r→∞
− − − →0.
Similarly we have
⏐
⏐
⏐
⏐
⏐
∫
U3
e−√
−1ut
t coth(κt)dt
⏐
⏐
⏐
⏐
⏐
≤
∫ r′
0
⏐
⏐
⏐
⏐
⏐
e−√
−1u(−r+sβ/α −s√−1)
−r +sβ/α −s√−1
⏐
⏐
⏐
⏐
⏐
⏐
⏐cosh
(
(α −β
√
−1)(−r +sβ/α −s
√
−1)
) ⏐
⏐ds
≤ |κ|
rα
∫ r′
0
e−us⏐
⏐cosh
(
−rα −
√
−1(sα −rβ +sβ2/α)
) ⏐
⏐ds
≤ |κ|
urα (1 −e−ur′
)
r→∞
− − − →0.
14 HITOSHI MURAKAMI
We also have⏐
⏐
⏐
⏐
⏐
∫
U2
e−√
−1ut
t coth(κt)dt
⏐
⏐
⏐
⏐
⏐
≤
∫ r
−r
⏐
⏐
⏐
⏐
⏐
e−√
−1u(s+r′β/α −r′√−1)
s +r′β/α −r′√−1
⏐
⏐
⏐
⏐
⏐
⏐
⏐coth
(
(α −β
√
−1)(s +r′β/α −r′√
−1)
) ⏐
⏐ds
≤e−ur′
r′
∫ r
−r
⏐
⏐coth
(
sα −
√
−1(r′α +sβ +r′β2/α)
) ⏐
⏐ds
=e−ur′
r′
∫ r
−r
⏐
⏐coth
(
sα −
√
−1
(
(n + 1/2)π +sβ
)) ⏐
⏐ds
=e−ur′
r′
∫ r
−r
⏐
⏐tanh
(
κs
) ⏐
⏐ds
(δ := max
−1≤s≤1
| tanh(κs)|> 0)
≤e−ur′
r′
(
2δ +
∫ −1
−r
|eκs −e−κs |
|eκs +e−κs |ds +
∫ r
1
|eκs −e−κs |
|eκs +e−κs |ds
)
≤e−ur′
r′
(
2δ +
∫ −1
−r
|eκs | + |e−κs |⏐
⏐|eκs | − |e−κs |
⏐
⏐ds +
∫ r
1
|eκs | + |e−κs |
⏐
⏐|eκs | − |e−κs |
⏐
⏐ds
)
= 2e−ur′
r′
(
δ +
∫ r
1
| coth(αs)|ds
)
= 2e−ur′
r′
(
δ + log(sinh(αr)) − log(sinh(α))
α
)
r→∞
− − − →0.
Therefore we have
∫
CR
e−√−1ut
t coth(κt)dt = 2π
√
−1
∞∑
l=1
Res
(
e−√−1ut
t coth(κt);t = lπ√−1
κ
)
= 2π
√
−1
∞∑
l=1
eluπ/κ
lπ√−1
= −2 log(1 −euπ/κ )
and so we have
Sγ (−π − √−1u +γ)
Sγ (π − √−1u −γ) = 1 −euπ/γ
1 −eu .
□
6. Proof of Proposition 3.1
In this section we follow [1, Appendix A] to show Proposition 3.1.
From [1, § 4.1] we have the following integral expression for | Re(z)| < π, or
| Re(z)| =π and Im(z) ≥ 0:
1
2√−1 Li2(−e
√−1z) = 1
4
∫
CR
ezt
t2 sinh(πt)dt.
Therefore we have
Sγ (z) = exp
( 1
2√−1γ Li2(−e
√−1z) +Iγ (z)
)
= exp
( N
ξ Li2(−e
√−1z) +Iγ (z)
)
,
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 15
where
Iγ (z) := 1
4
∫
CR
ezt
t sinh(πt)
( 1
sinh(γt) − 1
γt
)
dt
(see [1, Equation (4.2)]). Note that Iγ (z) is deﬁned for z with | Re(z)| ≤ π ([1,
Appendix A]).
Then we have from (2.3)
gN (z)
= exp
( N
ξ
(
Li2(−e
√−1π +u−ξz ) − Li2(−e−√−1π +u+ξz )
)
−Nuz
)
× exp
(
Iγ (π −
√
−1u +
√
−1ξz) −Iγ (−π −
√
−1u −
√
−1ξz)
)
= exp
(
N Φ(z)
)
exp
(
Iγ (π −
√
−1u +
√
−1ξz) −Iγ (−π −
√
−1u −
√
−1ξz)
)
.
(6.1)
We ﬁrst give an estimation for |Iγ (z)|.
Lemma 6.1 (see Lemma 3 in [1]) . If | Re(z)|<π , then we have
|Iγ (z)| ≤ A
( 1
π − Re(z) + 1
π + Re(z)
)
|γ| +B
(
1 +e− Im(z)R
)
|γ|
If | Re(z)| ≤ π, then we have
|Iγ (z)| ≤ 2A +B(1 +e− Im(z)R)|γ|.
Proof. We follow [1, Appendix A].
Put
ψ(w) := 1
sinh(w) − 1
w,
which is holomorphic in the open disk D0(π) with center 0 and radius π. Note that
(6.2) ψ(w) = w − sinh(w)
w sinh(w) = −wh(w)
k(w)
for entire functions h(w) and k(w) with
h(w) =
∞∑
j=0
w2j
(2j + 3)!
and
k(w) =
∞∑
j=0
w2j
(2j + 1)!
when |w|< π. Therefore there exists δ >0 such that min |w|≤δ |ψ(w)/w| =D >0
since lim w→0ψ(w)/w = 1/6.
Put Cδ := [−δ/|γ|, −R] ∪ Ω R ∪ [R,δ/ |γ|]. Consider the following integrals I0(z)
and I1(z) so that Iγ (z) = I0(z) +I1(z):
I0(z) := 1
4
∫
Cδ
exp(zt)
t sinh(πt)ψ(γt)dt,
I1(z) := 1
4
∫ −δ/ |γ |
−∞
exp(zt)
t sinh(πt)ψ(γt)dt + 1
4
∫ ∞
δ/ |γ |
exp(zt)
t sinh(πt)ψ(γt)dt.
Since lim w→∞wψ(w) = 0, ψ(w) has poles at w =mπ√−1 (m = ±1, ±2,... ), and
Im(γ) ⁄= 0, we have |γtψ(γt)| ≤ E for a positive number E. Note that E depends
only on the argument of γ and so only on ξ =γ × 2√−1N . So we have
|ψ(γt)| ≤ E
|γt|
16 HITOSHI MURAKAMI
for any t. Therefore we can apply the argument (replacing γ there with |γ|/E and
a with δ/|γ|) in [1, Page 532] to conclude
|I1(z)| ≤ E
δ
(
1 −e−2π |δ|/ |γ |)
if | Re(z)| ≤ π and
|I1(z)| ≤ E|γ|
2δ2(
1 −e−2πδ/ |γ |)
( e−(π −Re(z))δ/ |γ |)
π − Re(z) + e−(π +Re(z))δ/ |γ |)
π + Re(z)
)
if | Re(z)|<π .
Next we estimate I0(z). Let M (z,R ) be the maximum of
⏐
⏐
⏐ ezt
t sinh(πt )ψ(γt)
⏐
⏐
⏐ for
t ∈ Ω R. Then we have
⏐
⏐
⏐
⏐
∫
Ω R
exp(zt)
t sinh(πt)ψ(γt)dt
⏐
⏐
⏐
⏐ ≤πRM (z,R ).
From (6.2) we have
M (z,R ) = max
t∈Ω R
⏐
⏐
⏐
⏐
ezt
t sinh(πt)ψ(γt)
⏐
⏐
⏐
⏐
= max
t∈Ω R
|γ|
⏐
⏐
⏐
⏐
ezt
sinh(πt)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
h(γt)
k(γt)
⏐
⏐
⏐
⏐
since |γt| = |γ|R < π when t ∈ Ω R and R < 1. Then putting L(R) :=
maxt∈Ω R |h(z)/k(z)| and N (z,R ) := max t∈Ω R |ezt/(eπt −e−πt )| we can apply the
argument in [1, Page 533] to have the following estimation.
⏐
⏐
⏐
⏐
1
4
∫
Ω R
ezt
t sinh(πt)ψ(γt)dt
⏐
⏐
⏐
⏐ ≤ |γ|B(1 +e− Im(z)R)
for a constant B (depending only on R).
Now we will estimate the rest of I0(z). We have
⏐
⏐
⏐
⏐
⏐
∫ −R
−δ/ |γ |
ezt
t sinh(πt)ψ(γt)dt +
∫ δ/ |γ |
R
ezt
t sinh(πt)ψ(γt)dt
⏐
⏐
⏐
⏐
⏐
≤
∫ −R
−δ/ |γ
eRe(z)t
|t|| sinh(πt)| |ψ(γt)|dt +
∫ δ/ |γ
R
eRe(z)t
|t|| sinh(πt)| |ψ(γt)|dt
=
∫ δ/ |γ
R
eRe(z)t +e− Re(z)t
t sinh(πt) |ψ(γt)|dt
=2|γ|
∫ δ/ |γ
R
eRe(z)t +e− Re(z)t
eπt −e−πt
⏐
⏐
⏐
⏐
ψ(γt)
γt
⏐
⏐
⏐
⏐dt.
Sinceψ(w)/w is continuous in D0(π) and lim w→0ψ(w)/w = 1/6, there exists δ >0
such that min |w|<δ |ψ(w)/w| =D >0. Therefore if a<δ/ |γ|, then |γt| ≤ |γ|a<δ
in the integral and so we have
⏐
⏐
⏐
⏐
⏐
∫ −R
−δ/ |γ |
ezt
t sinh(πt)ψ(γt)dt +
∫ δ/ |γ |
R
ezt
t sinh(πt)ψ(γt)dt
⏐
⏐
⏐
⏐
⏐
≤2|γ|D
∫ δ/ |γ |
R
eRe(z)t +e− Re(z)t
eπt −e−πt dt
≤ 2|γ|D
1 −e−2πR
∫ a
R
(e−(π −Re(z))t +e−(π +Re(z))t)dt.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 17
Then from the argument in [1, Page 533] we have
⏐
⏐
⏐
⏐
⏐
∫ −R
−δ/ |γ |
ezt
t sinh(πt)ψ(γt)dt +
∫ δ/ |γ |
R
ezt
t sinh(πt)ψ(γt)dt
⏐
⏐
⏐
⏐
⏐
≤ 4δD
1 −e−2πR
when | Re(z)| ≤ π, and
⏐
⏐
⏐
⏐
⏐
∫ −R
−δ/ |γ |
ezt
t sinh(πt)ψ(γt)dt +
∫ δ/ |γ |
R
ezt
t sinh(πt)ψ(γt)dt
⏐
⏐
⏐
⏐
⏐
≤ 2|γ|D
(1 −e−2πR )
( 1 −e−(π −Re(z))δ/ |γ |
π − Re(z) + 1 −e−(π +Re(z))δ/ |γ |
π + Re(z)
)
when | Re(z)|<π .
Therefore if | Re(z)| ≤ π, we have
Iγ (z) ≤ E
δ
(
1 −e−2π |δ|/ |γ |) + |γ|B
(
1 +eIm(z)R
)
+ δD
1 −e−2πR
≤ 1
1 −e−2πR
( E
δ +δD
)
+ |γ|B
(
1 +eIm(z)R
)
since δ/|γ| ≥ R. If | Re(z)|<π we also have
|Iγ (z)|
≤ E|γ|
2δ2(
1 −e−2πδ/ |γ |)
( e−(π −Re(z))δ/ |γ |)
π − Re(z) + e−(π +Re(z))δ/ |γ |)
π + Re(z)
)
+ |γ|D
2(1 −e−2πR )
( 1 −e−(π −Re(z))δ/ |γ |
π − Re(z) + 1 −e−(π +Re(z))δ/ |γ |
π + Re(z)
)
+ |γ|B
(
1 +eIm(z)R
)
≤|γ|
( 1
π − Re(z) + 1
π + Re(z)
) 1
1 −e−2πR
( E
2δ2 + D
2
)
+ |γ|B
(
1 +eIm(z)R
)
.
The lemma follows by putting
A := 1
1 −e−2πR × max
{( E
2δ + δD
2
)
,
( E
2δ2 + D
2
)}
.
□
Now we prove Proposition 3.1.
First note that since gN (x) has no poles inside C+(ε) ∪C−(ε), we can assume
that ε = 0 without changing the sum, that is,
∫
C+(ε)
(tan(Nπx ) −
√
−1)gN (x)dx +
∫
C−(ε)
(tan(Nπx ) +
√
−1)gN (x)dx
=
∫
C+(0)
(tan(Nπx ) −
√
−1)gN (x)dx +
∫
C−(0)
(tan(Nπx ) +
√
−1)gN (x)dx
We decompose C+(0) into C+, 1 ∪ C+, 2 ∪ C+, 3, where C+, 1 connects 0 and
−u/(2π) + √−1, C+, 2 connects −u/(2π) + √−1 and 1 − u/(2π) + √−1, and
C+, 3 connects 1 −u/(2π) + √−1 and 1. Similarly we also decompose C−(0) in
to C−, 1 ∪C−, 2 ∪C−, 3, where C−, 1 connects 0 and u/(2π) − √−1, C−, 2 connects
u/(2π) − √−1 and 1 +u/(2π) − √−1, and C−, 3 connects 1 +u/(2π) − √−1 and −1.
LetI±,i (N ) be the integral of
(
tan(Nπx ) − √−1
)
gN (x) along C±,i (i = 1, 2, 3). We
18 HITOSHI MURAKAMI
will show that |I±,i (N )| is bounded from above by K±,i/N for a positive constant
K±,i independent of N .
We will give the following estimations for I±,i (N ).
(6.3) |I+, 1(N )|< K+, 1
N .
(6.4) |I+, 2(N )|< K+, 2
N .
(6.5) |I+, 3(N )|< K+, 3
N .
(6.6) |I−, 1(N )|< K−, 1
N .
(6.7) |I−, 2(N )|< K−, 2
N .
(6.8) |I−, 3(N )|< K−, 3
N .
Proof of (6.3). We ﬁrst estimate | tan(Nπ (−u/(2π) + √−1)t) − √−1|. We have
| tan(Nπ (−u/(2π) +
√
−1)t)) −
√
−1|
=
⏐
⏐
⏐
⏐
⏐
2e−N ut√
−1/ 2−N πt )
e−N ut√−1/ 2−N πt ) +eN ut√−1/ 2+N πt )
⏐
⏐
⏐
⏐
⏐
= 2e−2N πt
⏐
⏐e−N ut√
−1−2N πt + 1
⏐
⏐.
Since the denominator is bigger than 1 if Nut<π/ 2 we have
| tan(Nπ (−u/(2π) +
√
−1)t)) −
√
−1|< 2e−2N πt
when t<π/ (2Nu ). If t ≥π/(2Nu ), then the denominator is bigger than equal to
1 −e−2N πt . So we have
| tan(Nπ (−u/(2π) +
√
−1)t)) −
√
−1| ≤ 2e−2N πt
1 −e−2N πt ≤ 2e−2N πt
1 −e−π 2/u
when t ≥π/(2Nu ). Therefore for any 0 ≤t ≤ 1 we have
(6.9) | tan(Nπ (−u/(2π) +
√
−1)t) −
√
−1|< 2e−2N πt
1 −e−π 2/u .
So we have
(6.10) |I+, 1(N )| ≤ 2
1 −e−π 2/u
∫ 1
0
e−2N πt
⏐
⏐
⏐gN
((
− u
2π +
√
−1
)
t
) ⏐
⏐
⏐dt.
We estimate |gN ((−u/(2π) + √
−1)t)|.
Since the function gN is not well-deﬁned on the segment ( −u/(2π) + √−1)t
(Figure 1), we need to consider the segment ( −u/(2π) + √−1)t +ε) (0 ≤ t ≤ 1)
instead for small ε. (See the argument in [1, Page 534].)
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 19
From (6.1) we have
gN
((
− u
2π +
√
−1
)
t +ε
)
= exp
[
N Φ
((
− u
2π +
√
−1
)
t +ε
)]
× exp
[
Iγ
(
π −
√
−1u −
√
−1 |ξ|2t
2π +
√
−1εξ
)
−Iγ
(
−π −
√
−1u +
√
−1 |ξ|2t
2π −
√
−1εξ
)]
.
From Lemma 6.1, there exist A> 0 and B >0 such that |Iγ (z)| ≤ 2A +B|γ|(1 +
e− Im(z)R). So we have
⏐
⏐
⏐gN
((
− u
2π +
√
−1
)
t +ε
) ⏐
⏐
⏐
≤ exp
[
N Re Φ
((
− u
2π +
√
−1
)
t +ε
)] exp
(
2A +B|γ|(1 +e(u+|ξ|2t/ (2π )−εu)R
)
exp
(
2A +B|γ|(1 +e(u−|ξ|2t/ (2π )+εu)R)
≤ exp
[
N Re Φ
((
−ut
2π +
√
−1
)
t +ε
)]
exp
(
2A +B|γ|(1 +e(u+|ξ|2/ (2π )−εu)R
)
(6.11)
for 0 ≤t ≤ 1.
Now we want to estimate Re Φ
(
(−ut/(2π) + √
−1)t +ε
)
.
From the deﬁnition we have
Φ
((
− u
2π +
√
−1
)
t +ε
)
= 1
ξ
(
Li2(eu+|ξ|2t/ (2π )−εξ ) − Li2(eu−|ξ|2t/ (2π )+εξ )
)
+ u2t
2π −
√
−1ut −εu.
Since we may assume that Re( u + |ξ|2t/(2π) −ξε) = (1 −ε)u + |ξ|2t/(2π)> 0, there
are two cases to consider; the case where u − |ξ|2t/(2π) < 0 and the case where
u − |ξ|2t/(2π) ≥ 0.
If |z| > 1, it is convenient to replace Li 2(z) with Li 2(z−1) using the following
well-known formula.
(6.12) Li 2(z) + Li2(z−1) = −π2
6 − 1
2
(
log(−z)
) 2
,
where we choose a branch of log( −z) so that −π <Im log(−z)<π .
20 HITOSHI MURAKAMI
• The case where u − |ξ|2t/(2π) < 0. We choose ε small enough so that
u − |ξ|2t/(2π) +εu< 0. From (6.12) we have
Φ
((
− u
2π +
√
−1
)
t +ε
)
= 1
ξ
(
− Li2(e−u−|ξ|2t/ (2π )+εξ ) − Li2(eu−|ξ|2t/ (2π )+εξ )
−π2
6 − 1
2
(
u + |ξ|2t
2π −εξ +
√
−1π
) 2)
+ u2t
2π −
√
−1ut −εu
= 1
ξ
(
− Li2(eu−|ξ|2t/ (2π )+ξε ) − Li2(eu−|ξ|2t/ (2π )+ξε )
)
− π2
6ξ − 1
2ξ
(
u + |ξ|2t
2π −εξ +
√
−1π
) 2
+ u2t
2π −
√
−1ut −εu,
where in the ﬁrst equality we choose the sign of √−1π so that Im( u +
|ξ|2t/(2π) − εξ + π√−1) = −εu +π is between −π and π. Since the
dilogarithm function Li(z) is analytic when Re( z)< 1, we have
lim
εց0
Φ
((
− u
2π +
√
−1
)
t +ε
)
= 1
ξ
(
− Li2(e−u−|ξ|2t/ (2π )) − Li2(eu−|ξ|2t/ (2π ))
)
− π2
6ξ − 1
2ξ
(
u + |ξ|2t
2π +
√
−1π
) 2
+ u2t
2π −
√
−1ut.
Since Li 2(z) is real when z is real and z <1, we have
lim
εց0
Re Φ
((
− u
2π +
√
−1
)
t +ε
)
= − u
|ξ|2
(
Li2(e−u−|ξ|2t/ (2π )) + Li2(eu−|ξ|2t/ (2π ))
)
− uπ2
6|ξ|2 − u
2|ξ|2
(
u + |ξ|2t
2π
) 2
+ uπ2
2|ξ|2 − 4π(u + |ξ|2t/(2π))π
2|ξ|2 + u2t
2π
= − u
|ξ|2
(
Li2(e−u−|ξ|2t/ (2π )) + Li2(eu−|ξ|2t/ (2π ))
)
− 5uπ2
6|ξ|2 − u3
2|ξ|2 − u|ξ|2t2
8π2 −πt
<0
if u> 0.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 21
• The case where u − |ξ|2t/(2π) ≥ 0. In this case we have
Φ
((
− u
2π +
√
−1
)
t +ε
)
= 1
ξ
(
− Li2(e−u−|ξ|2t/ (2π )+εξ ) + Li2(e−u+|ξ|2t/ (2π )−εξ )
− 1
2
(
u + |ξ|2t
2π −εξ +π
√
−1
) 2
+ 1
2
(
u − |ξ|2t
2π +εξ −π
√
−1
) 2)
+ u2t
2π −
√
−1ut −uε
= 1
ξ
(
− Li2(e−u−|ξ|2t/ (2π )+εξ ) + Li2(e−u+|ξ|2t/ (2π )−εξ )
)
− 2u
ξ
( |ξ|2t
2π −εξ +π
√
−1
)
+ u2t
2π −
√
−1ut −uε
and so we have
lim
εց0
Re Φ
((
− u
2π +
√
−1
)
t +ε
)
= u
|ξ|2
(
− Li2(e−u−|ξ|2t/ (2π )) + Li2(e−u+|ξ|2t/ (2π ))
)
− Re
( 2u
ξ
( |ξ|2t
2π +π
√
−1
))
+ u2t
2π
= u
|ξ|2
(
− Li2(e−u−|ξ|2t/ (2π )) + Li2(e−u+|ξ|2t/ (2π ))
)
− 4π2u
|ξ|2 − u2t
2π
<0
if u> 0.
Therefore for any t we have Re Φ
(
(−u/(2π) + √−1)t +ε
)
≤ 0 for small ε> 0.
So from (6.10) and (6.11) we have
|I+, 1(N )| ≤ 2
1 −e−π 2/u exp
(
2A +B|γ|(1 +e(u+|ξ|2/ (2π )−εu)R
) ∫ 1
0
e−2N πtdt
= 1 −e−2N π
Nπ (1 −e−π 2/u ) exp
(
2A +B|γ|(1 +e(u+|ξ|2/ (2π ))R
)
< K+, 1
N
for a positive constant K+, 1. □
Proof of (6.6). Since tan is an odd function we have from (6.9)
(6.13) | tan
(
Nπ (u/(2π) −
√
−1)t
)
+
√
−1|< 2e−2N πt
1 −e−π 2/u
for any 0 ≤t ≤ 1.
So we have
(6.14) |I−, 1(N )| ≤ 2
1 −e−π 2/u
∫ 1
0
e−2N πt
⏐
⏐
⏐gN
(( u
2π −
√
−1
)
t
) ⏐
⏐
⏐dt.
We estimate |gN ((u/(2π) − √
−1)t)|.
As in the case of I+, 1 we need to calculate gN (gN ((u/(2π) − √−1)t) +ε).
22 HITOSHI MURAKAMI
From (6.1) we have
gN
(( u
2π −
√
−1
)
t +ε
)
= exp
[
N Φ
(( u
2π −
√
−1
)
t +ε
)]
× exp
[
Iγ
(
π −
√
−1u +
√
−1 |ξ|2t
2π +
√
−1εξ
)
−Iγ
(
−π −
√
−1u −
√
−1 |ξ|2t
2π −
√
−1εξ
)]
.
From Lemma 6.1, there exist A> 0 and B >0 such that |Iγ (z)| ≤ 2A +B|γ|(1 +
e− Im(z)R). So we have
⏐
⏐
⏐gN
(( u
2π −
√
−1
)
t +ε
) ⏐
⏐
⏐
≤ exp
[
N Re Φ
(( u
2π −
√
−1
)
t +ε
)] exp
(
2A +B|γ|(1 +e(u−|ξ|2t/ (2π )−εu)R
)
exp
(
2A +B|γ|(1 +e(u+|ξ|2t/ (2π )+εu)R)
≤ exp
[
N Re Φ
(( ut
2π −
√
−1
)
t +ε
)]
exp
(
2A +B|γ|(1 +e(u−|ξ|2/ (2π )−εu)R
)
(6.15)
for 0 ≤t ≤ 1.
Now we want to estimate Re Φ
(
(ut/(2π) − √
−1)t +ε
)
.
From the deﬁnition we have
Φ
(( u
2π −
√
−1
)
t +ε
)
= 1
ξ
(
Li2(eu−|ξ|2t/ (2π )−εξ ) − Li2(eu+|ξ|2t/ (2π )+εξ )
)
− u2t
2π +
√
−1ut −εu.
Since Re(u + |ξ|2t/(2π) +εξ) = (1 + ε)u + |ξ|2t/(2π) > 0, there are two cases to
consider; the case where u − |ξ|2t/(2π)< 0 and the case where u − |ξ|2t/(2π) ≥ 0.
• The case where u−|ξ|2t/(2π) ≤ 0. In this case we have u−|ξ|2t/(2π)−εu<
0. From (6.12) we have
Φ
(( u
2π −
√
−1
)
t +ε
)
= 1
ξ
(
Li2(eu−|ξ|2t/ (2π )−εξ ) + Li2(e−u−|ξ|2t/ (2π )−εξ )
+π2
6 + 1
2
(
u + |ξ|2t
2π +εξ −
√
−1π
) 2)
− u2t
2π +
√
−1ut −εu
= 1
ξ
(
Li2(eu−|ξ|2t/ (2π )−ξε ) + Li2(e−u−|ξ|2t/ (2π )−ξε )
)
+ π2
6ξ + 1
2ξ
(
u + |ξ|2t
2π +εξ −
√
−1π
) 2
− u2t
2π +
√
−1ut −εu.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 23
Therefore we have
lim
εց0
Φ
(( u
2π −
√
−1
)
t +ε
)
= 1
ξ
(
Li2(eu−|ξ|2t/ (2π )) + Li2(e−u−|ξ|2t/ (2π ))
)
+ π2
6ξ + 1
2ξ
(
u + |ξ|2t
2π −
√
−1π
) 2
− u2t
2π +
√
−1ut
and so
lim
εց0
Re Φ
(( u
2π −
√
−1
)
t +ε
)
= u
|ξ|2
(
Li2(eu−|ξ|2t/ (2π )) + Li2(e−u−|ξ|2t/ (2π ))
)
+ uπ2
6|ξ|2 + u
2|ξ|2
(
u + |ξ|2t
2π
) 2
− uπ2
2|ξ|2 − 4π(u + |ξ|2t/(2π))π
2|ξ|2 − u2t
2π
= u
|ξ|2
(
Li2(eu−|ξ|2t/ (2π )) + Li2(e−u−|ξ|2t/ (2π ))
)
− 7uπ2
3|ξ|2 + u3
2|ξ|2 + u|ξ|2t2
8π2 −πt
= − 2uπ2
|ξ|2 + u3
2|ξ|2 + u|ξ|2t2
8π2 −πt
since Li 2(z) ≤π2/6 for 0 <z ≤ 1. We can easily prove
−2uπ2
|ξ|2 + u3
2|ξ|2 + u|ξ|2t2
8π2 −πt<πt
when 0 <u< 1 and 2uπ/|ξ|2 ≤t ≤ 1. So we have
lim
εց0
Re Φ
(( u
2π −
√
−1
)
t +ε
)
<πt
in this case.
• The case where u−|ξ|2t/(2π)> 0. We choose ε so thatu−|ξ|2t/(2π)−εu>
0. In this case we have
Φ
(( u
2π −
√
−1
)
t +ε
)
= 1
ξ
(
− Li2(e−u+|ξ|2t/ (2π )+εξ ) + Li2(e−u−|ξ|2t/ (2π )−εξ )
− 1
2
(
u − |ξ|2t
2π −εξ +π
√
−1
) 2
+ 1
2
(
−u − |ξ|2t
2π −εξ +π
√
−1
) 2)
− u2t
2π +
√
−1ut −εu
and so we have
lim
εց0
Re Φ
(( u
2π −
√
−1
)
t +ε
)
= u
|ξ|2
(
− Li2(e−u+|ξ|2t/ (2π )) + Li2(e−u−|ξ|2t/ (2π ))
)
+ u2t
2π − 4uπ2
|ξ|2
<u2t
2π − 23uπ2
6|ξ|2 < 0
24 HITOSHI MURAKAMI
if 0 <u< 1 and 0 ≤t< 2uπ/|ξ|2.
Therefore for any 0 ≤ t ≤ 1 we have Re Φ
(
(u/(2π) − √−1)t +ε
)
≤ πt for small
ε> 0.
So from (6.14) and (6.15) we have
|I−, 1(N )| ≤ 2
1 −e−π 2/u exp
(
2A +B|γ|(1 +e(u−|ξ|2/ (2π ))R
) ∫ 1
0
e−N πtdt
= 2(1 −e−N π )
N (1 −e−π 2/u ) exp
(
2A +B|γ|(1 +e(u−|ξ|2/ (2π ))R
)
< K−, 1
N
for a positive constant K−, 1. □
Proof of (6.5). Since tan has period π we have
(6.16) | tan(Nπ (−u/(2π) +
√
−1)t) −
√
−1|< 2e−2N πt
1 −e−π 2/u
from (6.9)
From (6.16) we have
(6.17) |I+, 3(N )| ≤ 2
1 −e−π 2/u
∫ 1
0
e−2N πt
⏐
⏐
⏐gN
((
− u
2π +
√
−1
)
t + 1
) ⏐
⏐
⏐dt.
As in the case of I+, 1(N ) we consider the integral on the segment ( −u/(2π) +√
−1)t + 1 −ε (0 ≤t ≤ 1) for small ε.
We estimate Φ
(
(−u/(2π) + √−1)t + 1 −ε
)
. We have
Φ
((
− u
2π +
√
−1
)
t + 1 −ε
)
= 1
ξ
(
Li2(eu+|ξ|2t/ (2π )−(1−ε)ξ) − Li2(eu−|ξ|2t/ (2π )+(1−ε)ξ)
)
+ u2t
2π −
√
−1ut − (1 −ε)u.
Since we may assume that Re( u + |ξ|2t/(2π) − (1 −ε)ξ) = εu + |ξ|2t/(2π)> 0, there
are two cases to consider; the case where 2 u − |ξ|2t/(2π) ≤ 0 and the case where
2u − |ξ|2t/(2π)> 0.
• 2u − |ξ|2t/(2π) ≤ 0. In this case, since u − |ξ|2t/(2π) + (1 −ε)u< 0, from
(6.12) we have
Φ
((
− u
2π +
√
−1
)
t + 1 −ε
)
= 1
ξ
(
− Li2(e−u−|ξ|2t/ (2π )+(1−ε)ξ) − Li2(eu−|ξ|2t/ (2π )+(1−ε)ξ)
−π2
6 − 1
2
(
u + |ξ|2t
2π − (1 −ε)ξ +π
√
−1
) 2)
+ u2t
2π −
√
−1ut − (1 −ε)u
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 25
Since the dilogarithm function Li( z) is analytic when Re( z)< 1, we have
lim
εց0
Φ
((
− u
2π +
√
−1
)
t + 1 −ε
)
= 1
ξ
(
− Li2(e−|ξ|2t/ (2π )) − Li2(e2u−|ξ|2t/ (2π ))
)
− π2
6ξ − 1
2ξ
( |ξ|2t
2π −π
√
−1
) 2
+ u2t
2π −
√
−1ut −u.
So we have
lim
εց0
Re
((
− u
2π +
√
−1
)
t + 1 −ε
)
= − u
|ξ|2
(
Re Li2(e−|ξ|2t/ (2π )) + Re Li2(e2u−|ξ|2t/ (2π ))
)
− uπ2
6|ξ|2 − u
2|ξ|2
|ξ|4t2
4π2 + uπ2
2|ξ|2 − 4π|ξ|2t/(2π)π
2|ξ|2 + u2t
2π −u
= − u
|ξ|2
(
Re Li2(e−|ξ|2t/ (2π )) + Re Li2(e2u−|ξ|2t/ (2π ))
)
+ uπ2
3|ξ|2 − u|ξ|2t2
8π2 −πt + u2t
2π −u ≤ 0.
The last inequality follows since uπ 2
3|ξ|2 − u|ξ|2t2
8π 2 −πt + u2t
2π −u, is a quadratic
function with respect to u with non-positive maximum.
• 2u − |ξ|2t/(2π) > 0. In this case we may choose ε small so that u −
|ξ|2t/(2π) + (1 −ε)u> 0. Then we have
Φ
((
− u
2π +
√
−1
)
t + 1 −ε
)
= 1
ξ
(
− Li2(e−u−|ξ|2t/ (2π )+(1−ε)ξ) + Li2(e−u+|ξ|2t/ (2π )−(1−ε)ξ)
− 1
2
(
u + |ξ|2t
2π − (1 −ε)ξ +π
√
−1
) 2
+ 1
2
(
u − |ξ|2t
2π + (1 −ε)ξ −π
√
−1
) 2)
+ u2t
2π −
√
−1ut − (1 −ε)u
and so we have
lim
εց0
Re Φ
((
− u
2π +
√
−1
)
t + 1 −ε
)
= u
|ξ|2
(
− Li2(e−|ξ|2t/ (2π )) + Li2(e−2u+|ξ|2t/ (2π ))
)
+ 2u3
|ξ|2 − u2t
2π + 4π2u
|ξ|2 −u.
Putting s := |ξ|2t/(2π) and consider the function
f (u,s ) := − Li2(e−s) + Li2(e−2u+s) + 2u2 −us + 4π2 − |ξ|2 − 2π2s
u
= − Li2(e−s) + Li2(e−2u+s) +u2 −us − 2π2s
u
so that
u
|ξ|2f
(
u, |ξ|2t
2π
)
= lim
εց0
Re Φ
((
− u
2π +
√
−1
)
t + 1 −ε
)
−πt.
26 HITOSHI MURAKAMI
We will show f (u,s ) ≤ 0 for 0 ≤s< 2u ≤ 2.
We have
exp
[
−∂f (u,t )
∂t
]
= 2e2π 2/u (cosh(u) − cosh(s −u)).
Therefore it can be shown that for ﬁxed u, f (u,s ) is increasing for 0 ≤ s <
u − arccosh(cosh(u) − exp(−2π2/u)/2), decreasing for u − arccosh(cosh(u) −
exp(−2π2/u)/2) < s < u + arccosh(cosh(u) − exp(−2π2/u)/2), and increas-
ing for u + arccosh(cosh(u) − exp(−2π2/u)/2) < s < u . Since a graph of
f
(
u,u − arccosh(cosh(u) − exp(−2π2/u)/2)
)
looks as Figure 4 and
f (u, 2u) = − 23π2
6 −u2 − Li2(e−2u)< 0,
we see f (u,s ) ≤ 0.
0.2 0.4 0.6 0.8 1
-1
-0.8
-0.6
-0.4
-0.2
Figure 4. A graph of f
(
u,u − arccosh(cosh(u) − exp(−4π2/u)/2)
)
.
Therefore we ﬁnally have
|I+, 3(N )|< 2
1 −e−π 2/u exp
(
2A +B(1 +e(u+|ξ|2/ (2π ))R)|γ|
) ∫ 1
4πu/ |ξ|2
e−2N πtdt
= e−8N π 2u/ |ξ|2
−e−2N π
Nπ (1 −e−π 2/u ) exp
(
2A +B(1 +e(u+|ξ|2/ (2π ))R)|γ|
)
< K+, 3
N
for a positive constant K+, 3. □
Proof of (6.8). Since tan has period π we have
(6.18) | tan(Nπ ((u/(2π) −
√
−1)t + 1) +
√
−1|< 2e−2N πt
1 −e−π 2/u
from (6.9)
From (6.18) we have
(6.19) |I−, 3(N )| ≤ 2
1 −e−π 2/u
∫ 1
0
e−2N πt
⏐
⏐
⏐gN
((
− u
2π +
√
−1
)
t + 1
) ⏐
⏐
⏐dt.
As in the case of I+, 1(N ) we consider the integral on the segment ( u/(2π) −√
−1)t + 1 −ε (0 ≤t ≤ 1) for small ε.
We estimate Φ
(
(u/(2π) − √−1)t + 1 −ε
)
. We have
Φ
(( u
2π −
√
−1
)
t + 1 −ε
)
= 1
ξ
(
Li2(eu−|ξ|2t/ (2π )−(1−ε)ξ) − Li2(eu+|ξ|2t/ (2π )+(1−ε)ξ)
)
− u2t
2π +
√
−1ut − (1 −ε)u.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 27
We will calculate lim εց0 Φ
(
(u/(2π) − √−1)t + 1 −ε
)
.
Note that Re(u + |ξ|2t/(2π) + (1 −ε)ξ) = 2u + |ξ|2t/(2π) −εu> 0 for small ε.
Since Re(u − |ξ|2t/(2π) − (1 −ε)ξ) = −|ξ|2t/(2π) + εu, if t > 0 we assume that
Re(u − |ξ|2t/(2π) − (1 −ε)ξ)< 0. Therefore we assume that t> 0.
In this case from (6.12) we have
Φ
(( u
2π −
√
−1
)
t + 1 −ε
)
= 1
ξ
(
Li2(e−|ξ|2t/ (2π )+εξ ) + Li2(e−2u−|ξ|2t/ (2π )+εξ )
)
+ π2
6ξ + 1
2ξ
(
2u + |ξ|2t
2π −εξ +π
√
−1
) 2
− u2t
2π +
√
−1ut − (1 −ε)u
and
Re Φ
(( u
2π −
√
−1
)
t + 1 −ε
)
= 1
ξ
(
Li2(e−|ξ|2t/ (2π )+εξ ) + Li2(e−2u−|ξ|2t/ (2π )+εξ )
)
+ π2
6ξ + 1
2ξ
(
2u + |ξ|2t
2π −εξ +π
√
−1
) 2
− u2t
2π +
√
−1ut − (1 −ε)u.
So we have
lim
εց0
Φ
(( u
2π −
√
−1
)
t + 1 −ε
)
= 1
ξ
(
Li2(e−|ξ|2t/ (2π )) + Li2(e−2u−|ξ|2t/ (2π ))
)
+ π2
6ξ + 1
2ξ
(
2u + |ξ|2t
2π +π
√
−1
) 2
− u2t
2π +
√
−1ut −u
= u
|ξ|2
(
Li2(e−|ξ|2t/ (2π )) + Li2(e−2u−|ξ|2t/ (2π ))
)
+ uπ2
6|ξ|2 + u
2|ξ|2
(
2u + |ξ|2t
2π
) 2
− uπ2
2|ξ|2 + 4π2
2|ξ|2
(
2u + |ξ|2t
2π
)
− u2t
2π −u
≤ 11uπ2
3|ξ|2 + 2u3
|ξ|2 + u|ξ|2t2
8π2 +πt + u2t
2π −u< 3
2πt
if 0 <u< 1 and 0 <t ≤ 1.
Therefore we ﬁnally have
|I−, 3(N )|< 2
1 −e−π 2/u exp
(
2A +B(1 +e(u+|ξ|2/ (2π ))R)|γ|
) ∫ 1
0
e−N πt/ 2dt
= 4(1 −e−N π/ 2)
Nπ (1 −e−π 2/u ) exp
(
2A +B(1 +e(u+|ξ|2/ (2π ))R)|γ|
)
< K−, 3
N
for a positive constant K−, 3. □
28 HITOSHI MURAKAMI
Proof of (6.4). From [1, Equation (4.6)] we have
|I+, 2(N )| ≤ 4e−2πN
∫ 1−ε
ε
|gN (−u/(2π) +
√
−1 +t)|dt.
From (6.1) we have
|gN (−u/(2π) +
√
−1 +t)|
≤ exp
(
N Re(Φ( −u/(2π) +
√
−1 +t))
)
exp
(
4A + 2|γ|(1 +eR(u+u2/ (2π )+2π ))
)
.
Now estimate Re(Φ( −u/(2π) + √−1 +t)). We have
Φ
(
− u
2π +
√
−1 +t
)
= 1
ξ
(
Li2(eu+|ξ|2/ (2π )−ξt) − Li2(eu−|ξ|2/ (2π )+ξt)
)
+ u2
2π −
√
−1u −ut.
Since Re(u + |ξ|2/(2π) −ξt) = u(1 −t) +|ξ|2/(2π)> 0 and Re(u − |ξ|2/(2π) +ξt) =
u(1 +t) − |ξ|2/(2π) ≤ 0, we have
Φ
(
− u
2π +
√
−1 +t
)
= − 1
ξ
(
Li2(eu+|ξ|2/ (2π )−ξt) + Li2(eu−|ξ|2/ (2π )+ξt)
)
− π2
6ξ − 1
2ξ
(
u + |ξ|2
2π − (u + 2π
√
−1)t +π
√
−1
) 2
+ u2
2π −
√
−1u −ut
from (6.12). Therefore we have
Re Φ
(
− u
2π +
√
−1 +t
)
= − u
|ξ|2
(
Re Li2(eu+|ξ|2/ (2π )−ξt) + Re Li2(eu−|ξ|2/ (2π )+ξt)
)
− 2π
|ξ|2
(
Im Li2(eu+|ξ|2/ (2π )−ξt) + Im Li2(eu−|ξ|2/ (2π )+ξt)
)
+ (2t − 1)π − 1
2 (t2 + 1)u + u2t
2π − u3
8π2 + π2u
3|ξ|2
≤ − u
|ξ|2
(
Re Li2(eu+|ξ|2/ (2π )−ξt) + Re Li2(eu−|ξ|2/ (2π )+ξt)
)
− 2π
|ξ|2
(
Im Li2(eu+|ξ|2/ (2π )−ξt) + Im Li2(eu−|ξ|2/ (2π )+ξt)
)
+ (2t − 1)π.
For 0<r< 1 and 0 <θ < 2π we have
Re Li2(re
√−1θ) = − 1
2
∫ r
0
log(1 − 2s cosθ +s2)
s ds ≥ − 1
2
∫ r
0
log(1 + 2s +s2)
s ds
= −
∫ r
0
log(1 +s)
s ds ≥ −
∫ 1
0
log(1 +s)
s ds = Li 2(−1) = −π2
12.
We also have
Im Li2(re
√−1θ) = −
∫ r
0
arg(1 −se
√−1θ )
s ds.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 29
If 0 <θ ≤π the right hand side is non-negative. If π <θ< 2π we have
Im Li2(re
√−1θ) = −
∫ 1
0
arg(1 −se
√−1θ )
s ds +
∫ 1
r
arg(1 −se
√−1θ )
s ds
= Im Li2(e
√−1θ ) +
∫ 1
r
arg(1 −se
√−1θ)
s ds.
The second integral is positive and Im Li 2(e
√−1θ ) is bigger than or equal to
− Im Li2(exp(√−1π/3)) = −1.01494... .
Therefore we have
Re Φ
(
− u
2π +
√
−1 +t
)
≤ π2u
6|ξ|2 + 2π Im Li2(e
√−1π/ 3)
|ξ|2 + (2t − 1)π
So we have
|I+, 2(N )|
≤4 exp(4A + 2|γ|(1 +eR(u+u2/ (2π )+2π )))e−3πN
× exp
[
N
(
π2u
6|ξ|2 + 2π Im Li2(e
√−1π/ 3)
|ξ|2
)] ∫ 1
0
e2N πtdt
= 2(1 −e−2πN )
πN exp(4A + 2|γ|(1 +eR(u+u2/ (2π )+2π )))
× exp
[
πN
(
πu
6|ξ|2 + 2 Im Li2(e
√−1π/ 3)
|ξ|2 − 1
)]
< 2
πN exp(4A + 2|γ|(1 +eR(u+u2/ (2π )+2π )))
<K+, 2
N
for a positive constant K+, 2. Here we use the inequality
πu
6|ξ|2 + 2 Im Li2(e
√−1π/ 3)
|ξ|2 − 1< π
6 + 1.01494...
2π2 − 1< 0.
□
Proof of (6.7). From [1, Equation (4.6)] we have
|I−, 2(N )| ≤ 4e−2πN
∫ 1−ε
ε
|gN (u/(2π) −
√
−1 +t)|dt.
From (6.1) we have
|gN (u/(2π) −
√
−1 +t)|
≤ exp
(
N Re(Φ(u/(2π) −
√
−1 +t))
)
exp
(
4A + 2|γ|(1 +eR(u+u2/ (2π )+2π ))
)
.
Now estimate Re(Φ( u/(2π) − √−1 +t)). We have
Φ
( u
2π −
√
−1 +t
)
= 1
ξ
(
Li2(eu−|ξ|2/ (2π )−ξt) − Li2(eu+|ξ|2/ (2π )+ξt)
)
− u2
2π +
√
−1u −ut.
30 HITOSHI MURAKAMI
Since Re(u − |ξ|2/(2π) −ξt) = u(1 −t) − |ξ|2/(2π)< 0 and Re(u + |ξ|2/(2π) +ξt) =
u(1 +t) + |ξ|2/(2π)> 0, we have
Φ
( u
2π −
√
−1 +t
)
= 1
ξ
(
Li2(eu−|ξ|2/ (2π )−ξt) + Li2(e−u−|ξ|2/ (2π )−ξt)
)
+ π2
6ξ + 1
2ξ
(
u + |ξ|2
2π + (u + 2π
√
−1)t −π
√
−1
) 2
− u2
2π +
√
−1u −ut
from (6.12). Therefore we have
Re Φ
( u
2π −
√
−1 +t
)
= u
|ξ|2
(
Re Li2(eu−|ξ|2/ (2π )−ξt) + Re Li2(e−u−|ξ|2/ (2π )−ξt)
)
+ 2π
|ξ|2
(
Im Li2(eu−|ξ|2/ (2π )−ξt) + Im Li2(e−u−|ξ|2/ (2π )−ξt)
)
+ uπ2
6|ξ|2 − u2
2π −ut
+ u
2|ξ|2
( (
u + |ξ|2
2π +ut
) 2
−π2(2t − 1)2
)
+ 4π
2|ξ|2π(2t − 1)
(
u + |ξ|2
2π +ut
)
= u
|ξ|2
(
Re Li2(eu−|ξ|2/ (2π )−ξt) + Re Li2(e−u−|ξ|2/ (2π )−ξt)
)
+ 2π
|ξ|2
(
Im Li2(eu−|ξ|2/ (2π )−ξt) + Im Li2(e−u−|ξ|2/ (2π )−ξt)
)
+ ut2
2 + |ξ|2t
2π − 7uπ2
3|ξ|2 + u3
2|ξ|2 + u|ξ|2
8π2 −π.
For 0<r< 1 and 0 <θ < 2π we have
Re Li2(re
√−1θ) = − 1
2
∫ r
0
log(1 − 2s cosθ +s2)
s ds ≤ − 1
2
∫ r
0
log(1 − 2s +s2)
s ds
= −
∫ r
0
log(1 −s)
s ds ≤ −
∫ 1
0
log(1 −s)
s ds = Li 2(1) = π2
6 .
We also have
Im Li2(re
√−1θ) = −
∫ r
0
arg(1 −se
√−1θ)
s ds
= −
∫ 1
0
arg(1 −se
√−1θ )
s ds +
∫ 1
r
arg(1 −se
√−1θ )
s ds
≤ Im Li2(e
√−1θ ) ≤ Im Li2(e
√−1π/ 3) = 1.01494....
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 31
when 0 ≤θ ≤π. Since Im Li 2(re
√−1θ ) = − Im Li2(re
√−1(θ−π )) when π < θ≤ 2π,
we have
Re Φ
( u
2π −
√
−1 +t
)
= 4π
|ξ|2 Im Li2(e
√−1π/ 3) + ut2
2 + |ξ|2t
2π − 2uπ2
|ξ|2 + u3
2|ξ|2 + u|ξ|2
8π2 −π
(since 0 <t< 1 and 0 <u<π/ 2).
< |ξ|2t
2π + 1
π Im Li2(e
√−1π/ 3) + π
2 − 4π
17 + π
64 + 17π
64 −π
≤ |ξ|2t
2π + 1
π Im Li2(e
√−1π/ 3) − 247
544π.
when u<π/ 2.
So we have
|I−, 2(N )|
<4e(Im Li2(e
√−1π/ 3)/π −247π/ 544−2π )N exp
(
4A + 2|γ|(1 +eR(u+u2/ (2π )+2π ))
)
× lim
εց0
∫ 1−ε
ε
eN |ξ|2t/ (2π )dt
=4e(Im Li2(e
√−1π/ 3)/π −247π/ 544−2π )N exp
(
4A + 2|γ|(1 +eR(u+u2/ (2π )+2π ))
)
× 2π
N |ξ|2 (eN |ξ|2/ (2π ) − 1)
= 8π exp
(
4A + 2|γ|(1 +eR(u+u2/ (2π )+2π ))
)
N |ξ|2
×
(
e(Im Li2(e
√−1π/ 3)/π −247π/ 544−2π +|ξ|2/ (2π ))N
−e(Im Li2(e
√−1π/ 3)/π −247π/ 544−2π )N
)
< 8π exp
(
4A + 2|γ|(1 +eR(u+u2/ (2π )+2π ))
)
N |ξ|2
×
(
e(Im Li2(e
√−1π/ 3)/π −179π/ 544)N −e(Im Li2(e
√−1π/ 3)/π −247π/ 544−2π )N
)
< 8π exp
(
4A + 2|γ|(1 +eR(u+u2/ (2π )+2π ))
)
N |ξ|2
<K−, 2
N
for a positive constant K−, 2, since Im Li 2(e
√−1π/ 3)/π − 179π/544 = −0.710657... .
□
7. Proof of Proposition 3.2
In this section we again follow [1] to prove Proposition 3.2. From (6.1) w e have
∫
p(ε)
gN (w)dw =
∫
p(ε)
exp
(
N Φ(w)
)
dw +
∫
p(ε)
exp
(
N Φ(w)
)
hγ (w)dw
for any path in the parallelogram bounded by C+(ε)∪C−(ε) connecting ε and 1 −ε,
where
hγ (w) := exp
(
Iγ (π −
√
−1u +
√
−1ξw) −Iγ (−π −
√
−1u −
√
−1ξw)
)
− 1.
Note that hγ (w) is deﬁned for w with 0 < Im(ξw)< 2π, that is, for w between the
two parallel thick lines depicted in Figure 1.
32 HITOSHI MURAKAMI
Then we have ⏐
⏐
⏐
⏐
⏐
∫
p(ε)
gN (w)dw −
∫
p(ε)
exp
(
N Φ(w)
)
dw
⏐
⏐
⏐
⏐
⏐
≤
∫
p(ε)
⏐
⏐exp
(
N Φ(w)
)
hγ (w)
⏐
⏐dw
≤ max
w∈p(ε)
{
exp
(
N Re Φ(w)
)} ∫
p(ε)
|hγ (w)|dw
= max
w∈p(ε)
{
exp
(
N Re Φ(w)
)} ∫ 1−ε
ε
|hγ (w)|dw
≤ max
w∈p(ε)
{
exp
(
N Re Φ(w)
)} ∫ 1
0
|hγ (w)|dw.
(7.1)
Here we use the analyticity of hγ in the equality.
By the deﬁnition of hγ we have
(7.2) hγ (t) =
∞∑
n=1
1
n!
(
Iγ (π −
√
−1u +
√
−1ξt) −Iγ (−π −
√
−1u −
√
−1ξt)
) n
.
From Lemma 6.1, for 0 <t< 1 we have
⏐
⏐Iγ (π −
√
−1u +
√
−1ξt)
⏐
⏐ ≤A|γ|
( 1
2πt + 1
2π − 2πt
)
+B|γ|
(
1 +e(u−ut)R
)
and
⏐
⏐Iγ (−π −
√
−1u −
√
−1ξw)
⏐
⏐ ≤A|γ|
( 1
2π − 2πt + 1
2πt
)
+B|γ|
(
1 +e(u+ut)R
)
,
and so we have ⏐
⏐Iγ (π −
√
−1u + 2πt) −Iγ (−π −
√
−1u − 2πt)
⏐
⏐
≤A|γ|
π
( 1
1 −t + 1
t
)
+B|γ|
(
2 +e(1+t)uR +e(1−t)uR
)
≤|γ| (A′f (t) +B′)
for some positive constants A′ and B′, where we put f (t) := 1/t + 1/(1 −t). Since
f (t) ≥ 4 for 0 <t< 1 we have
⏐
⏐Iγ (π −
√
−1u +
√
−1ξw) −Iγ (−π −
√
−1u −
√
−1ξw)
⏐
⏐
≤|γ|
(
A′f (t) +B′f (t)
4
)
=A′′|γ|f (t),
(7.3)
where A′′ :=A′ +B′/4.
From the argument in [1, P. 537] we have
∫ 1−|γ |
|γ |
f (t)ndt ≤ 22n+1
∫ 1/ 2
|γ |
dt
tn
for n ≥ 1. Since |γ| = |ξ|/(2N ) we have
∫ 1/ 2
|γ |
dt
t = logN − log |ξ| ≤ logN
and ∫ 1/ 2
|γ |
dt
tn = 1
n − 1
( 1
|γ|n−1 − 2n−1
)
≤ 1
(n − 1)|γ|n−1.
for n ≥ 2.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 33
Therefore from (7.2) and (7.3) we have
∫ 1−|γ |
|γ |
|hγ (t)|dt ≤
∞∑
n=1
1
n! (A′′)n|γ|n
∫ 1−|γ |
|γ |
f (t)ndt
≤ 2|γ|
(
4A′′ logN +
∞∑
n=2
(4A′′)n
(n − 1)n!
)
≤ |ξ|
N (4A′′ logN + exp(4A′′) − 4A′′ − 1)
≤ K ′ logN
N
for a positive constant K ′ if N is suﬃciently large.
For 0 ≤t ≤ 1, we also have from Lemma 6.1
⏐
⏐Iγ (π −
√
−1u + 2πt) −Iγ (−π −
√
−1u − 2πt)
⏐
⏐
≤4A +B|γ|
(
2 +e(1+t)uR +e(1−t)uR
)
.
Since |γ| = |ξ|/(2N ), we have
|hγ (t)| ≤ exp
(
4A + B′|ξ|
2N
)
.
So we have ∫ |γ |
0
|hγ (t)|dt ≤ |ξ|
2N exp
(
4A + B′|ξ|
2N
)
≤ K ′′
N
and ∫ 1
1−|γ |
|hγ (t)|dt ≤ |ξ|
2N exp
(
4A + B′|ξ|
2N
)
≤ K ′′′
N
for positive constants K ′′ and K ′′′.
Therefore we have
∫ 1
0
|hγ (t)|dt ≤ K ′ logN
N + K ′′
N + K ′′′
N ≤ K2 logN
N
for a positive constant K2. Now from (7.1) we ﬁnally have
⏐
⏐
⏐
⏐
⏐
∫
p(ε)
gN (w)dw −
∫
p(ε)
exp
(
N Φ(w)
)
dw
⏐
⏐
⏐
⏐
⏐ ≤ K2 logN
N max
w∈p(ε)
{
exp
(
N Re Φ(w)
)}
,
proving Proposition 3.2.
8. Proof of Lemma 3.4
We will show that ξΦ(w0) is purely imaginary with positive imaginary part.
Then since ξ is in the ﬁrst quadrant, Φ( w0) is in also in the ﬁrst quadrant and so
Re Φ(w0)> 0.
Since ϕ(u) is purely imaginary (Remark 3.3), we have Li 2(eu−ϕ (u)) =
Li2(eu+ϕ (u)). Therefore from (3.4) and (6.12) we have
Im(ξΦ(w0)) = −2 Im Li2(eu+ϕ (u)) −u Im ˜ϕ(u)
= 2 Im Li2(e−u−ϕ (u)) + Im
(
u +ϕ(u) +π
√
−1
) 2
−u Im ˜ϕ(u)
= 2 Im Li2(e−u−ϕ (u)) +uϕ(u).
34 HITOSHI MURAKAMI
So we have
d Im(ξΦ(w0))
du
=2 Im
(
log(1 −e−u−ϕ (u))
(
1 +
√
−1d Imϕ(u)
du
))
+ Imϕ(u) +ud Imϕ(u)
du
=d Imϕ(u)
du
(
2 log |1 −e−u−ϕ (u)| +u
)
+ 2 arg(1 −e−u−ϕ (u)) + Imϕ(u)
=d Imϕ(u)
du log
(
(1 −e−u−ϕ (u))(1 −e−u+ϕ (u))eu
)
+ 2 arg(1 −e−u−ϕ (u)) + Imϕ(u)
=d Imϕ(u)
du log(eu +e−u −eϕ (u) −e−ϕ (u)) + 2 arg(1 −e−u−ϕ (u)) + Imϕ(u)
=2 arg(1 −e−u−ϕ (u)) + Imϕ(u)< 0
since −π/3< Imϕ(u)< 0.
Since ϕ(0) = −π√−1/3 and ϕ
(
log
(
(3 +
√
5)/2
) )
= 0, we have
ξΦ(w0) =



2 Im Li2
(
eπ √
−1/ 3
)
= 1.01494... (u = 0),
2 Im Li2
(
2
3+
√
5
)
= 0 ( u = log
(
(3 +
√
5)/2
)
).
Therefore Im(ξΦ(w0)) > 0 for 0 < u <log
(
(3 +
√
5)/2
)
, completing the proof of
Lemma 3.4.
