---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-022
section_title: "Page 22"
section_number: null
pages: 22-22
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Therefore, the required inequality |ρ|J ≤|σ|J + |τ|J means
|X| + |CJ(s)| ≤|X1| + |CJ(s1)| + |X2| + |CJ(s2)|.
By virtue of (4.2) and (4.3) this is equivalent to
|X| + |BJ(s)| ≤|X1| + |BJ(s1)| + |X2| + |BJ(s2)|.
(4.4)
We shall establish a stronger inequality,
|X| + |BJ(s)| ≤|X1| + |X2|,
(4.5)
which is equivalent to
|BJ(s)| ≤|X1 ∩X2|.
(4.6)
To prove the latter inequality, we shall show that each cycle c ∈BJ(s) contains a
point of X1 ∩X2.
By the deﬁnition of BJ(s), c contains both points of X1 and of X2. Therefore,
there exist points x1 ∈X1 ∩c and x2 ∈X2 ∩c such that sx1 = x2. We claim that
either x1 or x2 lies in X1 ∩X2. Indeed, if x1 ∈X1 \ X2 then
x2 = sx1 = ¯s1¯s2x1 = ¯s1x1 = s1x1 ∈X1 .
This shows that x2 ∈X1 ∩X2, which completes the proof.
□
Corollary 4.8 (of the proof). Let f ρ
στ̸ = 0 and |ρ|J = |σ|J + |τ|J. Then, in the
notation of the proof of Proposition 4.7, BJ(s1) = ∅, BJ(s2) = ∅, and (4.6) is
actually an equality.
Proof. Indeed, the equality |ρ|J = |σ|J +|τ|J means that (4.4) is an equality. Then
(4.5) is an equality, too. This implies all the claims.
□
Proposition 4.9. Assume J = N. For any partitions σ, τ,
p#
σ p#
τ = p#
σ∪τ + ⟨a linear combination of p#
ρ ’s with |ρ|N < |σ|N + |τ|N⟩.
Proof. We have
p#
σ p#
τ =
X
ρ
f ρ
στ p#
ρ .
By Proposition 4.7, only partitions ρ with |ρ|N ≤|σ|N + |τ|N can really contribute.
By Corollary 4.8, if f ρ
στ̸ = 0 and |ρ|N = |σ|N+|τ|N , then both BN(s1) and BN(s2)
are empty, which implies X1 ∩X2 = ∅. Therefore, ρ = σ ∪τ. Finally, by formula
(4.1), which we have derived from Corollary 4.4, f σ∪τ
στ
= 1. This completes the
proof.
□
Note that formula (4.1) can also be obtained from Proposition 4.9.
22
