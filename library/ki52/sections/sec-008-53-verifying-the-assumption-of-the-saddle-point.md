---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-008-53-verifying-the-assumption-of-the-saddle-point
section_title: "Verifying the assumption of the saddle point method"
section_number: 5.3
pages: 36-39
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Verifying the assumption of the saddle point method
In this section, in Lemma 5.7, we verify the assumption of the saddle point method
(Proposition 3.5, see also Remark 3.6 and Appendix B) when we apply Proposition 3.5
and Remark 3.6 to (46). The arguments of this section are due to Yokota [44].
Let V (t, s) and ˆV (t, s) be as in Section 2.2. As shown in Appendix B, V (t, s) uniformly
converges to ˆV (t, s) on ∆′ as N →∞. Hence, as mentioned in Remarks 3.3 and 3.6
and Appendix B, the saddle point method of the problem can be reduced to the saddle
point method of an integral of the form
∫
ϕ(t, s) eN ˆV (t,s)dt ds. Therefore, we verify the
assumption of the saddle point method for ˆV (t, s). We recall that the diﬀerentials of
ˆV (t, s) are given in (47).
In order to show Lemma 5.7 below, we calculate the behavior of the following function,
ft,s(δ1, δ2) = Re ˆV (t + δ1
√
−1, s + δ2
√
−1) −ςR .
The diﬀerentials of this function are given by
∂
∂δ1
ft,s(δ1, δ2) = Re
(√
−1 ∂
∂t
ˆV (t + δ1
√
−1, s + δ2
√
−1)
)
= −Im
(
−log
(
1 −1
x
)
−2π
√
−1
(
t + s −1
2
))
= Arg
(
1 −1
x
)
+ 2π
(
t + s −1
2
)
,
(58)
∂
∂δ2
ft,s(δ1, δ2) = Re
(√
−1 ∂
∂s
ˆV (t + δ1
√
−1, s + δ2
√
−1)
)
= −Im
(
−2 log
(
1 −1
y
)
−2π
√
−1 (t + 2s −1)
)
= 2
(
Arg
(
1 −1
y
)
+ 2π
(1
2t + s −1
2
))
,
(59)
where x = e2π√−1 (t+δ1
√−1) and y = e2π√−1 (s+δ2
√−1).
Lemma 5.5 (Yokota [44]). Fixing (t, s) ∈∆′ and δ2 ∈R, we regard ft,s(X, δ2) as a
function of X ∈R.
(1) If t + s ≥1
2, then ft,s(X, δ2) is monotonically increasing for X ∈R.
(2) If t + s < 1
2, then ft,s(X, δ2) has a unique minimal point at X = g1(t, s), where
g1(t, s) =
1
2π log sin 2π(t + s)
sin 2πs
,
i.e., ft,s(X, δ2) is monotonically decreasing for X < g1(t, s), and is monotonically increas-
ing for X > g1(t, s).
Proof. We put x = e2π√−1 (t+X√−1). Then, 1/x = e2πXe−2π√−1 t. We put θ = Arg (1 −1
x)
in this proof. Since t < 1
2, θ is in the following range,
0 < θ < 2π
(1
2 −t
)
.
36
When t + s ≥1
2, we show the lemma, as follows. By (58),
∂
∂X ft,s(X, δ2) = θ + 2π
(
t + s −1
2
)
> 0.
Therefore, ft,s(X, δ2) is monotonically increasing, and (1) holds.
When t + s < 1
2, we show the lemma, as follows. In this case, by (58),
∂
∂X ft,s(X, δ2)





> 0
if θ > 2π(1
2 −t −s),
= 0
if θ = 2π(1
2 −t −s),
< 0
if θ < 2π(1
2 −t −s).
Further, θ and X are related as shown in the following picture.
1
0
1
2πt
θ
e2πX
1/x
Hence, X is monotonically increasing as a function of θ, and they satisfy that
e2πX
sin θ =
1
sin(π −2πt −θ) .
This is rewritten,
X =
1
2π log
sin θ
sin(π −2πt −θ) .
Therefore,
∂
∂X ft,s(X, δ2)





