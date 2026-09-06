---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-014-213-then
section_title: "Then"
section_number: 2.13
pages: 12-14
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
B(x⇀ϕR) = 1 ↼ (x⇀ϕR) = ⟨1(1)x,ϕR⟩1(2) =
= ⟨1(1)(x↼ϕR), ˆ1⟩1(2) = ⊓L(x↼ϕR) = ⊓L(x(1↼ϕR)) =
= ⊓L(xB(ϕR))
hence B is a left A-module map. Here, in the last-but-one equality we have used one of the
four arrow identities of Scholium 2.7. Q.e.d.
Deﬁnition 2.13 By the trivial representation of the WHA A we mean the cyclic left A-module
Vε := A ˆAR with A-action Dε:A → EndK ˆAR, Dε(x)ϕ :=x⇀ϕ .
The third and fourth A-modules of the above Lemma demonstrate that the restrictio n of the
trivial representation to AL (AR) is equivalent to its left regular representation, hence fa ithful.
This is one of the instances where AL/R appears in the role of a ground ”ﬁeld”.
Later we will need the following strengthening of Lemma 2.6.
12
Lemma 2.14 Let A be a WHA and introduce the notation ZL := AL ∩ CenterA, ZR :=
AR ∩ CenterA, and Z :=AL ∩AR. Then the isomorphism (of algebras) κL
A:AL → ˆAR restricts
to an isomorphism ZL → ˆZ and the isomorphism κR
A:AR → ˆAL restricts to the isomorphism
ZR → ˆZ. Therefore
ZL⇀ ˆ1 = ˆZ = ˆ1↼ZR
Z⇀ ˆ1 = ˆZR, ˆZL = ˆ1↼Z .
The two isomorphisms have a common restriction to the hypercenter HypercenterA :=ZL ∩ZR
and yields an isomorphism Hypercenter A → Hypercenter ˆA.
Proof: Notice that for c ∈ CenterA ˆ1↼c =c⇀ ˆ1. Therefore xL ∈ZL ⇒xL⇀ ˆ1 = ˆ1↼xL ∈ ˆZ.
This proves κL
A(ZL) ⊂ ˆZ.
Ifz ∈Z then (z⇀ ˆ1)ϕ =z⇀ϕ by (2.20a) and z⇀ϕ =ϕ(z⇀ ˆ1) by (2.21b). Hence z⇀ ˆ1 is
central. This proves κL
A(Z) ⊂ ˆZR.
Since (κL
A)−1 = κR
ˆA, the analogue inclusions κR
A(ZR) ⊂ ˆZ and κR
A(Z) ⊂ ˆZL complete the
proof. Q.e.d.
The unusual feature of the trivial representation of WHA-s i s that it can be decomposable.
But this can occur only if the left and right subalgebras of th e dual have non-trivial intersection
as the next Proposition claims.
Proposition 2.15 LetA be a WHA, let (Vε,Dε) be its trivial representation as in Deﬁnition
2.13. Then
EndVε = Dε(ZL) = Dε(ZR) , (2.32)
where EndVε denotes the algebra of A-module endomorphisms of Vε.
Proof: Let T ∈ EndVε then T (x⇀ ˆ1) = x⇀T (ˆ1), for x ∈A, in particular
T (xL⇀ ˆ1) = xL⇀T (ˆ1) = ( xL⇀ ˆ1)T (ˆ1)
T (xL⇀ ˆ1) = T (S−1(xL)⇀ ˆ1) = S−1(xL)⇀T (ˆ1) = T (ˆ1)(xL⇀ ˆ1)
where we have made use of Eqns (2.20a) and (2.21b). Since by Le mma 2.6 AL⇀ ˆ1 = ˆAR,
ζ := T (ˆ1) ∈ Center ˆAR and T (ϕR) = ϕζ. Thus x⇀ζ = T (x⇀ ˆ1) = ( x⇀ ˆ1)ζ holds for all
x ∈A. It follows that
⟨ˆ⊓L(ζ),x ⟩= ⟨ζ, 1↼ (x⇀ ˆ1)⟩= ⟨(x⇀ ˆ1)ζ, 1⟩= ⟨x⇀ζ, 1⟩= ⟨ζ,x ⟩,
i.e. ζ ∈ ˆAL ∩ ˆAR ≡ ˆZ. Now by Lemma 2.14 there exists a zL ∈ZL such that ζ =zL⇀ ˆ1. We
can conclude that
T (ϕR) = ζϕR = (zL⇀ ˆ1)ϕR =zL⇀ϕR =Dε(zL)ϕR ,
i.e. T = Dε(zL). This proves End Vε ⊂ Dε(ZL). The opposite inclusion is trivial since
Dε(ZL) ⊂ Center (Dε(A)). This ﬁnishes the proof of End Vε =Dε(ZL).
Showing the other statement End Vε =Dε(ZR) one proceeds as above but chooses a zR ∈
ZR such that ζ = ˆ1↼zR. Then
T (ϕR) = ϕR(ˆ1↼zR) = ϕR(zR⇀ ˆ1) = zR⇀ϕR =
= Dε(zR)ϕR
completes the proof. Q.e.d.
Notice that the above Proposition does not imply that the tri vialA-module is semisimple. It
does imply, however, that Vε has a decomposition Vε ∼= ⊕νVν into indecomposable A-modules
in which the indecomposables are disjoint, i.e. Hom ( Vµ,Vν ) = 0 for all µ ⁄=ν.
13
Deﬁnition 2.16 If ZL = K1, or equivalently, if the trivial representation is indecom posable
then the WHA is called pure.
The name ”pure” comes from the C ∗-setting when the trivial representation arises from the
positive linear functional ε by the GNS construction. Thus A is pure iﬀ ε is pure.
Nota bene pureness is not a selfdual notion, duals of pure WHA -s may not be pure. Clearly,
A is pure iﬀ ZL ∼=ZR is trivial but ˆA is pure iﬀ Z is trivial.
