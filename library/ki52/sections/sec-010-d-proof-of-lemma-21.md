---
doc_id: ki52
doc_title: "On the asymptotic expansion of the Kashaev invariant of the 5 2 knot Tomotada Ohtsuki Introduction"
section_id: sec-010-d-proof-of-lemma-21
section_title: "Proof of Lemma 2.1"
section_number: D
pages: 48-49
source_pdf: ki52.pdf
source_sha256: 35ad4ee5a00d4a18
toc_source: inferred
doc_brief: "On the asymptotic expansion of the Kashaev invariant of the 5_2 knot — We give a presentation of the asymptotic expansion of the Kas haev invariant of the52 knot."
duplicate_of: "104171-qt-83"
---
Proof of Lemma 2.1
In this appendix, we give a proof of Lemma 2.1.
Proof of Lemma 2.1. We put
Λ(t) = Re
(
1
2π√−1 Li2(e2π√−1 t)
)
for t ∈R. We note that this function has period 1, and Λ(−t) = −Λ(t). Since
Λ′(t) = −log
(
2 sin πt
)
for 0 < t < 1, the behavior of Λ(t) is as follows.
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
Λ( 1
6)
→
0
→
−Λ(1
6)
→
0
Here, Λ( 1
6) = 0.161533... . See Figure 6 for the graph of Λ(t).
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
Figure 6: The graph of Λ(t) for 0 ≤t ≤1
We consider the following domain,
{
(t, s) ∈R2 

 Re ˆV (t, s) ≥ςR
}
.
(79)
48
For t, s ∈R,
Re ˆV (t, s) = −Λ(−t) −2 Λ(−s) = Λ(t) + 2 Λ(s).
Since 2Λ(1
6) −ςR = −0.127043... < 0, the values of Λ(t) and Λ(s) must be positive when
(t, s) is in the domain (79). Hence, the domain (79) is included in the following area,
{
(t, s) ∈R2 

 0 ≤t ≤0.5,
0 ≤s ≤0.5
}
.
We assume that 0 ≤t ≤0.5 and 0 ≤s ≤0.5 in the following of this proof.
We consider the minimal value tmin of t such that (t, s) is in the domain (79). It satisﬁes
that Λ(tmin) + 2Λ(1
6) = ςR. Since Λ(0.04) + 2Λ(1
6) −ςR = −0.031768... < 0, we have that
0.04 < tmin. Hence, the domain (11) is included in the area 0.04 ≤t for some suﬃciently
small ε > 0. Further, in similar ways, we can show that the domain (11) is included in
the area
{
(t, s) ∈R2 

 0.04 ≤t ≤0.4,
0.05 ≤s ≤0.4
}
for some suﬃciently small ε > 0. We assume that (t, s) is in the above area in the following
of this proof.
By expanding Λ(t) at t = 0.3, we can show that
Λ(t) ≤Λ(0.3) + Λ′(0.3)(t −0.3).
If (t, s) is in the domain (79),
ςR ≤Λ(t) + 2Λ(s) ≤Λ(0.3) + Λ′(0.3)(t −0.3) + 2
(
Λ(0.3) + Λ′(0.3)(s −0.3)
)
.
Hence,
t + 2s ≤ςR −3Λ(0.3)
Λ′(0.3)
+ 0.9.
Further, since t ≤0.4,
t + s ≤1
2
(ςR −3Λ(0.3)
Λ′(0.3)
+ 1.3
)
= 0.571668... < 0.6.
Therefore, the domain (11) is included in ∆′ for some suﬃciently small ε > 0, as required.
