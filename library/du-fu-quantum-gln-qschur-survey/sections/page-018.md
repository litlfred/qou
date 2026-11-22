---
doc_id: du-fu-quantum-gln-qschur-survey
doc_title: "QUANTUM gln, q-SCHUR ALGEBRAS AND THEIR"
section_id: page-018
section_title: "Page 18"
section_number: null
pages: 18-18
source_pdf: du-fu-quantum-gln-qschur-survey.pdf
source_sha256: 6852134eaffb3137
toc_source: undetermined
doc_brief: "Quantum gl_n, q-Schur algebras and their infinite/infinitesimal counterparts — We present a survey of recent developments of the Beilinson–Lusztig–MacPherson approach in the study of quantum gln"
---
18
JIE DU AND QIANG FU
Theorem 9.4 ([7, 7.4]). The map ζr : U(∞) →EndH(Ω⊗r
∞) factors through ¯ζr : V(∞, r) →
EndH(Ω⊗r
∞). In other words, we have ζr = ¯ζr ◦ξr. Hence, U(∞, r) = V(∞, r).
Remark 9.5. (1) The injective map ¯ζr : bK(∞, r) →EndH(Ω⊗r
∞) is not surjective; see [7,
Thm 7.4]. Thus, unlike the (ﬁnite) q-Schur algebra case, the homomorphism ζr from U(∞)
to the inﬁnite q-Schur algebra S(∞, r) is not surjective, i. e., the algebra U(∞, r) is a proper
subalgebra of S(∞, r).
(2) It can be proved (see [7, §8]) that the epimorphism ζr : U(∞) →U(∞, r) can be
extended to an algebra epimorphism ˆζr : bK(∞) →bK(∞, r) by sending P
A∈eΞ(∞) βA[A] to
P
A∈Ξ(∞,r) βA[A]. Thus, we obtain an algebra homomorphism ζr : bK(∞) →EndH(Ω⊗r
∞).
(3) It is possible to introduce a new algebra bK
†(∞) which has the inﬁnite q-Schur algebra as
a homomorphic image. Let bK
†(∞) be the vector space of all formal (possibly inﬁnite) Q(v)-
linear combinations P
A∈eΞ(∞) βA[A] which have the following properties: for any x ∈Z∞,
(9.5.1)
the set {A ∈eΞ(∞) | βA̸ = 0, col (A) = x} is ﬁnite.
In other words, for any µ ∈Zn, the sum P
A∈eΞ(∞) βA[A] · [diag(µ)] is ﬁnite. We can deﬁne
the product of two elements P
A∈eΞ(∞) βA[A], P
B∈eΞ(∞) γB[B] in bK
†(∞) to be P
A,B βAγB[A]·
[B]. This deﬁnes an associative algebra structure on bK
†(∞). This algebra has an identity
element P
λ∈Z∞[diag(λ)]: the sum of all [D] with D a diagonal matrix in eΞ(∞). One proves
that the map ζ†
r : bK
†(∞) →EndH(Ω⊗r
∞) sending P
A∈eΞ(∞) βA[A] to P
A∈Ξ(∞,r) βA[A] is an
epimorphism; see [7, 8.9].
10. Highest weight representations of U(∞)
In this section, we discuss the “standard” representation theory of U(∞). This includes
the category C of weight modules, the category Chi of weight modules with highest weights,
the category Cint of integrable modules and the category O, all of which are full subcategories
of the category U(∞)-Mod of U(∞)-modules.
Let X(∞) = {λ = (λi)i∈Z | λi ∈Z} be the weight lattice, and let
X+(∞) = {λ ∈X(∞) | λi ⩾λi+1 for all i ∈Z}
be the set of dominant weights. For i ∈Z, let as before ei = (· · · , 0, 1
i, 0 · · · ) and αi = ei −
ei+1. Then R(∞) = {ei−ej | i̸ = j} is the root system of gl∞, and R+(∞) = {ei−ej | i < j}
is the associated positive system. Let Π(∞) = {αi | i ∈Z} be the set of all simple roots,
and let ⩽be the partial ordering on X(∞) deﬁned by setting, for all λ, µ ∈X(∞), µ ⩽λ if
λ −µ ∈NΠ(∞).
For a U(∞)-module M and λ ∈X(∞), let Mλ = {x ∈M | Kix = υλix for i ∈Z}. If
Mλ̸ = 0, then λ is called a weight of M and Mλ is called a weight space; if M = ⊕λ∈X(∞)Mλ,
then M is called a weight module.
Let wt(M) = {λ ∈X(∞) | Mλ̸ = 0} denote the set of the weights of M. It is clear that,
for a U(∞)-module M and i ∈Z, we have
(10.0.2)
EiMλ ⊆Mλ+αi
and
FiMλ ⊆Mλ−αi.
