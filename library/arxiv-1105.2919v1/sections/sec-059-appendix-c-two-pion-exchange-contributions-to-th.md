---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral eﬀective ﬁeld theory and nuclear forces"
section_id: sec-059-appendix-c-two-pion-exchange-contributions-to-th
section_title: "Appendix C Two-pion exchange contributions to the 2NF at NNLO"
section_number: null
pages: 77-79
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
toc_source: outline
doc_brief: "Chiral eﬀective ﬁeld theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
Two-pion exchange diagrams that contribute at NNLO were shown in Fig. 4. These diagrams diﬀer from
the NLO diagrams, Fig. 3, by one insertion from the dimension-two Lagrangian, the vertices of which are
given in Appendix A.2.2. There are two kinds of second order vertices: The relativistic corrections of the
leading order Lagrangian, which are proportional to 1/MN, Eqs. (A.48)-(A.50), and new contact interactions
proportional to the LECs ci, Eqs. (A.51) and (A.52). Since the shapes of the NNLO diagrams are the same
as in the NLO case, the evaluation is very similar to what we presented in detail in Appendix B for the NLO
diagrams. The results for the irreducible 2PE at third order (NNLO) as derived by the Munich group [55]
were given in Sec. 4.1.2, Eqs. (4.13)–(4.18). Note that the irreducible 2PE depends on what is chosen for
the (reducible) iterated 1PE. For this, the Munich group applies the expression Eq. (4.25). Alternatively,
one may also use the form Eq. (4.26) implied by the BbS scheme [133], which diﬀers in third and higher
orders from the Munich expression. Therefore, when the BbS formalism is used, a (irreducible) correction
term has to be added to the Munich irreducible 2PE in higher orders. In terms of the notation introduced
in Eqs. (4.25) and (4.26), this correction term is given by:
V (KBW)
2π,it
−V (EM)
2π,it
=
Z
d3p′′
(2π)3
 1
Ep
−
1
Ep′′

