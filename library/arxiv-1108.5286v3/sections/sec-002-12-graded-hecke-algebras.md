---
doc_id: arxiv-1108.5286v3
doc_title: "Hochschild homology of affine Hecke algebras"
section_id: sec-002-12-graded-hecke-algebras
section_title: "Graded Hecke algebras"
section_number: 1.2
pages: 7-8
source_pdf: 1108.5286v3.pdf
source_sha256: 447d90883adce21e
doc_brief: "Hochschild homology of affine Hecke algebras — Let H = H(R,q ) be an aﬃne Hecke algebra with complex, possibly unequal parameters q, which are not roots of unity."
---
Graded Hecke algebras are also known as degenerate (aﬃne) He cke algebras. They
were introduced by Lusztig in [Lus2]. We call
˜R = (a∗,R, a,R∨, ∆) (5)
a degenerate root datum. We pick complex numbers kα forα ∈ ∆, such that kα =kβ
if α and β are in the same W -orbit. The graded Hecke algebra associated to these
data is the complex vector space
H = H( ˜R,k ) = S(t∗) ⊗ C[W ],
7
with multiplication deﬁned by the following rules:
• C[W ] and S(t∗) are canonically embedded as subalgebras;
• for x ∈ t∗ and sα ∈S we have the cross relation
x ·sα −sα ·sα(x) = kα⟨x, α∨⟩. (6)
Multiplication with any ǫ ∈ C× deﬁnes a bijection mǫ : t∗ → t∗, which clearly
extends to an algebra automorphism of S(t∗). From the cross relation (6) we see
that it extends even further, to an algebra isomorphism
mǫ : H( ˜R,ǫk ) → H( ˜R,k ) (7)
which is the identity on C[W ]. For ǫ = 0 this map is well-deﬁned, but obviously not
bijective.
Let Γ be a group of diagram automorphisms of R, and assume that kγ(α) =kα
for all α ∈R,γ ∈ Γ. Then Γ acts on H by the algebra automorphisms
ψγ : H → H,
ψγ(xsα) = γ(x)sγ(α) x ∈ t∗,α ∈ Π . (8)
By [Sol1, Proposition 5.1.a] the centre of the resulting cro ssed product algebra is
Z(H ⋊ Γ) = S(t∗)W ⋊Γ = O(t/(W ⋊ Γ)). (9)
We say that the central character of an H ⋊ Γ-representation is real if it lies in
a/(W ⋊ Γ).
