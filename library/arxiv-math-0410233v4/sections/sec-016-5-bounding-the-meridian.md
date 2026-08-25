---
doc_id: arxiv-math-0410233v4
doc_title: "Cusp shapes under cone deformation"
section_id: sec-016-5-bounding-the-meridian
section_title: "Bounding the meridian"
section_number: 5
pages: 28-31
source_pdf: 0410233v4.pdf
source_sha256: 1f7215c9f21aa2b7
doc_brief: "Cusp shapes under cone deformation — A horospherical torus about a cusp of a hyperbolic manifold inherits a Euclidean similarity structure, called a cusp sh ape."
---
We now show that the length of the shortest nontrivial simple closed curve
on the cusp torus is bounded throughout the cone deformation , provided the
tube radius about the singular locus stays large. Recall her e that we are
calling this shortest curve the meridian of the torus. The fo llowing lemma
is the last piece needed to complete the proof of Theorem 1.4.
Lemma 5.1. Suppose M is a hyperbolic cone manifold with one cusp, and
with singular locus Σ . Suppose the tube radius R about the singular locus is
at least log(2/
√
3). Then there exists a horoball neighborhood U of the cusp
such that the meridian of ∂U has length at least 1 − e−2R.
Proof. Let X = M −Σ. X admits an incomplete hyperbolic metric. Expand
the tube V = ∪Vi about the singular locus Σ until the tube hits itself. Each
Vi has the same tube radius R. Next expand the horoball U about the cusp
until it either becomes tangent to itself or to V .
We obtain a region Ω by continuing to expand U as follows. First, choose
a particular lift Ua of U in the universal cover. Because U is embedded in
H3 by the developing map on the universal cover ~X of X, we can assume
the developing map is one to one on Ua and takes ∂Ua to the plane z = 1
in H3.
Take Ω = Ua ∪ S, where S is the set consisting of all points x in ~X such
that the distance dist( x, ∂Ua) < dist(x, ∂Ub) for Ub any other lift of U , and
also such that the distance dist( φ(x), ∂U ) < dist(∂U, Σ), where φ is the
covering projection. Note that Ω is embedded in H3 by the developing map.
That is, the developing map is one to one on Ω.
CUSP SHAPES UNDER CONE DEFORMATION 29
a0 a1
p1
d
p0
H β
length(β) = L
Figure 3. The top edge of the quadrilateral maps to the
shortest path on ∂U under the covering projection.
Let p be a point on ∂U closest to Σ, and let p0 and p1 be lifts of p on ∂Ua
such that the projection of the path from p0 to p1 is shortest on ∂U . Let a0
be the point in the universal cover on a lift of Σ such that the p ath from p0
to a0 has length equal to the minimum distance from p0 to Σ. Similarly, let
a1 be the point on a lift of Σ such that the path from p1 to a1 has length
equal to the minimum distance from p1 to Σ. Note the interiors of the paths
between p0 and a0 and between p1 and a1 are contained in Ω.
Then note the interior of the geodesic β from a0 to a1 is also in Ω,
along with all the points in the quadrilateral with sides giv en by β and
the paths from p0 to p1, from p0 to a0, and from p1 to a1. This is be-
cause, ﬁrst, all points x in this quadrilateral (except the endpoints of β)
have dist(φ(x), ∂U ) < dist(∂U, Σ). Also, if any x were closer to some other
lift Ub of U , then there would be points in the quadrilateral equidistan t to
two diﬀerent lifts of U . All points equidistant to two diﬀerent lifts of U lie
on some totally geodesic planes of H3. Hence some geodesic must intersect
β but not the paths from p0 to a0, p1 to a1, or the path on the horosphere
∂Ua from p0 to p1. This is impossible.
Now let H be the length of the paths from p0 to a0 and from p1 to a1. Let
L be the length of β. We know that H ≥ R and L ≥ 2R since the distance
between any two components of the lift of Σ is greater than or e qual to
2R. We let d be the length of the path on the horosphere ∂Ua between p0
and p1. Since Ω is embedded by the developing map, we can assume the
quadrilateral is of the form shown in Figure 3.
Then solving for d in terms of H and L, d = 2e−H sinh(L/2).
Case 1: H = R. Then d ≥ 2e−R sinh(R) = 1 − e−2R.
Case 2: H > R Then U must be tangent to itself, say at a point q, and
not necessarily tangent to the tube about Σ. Then the image of Ω under the
developing map must contain some portion of the region above the geodesic
surface equidistant from a horizontal plane (the lift of ∂Ua) and some other
horosphere.
This geodesic surface is some portion of the (Euclidean) hem isphere with
radius 1, tangent to the lift of ∂Ua at a lift q0 of q. See Figure 4. The image
30 JESSICA S. PURCELL
√
3/2
q0
1
x
Figure 4.
of Ω under the developing map contains a neighborhood of poin ts on this
hemisphere about q0. If it were to contain all the points on the hemisphere
between the dotted lines in Figure 4 (that is, points whose pr ojection to C
have Euclidean distance at most 1 /2 from the projection of q0 to C), then
d ≥ 1.
Let x be one of these points. That is, the projection of x to C has
Euclidean distance at most 1 /2 from the projection of q0 to C. Note x
will lie in Ω provided dist( φ(x), ∂U ) < dist(∂U, Σ) = H, or provided H is
large enough. But now, dist( φ(x), ∂U ) = log(1 /height(x)), where height( x)
denotes the z–coordinate of x in H3. Thus this distance is at most log(2 /
√
3).
Since H > R , we can ensure d ≥ 1 by restricting to R ≥ log(2/
√
3). □
When we plug the result of Lemma 5.1 into Theorem 3.8, along wi th
the bound on ∑ bj of the previous section, we may complete the proof of
Theorem 1.4.
Theorem 1.4. Let M = Xτ be a hyperbolic 3–manifold with a cusp,
and let X = X0 be a hyperbolic 3–manifold which can be joined to M by
a smooth family of hyperbolic cone manifolds Xt with tube radius at least
R1 ≥ 0.56, and with n components of the singular locus. Let Ut be a horoball
neighborhood about the cusp. Let h(M ) denote the normalized height of the
cusp torus ∂Uτ . Let h(X) denote the normalized height of ∂U0. Then the
hyperbolic cone deformation can be parameterized such that the change in
normalized height is bounded in terms of R1 alone:
−(2π)2
√
n C(R1)
(1 − e−2R1)
√
2
≤ h(M ) − h(X) ≤ (2π)2
√
n C(R1)
(1 − e−2R1 )
√
2
.
Proof. Theorem 3.8, combined with Theorem 4.6 and Lemma 5.1 imply th at
−
√
n C(R1)
(1 − e−2R1)
√
2 ≤ ˙h ≤
√
n C(R1)
(1 − e−2R1)
√
2
and that the total time of the deformation is t = (2 π)2. We integrate the
above inequality over the deformation. The bounds on the lef t and right are
independent of t. Thus we obtain the conclusion of the theorem. □
CUSP SHAPES UNDER CONE DEFORMATION 31
Figure 5. Left to right: The link K. The link K with
crossing circles added. The link L.
