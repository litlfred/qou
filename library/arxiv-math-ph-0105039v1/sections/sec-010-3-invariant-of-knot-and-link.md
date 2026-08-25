---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-010-3-invariant-of-knot-and-link
section_title: "Invariant of Knot and Link"
section_number: 3
pages: 10-11
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
With the R-matrix ˇR : W⊗2 → W⊗2 satisfying the braid relation (2.24), we can deﬁne the
invariant of the knot K. We assume that we have the enhanced Yang–Baxter operators (ˇR, µ, α, β)
satisfying [2]
(
µ ⊗ µ
) ˇR = ˇR
(
µ ⊗ µ
)
, (3.1a)
Tr2
(
ˇR±1 (
1 ⊗ µ
) )
= α±1 β. (3.1b)
Here the operator µ acts on a space W. When the knot K is given as the closure of a braidξ which
is represented in terms of the Artin n string braid group,
⟨
σ1, . . . , σn−1
⏐
⏐
⏐
σi σj = σj σi, for |i − j| ≥ 2
σi σi+1 σi = σi+1 σi σi+1, for i = 1, . . . , n− 1
⟩
, (3.2)
we get the knot invariant τ (K);
τ (K) = α−w(ξ) β−n Tr1,...,n
(
bR(ξ) µ⊗n
)
, (3.3)
where w(ξ) is a writhe, i.e., a sum of the exponents, andbR(ξ) means to replace the braid operators
σ±1 by ˇR±1. Later we use another knot invariant,
τ1(K) = α−w(ξ) β−n Tr2,...,n
(
bR(ξ) µ⊗(n−1)
)
, (3.4)
which is associated for (1, 1)-tangle.
When we use the ˇR-matrix deﬁned in eq. (2.27), we ﬁnd that the µ operator deﬁned by 1
µ = e
π +γ
γ ˆp ⊗ e− π +γ
γ ˆpt
(3.5)
fulﬁlls eqs. (3.1) with parameters
α = e −i π 2+γ 2
γ , β = γ ei π 2+γ 2
γ
(1 − e2γ i) (1 − e2 π 2
γ i)
. (3.6)
In this computation Tr means integration, and we have used δ(x) = lim ∆ →0
∆
x2+∆ 2 . As a conse-
quence we have obtained the knot invariantτ1(K) from a set of the Yang–Baxter operators deﬁned
1 The author thanks Rinat Kashaev for pointing out an error of previous manuscript.
10
with eq. (2.22) and eqs. (3.5) – (3.6). We should stress that our invariant τ1(K) can be viewed as a
non-compact analogue of Kashaev’s invariant which coincides with the colored Jones polynomial
at a speciﬁc value as was proved in Ref. 7. In fact Kashaev’s R-matrix [3] was originally deﬁned
based on a reduction of the quantum S-operator when the deformation parameter eiγ approaches a
root of unity. In that case the pentagon identity (2.21) is replaced by
S1, 2(p, q, r) S1, 3(p, q r, s) S2, 3(q, r, s) = S2, 3(p q, r, s) S1, 2(p, q, r s),
where p, . . . , sare parameters, and a solution S is given in a ﬁnite-dimensional matrix.
In the following, we have interests in the asymptotic behavi or of the invariant τ1(K), and we
deﬁne
˜τ1(K) = lim
γ →0
(
2 i γ log τ1(K)
)
. (3.7)
As our construction of the invariant is essentially same wit h Kashaev’s invariant, we expect that
the conjecture (1.1) will be applicable to the invariant (3.7).
