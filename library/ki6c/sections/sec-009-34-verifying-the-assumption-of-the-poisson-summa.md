---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings"
section_id: sec-009-34-verifying-the-assumption-of-the-poisson-summa
section_title: "Verifying the assumption of the Poisson summation formula"
section_number: 3.4
pages: 20-22
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
doc_brief: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings — We give presentations of the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings."
---
Verifying the assumption of the Poisson summation formula
In this section, we verify the assumption of the Poisson summation formula in Lemma 3.4,
which is used in the proof of Theorem 1.1 for the 61 knot in Section 3.1. As we mentioned
in Remark 2.5, we verify the assumption for ˆV (t, s, u) instead of V (t, s, u), since V (t, s, u)
converges uniformly to ˆV (t, s, u) on ∆′ in the form mentioned in Remark 2.5.
Re ˆV (t, s, u) has a unique maximal point in ∆′ at
x0 = y0 = y0 = eπ√−1/3,
t0 = s0 = u0 = 1
6,
and its maximal value is 0.646131... . Hence,
Re ˆV (t, s, u) −ςR ≤0.142571...
(43)
for any (t, s, u) ∈∆′. Therefore, in the proof of Lemma 3.4, it is suﬃcient to decrease,
say, Re ˆV (t, s, u + δ√−1) −2πδ by this value, by moving δ (though we do not use this
value in the proof of the lemma).
Lemma 3.4. ˆV (t, s, u) −ςR satisﬁes the assumption of Proposition 2.3.
Proof. We show that ∂∆′ is null-homotopic in each of (17)–(20), (24) and (25).
As for (19), we show that we can move ∆′ into the following domain,
{
(t, s, u + δ
√
−1) ∈C3 

 (t, s, u) ∈∆′, δ ≥0, Re ˆV (t, s, u + δ
√
−1) −ςR −2πδ < 0
}
.
Hence, putting
F(δ) = Re ˆV (t, s, u + δ
√
−1) −ςR −2πδ,
it is suﬃcient to show that there exists δ0 > 0 such that
F(δ0) < 0
for any (t, s, u) ∈∆′, and
F(δ) < 0
for any (t, s, u) ∈∂∆′ and δ ∈[0, δ0].
(44)
Therefore, it is suﬃcient to show that
d
dδ F(δ) =
∂
∂δ Re ˆV (t, s, u + δ
√
−1) −ςR −2π < −ε′,
for some ε′ > 0 (because, if the above formula holds, then (44) holds for a suﬃciently
large δ0). Hence, it is suﬃcient to show that
Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π −ε′.
Further, as for (20), similarly as above, it is suﬃcient to show that
Re
( ∂
∂δ
ˆV (t, s, u −δ
√
−1)
)
< 2π −ε′
for some ε′ > 0.
20
Hence, as for (19) and (20), it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π −ε′
(45)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
= Re
(√
−1 · ∂
∂u
ˆV (t, s, u + δ
√
−1)
)
= −Im
(
−log(1 −z) + 2π
√
−1
(
t + s + u −1
2
))
= Arg (1 −z) −2π
(
t + s + u −1
2
)
,
where z = e2π√−1 u. Since 0 < u ≤1
2,
−2π
(1
2 −u
)
< Arg (1 −z) < 0.
Hence,
−2π(t + s) < Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π
(1
2 −t −s −u
)
.
Therefore, since t + s ≤0.4 + 0.5 = 0.9 and t, s, u ≥0,
−2π · 0.9 < Re
( ∂
∂δ
ˆV (t, s, u + δ
√
−1)
)
< 2π · 0.5,
and hence, (45) is satisﬁed.
As for (17) and (18), similarly as above, it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π −ε′
(46)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
= Arg (1 −y) −2π
(
2t + 2s + u −1
)
,
where y = e2π√−1 s. Since 0 < s ≤1
2,
−2π
(1
2 −s
)
< Arg (1 −y) < 0.
Hence,
−2π
(
2t + s + u −1
2
)
< Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π(1 −2t −2s −u).
Therefore, since t + (t + s + u) ≤0.4 + 0.94 = 1.34 and t ≥0.03, s, u ≥0,
−2π · 0.84 < Re
( ∂
∂δ
ˆV (t, s + δ
√
−1, u)
)
< 2π · 0.94,
21
and hence, (46) is satisﬁed.
As for (24) and (25), similarly as above, it is suﬃcient to show that
−(2π −ε′) < Re
( ∂
∂δ
ˆV (t + δ
√
−1, s −δ
√
−1, u)
)
< 2π −ε′
(47)
for some ε′ > 0. The middle term is calculated as
Re
( ∂
∂δ
ˆV (t + δ
√
−1, s −δ
√
−1, u)
)
= 2 Arg (1 −x) −Arg (1 −y) −2π
(
t −1
2
)
,
where x = e2π√−1 t. Since 0 < t ≤1
2,
−2π
(1
2 −t
)
< Arg (1 −x) < 0.
Further, since Arg (1 −y) is in the range mentioned above,
−2π
(1
2 −t
)
< Re
( ∂
∂δ
ˆV (t + δ
√
−1, s −δ
√
−1, u)
)
< 2π
(
1 −t −s
)
.
Therefore, since t ≥0.03 and s ≥0,
−2π · 0.5 < Re
( ∂
∂δ
ˆV (t + δ
√
−1, s −δ
√
−1, u)
)
< 2π · 0.97,
and hence, (47) is satisﬁed.
