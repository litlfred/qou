---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-014-32-quasifconformal-conjugacy
section_title: "Quasifconformal conjugacy"
section_number: 3.2
pages: 22-23
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
We now show that any two quasifuchsian representations are quasiconformally conjugate.
Theorem 3.4. If ρ1,ρ 2∈ QF (S), then there exists a quasiconformal map ϕ : ∂H3→ ∂H3, so
that ρ2(γ) =ϕ◦ρ2(γ)◦ϕ−1 for all γ∈ Γ.
Proof. Lethρi :S×[0, 1]→C1(Nρi) be orientation-preserving homeomorphism in the homotopy
class of ρi. Since C1(Nρi) is a compact C1-manifold, we may assume that hρi is bilipschitz. So
h =hρ2◦h−1
ρ1 :C1(Nρ1)→C1(Nρ2)
IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS 23
is a bilipschitz homeomorphism. We may then extend h radially in the coordinates to obtain
an orientation-preserving bilipschitz homeomorphism
H :Nρ1→Nρ2
where if x∈Nρ1−C1(Nρ1) has coordinates (y,t ), then H(x) has coordinates (h(y),t ).
Then H lifts to an orientation-preserving bilipschitz homeomorphism ˜H : H3→ H3 which
conjugates the action of ρ1(π1(S)) to the action of ρ2(π1(S), so, perhaps after precomposition
by an element of ρ1(π1(S)),
˜H◦ρ1(γ) =ρ2(γ)◦ ˜H
for allγ∈π1(S). Then ˜H extends to a quasiconformal homeomorphismϕ :∂H3→∂H3 so that
ϕ◦ρ1(γ) =ρ2(γ)◦ϕ
for all γ∈π1(S). □
If ρ1 is Fuchsian, then its limit set has measure zero, which implies that Λ( ρ2) = ϕ(Λ(ρ1))
also has measure zero.
Corollary 3.5. If ρ∈QF (S), then Λ(ρ) has measure zero.
