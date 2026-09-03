---
doc_id: arxiv-math-0701051v4
doc_title: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA"
section_id: sec-014-52-error-term-for-balanced-young-diagrams
section_title: "Error term for balanced Young diagrams"
section_number: 5.2
pages: 16-17
source_pdf: 0701051v4.pdf
source_sha256: 4592a048c3b84a8d
doc_brief: "ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS RELATED TO STANLEY CHARACTER FORMULA — We prove an upper bound for characters of the symmetric groups."
---
that if the permutation π is ﬁxed, its non-trivial cycle lengths are equal to
k1, . . . , kr ≥ 2, and the Young diagram λ is balanced (i.e. r(λ), c(λ) =
O(√n)) then
χλ(π) = 1
(n)| supp(π)|
r∏
i=1
Rki+1(λ) + O
(
n− |π |+2
2
)
.
The following theorem gives a uniform estimate for the error term in
Biane’s formula (note that if π is ﬁxed and the Young diagram balanced,
with ε = C√n and A = D √n we recover the result of Biane).
Theorem 16. There exists a constant a such that, for any 0 < ε < 1,
any Young diagram λ of size n and any permutation π ∈ Sn such that
| supp(π)|2 ≤ εA and r(λ), c(λ) ≤ A ≤ n we have:⏐
⏐
⏐
⏐
⏐χλ(π) − 1
(n)| supp(π)|
r∏
i=1
Rki+1(λ)
⏐
⏐
⏐
⏐
⏐ ≤
(
ε2 + A
n ε
)( aA
n
) |π|
,
where the ki are the lengths of the non-trivial cycles of π.
Proof. We can assume that π ∈ Sl has no ﬁxpoints. Using Theorem 2 and
Theorem 9 together with the fact that any minimal factorisat ion of π is a
product of minimal factorisations of its cycles, we can write:
Σ λ(π) −
r∏
i=1
Rλ
ki+1 =
∑
σ1,σ2∈Sl
σ1σ2=π
|σ1|+|σ2|>|π|
(−1)|σ1|N λ(σ1, σ2).
To such a pair (σ1, σ2) of permutations we can associate one of the pairs of
permutations (σ′
1, σ′
2) given by Lemma 13 with |σ′
1| ≥ 1.
ASYMPTOTICS OF CHARACTERS OF SYMMETRIC GROUPS 17
Consider separately the case|σ′
1| = 1. Then orbits(σ1, σ2) = orbits( σ′
1, σ′
2) ≥
|C(π)| − 1 and the ﬁrst inequality in (18) shows that
N λ(σ1, σ2) ≤ A|C(σ1)|+|C(σ2)|
( n
A2
) |C(π)|−1
therefore the estimate given by Proposition 12 can be improv ed to the fol-
lowing one:
N λ(σ1, σ2) ≤ Al−|C(π)|n|C(π)| 1
n.
Clearly A ≥ l therefore by the same argument as in the proof of Theorem
1, we obtain the inequality
⏐
⏐
⏐
⏐
⏐Σ λ(π) −
r∏
i=1
Rki+1(λ)
⏐
⏐
⏐
⏐
⏐ ≤ 4lAl−rnr
(
l2
n +
∑
i≥2
l2i
Aii!
)
.
The proof is now ﬁnished thanks to the remarks of the previous subsection
and the inequality exp(z) − 1 − z ≤ z2 for 0 < z < 1. □
