---
doc_id: arxiv-math-0108215v1
doc_title: "Möbius Energy of Thick Knots Eric J. Rawdon 2"
section_id: sec-015-3-b-13-13-for-b-p-notice-that-ℓ2-b-ℓ2-p
section_title: "((b + 1)3 − 13). For b > P , notice that ℓ∗(2, b] = ℓ∗(2, P ]"
section_number: 3
pages: 11-12
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
---
so ℓ∗[2, b] = ℓ∗[2, P ] = L − 2π.
We now show that
ℓ[2, r] ≤ ℓ∗[2, r] for all 2 ≤ r . (9)
11
The tube T [2, r] has volume πℓ[2, r]. But T [2, r] lies entirely within S[1, r + 1],
whose volume is 4
3π ((r + 1)3 − 13). Thus, when 2 ≤ r ≤ P ,
πℓ[2, r] ≤ 4
3 π
(
(r + 1)3 − 13
)
= πℓ∗[2, r].
If r > P , then ℓ∗[2, r] = ℓ∗[2, P ] = L − 2π ≥ ℓ[2, r]. Thus, we have (9).
We next partition Ydist into sets Wj whose distance to x is controlled, and
express I x
dist as the sum of the contributions from these sets.
Let n ∈ N and δ = P −2
n . Then,
ℓ∗[2, P ] = ℓ∗[2] + ℓ∗(2, 2 + δ] + ℓ∗(2 + δ, 2 + 2δ] + · · · + ℓ∗(P − δ, P]
= L − 2π.
We deﬁne a sequence of sets {Wj} using Lemma 7 as follows. Let ν0 = ℓ∗[2] and
νj = ℓ∗(2+(j−1)δ, 2+jδ] for 1 ≤ j ≤ n. Note that νn = ℓ∗(2+(n−1)δ, 2+nδ] =
ℓ∗(P − δ, P]. Since ν0 + ν1 + · · · + νn = L − 2π = µ(Ydist), by Lemma 7,
there exists a sequence 2 ≤ ρ0 ≤ ρ1 ≤ · · · ≤ ρn and a partition of Ydist into
measurable sets W0, · · · , Wn such that: for 1 ≤ j ≤ n, we have µ(Wj) = νj and
Wj ⊆ Ydist∩S[ρj−1, ρj]; for j = 0, we have µ(W0) = ν0 and W0 ⊆ Ydist∩S[2, ρ0].
We want to know how far each Wj is from x, so we next bound the radii ρj
(from below) in terms of j and δ. If y ∈ W0, then |x − y| ≥ 2 by Lemma
