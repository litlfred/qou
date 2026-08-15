---
doc_id: arxiv-1704.02352v2
doc_title: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS"
section_id: sec-018-43-estimates-on-some-classes-of-permutations
section_title: "Estimates on some classes of permutations"
section_number: 4.3
pages: 31-32
source_pdf: 1704.02352v2.pdf
source_sha256: 9a14dd6ee33248d3
doc_brief: "GAUSSIAN FLUCTUATIONS OF JACK-DEFORMED RANDOM YOUNG DIAGRAMS — We introduce a large class of random Y oung diagrams which can be regarded as a natural one-parameter deformation of so me classi- cal Y"
---
tation π we denote by C(π) the set of its cycles. The length
‖π‖ := l − |C(π)|
of a permutation π ∈ S(l) is deﬁned as the minimal number of factors
necessary to write π as a product of transpositions.
Lemma 4.3. F or all integersr ≥ 0 and l ≥ 1
#
{
π ∈ S(l) : ‖π‖ = r
}
≤ l2r
r! .
Proof. We claim that for each permutation π ∈ S(l) such that ‖π‖ = r
there exist at least r transpositions τ with the property that the permutation
π′ := πτ fulﬁlls ‖π′‖ = ‖π‖ − 1. Indeed, each such a transposition is of
the form τ = ( a, b) with a ⁄= b being elements of the same cycle of π; it
follows that the number of such transpositions is equal to
∑
c∈C(π)
(|c|
2
)
≥
∑
c∈C(π)
(
|c| − 1
)
= ‖π‖.
By repeating inductively the same argument for the collecti on of permu-
tations (π′) obtained above, it follows that the permutation π can be written
in at least r! different ways as a product of r transpositions. Since there are(l
2
)
< l 2 transpositions in S(l), this concludes the proof. □
32 MACIEJ DOŁ ˛ EGA AND PIOTR ´SNIADY
We revisit Section 3.8.2. In the following we will need a conv enient way
of parametrizing the equivalence classes in Xl/ ∼; for this purpose we note
that in each equivalence class one can choose a representati ve (which is not
necessarily unique) (σ1, σ2) with the property that the permutation σ2 has a
particularly simple cycle structure, namely
σ2 = (1, 2, . . . , i1)(i1 + 1, i1 + 2, . . . , i2) · · ·(iℓ−1 + 1, iℓ−1 + 2, . . . , iℓ)
for some increasing sequence 1 ≤ i1 < i 2 < · · · < i ℓ = l. Note that for a
ﬁxed ℓ = |C(σ2)|
(4.6) the number of permutations σ2 of the above form
is given by
( l
ℓ − 1
)
≤ lℓ−1.
