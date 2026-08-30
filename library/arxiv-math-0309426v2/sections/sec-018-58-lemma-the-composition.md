---
doc_id: arxiv-math-0309426v2
doc_title: "ELEMENTARY DIVISORS OF SPECHT MODULES"
section_id: sec-018-58-lemma-the-composition
section_title: "Lemma. The composition"
section_number: 5.8
pages: 8-9
source_pdf: 0309426v2.pdf
source_sha256: f2aa01164d9f243c
doc_brief: "ELEMENTARY DIVISORS OF SPECHT MODULES — 46 sections: MATTHIAS K ¨UNZER AND ANDREW MATHA; Introduction and statement of main; The Hecke algebra and permutation"
---
S(λ) ✲γλ
S(λ)∗ ✲ψ−1
λ
∼ S(λ′)# ✲γ#
λ ′
S(λ′)∗,# ✲(ψ#
λ ′ )−1
∼ S(λ)
is equal to scalar multiplication by (−q)ℓ(wλ ′ )qn−α(λ)−α(λ′)hλ(q).
Proof. The element zλ is mapped via γλ to ⟨zλ, −⟩λ, which is mapped via ψ−1
λ
to zλ′ ·# Twλyλ′ = zλ′T #
wλy#
λ′, which in turn goes to ⟨zλ′T #
wλy#
λ′, −⟩λ via γ#
λ′ , and
ﬁnally to
zλ ·# Twλ ′yλT #
wλy#
λ′ = ( −q)ℓ(wλ ′ )q−α(λ′)zλT −1
wλ zλ
= ( −q)ℓ(wλ ′ )qn−α(λ)−α(λ′)hλ(q)zλ
via (ψ#
λ′ )−1, by Lemma 5.7. □
LetIm be the m×m identity matrix. Recall that nλ = # Std(λ) is the dimension
of the Specht module S(λ).
5.9. Proposition. Suppose that λ is a partition of n.
(1) There exist invertible matrices A,B ∈ GLnλ (Z[q,q −1]) such that
G(λ) ·A ·G(λ′) ·B = hλ(q) ·Inλ .
(2) G(λ) is diagonalizable to the diagonal matrix D if and only if G(λ′) is
diagonalizable to the diagonal matrix hλ(q)D−1.
(3) G(λ) is divisibly diagonalizable if and only if G(λ′) is divisibly diagonal-
izable. In this case, the product of the ith elementary divisor of G(λ) and
the (nλ + 1 −i)th elementary divisor of G(λ′) is equal to hλ(q).
Recall that elementary divisors are only well deﬁned up to a unit in Z[q,q −1];
the same is true of their product in (3).
Proof. (1) The R-linear map γλ is represented by the matrix G(λ) with respect to
the Dipper–James basis and its dual basis. Thus the assertion follow s by (5.8).
(2) If G(λ) = SDT with S,T ∈ GLnλ (Z[q,q −1]) and D ∈ Z[q,q −1]nλ ×nλ is
a diagonal matrix, then G(λ′) = A−1T −1(hλ(q)D−1)S−1B−1. Since G(λ′) has
coeﬃcients in Z[q,q −1], so does hλ(q)D−1.
(3) Repeat the argument of (2). □
We remark that all of the results in this section hold more generally wh en the
Hecke algebra H is deﬁned over an integral domain R such that H ⊗R Q is
semisimple, where Q is the ﬁeld of fractions of R. (We need semisimplicity over Q
only when we apply Murphy’s results in the proof of Lemma 5.7.) In part icular,
Proposition 5.9 holds when R = F [q,q −1] and F is any ﬁeld. Notice that G(λ) is
always diagonalizable in this case because F [q,q −1] is a principle ideal domain.
ELEMENTARY DIVISORS OF SPECHT MODULES 9
