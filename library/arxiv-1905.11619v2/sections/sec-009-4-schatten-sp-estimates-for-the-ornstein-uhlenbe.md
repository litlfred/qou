---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-009-4-schatten-sp-estimates-for-the-ornstein-uhlenbe
section_title: "Schatten Sp-estimates for the Ornstein-Uhlenbeck semi-group on q-Gaussians"
section_number: 4
pages: 10-11
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
toc_source: outline
---
We show that q-Gaussians Γq(HR) with the Ornstein-Uhlenbeck semi-group are gradient-Sp for
a range of q depending on p and the dimension of the Hilbert space HR.
4.1. q-Gaussian algebras. Let HR be a ﬁnite dimensional real Hilbert space with complexiﬁcation
H = HR ⊗C.
We denote by I the complex conjugation on H and we extend it to H⊗n by
I(v1 ⊗· · · ⊗vn) := Ivn ⊗· · · ⊗Iv1. Let q ∈(−1, 1) and consider the symmetrization operator on
H⊗n given by
P n
q (ξ1 ⊗. . . ⊗ξn) =
X
σ∈Sn
qi(σ)ξσ(1) ⊗. . . ⊗ξσ(n),
where i(σ) is the number of inversions in σ. Recall that an inversion is a pair (a, b) ∈{1, . . . , n}
with a < b and σ(a) > σ(b). For q ∈(−1, 1) we set new inner products on H⊗n by
⟨ξ, η⟩q = ⟨P n
q ξ, η⟩,
and we refer to the Hilbert space with this q-deformed inner product as H⊗n
q
. Also set the q-Fock
space Fq(H) = CΩ⊕(⊕∞
n=1H⊗n
q
), with Ωa unit vector called the vacuum vector. Note that the
conjugation I extends to an antiunitary operator on Fq(H); a typical permutation does not preserve
the q-deformed inner product, so it is a special feature of the permutation reversing the order. We
set the left creation operator for ξ ∈H,
lq(ξ)η1 ⊗. . . ⊗ηn = ξ ⊗η1 ⊗. . . ⊗ηn,
and the annihilation operator l∗
q(ξ) = lq(ξ)∗. These operators are bounded and extend to Fq(H)
for q ∈(−1, 1). We deﬁne the q-Gaussian algebra as
Γq := Γq(HR) := A′′
q,
Aq := ∗−alg{ lq(ξ) + lq(ξ)∗| ξ ∈HR}.
We let ϕΩbe the (tracial) vacuum state on Γq(HR) given by ϕΩ(x) = ⟨xΩ, Ω⟩. Ωis a separating
and cyclic vector for Γq(HR) and so ϕΩis faithful and Fq(H) is the standard Hilbert space of Γq.
In this setting Ωis a tracial vector and further Γq is a II1-factor [Ric05].
For vectors ξ1, . . . , ξn ∈H there exists a unique operator Wq(ξ1 ⊗. . . ⊗ξn) ∈Γq(HR) such that,
Wq(ξ1 ⊗. . . ⊗ξn)Ω= ξ1 ⊗. . . ⊗ξn.
We call these operators elementary Wick operators or elementary Wick words.
The
Ornstein-Uhlenbeck quantum Markov semi-group is then deﬁned by1
Φt(Wq(ξ1 ⊗. . . ⊗ξn)) = e−tnWq(ξ1 ⊗. . . ⊗ξn).
It comes with a generator (the quantum Dirichlet form) given by the number operator
∆(ξ1 ⊗. . . ⊗ξn) = nξ1 ⊗. . . ⊗ξn.
We determine the cohomology as follows.
1It extends to the q-Gaussian algebra by [BKS97, Theorem 2.11].
L2-COHOMOLOGY, DERIVATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS
11
Theorem 4.1. For any Aq-Aq-bimodule H we have Hn(Aq, H) = 0 for n ≥2.
Proof. Let e1, . . . , em be an orthonormal basis of HR. We claim that algebraically Aq is isomorphic
to the ∗-algebra of non-commutative polynomials in m self-adjoint variables X1, . . . Xm by the
identiﬁcation Xi := Wq(ei). Indeed, let P be a non-commutative polynomial and suppose that
P(X1, . . . , Xm) = 0. Let Q(X1, . . . , Xn) = Xi1 . . . Xid be a monomial occuring in P of highest
degree d. Then, from Lemma 4.3 below, we ﬁnd Q(X1, . . . , Xn) = Wq(Xi1 ⊗. . . ⊗Xid) + A where
A is a linear combination of Wick operators Wq(ξ1 ⊗. . . ⊗ξk) of tensors of order k < d.
If
P(X1, . . . , Xm) = 0 we must therefore have that Q(X1, . . . , Xm) = 0. By induction we conclude
that P = 0.
Now in [CaEi56, p. 192] it is shown that for the algebra of non-commutative polynomials, the
Hochschild cohomology with coeﬃcients in any bimodule is 0.
Alternatively, see [Kas04, Eqn.
(5.11)] for an explicit short exact projective resolution which also yields this result.
□