M 2
N
p2 −p′′2 + iϵV1π(⃗p ′,⃗p ′′) V1π(⃗p ′′,⃗p)
(C.1)
=
−
Z
d3p′′
(2π)3
M 2
N
Ep′′Ep(Ep′′ + Ep)V1π(⃗p ′,⃗p ′′) V1π(⃗p ′′,⃗p)
(C.2)
≈
−
Z
d3p′′
(2π)3
1
2MN
V1π(⃗p ′,⃗p ′′) V1π(⃗p ′′,⃗p) ,
(C.3)
with the last line showing the correction in third order or NNLO, which is what we want to calculate here.
Using Eq. (4.5) and the relation τ 1 · τ 2 τ 1 · τ 2 = 3 −2 τ 1 · τ 2, and deﬁning⃗l =⃗p −⃗p ′′, yields
V (KBW)
2π,it
−V (EM)
2π,it
=
−
g4
A
32f 4πMN
(3 −2 τ 1 · τ 2)
Z
d3l
(2π)3⃗
σ1 · (⃗l +⃗q)⃗σ2 · (⃗l +⃗q)
(⃗l +⃗q)2 + m2π⃗
σ1 ·⃗l⃗σ2 ·⃗l
l2 + m2π
(C.4)
=
−
g4
A
32f 4πMN
(3 −2 τ 1 · τ 2)
Z 1
0
dx
Z
d3l
(2π)3⃗
σ1 · (⃗l +⃗q)⃗σ2 · (⃗l +⃗q)⃗σ1 ·⃗l⃗σ2 ·⃗l
[⃗l2 + (2⃗l ·⃗q +⃗q2)x + m2π]2
,(C.5)
77
where, in the last line, we introduced the Feynman trick. We now extend the integral to (D −1) dimensions
and make the change of variables λ⃗k =⃗l + x⃗q (cf. Appendix B.1.2),
V (KBW)
2π,it
−V (EM)
2π,it
=
−
g4
A
32f 4πMN
(3 −2 τ 1 · τ 2)λ3
Z 1
0
dx
Z
dD−1k
(2π)D−1 ×
×⃗
σ1 · [⃗k + (1 −x)˜q]⃗σ2 · [⃗k + (1 −x)˜q]⃗σ1 · (⃗k −x˜q)⃗σ2 · (⃗k −x˜q)
[k2 + ˜m2π + ˜q2x(1 −x)]2
.
(C.6)
Since⃗
σi · [⃗k + (1 −x)˜q]⃗σi · (⃗k −x˜q)
=
k2 + ˜q2x(x −1) −(2x −1)⃗k · ˜q + i⃗σi · (˜q ×⃗k) ,
(C.7)
we obtain, making use of Eq. (B.94),
V (KBW)
2π,it
−V (EM)
2π,it
=
−
g4
A
32f 4πMN
(3 −2 τ 1 · τ 2)λ3
Z 1
0
dx
Z
dD−1k
(2π)D−1 ×
×
[k2 + ˜q2x(x −1)]2 +
k2
D−1[(2x −1)2˜q2 −(⃗σ1 × ˜q)(⃗σ2 × ˜q)]
[k2 + ˜m2π + ˜q2x(1 −x)]2
.
(C.8)
Applying (⃗σ1 × ˜q)(⃗σ2 × ˜q) = λ−2[q2⃗σ1 ·⃗σ2 −(⃗σ1 ·⃗q)(⃗σ2 ·⃗q)], leads to
VC
=
−
3g4
A
32f 4πMN
λ3
Z 1
0
dx
Z
dD−1k
(2π)D−1
[k2 + ˜q2x(x −1)]2 +
k2
D−1(2x −1)2˜q2
[k2 + ˜m2π + ˜q2x(1 −x)]2
(C.9)
WC
=
−2
3VC
(C.10)
VT
=
−
3g4
A
32f 4πMN
λ
Z 1
0
dx
Z
dD−1k
(2π)D−1
k2
D−1
[k2 + ˜m2π + ˜q2x(1 −x)]2
(C.11)
VS
=
−q2VT
(C.12)
WT
=
−2
3VT
(C.13)
WS
=
−q2WT .
(C.14)
Using the volume element in (D −1) dimensions, Eqs. (B.28) and (B.29), we ﬁnd
VC
=
−
3g4
A
32f 4πMN
2λ3
Γ( D−1
2 )(4π)(D−1)/2
Z 1
0
dx
Z ∞
0
dk
kD+2 + kD˜q2 h
2x(x −1) + (2x−1)2
D−1
i
+ kD−2˜q4x2(x −1)2
[k2 + ˜m2π + ˜q2x(1 −x)]2
,
(C.15)
VT
=
−
3g4
A
32f 4πMN
2λ
Γ( D−1
2 )(4π)(D−1)/2
1
D −1
Z 1
0
dx
Z ∞
0
dk
kD
[k2 + ˜m2π + ˜q2x(1 −x)]2 .
(C.16)
Performing the k-integration yields
VC
=
−
3g4
A
32f 4πMN
λ3
Γ(2)Γ( D−1
2 )(4π)(D−1)/2
Z 1
0
dx
(
Γ( D+3
2 )Γ( 1−D
2 )
[ ˜m2π + ˜q2x(1 −x)](1−D)/2
+
Γ( D+1
2 )Γ( 3−D
2 )˜q2 h
2x(x −1) + (2x−1)2
D−1
i
( ˜m2π + ˜q2x(1 −x))(3−D)/2
+ Γ( D−1
2 )Γ( 5−D
2 )˜q4x2(x −1)2
[ ˜m2π + ˜q2x(1 −x)](5−D)/2


,
(C.17)
VT
=
−
3g4
A
32f 4πMN
λ
Γ(2)Γ( D−1
2 )(4π)(D−1)/2
1
D −1
Z 1
0
dx
Γ( D+1
2 )Γ( 3−D
2 )
[ ˜m2π + ˜q2x(1 −x)](3−D)/2 .
(C.18)
78
We choose D = 4 −η and take the limit η →0,
VC
=
−
3g4
A
256πf 4πMN
Z 1
0
5m4
π −m2
πq2(1 −20x + 20x2) + q4x(−1 + 17x −32x2 + 16x3)
p
m2π + q2x(1 −x)
,
(C.19)
VT
=
3g4
A
256πf 4πMN
Z 1
0
p
m2π + q2x(1 −x) ,
(C.20)
and, performing the x-integration, we ﬁnally obtain
VC
=
−
3g4
A
256πf 4πMN
(mπw2 + ew4A(q)) ,
(C.21)
VT
=
3g4
A
512πf 4πMN
(mπ + w2A(q)) .
(C.22)
