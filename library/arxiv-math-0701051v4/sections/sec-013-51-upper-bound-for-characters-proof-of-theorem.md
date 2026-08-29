---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-013-51-upper-bound-for-characters-proof-of-theorem
section_title: "Upper bound for characters: proof of Theorem ??"
section_number: 5.1
pages: 15-16
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
Proof of Theorem 1. Let k1, . . . , kr ≥ 2 be the lengths of the non-trivial
cycles in the cycle decomposition of π ∈ Sn. It follows that l := k1 + · · · +
kr = | supp π| and in the following we will regard π as an element of Sl.
We denote A = max(l, r(λ), c(λ)).
We consider a map which to a pair (σ1, σ2) associates any pair (σ′
1, σ′
2)
as prescribed by Lemma 13. For any ﬁxed σ′
2 the permutations σ2 such that
|σ′
2| = |σ′
2σ−1
2 | + |σ2| can be identiﬁed with non-crossing partitions of the
cycles of σ′
2 (see [Bia97, Section 1.3]). It follows that the number of suc h
permutations σ2 is equal to the product of appropriate Catalan numbers and,
hence, this product is bounded from above by 4l. Therefore Theorem 2 and
16 V ALENTIN FÉRAY AND PIOTR ´SNIADY
Proposition 12 show that
|Σ λ(π)| ≤
∑
σ1,σ2∈Sl,
σ1σ2=π
Al−rnr
( 1
A
) o(σ1,σ2)
≤ 4l ∑
σ′
1,σ′
2∈Sl,
σ′
1σ′
2=π
Al−rnr
( 1
A
) |σ′
1|
≤ 4lAl−rnr
∑
σ′
1∈Sl
( 1
A
) |σ′
1|
≤ 4lAl−rnr
∑
i≥0
l2i
Aii! ,
where the last inequality follows from Lemma 14. It follows that
(20) |Σ λ(π)| ≤ 4lAl−rnre
l2
A ≤ (4e)lAl−rnr.
After dividing by (n)l ≥
( n
e
) l
, we obtain |χλ(π)| ≤ (4e2)l(A/n)l−r, which
ﬁnishes the proof because l = | supp π| ≤ 2|π| and l − r = |π|. □
