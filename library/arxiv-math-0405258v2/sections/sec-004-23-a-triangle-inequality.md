---
doc_id: arxiv-math-0405258v2
doc_title: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES"
section_id: sec-004-23-a-triangle-inequality
section_title: "A triangle inequality"
section_number: 2.3
pages: 5-6
source_pdf: 0405258v2.pdf
source_sha256: dbd6bf5a94deebaf
doc_brief: "SECOND ORDER FREENESS AND FLUCTUATIONS OF RANDOM MATRICES: II. UNITARY RANDOM MATRICES — We extend the relation between random matrices and free probability theory from the level of expectations to"
---
If, for 1 ≤ i ≤ k, πi is a permutation of the set Ai we denote by
π1 × · · · × πk ∈ Sn the concatenation of these permutations. We say
that π = π1 × · · · × πk is a cycle decomposition if additionally every
factor πi is a cycle.
Notation 2.1. 1) For A ∈ P (n) we put |A| := n − #(A)
2) For any π ∈ Sn and any π-invariant A ∈ P (n) we put
|(A, π)| := 2|A| − |π|.
Lemma 2.2. 1 ) For all A, B ∈ P (n) we have
|A ∨ B| ≤ | A| + |B|
2) If π and σ are in Sn and A, B ∈ P (n) are π and σ invariant respec-
tively, then
|(A ∨ B, πσ)| ≤ | (A, π)| + |(B, σ)|.
6 J. A. MINGO, P. ´SNIADY, AND R. SPEICHER
Proof. 1) Each block of B with k points can glue together at most k
blocks of A, thereby reducing the number of blocks of A by at most
k − 1. Thus B can reduce by at most n − #(B) the number of blocks
of A. Hence the diﬀerence between #( A) and #( A ∨ B) cannot exceed
n − #(B) and hence
#(A) − #(A ∨ B) ≤ n − #(B).
This is equivalent to our assertion.
2) We prove this, for ﬁxed π and σ by induction on |A| + |B|. The
smallest possible value of |A|+|B| occurs when |A| = |π| and |B| = |σ|.
But then we have (since A ∨ B ≥ πσ)
2|A ∨ B| − |πσ| ≤ | A ∨ B| ≤ | A| + |B| by (1)
which is exactly our assertion for this case. For the induction step n ote
that we have just shown that
2|A ∨ B| − |πσ| ≤ 2|A| − |π| + 2|B| − |σ|
when |A| = |π| and B| = |σ|. Now one only has to observe that if one
increases |A| (or |B|) by 1 then |A ∨ B| can also increase by at most
1.
