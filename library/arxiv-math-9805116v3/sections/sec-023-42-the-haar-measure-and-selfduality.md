---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-023-42-the-haar-measure-and-selfduality
section_title: "The Haar measure and selfduality"
section_number: 4.2
pages: 33-35
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Recall that the Haar measure in a WHA A has been deﬁned in Deﬁnition 3.24 as the unique
elementh ∈A making the integral
∫
ϕ := ⟨ϕ, h⟩of a function ϕ:A → |C to be a non-degenerate
functional invariant under left and right translations and normalized according to
∫
ϕL = ˆε(ϕL)
for ϕL ∈ ˆAL. The suﬃcient conditions for its existence given by Theorem 3.27 will be used
here to prove the next Theorem.
Theorem 4.5 In a C ∗-WHA A Haar measure h ∈ A exists. It is selfadjoint, h∗ = h, and
such that
(ϕ,ψ ) := ⟨ϕ∗ψ, h⟩, ϕ,ψ ∈ ˆA , (4.10)
is a scalar product on ˆA making ˆA a Hilbert space and making the left regular module ˆA
ˆA a
faithful ∗-representation of the ∗-WHA ˆA. Thus ˆA is a C ∗-WHA, too.
Proof: A being a ﬁnite dimensional C ∗-algebra is semisimple. By Proposition 4.4 there exists
ag implementingS2. This g was shown to be positive and invertible, hence tr Dr(g−1)> 0 for
all r ∈ SecA. Therefore all the conditions of Theorem 3.27 are satisﬁed a nd Haar measure h
exists.
Since h is non-degenerate, ( , ) is a non-degenerate sesquilinear form on ˆA. So it remains
to show positivity. By the equality
(ψ,ψ ) = ⟨ψ∗ψ, h⟩= ⟨ψ,S (h(1))∗⟩ ⟨ψ,h (2)⟩ (4.11)
positivity of ( , ) follows if we can show that ( S ⊗ id ) ◦ ∆( h) belongs to the positive cone
P =
{ ∑
k
a∗
k ⊗ak | ak ∈A
}
⊂A ⊗A . (4.12)
Therefore the next Lemma will complete the proof. Q.e.d.
33
Lemma 4.6 Choose matrix units {eαβ
q } for A and let g denote the element determined in
Proposition 4.4. If furthermore ∑
ixi ⊗yi is the quasibasis of the trace τ :A → |C with trace
vectorτq = trq(g−1) then
S(h(1)) ⊗h(2) =
∑
i
xi ⊗g−1yi =
∑
q∈SecA
1
τq
∑
αβ
eαβ
q g−1/2 ⊗g−1/2eβα
q (4.13)
h(1) ⊗S(h(2)) =
∑
i
xig ⊗yi =
∑
q∈SecA
1
τq
∑
αβ
eαβ
q g1/2 ⊗g1/2eβα
q (4.14)
Proof: The quasibasis of χ = g⇀τ is ∑ xig−1 ⊗yi and since χ is the dual left integral of
h, this quasibasis is equal to h(2) ⊗S−1(h(1)). This implies the ﬁrst row. By property iii)
of Proposition 4.4 τ is an S-invariant trace, therefore its quasibasis can also be writ ten as∑
iyi ⊗xi =∑
iS−1(xi) ⊗S−1(yi). Thus the second row follows from the ﬁrst. Q.e.d.
From now on h ∈A will always denote the Haar measure of A and ˆh ∈ ˆA that of ˆA.
Lemma 4.7 In a C ∗-WHA A the counit is a positive linear functional, ε(x∗x) ≥ 0, x ∈A.
Proof:
ε(x∗x) = ε(x∗1(1))ε(1(2)1(2′))ε(1(1′ )x) = ε(⊓L(x)∗ ⊓L (x)) = ⟨ˆh, ⊓L(x)∗ ⊓L (x)⟩ ≥ 0,
where we have used ˆh|AL = ε|AL, which follows from ⟨ˆh, xL⟩= ⟨ˆ⊓L(ˆh), xL⟩= ⟨ˆ1, xL⟩ for all
xL ∈AL. Q.e.d.
A being semisimple the trivial representation Vε decomposes into irreducibles Vq each of
them with multiplicity 1 by Proposition 2.15. The sectors q ∈ S ecA occuring in Vε with
non-zero multiplicity will be called vacuum sectors.
Vε ∼=
⨁
q∈VacA
Vq . (4.15)
By Proposition 2.15 there is a bijection q ↦→zL
q from the set VacA of vacuum sectors to the
set of minimal projections in ZL such that, with zR
q :=S(zL
q ), we have
Dε(zL
q ) = Dε(eq) = Dε(zR
q ) (4.16)
zL
q = ⊓L(eq) ⊓R(eq) = zR
q (4.17)
where eq denotes the minimal central projection in A supporting the irreducible vacuum rep-
resentationDq.
Lemma 4.8 Dr(h) is a 1-dimensional projection for r ∈ VacA and Dr(h) = 0 if r is not a
vacuum sector. The algebra of 2-sided integrals is generate d by minimal projections hq
I(A) = hAh = Span {hq |q ∈ VacA }, h q =heq . (4.18)
The non-degenerate 2-sided integrals are presisely the inv ertible elements: I∗(A) = I(A)×.
Proof: If Dr(h) ⁄= 0 then pick up a non-zero vector vr from the subspace Dr(h)Vr of the
irreducible A-module Vr and deﬁne
T :AL →Vr , Tx L :=Dr(xL)vr . (4.19)
34
This map is a non-zero left A-module map if we equip AL with the structure of the trivial
A-module AAL introduced in Lemma 2.12. Indeed,
Dr(x)TxL =Dr(xxLh)vr =Dr(⊓L(xxL)h)vr =T ⊓L (xxL) . (4.20)
Therefore r ∈ VacA. This proves that Dr(h) = 0 for r ⁄∈ VacA.
Now let the Haar integral act on the trivial left A-module A ˆAR.
Dε(h)ϕR = h⇀ϕR ∈ ˆAL ∩ ˆAR ≡ ˆZ . (4.21)
Thus Dε(h): ˆAR → ˆZ is a projection, onto. If zL is a minimal projection in ZL then zL⇀ ˆ1
is a minimal projection in ˆZ by Lemma 2.14. Hence Dε(zLh) maps ˆAR onto (zL⇀ ˆ1) ˆZ ∼= |C.
This proves that Dε(zLh), the restriction of which is precisely Dq(h) for some q ∈ VacA, is a
1-dimensional projection. If i ∈ I then by the 2-sided normalization of h one can write i =hih.
Conversely,hxh is a 2-sided integral for all x ∈A. This proves the remaining assertions. Q.e.d.
The Haar measure provides conditional expectations
EL:A →AL, E L(x) = ˆh⇀x (4.22)
ER:A →AR, E R(x) = x↼ ˆh (4.23)
As a matter of fact by Lemma 3.2.c) the image of EL is in AL since ˆh is a left integral. EL
is unit preserving since ˆh is normalized. Finally, EL is positive since ˆh is positive and ∆ is a
∗-algebra map.
