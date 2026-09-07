---
doc_id: arxiv-1905.02045v3
doc_title: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM"
section_id: sec-004-2-two-reciprocity-formulae-for-the-q-pochhammer
section_title: "Two reciprocity formulae for the q-Pochhammer symbol"
section_number: 2
pages: 8-9
source_pdf: 1905.02045v3.pdf
source_sha256: 8e7eb17c7d1f4f4e
doc_brief: "MODULARITY AND VALUE DISTRIBUTION OF QUANTUM — We obtain an exact modularity relation for the q-Pochhammer symbol."
---
2.1. Abel-Plana’s summation formula. Our argument is based on the Abel-Plana sum-
mation formula.
We denote by γε the following integration contour.
γε
ε
−iε
Lemma 1. Letα,β,β ′∈ R withα≤β <β′. Let f be an analytic function on a neighborhood
of U :={z∈ C|α≤ Re(z)≤β′}\{ α,β}. Assume that the following holds :
(1) f(z) is holomorphic at β ifβ is an integer, and otherwise f(z) =o(|z−β|−1) asz→β
with z∈U,
(2) f(x±iy) =o(e2πy/y2) as y→ +∞, uniformly in x∈ [α,β ],
(3) f is integrable on (α,β ).
Then we have
∑
α<n≤β
f(n) =
∫ β
α
f(t)dt−C(f,α ) +C(f,β ),(2.1)
where
C(f,α ) := lim
ε→0+
(
−i
∫
γε
f(α +it)dt
e(−α)e2πt− 1 +i
∫
γε
f(α−it)dt
e(α)e2πt− 1
)
.
Proof. The arguments in [36, Chapter 8, eq. (3.01)] are readily adapted. □
Fork∈ Z≥0, k⁄= 1, let ˜Bk(t) =Bk({t}) where{t} is the fractional part of t and Bk is the
k-th Bernoulli polynomial, and let ˜B1(t) = B1({t}) for t /∈ Z and ˜B1(n) = 0 for n∈ Z. We
require the following computation.
Lemma 2. For𝓁∈ Z≥0 and v∈ [0, 1), we have
∫ ∞
0
Im
( (−it)𝓁
e(v)e2πt− 1
)
dt = (−1)𝓁 ˜B𝓁+1(v)
2(𝓁 + 1) .
Moreover, for all ω∈ C r (−∞, 1], we have∫ ∞
0
dt
ωe2πt− 1 =−1
2π log(1−ω−1)
with log being the principal determination.
MODULARITY AND DISTRIBUTION OF QUANTUM KNOTS INV ARIANTS 9
Proof. The second claim is easy to prove by expanding the fraction as a power series in ω,
ﬁrst for ω∈ (1,∞], and then by analytic continuation. To show the ﬁrst claim, ﬁrst we note
that for 𝓁 = 0, v = 0, the fraction is a real number, and both sides evaluate to 0. We may
therefore assume that 𝓁≥ 1 or v⁄= 0. Then
∫ ∞
0
Im
( (−it)𝓁
e(v)e2πt− 1
)
dt = 1
(2π)𝓁+1 Im
(
e(−v)(−i)𝓁
∫ ∞
0
t𝓁e−tdt
1− e(−v)e−t
)
= 𝓁!
(2π)𝓁+1 Im
(
(−i)𝓁∑
n≥1
e(−nv)
n𝓁+1
)
by [19, eq. (3.411.6)]. We write Im (( −i)𝓁 e(−nv)) = (−1)𝓁+1 cos(2πnv− π
2 (𝓁 + 1)), and
conclude by the Fourier expansion of Bernoulli polynomials [19, eq. (9.622.1)]. □
