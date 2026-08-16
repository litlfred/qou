---
doc_id: arxiv-2401.04019v1
doc_title: "TRUNCA TED THET A SERIES RELA TED TO THE JACOBI TRIPLE PRODUCT IDENTITY"
section_id: sec-009-7-concluding-remarks
section_title: "Concluding remarks"
section_number: 7
pages: 18-20
source_pdf: 2401.04019v1.pdf
source_sha256: 1a29e52a81639640
doc_brief: "TRUNCATED THETA SERIES RELATED TO THE JACOBI TRIPLE PRODUCT IDENTITY — The work of Andrews and Merca on the truncated Euler’s pen- tagonal number theorem led to a resurgence in research on tru ncated"
---
In this article we considered several conjectures and identities th at ﬁrst appeared
in [14]. Identities (6.7), (6.10), (6.12) and (6.13) from [14] are prove d using the
Jacobi Triple Product identity in [13]. We generalized these identities a nd gave both
analytic and combinatorial proofs. Considerations of similar identitie s from [14],
and their proofs in [13] led us to discover an interesting result about the number
of distinct 5-regular partitions of n. Theorem 1.1 proves the cases k = 1 , 2, 3
of Conjecture 4.3 in [14] which concerns the non-negativity of the c oeﬃcients of
a certain truncated theta function. The theorem gives inequalities involving the
number of partitions of n with parts congruent to ±S mod R and it also leads to
results involving the generalizations of the minimal excludant statist ic for partitions.
At the end of [14], Merca made another conjecture about the non- negativity of
the coeﬃcients of a truncated series. Suppose R ≥ 2 and 1 ≤S <R and deﬁne
T±(q,k,S,R ) := 1
(qS,q R−S;qR)∞
∞∑
n=k
qn(3n∓1)R/2±3nS(1 −qS±nR).
Conjecture 6.15 on [14] states that, for all k ≥ 1, each ofT+(q,k,S,R ), −T−(q,k,S,R ),
and T−(q,k,S,R ) +T+(q,k,S,R ) has non-negative coeﬃcients. We establish the
ﬁrst two parts of the conjecture.
Theorem 7.1. For 1 ≤S <R and k ≥ 1,
(i) T+(q,k,S,R ) has non-negative coeﬃcients;
(ii) T−(q,k,S,R ) has non-positive coeﬃcients.
Proof. Let 1 ≤S <R and k ≥ 1.
To show that for the q-series T+(q,k,S,R ) has non-negative coeﬃcients, we
rewrite it as
T+(q,k,S,R )
= 1
(qS,q R−S;qR)∞
∞∑
n=k
qn(3n−1)R/2+3nS(1 −qn(R−S) +qn(R−S) −qS+nR)
= 1
(qS,q 2R−S;qR)∞
∞∑
n=k
qn(3n−1)R/2+3nS 1 −qn(R−S)
1 −qR−S
+ 1
(qS+R,q R−S;qR)∞
∞∑
n=k
qn(3n−1)R/2+3nS+nR−nS 1 −q(n+1)S
1 −qS
= 1
(qS,q 2R−S;qR)∞
∞∑
n=k
qn(3n−1)R/2+3nS(1 +qR−S +q2(R−S) + · · · +q(n−1)(R−S))
+ 1
(qS+R,q R−S;qR)∞
∞∑
n=k
qn(3n+1)R/2+2nS(1 +qS +q2S + · · · +qnS).
Clearly, this q-series has non-negative coeﬃcients.
If k ≥ 2, we rewrite
−T−(q,k,S,R )
= − 1
(qS,q R−S;qR)∞
∞∑
n=k
qn(3n+1)R/2−3nS(1 −qS−nR)
TRUNCATED THETA SERIES RELATED TO THE JTP IDENTITY 19
= 1
(qS,q R−S;qR)∞
∞∑
n=k
qn(3n+1)R/2−3nS+S−nR(1 −qn(R−S) +qn(R−S) −qnR−S)
= 1
(qS,q 2R−S;qR)∞
∞∑
n=k
qn(3n+1)R/2−3nS+S−nR 1 −qn(R−S)
1 −qR−S
+ 1
(qS+R,q R−S;qR)∞
∞∑
n=k
qn(3n+1)R/2−3nS+S−nR+nR−nS 1 −q(n−1)S
1 −qS
= 1
(qS,q 2R−S;qR)∞
∞∑
n=k
qn(3n−1)R/2−3nS+S(1 +qR−S +q2(R−S) + · · · +q(n−1)(R−S))
+ 1
(qS+R,q R−S;qR)∞
∞∑
n=k
qn(3n+1)R/2−4nS+S(1 +qS +q2S + · · · +q(n−2)S).
If k = 1, we have
−T−(q, 1,S,R ) = qR−2S
(qS,q 2R−S;qR)∞
−T−(q, 2,S,R ).
Clearly, in each case −T−(q, 1,S,R ) has non-negative coeﬃcients. □
Finally, we note that results of a similar ﬂavor appear in [15]. Let g(n) =
|P±1,5(n)| (respectively h(n) = |P±2,5(n)|) be the number of partitions of n into
parts congruent to ±1 mod 5 (respectively ±2 mod 5). If ξ(n) is either of g(n) or
h(n), Merca [15, Corollary 3.3] proves the following families of linear homog eneous
inequalities. For k ≥ 1, S ∈ {1, 2}, and n ≥ 0
(26)
u±
ξ,S (n) := ±
∞∑
j=k
(ξ (n − 5j(3j ± 1)/2 ± 3jS ) −ξ (n − 5j(3j ± 1)/2 ∓ (3j ± 1)S)) ≥ 0
and asks for combinatorial interpretations of these sums. The re quested interpre-
tations can be read oﬀ the generating functions obtained in the pro ofs in [15].
In the proof of [15, Theorem 2.1] (with R = 5,S = 1) it is shown that
∞∑
n=0
u+
g,1(n)qn = 1
(q6,q 4;q5)∞
∞∑
j=k
q5j(3j+1)/2−3j (
1 +q +q2 + · · · +q6j)
.
Now, 1
(q6,q 4;q5)∞
is the generating function for the number of partitions λ ∈
P±1,5(n) of n with no part equal to 1. We can interpret q5j(3j+1)/2−3j as generating
a single partition (5 j + 1)j ∪δ1,5,j.
Then
u+
g,1(n) = |{(λ, (5j + 1)j ∪δ1,5,j) ⊢n |λ ∈ P ±1,5,m λ(1) ≤ 6j,j ≥k}|.
In a similar way we can show that
u+
h,2(n) = |{(λ, (5(j − 1) + 2)j ∪δ2,5,j) ⊢n |λ ∈ P ±2,5,m λ(2) ≤ 6j,j ≥k}|
u−
g,1(n) = |{(λ, (5j + 1)j−1 ∪δ1,5,j ∪ (4)) ⊢n |λ ∈ P ±1,5,m λ(1) ≤ 6j − 2,j ≥k}|
u−
h,2(n) = |{(λ, (5(j − 1) + 2)j−1 ∪δ2,5,j ∪ (3)) ⊢n |λ ∈ P ±2,5,m λ(2) ≤ 6j − 2,j ≥k}|.
20 CRISTINA BALLANTINE AND BROOKE FEIGON
Using the generating functions in [15, Corollary 3.2], we have
u+
g,2(n) = |{(λ, (δ4,5,2j−1 \δ4,5,j−1)) ⊢n |λ ∈ P ±1,5,m λ(1) ≤ 12j + 1,j ≥k}|
u−
g,2(n) = |{(λ, (δ4,5,2j−2 \δ4,5,j−1) ∪ (5(j − 1) + 1)) ⊢n |λ ∈ P ±1,5,m λ(1) ≤ 12j − 3,j ≥k}|
u+
h,1(n) = |{(λ, (δ2,5,2j \δ2,5,j)) ⊢n |λ ∈ P ±2,5,m λ(2) ≤ 3j − 2,j ≥k}|
+ |{(λ, (δ3,5,2j+1 \δ3,5,j+2) ∪ (5j + 3)) ⊢n |λ ∈ P ±2,5,m λ(3) = 1,j ≥k}|
u−
h,1(n) = |{(λ, (δ2,5,2j−1 \δ2,5,j) ∪ (5(j − 1) + 3)) ⊢n |λ ∈ P ±2,5,m λ(2) ≤ 3j − 3,j ≥k}|
+ |{(λ, (δ3,5,2j \δ3,5,j+1) ∪ (5(j − 1) + 2)) ⊢n |λ ∈ P ±2,5,m λ(3) = 1,j ≥k}|.
