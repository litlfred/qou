---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I:"
section_id: sec-007-23-gaussian-integrals
section_title: "Gaussian integrals"
section_number: 2.3
pages: 13-14
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
doc_brief: "MOD-φ CONVERGENCE, I: — In this paper, we use the framework of mod- φ convergence to prove pre- cise large or moderate deviations for quite general sequences of real valued random variables (Xn)n∈N"
---
several times throughout the paper, so we decided to present them together here.
Lemma 2.7 (Gaussian integrals).
(1) moments:
1√
2π
∫
R
e− x2
2 x2m dx = (2m− 1)!! = (2m− 1)(2m− 3)··· 3 1,
and the odd moments vanish.
(2) Fourier transform: with g (x) = e− x2
2√
2π , one has
g∗(ζ) =
∫
R
g(x) eixζ dx = e− ζ2
2 .
More generally, with the Hermite polynomials Hr(x) = (−1)r e
x2
2 ∂r
∂xr (e− x2
2 ), one has
(g Hr)∗(ζ) = ( iζ)r e− ζ2
2 .
(3) tails: if a → +∞, then
∫ ∞
0
e− (y+a)2
2 dy = e− a2
2
a
(
1− 1
a2 + O
( 1
a4
))
∫ ∞
0
y e− (y+a)2
2 dy = e− a2
2
a2
(
1 + O
( 1
a2
))
∫ ∞
0
y2 e− (y+a)2
2 dy = O

e− a2
2
a3


∫ ∞
0
y3 e− (y+a)2
2 dy = O

e− a2
2
a2


In particular, the tail of the Gaussian distribution is 1√
2π
∫ ∞
a e− x2
2 dx≃ 1
a
√
2π e− a2
2 .
(4) complex transform: for β > 0,
∫
R
e− β2
2
2π
e− w2
2
β + iw dw =
∫ ∞
β
e− α2
2
√
2π
dα = P[NR(0, 1)≥ β].
Proof. Recall that the generating series of Hermite polynomials ([Sze75, Chapter 5]) is
∞
∑
r=0
Hr(x) tr
r! = e
x2
2
∞
∑
r=0
(−t)r
r!
∂r
∂xr
(
e− x2
2
)
= e
x2
2 e− (x−t)2
2 = e− t2
2 +tx.
Integrating against g(x) eixζ dx yields
∞
∑
r=0
(g(x) Hr(x))∗(ζ) tr
r! = 1√
2π
∫
R
e− (x−t)2
2 +iζx dx
= eiζt
√
2π
∫
R
e− y2
2 +iζy dy = eiζt− ζ2
2 =
∞
∑
r=0
(iζ)re− ζ2
2
tr
r!
14 VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
whence the identity (2) for Fourier transforms.
With r = 0, one gets the Fourier transform of the Gaussian g∗(ζ) = e− ζ2
2 , hence the
moments (1) by derivation at ζ = 0. The estimate of tails (3) is obtained by an integra-
tion by parts; notice that similar techniques yield the tails of distributions xm e−x2/2 dx
with m≥ 1. Finally, as for the complex transform (4), remark that
F(β) =
∫
R
e− β2
2
2π
e− w2
2
β + iw dw = 1
2iπ
∫
Γ=β+iR
e
(z−β)2−β2
2
z dz,
the second integral being along the complex curve Γ = β + iR. By standard complex
analysis arguments, this integral is the same along any line Γ′ = β′ + iR (for β′ > 0).
Namely
F(β) = 1
2iπ
∫
Γ′=β′+iR
e
(z−β)2−β2
2
z dz.
Since limβ→+∞ F(β) = 0,
F(β) =−
∫ ∞
β
F′(α) dα =
∫ ∞
β
( 1
2iπ
∫
Γ′=β′+iR
e
(z−α)2−α2
2 dz
)
dα.
Again, the integration line Γ′ in the second integral can be replaced by Γ = α + iR and
we get
F(β) =
∫ ∞
β
( 1
2iπ
∫
Γ=α+iR
e
(z−α)2−α2
2 dz
)
dα. =
∫ ∞
β
e− α2
2
√
2π
dα,
which is the tail P[NR(0, 1)≥ β] of a standard Gaussian law. □
Also, there will be several instances of the Laplace method for asymptotics of integrals,
but each time in a different setting; so we found it more convenient to reprove it each
time.
3. F LUCTUATIONS IN THE CASE OF LATTICE DISTRIBUTIONS
