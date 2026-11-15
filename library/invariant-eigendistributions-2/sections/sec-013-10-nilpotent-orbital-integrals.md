---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-013-10-nilpotent-orbital-integrals
section_title: "Nilpotent orbital integrals"
section_number: 10
pages: 24-26
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
For each Go-orbit O in igo∗let µO be the distribution on go∗deﬁned by
⟨µO, f⟩=
1
(2πi)d

O
fe−σO
(1)
with d = dimCO. µO is a tempered distribution on igo∗. (Of course, we use igo∗rather than go∗or go
only to conform with the deﬁnition of the distributions θΓ , which will simplify the notation.) We denote
by µO the Fourier transform of µO, a tempered distribution on go, given by a locally integrable function.
In this sense :
µO(ξ) =
1
(2πi)d

Oλ
exO−σO.
For regular λ ∈ih∗we set Oλ = Go · λ and µλ = µOλ. Since Go · λ = K · (λ + ibo
⊥) = pλS1 for such λ
we ﬁnd that its Fourier transform is
µλ =
1
(2πi)n

Oλ
eλ−σλ = 1
π

y∈Wo
ey−1λ
(2)
as tempered distributions on go.
REPRESENTATIONS OF WEYL GROUPS
25
Now take for O a nilpotent Go-orbit in igo∗. From (8.7) we know that its Fourier transform µO = θO
is
µO = 1
e!
pO
π
(3)
where pO is the distribution on go which on ho is given by the up to scalars unique Wo-invariant polynomial
of degree e = e(O) on h transforming according to the irreducible character χO⊗χO under W = Wo×Wo.
Using (8.20) we have for any regular λ ∈h∗a formula
µO = const. 1
π

y∈W
cO(y)y−1 · λe
(4)
for a constant depending on O and λ, namely
const. =
eo
e!cO(λ)|W|
in the notation of section 8. Alternatively, using (9.9):
µO(x) = const.

y∈Wo
χσ(y)⟨x1, y · x2⟩eo
(5)
where this time the constant depends only on O , namely
const. =
1
kOe!.
(4) is a rather explicit formula for the invariant eigendistributions µO on go, which have inﬁnitesimal
character 0. Compare this with Harish-Chandra’s formula for eigendistributions with regular inﬁnitesimal
character λ :
θ = 1
π

y∈W
myey−1λ.
(6)
(Of course, (6) is part of the genesis of (4).)
Formula (3) quickly leads to a formula for µO itself as follows. Let ∂O be the constant coeﬃcient
operator on h∗corresponding to the polynomial pO on h. It satisﬁes
∂O,λe⟨λ,x⟩|λ=0 = pO(x).
where the subscript λ on ∂O,λ means “diﬀerentiation with respect to λ”.
Diﬀerentiating equation (2) with respect to λ and evaluating at λ = 0 one gets
lim
λ →0
∂O,λµλ(x) =
lim
λ →0
∂O,λ
 1
π

y∈Wo
e⟨λ,y·x⟩

= |Wo|
π
pO(x) = e!|Wo|µO(x).
Inverting the Fourier transforms we arrive at
REPRESENTATIONS OF WEYL GROUPS
26
10.1 Theorem. Let O be a nilpotent Go-orbit in igo∗. Then
µO = e!|Wo| lim
λ →0
∂O,λµλ
(7)
and
µO(x) = const.(λ, O) 
π

y∈W
χO(y)⟨λ, y · x⟩e
(8)
= const.(O) 
π

y∈Wo
χσ(y)⟨x, y · x⟩eo
(9)
The formula (7) has some history. For O = {0},
χO = sign representation of Wo, pO = const.π, and (7)
becomes Harish-Chandra’s Limit Formula
µO = const. lim
λ →0
∂π,λµλ(x).
For special orbits Formula (7) was proved by Barbasch-Vogan [1982, 1983] by case by case computations
and conjectured to hold in general. This conjecture was then proved by Hotta-Kashiwara [1984] (using
the theory of holonomic systems).
