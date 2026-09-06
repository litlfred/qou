---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-014-32-hopf-modules-since-a-quantum-groupoid-h-is-bo
section_title: "Hopf modules. Since a quantum groupoid H is both algebra and coalgebra,"
section_number: 3.2
pages: 11-12
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
one can consider modules and comodules over H. As in the theory of Hopf algebras,
an H-Hopf module is an H-module which is also an H-comodule such that these
two structures are compatible (the action “commutes” with coact ion) :
Deﬁnition 3.2.1. A right H-Hopf module is such a k-vector space M that
(i) M is a right H-module via m ⊗h ↦→m ·h,
(ii) M is a right H-comodule via m ↦→ρ(m) = m(0) ⊗m(1),
(iii) (m ·h)(0) ⊗ (m ·h)(1) =m(0) ·h(1) ⊗m(1)h(2)
for all m ∈M and h ∈H.
Remark 3.2.2. Condition (iii) above means that ρ is a right H-module map, where
(M ⊗H)∆(1) is a right H-module via (m ⊗h)∆(1) ·h = (m ·h(1)) ⊗ (h ·h(2)).
Example 3.2.3. H itself is an H-Hopf module via ρ = ∆.
Example 3.2.4. The dual vector space ˆH becomes a right H-Hopf module :
φ ·h =S(h)⇀φ φ (0)⟨ψ, φ(1) ⟩ =ψφ,
for all φ,ψ ∈ ˆH, h∈H. Indeed, we need to check that
(φ ·h)(0) ⊗ (φ ·h)(1) =φ(0) ·h(1) ⊗φ(1)h(2), φ ∈ ˆH,h ∈H.
Evaluating both sides against ψ ∈ ˆH in the ﬁrst factor we have :
(φ(0) ·h(1))⟨ψ, φ(1)h(1) ⟩ = ( ψ(1)φ) ·h(1)⟨ψ(2), h(2) ⟩
= ψ(1)φ(1)⟨S(ψ(2)φ(2)), h(1) ⟩⟨ψ(3), h(2) ⟩
= ψ(1)φ(1)⟨S−1εs(ψ(2))φ(2), S(h) ⟩
= ψφ(1)⟨φ(2), S(h) ⟩
= ψ(S(h)⇀φ ) = ψ(φ ·h)
= ( φ ·h)(0)⟨ψ, (φ ·h)(1) ⟩.
where we used Proposition 2.3.4 and that S−1εs(ψ) ∈ ˆHt for all ψ ∈ ˆH.
The fundamental theorem for Hopf modules over Hopf algebras ([M ], 1.9.4) gen-
eralizes to quantum groupoids as follows :
Theorem 3.2.5 ([BNSz], 3.9) . LetM be a right H-Hopf module and
N =CoinvM = {m ∈M |m(0) ⊗m(1) =m1(1) ⊗ 1(2)}(20)
be the set of coinvariants. The Ht-module tensor product N ⊗HtH (whereN is a
right Ht-submodule) is a right H-Hopf module via
(n ⊗h) ·g =n ⊗hg, (n ⊗h)(0) ⊗ (n ⊗h)(1) = (n ⊗h(1)) ⊗h(2),(21)
for all h,g ∈H and n ∈N . Then the map
α :N ⊗HtH →M :n ⊗h ↦→n ·h(22)
is an isomorphism of right Hopf modules.
