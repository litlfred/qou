---
doc_id: arxiv-2205.07095v1
doc_title: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko"
section_id: sec-005-32-derivation-of-equations-for-correlation-funct
section_title: "Derivation of equations for correlation functions."
section_number: 3.2
pages: 6-8
source_pdf: 2205.07095v1.pdf
source_sha256: 2ec6916399150e2d
doc_brief: "Virial Expansions for Correlation Functions in Canonical Ensemble A. L. Rebenko — The inﬁnite set of coupled integral nonlinear equations for correlation func- tions in the case of classical"
---
The correlation functions of the canonical ensemble of the s ystem N of
particles in some limited volume Λ in conﬁguration η = {x1,...,x m} are
determined by the sequence
ρ(N )
Λ (η) :=



1, atη = ∅,
̺ = N
V at |η| = 1,V =σ(Λ),
0, at; |η| =m > N,
(3.11)
and for 2 ≤m ≤N ,
ρ(N )
Λ (η) := 1
ZΛ (β,N )
∫
Γ (N − m)
Λ
dγ
(N −m)!e−βU (η∪γ), (3.12)
where
ZΛ (β,N ) = 1
N !
∫
Γ (N )
Λ
e−βU (γ)dγ, (3.13)
and ̺ is the density of the particles in the system.
To derive equation for correlation functions using lemma 2. 1 we write
down the right hand part of (3.12) by the integral (2.1):
ρ(N )
Λ (η) = 1
ZΛ (β,N )
∫
Γ Λ
e−βU (η∪γ)1 1N −m(γ)λσ(dγ), |η| ≤ N, (3.14)
where
1 1N −m(γ) :=
{
1, |γ| =N −m,
0, |γ| ⁄=N −m.
(3.15)
Introduce a notationη(ˆx) :=η\{x}. Let in conﬁguration η = {x1,...,x m}
the coordinate x1 such that, for which the following inequality is true:
W (x1;η(ˆx1)) =
m∑
k=2
φ(|x1 −xk|) ≥ − B, B ≥ 0. (3.16)
Then
U (η ∪γ) = W (x1;η(ˆx1)) +W (x1;γ) +U (η(ˆx1) ∪γ) (3.17)
and
e−βW (x1;γ) =
∏
y∈γ
[
(e−βφ(|x1−y|) − 1) + 1
]
=
∑
ξ⊆γ
K(x1;ξ), (3.18)
6
where
K(x1;ξ) :=
{ ∏
y∈ξ(e−βφ(|x1−y|) − 1), |ξ| ≥ 1,
1, ξ = ∅.
(3.19)
Then
ρ(N )
Λ (η) = e−βW (x1;η(ˆx1))
ZΛ (β,N )
∫
Γ Λ
e−βU (η(ˆx1)∪γ)×
× 1 1N −m(γ)
∑
ξ⊆γ
K(x1;ξ)1 1Λ (γ \ξ)λσ(dγ). (3.20)
Apply to the integral in (3.20) the lemma 2.1 with
G(γ) = e−βU (η(ˆx1)∪γ)1 1N −m(γ) and H(ξ;γ \ξ) = K(x1;ξ)1 1Λ (γ \ξ). (3.21)
Then
ρ(N )
Λ (η) = e−βW (x1;η(ˆx1))
ZΛ (β,N )
∫
Γ Λ
∫
Γ Λ
e−βU (η(ˆx1)∪ξ∪γ)×
× 1 1N −m(ξ ∪γ)K(x1;ξ)1 1Λ (γ)λσ(dγ)λσ(dξ). (3.22)
Rewrite the right hand side in the following way
ρ(N )
Λ (η) = e−βW (x1;η(ˆx1))ZΛ (β,N − 1)
ZΛ (β,N )
∫
Γ Λ
K(x1;ξ)× (3.23)
×
[ 1
ZΛ (β,N − 1)
∫
Γ Λ
e−βU (η(ˆx1)∪ξ∪γ)1 1N −m−|ξ|(γ)λσ(dγ)
]
λσ(dξ).
Taking into account (3.14)(N −m − |ξ| =N − 1 − (m − 1 +|ξ|)) we obtain:
ρ(N )
Λ (η) = e−βW (x1;η(ˆx1))aΛ
N
∫
Γ Λ
K(x1;ξ)ρ(N −1)
Λ (η(ˆx1) ∪ξ)λσ(dξ), (3.24)
where |η| =m η = {x1,...,x m}, 1 <m<N , and
aΛ
N = ZΛ (β,N − 1)
ZΛ (β,N ) . (3.25)
Form = 1
ρ(N )
Λ ({x1}) = N
V =aΛ
N
∫
Γ Λ
K(x1;ξ)ρ(N −1)
Λ (ξ)λσ(dξ), V =σ(Λ). (3.26)
Note, also, that
ρ(N )
Λ (η) = 0, if |η| ≥ N. (3.27)
7
In the thermodynamic limit
Λ ↑ Rd, lim
V →∞
N →∞
V
N =v, 1
v =̺, (3.28)
existing of which was proved in [3] we have the following equa tion
ρ(η) = ̺a(̺)e−βW (x1;η(ˆx1))
∫
Γ 0
K(x1;ξ)ρ(η(ˆx1) ∪ξ)λσ(dξ), (3.29)
where
lim
V =N/̺
N →∞
ZΛ (β,N − 1)
ZΛ (β,N ) = ̺a(̺), V =σ(Λ) (3.30)
and
a(̺) = 1
~Q(ρ)
, ~Q(ρ) =
∫
Γ 0
K(x1;ξ)ρ(ξ)λσ(dξ). (3.31)
