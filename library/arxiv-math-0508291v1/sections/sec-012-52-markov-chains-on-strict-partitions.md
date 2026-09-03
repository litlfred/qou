---
doc_id: arxiv-math-0508291v1
doc_title: "Stein’s Method and Random Character Ratios"
section_id: sec-012-52-markov-chains-on-strict-partitions
section_title: "Markov chains on strict partitions"
section_number: 5.2
pages: 32-34
source_pdf: 0508291v1.pdf
source_sha256: d2d541426aaec742
doc_brief: "Stein’s Method and Random Character Ratios — Stein’s method is used to prove limit theorems for random character ratios."
---
Markov chain on DP (n) to be used in deﬁning an exchangeable pair for the
proof of Theorem 5.2.
Motivated by constructions in the group and Gelfand pair cas es, it would
be natural, for τ a ﬁxed element of DP (n), to deﬁne a “Markov chain” Jτ
on DP (n) with transition “probabilities”
Jτ (λ,ρ ) := gρ
2l(ρ)gλgτ
∑
ν∈OP (n)
2l(ν)X λ
νX ρ
νX τ
ν
zν
.
Using Lemma 5.4, one can see that ∑
ρJτ (λ,ρ ) = 1 for all λ, and that Jτ
satisﬁes the reversibility condition
2n−l(λ )g2
λ
n! Jτ (λ,ρ ) = 2n−l(ρ)g2
ρ
n! Jτ (ρ,λ )
for all λ,ρ ∈DP (n). Unfortunately, the quantity Jτ (λ,ρ ) can be negative.
For instance one can check from Lemma 5.6 that J(2, 1)((2, 1), (2, 1)) = −1.
To deal with the complication raised in the previous paragra ph, it is
helpful to introduce a genuine Markov chain L on DP (n), with transition
probabilities
L(λ,ρ ) = 2gρ
ngλ
∑
η ∈DP (n−1)
η րλ,η րρ
2l(η)−l(ρ).
Hereη րλ means that η is obtained from λ by decreasing the size of some
part by exactly one.
Lemma 5.7 proves that L is a Markov chain which is reversible with
respect to shifted Plancherel measure. As is mentioned in th e proof, the
deﬁnition ofL was motivated by the theory of harmonic functions on Brattel i
diagrams.
Lemma 5.7. The transition probabilities of L are real and non-negative
and sum to 1. Moreover the chain L is reversible with respect to shifted
Plancherel measure.
Proof. This is a special case of a construction in Section 2 of [F1]. T o see
this, one takes the underlying Bratteli diagram to be the Sch ur graph, the
properties of which are discussed in Section 5 of [BO2]. The v ertices of the
Schur graph are all partitions of all non-negative integers with distinct parts,
and the edge multiplicity between η ∈ DP (n − 1) and λ ∈ DP (n) is 1 if
η րλ, and is 0 otherwise. The combinatorial dimension of a shape λ isgλ ,
and if π denotes shifted Plancherel measure, the function π (λ )
gλ
is harmonic
on the Schur graph. □
33
Proposition 5.9 will establish a fundamental relation betw een the Markov
chainL and the “Markov chain” J(n−1, 1). The argument involves symmetric
function theory, and ﬁrst a lemma is needed about properties of a certain
subring Γ of the ring of symmetric functions, deﬁned on page 2 52 of [Mac].
Recall from page 255 of [Mac] that there is an inner product on Γ which
satisﬁes the properties
(1) ⟨pλ,p µ ⟩ = 2 −l(λ )zλδλ,µ if λ,µ ∈OP (n).
(2) ⟨Pλ,P µ ⟩ = 2 −l(λ )δλ,µ if λ,µ ∈DP (n).
Here pλ is a power sum symmetric function and Pλ is a Hall-Littlewood
polynomial with the parameter t = −1. It is also helpful to recall, from
page 247 of [Mac], that for λ ∈DP (n),
Pλ = 2 −l(λ ) ∑
ν∈OP (n)
2l(ν)
zν
X λ
νpν.
Lemma 5.8. Letp⊥
1 be the adjoint in Γ of multiplication by p1.
(1) ([Mac], page 265) p⊥
1 = 1
2
∂
∂p 1
.
(2) p⊥
1Pλ =∑
η ∈DP (n−1)
η րλ
2l(η)−l(λ )Pη.
Proof. Only the second assertion needs to be proved. Consider the co eﬃcient
of Pη in p⊥
1Pλ . It is
⟨p⊥
1Pλ,P η⟩
⟨Pη,P η⟩ = ⟨Pλ,p 1Pη⟩
⟨Pη,P η ⟩ = 2 l(η)⟨Pλ,p 1Pη⟩.
From Section 3.8 of [Mac],
p1Pη =
∑
λ ∈DP (n)
η րλ
Pλ,
which implies the result. □
Proposition 5.9 can now be proved.
Proposition 5.9. Suppose that n ≥ 3, so that (n − 1, 1) is a strict partition.
Then
L(λ,ρ ) = n − 2
n J(n−1, 1)(λ,ρ )
for λ,ρ ∈DP (n) such that λ ⁄=ρ.
Proof. By Lemma 5.6,
J(n−1, 1)(λ,ρ ) = gρ
2l(ρ)gλ (n − 2)
∑
ν∈OP (n)
2l(ν)X λ
νX ρ
ν (m1(ν) − 2)
zν
.
34
Since λ ⁄=ρ, Lemma 5.3 and part 1 of Lemma 5.8 imply that this is equal
to
gρ
2l(ρ)gλ (n − 2)
∑
ν∈OP (n)
2l(ν)X λ
νX ρ
νm1(ν)
zν
= gρ
2l(ρ)gλ (n − 2)
⟨ ∑
ν∈OP (n)
m1(ν) 2l(ν)
zν
X λ
νpν,
∑
ν∈OP (n)
2l(ν)
zν
X ρ
νpν
⟩
= 2l(λ )gρ
gλ (n − 2) ⟨2p1p⊥
1Pλ,P ρ⟩
= 2l(λ )+1gρ
gλ (n − 2) ⟨p⊥
1Pλ,p ⊥
1Pρ⟩.
By part 2 of Lemma 5.8, this is
2l(λ )+1gρ
gλ (n − 2)
⟨ ∑
η ∈DP (n−1)
η րλ
2l(η)−l(λ )Pη,
∑
η ∈DP (n−1)
η րρ
2l(η)−l(ρ)Pη
⟩
= 2gρ
gλ (n − 2)
∑
η ∈DP (n−1)
η րλ,η րρ
2l(η)−l(ρ)
= n
n − 2L(λ,ρ ).
□
