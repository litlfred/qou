---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-019-54-verifying-the-assumption-of-the-poisson-summa
section_title: "Verifying the assumption of the Poisson summation formula"
section_number: 5.4
pages: 52-53
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Verifying the assumption of the Poisson summation formula
In this section, we verify the assumption of the Poisson summation formula in Lemma 5.2,
which is used in the proof of Theorem 1.1 for the 63 knot in Section 5.1. As we mentioned
in Remark 2.5, we verify the assumption for ˆV (t, s, u) instead of V (t, s, u), since V (t, s, u)
converges uniformly to ˆV (t, s, u) on ∆′ in the form mentioned in Remark 2.5.
By computer calculation, we can see that the maximal value of Re ˆV −ς is about
0.02. Therefore, in the proof of Lemma 5.2, it is suﬃcient to decrease, say, Re ˆV (t, s, u +
δ√−1) −2πδ by 0.02, by moving δ (though we do not use this value in the proof of the
lemma).
Lemma 5.2. ˆV (t, s, u) −ς satisﬁes the assumption of Proposition 2.3.
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
(89)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t + δ
√
−1, s, u)
)
= 2 Arg (1 −x) −Arg
(
1 −x
y
)
−2π
(
t −1
2
)
,
where x = e2π√−1(t+δ√−1). Since 0.18 ≤t ≤0.3,
−2π
(1
2 −t
)
< Arg (1 −x) < 0.
Further, since 0.3 ≤s −t ≤0.47,
0 < Arg
(
1 −x
y
)
< 2π
(1
2 −s + t
)
.
Therefore,
−2π(1 −s) < Re
( ∂
∂δ
ˆV (t + δ
√
−1, s, u)
)
< 2π
(1
2 −t
)
.
Since s ≥0.54 and t ≥0.18,
−2π · 0.46 < Re
( ∂
∂δ
ˆV (t + δ
√
−1, s, u)
)
< 2π · 0.32,
and hence, (89) is satisﬁed.
As for (17) and (18), similarly as above, it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π −ε′
(90)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
= −2 Arg (1 −y) + Arg
(
1 −x
y
)
+ Arg
(
1 −y
z
)
+ 2π
(
s −1
2
)
52
where y = e2π√−1(s+δ√−1). Since 0.54 ≤s ≤0.7,
0 < Arg (1 −y) < 2π
(
s −1
2
)
.
Further, since 0.3 ≤s −t ≤0.47,
0 < Arg
(
1 −x
y
)
< 2π
(1
2 −s + t
)
.
Furthermore, since 0.3 ≤s −u ≤0.47,
−2π
(1
2 −s + u
)
< Arg
(
1 −y
z
)
< 0.
Therefore,
−2π · u < Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π · t.
Since u ≤0.3 and t ≤0.3,
−2π · 0.3 < Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π · 0.3,
and hence, (90) is satisﬁed.
As for (19) and (20), similarly as above, it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π −ε′
for some ε′ > 0. We obtain this formula from (89) by the symmetry (87).
