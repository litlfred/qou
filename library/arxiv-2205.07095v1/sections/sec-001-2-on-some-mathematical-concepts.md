---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko"
section_id: sec-001-2-on-some-mathematical-concepts
section_title: "On some mathematical concepts"
section_number: 2
pages: 3-4
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical"
---
2.1 Conﬁguration spaces and Lebesgue-Poisson measure.
Letσ be a Lebesgue measure in Rd. Conﬁguration space Γ := Γ Rd consists
of all locally ﬁnite subsets of the space Rd. This deﬁnition is quite natural
from the point of view of physics, because an inﬁnite number o f particles
cannot be in a bounded volume.
Denote the set of all ﬁnite conﬁgurations of the space Γ by Γ 0, and by
Γ (n) conﬁguration space with a ﬁxed number of points.
If all such conﬁgurations are in some bounded set Λ ⊂ Rd, then the
corresponding space will be Γ (n)
Λ .
State of an ideal gas in equilibrium statistical mechanics i s described
by the Poisson measure πzσ on conﬁguration space Γ, where z >0 is the
activity (physical parameter that associated with the dens ity of particles
in the system).
But we need so-called Lebesgue-Poisson measure, i.e. the Po isson mea-
sure on the space of ﬁnite conﬁgurations, which in some sense is absolutely
continuous with respect to the Lebesgue measure in contrast to the πσ
measure for Γ. Integral for Lebesgue-Poisson measure in spa ce Γ 0 (or Γ Λ )
is determined by the formula:
∫
Γ X
F (γ)λzσ(dγ) :=
∞∑
n=0
zn
n!
∫
X
· · ·
∫
X
F ({x1,...,x n})σ(dx1) · · ·σ(dxn) =
=
∞∑
n=0
zn
n!
∫
X
· · ·
∫
X
Fn(x1,...,x n)dx1 · · ·dxn, (2.1)
for all measurable functions F = {Fn}n≥0, Fn ∈ L1(Xn), and Γ X ∈
{Γ 0, Γ Λ ). Such measure not only simpliﬁes the recording of cumberso me ex-
pressions and combinatorial proofs, but also allows to get s ome new results
based on properties inﬁnite divisibility (see, for example , [18, 20, 19, 14].
In the language of integrals with the measure λzσ we give one well-
known and important identity, which will be used very often b elow (see,
for example, [8]).
3
Lemma 2.1 For all measurable functions G : Γ 0 ↦→R and H : Γ 0 × Γ 0 ↦→
R, for which G(ξ ∪γ)H(ξ,γ ) ∈L1(Γ 0 × Γ 0,λσ ⊗λσ), the following equality
is true:
∫
Γ 0
G(γ)
∑
ξ⊆γ
H(ξ,γ \ξ)λσ(dγ) =
∫
Γ 0
∫
Γ 0
G(ξ ∪γ)H(ξ,γ )λσ(dγ)λσ(dξ).
(2.2)
Proof. Let ξ ↾ Γ (k)
0 = {x1,...,x k} := {x}k
1, γ ↾ Γ (m)
0 = {xk+1,...,x k+m} :=
{x}k+m
k+1 . Then
∫
Γ 0
∫
Γ 0
G(ξ ∪γ)H(ξ,γ )λσ(dγ)λσ(dξ) =
=
∞∑
k,m=0
1
k!m!
∫
Rdk
∫
Rdm
G({x}k+m
1 )H({x}k
1, {x}k+m
k+1 )σ(dx)k+m =
=
∞∑
n=0
1
n!
n∑
k=0
(n
k
) ∫
Rdn
G({x}n
1)H({x}k
1, {x}n
k+1)σ(dx)n =
=
∫
Γ 0
G(γ)
∑
ξ⊆γ
H(ξ,γ \η)λσ(dγ).
■
Note that the introduction of the measure (2.1) and the appli cation of
the lemma 2.1 greatly simpliﬁes the calculations of many com binatorial
statements.
