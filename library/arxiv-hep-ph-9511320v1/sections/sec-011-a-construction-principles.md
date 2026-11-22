---
doc_id: arxiv-hep-ph-9511320v1
doc_title: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields"
section_id: sec-011-a-construction-principles
section_title: "Construction Principles"
section_number: A
pages: 19-22
source_pdf: 9511320v1.pdf
source_sha256: 4336112cecabdfdf
toc_source: inferred
doc_brief: "Chiral Lagrangians for Baryons Coupled to Massive Spin-1 Fields — We analyze the eﬀective low–energy ﬁeld theory of Goldstone bosons and baryons chirally coupled to massive spin–1 ﬁelds."
---
Construction Principles
Here, we collect a few useful formulae which are needed to construct the
eﬀective Lagrangians L(1)
BφW and L(1)
BφV . To the order we are working, we can
make use of the equation of motion for the baryon ﬁelds derived from L(1)
Bφ
iγµ[Dµ, B] −mB + 1
2Dγµγ5{uµ, B} + 1
2Fγµγ5[uµ, B] = 0 .
(A.1)
In fact, only the chiral–covariant kinetic and the mass terms will be of rele-
vance to the order we are working. It is worth to stress that we only consider
processes with at most two external pions or one external vector source, like
e.g. single vector–meson exchange in Goldstone boson–baryon scattering or
t–channel vector meson exciations contributing to the baryon electromagnetic
form factors. It is straightforward to generalize our considerations to more
complicated processes. In what follows, we frequently employ our short–hand
notation (A, B) meaning either [A, B] or {A, B}.
Consider ﬁrst the tensor ﬁeld formulation. We want to construct terms which
contain one antisymmetric tensor and at most two covariant derivatives since
in the low energy domain
[Dµ, [Dν, Wλκ]] = O(q2) .
(A.2)
Because of the antisymmetry of Wµν, many terms vanish. We give one example
Tr

¯B

[Dµ, [Dν, Wµν] , B

∼Tr

¯B

[uµ, uν], Wµν] , B

= 0 ,
(A.3)
for the processes under consideration. The term on the right–hand–side of
Eq.(A.3) gives rise to e.g. a vector-two-pion-baryon seagull term and is thus
of no relevance here. The discrete symmetries P, C and T as well as hermitic-
ity and Lorentz and chiral invariance strongly constrain the possible terms.
Consider e.g. charge conjugation. We have
C :
W c
µν = −W T
µν , Bc = C ¯BT , ¯Bc = BT C , Dc
µ = −DT
µ ,
(A.4)
and the standard transformation properties for the Dirac matrices. This elim-
inates for example a term like
Tr

¯Bγµ

D2W , D3B
c
≃−Tr

¯Bγµ

(D2, W) , D3B

,
(A.5)
in symbolic notation (i.e. dropping all unnecessary indices). The ’≃’ means
that we have dropped terms of higher order which arise when one moves the
covariant derivatives around. Under parity transformations
P :
P Wµν(x) P † = W µν(˜x) , P Dµ(x) P † = Dµ(˜x) ,
P B(x) P † = γ0 B(˜x) , P ¯B(x) P † = ¯B(˜x) γ0 ,
(A.6)
with ˜xµ = xµ. We also note that while Wµν is hermitean, W †
µν = Wµν, the
covariant derivative is anti-hermitean, D†
µ = −Dµ. With these tools at hand,
one readily constructs the eﬀective Lagrangian Eq.(19).
For the vector ﬁeld formulation, one can proceed similarly. Here, however,
it is helpful to remember the standard ρ–meson–nucleon vector and tensor
couplings,
LρN = g
2
¯ΨN

γµ⃗ρµ ·⃗τ −κρ
2m σµν ∂ν⃗ρµ ·⃗τ

ΨN .
(A.7)
These terms can easily be transcribed into SU(3) vector meson-baryon cou-
plings (in the vector ﬁeld formulation) of the type
Tr [ ¯B γµ (Vµ , B) ]
and
Tr [ ¯B σµν (DνVµ , B) ] .
(A.8)
Furthermore, up to order q4 and for diagrams with one baryon line running
through, because of momentum conservation we have [Dµ, V µ] = 0. This ar-
gument holds e.g. for elastic forward scattering. More generally, such terms
do not contribute to the eﬀective action since
∂x
µ ∂λ,y Gνλ(x) −∂x
ν ∂λ,y Gµλ(x) = 0
(A.9)
This condition eliminates a large class of possible terms. To arrive at the
terms shown in Eq.(31), one makes use of the antisymmetry of Vµν and uses
the equations of motion to let the covariant derivative act on the baryon ﬁelds
as much as possible. Of course, the discrete symmetries, hermiticity and so on
have to be obeyed. These are more standard in the vector ﬁeld formulation
and we thus refrain from discsussing these in detail here.
The last point we want to address are the terms in LBφV which contain the
symmetric tensor ¯Vµν. One example is the last term in Eq.(31), another such
term is e.g. given by
Tr

¯B γµ

[Dλ, ¯Vµν] , [Dλ, [Dν, B]]

.
(A.10)
In the eﬀective action, it leads to the following four–point function (to be
precise, the derivative of it),
−i ∆†
µν,ρσ(x, y) =
∂x
ν ∂y
σ Gµρ(x, y) + ∂x
ν ∂y
ρ Gµσ(x, y) −∂x
µ ∂y
σ Gνρ(x, y) −∂x
µ ∂y
ρ Gνσ(x, y)
= −i
Z
d4k
(2π)4
e−ik·(x−y)
k2 −M2
V + iǫ

gµρkνkσ + gµσkνkρ −gνρkµkσ −gνσkµkρ

,
(A.11)
which is symmetric under ρ ↔σ. Therefore, such a term or the last one
in Eq.(31) do not seem to have analoga in the antisymmetric tensor ﬁeld
formulation. If that were to be true, then already at tree level one would have
an inequivalence between the two representations for the massive spin–1 ﬁelds
starting at order O(q4). However, setting (see also appendix B)
Vν = −1
M2
V
Dλ Vλν
(A.12)
one can rewrite ¯Vµν in the following way
¯Vµν = −1
M2
V
(Dµ Dλ Vλν + Dν Dλ Vλµ ) .
(A.13)
This latter object is up to an irrelevant prefactor similar to the tensor ﬁeld
combination
Dµ Dλ Wλν + Dν Dλ Wλµ ,
(A.14)
which after using the equations of motion for Wµν can be recast into the form
2Dµ Dλ Wλν + M2
V Wµν .
(A.15)
Consequently, if we decompose ¯Vµν as
¯Vµν = 2 Dµ Vν −Vµν ,
(A.16)
one realizes that the seemingly inequivalent terms containing the symmet-
ric tensor ¯Vµν are also appearing in the tensor ﬁeld formulation for appro-
priate combinations of Wµν and the covariant derivatives (like e.g. given in
Eq.(A.15)).
