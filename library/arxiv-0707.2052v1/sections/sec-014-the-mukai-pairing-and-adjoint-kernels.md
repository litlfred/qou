---
doc_id: arxiv-0707.2052v1
doc_title: "The Mukai pairing, I: a categorical approach"
section_id: sec-014-the-mukai-pairing-and-adjoint-kernels
section_title: "The Mukai pairing and adjoint kernels"
section_number: null
pages: 20-21
source_pdf: 0707.2052v1.pdf
source_sha256: 0a1d1cca848706be
doc_brief: "The Mukai pairing, I: a categorical approach — We study the Hochschild homology of smooth spaces, emphasiz ing the importance of a pairing which generalizes Mukai’s pairi ng on the cohomology of K3"
---
In this section we deﬁne the Mukai pairing on the Hochschild h omology of
a space and show that the push-forwards of adjoint kernels ar e themselves
adjoint linear maps with respect to this pairing.
First observe from Section 3.4 that we have two isomorphisms :
τR, τL: HH•(X) = Hom− •(Σ− 1
X , IdX) ∼−→ Hom•(IdX, ΣX),
given by
τR

 v

 := v and τL

 v′

 := v′ .
Note that this diﬀers slightly from the given deﬁnition, but we have used
the uniqueness of adjoints. The above isomorphisms allow th e deﬁnition of
the Mukai pairing as follows.
Deﬁnition. The Mukai pairing on the Hochschild homology of a space X
is the map
⟨− , − ⟩M : HH•(X) ⊗ HH•(X)→ k,
deﬁned by ⟨
v, v ′⟩
M := Tr
(
τR(v) ◦ τL(v ′)
)
.
20
Diagrammatically, this is
⟨
v , v′
⟩
M
:= Tr

 v v′

 .
Observe that as τR and τL are both isomorphisms and as the Serre pairing
is non-degenerate, it follows that the Mukai pairing is non- degenerate.
We can now easily show that adjoint kernels give rise to adjoi nt maps
between the corresponding Hochschild homology groups.
Theorem 8 (Adjointness). If Φ : X→ Y and Ψ : Y→ X are adjoint kernels,
Ψ ⊣ Φ, then the corresponding push forwards are adjoint with resp ect to the
Mukai pairing in the sense that for all w ∈ HH•(X) and v ∈ HH•(Y) we have
⟨Ψ∗(v), w ⟩M = ⟨v, Φ ∗(w)⟩M.
Proof. Note ﬁrst that Ψ∗ = Φ∗, by Theorem 7. Thus
⟨Ψ∗(v), w ⟩M = ⟨Φ∗(v), w ⟩M = Tr


Φ 
v w 


= Tr

 v
Φ 
w 

 = Tr

 v w 
Φ 


= ⟨v, Φ ∗(w)⟩M.
Corollary 9. If the integral kernel Φ : X→ Y induces an equivalence on
derived categories, then Φ∗ : HH•(X)→ HH•(Y) is an isometry.
Proof. If Φ induces an equivalence, then it has a left adjoint Ψ : Y → X
which induces the inverse, so Ψ ◦ Φ ∼= IdX, and we know that (IdX)∗ is the
identity map. Thus
⟨Φ∗v, Φ ∗w⟩M = ⟨Ψ∗Φ∗v, w ⟩M = ⟨(Ψ ◦ Φ)∗v, w ⟩M = ⟨v, w ⟩M.
