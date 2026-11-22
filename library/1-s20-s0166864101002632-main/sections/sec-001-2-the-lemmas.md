---
doc_id: 1-s20-s0166864101002632-main
doc_title: "PII: S0166-8641(01)00263-2"
section_id: sec-001-2-the-lemmas
section_title: "The lemmas"
section_number: 2
pages: 3-7
source_pdf: 1-s2.0-S0166864101002632-main.pdf
source_sha256: bc5aa8a7663b2a9f
toc_source: inferred
doc_brief: "PII: S0166-8641(01)00263-2 — The Möbius energy of a knot is an energy functional for smooth curves based on an idea of self- repelling."
---
The ﬁrst lemma is a version of a theorem of Schur. This is taken from [10], with the slight
adjustment that we do not need to consider general planar convex curves as the reference
curves, just circles.
Lemma 1. Let K be a C2 smooth curve in R3 whose curvature everywhere is ⩽some
number k. Let C be a circle of curvature k, i.e., of radius r = 1
k . Let x,y ∈K and s,t ∈C
be any points such that arc(x,y) = arc(s,t) ⩽πr. Then the chord distances satisfy
|x −y| ⩾|s −t|.
Proof. See Schur’s Theorem in [10].
✷
We also will use results on thickness of knots developed in [21]. Let K be a smooth
knot in R3, a simple closed curve that is at least C2 smooth. We assume C2 smoothness
throughout this paper, and the work in [21] assumed that as well; but in fact the deﬁnition
and results there can be modiﬁed to deal with C1,1 curves (this has been noted by
R. Litherland, O. Durumeric, and [9,17]).
For each x ∈K, let D(x,r) denote the disk of radius r centered at x and orthogonal at x
to K. For sufﬁciently small r > 0, the disks are pairwise disjoint, their union forming
a tubular neighborhood of K. We deﬁne the injectivity radius of K, R(K), to be the
supremum of such good radii. The radius R(K) measures the maximum thickness of
“rope” that could be used to form the curve K. Of course, R(K) changes with scale. We
deﬁne the scale-invariant ropelength or length energy of K to be
EL(K) = arclength(K)
R(K)
.
The radius R(K) is affected by curvature and by points of K that are far apart in the
sense of arclength but close in space. For the latter kinds of points, distances will be
100
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
minimized at pairs of points (x,y) that are critical points for the distance function |x −y|.
Speciﬁcally, deﬁne the critical self-distance of K to be the minimum of |x −y| over all
pairs (x,y) ∈K × K, x̸ = y, for which the chord x −y is perpendicular to K at either or
both of its endpoints. Let MinRad(K) denote the minimum radius of curvature of K. We
then have from [21]:
Lemma 2. The thickness of a smooth knot is bounded by the minimum radius of curvature
and half the critical self-distance. In fact,
R(K) = min

MinRad(K), 1
2 critical self-distance(K)

.
The next lemma is a consequence of Lemmas 1 and 2.
Lemma 3. Suppose K is a smooth knot of thickness R(K) = r. For any x,y ∈K, such
that arc(x,y) ⩾πr, we must have |x −y| ⩾2r.
Proof. Fix x and consider ﬁrst the two points y ∈K for which arc(x,y) = πr. Since, by
Lemma 2, the curvature of K is everywhere ⩽1/r, and arc(x,y) = πr, so in particular it
is ⩽πr, we can apply Schur’s Theorem to the arc from x to such y to conclude that |x −y|
is at least as large as for the corresponding points on a circle of radius r, i.e., |x −y| ⩾2r.
Now consider the arc Y of K consisting of those points y with arc(x,y) ⩾πr. Let y0
be a point of Y that minimizes distance to x. If y0 is closer to x than 2r then, from the
preceding paragraph, it cannot be an endpoint of Y; thus it would have to be a critical
point for the function |x −y|. But by Lemma 2, any such critical pair (x,y) has distance
⩾2r.
✷
In the next two lemmas, we obtain the linear bound for the energy contribution of
proximal pairs, that is, points for which arc(x,y) ⩽πR(K).
Lemma 4. For a ﬁxed point s on a circle C of radius R,

