---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-022-2-1-e2-cosθ
section_title: "(1 −e−2 cosθ )"
section_number: 2
pages: 20-21
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
(
Re
(
ze
√−1θ)
− cosθ
)
)
.
This converges to zero as r → ∞ since 0 < Re(ze
√−1θ)< cosθ and Imz ≥ 0. Note
that M depends on r but that it is bounded because it is periodic with respect to
r.
Putting x =r(e
√−1θ +y√−1), we have
⏐
⏐
⏐
⏐
⏐
∫
U
+
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
∫ 1
0
e(2z−1)r(e
√
−1θ +y√−1) ×r√−1
sinh(r(e
√−1θ +y√−1)) dy
⏐
⏐
⏐
⏐
⏐
≤ 1
(r cosθ)m
∫ 1
0
r
⏐
⏐
⏐e(2z−1)r(e
√
−1θ +y√−1)
⏐
⏐
⏐
⏐
⏐sinh(r(e
√
−1θ +y√−1))
⏐
⏐dy
≤ 2re
2r Re
(
ze
√
−1θ
)
−r cosθ
(r cosθ)m (er cosθ −e−r cosθ ) ×
∫ 1
0
e−2ry Imzdy
= 2e
2r Re
(
ze
√−1θ
)
−2r cosθ
rm−1 cosmθ (1 −e−2r cosθ ) ×
∫ 1
0
e−2ry Imzdy
→ 0 ( r → ∞)
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 21
since Re(ze
√−1θ)< cosθ, noting that the last integral becomes either 1 (if z is real)
or 1−e−2r Im z
2r Imz (otherwise).
Similarly, putting x =r(−e
√−1θ +y√−1), we have
⏐
⏐
⏐
⏐
⏐
∫
U −
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
∫ 1
0
e−(2z−1)r(e
√
−1θ −y√−1) ×r√−1
sinh(r(e
√−1θ −y√−1)) dy
⏐
⏐
⏐
⏐
⏐
≤ 1
(r cosθ)m
∫ 1
0
r
⏐
⏐
⏐e−(2z−1)r(e
√
−1θ −y√−1)
⏐
⏐
⏐
⏐
⏐sinh(r(e
√
−1θ −y√−1))
⏐
⏐dy
≤ 2re−2r Re
(
ze
√
−1θ
)
+r cosθ
(r cosθ)m (er cosθ −e−r cosθ ) ×
∫ 1
0
e−2ry Imzdy
= 2e
−2r Re
(
ze
√−1θ
)
rm−1 cosmθ (1 −e−2r cosθ) ×
∫ 1
0
e−2ry Imzdy
→ 0 ( r → ∞)
since 0 < Re(ze
√−1θ ). Therefore from (6.1) we have
lim
r→∞
∫
C r
θ
e(2z−1)x
x sinh(x)dx = 2 lim
r→∞
⌊r⌋∑
k=1
e2kzπ √−1
k ,
which converges to −2 log(1−e2π √−1z) asr → ∞ when
⏐
⏐
⏐e2zπ √
−1
⏐
⏐
⏐< 1, ore2zπ √
−1 ⁄=
