---
doc_id: arxiv-math-0502543v2
doc_title: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR IGOR RIVIN"
section_id: sec-001-3-convex-polytopes
section_title: "Convex polytopes"
section_number: 3
pages: 5-11
source_pdf: 0502543v2.pdf
source_sha256: 227ef8150cb08faf
doc_brief: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR IGOR RIVIN — In his paper [6] J."
---
spherical polytopes in all dimensions) the proof given in Section 2
goes through without change, with the one proviso that it is n ot
currently known whether the volume of a polytope is determin ed
up to congruence by its dihedral angles. Such a uniqueness re sult is
conjectured (indeed, it is conjectured that a polytope is determined up
to congruence by the dihedral angles), and is easy to prove fo r simple
polytopes – those with simplicial links of vertices – this fo llows in
arbitrary dimension from the corresponding result in 3 dime nsions.
For the 3-dimensional result see, eg, [8, 10]. In the rest of this paper we
will be concerned with the most interesting case of convex polyhedra
in H3.
First, we recall the following result of [10, 8]:
Theorem 4 ([10, 8]). A metric space (M, g) homeomorphic to S2 can arise
as the Gaussian image G (P) of a compact convex polyhedron P in H3 if and
only if the following conditions hold:
• (a) The metric g has constant curvature 1 away from a ﬁnite collec-
tion of cone points.
• (b) The cone angle at each c i is greater than 2π.
• (c) The lengths of closed geodesics of (M, g) are all strictly greater
than 2π.
Assume now, for simplicity , that the polyhedron P is simple (as
pointed out above, this also allows us to assume that the geom etry
is determined by the dihedral angles). In that case, the spac e of
admissible metrics ΩP (as per Theorem 4) is parametrized by the
exterior dihedral angles (the cell decomposition dual to that of P gives
a triangulation of the Gaussian image, and the (exterior) di hedral
angles are the lengths of edges of the triangulation.) Theor ems 9,10
immediately imply the following:
Theorem 5. There exists a constant L 0, such that the maximal length ℓP of
an edge of P is bounded as follows:
ℓP ≤ max(L0, −2N log(d(P, ∂
ΩP)/12N)),
where N is the number of vertices of P .
6 IGOR RIVIN
Proof. Assume the contrary . Then, there exists a sequence of polyhe -
dra P1, . . . ,Pn, . . . with diameter ρ(Pi) ≥ ℓ)Pi going to infnity , which
are farther than 12 N exp(−ρ/2N). By choosing a subsequence, we
may assume that there is a ﬁxed cycle of faces F1, . . . ,Fk of P, such that
the sum of dihedral angles along the edgesei = Fi∩Fi+1 is smaller than
2π + 12N exp(−ρ/2N), (by Theorem 9) and which are a 4 N exp(−2ρ)
quasigeodesic (by Theorem 10). Since the limit point of the Pi is not
in ΩP (by Theorem 4), the result follow. □
The following corollary is immediate (by Schl¨ aﬂi, see Sect ion 2):
Corollary 3. The volume is in W 1,p(Ωp) for all p > 0.
We now have almost enough to show that volume extends to Ωp,
except for the slight matter of not having the required (by Theorem 3)
regularity result for ∂ΩP. Such a result seems quite non-trivial, since
the length of the shortest closed geodesic is a rather badly b ehaved
quantity . However, there are two very important special cases where
ΩP is actually a convex polytope, so this problem is ﬁnessed. Th e
ﬁrst is when we restrict the dihedral angles to be non-obtuse . This
case is covered by
Theorem 6 (Andreev’s theorem ([1])) . Let C be an abstract polyhedron
with more than 4 faces, and suppose that non-obtuse angles αi are given
corresponding to each edge e i of C. There is a compact convex hyperbolic
polyhedron whose faces realize C with dihedral angle αi at each edge e i if
and only if the following conditions hold:
(1) For each edge e i, 0 < α i ≤ π/2.
(2) For any three distinct edges e 1, e2, e3 meeting at a vertex, α1 + α2 +
α3 > π.
(3) Whenever Γis a prismatic 3-circuit intersecting edges e1, e2, e3, then
α1 + α2 + α3 < π.
(4) Whenever Γis a prismatic 4-circuit intersecting edges e 1, e2, e3, e4,
then α1 + α2 + α3 + α4 < 2π.
(5) Whenever there is a four-sided face bounded by edges e 1, e2, e3, e4
(enumerated successively), with edges e 12, e23, e34, e41 entering the
four vertices, then:
α1 + α3 + α12 + α23 + α34 + α41 < 3π,(3)
α2 + α4 + α12 + α23 + α34 + α41 < 3π.(4)
The other special case is that of hyperideal polyhedra:
Theorem 7 (Bao-Bonahon, [2]). Let σ be a cell decomposition of S 2, and
let w : σ1 → (0, π) be a map on the set of edges of σ. Then there exists a
CONTINUITY OF VOLUMES 7
hyperideal polyhedron with combinatorics given by σ and exterior dihedral
angles given by w if and only if:
(1) The sum of the values of w on each circuit in σ1 is not smaller than
2π, and is strictly greater if the circuit is non-elementary.
(2) The sum of values of w on each simple path in σ1 is strictly larger
than π.
The hyperideal polyhedron is then unique.
4. D egeneration estimates
The results of this section are a quantitative version of the results
of the compactness results of [10, 8]. First, some key lemmas . The
general setup will be as follows: L is a geodesic in H3, t is a real
number (generally large) andP, P−, P+ are three planes, all orthogonal
to L, and such that d(P, P−) = d(P, P+) = t, and d(P−, P+) = 2t. We
denote x0 = L ∩ P.
In the sequel, we use the hyperboloid model of H3, where H3 is
represented by the set ⟨x, x⟩= −1; x0 > 0, in the R4 equipped with the
scalar product ⟨x, y⟩= −x1y1 + ∑4
i=2 xiyi. The reader is referred to [11]
(as well as [10]) for the details (which will be used below).
Returning back to our setup, we can assume, without loss of ge n-
erality , that
x0 =












