---
doc_id: arxiv-math-0401084v3
doc_title: "THE COLORED JONES POL YNOMIALS OF THE"
section_id: sec-004-appendix-optimistic-limit
section_title: "Appendix. Optimistic limit"
section_number: null
pages: 15-16
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
doc_brief: "THE COLORED JONES POLYNOMIALS OF THE — W e calculate limits of the colored Jones polynomials of the ﬁ gure- eight knot and conclude that in most cases they determine the volumes and the Chern–Simons"
---
In this appendix, we will consider integral surgeries along the ﬁgure -eight knot.
Let Ep, 1 be the p-surgery along the ﬁgure-eight knot with p ∈ Z. Then our
parameter u and v satisﬁes pu + v = 2π√−1. From Corollary 2.4 we have
Vol(Ep, 1) +
√
−1 CS(Ep, 1) ≡ H(u)√−1 − πu − uv
4√−1 − π
2 λ(γ) mod π2√
−1Z.
By [8, (4.6)], we have
λ(γ) = 2π√−1
p − v
p = u.
(Note that we follow orientation conventions of [16, 24] and so the s ign of v is
opposite to that in [8].) Therefore
Vol(Ep, 1) +
√
−1 CS(Ep, 1)
≡ −
√
−1 Li2
(
y−1 exp(−u)
)
+
√
−1 Li2 (y exp(−u)) −
√
−1u
{
log(−y) + π
√
−1
}
− πu − u
4√−1 (2π
√
−1 − pu) − π
2 u
≡ 1√−1
{
Li2
(
y−1 exp(−u)
)
− Li2 (y exp(−u)) + u log(−y) − uπ
√
−1 + pu2
4
}
mod π2√
−1Z
and so
− CS(Ep, 1) +
√
−1 Vol(Ep, 1)
≡ Li2
(
y−1 exp(−u)
)
− Li2 (y exp(−u)) + u log(−y) − uπ
√
−1 + pu2
4 mod π2Z.
Now we deﬁne
Vp(ξ, η) := Li 2
(
ξ−1η−1)
− Li2
(
ξη −1)
+ (log(−ξ))(log η) − π
√
−1 log η + p
4 (log η)2
= H(ξ, η) + p
4 (log η)2 − 2π
√
−1 log η.
We will calculate ∂ Vp(ξ, η)/∂ξ
⏐
⏐
ξ=y,η =m2 and ∂ Vp(ξ, η)/∂η
⏐
⏐
ξ=y,η =m2. First we have
from (3.2)
∂ Vp(ξ, η)
∂ξ
⏐
⏐
⏐
⏐
ξ=y,η =m2
= ∂ H (ξ, η)
∂ξ
⏐
⏐
⏐
⏐
ξ=y,η =m2
= 0.
Next we have
∂ Vp(ξ, η)
∂η
⏐
⏐
⏐
⏐
ξ=y,η =m2
= ∂ H (ξ, η)
∂η
⏐
⏐
⏐
⏐
ξ=y,η =m2
+ p log
(
m2)
2m2 − 2π√−1
m2 .
16 HITOSHI MURAKAMI AND YOSHIYUKI YOKOTA
On the other hand
v
2 = d H(u, m2)
du − π
√
−1
= ∂ H (ξ, η))
dξ
⏐
⏐
⏐
⏐
ξ=y,η =m2
+ ∂ H (ξ, η)
dη
⏐
⏐
⏐
⏐
ξ=y,η =m2
× d m2
du − π
√
−1
= exp u × ∂ H (ξ, η)
dη
⏐
⏐
⏐
⏐
ξ=y,η =m2
− π
√
−1.
Therefore
∂ Vp(ξ, η)
∂η
⏐
⏐
⏐
⏐
ξ=y,η =m2
= v/2 + π√
−1
exp u + pu
2 exp u − 2π√−1
exp u = 0.
In [11] the ﬁrst author calculated a ‘fake’ limit of the Witten–Reshetikhin–Turaev
invariants of the ( p, 1)-Dehn surgery of the ﬁgure-eight knot and obtained the fol-
lowing observation.
Observation. Let p be an integer between −100 and 100, and τp the ‘optimistic’
limit of the Witten–Reshetikhin–Turaev invariant of the (p, 1)-Dehn surgery along
the ﬁgure-eight knot. Then there exists (ξ0, η0) such that the following equalities
hold numerically (up to 8 digits):
(1) ∂ Vp
∂ξ (ξ0, η0) = ∂ Vp
∂η (ξ0, η0) = 0 , and
(2) τp = Vp(ξ0, η0) = CS( Ep, 1) + √−1 Vol(Ep, 1).
Note that the observation above was conﬁrmed by the second aut hor [22]. Note
also that the sign of CS is reversed since the orientation convention here is diﬀerent.
