---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-015-23-twisted-bimodules
section_title: "Twisted (bi)modules"
section_number: 2.3
pages: 6-8
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — W e show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼= ν A1[d]."
---
one-sided modules, as follows. Let A be an algebra and let M be an A-bimodule.
For every pair of algebra automorphisms σ, τ of A, we write σM τ for the A-bimodule
deﬁned by
a · m · b = σ(a)mτ (b)
for all a, b ∈ A and all m ∈ M . When one or the other of σ, τ is the identity map we
shall simply omit it, writing for example σM for σM 1. If φ is another automorphism
of A, then the map x ↦→φ(x) for all x ∈ A deﬁnes an isomorphism of A-bimodules
σAτ → φσAφτ . In particular,
σAτ ∼= Aσ−1τ ∼= τ −1σA(2.3.1)
NOETHERIAN HOPF ALGEBRAS 7
as A-bimodules. If τ is an inner automorphism of A, given by conjugation x ↦→
uxu−1 by the unit u of A, then the map on A given by left multiplication by u
shows that
σAβ ∼= τ σAβ ∼= σAβτ(2.3.2)
for all automorphisms σ and β of A.
Let M be an A-bimodule. Deﬁne
ZM (A) := {a ∈ A : am = ma ∀ m ∈ M }.
Then ZM (A) is a subalgebra of A. For any algebra automorphism σ, write
Z σ
A(M ) = {m ∈ M | am = mσ(a) ∀ a ∈ A},
so Z σ(M ) is a ZM (A)-submodule of M . When M = A, Z σ(M ) is the space of
σ−1-normal elements of A. We write Z(M ) for Z idA(M ); of course Z(A) = ZA(A)
is just the centre of A, and Z σ(A) is a Z(A)-module. We shall denote by N (A)
the multiplicative subsemigroup of Aut k-alg(A) consisting of those automorphisms
σ such that A contains a σ-normal element which is not a zero divisor.
Lemma. Let A be an algebra and let M be an A-bimodule.
(a) Under the canonical identiﬁcation of M with M σ as k-vector spaces,
Z σ
A(M ) = Z(M σ).
(b) Let σ and τ be algebra automorphisms of A. Then τ carries Z(Aστ ) to
Z(Aτ σ).
(c) Suppose that A is a Hopf algebra. If σ is a Hopf algebra automorphism of
A, then σ(L(M )) ∼= L(σM σ). In particular,
σ(L(τ A)) ∼= L(στ Aσ) ∼= L(τ A).
Proof. (a) is simply the deﬁnition.
(b) By (a) we may regard Z(Aστ ) and Z(Aτ σ) as subsets of A. For every
x ∈ Z(Aστ ), ax = xστ (a) for all a ∈ A. Then, for all a ∈ A,
aτ (x) = τ (τ −1(a)x) = τ (xστ τ−1(a)) = τ (x)τ σ(a).
This means that τ : Z(Aστ ) − →Z(Aτ σ) is an isomorphism.
(c) The second assertion is a special case of the ﬁrst, so we consid er the ﬁrst
one only. Let ∗, · and • be the left action of A on σ(L(M )), L(M ) and L(σM σ)
respectively. For every a ∈ A and m ∈ M ,
a ∗ m = σ(a) · m =
∑
σ(a)1mS(σ(a)2) =: ( ∗).
Let ·σ be the action of A on σM σ. Since σ commutes with product, coproduct and
antipode, then we continue
(∗) =
∑
σ(a1)mσ(S(a2)) =
∑
a1 ·σ m ·σ S(a2) = a • m.
□
8 K.A. BROWN AND J.J. ZHANG