t∈C
1
|s −t|2 −
1
arc(s,t)2 = 2
πR .
Proof. Fix s on a circle C of radius R. Note that if arc(s,t) = θ, then |s −t|2 =
R2(2 −2 cosθ). Thus,

t∈C
1
|s −t|2 −
1
arc(s,t)2 = 2
πR

0
1
R2(2 −2 cos(t/R)) −1
t2 dt = 2
πR .
✷
Lemma 5. If K is a smooth knot in R3, then

x∈K

arc(x,y)⩽πR(K)
1
|x −y|2 −
1
arc(x,y)2 ⩽2
π EL(K).
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
101
Proof. We begin by rescaling K to have R(K) = 1; note this leaves each side of the
inequality unchanged. Then EL(K) is just the new total arclength of K, which we
abbreviate L. By Lemma 2, the curvature of K everywhere is ⩽
1
R(K) = 1. For points
x,y on K with arc(x,y) ⩽π, let s,t be points on the circle, C, of radius 1 = R(K), for
which arc(s,t) = arc(x,y). By Schur’s Theorem (Lemma 1), we have |x −y| ⩾|s −t|, so
1
|x −y|2 −
1
arc(x,y)2 ⩽
1
|s −t|2 −
1
arc(x,y)2 =
1
|s −t|2 −
1
arc(s,t)2 .
(2)
For a ﬁxed x on K and a ﬁxed s on C, (2) and Lemma 4 give us

arc(x,y)⩽π
1
|x −y|2 −
1
arc(x,y)2 ⩽

arc(s,t)⩽π
1
|s −t|2 −
1
arc(s,t)2 = 2
π .
Thus,

x∈K

arc(x,y)⩽π
1
|x −y|2 −
1
arc(x,y)2 ⩽

x∈K
2
π = 2
π L.
✷
Finally, we need a lemma about measurable subsets of K. When we talk about
“measure”, we mean the one-dimensional Lebesgue measure on K that is just arclength
when applied to intervals. We actually use only Borel sets.
We want to deﬁne subsets of K of speciﬁed measure that are closest, in terms of spatial
distance, to a given point x ∈K. First we need a preliminary lemma about decomposing
measurable sets.
Lemma 6. Suppose W is a measurable subset of K and m1,m2 > 0 are numbers with
m1 + m2 = µ(W). Then we can partition W into measurable sets W1,W2, with µ(Wj) =
mj, j = 1,2.
Proof. Orient K, ﬁx a point z0 ∈K, and consider the intersections of W with intervals
Iz = [z0,z] as z ranges over K. Since the measure of a subset of an interval is bounded by
the length of the interval, the function µ(W ∩Iz) is continuous in z. The measure µ(W ∩Iz)
is arbitrarily small when z ≈z0, is monotonically nondecreasing as z moves around K, and
eventually exceeds m1 as z approaches z0 from the “back”. Thus there must be a value of
z for which µ(W ∩Iz) = m1.
✷
In the next lemma, and the proof of the main theorem, we use the following notation.
For x ∈K ﬁxed, a ⩽b, let S(a,b], S[a,b], S[a] denote spherical shells of radius from a
to b, and the sphere of radius a, all centered at x.
Lemma 7. Suppose K is a smooth knot with R(K) = 1. Fix x ∈K and let Y be the subset
of K consisting of all points y with arc(x,y) ⩾π. Let ν1,ν2,...,νm > 0 be numbers such
that ν1 + ν2 + ··· + νm = L −2π (i.e., µ(Y)). Then there exists a sequence of radii
2 ⩽ρ1 ⩽ρ2 ⩽··· ⩽ρm
102
E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
and a partition of Y into measurable sets W1,W2,...,Wm such that
(a) for each j, µ(Wj) = νj, and
(b) W1 ⊆Y ∩S[2,ρ1] and for each j > 1, Wj ⊆Y ∩S[ρj−1,ρj].
Proof. The proof is nearly straightforward. There is a slight complication because the knot
K might intersect some spheres S[ρ] in sets of positive length.
Since R(K) = 1 and y ∈Y has arc(x,y) ⩾π, by Lemma 3, |x −y| ⩾2, so Y ⊆
S[2,L/2]. We deﬁne the radius ρm ⩽L/2 to be the smallest radius ρ for which Y is
contained in S[2,ρ].
We construct radii ρj and sets Wj inductively, with a slight variation at the ﬁnal step.
For the degenerate case m = 1, of course, W1 = Y and ρ1 = ρm is as above.
We now begin the induction. Suppose ﬁrst that µ(Y ∩S[2]) ⩾ν1. By Lemma 6, we can
partition Y ∩S[2] into sets W1 ∪V , where µ(W1) = ν1; let ρ1 = 2.
Now suppose µ(Y ∩S[2]) < ν1. Let
Rlow =

