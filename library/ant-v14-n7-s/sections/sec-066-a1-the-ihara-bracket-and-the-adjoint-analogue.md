---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-066-a1-the-ihara-bracket-and-the-adjoint-analogue
section_title: "A.1. The Ihara bracket and the adjoint analogue"
section_number: null
pages: 78-79
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
[Deligne and Goncharov 2005, Section 5.10]. The Ihara bracket is the Lie bracket of Lie(Vω), regarded
via the isomorphism Lie(Vω)≃ Lie(51,0),v↦→v(150); namely, it is given by the following formula
[loc. cit, Section 5.12–5.13]:
{ f, g}=[ f, g]+ D f(g)+ Dg( f),
where D f is the derivation which sends e0↦→ 0 and eξ↦→[ f(ξ), eξ] for any ξ∈µN(K). The Ihara
bracket is a Poisson bracket; namely it satisﬁes the equality{ f g, h}={ f, h}g+ f{g, h}.
Let ˜Vω be the preimage of ˜51,0 by the isomorphism Vω ∼−→51,0,v↦→v(150).
We have deﬁned in [Jarossay 2015, Deﬁnition 1.1.3] the adjoint Ihara product ((1 -6)) and we have
proved in [loc. cit., Proposition 1.1.4] that Ad(e1) is an isomorphism of groups from(˜51,0(K),◦∫1,0) ∼−→
(Ad˜51,0(K)(e1),◦
∫1,0
Ad).
We have viewed Lie(˜Vω) as a subset of K⟨⟨e0∪µN⟩⟩and we can again view Lie(Ad˜Vω(e1)) as a subset
of K⟨⟨e0∪µN⟩⟩. The derivative of f↦→ f−1e1 f , the map f↦→[ e1, f] is the isomorphism of Lie algebras
deﬁned by Lie(˜Vω) ∼−→ Lie(Ad˜Vω(e1)).
Proposition A.1.1. The Lie bracket of Lie(Ad˜Vω(e1)) is{ f, g}Ad= d f(g)− dg( f) where d f is the
derivation sending e0↦→ 0, eξ↦→ f(ξ) for allξ∈µN(K).
Let the product.
∫1,0
Ad on Ad˜51,0(K)(e1) be deﬁned by(g−1e1g).
∫1,0
Ad( f−1e1 f)=(g f)−1e1(g f), and its
Lie version be[g, e1].
∫1,0
Ad[ f, e1]=[ g f, e1].
Then,{·,·} Ad is a Poisson bracket, namely, it satisﬁes{a.
∫1,0
Ad b, c}={ a, c}.
∫1,0
Ad b+ a.
∫1,0
Ad{b, c}.
Proof. Let us proceed as in the proof of Proposition 5.13 in [Deligne and Goncharov 2005]. We write
g= 1+ aϵ. When ϵ→ 0, we have(1+ aϵ)◦
∫1,0
Ad f= f+ϵdg( f)+ O(ϵ2). Thus, the action of Lie(Vω)
on Ad(˜51,0)(e1) by◦
∫1,0
Ad is by g↦→ dg. This map is injective. By the injectivity of d, we only have to
show that[d f, dg]= dd f(g)−dg( f). Since they are derivations, it is sufﬁcient to prove that these two maps
Pro-unipotent harmonic actions and dynamical properties of p -adic cyclotomic multiple zeta values 1745
agree on e1, and this follows directly from their deﬁnitions. The fact that it is a Poisson bracket follows
from the isomorphism of Lie algebras Lie(˜Vω) ∼−→ Lie(Ad˜Vω(e1)). □
Deﬁnition A.1.2. We call{·,·} Ad the adjoint Ihara bracket.
