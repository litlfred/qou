---
doc_id: ki6c
doc_title: "On the asymptotic expansions of the Kashaev invariant of the knots with 6 crossings Tomotada Ohtsuki and Yoshiyuki Yokota Introduction"
section_id: sec-002-22-some-behaviors-of-the-dilogarithm-function
section_title: "Some behaviors of the dilogarithm function"
section_number: 2.2
pages: 6-7
source_pdf: ki6c.pdf
source_sha256: b13a73517b349654
toc_source: inferred
---
In this section, we show some behaviors of the dilogarithm function.
We put
Λ(t) = Re
(
1
2π√−1 Li2(e2π√−1 t)
)
.
Since
Λ′(t) = −log 2 sin πt,
Λ′′(t) = −π cot πt,
the behavior of Λ(t) is as follows.
t
0
· · ·
1
6
· · ·
1
2
· · ·
5
6
· · ·
1
Λ(t)
0
→
Λ(1
6)
→
0
→
−Λ(1
6)
→
0
Λ′(t)
+
0
−
−
−
0
+
Λ′′(t)
−
−
−
0
+
+
+
Here, Λ( 1
6) = 0.161533... . For the graph of Λ(t), see Figure 1.
0.6
0.2
0.4
0.8
−
−
−
0.05
0.05
0.10
0.10
0.15
0.15
1.0
Figure 1: The graph of Λ(t) for 0 ≤t ≤1
Further, the behavior of Li2
(
e2π√−1 (t+X√−1))
ﬁxing t is presented by the following
lemma.
Lemma 2.2. Let t be a real number with 0 < t < 1. Then, there exists C > 0 such that
({
0
if X ≥0
2π
(
t −1
2
)
X if X < 0
)
−C < Re
(
1
2π√−1 Li2
(
e2π√−1 (t+X√−1)))
<
({
0
if X ≥0
2π
(
t −1
2
)
X if X < 0
)
+ C
for any X ∈R.
Proof. Since
lim
X→∞Re
(
1
2π√−1 Li2
(
e2π√−1 (t+X√−1)))
= Re
(
1
2π√−1 Li2(1)
)
= 0,
the “X ≥0” part of the lemma is satisﬁed.
6
Further, by (7) and (10),
Li2
(
e2π√−1 ˜t)
+ Li2
(
e−2π√−1 ˜t)
= 2π2(˜t2 −˜t + 1
6
)
.
Hence,
Re
1
2π√−1
(
Li2
(
e2π√−1 (t+X√−1))
+ Li2
(
e−2π√−1 (t+X√−1)))
= 2π
(
t −1
2
)
X.
Therefore, we obtain the “X < 0” part of the lemma from the “X ≥0” part.
2.3
