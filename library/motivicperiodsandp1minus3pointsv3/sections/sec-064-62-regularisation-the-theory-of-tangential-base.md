---
doc_id: motivicperiodsandp1minus3pointsv3
doc_title: "Motivic periods and P^1 minus 3 points"
section_id: sec-064-62-regularisation-the-theory-of-tangential-base
section_title: "Regularisation. The theory of tangential base points ([10], §15) gives"
section_number: 6.2
pages: 21-21
source_pdf: MotivicPeriodsandP1minus3pointsv3.pdf
source_sha256: 7870572b8cc316d0
doc_brief: "Motivic periods and P^1 minus 3 points — This is a review of the theory of the motivic fundamental grou p of the projective line minus three points, and its relation to mult iple zeta values."
---
a general procedure for regularising iterated integrals on curves. If one applies this
to the orbifold Γ \ \H, where Γ = SL 2(Z), one can show that it yields the completely
explicit formulae below, which generalise Zagier’s formul a for a single Eisenstein
series. I shall only state the ﬁnal answer. Via the map
τ ↦→q = exp(2iπτ ) : H − → {q ∈ C : 0 < |q| < 1} = D×
a natural choice of tangential base point (denoted
→
1∞) corresponds to the tangent
vector 1 at q = 0. Since in this case we have explicit models H ⊂ C for a universal
covering space of Γ \ \H, and C for the universal covering of D×, one can compute
all regularised iterated integrals by pulling them back to C as follows.
First, if f = ∑
n≥0 fnqn is the Fourier expansion of f , write
f ∞(τ ) = (2 πi)k−1f0(X − τ Y )k−2dτ ∈ Γ( C, Ω 1
C ⊗ Vk−2) (6.3)
Deﬁne a linear operator R on the tensor coalgebra on Γ( C, Ω 1
C ⊗ V ) by
R[ω1| . . . |ωn] =
n∑
i=0
(−1)n−i[ω1| . . . |ωi] x [ω∞
n | . . . |ω∞
i+1]
=
n∑
i=1
(−1)n−i
[
[ω1| . . .|ωi−1] x [ω∞
n | . . . |ω∞
i+1]
⏐
⏐
⏐ωi − ω∞
i
]
.
where V = ⨁
k Vk and ω∞ is the ‘residue at inﬁnity’ of ω deﬁned by (6 .3). The
regularised iterated integral can be expressed as ﬁnite integrals
∫ →
1∞
τ
[ω
1| . . . |ωn] =
n∑
i=0
∫ ∞
τ
R[ω1| . . . |ωi]
∫ 0
τ
[ω∞
i+1| . . .|ω
∞
n ]
It takes values in Vk1−2 ⊗ . . . ⊗ Vkn−2 ⊗ C if ω1, . . . , ωn are of weights k1, . . . kn,
and hence admits a right action of Γ. The integrals in the righ t factor on the
right-hand side are simply polynomials in τ and can be computed explicitly.
