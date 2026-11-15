---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-006-5-coherent-families-of-eigendistributions
section_title: "Coherent families of eigendistributions."
section_number: 5
pages: 7-10
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
To bring in the Integral Formula we need to pass from the conormal variety Z of the K-action to the
conormal variety S of the Go-action by means of the involution ι : (x, y) →(x, ¯y) of g = go × go which
interchanges go = {(x, ¯x)} and k = {(x, x)}. Use this automorphism ι to transfer the represention of W on
H∗(Z) constructed above from Z to S. It is still induced by the transformations aλ(w) = pwλ(w)−1 ◦pλ
with pλ : B∗→Ωλ, u · (b1, ν) →u · (λ + ν), except that for S we need to take b1 = s1 = bo × ¯bo as
base-point in the deﬁnition of pλ (because ιab1,λ(w)ι = aιb1,ιλ(w) ∼aιb1,λ(w)).
REPRESENTATIONS OF WEYL GROUPS
8
Recall the Integral Formula: for Γ ∈H2n(S, C), and regular λ ∈h∗,
1
(2πi)n

pλΓ
exλ−σλ =
1
π(x)

y∈W
myey−1λ.
(1)
We also know that for Γ = Sw, my is up to a sign the local Euler number of Sw at sy :
my = (−1)no+l(w)−l(y)Euy(Sw) = (−1)no+l(w)−l(y)Euy(Zw)
(for Γ = Sw).
(1) is interpreted as an invariant eigendistribution on go, which we denoted θΓ (λ) :
θΓ (λ) =
1
(2πi)n

pλΓ
exλ−σλ
The right side of (1) may be written as
θΓ (λ) = 1
π

y∈W/Wo
myϕy(λ)
where
ϕy(λ) = 1
π

w∈Wo
e(yw)−1λ.
(2)
Any family θ(λ) of Go-invariant eigendistributions depending on λ ∈h∗which for regular λ is given by a
formula
θ(λ) = 1
π

y∈W
myey−1λ.
(3)
with myz = my for z ∈Wo, or equivalently
θ(λ) = 1
π

y∈W/Wo
myϕy(λ)
(4)
will be referred to as a coherent family of invariant eigendistributions on go∗. Is is evident that a coherent
family θ is determined by its value θ(λ) at a single regular λ. Furthermore, any θ(λ) given by (3) or (4)
for a single regular λ extends uniquely to a coherent family: to see this it suﬃces to know that the ϕy(λ)
extend, and that will become clear shortly. We shall denote the space of coherent families of invariant
eigendistributions on go by CH(go, C) or CH(go, Z) depending on whether we use complex or integral
coeﬃcients my in (3) or (4). The C or Z will be omitted when understood or unimportant.
The Weyl group W = Wo × Wo operates on the θ in the obvious way:
(w · θ)(λ) = θ(w−1λ)
and the resulting representation of W on CH(go, C) is evidently the biregular representation on Z[W/Wo] ≈
Z[Wo], with the ϕw, w ∈W/Wo, corresponding to the basis elements wWo of Z[W/Wo]. On the other
hand, we have the representation of W on H2n(S, Z) constructed above.
REPRESENTATIONS OF WEYL GROUPS
9
5.1 Theorem. The map
H2n(S, Z) →CH(go, Z),
Γ →θΓ ,
given by the Integral Formula is a W −isomorphism.
More precisely, the homology classes w·S1, w∈W/Wo, form a basis for H2n(S, Z). They correspond
to the basis (−1)noϕw,
w ∈W/Wo, of CH(go, Z) under the bijection Γ →θΓ .
Proof. That the map H2n(S) →CH(go) is a bijection we know from the Integral Formula : its matrix
(−1)no+l(w)−l(y)Euy(Sw) with respect to the bases Sw of H2n(S) and ϕw of CH(go), is integral and
unipotent-triangular with respect to the Bruhat order on W/Wo.
It suﬃces to prove the second assertion which says explicitly that for regular λ ∈h∗,
1
(2πi)n

pλwS1
exλ−σλ = (−1)no
π(x)

y∈Wo
e(wy)−1λ(x).
(5)
For w = 1 this is a special case of the Integral Formula : the K-orbit Z1 = K·z1 is smooth, so Euy(Z1) = 1
or 0, according as y ∈Wo or not. To see that (5) holds for all w ∈W we only need to identify the pλwS1.
The cycle pλS1 is the image under the map
pλ : B∗→Ωλ, u · (b1, ν) →u · (λ + ν)
of the conormal bundle of the closed Go-orbit Go · s1, where s1 = bo × ¯bo . That conormal bundle is
Go · {(s1, ν)|ν ∈s1⊥∩igo⊥}
Since Go = KoBo and bo ⊂s1 this conormal is also
= Ko · {(b1, ν)|ν ∈ibo
⊥}.
where bo
⊥⊂go∗is the orthogonal of bo in go∗(not in g∗). Its image under pλ becomes Ko · {λ + ibo
⊥}.
From the deﬁnition of the action of W on H2n(S) one ﬁnds that the cycle pλw · S1 on Ωλ which
ﬁgures in (5) is properly homotopic to Ko · {w−1λ + ibo
⊥}:
pλw · S1 ∼Ko · {w−1λ + ibo
⊥} on Ωλ.
taken with the appropriate orientation. So (5) says
1
(2πi)n

Ko·{w−1λ+ibo⊥}
exλ−σλ = (−1)no
π(x)

y∈Wo
e(wy)−1λ(x).
(6)
We know that this formula holds for w = 1 (and regular λ). Replacing λ by wλ one sees that it holds for
all w ∈W. Furthermore, writing the integral (6) as a double integral, ﬁrst over bo
⊥, then over Ko, one
sees that (6) exists for all λ ∈h∗(regular or not). This means that
ϕw(λ) is entire analytic in λ ∈h∗
as promised above. This ﬁnishes the proof of the theorem. We record explicitly the special case when
Γ = Sw :
REPRESENTATIONS OF WEYL GROUPS
