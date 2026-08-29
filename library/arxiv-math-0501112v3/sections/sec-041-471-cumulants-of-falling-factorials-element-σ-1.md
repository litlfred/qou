---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-041-471-cumulants-of-falling-factorials-element-σ-1
section_title: "Cumulants of falling factorials. Element Σ 1, . . . , 1"
section_number: 4.7.1
pages: 24-26
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
k times
∈ C(Sq ) is
equal to q(q − 1) · · ·(q + 1 − k), the multiple of identity, therefore no
matter which representation we consider we always have
EΣ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
k times
∈ C(Sq ) = q(q − 1) · · ·(q + 1 − k).
However, it should be stressed that if we consider the algebra of conjugacy
classes equipped with the disjoint product then this elemen t is not longer a
multiple of identity and
Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
k1 times
• Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
k2 times
= Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
k1 +k2 times
.
Lemma 4.8. For any integersl1, . . . , l n ≥ 1
k•(Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
, . . . , Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
) = O(ql1 +···+ln+1− n).
Proof. It is easy to check that
k(Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
, . . . , Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
) =
{
q(q − 1) · · ·(q + 1 − l1) if n = 1,
0 if n ≥ 2,
GAUSSIAN FLUCTUATIONS OF CHARACTERS OF SYMMETRIC GROUPS 25
hence in particular
k(Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
, . . . , Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
)q−( l1 +···+ln+1− n) = O(1).
We leave it as a simple exercise to the reader to check that the presented
above proof of the implication (3.3) =⇒ (3.2) can be applied here. □
Proof of the implication (3.1) =⇒ (3.2). Our goal is to estimate the right-
hand side of (4.9). The assumption (3.1) implies that
kπ (1) (σ 1, . . . , σ n) = O
(
q−
|σ 1 |+···+|σ n |+2n − 2(number of blocks of π (1))
2
)
;
Lemma 4.8 implies that
k•
π (2) (Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
, . . . , Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
) = O
(
ql1 +···+ln +(number of blocks of π (2))− n)
.
Now it is enough to use Lemma 4.6. □
We leave the proof of the identity
lim
q →∞
Cov•(Σ l1 , Σ l2)q− l1 +l2
2 = lim
q →∞
Cov(σ 1, σ 2)q
l1 +l2
2 − l1l2cl1+1cl2 +1
which is a part of Theorem 3.2 as a simple exercise.
Proof of (3.2) =⇒ (3.1). We use the induction over n. We let us split the
sum in equation (4.9) into the sum of terms with π (1) is the maximal parti-
tion with only one block and the sum of all the other terms; therefore
k(σ 1, . . . , σ n)E
(
Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
• · · · • Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
)
= k•(Σ l1 , . . . , Σ ln )−
∑
π (1),π (2)
kπ (1) (σ 1, . . . , σ n) k•
π (2) (Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
l1 times
, . . . , Σ 1, . . . , 1
/bracehtipupleft
/bracehtipdownright/bracehtipdownleft /bracehtipupright
ln times
),
where the sum runs over partitions π (1), π (2) such as in (4.9) with the addi-
tional constraint that π (1) is not equal to the maximal partition with only one
block. We use the inductive hypothesis and estimate the summ ands on the
right-hand side in the same way as in the proof of the opposite implication
above. □
4.8. Proof of the main theorem: equivalence (3.3) ⇐ ⇒ (3.4).
Proof of equivalence (3.3) ⇐ ⇒ (3.4). It is enough to apply Corollary 4.7.
□
