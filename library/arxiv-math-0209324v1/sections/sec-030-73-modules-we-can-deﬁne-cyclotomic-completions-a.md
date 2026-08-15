---
doc_id: arxiv-math-0209324v1
doc_title: "CYCLOTOMIC COMPLETIONS OF POL YNOMIAL RINGS KAZUO HABIRO"
section_id: sec-030-73-modules-we-can-deﬁne-cyclotomic-completions-a
section_title: "Modules. We can deﬁne cyclotomic completions also for any Z-modules"
section_number: 7.3
pages: 16-17
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
---
as follows. Let A be a Z-module, and let A[q] denote the Z[q]-module of poly-
nomials in q with coeﬃcients in A. For each S⊂ N let A[q]S denote the
completion
A[q]S = lim←−f ∈Φ ∗
S
A[q]/f A [q].
If A is a ring, then this deﬁnition of A[q]S is compatible with the previous
one. Some results in the present paper can be generalized to t he A[q]S.
For example, Theorem 4.2 is generalized as follows. Let ⇔A denote the
relation on N such that m⇔A n if and only if either we have A = 0, or m/n
is an integer power of a prime p with A being p-adically separated.
Theorem 7.6. Let A be a Z-module, and let S′⊂ S⊂ N be subsets. Suppose
that for each n∈ S there is a sequence S′∋ n′⇔A···⇔ A n in S. Then
the homomorphism ρA
S,S ′ : A[q]S→ A[q]S′
induced by idA[q] is injective.
Proof. One way to prove Theorem 7.6 is to modify Section 3 and the proo f
of Theorem 4.2. We roughly sketch the necessary modiﬁcation s. Section 3
is generalized as follows. For two elements f, g ∈M R and an R-module,
we write f⇒A g if f I⇒A g for some ideal I with A being I-adically sep-
arated. Then Proposition 3.2 with R replaced with an R-module A holds.
Generalizations of Theorem 3.4 and Corollary 3.5 to R-modules is straight-
forward. Theorem 7.6 follows immediately from the generali zed version of
Corollary 3.4.
Alternatively, we can use Theorem 4.2 as follows. Since the c ase A = 0 is
trivial, we assume not. Let A′ = Z⊕ A be the ring with the multiplication
(m, a )(n, b ) = ( mn, mb + na) and with the unit (1 , 0). Then for m, n ∈ N we
have m⇔A n if and only if m⇔A′ n. Hence we can apply Theorem 4.2 to
obtain the injectivity of ρA′
S,S ′. We can identify ρA′
S,S ′ with the direct product
ρZ
S,S ′⊕ ρA
S,S ′ : Z[q]S⊕ A[q]S→ Z[q]S′
⊕ A[q]S′
.
Hence ρA
S,S ′ is injective. □
7.4. Non-surjectivity of ρZ
N, {n}.
Proposition 7.7. (1) If m, n ∈ N, m ⇔Z n, and m ⁄= n, then the
homomorphism ρZ
{m,n }, {m} : Z[q]{m,n }→ Z[q]{m} is not surjective.
(2) If m|n and m ⁄= n, then the homomorphism ρZ
⟨n⟩, ⟨m⟩: Z[q]⟨n⟩ →
Z[q]⟨m⟩ is not surjective.
(3) For each nonempty, ﬁnite subset S⊂ N, the homomorphism ρZ
N,S : Z[q]N→
Z[q]S is not surjective.
CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS 17
Proof. (1) We have m/n = pe for some prime p and an integer e ⁄= 0.
Consider the following commutative diagram of natural homo morphisms.
Z[q]{m,n } ρZ
{m,n }, {m}
−−−−−−−→Z[q]{m}


↓


↓ b
Z[q]/ (Φ n(q)) −−−−→
c
Zp[q]/ (Φ n(q))
It follows from Zp[q]/ (Φ n(q))≃ lim
←−j Z[q]/ (Φ n(q), p j), Φ m(q)∈
√
(Φ n(q), p ),
and p∈ (Φ m(q), Φ n(q)) that b is a well-deﬁned, surjective homomorphism.
Since c is not surjective, ρZ
{m,n }, {m} is not surjective.
(2) We may assume that n = pm for a prime p. The case m = 1 is
contained in (1) above. There are isomorphisms Z[q]⟨m⟩≃ Z[qm]⟨1⟩⊗Z[qm]
Z[q] and Z[q]⟨pm⟩≃ Z[qm]⟨p⟩⊗Z[qm] Z[q] induced by the isomorphism Z[q]≃
Z[qm]⊗Z[qm] Z[q]. Then the case m = 1 implies the non-surjectivity of
ρZ
⟨pm⟩, ⟨m⟩.
(3) This follows from (2) above, since ρZ
N,S factors through ρZ
⟨n⟩, ⟨m⟩ for
some m, n with m|n and m⁄= n. □
