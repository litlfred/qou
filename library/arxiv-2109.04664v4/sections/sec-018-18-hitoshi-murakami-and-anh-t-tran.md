---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-018-18-hitoshi-murakami-and-anh-t-tran
section_title: "HITOSHI MURAKAMI AND ANH T. TRAN"
section_number: 18
pages: 18-19
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
Hence we have
(
1 −e−2π √
−1z
) ∫
C r
θ
e(2z−1)x
sinh(x) dx
=e−2π √−1z
(
−
∫
C r
θ
e(2z−1)x
sinh(x) dx +
∫
C r
θ +π √−1
e(2z−1)x
sinh(x) dx
)
=e−2π √−1z
( ∫
V +
r
e(2z−1)x
sinh(x) dx −
∫
V −
r
e(2z−1)x
sinh(x) dx
)
−e−2π √−1z2π
√
−1 Res
( e(2z−1)x
sinh(x) ;x =π
√
−1
)
,
where V ±
r is the vertical segment connecting ±re
√−1θ and ±re
√−1θ +π √−1, ori-
ented upward. Since Res
(
e(2z−1)x
sinh(x) ;x =π √−1
)
= limx→π √−1
e(2z−1)x (x−π √−1)
sinh(x) =
−e(2z−1)π √−1, we have
(
1 −e−2π √−1z
) ∫
C r
θ
e(2z−1)x
sinh(x) dx
=e−2π √−1z
( ∫
V +
r
e(2z−1)x
sinh(x) dx −
∫
V −
r
e(2z−1)x
sinh(x) dx
)
− 2π
√
−1.
We will show that lim
r→∞
∫
V ±
r
e(2z−1)x
sinh(x) dx = 0.
Since
∫
V ±
r
e(2z−1)x
sinh(x) dx =π
√
−1
∫ 1
0
e(2z−1)(±re
√−1θ +π √−1s)
sinh(±re
√−1θ +π √−1s)ds
and | sinh(w)| = 1
2 |ew −e−w| ≥ 1
2
⏐
⏐eRew −e− Rew⏐
⏐ for any w ∈ C, we have
⏐
⏐
⏐
⏐
∫
V ±
r
e(2z−1)x
sinh(x) dx
⏐
⏐
⏐
⏐ ≤π
∫ 1
0
⏐
⏐
⏐
⏐
⏐
e(2z−1)(±re
√
−1θ +π √−1s)
sinh(±re
√−1θ +π √−1s)
⏐
⏐
⏐
⏐
⏐ds
≤π
∫ 1
0
2eRe((2z−1)(±re
√
−1θ +π √−1s))
⏐
⏐
⏐eRe(±re
√
−1θ +π √−1s) −e− Re(±re
√−1θ +π √−1s)
⏐
⏐
⏐
ds
= 2πe ±r Re((2z−1)e
√
−1θ )
er cosθ −e−r cosθ
∫ 1
0
e−πs Im(2z−1)ds.
From the assumption 0 < Re(zeθ√−1) < cosθ, we have
⏐
⏐
⏐Re
(
(2z − 1)e
√
−1θ
) ⏐
⏐
⏐<
cosθ. Therefore we see that
⏐
⏐
⏐
⏐
∫
V ±
r
e(2z−1)x
sinh(x) dx
⏐
⏐
⏐
⏐ →
r→∞
0
and so we have
∫
Cθ
e(2z−1)x
sinh(x) dx = lim
r→∞
∫
C r
θ
e(2z−1)x
sinh(x) dx = −2π √−1
1 −e−2π √−1z.
□
The following lemma shows (2.3) and (2.4).
