---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-015-51-theorem-the-map
section_title: "Theorem. The map"
section_number: 5.1
pages: 9-11
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 25 sections: Introduction; Construction of Weyl group represe"
---
H2n(S, Z)→CH(go, Z), Γ→θΓ,
given by the Integral Formula is a W −isomorphism.
More precisely, the homology classes w·S1, w∈W/Wo, form a basis for H2n(S, Z). They correspond
to the basis (−1)noϕw,w ∈W/Wo,o f CH(go, Z) under the bijection Γ→θΓ .
Proof. That the mapH2n(S) → CH(go) is a bijection we know from the Integral Formula : its matrix
(−1)no+l(w)−l(y)Euy(Sw) with respect to the basesSw of H2n(S)a n dϕw of CH(go), is integral and
unipotent-triangular with respect to the Bruhat order onW/Wo.
It suﬃces to prove the second assertion which says explicitly that for regularλ∈h∗,
1
(2πi)n
∫
pλwS1
exλ−σλ = (−1)no
π(x)
∑
y∈Wo
e(wy)−1λ(x). (5)
Forw = 1 this is a specialcase ofthe IntegralFormula: theK-orbitZ1 =K·z1 is smooth, soEuy(Z1)=1
or 0, according asy ∈Wo or not. To see that (5) holds for allw ∈W we onlyneed to identifythepλwS1.
The cyclepλS1 is the image under the map
pλ :B∗ → Ωλ,u ·(b1,ν)→u·(λ+ν)
of the conormal bundle of the closedGo-orbit Go ·s1, where s1 =bo ×¯bo . That conormal bundle is
Go ·{(s1,ν)|ν ∈s1⊥ ∩igo⊥}
Since Go =KoBo and bo ⊂s1 this conormal is also
=Ko ·{(b1,ν)|ν ∈ibo
⊥}.
where bo
⊥ ⊂go∗ is the orthogonal ofbo in go∗ (not ing∗). Its image underpλ becomes Ko ·{λ+ibo
⊥}.
From the deﬁnition of the action ofW on H2n(S) one ﬁnds that the cyclepλw·S 1 on Ωλ which
ﬁgures in (5) is properlyhomotopic toKo ·{w−1λ+ibo
⊥}:
pλw·S 1 ∼Ko ·{w−1λ+ibo
⊥} on Ωλ.
taken with the appropriate orientation. So (5) says
1
(2πi)n
∫
Ko·{w−1λ+ibo ⊥}
exλ−σλ = (−1)no
π(x)
∑
y∈Wo
e(wy)−1λ(x). (6)
We know that this formula holds forw =1( a n dr e g u l a rλ). Replacing λ by wλ one sees that it holds for
all w ∈ W. Furthermore, writing the integral (6) as a double integral, ﬁrst overbo
⊥, then overKo, one
sees that (6) exists for allλ∈h∗ (regular or not). This means that
ϕw(λ) is entire analytic in λ∈h∗
as promised above. This ﬁnishes the proof of the theorem. We record explicitlythe special case when
Γ= Sw :
REPRESENTATIONS OF WEYL GROUPS 10
5.2 Corollary .
Sw =
∑
y∈W/Wo
(−1)l(w)−l(y)Euy(Sw)y·S 1.
or equivalently
Zw =
∑
y∈W/Wo
(−1)l(w)−l(y)Euy(Zw)y·Z 1.
6. Characters and characteristic cycles.
As a ﬁrst and immediate application of Theorem 5.1 we derive a formula for the global character of a
(g,K )-module as a contour integral over the characteristic cycle of the corresponding (D,K)-module.
Westartwithsomegeneralremarksaboutglobalcharacters. A( g,K )-moduleM with inﬁnitesimal
character λ ∈ h is the Harish-Chandra module of an admissible representation ofGo, whose global
character is an invariant eigendistribution Θ =ch(M)o nGo. It follows from results of Harish-Chandra
[1965] that one has an identityof distributions in a neighbourhood of 0 ingo :
Θ(expx)= j(x)−1θ(x)( 1 )
where θ is an invariant eigendistribution ongo with inﬁnitesimal characterλ and
j(x)=d e t1/2(eadx/2 −e−adx/2
adx )= ∆(x)
π(x) on ho.
Here π = ∏
α∈∆+ α as before, and
∆=
∏
α∈∆+
(eα/2 −e−α/2)
is the Weyl denominator. The products are over the rootsα of ho in bo
⊥. If λ∈h∗ is regular, as we shall
now assume, the Integral Formula allows us to writeθ = θΓ(λ) for a unique Γ∈ H2n(S). We shall call
this homologyclass Γ, or any2n-cycle representing it, thecharacter contour of the (g,K )-module M,
and denote itC(M). It should be noted thatC(M) depends on the choice of the elementλ in theW-orbit
in h∗ determined bythe inﬁnitesimal character ofM and on the Borel subalgebras1 used to deﬁne the
map pλ.
Recall the Beilinson-Bernstein[1981]correspondencebetween (g,K )-modules and (D,K)-modules.
We consider onlythe case of regular integral inﬁnitesimal character; one mayas well assume (as we now
do) that the inﬁnitesimal character is represented by−ρ where ρ =( ρo,ρo)i sh a l ft h es u mo ft h er o o t s
of h in z1 =bo ×bo.
TheBeilinson-Bernsteincorrespondencebasedonthedata( z1,−ρ)associatestoeach( g,K )-module
M with inﬁnitesimal character -ρ the (D,K)-moduleM =D⊗M.( D is the sheaf of diﬀerential operators
onB as in [Beilinson-Bernstein]; the tensor product is overU(g) as explained there.) This correspondence
is an equivalence of categories.
For eachK-orbitZy =K·y−1z1 there is an inducedD-module which we shall denoteIy.W r i t eIy
for the corresponding (g,K )-module. It is known thatIy is an induced (principal series) (g,K )-module.
The corresponding representation ofGo has global character
REPRESENTATIONS OF WEYL GROUPS 11
1
∆
∑
w∈W
e−(yw)−1ρ.
(Thisisaspecialcaseoftherelationbetweentwoofthethreeclassificationsof (
g,K)-modules,ofHecht −Miliˇci´c−Schmid−Wolf [1986].)
Under the correspondence (1) between invariant eigendistributions onGo and on go the global
character corresponds to the distribution
1
π
∑
w∈W
e−(yw)−1ρ. (2)
In analogywith the data (z1,−ρ) for the Beilinson-Bernstein correspondence it seems natural to base
the character contours on the data (s1,−σ) which correspond to (z1,−ρ) under the automorphismι
interchangingk and go : s1 =bo ×¯bo and σ =(ρo,−ρo). We therefore write (2) as
1
π
∑
w∈W
e−(wιyw)−1σ =ϕw1y(−σ)( 3 )
where wι ∈W is the Weyl group element withwιρ =σ.
It follows from Theorem 5.1 that the character contour of the (g,K )-module Iy (based on the data
(s1,−σ)i s
C(Iy)= wιy·S 1 (4)
On the other hand, to a (D,K)-module M one can associate acharacteristic cycle;t h i si sa na l g e b r a i c
cycle of complex dimensionn on B∗ which is known to lie on the conormal varietyZ of theK-action
on B for these modulesM. It determines therefore a homologyclass inH2n(Z), denotedCh(M). Bya
result of Tanisaki [1985] (or bythe corresponding result of Kasihwara-Tanisaki[1984] for (D,B)-modules,
which amounts to essentiallythe same thing whengo itself is complex, as here) the characteristic cycle of
the inducedD-module Iy is
Ch(Iy)= y·Z 1. (5)
Since theIy and Iy form bases for the respectiveK-groups one ﬁnds bycomparing (4) and (5) :
