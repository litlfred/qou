---
doc_id: arxiv-1905.11619v2
doc_title: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS"
section_id: sec-008-33-the-haagerup-averaging-technique
section_title: "The Haagerup averaging technique"
section_number: 3.3
pages: 9-11
source_pdf: 1905.11619v2.pdf
source_sha256: f634f9ec4357d5f3
doc_brief: "L2-COHOMOLOGY, DERIVATIONS AND QUANTUM MARKOV SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS — We study (quasi-)cohomological properties through an anal ysis of quantum Markov semi-groups."
---
Sp properties behave well under Haagerup averaging technique s. We believe this result is of inde-
pendent interest, though we will not use it in the subsequent sections.
Let Λ be a discrete group with group algebra C[Λ] and von Neumann algebra ( L(Λ) , τ). We will
identify Λ with its image under the left regular representat ion. So for γ∈ Λ we will also write γ for
the associated unitary in L(Λ). Let (Φ t)t≥0 be a quantum Markov semi-group on L(Λ). Consider
the map,
(3.5) Ψ t = E◦ (Φ t⊗ id)◦ δΛ
where δΛ :L(Λ) →L (Λ)⊗L(Λ) is the comultiplication δΛ : γ↦→γ⊗ γ and E is the conditional
expectation of L(Λ)⊗L(Λ) onto the image of δΛ (post-composed with the inverse of δΛ so that
the range is contained in L(Λ)). Then Ψ t is a completely positive Fourier multiplier with symbol
ϕt(γ) = τ (Φ t(γ)γ−1), γ∈ Γ.
Lemma 3.13. Let Ψ t :L(Λ) →L (Λ) , t≥ 0 be unital completely positive Fourier multipliers (not
necessarily a semi-group) and suppose that for every γ∈ Λ the limit ∆ Ψ
0 (γ) := lim tց0 1
t (γ− Ψ t(γ))
exists. Then ∆ Ψ
0 deﬁnes a preclosed (unbounded) operator on ℓ2(Γ) with closure ∆ Ψ . Moreover,
exp(−t∆ Ψ ) is a quantum Markov semi-group.
Proof. Since ∆ Ψ
0 acts diagonally on ℓ2(Λ) with respect to the basis γ ∈ Λ it is preclosed. The
remaining statements follow by following the construction s in [Jol04] and [CaSk15, Proposition 5.5].
Alternatively, there is the following short proof. Let ϕt be the symbol of the Fourier multiplier Ψ t
which is positive deﬁnite and ϕt(e) = 1. Consider the state µt on C[Λ] that maps γ∈ Λ to ϕt(γ).
Then ∆ 0(γ) := lim tց0 1
t (µt− ε) deﬁnes a generating functional on C[Λ] where ε(γ) = 1 , γ∈ Λ
is the counit (see [DFSW16, Section 6.2] for generating func tionals). Therefore νt := exp(−t∆ 0)
deﬁnes a convolution semi-group of states on C[Λ]. Since the Fourier multiplier Ψ t = (id⊗ νt)◦ δΛ
is a trace preserving ucp map it extends from C[Λ] to a quantum Markov semi-group on L(Λ) with
generator ∆ Ψ . □
Lemma 3.14. Let (Φ t)t≥0 be a quantum Markov semi-group on L(Γ) with generator ∆ and assume
C[Γ] is in the domain of ∆ . Consider Ψ t as in (3.5) and let ∆ Ψ be as in Lemma 3.13. We have,
∆ Ψ (γ) = d
dt|t=0⟨Φ t(γ), γ⟩γ =⟨∆( γ), γ⟩γ, γ ∈ Γ⊆ C[Γ] .
Proof. This is clear from the deﬁnitions. □
The following theorem shows that under a domain condition on ∆ we may average a quantum
Markov semi-group to a semi-group of Fourier multipliers wh ile retaining the property of being
gradient-Sp.
Theorem 3.15. Let (Φ t)t≥0 be a quantum Markov semi-group on L(Γ) with generator ∆ and
assume C[Γ] is in the domain of ∆ . If (Φ t)t≥0 is gradient-Sp then so is exp(−t∆ Ψ ).
Proof. Take µ1, µ2∈ Γ ﬁxed. Since (Φ t)t≥0 is gradient-Sp we have that the assignment
Ψ µ 1,µ 2 : γ↦→∆( µ1γµ2) + µ1∆( γ)µ2− µ1∆( γµ2)− ∆( µ1γ)µ2
is inSp as an operator on ℓ2(Γ). Therefore, also
µ−1
1 Ψ µ 1,µ 2(· )µ−1
2 : γ↦→µ−1
1 ∆( µ1γµ2)µ−1
2 + ∆( γ)− ∆( γµ2)µ−1
2 − µ−1
1 ∆( µ1γ)
10 MARTIJN CASPERS, YUSUKE ISONO, AND MATEUSZ W ASILEWSKI
is inSp. Let D be the conditional expectation of B(ℓ2(Γ)) onto the diagonal operators in B(ℓ2(Γ)).
Certainly D(µ−1
1 Ψ µ 1,µ 2(· )µ−1
2 ) is in Sp and, further,
D(µ−1
1 Ψ µ 1,µ 2(· )µ−1
2 )(γ) = µ−1
1 ∆ Ψ (µ1γµ2)µ−1
2 + ∆ Ψ (γ)− ∆ Ψ (γµ2)µ−1
2 − µ−1
1 ∆ Ψ (µ1γ).
Multiplying again with µ1 and µ2 shows that the assignment
γ↦→∆ Ψ (µ1γµ2) + µ1∆ Ψ (γ)µ2− µ1∆ Ψ (γµ2)− ∆ Ψ (µ1γ)µ2
is inSp. □
4. SchattenSp-estimates for the Ornstein-Uhlenbeck semi-group on q-Gaussians
We show that q-Gaussians Γ q(HR) with the Ornstein-Uhlenbeck semi-group are gradient- Sp for
a range of q depending on p and the dimension of the Hilbert space HR.
4.1. q-Gaussian algebras. Let HR be a ﬁnite dimensional real Hilbert space with complexiﬁcat ion
H = HR⊗ C. We denote by I the complex conjugation on H and we extend it to H ⊗n by
I(v1⊗···⊗ vn) := Iv n⊗···⊗ Iv 1. Let q∈ (−1, 1) and consider the symmetrization operator on
H ⊗n given by
P n
q (ξ1⊗ . . .⊗ ξn) =
∑
σ ∈Sn
qi(σ )ξσ (1)⊗ . . .⊗ ξσ (n),
where i(σ) is the number of inversions in σ. Recall that an inversion is a pair ( a, b)∈{ 1, . . . , n}
with a < b and σ(a) > σ (b). For q∈ (−1, 1) we set new inner products on H ⊗n by
⟨ξ, η⟩q =⟨P n
q ξ, η⟩,
and we refer to the Hilbert space with this q-deformed inner product as H ⊗n
q . Also set the q-Fock
space Fq(H) = CΩ⊕ (⊕∞
n=1H ⊗n
q ), with Ω a unit vector called the vacuum vector. Note that the
conjugation I extends to an antiunitary operator on Fq(H); a typical permutation does not preserve
the q-deformed inner product, so it is a special feature of the per mutation reversing the order. We
set the left creation operator for ξ∈ H,
lq(ξ)η1⊗ . . .⊗ ηn = ξ⊗ η1⊗ . . .⊗ ηn,
and the annihilation operator l∗
q (ξ) = lq(ξ)∗. These operators are bounded and extend to Fq(H)
for q∈ (−1, 1). We deﬁne the q-Gaussian algebra as
Γ q := Γ q(HR) :=A′′
q , Aq :=∗−alg{ lq(ξ) + lq(ξ)∗| ξ∈ HR}.
We let ϕΩ be the (tracial) vacuum state on Γ q(HR) given by ϕΩ (x) =⟨xΩ , Ω⟩. Ω is a separating
and cyclic vector for Γ q(HR) and so ϕΩ is faithful and Fq(H) is the standard Hilbert space of Γ q.
In this setting Ω is a tracial vector and further Γ q is a II 1-factor [Ric05].
For vectors ξ1, . . . , ξn∈ H there exists a unique operator Wq(ξ1⊗ . . .⊗ ξn)∈ Γ q(HR) such that,
Wq(ξ1⊗ . . .⊗ ξn)Ω = ξ1⊗ . . .⊗ ξn.
We call these operators elementary Wick operators or elementary Wick words . The
Ornstein-Uhlenbeck quantum Markov semi-group is then deﬁned by 1
Φ t(Wq(ξ1⊗ . . .⊗ ξn)) = e−tnWq(ξ1⊗ . . .⊗ ξn).
It comes with a generator (the quantum Dirichlet form) given by the number operator
∆( ξ1⊗ . . .⊗ ξn) = nξ1⊗ . . .⊗ ξn.
We determine the cohomology as follows.
1It extends to the q-Gaussian algebra by [BKS97, Theorem 2.11].
L2-COHOMOLOGY, DERIV ATIONS AND SEMI-GROUPS ON q-GAUSSIAN ALGEBRAS 11
Theorem 4.1. For anyAq-Aq-bimodule H we have H n(Aq, H) = 0 for n≥ 2.
Proof. Let e1, . . . , em be an orthonormal basis of HR. We claim that algebraically Aq is isomorphic
to the ∗-algebra of non-commutative polynomials in m self-adjoint variables X1, . . . Xm by the
identiﬁcation Xi := Wq(ei). Indeed, let P be a non-commutative polynomial and suppose that
P (X1, . . . , Xm) = 0. Let Q(X1, . . . , Xn) = Xi1 . . . Xid be a monomial occuring in P of highest
degree d. Then, from Lemma 4.3 below, we ﬁnd Q(X1, . . . , Xn) = Wq(Xi1⊗ . . .⊗ Xid) + A where
A is a linear combination of Wick operators Wq(ξ1⊗ . . .⊗ ξk) of tensors of order k < d . If
P (X1, . . . , Xm) = 0 we must therefore have that Q(X1, . . . , Xm) = 0. By induction we conclude
that P = 0.
Now in [CaEi56, p. 192] it is shown that for the algebra of non- commutative polynomials, the
Hochschild cohomology with coeﬃcients in any bimodule is 0. Alternatively, see [Kas04, Eqn.
(5.11)] for an explicit short exact projective resolution w hich also yields this result. □
