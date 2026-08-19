---
doc_id: arxiv-2208.13692v1
doc_title: "BRING’S CURVE: OLD AND NEW"
section_id: sec-007-32-vertices-and-face-centres
section_title: "Vertices and Face-Centres"
section_number: 3.2
pages: 17-18
source_pdf: 2208.13692v1.pdf
source_sha256: 567eff9fb44ef3e5
doc_brief: "European Journal of Mathematics (2024) 10:3 RESEARCH ARTICLE — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
duplicate_of: "s40879-023-00706-0"
---
polygon to the R&R model of the curve, and this gives us a concrete expression for the
remaining geometric points.
Proposition 3.8. The face-centres are exactly the points ﬁxed by an order-5 automorphism
of the curve. They are given in the P4-model by the permutations of [1 : ζ : ζ 2 : ζ 3 : ζ 4].
The corresponding points in the HC-model are the desingularizations of Vk, together with a,
b, c, d, and
(1) [−2ζ 3− 2ζ 2 :ζ 3 +ζ 2− 1 : 1] = [
√
5 + 1 :−
√
5/2− 3/2 : 1] = [2j :j′− 2 : 1],
(2) [−2ζ 3− 2 :−2ζ 3−ζ− 1 : 1],
(3) [−2ζ 2− 2ζ :−ζ 3 +ζ + 1 : 1],
13The osculating plane at a pointP on a curve is the limiting plane through P ,P ′,P ′′ asP ′,P ′′→P
on the curve [Sal62].
18 H. W. BRADEN AND LINDEN DISNEY-HOGG
(4) [2ζ 3 + 2ζ 2 + 2ζ :ζ 3 + 2ζ 2 + 2ζ + 1 : 1],
(5) [−2ζ 2− 2 :ζ 3−ζ 2 +ζ : 1],
(6) [2ζ 3 + 2ζ + 2 :ζ 2−ζ + 1 : 1],
(7) [−2ζ 3− 2ζ : 2ζ 3 +ζ 2 +ζ + 2 : 1]
(8) [2ζ 3 + 2ζ 2 + 2 :−ζ 3−ζ 2− 2 : 1] = [−
√
5 + 1 :
√
5/2− 3/2 : 1] = [2j′ :j− 2 : 1],
(9) [2ζ 2 + 2ζ + 2 :−ζ 3− 2ζ 2−ζ : 1],
(10) [−2ζ− 2 :−ζ 2− 2ζ− 1 : 1],
wherej,j′ are the roots identiﬁed by Dye mentioned in §2.3.
Proof. Certainly the order-5 rotation about a face-centre ﬁxes that centre, and so a Riemann-
Hurwitz counting argument gives us that the 24 face-centres are the ﬁxed points of order-5
automorphisms. It is a simple matter of computation to verify the given expressions are
ﬁxed; this may be done in Sage. □
The Galois group Gal( Q[ζ]/Q)∼= C4 acts element-wise on the face-centres and the or-
bits partition the set of face-centres into 6 sets of 4. Each set of 4 face-centres form the
vertices of a quadrilateral whose edges lie in {H2 = 0} [Edg78]. Moreover, the faces of the
dodecadodecahedron corresponding to the face-centres in each quadrilateral are parallel.
We have a similar result for the vertices.
Proposition 3.9. The vertices are exactly the points ﬁxed by an order-4 automorphism of
the curve. They are given in the P4-model by the permutations of [1 :i :−1 :−i : 0].
We could use our birational map as above to give the vertices in HC coordinates, but
these are not very illuminating. For example, that vertex [1 : i :−1 :−i : 0] maps to
[X :Y :Z] = [(3ζ 3−ζ 2 + 2ζ + 1)i + 3ζ 3 + 3ζ 2 + 5 : (2ζ 3 + 2ζ + 1)i + 2ζ 3 + 2ζ 2 + 2 : 1]
though [1 :−1 :i :−i : 0] maps to [1 : (−1 +i)/2 : (−1 +i)/2].
