---
doc_id: 0504116v2
doc_title: "On deformations of hyperbolic 3-manifolds with geodesic boundary"
section_id: sec-014-a1-the-tangent-space-to-a-representation
section_title: "A.1 The tangent space to a representation"
section_number: null
pages: 21-22
source_pdf: 0504116v2.pdf
source_sha256: 24a8c998e40aed5d
doc_brief: "On deformations of hyperbolic 3-manifolds with geodesic boundary (Frigerio, AGT 6 (2006) 435–457) — the solution variety of consistency equations for a geometric partially truncated triangulation…"
---
Let G be a Lie group with associated Lie algebra g and Γ be any group, and denote by
R(Γ, G) the set of representations of Γ in G. We say that a path{ρt∈R (Γ, G) : t∈
(−ε,ε )} is smooth ifρt(γ) is a smooth function of t for anyγ∈ Γ. If{ρt} is a smooth
path of representations, the tangent vector to the map t↦→ρt(γ) at 0 gives an element
in Tρ0(γ)G. Identifying this tangent space with g = T1G by right translation we get an
element ˙ρ(γ) of the Lie algebra g:
˙ρ(γ) = d
dt
⏐⏐⏐
t=0
(
ρt(γ)ρ0(γ)−1)
.
Differentiating the homomorphism relationρt(γ1γ2) =ρt(γ1)ρt(γ2) we see that ˙ρ : Γ→
g satisﬁes the so-called cocycle relation
˙ρ(γ1γ2) = ˙ρ(γ1) + Ad(ρ0(γ1))( ˙ρ(γ2)),
Algebraic &GeometricTopology 6 (2006)
456 Roberto Frigerio
where Ad : G→ GL(g) is the usual adjoint representation.
Consider now a trivial deformation of ρ0, ie, let t↦→ gt be a smooth path in G starting
at the identity and set ρt(γ) = gtρ0(γ)g−1
t for all γ∈ Γ. Then differentiation shows
that
˙ρ(γ) = ˙g− Ad(ρ0(γ))(˙g)
for anyγ∈ Γ, where ˙g∈ g is the tangent vector to t↦→ gt at t = 0. We now set:
Z1(Γ; g;ρ0) = {c : Γ→ g : c(γ1γ2) = c(γ1) + Ad(ρ0(γ1))(c(γ2))}
B1(Γ; g;ρ0) = {b : Γ→ g : b(γ) = m− Ad(ρ0(γ))(m) for some m∈ g}
H1(Γ; g;ρ0) = Z1(Γ; g;ρ0)/B1(Γ; g;ρ0)
The above discussion shows that Z1(Γ; g;ρ0) corresponds in some sense to the tangent
space of R(Γ, G) at ρ0. Under this identiﬁcation the module B1(Γ; g;ρ0) should
represent the tangent space to trivial deformations ofρ0, so H1(Γ; g;ρ0) should give
the tangent space ofR(Γ, G)/G at [ρ0] (however, this holds true only in the setting of
algebraic schemes).
Let c∈ Z1(Γ; g;ρ), and suppose that Γ0 is a normal subgroup ofΓ such thatρ(γ) = 1G,
c(γ) = 0 for all γ∈ Γ0. Let also ¯ρ : Γ/Γ0→ G be the representation induced byρ.
Lemma A.1 The map ¯c : Γ/Γ0→ M deﬁned by ¯c([γ]) = c(γ) is well-deﬁned and
gives a cocycle ¯c∈ Z1(Γ/Γ0; g; ¯ρ). Moreover, we have ¯c∈ B1(Γ/Γ0; g; ¯ρ) if and only
if c∈ B1(Γ; g;ρ).
