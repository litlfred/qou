---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-024-22-hitoshi-murakami-and-anh-t-tran
section_title: "HITOSHI MURAKAMI AND ANH T. TRAN"
section_number: 22
pages: 22-24
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
and
Res
( e(2z−1)x
x2 sinh(x) ;x = −kπ
√
−1
)
= lim
x→−k√−1
(x +k√−1)e(2z−1)x
x2 sinh(x) = −e−2kπ √−1
k2π 2 .
Sincee(2z−1)x = 1 + (2z − 1)x + (2z−1)2x2
2 + · · · and 1
sinh(x) = 1
x − x
6 + · · ·, we have
Res
( e(2z−1)x
x sinh(x) ;x = 0
)
= 2z − 1
and
Res
( e(2z−1)x
x2 sinh(x) ;x = 0
)
= 2z2 − 2z + 1
3.
We can prove the integrals along Hr and U ±
r converge to zero as r → ∞ in
similar ways to the cases of
Hr and U
±
r .
Putting x =ye
√
−1θ −r√−1 and assuming r> 1, we have
⏐
⏐
⏐
⏐
⏐
∫
H
r
e(2z−1)x
xm sinh(x)dx
⏐
⏐
⏐
⏐
⏐
≤ 1
(r cosθ)m
⏐
⏐
⏐
⏐
⏐
∫ r
−r
e(2z−1)(ye
√
−1θ −r√−1) ×e
√−1θ
sinh(ye
√−1θ −r√−1) dy
⏐
⏐
⏐
⏐
⏐
≤ e2r Imz
(r cosθ)m
∫ r
−r
e
y Re
(
(2z−1)e
√−1θ
)
⏐
⏐sinh(ye
√
−1θ −r√−1)
⏐
⏐dy
(M := max
− 1≤ y≤ 1
e
y Re
(
(2z− 1)e
√
−1θ
)
⏐
⏐sinh(ye
√
− 1θ − r√ − 1)
⏐
⏐ > 0)
≤ e2r Imz
(r cosθ)m
×

2M +
∫ −1
−r
2e
2y Re
(
ze
√
−1θ
)
−y cosθ
e−y cosθ −ey cosθ dy +
∫ r
1
2e
2y Re
(
ze
√−1θ
)
−y cosθ
ey cosθ −e−y cosθ dy

,
which converges to zero as r → ∞.
Putting x =r(e
√
−1θ −y√−1), we have
⏐
⏐
⏐
⏐
⏐
∫
U
+
r
e(2z−1)xxm sinh(x)dx
⏐
⏐
⏐
⏐
⏐ ≤ 1
(r cosθ)m
⏐
⏐
⏐
⏐
⏐
∫ 1
0
e(2z−1)r(e
√
−1θ −y√−1) × (−r√−1)
sinh(r(e
√−1θ −y√−1)) dy
⏐
⏐
⏐
⏐
⏐
≤ 2re
2r Re
(
ze
√
−1θ
)
−r cosθ
(r cosθ)m(er cosθ −e−r cosθ)
∫ 1
0
e2ry Imzdy
= 2e2r Re
(
ze
√−1θ
)
−2r cosθ
rm−1 cosmθ(1 −e−2r cosθ ) ×
∫ 1
0
e2ry Imzdy,
since 0 < Re(ze
√−1θ )< cosθ, noting that the last integral becomes either 1 (if z is
real) or e2r Im z−1
2r Imz (otherwise).
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 23
Similarly, putting x = −r(e
√−1θ +y√−1), we have
⏐
⏐
⏐
⏐
⏐
∫
U
−
r
e(2z−1)xxm sinh(x)dx
⏐
⏐
⏐
⏐
⏐ ≤ 1
(r cosθ)m
⏐
⏐
⏐
⏐
⏐
∫ 1
0
e−r(2z−1)(e
√
−1θ +y√−1) × (−r√−1)
sinh(−r(e
√−1θ +y√−1)) dy
⏐
⏐
⏐
⏐
⏐
≤ 2re−2r Re
(
ze
√
−1θ
)
+r cosθ
(r cosθ)m(er cosθ −e−r cosθ )
∫ 1
0
e2ry Imzdy
= 2e
−2r Re
(
ze
√−1θ
)
rm−1 cosmθ(1 −e−2r cosθ) ×
∫ 1
0
e2ry Imzdy
→ 0 ( r → ∞)
since 0 < Re(ze
√−1θ ). So from (6.2) we have
lim
r→∞
∫
C r
θ
e(2z−1)x
x sinh(x)dx = −2π
√
−1 lim
r→∞
⌊r⌋∑
k=0
Res
( e(2z−1)x
x sinh(x) ;x = −kπ
√
−1
)
.
= −2π
√
−1(2z − 1) + 2 lim
r→∞
⌊r⌋∑
k=1
e−2kzπ √
−1
k .
Since this series converges to − log
(
1 −e−2zπ √−1
)
as r → ∞ if Im z < 0 from
Lemma 6.3, we ﬁnally have
∫
Cθ
e(2z−1)x
x sinh(x)dt = −2π
√
−1(2z − 1) − 2 log
(
1 −e−2zπ √−1
)
,
completing the proof when Im z <0.
Similarly, we have
lim
r→∞
∫
C r
θ
e(2z−1)x
x2 sinh(x)dx = −2π
√
−1 lim
r→∞
⌊r⌋∑
k=0
Res
( e(2z−1)x
x2 sinh(x) ;x = −kπ
√
−1
)
.
= −2π
√
−1
(
2z2 − 2z + 1
3
)
+ 2√−1
π lim
r→∞
⌊r⌋∑
k=1
e−2kzπ √
−1
k2 .
The series converges to Li 2
(
e−2zπ √−1
)
and so
∫
Cθ
e(2z−1)x
x2 sinh(x)dt = −2π
√
−1
(
2z2 − 2z + 1
3
)
+ 2√−1
π Li2
(
e−2zπ √−1
)
,
completing the proof when Im z <0. □
We give a proof for the following well-known lemma.
Lemma 6.3. For a complex number w with |w| ≤ 1, the series ∑ ∞
k=1
wk
k2 con-
verges to Li2(w). Here we use Li2(w) := −
∫w
0
log(1−t)
t dt as the deﬁnition of the
dilogarithm.
Proof. Put ak := 1
k2 .
Then we have ⏐
⏐
⏐
⏐
ak+1
ak
⏐
⏐
⏐
⏐ =
( k
k + 1
) 2
→ 1
ask → ∞. Therefore from d’Alembert’s ratio test, the radius of convergen ce of the
power series ∑ ∞
k=1akwk is 1. So we can diﬀerentiate it term by term if |w| < 1,
