---
doc_id: arxiv-1409.2849v1
doc_title: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS"
section_id: sec-004-31-ellis-newman-lemma-and-deconvolution-of-a-lar
section_title: "Ellis-Newman lemma and deconvolution of a large Gaussian noise"
section_number: 3.1
pages: 11-13
source_pdf: 1409.2849v1.pdf
source_sha256: 7bf9646716fbb247
doc_brief: "MOD-GAUSSIAN CONVERGENCE AND ITS APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS — In this paper we complete our understanding of the role played by the lim- iting (or residue) function in the"
---
for a moment that hypothesis (A) is replaced by the stronger hypotheses of Deﬁnition
2, with c = + ∞ and thereforeBc = C. Fix then 0 < a < b, and consider the partial
integral E[e(Xn)2/2tn 1 tna≤Xn≤tnb]. By integration by parts of Riemann-Stieltjes integrals,
one has:
∫ tnb
tna
e
x2
2tn Pn[dx] =
[
−e
x2
2tn Pn[Xn≥ x]
]tnb
tna
+
∫ tnb
tna
x
tn
e
x2
2tn Pn[Xn≥ x] dx
=
[
−e
tn x2
2 Pn[Xn≥ tnx]
]b
a
+
∫ b
a
tnx e
tn x2
2 Pn[Xn≥ tnx] dx
=
([
− ψ(x)√2πtn x
]b
a
+
√
tn
2π
∫ b
a
ψ(x) dx
)
(1 + oa,b(1))
=
(√
tn
2π
∫ b
a
ψ(x) dx
)
(1 + oa,b(1))
because of the estimates of precise deviations (2). In this computation, oa,b(1) is uni-
form for a, b in compact sets of (0, +∞). In fact this estimate remains true for a, b in a
12 PIERRE-LOÏC MÉLIOT AND ASHKAN NIKEGHBALI
compact set of R; hence, a and b can be possibly negative. If the estimate is also true
with a =−∞ and b = + ∞, then
Qn[tna≤ Yn≤ tnb] = E[e(Xn)2/2tn 1 tna≤Xn≤tnb]
E[e(Xn)2/2tn]
=
√
tn
2π
∫ b
a ψ(x) dx
√
tn
2π
∫ +∞
−∞ ψ(x) dx
(1 + o(1))
=
∫ b
a ψ(x) dx
∫ +∞
−∞ ψ(x) dx
(1 + o(1)),
so ( Yn
tn )n∈N converges in law to the density ψ(x)/
∫
R ψ(x) dx.
We now wish to identify the most general conditions under which this convergence
in law happens. To this purpose, it is useful to produce random variables with density
ψn(x)/
∫
R ψn(x) dx. They are given by the following Proposition, which appeared in
[EN78] as Lemma 3.3:
Proposition 5. Let Gn be a centred Gaussian variable with variance 1
tn , and independent from
Yn. The law of Wn = Gn + Yn
tn has density ψn(x)/
∫
R ψn(x) dx.
Proof. Denote Zn = E[e(Xn)2/2tn], and fX(x) dx (respectively, PX) the density (respec-
tively, the law) of a random variable X. One has
P[Wn≤ w] =
∫ w
−∞
(∫
R
fGn(x− u) P Yn
tn
[du]
)
dx
=
√
tn
2π
∫ w
−∞
(∫
R
e−
tn (x− y
tn )2
2 PYn[dy]
)
dx
=
√
tn
2π
∫ w
−∞
(∫
R
eyx− y2
2tn Qn[dy]
)
e− tn x2
2 dx
= 1
Zn
√
tn
2π
∫ w
−∞
(∫
R
eyx Pn[dy]
)
e− tn x2
2 dx
= 1
Zn
√
tn
2π
∫ w
−∞
ψn(x) dx.
Making w go to +∞ gives an equation for Zn =
√
tn
2π
∫
R ψn(x) dx. One concludes that:
P[Wn≤ w] =
∫ w
−∞ ψn(x) dx∫ ∞
−∞ ψn(x) dx .
□
This important property was not used in our previous works: to get the residue of
deconvolution ψn of a random variable Xn by a large Gaussian variable of variance tn
(that is to say that one wants toremove a Gaussian variable of variance tn from Xn), one
can make the exponential change of measure (9), and add an independent Gaussian
MOD-GAUSSIAN CONVERGENCE AND APPLICATIONS FOR MODELS OF STATISTICAL MECHANICS13
variable of variance tn: the random variable thus obtained, which is tnWn with the
previous notation, has density proportional to ψn(w/tn) dw.
