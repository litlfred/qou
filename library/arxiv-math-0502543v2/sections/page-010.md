---
doc_id: arxiv-math-0502543v2
doc_title: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR"
section_id: page-010
section_title: "Page 10"
section_number: null
pages: 10-10
source_pdf: 0502543v2.pdf
source_sha256: 227ef8150cb08faf
toc_source: undetermined
doc_brief: "CONTINUITY OF VOLUMES – ON A GENERALIZATION OF A CONJECTURE OF J.W.MILNOR — 12 sections: Page 1; Page 2; Page 3"
---
10
IGOR RIVIN
Proof. The spherical Law of Cosines states that:
cos(A) = cos(α) + cos(β) cos(γ)
sin(β) sin(γ)
.
It follows that
cos(A) −2ǫ2 ≤cos(A)(1 −ǫ2) −ǫ2 ≤cos(α) ≤cos(A) + ǫ2.
The assertion of the lemma follows immediately.
□
Corollary 4. Let F1 and F2 be two planes intersecting at a dihedral angle
α, with both F1 and F2 intersecting a third plane P, at angles whose cosines
are smaller than ǫ. Let A be the angle between F1 ∩P and F2 ∩P. Then
|α −A| < 2ǫ.
Proof. Apply Lemma 3 to the link of the point F1 ∩F2 ∩P.
□
Lemma 4. Let V be a convex polygon in the hyperbolic plane H2, such that
all the vertices of V lie within a distance r of a certain point O. Then, the
sum of the exterior angles of V is smaller than 2π cosh(r).
Proof. The area of a disk of radius r in H2 equals 4π sinh2(r/2) =
2π(cosh(r) −1) (see [12]). Since V is contained in such a disk, its area
is at most 2π(cosh(r)−1), and since the area of V equals the diﬀerence
between the sum of the exterior angles and 2π, the statement of the
lemma follows.
□
Now we are ready to show the following:
Theorem 9. Let X be a convex polyhedron with N vertices in H3 of diameter
ρ ≫1. Then, there exists a cyclic sequence of faces F1, . . . , Fk = F1, with
Fi sharing an edge ei with Fi+1 (indices taken
mod k) so that the sum of
exterior dihedral angles at e1, . . . , ek is smaller than 2π+12N exp(−ρ/2N).
Proof. Take a diameter D of X of length ρ, place points p1, . . . , pN
equally spaced on D. By the pigeonhole principle, one of the segments
pipi+1 contains no vertices of X. Let x0 be the midpoint of the segment
pipi+1. Construct planes orthogonal to D at x0 (P) and pi (P−), and at
pi+1 (P+). Let t = ρ/(2N). The portion of X contained between P−and
P+ is a polyhedral cylinder, consisting of faces F1, . . . , Fk. By Lemma
2, the intersection of X with P is a polygon P, whose sum of exterior
angles is at most 2π(4 exp(−2t) + 1), and so by Corollary 4, combined
with Lemma 1, the sum of the dihedral angles corresponding to pairs
FiFi+1 is at most 2π(4 exp(−2t) + 1) + 6k exp(−t). Since k is no greater
than the number of faces of X, which, in turn, is at most 2N −4.
□