> 0
if X > g1(t, s),
= 0
if X = g1(t, s),
< 0
if X < g1(t, s),
where we put
g1(t, s) =
1
2π log sin 2π(1
2 −t −s)
sin 2πs
=
1
2π log sin 2π(t + s)
sin 2πs
.
Hence, (2) holds.
Lemma 5.6 (Yokota [44]). Fixing (t, s) ∈∆′ and δ1 ∈R, we regard ft,s(δ1, Y ) as a
function of Y ∈R.
(1) If t + 2s ≥1, then ft,s(δ1, Y ) is monotonically increasing for Y ∈R.
(2) If t + 2s < 1, then ft,s(δ1, Y ) has a unique minimal point at Y = g2(t, s), where
g2(t, s) =
1
2π log sin π(t + 2s)
sin πt
,
i.e., ft,s(δ1, Y ) is monotonically decreasing for Y < g2(t, s), and is monotonically increas-
ing for Y > g2(t, s).
37
Proof. We put y = e2π√−1 (s+Y √−1). Then, 1/y = e2πY e−2π√−1 s. We put θ = Arg (1 −1
y)
in this proof. Since s < 1
2, θ is in the following range,
0 < θ < 2π
(1
2 −s
)
.
When t + 2s ≥1, we show the lemma, as follows. By (59),
∂
∂Y ft,s(δ1, Y ) = 2
(
θ + π
(
t + 2s −1
))
> 0.
Hence, ft,s(δ1, Y ) is monotonically increasing, and (1) holds.
When t + 2s < 1, we show the lemma, as follows. In this case, by (59),
∂
∂Y ft,s(δ1, Y )





> 0
if θ > 2π(1
2 −1
2t −s),
= 0
if θ = 2π(1
2 −1
2t −s),
< 0
if θ < 2π(1
2 −1
2t −s).
Further, similarly as in the proof of Lemma 5.5, θ and Y are related by
Y
=
1
2π log
sin θ
sin(π −2πs −θ) .
Since Y is monotonically increasing as a function of θ,
∂
∂Y ft,s(δ1, Y )





> 0
if Y > g2(t, s),
= 0
if Y = g2(t, s),
< 0
if Y < g2(t, s),
where we put
g2(t, s) =
1
2π log
sin 2π(1
2 −1
2t −s)
sin
(
π −2πs −2π(1
2 −1
2t −s)
) =
1
2π log sin π(t + 2s)
sin πt
.
Hence, we obtain the lemma.
Lemma 5.7 (Yokota [44]). When we apply Proposition 3.5 (saddle point method) to (46),
the assumption of Proposition 3.5 holds.
Proof. We show that there exists a homotopy ∆′
δ (0 ≤δ ≤1) between ∆′
0 = ∆′ and ∆′
1
such that
(tc, sc) ∈∆′
1,
(60)
∆′
1 −{(tc, sc)} ⊂
{
(t, s) ∈C2 

 Re ˆV (t, s) < ςR
}
,
(61)
∂∆′
δ ⊂
{
(t, s) ∈C2 

 Re ˆV (t, s) < ςR
}
.
(62)
For a suﬃciently large R > 0, we put
ˆg1(t, s) =
{
max {−R, g1(t, s)}
if t + s < 1
2,
−R
if t + s ≥1
2,
38
ˆg2(t, s) =
{
max {−R, g2(t, s)}
if t + 2s < 1,
−R
if t + 2s ≥1.
We note that, since g1(t, s) →−∞as t+s →1
2, ˆg1(t, s) is continuous, and similarly, since
g2(t, s) →−∞as t + 2s →1, ˆg2(t, s) is continuous. We put
∆′
δ =
{(
t + δ · ˆg1(t, s)
√
−1, s + δ · ˆg2(t, s)
√
−1
)
∈C2 

 (t, s) ∈∆′}
.
We show (62), as follows. From the deﬁnition of ∆′,
∂∆′ ⊂
{
(t, s) ∈C2 

 Re ˆV (t, s) < ςR
}
.
Further, by Lemmas 5.5 and 5.6,
Re ˆV
(
t + δ · ˆg1(t, s)
√
−1, s + δ · ˆg2(t, s)
√
−1
)
≤ˆV (t, s)
for any δ ∈[0, 1] and any (t, s) ∈∆′. Hence, (62) holds.
We show (60) and (61), as follows. Consider the following functions
F(t, s, X, Y ) = Re ˆV
(
t + X
√
−1, s + Y
√
−1
)
,
h(t, s) = F
(
t, s, ˆg1(t, s), ˆg2(t, s)
)
.
When t + 2s ≥1, −h(t, s) is suﬃciently large (because we let R be suﬃciently large),
and (61) holds in this case. When t + 2s < 1, it is shown from the deﬁnitions of g1(t, s)
and g2(t, s) that
∂F
∂X = 0 at X = g1(t, s) and ∂F
∂Y = 0 at Y = g2(t, s). Hence, Im ∂ˆV
∂t =
Im ∂ˆV
∂s = 0 at
(
t + g1(t, s)√−1, s + g2(t, s)√−1
)
. Further, ∂h
∂t = Re ∂ˆV
∂t and ∂h
∂s = Re ∂ˆV
∂s
at
(
t + g1(t, s)√−1, s + g2(t, s)√−1
)
. Therefore, when (t, s) is a critial point of h(t, s),
(
t + g1(t, s)√−1, s + g2(t, s)√−1
)
is a critical point of ˆV . It follows that h(t, s) has a
unique maximal point at (t, s) = (Re tc, Re sc). Therefore, (60) and (61) hold.
