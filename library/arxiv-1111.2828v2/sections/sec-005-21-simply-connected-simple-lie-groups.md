---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-005-21-simply-connected-simple-lie-groups
section_title: "Simply connected, simple Lie groups"
section_number: 2.1
pages: 8-9
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
H 2(G; Z) are trivial, and H 3(G; Z) ∼= Z. Hence, by the Serre spectral sequence for the universal
bundle, we have an isomorphism
(2.2) S : H 4(BG; Z) ∼= H 3(G; Z) ∼= Z
called the suspension. The Killing form on G deﬁnes an invariant polynomial B ∈ I 2(G; F), and
since B is real on the maximal compact subgroup K of G, W (B) is a real class. Hence, there exists
a unique positive real number α such that W (αB) is a generator of H 4(BG; 4π2Z). We refer to αB
as the renormalized Killing form , and denote the Cheeger-Chern-Simons class SαB,W (αB) byˆc.
Recall that every class in H 3(G; F) can be represented by a G-invariant 3-form. The following is
well known (see e.g. Kamber-Tondeur [ 18, (5.74) p. 116]).
Proposition 2.1. Let P ∈ I 2(G; F). The suspension of W (P ) is represented by the invariant
3-form
(2.3) σ(P ) = − 1
6 P (ω ∧ [ω, ω]) ∈ Ω 3(G; F)G
where ω is the Maurer-Cartan form on G. □
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 9
Let E → M be a G-bundle with ﬂat connection θ. We can view θ as a map g∗ → Ω 1(E; F), so
by taking exterior powers, θ induces a map
(2.4) θ : Ω 3(G)G = ∧3(g∗) → Ω 3(E; F).
Note that θ(σ(P )) = − 1
6P (θ ∧ [θ, θ]). In the following, P denotes the renormalized Killing form.
Proposition 2.2 ([6, Proposition 2.8]) . Let E → M be a G-bundle, with ﬂat connection θ, over a
closed 3-manifold M . The cohomology class ˆc(E) ∈ H 3(M ; F/4π2Z) satisﬁes
(2.5) ˆc(E)([M ]) =
∫
M
s∗(
θ(σ(P ))
)
∈ F/4π2Z,
where s is a section of E (which exists since G is 2-connected). □
Remark 2.3. Since σ(P ) ∈ H 3(G; 4π2Z) is a generator, it follows that a change of section changes
the integral by a multiple of 4π2Z.
Example 2.4. For G = SL(n, C), the renormalized killing form P equals 1
2 Tr, where Tr is the trace
form (A, B) ↦→Tr(AB). For a ﬂat connection, dθ = − 1
2 [θ, θ] = −θ ∧ θ, so ( 2.5) yields
(2.6) ˆc(E)([M ]) = 1
2
∫
M
s∗(
Tr(θ ∧ dθ + 2
3 θ ∧ θ ∧ θ)
)
∈ C/4π2Z
recovering the Chern-Simons integral ( 1.1). Note that P also equals the (renormalized) second
Chern-polynomial c2. It thus follows that ˆc =ˆc2.
