---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-017-6-proofs-of-lemmas
section_title: "Proofs of lemmas"
section_number: 6
pages: 16-18
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
In this section, we give proofs of lemmas used in this paper.
Proof of Lemma 2.1. Putting x :=yeθ√
−1, the integral becomes
∫
C0
exp
(
(2z − 1)yeθ√−1
)
y sinh(yeθ√−1) sinh(γye θ√−1)dy.
Noting that
sinh(as) ∼
s→∞
1
2eas
and that
sinh(as) ∼
s→−∞
− 1
2e−as
for a complex number a with Re(a)> 0, we have
exp
(
(2z − 1)yeθ√−1
)
y sinh(yeθ√−1) sinh(γye θ√−1) ∼
y→∞
1
y exp
(
(2z − 2 −γ)eθ√−1y
)
and
exp
(
(2z − 1)yeθ√−1
)
y sinh(yeθ√−1) sinh(γye θ√−1) ∼
y→−∞
1
y exp
(
(2z +γ)eθ√−1y
)
since Re
(
eθ√−1
)
= cosθ> 0 and Re
(
γeθ√−1
)
= ξ
2Nπ sinθ> 0. So we have
⏐
⏐
⏐
⏐
⏐
⏐
exp
(
(2z − 1)yeθ√
−1
)
y sinh(yeθ√−1) sinh(γye θ√−1)
⏐
⏐
⏐
⏐
⏐
⏐
< C
y exp
(
Re
(
(2z − 2 −γ)eθ√−1
)
y
)
when y> 0 for a positive constant C, and
⏐
⏐
⏐
⏐
⏐
⏐
exp
(
(2z − 1)yeθ√
−1
)
y sinh(yeθ√−1) sinh(γye θ√−1)
⏐
⏐
⏐
⏐
⏐
⏐
< C′
|y| exp
(
− Re
(
(2z +γ)eθ√−1
)
y
)
when y < 0 for a positive constant C′. Therefore, if −ξ sinθ
4Nπ < Re(zeθ√−1) <
cosθ + ξ sinθ
4Nπ , then the integrals
∫ ∞
1
exp
(
(2z − 1)yeθ√−1
)
y sinh(yeθ√−1) sinh(γye θ√−1)dy
and
∫ −1
−∞
exp
(
(2z − 1)yeθ√−1
)
y sinh(yeθ√−1) sinh(γye θ√−1)dy
converge and the lemma follows. □
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 17
Proof of Lemma 2.2. Putting x =ye
√−1θ , we have
∫
Cθ
e(2z−1)x
xm sinxdx = 1
e(m−1)√−1θ
∫
C0
e(2z−1)ye
√−1θ
ym sinh
(
ye
√−1θ) dy.
So we need to show that
∫ r
1
e(2z−1)ye
√−1θ
ym sinh
(
ye
√−1θ) dy
and
∫ −1
−r
e(2z−1)ye
√−1θ
ym sinh
(
ye
√−1θ) dy
converge when r → ∞ for m = 0, 1, 2.
We have
⏐
⏐
⏐
⏐
⏐
∫ r
1
e(2z−1)ye
√
−1θ
ym sinh
(
ye
√−1θ) dy
⏐
⏐
⏐
⏐
⏐ ≤
∫ r
1
2e
2y Re
(
ze
√
−1θ
)
−y cosθ
ym (ey cosθ −e−y cosθ)dy
=
∫ r
1
2e2y
(
Re(ze
√−1θ )−cosθ
)
ym(1 −e−2y cosθ ) dy,
which converges when r → ∞ since Re(ze
√−1θ )< cosθ.
We also have
⏐
⏐
⏐
⏐
⏐
∫ −1
−r
e(2z−1)ye
√
−1θ
ym sinh(ye
√−1θ)dy
⏐
⏐
⏐
⏐
⏐ ≤
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
|ym (ey cosθ −e−y cosθ)|dy
=
∫ −1
−r
2e2y Re(ze
√−1θ )
|ym(e2y cosθ − 1)|dy,
which converges when r → ∞ since Re(ze
√−1θ )> 0. □
Now we calculate the integrals in Lemma 2.2 to prove Lemma 2.5.
The following lemma shows (2.2).
Lemma 6.1. If 0< Re(zeθ√
−1)< cosθ, then we have
∫
Cθ
e(2z−1)x
sinh(x) dx = −2π √−1
1 −e−2π √−1z.
Proof. Put Cr
0 := C0 \
(
(−∞, −r) ∪ (r, ∞)
)
for r >1, Cr
θ :=e
√−1θCr
0 , and Cr
θ +
π √−1 := {w +π √−1 |w ∈Cr
θ }. We ﬁrst note that
∫
C r
θ
e(2z−1)x
sinh(x) dx =
∫
C r
θ +π √−1
e(2z−1)(x−π √−1)
sinh(x −π √−1)d(x −π
√
−1)
=e−2π √−1z
∫
C r
θ +π √−1
e(2z−1)x
sinh(x) dx.
