---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-013-21-restriction-via
section_title: "Restriction via"
section_number: 2.1
pages: 5-6
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
coproduct. Then we may view A as a subalgebra of the algebra A⊗A via ∆. Deﬁne
a functor
ResA : ( A ⊗ A) − Mod → A − Mod
by restriction of the scalars via ∆, so that Res A is equivalent to the functor
HomA⊗A(A⊗A(A ⊗ A)A, −).
Lemma. Let A be a Hopf algebra and B be any algebra.
(a) ResA is an exact functor.
(b) Let N be an A ⊗ Bop-module. Then ResA(A ⊗ N ) with restriction of Bop-
module from N is isomorphic to AA ⊗ kNB as A ⊗ Bop-modules where the
left A-module on kNB is trivial. The isomorphism from ResA(A ⊗ N ) to
AA ⊗ kNB is given by
a ⊗ n ↦→
∑
a1 ⊗ S(a2)n,
where ∆( a) = ∑ a1 ⊗ a2, with inverse a′ ⊗ n′ ↦→∑ a′
1 ⊗ a′
2n′.
(c) ResA preserves freeness. Similarly, A ⊗ A is a free right A-module via the
coproduct ∆ .
(d) ResA preserves projectivity.
(e) ResA preserves injectivity.
6 K.A. BROWN AND J.J. ZHANG
Proof. (a) This is clear.
(b) By the left-module version of the fundamental theorem of Hop f modules [Mo,
Theorem 1.9.4] A ⊗ N is free over A with basis given by a k-basis of N , because N
is the space of coinvariants of the left A-comodule A ⊗ N . It’s easy to verify that
the isomorphism given in the proof of [Mo, Theorem 1.9.4] has the desir ed form,
and that it preserves the Bop-module action.
(c) This follows from (b) and its right-hand analogue, with N = A.
(d) This is true because Res A(A ⊗ A) is free by (c).
(e) Let M be an injective A ⊗ A-module. Then
HomA(−, ResA(M )) ∼= HomA(−, HomA⊗A(A⊗A(A ⊗ A)A, M)) =: ( ∗)
By the Hom −⊗ adjunction
(∗) ∼= HomA⊗A(A⊗A(A ⊗ A)A ⊗A −, M) =: ( ∗∗).
By (c) ( A ⊗ A)A is free, hence ﬂat. Since M is A ⊗ A-injective, the functor ( ∗∗) is
exact. Hence Res A(M ) is A-injective. □
