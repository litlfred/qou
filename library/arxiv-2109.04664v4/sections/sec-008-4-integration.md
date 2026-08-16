---
doc_id: arxiv-2109.04664v4
doc_title: "ON THE ASYMPTOTIC BEHA VIOR OF THE COLORED JONES POL YNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIA TED WITH A REAL NUMBER"
section_id: sec-008-4-integration
section_title: "Integration"
section_number: 4
pages: 10-11
source_pdf: 2109.04664v4.pdf
source_sha256: 639cd40a29752e3f
doc_brief: "ON THE ASYMPTOTIC BEHAVIOR OF THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT ASSOCIATED WITH A REAL NUMBER — W e study the asymptotic behavior of the N -dimensional colored Jones polynomial"
---
In this section, we use the Poisson summation formula (see [28, Prop osition 4.2])
to change the summation in (3.6) into an integration. Then by using th e saddle
point method (see also [28, Proposition 3.2]) to prove Theorem 1.5.
Deﬁne
ψ (z) := F (z +ϕ (ξ)/ξ ) −F (ϕ (ξ)/ξ )
in the region
(4.1){
z ∈ C
⏐
⏐
⏐ −ϕ (ξ)
ξ ≤ Rez <1 − ϕ (ξ)
ξ , −1 − ϕ (ξ)
ξ < Imz
tanθ + Rez <1 − ϕ (ξ)
ξ
}
.
Then since ψ (0) = 0, ψ ′(0) = 0, and ψ ′′(0) = −ξ
√
(2 cosh(ξ) − 1)2 − 4 from (3.4)
and (3.5), ψ (z) is of the form
ψ (z) = −ξ
2
√
(2 cosh(ξ) − 1)2 − 4 ×z2 +a3z3 +a4z4 + · · ·
in (4.1).
Lemma 4.1. If x ⁄= 0 is real and satisﬁes −ϕ (ξ)/ξ ≤ x < 1 − ϕ (ξ)/ξ , then
ψ (x)< 0.
Proof. Since eξ +e−ξ −eϕ (ξ) −e−ϕ (ξ) = 1, we have
ψ ′(x) = log(eξ +e−ξ −eξx+ϕ (ξ) −e−ξx−ϕ (ξ))
= log(eϕ (ξ) +e−ϕ (ξ) −eξx+ϕ (ξ) −e−ξx−ϕ (ξ) + 1)
= log
(
e−ϕ (ξ)(1 −eξx)(e2ϕ (ξ) −e−ξx) + 1
)(4.2)
THE COLORED JONES POLYNOMIAL OF THE FIGURE-EIGHT KNOT 11
from (3.2). Therefore we see that ψ ′(x) = 0 if x = 0 or −2ϕ (ξ)/ξ , ψ ′(x) > 0 if
−2ϕ (ξ)/ξ <x< 0, and ψ ′(x)< 0 otherwise.
Therefore for −ϕ (ξ)/ξ < x <0, ψ (x) is monotonically increasing and for 0 <
x< 1 −ϕ (ξ)/ξ it is monotonically decreasing. So ψ (x) takes its unique maximum
0 at x = 0, which shows that ψ (x)< 0 when x ⁄= 0.
□
Now we use the following proposition.
Proposition 4.2 ([28, Proposition 4.2]) . Letb− andb+ be real numbers with b− <
0<b +. Put
Λ :=
{ k
N
⏐
⏐
⏐k ∈ Z,b − ≤ k
N ≤b+
}
,
C := {t ∈ R |b− ≤t ≤b+},
D := {z ∈ C | Reψ (z)< 0}.
Assume that ψ (z) is a holomorphic function of the form
(4.3) ψ (z) = az2 +a3z3 +a4z4 + · · ·
with Re(a) < 0, deﬁned in a neighborhood P of 0 ∈ C that includes the δ0-
neighborhoodNδ0 of 0 for δ0 > 0. We choose P so that the region D ∩P has
two connected components. We also assume the following:
(1) b− and b+ are in diﬀerent components of D ∩P and moreover Reψ (b±)<
−ε0 for some ε0> 0,
(2) Both b− and b+ are in a connected component of
(4.4) {x +y
√
−1 |x ∈ [b−,b +],y ∈ [0,δ 0], Reψ (x +y
√
−1)< 2πy }
(3) Both b− and b+ are in a connected component of
(4.5) {x −y
√
−1 |x ∈ [b−,b +],y ∈ [0,δ 0], Reψ (x −y
√
−1)< 2πy }
Then there exists ε> 0, depending on a and ε0, such that
1
N
∑
z∈Λ
eNψ (z) =
∫
C
eNψ (z)dz +O(e−Nε ).
We will show that ψ (z) satisﬁes the assumptions of Proposition 4.2.
Put b− := −ϕ (ξ)/ (2ξ), b+ := (1 −ϕ (ξ)/ξ )/ 2, δ0 := 1
