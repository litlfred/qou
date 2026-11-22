---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-023
section_title: "Page 23"
section_number: null
pages: 23-23
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Proposition 4.10. The ﬁltration of A deﬁned by degN( · ) coincides with the weight
ﬁltration.
Proof. For any r = 0, 1, . . ., let A′
r ⊂A denote the rth member of the ﬁrst ﬁltration,
and let A′′
r ⊂A has the same meaning for the second ﬁltration. Recall that
A′
r = span{p#
ρ | |ρ|N = |ρ| + ℓ(ρ) ≤r},
A′′
r = span{epk1 . . . epkl | k1, . . ., kl ≥2,
k1 + · · · + kl ≤r}.
Clearly,
A′
0 = A′′
0 = A′
1 = A′′
1 = R · 1.
We shall prove that for any r ≥2, both A′
r ⊆A′′
r and A′′
r ⊆A′
r. By Proposition
4.9,
A′
r = span{p#
k1 . . . p#
kl | k1, . . .kl ≥1,
k1 + · · · + kl + l ≤r}.
Therefore, it suﬃces to show that
p#
k ∈span{epk1 . . . epkl | k1, . . ., kk ≥2,
k1 + · · · + kl ≤k + 1},
epk ∈span{p#
k1 . . .p#
kl | k1, . . . , kl ≥1,
k1 + · · · + kl + l ≤k}.
The ﬁrst inclusion follows from Proposition 3.5, and the second inclusion follows
from Proposition 3.7.
□
In the remaining part of the section we focus on the ﬁltration corresponding to
J = {1}. It ﬁrst appeared in [Ke1], and we propose to call it the Kerov ﬁltration
of A.
Let us abbreviate
|ρ|1 = |ρ|{1} = |ρ| + m1(ρ),
deg1( · ) = deg{1}( · ).
The next three results will be used in §6.
Proposition 4.11. For any partition σ,
p#
σ p#
1 = p#
σ∪1 + ⟨a term of lower degree with respect to deg1( · )⟩.
Proof. Actually, the following exact formula holds:
p#
σ p#
1 = p#
σ∪1 + |σ| · p#
σ .
(4.7)
To prove this, apply Deﬁnition 4.1 and evaluate both sides at a partition λ. It suf-
ﬁces to assume that n = |λ| is large enough, n ≥|σ|+1. Then we get, abbreviating
k = |σ|,
p#
σ (λ) = n↓k · χλ
σ∪1n−k
dim λ
,
p#
σ∪1(λ) = n↓(k+1) · χλ
σ∪1n−k
dim λ
,
because (σ ∪1) ∪1n−k−1 = σ ∪1n−k.
Therefore, the veriﬁcation of (4.7) at λ reduces to the relation
n↓k · n = n↓(k+1) + n↓k · k,
which is trivial.
□
Note that Proposition 4.11 can also be obtained from Proposition 4.7. We shall
use this approach in the next proposition.
23
