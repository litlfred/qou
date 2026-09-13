---
doc_id: arxiv-math-0108215v1
doc_title: "Möbius Energy of Thick Knots Eric J. Rawdon 2"
section_id: sec-004-2-the-lemmas
section_title: "The Lemmas"
section_number: 2
pages: 3-7
source_pdf: 0108215v1.pdf
source_sha256: 191784d2ccb3415a
---
The ﬁrst lemma is a version of a theorem of Schur. This is taken from [3 1],
with the slight adjustment that we do not need to consider general planar
convex curves as the reference curves, just circles.
3
Lemma 1 Let K be a C 2 smooth curve in R3 whose curvature everywhere is
≤ some number k. Let C be a circle of curvature k, i.e. of radius r = 1
k . Let
x, y ∈ K and s, t ∈ C be any points such that arc(x, y) = arc( s, t) ≤ πr. Then
the chord distances satisfy
|x − y| ≥ | s − t|.
PROOF. See Schur’s Theorem in [31]. ✷
We also will use results on thickness of knots developed in [18]. Let K be
a smooth knot in R3, a simple closed curve that is at least C 2 smooth. We
assume C 2 smoothness throughout this paper, and the work in [18] assumed
that as well; but in fact the deﬁnition and results there can be modiﬁe d to
deal with C 1, 1 curves (this has been noted by R. Litherland, O. Durumeric,
and [22,32]).
For each x ∈ K, let D(x, r) denote the disk of radius r centered at x and
orthogonal at x to K. For suﬃciently small r > 0, the disks are pairwise
disjoint, their union forming a tubular neighborhood of K. We deﬁne the
injectivity radius of K, R(K), to be the supremum of such good radii. The
radius R(K) measures the maximum thickness of “rope” that could be used
to form the curve K. Of course, R(K) changes with scale. We deﬁne the
scale-invariant ropelength or length energy of K to be
EL(K) = arclength(K)
R(K) .
The radius R(K) is aﬀected by curvature and by points of K that are far
apart in the sense of arclength but close in space. For the latter kin ds of
points, distances will be minimized at pairs of points ( x, y) that are critical
points for the distance function |x − y|. Speciﬁcally, deﬁne the critical self-
distance of K to be the minimum of |x − y| over all pairs ( x, y) ∈ K × K,
x ⁄= y, for which the chord x − y is perpendicular to K at either or both of
its endpoints. Let MinRad( K) denote the minimum radius of curvature of K.
We then have from [18]:
Lemma 2 The thickness of a smooth knot is bounded by the minimum radiu s
of curvature and half the critical self-distance. In fact,
R(K) = min
{
MinRad(K) , 1
2 critical self distance (K)
}
.
4
The next lemma is a consequence of Lemmas 1 and 2.
Lemma 3 Suppose K is a smooth knot of thickness R(K) = r. For any
x, y ∈ K, such that arc(x, y) ≥ πr, we must have |x − y| ≥ 2r.
PROOF. Fix x and consider ﬁrst the two points y ∈ K for which arc( x, y) =
πr. Since, by Lemma 2, the curvature of K is everywhere ≤ 1/r, and arc(x, y) =
πr, so in particular it is ≤ πr, we can apply Schur’s Theorem to the arc from
x to such y to conclude that |x − y| is at least as large as for the corresponding
points on a circle of radius r, i.e. |x − y| ≥ 2r.
Now consider the arc Y of K consisting of those points y with arc( x, y) ≥ πr.
Let y0 be a point of Y that minimizes distance to x. If y0 is closer to x than
2r then, from the preceding paragraph, it cannot be an endpoint of Y ; thus
it would have to be a critical point for the function |x − y|. But by Lemma 2,
any such critical pair ( x, y) has distance ≥ 2r. ✷
In the next two lemmas, we obtain the linear bound for the energy co ntribution
of proximal pairs, that is, points for which arc( x, y) ≤ πR(K).
Lemma 4 For a ﬁxed point s on a circle C of radius R,
∫
t∈C
1
|s − t|2 − 1
arc(s, t)2 = 2
πR .
PROOF. Fix s on a circle C of radius R. Note that if arc( s, t) = θ, then
|s − t|2 = R2(2 − 2 cos θ). Thus,
∫
t∈C
1
|s − t|2 − 1
arc(s, t)2 = 2
∫ πR
0
1
R2(2 − 2 cos(t/R)) − 1
t2 dt
= 2
πR .
✷
Lemma 5 If K is a smooth knot in R3, then
∫
x∈K
∫
arc(x,y )≤πR (K)
1
|x − y|2 − 1
arc(x, y)2 ≤ 2
π EL(K) .
5
PROOF. We begin by rescaling K to have R(K) = 1; note this leaves each
side of the inequality unchanged. Then EL(K) is just the new total arclength
of K, which we abbreviate L. By Lemma 2, the curvature of K everywhere
is ≤ 1
R(K) = 1. For points x, y on K with arc( x, y) ≤ π, let s, t be points on
the circle, C, of radius 1 = R(K), for which arc( s, t) = arc( x, y). By Schur’s
Theorem (Lemma 1), we have |x − y| ≥ | s − t|, so
1
|x − y|2 − 1
arc(x, y)2 ≤ 1
|s − t|2 − 1
arc(x, y)2 = 1
|s − t|2 − 1
arc(s, t)2 . (2)
For a ﬁxed x on K and a ﬁxed s on C, (2) and Lemma 4 give us
∫
arc(x,y )≤π
1
|x − y|2 − 1
arc(x, y)2 ≤
∫
arc(s,t )≤π
1
|s − t|2 − 1
arc(s, t)2
= 2
π .
Thus, ∫
x∈K
∫
arc(x,y )≤π
1
|x − y|2 − 1
arc(x, y)2 ≤
∫
x∈K
2
π = 2
π L .
✷
Finally, we need a lemma about measurable subsets of K. When we talk about
“measure”, we mean the one-dimensional Lebesgue measure on K that is just
arclength when applied to intervals. We actually use only Borel sets.
We want to deﬁne subsets of K of speciﬁed measure that are closest, in terms
of spatial distance, to a given point x ∈ K. First we need a preliminary lemma
about decomposing measurable sets.
Lemma 6 Suppose W is a measurable subset of K and m1, m2 > 0 are num-
bers with m1 + m2 = µ(W ). Then we can partition W into measurable sets
W1, W2, with µ(Wj) = mj , j = 1, 2.
PROOF. Orient K, ﬁx a point z0 ∈ K, and consider the intersections of W
with intervals Iz = [z0, z] as z ranges over K. Since the measure of a subset of
an interval is bounded by the length of the interval, the function µ(W ∩ Iz)
is continuous in z. The measure µ(W ∩ Iz) is arbitrarily small when z ≈ z0,
is monotonically nondecreasing as z moves around K, and eventually exceeds
m1 as z approaches z0 from the “back”. Thus there must be a value of z for
which µ(W ∩ Iz) = m1. ✷
In the next lemma, and the proof of the main theorem, we use the fo llowing
notation. For x ∈ K ﬁxed, a ≤ b, let S(a, b], S[a, b], S[a] denote spherical shells
of radius from a to b, and the sphere of radius a, all centered at x.
6
Lemma 7 Suppose K is a smooth knot with R(K) = 1 . Fix x ∈ K and
let Y be the subset of K consisting of all points y with arc(x, y) ≥ π. Let
ν1, ν2, . . . , νm > 0 be numbers such that ν1 + ν2 + · · · + νm = L − 2π (i.e.
µ(Y )). Then there exists a sequence of radii
2 ≤ ρ1 ≤ ρ2 ≤ · · · ≤ ρm
and a partition of Y into measurable sets W1, W2, . . . , Wm such that
(a) for each j, µ(Wj) = νj, and
(b) W1 ⊆ Y ∩ S[2, ρ1] and for each j > 1, Wj ⊆ Y ∩ S[ρj−1, ρj].
PROOF. The proof is nearly straightforward. There is a slight complication
because the knot K might intersect some spheres S[ρ] in sets of positive length.
Since R(K) = 1 and y ∈ Y has arc( x, y) ≥ π, by Lemma 3, |x − y| ≥ 2, so
Y ⊆ S[2, L/2]. We deﬁne the radius ρm ≤ L/2 to be the smallest radius ρ for
which Y is contained in S[2, ρ].
We construct radii ρj and sets Wj inductively, with a slight variation at the
ﬁnal step. For the degenerate case m = 1, of course, W1 = Y and ρ1 = ρm is
as above.
We now begin the induction. Suppose ﬁrst that µ(Y ∩ S[2]) ≥ ν1. By Lemma
6, we can partition Y ∩ S[2] into sets W1 ∪ V , where µ(W1) = ν1; let ρ1 = 2.
Now suppose µ(Y ∩ S[2]) < ν 1. Let
Rlow = {ρ : µ(Y ∩ S[2, ρ]) < ν 1}
and r1 = sup(Rlow). Similarly, let
Rhigh = {ρ : µ(Y ∩ S[2, ρ]) ≥ ν1}
and let r′
1 = inf( Rhigh). Here Rlow ⁄= ∅ because µ(Y ∩ S[2]) < ν 1, so 2 ∈ Rlow,
and Rhigh ⁄= ∅ because ρm ∈ Rhigh.
We claim r1 = r′