1
0
0
0












,
that
P⊥ =












0
1
0
0












,
and hence, that P+ = φ(t)P, while P− = φ(−t)P, where
φ(r) =












cosh(r) sinh( r) 0 0
sinh(r) cosh( r) 0 0
0 0 1 0
0 0 0 1












.
Since φ(r) is symmetric, it follows that
P+⊥ = φ(t)P⊥ =












cosh(t)
sinh(t)
0
0












,
8 IGOR RIVIN
while
P−⊥ = φ(t)P⊥ =












cosh(t)
− sinh(t)
0
0












,
Lemma 1. Let Q be a plane in H3 which intersects both P − and P+. Then,
there exists t 0, such that Q intersects P , and the cosine of the angle α of
intersection satisﬁes | cos(α)| < 3e−t, as long as t > t0. The number t 0 can
be picked independently of Q.
Proof. Let the unit normal Q⊥ to Q be Q⊥ =












a
b
c
d












. Since two planes
intersect if and only if the scalar product of their unit norm als is less
than 1 in absolute value, we have, from the hypotheses of the l emma
and the description of the unit normals to P− and P+ above that:
|a cosh(t) + b sinh(t)| < 1(5)
|a cosh(t) − b sinh(t)| < 1.(6)
Squaring the two inequalities, and adding them together we o btain:
a2 cosh2(t) + b2 sinh2(t) < 1.
Since, under the hypotheses of the lemma, min(cosh( t), sinh(t)) >
et/3, it follows that
a2 + b2 < 3/et,
and so max( a, b) < 3e−t. Now, the cosine of the angle between Q and
P equals ⟨Q⊥, P⊥⟩= b, so the result follows. □
Remark 8. The constant 3 is far from sharp (especially for larger t).
Lemma 2. There exists a t 0, such that if M is a line in H3 which intersects
both P − and P +, then M intersects P , and cosh(d(P ∩ M, x0)) < 4e−2t + 1,
as long as t > t0.
Proof. Assume that M ∩ P+ = φ(t)p1, and M ∩ P− = φ(−t)p1, where
p1,2 ∈ P. (This is always possible, since P+ = φ(t)P, P− = φ(−t).) The
intersection of M with P is then given by
M ∩ P = x(M ∩ P+) + y(M ∩ P−)
‖x(M ∩ P+) + y(M ∩ P−)‖,
where x and y are chosen so that the linear combination is actually in
P, or, in other words, the second coordinate of the linear combination
vanishes. We abuse notation above by writing ‖Z‖=
√
−⟨Z, Z⟩.
CONTINUITY OF VOLUMES 9
Let us now compute. Set (for i = 1, 2)
pi =












ai
0
ci
di












.
It follows that
M ∩ P+ =












a1 cosh(t)
a1 sinh(t)
c1
d1












.
while
M ∩ P− =












a2 cosh(t)
−a2 sinh(t)
c2
d2












.
It follows that we can choose x = 1/(2a1), y = 1/(2a2), so that
m = xM ∩ P+ + yM ∩ P− =












cosh(t)
0
1
2(c1/a1 + c2/a2)
1
2(d1/a1 + d2/a2)












