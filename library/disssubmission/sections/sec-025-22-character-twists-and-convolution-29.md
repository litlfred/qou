---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-025-22-character-twists-and-convolution-29
section_title: "Character twists and convolution 29"
section_number: 2.2
pages: 37-38
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
of the diagram
a∗L
ϕ // L⊠L p∗
1L⊗ p∗
2L
σ∗a∗L
σ∗(ϕ) // σ∗(L⊠L) p∗
2L⊗ p∗
1L
S′∼=
OO
where σ : X×X→ X×X is the morphism (x,y)↦→ (y,x) and S′ is the
symmetry constraint of the ordinary tensor product. Since in any case our
diagram commutes up to a scalar inΛ∗, it sufﬁces to check commutativity
on the stalks at the origin(0,0). There everything boils down to the fact
that (λ⊗λ)(u⊗v) = (λ⊗λ)(v⊗u) for allu,v∈ L0.
Next we claim that the isomorphismsψ are also compatible with the
associativity constraint of the symmetric monoidal category(Dbc (X,Λ),∗).
Indeed, by strictness [106, p. 11] the associativity constraints are the iden-
tity morphisms, so it sufﬁces to show that the diagram
((A∗B)∗C)χ
ψ // ((A∗B)χ)∗Cχ
ψ∗id // (Aχ∗Bχ)∗Cχ
(A∗(B∗C))χ
ψ // Aχ∗((B∗C)χ)
id∗ψ // Aχ∗(Bχ∗Cχ)
commutes for allA,B,C∈ Dbc (X,Λ). Writing
((A∗B)∗C)χ = Ra∗R(a×id)∗(((A⊠B)⊠C)⊗(a×id)∗a∗L)
and similarly for the other convolutions, the commutativity of the diagram
becomes equivalent to the commutativity of the diagram onX×X×X
(a×id)∗a∗L
(a×id)∗ϕ// (a×id)∗L⊠L = a∗L⊠L
ϕ⊠id // (L⊠L)⊠L
(id×a)∗a∗L
(id×a)∗ϕ// (id×a)∗L⊠L = L⊠a∗L
id⊠ϕ // L⊠(L⊠L)
Again it sufﬁces to check the commutativity on stalks at(0,0,0). The upper
arrow becomes the composition
(ϕ⊗id)◦ϕ : L0−→L0⊗ΛL0−→ (L0⊗ΛL0)⊗ΛL0.
The inverse morphism maps(α·v⊗β·v)⊗γ·v to (αβ)γ·v. By a similar
computation for the lower row, the commutativity of the diagram hence
boils down to the associativity law(αβ)γ = α(β γ) of the ﬁeldΛ. □
As a trivial by-product, the tensor functoriality provides a simple proof
of the following result of [59].
