---
doc_id: arxiv-0905.0591v3
doc_title: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS"
section_id: sec-009-33-change-of-variables
section_title: "Change of variables"
section_number: 3.3
pages: 8-9
source_pdf: friedvidu1.pdf
source_sha256: cfeaf61f759a6af8
doc_brief: "A SURVEY OF TWISTED ALEXANDER POLYNOMIALS — We give a short introduction to the theory of twisted Alexand er polynomials of a 3–manifold associated to a representation of its fundam ental group."
---
variables in twisted Alexander polynomials, in particular this discussion will show how to
A SUR VEY OF TWISTED ALEXANDER POLYNOMIALS 9
obtain one–variable twisted Alexander polynomials from mu lti–variable twisted Alexander
polynomials.
Throughout this section let N be a 3–manifold with empty or toroidal boundary, let ψ :
π1(N ) →F be a non–trivial homomorphism to a free abelian group F and let γ :π1(N ) →
GL(k,R ) be a representation. Furthermore let φ : F → H also be a homomorphism to a
free abelian group such that φ◦ψ is non–trivial. We denote the induced ring homomorphism
R[F ] →R[H] by φ as well. Let
S = {f ∈R[F ] |φ(R[F ]) ⁄= 0 ∈R[H]}.
Note that φ induces a homomorphism R[F ]S−1 →Q(R[H]) which we also denote by φ.
The following is a slight generalization of [FK08a, Theorem 6.6], which in turn builds on
ideas of Turaev (cf. [Tu86] and [Tu01]).
Proposition 3.4. We have τ (N,γ ⊗ψ) ∈R[F ]S−1, and
τ (N,γ ⊗ψ ◦φ) .=φ(τ (N,γ ⊗ψ)).
The following is now an immediate corollary of the previous p roposition and Proposition
3.2.
Corollary 3.5. Assume that γ :π1(N ) → GL(k,R ) is a representation with R a Noetherian
UFD. If φ
(
∆ γ⊗ψ
N
)
⁄= 0, then we have the following equality:
2∏
i=0
(
∆ γ⊗φ◦ψ
N,i
) (−1)i+1
.=φ
( 2∏
i=0
(
∆ γ⊗ψ
N,i
) (−1)i+1
)
.
In particular, if rank {Im{π1(N )
φ◦ψ
− − →H}} ≥ 2, then
∆ γ⊗φ◦φ
N
.=φ
(
∆ γ⊗ψ
N
)
.
