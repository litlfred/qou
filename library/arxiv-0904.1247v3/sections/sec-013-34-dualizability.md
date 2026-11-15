---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-013-34-dualizability
section_title: "Dualizability"
section_number: 3.4
pages: 25-27
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
rigid categories as objects in the symmetric monoidal (∞, 2)-category Alg(1)(StC), the Morita 2-
category of monoidal categories [L3, Section 4.1]. This interpretation will not require any technical
notions of (∞, 2)-category theory — we recall the notion of 2-dualizability as it specializes in our
setting to speciﬁc identities formulated for monoidal ∞-categories.
A Morita morphism between two (stable presentable) monoidal ∞-categories A, B is an Aop ⊗B-
module category. The evaluation and coevaluation Morita morphisms for a monoidal category A
are the Morita morphisms
VectC
A
/ A ⊗Aop
A
/ VectC
25
given by the object A itself in an obvious way.
Deﬁnition 3.15. (1) [L3, Proposition 4.2.3] A 2-dualizable object of Alg(1)(StC) is a monoidal
category A such that the evaluation Morita morphism evA : A ⊗Aop →S has both a right and a left
adjoint.
(2) [L3, Deﬁnition 4.2.6] A Calabi-Yau structure on a monoidal category A ∈Alg(1)(StC) is an
S1-invariant functional Tr(A) = A⊗A⊗Aop A →S which is the counit of an adjunction between evA
and coevA.
In this deﬁnition, an adjoint for a Morita morphism is given by a (left or right) dual Morita
morphism (as in Remark 2.8) together with unit and counit morphisms satisfying the standard
identities.
The S1 = SO(2) action on Tr(A) is an ∞-categorical version of the Connes cyclic
structure on Hochschild homology, and is provided by the one-dimensional Cobordism Hypothesis,
thanks to the identiﬁcation of Tr(A) with the dimension of the dualizable object A in the underlying
Morita (∞, 1)-category. It can be described explicitly via topological chiral homology, see the proof
of Theorem 6.3.
We will also need a natural weakening of the notion of Calabi-Yau structure.
Namely, a 2-
dualizable monoidal category A admits a canonical automorphism SA, the Serre automorphism,
with the property
evR
A = (SA ⊗idAop) ◦coevA
(see [L3, Proposition 4.2.3]). It can be interpreted as a monodromy of the object A around the
SO(2)-action, i.e., the ﬁrst obstruction to SO(2)-invariance of A, or as encoding the action of the
free group on the circle ΩS2 = ΩΣSO(2) on A.
Deﬁnition 3.16. A weakly Calabi-Yau monoidal category is a 2-dualizable monoidal category with
a trivialization of the Serre automorphism SA ≃idA, i.e., an isomorphism of A-bimodules SA ≃A.
Given such a trivialization, one can deﬁne a trace functional
A
tr
/
τ
)❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
Tr(A) ≃evA ◦coevA ≃evA ◦evR
A

VectC
with the vertical map the counit of the adjunction. A Calabi-Yau structure is then a factorization
of this trace through the ﬁxed points of S1 on Tr(A).
The notion of 2-dualizability reproduces the two senses of duality for A as an Ae-module appearing
in Deﬁnition 2.7.
Lemma 3.17. (1) A monoidal category A is Ae-dualizable if and only if the evaluation Morita
morphism evA : Ae →VectC admits a left adjoint. In this case, the left adjoint is given by the
bimodule dual A! ∈Ae -mod.
(2) A monoidal category A is StC-dualizable if and only if the evaluation Morita morphism
evA : Ae →VectC admits a colimit-preserving right adjoint. In this case, the right adjoint is given
by the StC-dual A′ ∈Ae -mod.
(3) The Serre automorphism SA of a 2-dualizable category A is represented (as Morita endomor-
phism of A) by the A-bimodule A′.
Proof. The assertions are immediate from the deﬁnitions. The bimodule giving the left adjoint is the
bimodule dual A!. The bimodule giving the right adjoint is the plain dual A′. Hence the discrepancy
SA between the right adjoint and the coevaluation VectCAAe is also given by the bimodule A′.
□
Now our prior results admit the following reinterpretation.
Theorem 3.18. Let A ∈Alg(StC) be a semi-rigid category. Then A is 2-dualizable.
A pivotal structure on A gives rise to a weak Calabi-Yau structure on A.
26
Proof. Proposition 2.6 and Lemma 2.9 imply A is StC-dualizable. Proposition 3.14 implies A is Ae-
dualizable, with Ae and S-dual identiﬁed. Hence Lemma 3.17 implies A is fully dualizable. Moreover
a pivotal structure on A is equivalent to a particular identiﬁcation SA = A′ ≃A of bimodules, as
required to make A weakly Calabi-Yau.
□
