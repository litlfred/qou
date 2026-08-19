---
doc_id: arxiv-math-0209324v1
doc_title: "CYCLOTOMIC COMPLETIONS OF POL YNOMIAL RINGS KAZUO HABIRO"
section_id: sec-020-74-non-surjectivity-of-ρz
section_title: "Non-surjectivity of ρZ"
section_number: 7.4
pages: 16-17
source_pdf: 0209324v1.pdf
source_sha256: ae2ea5024a0a45e8
doc_brief: "CYCLOTOMIC COMPLETIONS OF POLYNOMIAL RINGS KAZUO HABIRO — The main object of study in this paper is the completion Z[q]N = lim←− n Z[q]/ ((1− q)(1− q2)···(1− qn)) of the polynomial ring Z[q], which"
---
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
