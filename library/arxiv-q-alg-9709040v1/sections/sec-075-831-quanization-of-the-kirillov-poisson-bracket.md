---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-075-831-quanization-of-the-kirillov-poisson-bracket
section_title: "Quanization of the Kirillov-Poisson bracket"
section_number: 8.3.1
pages: 39-40
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
Let g be a ﬁnite-dimensional Lie algebra over R. The dual space to g endowed with the Kirillov-Poisson
bracket is naturally a Poisson manifold (see [Ki]). We remin d here the formula for this bracket: if p∈ g∗ is
a point and f,g are two functions on g then the value{f,g}|p is deﬁned as ⟨p, [df|p,dg|p]⟩where diﬀerentials
of functions f,g at p are considered as elements of g≃ (g∗)∗. One can consider g∗ as an algebraic Poisson
manifold because coeﬃcients of the Kirillov-Poisson brack et are linear functions on g∗.
Theorem. The canonical quantization of the Poisson manifold g∗ is isomorphic to the family of algebras
U¯h(g) deﬁned as universal enveloping algebras of g endowed with the bracket ¯h[, ].
Proof: in 6.4 we constructed a canonical star-product on the algebr a of functions on a aﬃne space for
a given Poisson structure. Thus, we have canonical star-pro duct on C∞(g∗). We claim that the product of
any two polynomials on g∗ is a polynomial in ¯ h with coeﬃcients which are polynomials on g∗. The reason
is that the star-product is constructed using contraction o f indices. Let us denote by β∈ g∗⊗ g∗⊗ g the
tensor giving the Lie bracket on g. All natural operations Sym k(g)⊗Sym l(g)−→Sym m(g) which can be
deﬁned by contractions of indices with several copies of β, exist only for m≤k +l, and for every given m
there are only ﬁnitely many ways to contract indices. Thus, i t makes sense to put ¯h equal to 1 and obtain a
product on Sym (g) =⊕k≥0Sym k(g). We denote this product also by ⋆.
It is easy to see that for γ1,γ 2∈ g the following identity holds:
γ1⋆γ 2−γ2⋆γ 1 = [γ1,γ 2] .
Moreover, the top component of ⋆-product which maps Sym k(g)⊗Sym l(g) toSym k+l(g), coincides with the
product on Sym (g). From this two facts one concludes that there exists a uniqu e isomorphism of algebras
Ialg : (Ug,·)−→(Sym (g),⋆ )
such that Ialg(γ) = γ for γ∈ g, where · denotes the universal enveloping algebra of g with the standard
product.
One can easily recover variable ¯h in this description and get the statement of the theorem. Q.E.D.
Corollary . The center of the universal enveloping algebra is canonical ly isomorphic as an algebra to the
algebra
(
Sym (g)
) g
of g-invariant polynomials on g∗.
Proof: The center of Ug is 0-th cohomology for the (local) Hochschild complex of Ug endowed with
the standard cup-product. The algebra
(
Sym (g)
) g
is the 0-th cohomology of the algebra of polyvector ﬁelds
on g∗ endowed with the diﬀerential [ α,·] where α is the Kirillov-Poisson bracket. From the theorem 8.2 we
conclude that applying the tangent map to U we get an isomorphism of algebras.
39
