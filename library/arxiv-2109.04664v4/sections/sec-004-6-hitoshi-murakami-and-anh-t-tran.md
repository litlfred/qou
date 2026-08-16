---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-004-6-hitoshi-murakami-and-anh-t-tran
section_title: "HITOSHI MURAKAMI AND ANH T. TRAN"
section_number: 6
pages: 6-7
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
L2(z) =





Li2
(
e2π √
−1z
)
if Imz ≥ 0,
π 2(
2z2 − 2z + 1
3
)
− Li2
(
e−2π √−1z
)
if Imz <0.
(2.4)
Proofs are also given in Section 6.
Remark 2.6. In (2.3) and (2.4), we use log(1 −x) and Li 2(x) only for |x| ≤ 1 (x ⁄= 1).
Since
TN (z −γ/ 2) −TN (z +γ/ 2) =
∫
Cθ
e(2z−γ −1)x −e(2z+γ −1)x
4x sinh(x) sinh(γx) dx
= −
∫
Cθ
e(2z−1)x
2x sinh(x)dx
= L1(z),
we have the following corollary.
Corollary 2.7. If 0< Re(zeθ√
−1)< cosθ, then we have
(2.5) exp (TN (z −γ/ 2))
exp (TN (z +γ/ 2)) = 1 −e2π √−1z.
We will show relations among the functions TN (z) and Lm(z) (m = 0, 1, 2).
We can prove that 1
NTN (z) uniformly converges to 1
ξ L2(z). More precisely, we
have the following proposition. See [28, Proposition A.1].
Proposition 2.8. For any positive real number M and a suﬃciently small positive
real number ν, we have
TN (z) = N
ξ L2(z) +O(1/N ) ( N → ∞)
in the region
{z ∈ C |ν ≤ Re(zeθ√−1) ≤ cosθ −ν, | Imz| ≤ M }.
In particular, the function 1
NTN (z) uniformly converges to 1
ξ L2(z) in the region
above.
A proof is given in Section 6. Since we may regard L2(z) as a variant of the
dilogarithm from Lemma 2.5, the function TN (z) is another quantum dilogarithm.
The functions L0(z), L1(z), and L2(z) are related as follows.
Lemma 2.9. The derivatives of L1(z) and L2(z) are given as follows:
d L2
dz (z) = −2π
√
−1L1(z),
d L1
dz (z) = −L0(z).
Proof. We have
d L2
dz (z) = π √−1
2
∫
Cθ
( d
dz
e(2z−1)x
x2 sinh(x)
)
dx
=π
√
−1
∫
Cθ
e(2z−1)x
x sinh(x)dx
= −2π
√
−1L1(z),
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 7
and
d L1
dz (z) = − 1
2
∫
Cθ
( d
dz
e(2z−1)x
x sinh(x)
)
dx
= −
∫
Cθ
e(2z−1)x
sinh(x) dx
= −L0(z),
completing the proof. □
