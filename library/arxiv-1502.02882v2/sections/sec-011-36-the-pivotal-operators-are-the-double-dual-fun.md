---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-011-36-the-pivotal-operators-are-the-double-dual-fun
section_title: "The pivotal operators are the double dual functor"
section_number: 3.6
pages: 18-20
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
Our approach to the ‘double dual functor’ on a fusion categoryC been to encode
it in a canonical monoidal endofunctor T : C→ C, whose underlying functor
is simply the identity. The advantage of our approach is that it is canonical,
not requiring arbitrary choices of duals for objects. Such ﬁxed initial choices of
duals tend to complicate calculations, as the expression for ωV,W in equation
(23) below shows. We now connect our approach to the usual approach, taking
more care than is common in the literature.
We deﬁne a system of right duals on a fusion category C as a choice, for
every object V ∈ C, of a triple
(V∗, ηV : 1→V∗⊗V, ϵV :V⊗V∗→ 1)
which equips V∗ as a right dual of V . It is then a routine calculation to check
that this makes ∗ : C→ Cop into a well-deﬁned functor, which is equipped
with canonical isomorphisms V∗⊗W∗→ (W⊗V )∗ making it into a monoidal
functor. In particular, given such a choice of right duals, we have the associated
18
double dual monoidal endofunctor∗∗ of C, and the following explicit coherence
isomorphismsωV,W :V∗∗⊗W∗∗→ (V⊗W )∗∗, expressed graphically as follows:
ωV,W =
 (23)
Given any other system of right duals ∗′ on C, there is a unique monoidal
natural isomorphism ϑ :∗⇒∗ ′ such that ηV∗′ = (ϑ⊗ idV )◦ηV∗. Horizontally
composing ϑ with itself, we get a monoidal natural isomorphism θ :∗∗⇒∗ ′∗′.
Theorem 3.29. (i) Given any system of right duals ∗ on a fusion category
C, there is a canonical monoidal natural isomorphism β :T ⇒∗∗.
(ii) These isomorphisms are natural in the following sense: if ∗′ is another
system of right duals on C, then the diagram
V
V∗∗ V∗′∗′
β(∗)
V
β(∗′)
V
θV
commutes for all V ∈ C.
Proof. (i) We deﬁne βV by choosing a basis ei,α : Xi→ V for the hom-sets
Hom(Xi,V ) where i ranges over a representative set of simple objects, with
19
corresponding dual basis ˆei,α, and then setting
βV :=
∑
i,α
(24)
where we have used the partner convention on the Xi strands. It is easy to
check that this deﬁnition is independent of the basis choice ei,α, and that this
indeed deﬁnes a natural transformation β :T ⇒∗∗ of the underlying functors.
Forβ to be monoidal, we need to verify that the following coherence diagram
commutes:
V⊗W V⊗W
(V⊗W )∗∗ V∗∗⊗W∗∗
TV,W
βV⊗βW
ωV,W
βV⊗W
(25)
Substitute the deﬁnition (23) of ωV,W and the deﬁnition (24) of βV into the
equation (25). The left and right hand sides simplify considerably. It is suﬃcient
to check the remaining identity on the representative simple objects V = Xk,
W =Xl, where it is an elementary string diagram veriﬁcation, best performed
in a pivotal basis. The diagram for part (ii) is simpler and can be veriﬁed
directly.
Combining this with Theorem 3.28, which says thatT 2 = id, we immediately
obtain the following.
Corollary 3.30 (cf. [9, Thm 2.6]) . For any system of right duals ∗ on a fusion
category C, there is a canonical monoidal natural isomorphism id⇒∗∗∗∗ , which
is natural with respect to the choice of system of right duals ∗.
