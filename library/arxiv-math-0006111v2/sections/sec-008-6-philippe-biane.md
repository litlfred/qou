---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: sec-008-6-philippe-biane
section_title: "PHILIPPE BIANE"
section_number: 6
pages: 6-8
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of s ymmet- ric groups."
---
depends only on the set J of places where ik or jk is 0, and the partition of the
set ( {1, 2,...,n 1} ∪ { 1′, 2′,... ,n ′
2}) \J given by the equivalence relation u ∼ v
if iu = iv, u ∼ v′ if iu = jv′, or u′ ∼ v′ if ju′ = jv′ . Given such a set J ⊂
{1, 2,...,n 1} ∪ { 1′, 2′,... ,n ′
2} and the partition π , the number of corresponding
terms in the sum is equal to ( q)comp(π ) where (q)r = q(q − 1)... (q −r + 1) and
comp(π ) is the number of components of π . Denoting by ψ (π,J ) the common value
of ψ on sequences corresponding to the set J and the partition π , the right hand
side of (2.1.2) can be rewritten as a sum of the form
(2.1.4)
∑
π,J
1
(q + 1)2 (q)comp(π )ψ (π,J )
Analogously we can write the right hand side of (2.1.3) as
(2.1.5)
∑
π 1 ,J 1
π 2 ,J 2
1
(q + 1)2 (q)comp(π 1)ψ (π 1,J 1)(q)comp(π 2)ψ (π 2,J 2)
Let h(π ) denote the conjugacy class of the permutation correspondi ng to π , and
let |h(π )| denote the length of any of its elements. Hypothesis (1) of De ﬁnition 1.3
implies a bound |ψ (π,J )| ≤ Cq −|h(π )|/ 2. Furthermore, by an argument similar to
Lemma 4.3.2 of [B] one can see that if J ⁄= ∅, then
n + |h(π )| ≥ 2comp(π ) − 1
therefore the total contribution of terms such that J ⁄= ∅ can be bounded by
Cqn/ 2−1 for some constant C depending only on n and on the sequence ( cl)1≤l≤n.
A similar argument using Lemma 4.3.2 of [B] would apply to (2. 1.3), we shall
therefore restrict the sums in (2.1.2) and (2.1.3) to i′s andj′s in the range 1,... ,q ,
and replace (2.1.4) by a sum
(2.1.6)
∑
π
1
(q + 1)2 (q)comp(π )ψ (π )
over partitions π of {1, 2,...,n 1} ∪ { 1′, 2′,... ,n ′
2}. Consider now the contri-
bution to (2.1.6) of partitions π such that some u ∈ { 1, 2,...,n 1} and some
v′ ∈ { 1′, 2′,...,n ′
2} are in the same component, then using Lemma 5.1.2 from
[B] and the estimate (1) of Deﬁnition 1.3 we can again bound th is contribution
by Cqn/ 2−1. It remains to consider the contribution of partitions π which split
as the union of a partition π 1 of {1,...,n 1} and a partition π 2 of {1′, 2′,...,n ′
2}.
For such a partition, any associated permutation ( i1i2)... (in1i1)(j1j2)... (jn2j1)
is the product of two permutations with disjoint supports ( i1i2)... (in1i1) and
(j1j2)... (jn2j1), so that by the asymptotic factorization property, one has
|ψ
(
(i1i2)... (in1i1)(j1j2)... (jn2j1)
)
−ψ
(
(i1i2)... (in1i1)
)
ψ
(
(j1j2)... (jn2j1)
)
|
≤δq−|h(π )|/ 2
Since by [B], Section 4.3, one has ni + |h(πi)| ≥ 2comp(πi) − 2 we can replace
(2.1.6) by
(2.1.7)
∑
π =π 1∪π 2
1
(q + 1)2 (q)comp(π )ψ (π 1)ψ (π 2)
APPROXIMATE F ACTORIZATION AND CONCENTRATION 7
making an error bounded by Cδql/ 2. On the other hand the right hand side of
(2.1.5) can be replaced by
(2.1.8)
∑
(π 1,π 2)
1
(q + 1)2 (q)comp(π 1)(q)comp(π 2)ψ (π 1)ψ (π 2)
The diﬀerence between (2.1.7) and (2.1.8) is
∑
(π 1,π 2)
1
(q + 1)2 ((q)comp(π ) − (q)comp(π 1)(q)comp(π 2))ψ (π 1)ψ (π 2)
One has
comp(π 1 ∪π 2) = comp(π 1) +comp(π 2)
thus
|(q)comp(π 1∪π 2) − (q)comp(π 1)(q)comp(π 2)| ≤ Cqcomp(π 1)+comp(π 2)−1
By Lemma 4.3.2 and 4.3.3 of [B], one has
n1 +n2 + |h(π 1)| + |h(π 2)| ≥ 2(comp(π 1) +comp(π 2)) − 4
therefore each term in this diﬀerence is bounded by Cql/ 2−1 and one gets the stated
result. □
Using the Lemma, we can now estimate the variance of mn(λ) under the measure
Πψ , indeed it follows from Section 3.3 in [B] that one has
Πψ ((ml(λ) −ml(ψ ))2) = τψ (⟨Γ(ψ )l⟩2) −τψ (⟨Γ(ψ )l⟩)2
therefore, using Lemma 2.1, for ψ ∈ Fn
c,δ one has
Πψ ((ml(λ) −ml(ψ ))2) ≤K(δ +q−1)ql by Lemma 2.1
Theorem 1 now follows by an application of Markov’s inequali ty. □
Corollary 1 is a simple consequence of Theorem 1 and of the mom ent-cumulant
formula.
Finally for the proof of Theorem 2, we can use the same argumen ts as in Section
4 of [B], and the hypotheses (1) and (2) of Deﬁnition 3.1. This shows that there
exists a constant K such that, for all ψ ∈ Fn
c,δ , all l ≤ n and all cycle ρ on l − 1
elements, one has
|cl(ψ )q1−l −ψ (ρ)| ≤ K(δ +q−1)q−l/ 2 for all l ≤n
This, combined with Corollary 1 gives Theorem 2. □
