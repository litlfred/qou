---
doc_id: arxiv-0906.1500v4
doc_title: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds"
section_id: sec-034-822-computation-of-ϕadρ
section_title: "Computation of ∆ ϕ⊗Ad◦ρ"
section_number: 8.2.2
pages: 24-25
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "Twisted Alexander invariant and non-abelian Reidemeister torsion for hyperbolic three-manifolds — W e study a computational method of the hyperbolic Reidemeister torsion (also called in the"
---
∂M (t). By using the Multiplicativity Lemma, we have
∆ ϕ⊗Ad◦ρ
∪b
ℓ=1T 2
ℓ
(t) = ( −1)b−1∆ ϕ⊗Ad◦ρ
T 2
b
(t) · ∆ ϕ⊗Ad◦ρ
∪b−1
ℓ=1 T 2
ℓ
(t).
Hence we have
∆ ϕ⊗Ad◦ρ
∂M (t) = ( −1)b(b−1)/2
b∏
ℓ=1
∆ ϕ⊗Ad◦ρ
T 2
ℓ
(t).
Furthermore a direct computation provides the following lemma:
Lemma 15. The torsion ∆ ϕ⊗Ad◦ρ
T 2
ℓ
(t) of the ℓ-th component of ∂M with the homology
orientation given by the ordered basis {[ [T 2
ℓ ] ], [ [λℓ] ], [ [µℓ] ], [ [pℓ] ]} is equal to +1.
As a consequence, the twisted Alexander invariant of ∂M is given by:
(35) ∆ ϕ⊗Ad◦ρ
∂M (t) = ( −1)b(b−1)/2.
8.2.3. Computation of ∆ ϕ⊗Ad◦ρ
(M,∂M )(t). Here we use the duality properties of torsion proved
by M. Farber and V. Turaev in [FT00]. We write the torsion ∆ ϕ⊗Ad◦ρ
(M,∂M )(t) in the right
hand side of Equation (34) as the torsion in the left hand side with a sig n term. Let
(M ′, ∂M ′) denotes the dual cell decomposition of ( M, ∂M ). Using the invariance of the
Reidemeister torsion under subdivisions of CW–pairs we obtain :
∆ ϕ⊗Ad◦ρ
(M,∂M )(t) = ∆ ϕ⊗Ad◦ρ
(M ′,∂M ′)(t).
Let ρ⋆ : π1(M ) → SL2(C) be the following representation
ρ⋆ =
( 0 1
−1 0
)
ρ
( 0 1
−1 0
) −1
.
Using the invariance of the Reidemeister torsion under conjugation of representations we
thus have
∆ ϕ⊗Ad◦ρ
(M,∂M )(t) = ∆ ϕ⊗Ad◦ρ
(M ′,∂M ′)(t) = ∆ ϕ⊗Ad◦ρ⋆
(M ′,∂M ′)(t).
Observe that the pair ( M ′, ∂M ′) and the representation ϕ ⊗ Ad ◦ ρ⋆ give the dual
chain complex of M twisted by the representation
ϕ ⊗ Ad ◦ ρ, i.e., the sl2(C(t))ρ⋆ -twisted
chain complex C∗(M ′, ∂M ′; sl2(C(t))ρ⋆ ) can be identiﬁed with the dual chain complex
of C∗(M ; sl2(t)ρ). By using this identiﬁcation and the duality of torsion in [FT00], the
torsion ∆ ϕ⊗Ad◦ρ
(M,∂M )(t) is expressed as
∆ ϕ⊗Ad◦ρ
(M,∂M )(t) = ∆ ϕ⊗Ad◦ρ⋆
(M ′,∂M ′)(t)
= (−1)s(H∗(M;R))+s(C∗(M;R)) · (−1)s(C∗(M;sl2(C(t))ρ)) · ∆ ϕ⊗Ad◦ρ
M (t).(36)
Here s(C∗) = ∑ m
q=1 αq−1(C∗)αq(C∗) for a chain complex C∗ = Cm ⊕ · · · ⊕ C0, with
αq(C∗) = ∑ q
j=0 dim Cj . Further observe the sign term diﬀerence between Farber–
Turaev’s formula and Equation (36): here the sign term ∑ (m−1)/2
q=0 α2q(C∗) used in [FT00]
is omitted from s(C∗) because we use the complex C∗(M ′, ∂M ′; sl2(C(t))ρ) instead of the
dual complex of C∗(M ; sl2(C(t))ρ).
24
The ﬁrst sign ( −1)s(H∗(M;R))+s(C∗(M;R)) in Equation (36) comes from the duality of
the sign terms τ0 in ∆ ϕ⊗Ad◦ρ
(M,∂M )(t) and the second one ( −1)s(C∗(M;sl2(C(t))ρ)) in Equa-
tion (36) comes from the duality of torsions for C∗(M ; sl2(C(t))ρ). Since s(C∗(M ; R))
and s(C∗(M ; sl2(C(t))ρ)) are equal in Z/2Z, it turns out that
(37) ∆ ϕ⊗Ad◦ρ
(M,∂M )(t) = ( −1)s(H∗(M;R))∆ ϕ⊗Ad◦ρ
M (t).
