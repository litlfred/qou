---
doc_id: arxiv-math-0108215v1
doc_title: "Möbius Energy of Thick Knots Eric J. Rawdon 2"
section_id: sec-016-3-for-1-j-n-we-claim-x-y-2-j-1δ-for-all-y-wj-exc
section_title: "For 1 ≤ j ≤ n, we claim |x − y| > 2 + ( j − 1)δ for all y ∈ Wj, except"
section_number: 3
pages: 12-14
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
doc_brief: "Möbius Energy of Thick Knots Eric J. Rawdon 2 — The M¨ obius energy of a knot is an energy functional for smoot h curves based on an idea of self-repelling."
---
perhaps a set of measure 0. Suppose M is a non-zero measure subset of W1
such that for all y ∈ M, we have |x − y| ≤ 2. Then W0 ∪ M ⊆ Y [2] and
ℓ[2] ≥ µ(W0) + µ(M) > µ (W0) = ℓ∗[2], which contradicts (9). We continue
using induction. Suppose for all 0 ≤ k < j ≤ n, we have |x − y| > 2 + (k − 1)δ.
Suppose M is a non-zero measure subset of Wj such that for all y ∈ M, we
have |x − y| ≤ 2 + (j − 1)δ. Then W0 ∪ W1 ∪ · · · ∪Wj−1 ∪ M ⊆ Y [2, 2 + (j − 1)δ].
Thus,
πℓ[2, 2 + (j − 1)δ] ≥ µ(W0) + µ(W1) + · · · + µ(Wj−1) + µ(M)
> µ(W0) + µ(W1) + · · · + µ(Wj−1)
= π ( ℓ∗[2] + ℓ∗(2, 2 + δ] + · · · + ℓ∗(2 + (j − 2)δ, 2 + (j − 1)δ] )
= πℓ∗[2, 2 + (j − 1)δ],
which contradicts (9).
12
Since Ydist = W0 ∪ W1 ∪ · · · ∪ Wn,
I x
dist =
∫
y∈W0
1
|x − y|2 +
∫
y∈W1
1
|x − y|2 + · · · +
∫
y∈Wn
1
|x − y|2
< 1
22 ℓ∗[2] + 1
22 ℓ∗(2, 2 + δ] + · · · + 1
(P − δ)2 ℓ∗(P − δ, P]. (10)
The ﬁrst term of (10) is 104
12 . The rest is
n∑
j=1
1
(2 + (j − 1)δ)2 ℓ∗(2 + (j − 1)δ, 2 + jδ) , which equals
n∑
j=1
1
r2
j
(
4(rj + 1)2∆ r + 4(rj + 1)∆ r2 + 4
3 ∆ r3
)
,
where rj = 2 + ( j − 1)δ and ∆ r = δ. This is a Riemann sum for
∫ P
2
4(r+1)2
r2 dr
plus terms of higher order in ∆ r whose contribution approaches 0 as ∆ r → 0.
The bound (10) holds for all choices of n, so as n → ∞, we get
I x
dist ≤ 104
12 +
∫ P
2
4(r + 1)2
r2 dr
= 8
3 + 4P − 4
P + 8 ln(P ) − 8 ln(2) .
We then multiply by L to get
Edist ≤ L
( 8
3 + 4P − 4
P + 8 ln(P ) − 8 ln(2)
)
. (11)
Combining (5) with (11) yields
EO4(K) ≤ L
( 8
3 + 4P − 4
P + 8 ln(P ) − 8 ln(2)
)
+ 4 . (12)
We substitute P =
(
3
4L − 3π
2 + 1
) 1/ 3
− 1 to obtain our ﬁnal bound.
This bound is messy, but on the order of L4/ 3. We use a computer algebra
system to plot the bound divided by L4/ 3. The ratio achieves its maximum of
≈ 4.5626 near L = 1115. Thus, for all L we have
EO4(K) ≤ 4.57L4/ 3.
✷
For some values of L, in particular as L gets very large, the coeﬃcient 4 .57
can be further reduced. If 104
3 + 2 π < L < 128 or L > 376,000, we have
EO4(K) ≤ 4L4/ 3. As L tends to inﬁnity, the constant decreases to 3
1
3 4
2
3 ≈ 3.63.
13
