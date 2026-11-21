---
doc_id: 0406242v4
doc_title: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction"
section_id: sec-011-7-ruling-out-some-degeneracies
section_title: "Ruling out some degeneracies"
section_number: 7
pages: 19-20
source_pdf: 0406242v4.pdf
source_sha256: 27e48b483007b824
toc_source: outline
doc_brief: "On canonical triangulations of once-punctured torus bundles and two-bridge link complements Introduction — 29 sections: Front matter; Introduction; Conjugacy in SL(2,Z) and the Farey"
---
Ruling out some degeneracies
From now on, we ﬁx (wi) in the compact polyhedron ¯P at a point which maximizes the
total hyperbolic volume of all tetrahedra. To prove that (wi) is critical for the volume
V , we only need to make sure that (wi) lies in the interior P of ¯P, ie that all xi, yi, zi lie
in (0, π).
Proposition 7.1 If for some index i, one of the numbers xi, yi, zi is 0, then two of
them are 0 and the third is π. In other words, there are no simple degeneracies, only
double degeneracies.
Proof If not, consider an afﬁne segment from (wi) to some interior point of P. By
Proposition 6.7, the partial derivative of V at (wi) along that segment is not bounded
above, so V was not maximal at (wi).
Tetrahedra ∆i such that (xi, yi, zi) has one, and therefore two vanishing terms are called
ﬂat, and are characterized by the property that wi is either 0 or π
2 .
Proposition 7.2 (Domino effect) If two consecutive tetrahedra ∆i−1, ∆i are ﬂat, then
∆i+1 is ﬂat, too.
Proof We use only Figure 5 and the deductions recorded in (3). There are three cases:
(1) If i is not a hinge index, ﬂatness of ∆i implies wi−1 + wi+1 ∈{0, π}. By the
range condition 0 ≤w ≤π
2 , this implies wi+1 ∈{0, π
2 }, so ∆i+1 is ﬂat.
(2) If i is a hinge index and wi = π
2 , we must have |wi−1 −wi+1| = π
2 , so by the
range condition, wi+1 is 0 or π
2 , and ∆i+1 is ﬂat.
(3) If i is a hinge index and wi = 0, we have |wi+1 −wi−1| ≤0 so wi+1 = wi−1.
But ∆i−1 is assumed ﬂat, and therefore so is ∆i+1. Note that ﬂatness of ∆i−1
was needed only in this case.
Proposition 7.3 If ∆i is ﬂat, then i is a hinge index and wi = 0.
Geometry & Topology 10 (2006)
1258
Franc¸ois Gu´eritaud and David Futer
Proof In all other cases, the proof of Proposition 7.2 actually forces ∆i+1 to be ﬂat,
which triggers a domino effect: all ∆j’s are ﬂat, and the volume is 0 — certainly not
maximal.
Easy Fact 7.4 If ABC is a Euclidean triangle with positive angles and edge lengths
a, b, c, then
a = b
⇐⇒
bA = bB
⇐⇒
sin bA = sin bB
a < b
⇐⇒
bA < bB
⇐⇒
sin bA < sin bB.
The volume V is still supposed maximal, and we assume that some tetrahedra ∆i are
ﬂat, ie that some hinge parameters wi vanish. Places where a parameter wi vanishes will
be signalled by a vertical bar: . . . LL|RR . . . By Proposition 7.2, consecutive vertical
bars are always separated by at least two letters.
The patterns RL|RL and LR|LR can never occur, because increasing the incriminated
wi to ε would automatically increase the volume (note that wi−1 = wi+1 =: A by the
hinge condition (3)-iii):
Ω
L
R
|
L
R
wi
u
A
0 + ε
A
v
xi
.
u + A −ε
ε
ε + A −v
.
yi
.
−u + A + ε
ε
−ε + A + v
.
zi
.
π −2A
π −2ε
π −2A
.
This implies
exp −∂V
∂ε

ε=0 = 1
4 · sin(A −u)
sin(A + u)
sin(A −v)
sin(A + v) < 1
where we used 7.4, Proposition 6.1 and Proposition 6.8 (with λ = 0).
Any vertical bar thus lives next to at least two consecutive identical letters (on at least one
side). However, the patterns R|LL|R and L|RR|L are also prohibited by Proposition 7.3,
since the central (nonhinge) tetrahedron would have one vanishing angle (a + c = 0 in
the notations of Figure 5).
