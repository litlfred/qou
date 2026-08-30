---
doc_id: s40879-023-00706-0
doc_title: "Bring's curve: old and new"
section_id: sec-007-32-vertices-and-face-centres
section_title: "Vertices and face-centres"
section_number: 3.2
pages: 22-23
source_pdf: s40879-023-00706-0.pdf
source_sha256: 4c5af312d2e5d6a7
doc_brief: "Bring's curve: old and new — Bring’s curve, the unique Riemann surface of genus 4 with automorphism group S5, has many exceptional properties."
---
Using [8, Figure 2] we are able to link the Petrie polygon to the R&R model of the
curve, and this gives us a concrete expression for the remaining geometric points.
Proposition 3.8 The face-centres are exactly the points ﬁxed by an order- 5 auto-
morphism of the curve. They are given in the P4-model by the permutations of
[1: ζ : ζ 2 : ζ 3 : ζ 4]. The corresponding points in the normalisationB of the HC-model
are the desingularizations of Vk , together with a, b, c, d, and
•[ − 2ζ 3 − 2ζ 2 : ζ 3 + ζ 2 − 1: 1]=[
√
5 + 1:−
√
5/2 − 3/2 : 1]=[ 2 j : j′− 2 : 1],
•[ − 2ζ 3 − 2 :− 2ζ 3 − ζ − 1: 1],
•[ − 2ζ 2 − 2ζ :− ζ 3 + ζ + 1: 1],
•[ 2ζ 3 + 2ζ 2 + 2ζ : ζ 3 + 2ζ 2 + 2ζ + 1: 1],
•[ − 2ζ 2 − 2 : ζ 3 − ζ 2 + ζ : 1],
16 The osculating plane at a point P on a curve is the limiting plane through P, P′, P′′as P′, P′′→ P on
the curve [55].
123
Bring’s curve: old and new Page 23 of 46 3
•[ 2ζ 3 + 2ζ + 2 : ζ 2 − ζ + 1: 1],
•[ − 2ζ 3 − 2ζ : 2ζ 3 + ζ 2 + ζ + 2 : 1]
•[ 2ζ 3+2ζ 2+2 :− ζ 3−ζ 2−2 : 1]=[ −
√
5+1:
√
5/2−3/2 : 1]=[ 2 j′: j−2 : 1],
•[ 2ζ 2 + 2ζ + 2 :− ζ 3 − 2ζ 2 − ζ : 1],
•[ − 2ζ − 2 :− ζ 2 − 2ζ − 1: 1],
where j , j′are the roots identiﬁed by Dye mentioned in Sect. 2.3.
Proof Certainly the order-5 rotation about a face-centre ﬁxes that centre, and so a
Riemann–Hurwitz counting argument gives us that the 24 face-centres are the ﬁxed
points of order-5 automorphisms. It is a simple matter of computation to verify the
given expressions are ﬁxed; this may be done in Sage.
The Galois group Gal (Q[ζ]/Q) ∼= C4 acts element-wise on the face-centres and
the orbits partition the set of face-centres into six sets of 4. Each set of four face-centres
form the vertices of a quadrilateral whose edges lie in {H2 = 0} [24]. Moreover, the
faces of the dodecadodecahedron corresponding to the face-centres in each quadrilat-
eral are parallel.
We have a similar result for the vertices.
Proposition 3.9 The vertices are exactly the points ﬁxed by an order- 4 auto- mor-
phism of the curve. They are given in the P
4-model by the permutations of
[1: i :− 1:− i : 0].
We could use our birational map as above to give the vertices in HC coordinates,
but these are not very illuminating. For example, that vertex [1: i :− 1:− i : 0] maps
to
[X : Y : Z]=
[
(3ζ 3 − ζ 2 + 2ζ + 1)i + 3ζ 3 + 3ζ 2 + 5: (2ζ 3 + 2ζ + 1)i
+ 2ζ 3 + 2ζ 2 + 2 : 1
]
though [1:− 1: i :− i : 0] maps to [1: (− 1 + i)/2 :(− 1 + i)/2].