ρ: µ

Y ∩S[2,ρ]

< ν1

and r1 = sup(Rlow). Similarly, let
Rhigh =

ρ: µ

Y ∩S[2,ρ]

⩾ν1

and let r′
1 = inf(Rhigh). Here Rlow̸ = ∅because µ(Y ∩S[2]) < ν1, so 2 ∈Rlow, and
Rhigh̸ = ∅because ρm ∈Rhigh.
We claim r1 = r′
1. Each element of Rlow is < each element of Rhigh. Thus, r1 ⩽r′
1. If
the inequality is strict, then for each ρ ∈(r1,r′
1), µ(Y ∩S[2,ρ]) ⩾ν1, which contradicts
ρ < r′
1.
Now deﬁne ρ1 = r1 = r′
1. The set Y ∩S[2,r1) is a monotone union of sets, each with
measure < ν1. Thus, µ(Y ∩S[2,ρ1)) ⩽ν1. On the other hand, Y ∩S(r′
1,∞) is a monotone
union of sets, each with measure < µ(Y) −ν1. Thus, µ(Y ∩S(ρ1,∞)) ⩽µ(Y) −ν1, so
µ(Y ∩S[2,ρ1]) ⩾ν1.
Using Lemma 6, we extract a subset of Y ∩S[ρ1] whose measure is whatever µ(Y ∩
S[2,ρ1)) may lack to make ν1, and let W1 be the union of this set with Y ∩S[2,ρ1).
To continue the induction, let Y1 = Y −W1. Note Y1 ⊆Y ∩S[ρ1,∞).
Suppose ρ1,...,ρj−1 and W1,...,Wj−1 have been chosen as required in the statement
of the lemma and the set Yj−1 = Y −(W1 ∪··· ∪Wj−1) ⊆S[ρj−1,∞). Note that
since W1,...,Wj−1 ⊆Y ∩S[2,ρj−1], Y ∩S(ρj−1,∞) ⊆Yj−1. So for any ρ,ρ′ with
ρj−1 < ρ < ρ′, we have Yj−1 ∩S[ρ,ρ′] = Y ∩S[ρ,ρ′].
Now proceed much like the initial case. If j = m, we ﬁnish by taking Wj = Yj−1 and
ρm as above.
There are two cases: If µ(Yj−1 ∩S[ρj−1]) ⩾νj, then let Wj be a subset of Yj−1 ∩
S[ρj−1] of measure νj , ρj = ρj−1, and Yj = Yj−1 −Wj.
Suppose now µ(Yj−1 ∩S[ρj−1]) < νj. Deﬁne
Rlow =

ρ: µ

Yj−1 ∩S[ρj−1,ρ]

< νj

and rj = sup(Rlow). Similarly, let
Rhigh =

ρ: µ

Yj−1 ∩S[ρj−1,ρ]

⩾νj

E.J. Rawdon, J. Simon / Topology and its Applications 125 (2002) 97–109
103
and let r′
j = inf(Rhigh). Here Rlow̸ = ∅because ρj−1 ∈Rlow and Rhigh̸ = ∅because
ρm ∈Rhigh.
As in the initial case, we have rj = r′
j, and we deﬁne ρj = rj = r′
j . Also, µ(Yj−1 ∩
S[ρj−1,ρj)) ⩽νj and µ(Yj−1 ∩S[ρj−1,ρj]) ⩾νj.
Let Wj be the union of Yj−1 ∩S[ρj−1,ρj) with a subset of Yj−1 ∩S[ρj] of however
much additional measure is needed to reach νj. Finally, let Yj = Yj−1 −Wj. Note then
Yj ⊆Y ∩S[ρj,∞).
✷
