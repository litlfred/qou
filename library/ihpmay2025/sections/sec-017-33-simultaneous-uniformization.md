---
doc_id: ihpmay2025
doc_title: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS"
section_id: sec-017-33-simultaneous-uniformization
section_title: "Simultaneous uniformization"
section_number: 3.3
pages: 23-24
source_pdf: IHPMay2025.pdf
source_sha256: 0440a39721552a9e
toc_source: outline
doc_brief: "IHP LECTURES ON HYPERBOLIC 3-MANIFOLDS — These notes are designed to accompany my mini-course on hyperbolic 3-manifolds at IHP in May 2025."
---
Bers [8] showed that B gives a complete parametrization of QF(S).
Theorem 3.6. The map
B : QF(S) →T (S) × T ( ¯S)
is a homeomorphism.
Proof. We first prove that B is injective.
If B(ρ1) = B(ρ2), then there exists a conformal
map ψ : ∂cNρ1 →∂cNρ2 in the homotopy class of hρ2 ◦h−1
ρ1 . This map lifts to a conformal
homeomorphism ˜ψ : Ω(ρ1) →Ω(ρ2) so that ρ2(γ) = ˜ϕ ◦ρ1(γ) ◦˜ϕ−1 for all γ ∈π1(S).
We may use the radial coordinates on b
Nρi −C1(Nρi) to extend ψ to a differentiable bilipschitz
homeomorphism Ψ from Nρ1 \ intC1(Nρ1) to Nρ2 \ intC1(Nρ2). Since C1(Nρ1) and C1(Nρ2) are
homeomorphic, we may then extend Ψ to a differentiable bilipschitz diffeomorphism from Nρ1
to Nρ2. The map Ψ lifts to a bilipschitz map from H3 to H3 which admits a continuous extension
to a quasiconformal homeomorphism C of ∂H3. By construction, C agrees with ˜ψ on Ω(ρ1).
(Bers uses a more analytic argument to construct the extension C.)
Since Λ(ρ1) has measure zero and C is conformal on Ω(ρ1), we conclude that C is conformal
and that ρ2(γ) = C ◦ρ1(γ) ◦C−1 for all γ ∈π1(S). Therefore ρ1 = ρ2 ∈QF(S).
The fact that B is surjective is an application of the Measurable Riemann Mapping Theorem.
Suppose that (Y, ¯Z) ∈T (S) × T ( ¯S). Let ρ0 be a Fuchsian group so that B(ρ0) = (X, ¯X). Let
ψ : X ∪¯X →Y ∪¯Z be an orientation-preserving diffeomorphism (in the correct homotopy
class). We may lift ψ to a map ˜ψ : Ω(ρ0) →H2 ∪H2 and compute its Beltrami differential µ ˜ψ.
We may then extend µ ˜ψ to a Beltrami differential on ∂H3 by setting it equal to 0 on Λ(ρ0).
The Measurable Riemann Mapping Theorem implies that there exists a quasiconformal map
ϕ : ∂H3 →∂H3 with Beltrami differential µ.
By construction, ψ ◦ρ0(g)ψ−1 is conformal, so ψ ◦ρ0(g) and ψ have the same Beltrami
differential for all g ∈π1(S). Thus, ϕ ◦ρ0(g) and ϕ have the same Beltrami differential on
24
RICHARD D. CANARY
Ω(ρ0), and hence on ˆC, for all g ∈π1(S). The uniqueness portion of the Measurable Riemann
Mapping Theorem then implies that ϕ ◦ρ0(g) and ϕ differ by postcomposition by a M¨obius
transformation. Therefore, ϕ ◦ρ0(g) ◦ϕ−1i is conformal, for all g ∈π1(S), so we obtain a
faifthful representation ρ : π1(S) →PSL(2, C) defined by ρ(γ) = ϕ ◦ρ0(γ) ◦ϕ−1 for all γ ∈Γ. ρ
is discrete since ρ(π1(S)) acts properly discontinuously on ϕ(Ω(ρ0)).
Then b
Nρ is an irreducible, orientable manifold homotopy equivalent to S. It has two boundary
components which are homotopic, hence homologous, which implies that b
Nρ is compact, and
hence that ρ is convex cocompact. Since ϕ and ˜ψ have the same Beltrami differential on Ω(ρ0),
we see that ϕ ◦˜ψ−1 is a conformal homeomorphism from H2 ∪H2 to Ω(ρ) which descends to
a conformal homeomorphism from Y ∪¯Z to ∂cNρ. Therefore, B(ρ) = (Y, ¯Z). (If one prefers a
more geometric argument, one may use work of Douady and Earle [34] to extend the quotient
of ϕ to a homeomorphism of b
Nρ0 to b
Nρ which is bilipschitz on Nρ0.) Therefore, ρ ∈QF(S) and
B(ρ) = (Y, ¯Z).) We have now shown that B is surjective which completes the proof.
□
