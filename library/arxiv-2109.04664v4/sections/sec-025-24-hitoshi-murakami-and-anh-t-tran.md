---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-025-24-hitoshi-murakami-and-anh-t-tran
section_title: "HITOSHI MURAKAMI AND ANH T. TRAN"
section_number: 24
pages: 24-26
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
and we obtain
d
dw
( ∞∑
k=1
wk
k2
)
=
∞∑
k=1
wk−1
k = − log(1 −w)
w .
Therefore we conclude that ∑ ∞
k=1
wk
k2 = −
∫w
0
log(1−t)
t dt.
If w = 1, the series ∑ ∞
k=1ak converges by the integral test.
Finally, we assume that |w| = 1 with w ⁄= 1, and apply Abel’s test. Since
the sequence {ak} is positive and monotonically decreasing with lim k→∞ak = 0,
the power series ∑ ∞
k=1akwk converges if |w| = 1 ( w ⁄= 1). We can also apply
Abel’s theorem to conclude that ∑ ∞
k=1akzk converges to∑ ∞
k=1akwk provided that
z approachesw along the radius. Note that this includes the case w = 1. Therefore
we also conclude that ∑ ∞
k=1
wk
k2 = −
∫w
0
log(1−t)
t dt for the case |w| = 1 by choosing
the integral path as the radius connecting 0 and w. □
We prove that 1
NTN (z) uniformly converges to 1
ξ L2(z).
Proof of Proposition 2.8. We have
⏐
⏐
⏐
⏐TN (z) − N
ξ L2(z)
⏐
⏐
⏐
⏐ = 1
4
⏐
⏐
⏐
⏐
∫
Cθ
( e(2z−1)x
x sinh(x) sinh(γx) − e(2z−1)x
γx 2 sinh(x)
)
dx
⏐
⏐
⏐
⏐
= 1
4
⏐
⏐
⏐
⏐
∫
Cθ
e(2z−1)x
γx 2 sinh(x)
( γx
sinh(γx) − 1
)
dx
⏐
⏐
⏐
⏐
≤ πN
2|ξ|
∫
Cθ
⏐
⏐
⏐
⏐
e(2z−1)x
x2 sinh(x)
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
γx
sinh(γx) − 1
⏐
⏐
⏐
⏐dx.
Since γx
sinh(γx ) = 1 − (γx )2
6 +O((γx)4),
⏐
⏐
⏐ γx
sinh(γx ) − 1
⏐
⏐
⏐< C|x|2
N 2 for a positive constant
C since γ = ξ
2Nπ √−1 . So we have
⏐
⏐
⏐
⏐TN (z) − N
ξ L2(z)
⏐
⏐
⏐
⏐ ≤ C′
N
∫
Cθ
⏐
⏐
⏐
⏐
e(2z−1)x
sinh(x)
⏐
⏐
⏐
⏐dx,
where C′ := Cπ
2|ξ| . Put
I+ := lim
r→∞
∫ re
√−1θ
e
√−1θ
⏐
⏐
⏐
⏐
e(2z−1)x
sinh(x)
⏐
⏐
⏐
⏐dx,
I− := lim
r→∞
∫ −e
√
−1θ
−re
√−1θ
⏐
⏐
⏐
⏐
e(2z−1)x
sinh(x)
⏐
⏐
⏐
⏐dx,
I0 :=
∫
|x|=1,θ ≤argx≤π +θ
⏐
⏐
⏐
⏐
e(2z−1)x
sinh(x)
⏐
⏐
⏐
⏐dx.
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 25
Putting x :=e
√−1θy, we have
I+ =
∫ ∞
1
⏐
⏐
⏐e(2z−1)yeθ √
−1
⏐
⏐
⏐
| sinh(ye
√−1θ )|dy
≤
∫ ∞
1
2e2y Re(zeθ √−1)−y cosθ
ey cosθ −e−y cosθ dy
=
∫ ∞
1
2e2y
(
Re(zeθ √−1)−cosθ
)
1 −e−2y cosθ dy
≤ 2
1 −e−2 cosθ
∫ ∞
1
e−2yν dy
= e−2ν
(1 −e−2 cosθ)ν.
Here we use the assumption Re( zeθ√−1) ≤ cosθ −ν.
Similarly, we have
I− =
∫ −1
−∞
⏐
⏐
⏐e(2z−1)yeθ √
−1
⏐
⏐
⏐
| sinh(ye
√−1θ )|dy
≤
∫ −1
−∞
2e2y Re(zeθ √−1)−y cosθ
e−y cosθ −ey cosθ dy
=
∫ −1
−∞
2e2y Re(zeθ √−1)
1 −e2y cosθ dy
≤ 2
1 −e−2 cosθ
∫ −1
−∞
e2yν dy
= e2ν
(1 −e−2 cosθ)ν.
Here we use the assumption Re( zeθ√−1) ≥ν.
Finally, putting x = eτ √−1 (θ ≤ τ ≤ θ + π ) and L :=
minθ≤τ ≤θ+π | sinh(e
√−1τ )|> 0, we have
I0 =
∫ θ+π
θ
⏐
⏐
⏐e(2z−1)eτ √
−1
⏐
⏐
⏐
| sinh(e
√−1τ )| |
√
−1eτ √−1|dτ
≤ 1
L
∫ θ+π
θ
e2 Re(zeτ √−1)−cosτdτ
= 1
L
∫ θ+π
θ
e(2 Rez−1) cosτ −2 sinτ Imzdτ,
which is bounded from the above because both Re z and Imz are bounded.
Therefore we conclude that
⏐
⏐
⏐TN (z) − N
ξ L2(z)
⏐
⏐
⏐ ≤ C ′′
N for some constant C′′ that
does not depend on z. □
Proof of Lemma 3.1. Recall that γ = ξ
2Nπ √−1 .
