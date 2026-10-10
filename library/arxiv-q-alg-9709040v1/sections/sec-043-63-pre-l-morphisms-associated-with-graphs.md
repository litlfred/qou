---
doc_id: arxiv-q-alg-9709040v1
doc_title: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I"
section_id: sec-043-63-pre-l-morphisms-associated-with-graphs
section_title: "Pre-L∞-morphisms associated with graphs"
section_number: 6.3
pages: 23-24
source_pdf: 9709040v1.pdf
source_sha256: 8baf650d86c5b8ab
doc_brief: "DEFORMATION QUANTIZATION OF POISSON MANIFOLDS, I — 83 sections: Front matter; Introduction; Deformation quantization"
---
For any admissible graph Γ with n vertices of the ﬁrst type, m vertices of the second type, and 2 n +
m− 2 +l edges where l∈ Z, we deﬁne a linear map UΓ :⊗nTpoly(Rd)−→Dpoly(Rd)[1 +l−n]. This map
has only one non-zero graded component ( UΓ )(k1,...,k n) where ki = #Star(i)− 1, i = 1,...,n . If l = 0 then
fromUΓ after anti-symmetrization we obtain a pre- L∞-morphism.
Let γ1,...,γ n be polyvector ﬁelds on Rd of degrees (k1 + 1),..., (kn + 1), and f1,...,f m be functions
on Rd. We are going to write a formula for function Φ on Rn:
Φ := ( UΓ (γ1⊗... ⊗γn)) (f1⊗... ⊗fm) .
The formula for Φ is the sum over all conﬁgurations of indices running from 1 to d, labeled by EΓ :
Φ =
∑
I:EΓ−→{1,...,d }
Φ I ,
where Φ I is the product over all n +m vertices of Γ of certain partial derivatives of functions gj and of
coeﬃcients of γi.
Namely, with each vertex i, 1≤ i≤ n of the ﬁrst type we associate function ψi on Rd which is a
coeﬃcient of the polyvector ﬁeld γi:
ψi =⟨γi,dx I(e1
i )⊗... ⊗dxI(e
ki +1
i )⟩.
Here we use the identiﬁcation of polyvector ﬁelds with skew- symmetric tensor ﬁelds as
ξ1∧... ∧ξk+1−→
∑
σ∈Σ k+1
sgn(σ)ξσ 1⊗... ⊗ξσ k+1∈ Γ( Rd,T⊗(k+1)) .
For each vertex j of second type the associated function ψj is deﬁned as fj.
Now, at each vertex of graph Γ we put a function on Rd (i.e. ψi or ψj). Also, on edges of graph Γ
there are indices I(e) which label coordinates in Rd. In the next step we put into each vertex v instead of
function ψv its partial derivative 
 ∏
e∈EΓ , e =(∗,v )
∂I(e)

ψv,
23
and then take the product over all vertices v of Γ. The result is by deﬁnition the summand Φ I .
Construction of the function Φ from the graph Γ, polyvector ﬁ elds γi and functions fj, is invariant
under the action of the group of aﬃne transformations of Rd because we contract upper and lower indices.