.
It follows that
(7) − cosh(d(M ∩ P, x0)) =
⟨m
‖m‖, x0
⟩
=
− cosh(t)√
cosh2(t) − 1/4 ((c1/a1 + c2/a2)2 + (d1/a1 + d2/a2)2)
.
Since c2
i + d2
i + 1 = a2
i , for i = 1, 2 it follows that |ci/ai| < 1, and
similarly |di/ai| < 1, so that
cosh2(t) ≥ cosh2(t)−1/4
(
(c1/a1 + c2/a2)2 + (d1/a1 + d2/a2)2
)
> cosh2(t)−2.
It follows that
cosh(d(M ∩ P, x0)) ≤ 1
√
1 − 2/ cosh2(t)
,
and the assertion of the lemma follows by elementary calculu s. □
Lemma 3. Let T be a spherical triangle with sides A , B, C and (opposite)
angles α, β, γ. Suppose that | cos(β)| < ǫ ≪ 1, | cos(γ)| < ǫ ≪ 1. Then
|α − A| < 2ǫ|.
10 IGOR RIVIN
Proof. The spherical Law of Cosines states that:
cos(A) = cos(α) + cos(β) cos(γ)
sin(β) sin(γ) .
It follows that
cos(A) − 2ǫ2 ≤ cos(A)(1 − ǫ2) − ǫ2 ≤ cos(α) ≤ cos(A) + ǫ2.
The assertion of the lemma follows immediately . □
Corollary 4. Let F 1 and F 2 be two planes intersecting at a dihedral angle
α, with both F 1 and F2 intersecting a third plane P, at angles whose cosines
are smaller than ǫ. Let A be the angle between F 1 ∩ P and F 2 ∩ P. Then
|α − A| < 2ǫ.
Proof. Apply Lemma 3 to the link of the point F1 ∩ F2 ∩ P. □
Lemma 4. Let V be a convex polygon in the hyperbolic plane H2, such that
all the vertices of V lie within a distance r of a certain point O. Then, the
sum of the exterior angles of V is smaller than 2π cosh(r).
Proof. The area of a disk of radius r in H2 equals 4 π sinh2(r/2) =
2π(cosh(r) − 1) (see [12]). Since V is contained in such a disk, its area
is at most 2π(cosh(r) − 1), and since the area of V equals the diﬀerence
between the sum of the exterior angles and 2 π, the statement of the
lemma follows. □
Now we are ready to show the following:
Theorem 9. Let X be a convex polyhedron with N vertices inH3 of diameter
ρ ≫ 1. Then, there exists a cyclic sequence of faces F 1, . . . ,Fk = F1, with
Fi sharing an edge e i with F i+1 (indices taken mod k) so that the sum of
exterior dihedral angles at e1, . . . ,ek is smaller than 2π + 12N exp(−ρ/2N).
Proof. Take a diameter D of X of length ρ, place points p1, . . . ,pN
equally spaced onD. By the pigeonhole principle, one of the segments
pipi+1 contains no vertices of X. Let x0 be the midpoint of the segment
pipi+1. Construct planes orthogonal to D at x0 (P) and pi (P−), and at
pi+1 (P+). Let t = ρ/(2N). The portion of X contained between P− and
P+ is a polyhedral cylinder, consisting of faces F1, . . . ,Fk. By Lemma
2, the intersection of X with P is a polygon P, whose sum of exterior
angles is at most 2 π(4 exp(−2t) + 1), and so by Corollary 4, combined
with Lemma 1, the sum of the dihedral angles corresponding to pairs
FiFi+1 is at most 2 π(4 exp(−2t) + 1) + 6k exp(−t). Since k is no greater
than the number of faces of X, which, in turn, is at most 2 N − 4. □
CONTINUITY OF VOLUMES 11
Theorem 10. With notation as in Theorem 9, the faces F 1, . . . ,Fk form a
curve in the Gaussian image of X with geodesic curvature not e xceeding
3k exp(−ρ/N)).
Remark 11. The reader is referred to [8, 10] for a more thorough
discussion of geodesics on spherical cone manifold, but su ﬃce it
to say that the contribution of the face Fi to the geodesic curvature
is 0 if the two edges are (hyper)parallel, and equal to the ang le of
intersection if they intersect.
Proof. Let e1 and e2 be the two edges of F. If e1 and e2 do not intersect,
there is nothing to prove (by the remark above. If they do inte rsect at
a point C, note that C is at a distance at least ρ/2N from x0, while the
intersections A and B of e1 and e2 with P are at most arccosh(4 exp(-
rho/N) + 1) ≈
√
8 exp(−ρ/2N) away from x0, and so at most (for large
ρ) 6 exp(−ρ/2N) away from each other. We will only use the (much
cruder) estimate cosh( AB) ≤ 2. Now, apply the hyperbolic law of
cosines to the triangle ABC, to get:
(8) 1 ≥ cos(γ) = − cosh(AB) + cosh(AC) cosh(BC)
sinh(AC) sinh(BC) ≥
1 − cosh(AB)
sinh(AC) sinh(BC) ≥ 1 − 2
sinh(AC) sinh(BC) ≥ 1 − 8 exp(−ρ/2N).
The estimate now follows.
□
Remark 12. The argument above is easily modiﬁed to show that the
curve dual to F1, . . . ,Fk has small geodesic curvature viewed as a
curve in S3
1, and not just in X∗.
