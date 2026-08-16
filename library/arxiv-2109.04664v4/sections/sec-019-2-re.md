---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-019-2-re
section_title: "Re"
section_number: 2
pages: 19-20
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
Lemma 6.2. If 0< Re(zeθ√−1)< cosθ, then we have
∫
Cθ
e(2z−1)x
x sinh(x)dx =





−2 log
(
1 −e2π √
−1z
)
if Imz ≥ 0,
−2π √−1(2z − 1) − 2 log
(
1 −e−2π √−1z
)
if Imz <0.
and
∫
Cθ
e(2z−1)x
x2 sinh(x)dx
=







− 2√
−1
π Li2
(
e2π √−1z
)
if Imz ≥ 0,
−2π √−1
(
2z2 − 2z + 1
3
)
+ 2√−1
π Li2
(
e−2π √−1z
)
if Imz <0.
Proof. First we assume that Im z ≥ 0.
For a real number r > 1, let U
±
r be the vertical segment connecting ±re
√
−1θ
and ±re
√−1θ +r√−1, and Hr be the segment connecting −re
√−1θ +r√−1 and
re
√−1θ +r√−1. Here we assume that r is not an integer multiple of π so that
Hr avoids the poles of e(2z−1)x
xm sinh(x) (m = 1, 2) as a function of x. We orient U
±
r
upward and
Hr from left to right. Note that the distance between the origin and
the line containing U
±
r is r cosθ, and that the distance between the origin and the
line containing
Hr is also r cosθ.
By the residue theorem we have
∫
C r
θ
e(2z−1)x
xm sinh(x)dx −
∫
Hr
e(2z−1)x
xm sinh(x)dx
+
∫
U
+
r
e(2z−1)x
xm sinh(x)dx −
∫
U
−
r
e(2z−1)x
xm sinh(x)dx
=2π
√
−1
⌊r⌋∑
k=1
Res
( e(2z−1)x
xm sinh(x) ;x =kπ
√
−1
)
(6.1)
for m = 1, 2, where ⌊r⌋ is the greatest integer less than or equal to r. Since the
order of the pole x =kπ √
−1 of e(2t−1)x
xm sinh(x) for k = 1, 2, 3,... is one, we have
Res
( e(2z−1)x
x sinh(x) ;x =kπ
√
−1
)
= lim
t→kπ √−1
(x −kπ √−1)e(2z−1)x
x sinh(x) = e2kzπ √−1
kπ √−1
and
Res
( e(2z−1)x
x2 sinh(x) ;x =kπ
√
−1
)
= lim
x→kπ √−1
(x −k√−1)e(2z−1)x
x2 sinh(x) = −e2kzπ √−1
k2π 2 .
Next, we calculate integrals along Hr and U
±
r . Note that since the distance
between the origin and any point on these segments is greater than or equal to
r cosθ, we have
⏐
⏐
⏐
⏐
∫
H r
e(2z−1)x
xm sinh(x)dx
⏐
⏐
⏐
⏐ ≤ 1
(r cosθ)m
⏐
⏐
⏐
⏐
∫
H r
e(2z−1)x
sinh(x) dx
⏐
⏐
⏐
⏐
and
⏐
⏐
⏐
⏐
⏐
∫
U ±
r
e(2z−1)x
xm sinh(x)dx
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
∫
U ±
r
e(2z−1)x
sinh(x) dx
⏐
⏐
⏐
⏐
⏐
for m = 1, 2.
