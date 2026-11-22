---
doc_id: arxiv-2104.07437v4
doc_title: "Peacock patterns and new integer invariants in topological string theory"
section_id: sec-022-b-fast-algorithm-for-the-second-resurgent-struct
section_title: "B Fast algorithm for the second resurgent structure of local P2"
section_number: null
pages: 44-45
source_pdf: 2104.07437v4.pdf
source_sha256: a0f28a6b61618467
toc_source: outline
doc_brief: "Peacock patterns and new integer invariants in topological string theory — Topological string theory near the conifold point of a Calabi–Yau threefold gives rise to factorially divergent power series"
---
Fast algorithm for the second resurgent structure of local P2
In this section we present a fast algorithm to compute the asymptotic series Φ0;2(gs) for the
geometry of local P2.
We ﬁnd from (3.171) that the series Φ0;2(gs) appears in the asymptotic analysis of the
anti-holomorphic block eH0(˜q) given by (3.165a). This is actually also true for the partial anti-
holomorphic block
eHpart
0
(˜q) = 3φ2
 wa, wa, ˜q
w−1
a ˜q, w−1
a ˜q; ˜q, w−1
a ˜q

−3φ2
 wa, wa, ˜q
w−1
a ˜q, w−1
a ˜q; ˜q, ˜q

.
(B.1)
We show that it is possible to extract the series Φ0;2(gs) from this partial anti-holomorphic block
in the small gs limit in a very eﬃcient way.
We ﬁrst spell out the summation in the deﬁnition of the q-hypergeometric functions,
eHpart
0
(˜q) =
∞
X
k=0
(wa; ˜q)2
k
(w−1
a ˜q; ˜q)2
k
w−2k
a
˜qk 
(−w−1/2
a
)k −(w1/2
a
)k
,
(B.2)
where we used the property that w3
a = 1, w3/2
a
= −1. We denote the ˜q-dependent component in
the summand as
R(k; wa) :=
(wa; ˜q)2
k
(w−1
a ˜q; ˜q)2
k
w−2k
a
˜qk.
(B.3)
Let us introduce the notation
˜q = eη,
η = 4π2i
3 gs.
(B.4)
In the limit
gs →0,
η →0
(B.5)
we ﬁnd with the help of (A.21) that
R(k; wa) = exp
(
k(η −2 log(wa)) + 2
∞
X
ℓ=0
ηℓ−1
Bℓ(0) −Bℓ(k)
ℓ!
Li2−ℓ(wa)
−Bℓ(1) −Bℓ(1 + k)
ℓ!
Li2−ℓ(w−1
a )

.
(B.6)
By using the polylogarithm identitities
Li−n(z) + (−1)n Li−n(1/z) = 0,
n = 1, 2, . . .
Li0(z) + Li0(1/z) = −1
Li1(z) −Li1(1/z) = −log(−z),
z̸ ∈(0, 1]
(B.7)
– 43 –
and the Bernoulli polynomial identity
(−1)ℓBℓ(x) = Bℓ(1 −x),
ℓ≥0.
(B.8)
the expression of R(k; wa) can be simpliﬁed to
R(k; wa) = exp
(
−k2η +
∞
X
ℓ=2
ηℓ−1 2Bℓ(0) −Bℓ(k) −Bℓ(−k)
ℓ!
(Li2−ℓ(wa) + Li2−ℓ(wa))
)
.
(B.9)
If we expand this expression in terms of η, we ﬁnd that the coeﬃcients are polynomials of k;
more precisely,
R(k; wa) = 1 +
∞
X
n=1
ηn
2n
X
m=2
Rn;m(wa)km,
(B.10)
where we use Rn;m(wa) to denote the wa-dependent coeﬃcients in the k-polynomial. Finally by
summing up the index k and using the deﬁnition of the polylogarithm
Li−m(x) =
∞
X
k=0
kmxk,
(B.11)
we arrive at the following formula
eHpart
0
(˜q) ∼−
i
√
3 +
∞
X
n=1
ηn
2n
X
m=2
Rn;m(wa)

Li−m(−w−1/2
a
) −Li−m(−w1/2
a
)

= −
i
√
3

1 + 8π2
9
√
3gs + 16π4
81 g2
s + . . .

.
(B.12)
The ﬁrst line here is strictly speaking not an identity because (B.11) is only valid for |x| < 1,
while | −w−1/2
a
| = | −w1/2
a
| = 1. We also know from the radial asymptotic formula (3.171) that
the ﬁrst line of (B.12) cannot be possibly exact. The calculation from the ﬁrst to the second
line, however, is legitimate, and we identify the series to be −i/
√
3 · Φ0;2(gs). Therefore we cand
use the ﬁrst line of (B.12) to calculate Φ0;2(gs), which turns out to be very eﬃcient, allowing us
to obtain 700 terms of Φ0;2(gs).
