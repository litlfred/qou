---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-014-44-verifying-the-assumption-of-the-poisson-summa
section_title: "Verifying the assumption of the Poisson summation formula"
section_number: 4.4
pages: 35-37
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Verifying the assumption of the Poisson summation formula
In this section, we verify the assumption of the Poisson summation formula in Lemma 4.3,
which is used in the proof of Theorem 1.1 for the 62 knot in Section 4.1. As we mentioned
in Remark 2.5, we verify the assumption for ˆV (t, s, u) instead of V (t, s, u), since V (t, s, u)
converges uniformly to ˆV (t, s, u) on ∆′ in the form mentioned in Remark 2.5.
By computer calculation, we can see that the maximal value of Re ˆV −ςR is about
0.06. Therefore, in the proof of Lemma 4.3, it is suﬃcient to decrease, say, Re ˆV (t, s, u +
δ√−1) −2πδ by 0.06, by moving δ (though we do not use this value in the proof of the
lemma).
Lemma 4.3. ˆV (t, s, u) −ςR satisﬁes the assumption of Proposition 2.3.
Proof. We show that ∂∆′ is null-homotopic in each of (15)–(20).
As for (15) and (16), similarly as the proof of Lemma 3.4, it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t + δ
√
−1, s, u)
)
< 2π −ε′
(65)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t + δ
√
−1, s, u)
)
= −2 Arg (1 −x) + Arg
(
1 −y
x
)
+ 2π
(
t −1
2
)
,
where x = e2π√−1 (t+X√−1) and y/x = e−2π√−1 (t−s)e2π(X−Y ). Since 0.6 ≤t ≤0.9,
0 < Arg (1 −x) < 2π
(
t −1
2
)
.
Hence,
−2π
(
t −1
2
)
< −2 Arg (1 −x) + 2π
(
t −1
2
)
< 2π
(
t −1
2
)
.
Further,
min
{
0, −2π
(
t −s −1
2
)}
< Arg
(
1 −y
x
)
< max
{
2π
(1
2 −t + s
)
, 0
}
.
Therefore,
min
{
−2π
(
t−1
2
)
, −2π
(
2t−s−1
)}
< Re
( ∂
∂δ
ˆV (t+δ
√
−1, s, u)
)
< max
{
2π·s, 2π
(
t−1
2
)}
.
35
Since t ≤0.9, t + (t −s) ≤0.9 + 0.67 = 1.57 and s ≤0.4,
−2π · 0.6 < Re
( ∂
∂δ
ˆV (t + δ
√
−1, s, u)
)
< 2π · 0.4,
and hence, (65) is satisﬁed.
As for (17) and (18), similarly as above, it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π −ε′
(66)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
= 2 Arg (1 −y) −Arg
(
1 −y
x
)
−2π(2s + u −1),
where y = e2π√−1 (s+Y √−1) and y/x = e−2π√−1 (t−s)e2π(X−Y ). Since 0.14 ≤s ≤0.4,
−2π
(1
2 −s
)
< Arg (1 −y) < 0.
Hence,
−2π · u < 2 Arg (1 −y) −2π(2s + u −1) < 2π(1 −2s −u).
Since u ≤0.4 and 2s + u ≥0.33,
−2π · 0.4 < 2 Arg (1 −y) −2π(2s + u −1) < 2π · 0.67.
Further,
min
{
0, −2π
(
t −s −1
2
)}
< Arg
(
1 −y
x
)
< max
{
2π
(1
2 −t + s
)
, 0
}
.
Since 0.3 ≤t −s ≤0.67,
−2π · 0.17 < Arg
(
1 −y
x
)
< 2π · 0.2.
Therefore,
−2π · 0.57 < Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π · 0.87,
and hence, (66) is satisﬁed.
As for (19) and (20), similarly as above, it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π −ε′
(67)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
= Arg (1 −z) −2π
(
s + u −1
2
)
,
36
where z = e2π√−1 (u+Z√−1). Since 0.05 ≤u ≤0.4,
−2π
(1
2 −u
)
< Arg (1 −z) < 0.
Therefore,
−2π · s < Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π
(1
2 −s −u
)
.
Since s ≤0.4 and s + u ≥0.19,
−2π · 0.4 < Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π · 0.31,
and hence, (67) is satisﬁed.
