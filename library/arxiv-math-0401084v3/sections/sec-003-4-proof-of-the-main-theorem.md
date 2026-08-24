---
doc_id: arxiv-math-0401084v3
doc_title: "Some limits of the colored Jones polynomials of the figure-eight knot"
section_id: sec-003-4-proof-of-the-main-theorem
section_title: "Proof of the main theorem"
section_number: 4
pages: 14-15
source_pdf: 0401084v3.pdf
source_sha256: f56bbd4cee4f3418
doc_brief: "Some limits of the colored Jones polynomials of the figure-eight knot — W e calculate limits of the colored Jones polynomials of the ﬁ gure- eight knot and conclude that in most cases they determine"
---
In this section we will prove the main theorem.
First we will calculate the derivative of H(u) := H(y, m2).
Lemma 4.1.
d
(
H(u) − π√
−1u
)
du = v
2 .
Proof. We ﬁrst calculate the partial derivatives of H(ξ, η). We have
∂ H (ξ, η)
∂ξ = 1
ξ
{
log
(
1 − ξ−1η−1)
+ log
(
1 − ξη −1)
+ log η
}
= 1
ξ log
(
η + η−1 − ξ − ξ−1)
and
∂ H (ξ, η)
∂η = 1
η
{
log
(
1 − ξ−1η−1)
− log
(
1 − ξη −1)
+ log(−ξ)
}
= 1
η
{
log
(1 − ξη
η − ξ
)
+ π
√
−1
}
.
Since
∂ H (ξ, η)
∂ ξ
⏐
⏐
⏐
⏐
ξ=y,η =m2
= 1
y log
(
m + m−1 − y − y−1)
= 0
from (3.2) we have
d H(u)
du = ∂ H (ξ, η)
∂ξ
⏐
⏐
⏐
⏐
ξ=y,η =m2
× d y
du + ∂ H (ξ, η)
∂η
⏐
⏐
⏐
⏐
ξ=y,η =m2
× d m2
du
= log
(1 − ym2
m2 − y
)
+ π
√
−1.
But since {
ym2 + zm2 = 1
z−1 + m2y−1 = 1,
we have
d
(
H(u) − π√−1u
)
du = log
(
z(1 − z)
)
= v
2 .
□
Next we will calculate H(0).
Lemma 4.2.
H(0) =
√
−1 Vol
(
S3 \ E
)
Proof. Since m
⏐
⏐
u=0 = −1 and y
⏐
⏐
u=0 = exp(−π√
−1/3), we have
H(0) = Li 2
(
e−π √−1/ 3
)
− Li2
(
eπ √−1/ 3
)
= 4
√
−1 L(π/6)
from (3.3).
On the other hand from the equality
L(2θ) = 2 L(θ) − 2 L(π/2 − θ)
THE COLORED JONES POLYNOMIALS OF THE FIGURE-EIGHT KNOT 15
(see for example [9, Lemma 1]), we have 4 L(π/6) = 6 L(π/3), which equals the
volume of S3 \ E. □
Proof of Corollary 2.4. We see that
Φ( u) = 4 H(u) − 4π
√
−1u − 4H(0)
and so
f (u) = H(u) − π
√
−1u − uv/4 −
√
−1 Vol
(
S3 \ E
)
since CS
(
S3 \ E
)
= 0. Therefore from Theorem 2.1
Vol (Eu) +
√
−1 CS (Eu) = H(u)√−1 − πu − uv
4√−1 − π
2 λ(γ).
□
