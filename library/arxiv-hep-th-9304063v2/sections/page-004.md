---
doc_id: arxiv-hep-th-9304063v2
doc_title: "arXiv:hep-th/9304063v2 29 Jan 1999"
section_id: page-004
section_title: "Page 4"
section_number: null
pages: 4-4
source_pdf: 9304063v2.pdf
source_sha256: 14a82437462eae23
toc_source: undetermined
doc_brief: "arXiv:hep-th/9304063v2 29 Jan 1999 — 18 sections: Page 1; Page 2; Page 3"
---
q(s; λ) ∼
√
λ
2αΓ(1 + α) sα/2 ,
s →0.
(1.17)
This equation is reducible to a special case of the PV diﬀerential equation;3 explicitly, if q(s) = (1 + y(x))/(1 −y(x))
with s = x2, then y(x) satisﬁes PV with α′ = −β′ = α2/8, γ′ = 0 and δ′ = −2. (We have primed the usual PV
parameters to avoid confusion with the α in our kernel. We mention that this special PV can be expressed algebraically
in terms of a third Painlev´e transcendent and its ﬁrst derivative [13]. We mention also that an argument can be given
that (1.16) must be reducible to one of the 50 canonical types of diﬀerential equations found by Painlev´e, without an
explicit veriﬁcation being necessary. This will be discussed at the end of section II B.) It is sometimes convenient to
transform (1.16) by making the substitution
q(s) = cos ψ(s),
so that ψ satisﬁes
ψ′′ + 1
sψ′ = 1
8s sin (2ψ) −α2
4s2
cos ψ
sin3 ψ .
(1.18)
The Fredholm determinant is expressible in terms of q by the formula
D(J; λ) = exp

−1
4
Z s
0
log s
t q(t)2 dt

.
(1.19)
Denoting by R(s) minus the logarithmic derivative of D(J; λ) with respect to s, we have also the representation
R(s) = 1
4 cos2 ψ(s) + s
dψ
ds
2
−α2
4s cot2 ψ(s) .
(1.20)
Furthermore, R(s) itself satisﬁes a diﬀerential equation which in the Jimbo-Miwa-Okamoto σ notation for Painlev´e
III (see, in particular, (3.13) in [14]) is
(sσ′′)2 + σ′ (σ −sσ′) (4σ′ −1) −α2 (σ′)2 = 0
(1.21)
where σ(s) = sR(s); it has small s expansion
σ(s; λ) = cα s1+α

1 −
1
2(2 + α)s +
3 + 2α
16(1 + α)(2 + α)(3 + α)s2 + · · ·

+
1
1 + αc2
α s2+2α

1 −
3 + 2α
2(2 + α)2 s + · · ·

+
1
(1 + α)2 c3
α s3+3α [1 + · · ·] + · · ·
(1.22)
where
cα =
λ
22α+2
1
Γ(1 + α)Γ(2 + α) .
We mention that in the special case α = 0 and λ = 1 we have D(J; 1) = e−s/4, q(s; 1) = 1, ψ(s, 1) = 0, and
σ(s, 1) = s/4 exactly [7,8,11].
3The Painlev´e V diﬀerential equation is
d2y
dx2 =

1
2y +
1
y −1
 dy
dx
2
−1
x
dy
dx + (y −1)2
x2

α′y + β′
y

+ γ′y
x + δ′y(y + 1)
y −1
where α′, β′, γ′, and δ′ are constants.
4
