---
doc_id: arxiv-math-0006057v2
doc_title: "Finite Quantum Groupoids and Their Applications"
section_id: sec-011-012-module-and-comodule-algebras
section_title: "Module and comodule algebras"
section_number: 0.12
pages: 13-14
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
toc_source: inferred
doc_brief: "Finite Quantum Groupoids and Their Applications — We give a survey of the theory of ﬁnite quantum groupoids (weak Hopf algebras), including foundations of the theory and applications to ﬁnite depth"
---
1) h · ab = (h(1) · a)(h(2) · b),
2) h · 1 = εt(h) · 1.
If A is an H-module algebra we will also say that H acts on A.
1) ρ(ab) = a(0)b(0) ⊗a(1)b(1),
2) ρ(1) = (id ⊗εt)ρ(1).
and the unit of A#H is 1#1.
Proof. (i) ⇒(ii) : Suppose that H is semisimple, then since Ker εt is a left ideal
in H we have Ker εt = Hp for some idempotent p. Therefore, Ker εt(1 −p) = 0
and l = 1 −p is a left integral by Lemma 3.1.3(iv). It is normalized since εt(l) =
1 −εt(p) = 1. (ii) ⇒(iii) : if l is normalized then l(1) ⊗S(l(2)) is a separability
element of H by Lemma 3.1.3(ii). (iii) ⇒(i) : this is a standard result [P].
e∈G0
1
|e|le is a nor-
malized integral in kG.
Given a left integral l, one can show ([BNSz], 3.18) that if there exists λ ∈bH
such that λ ⇀l = 1, then it is unique, it is a left integral in bH and l ⇀λ = b1.
Such a pair (l, λ) is called a dual pair of left integrals. One deﬁnes dual pairs of
right integrals in a similar way.
Deﬁnition 4.1.1. An algebra A is a (left) H-module algebra if A is a left H-module
via h ⊗a →h · a and
Deﬁnition 4.1.2. An algebra A is a (right) H-comodule algebra if A is a right
H-module via ρ : a →a(0) ⊗a(1) and
It follows immediately that A is a left H-module algebra if and only if A is a
right bH-comodule algebra.
Example 4.1.3.
(i) The target counital subalgebra Ht is a trivial H-module
algebra via h · z = εt(hz), h ∈H, z ∈Ht.
(ii) H is an bH-module algebra via the dual action φ ⇀h = h(1)⟨φ, h(2) ⟩, φ ∈
bH, h ∈H.
(iii) Let A = CH(Hs) = {a ∈H | ay = ya
∀y ∈Hs}, be the centralizer of Hs in
H, then A is an H-module algebra via the adjoint action h · a = h(1)aS(h(2)).
4.2. Smash products. Let A be an H-module algebra, then a smash product
algebra A#H is deﬁned on a k-vector space A ⊗Ht H, where H is a left Ht-module
via multiplication and A is a right Ht-module via
a · z = S−1(z) · a = a(z · 1),
a ∈A, z ∈Ht,
as follows. Let a#h be the class of a ⊗h in A ⊗Ht H, then the multiplication in
A#H is given by the familiar formula
(a#h)(b#g) = a(h(1)#b)#h(2)g,
a, b, ∈A, h, g ∈H,
14
DMITRI NIKSHYCH AND LEONID VAINERMAN
Example 4.2.1. H is isomorphic to the trivial smash product algebra Ht#H.
