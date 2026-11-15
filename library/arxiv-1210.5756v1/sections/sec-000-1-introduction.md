---
doc_id: arxiv-1210.5756v1
doc_title: "Contact Graphs of Unit Sphere Packings Revisited ∗"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-3
source_pdf: 1210.5756v1.pdf
source_sha256: c7546a79a85b8dd5
toc_source: outline
doc_brief: "Contact Graphs of Unit Sphere Packings Revisited ∗ — The contact graph of an arbitrary ﬁnite packing of unit balls in Euclidean 3-space is the (simple) graph whose vertices correspond to the packing"
---
Introduction
Let Ed denote d-dimensional Euclidean space. Then the contact graph of an arbitrary ﬁnite packing of unit
balls (i.e., of an arbitrary ﬁnite family of non-overlapping balls having unit radii) in Ed is the (simple) graph
whose vertices correspond to the packing elements and whose two vertices are connected by an edge if and
only if the corresponding two packing elements touch each other. One of the most basic questions on contact
graphs is to ﬁnd the maximum number of edges that a contact graph of a packing of n unit balls can have in
Ed. In 1974 Harborth [7] proved the following optimal result in E2: the maximum number of touching pairs
in a packing of n congruent circular disks in E2 is precisely ⌊3n−√12n −3⌋. In dimensions three and higher
only estimates are known for the maximum number of touching pairs. In particular, just very recently the
ﬁrst named author [2] proved that the number of touching pairs in an arbitrary packing of n unit balls in E3
is always less than 6n −0.695n
2
3 . Moreover, it is proved in [1] that for d ≥4 the number of touching pairs
in an arbitrary packing of n unit balls in Ed is less than
1
2τd n −1
2d δ
−d−1
d
d
n
d−1
d ,
where τd stands for the kissing number of a unit ball in Ed (i.e., it denotes the maximum number of non-
overlapping unit balls of Ed that can touch a given unit ball in Ed) and δd denotes the largest possible density
for (inﬁnite) packings of unit balls in Ed. For a nice survey on recognition-complexity results of ball contact
graphs we refer the interested reader to [8].
In this paper, ﬁrst we improve the above quoted upper bound of [2] as follows.
∗Keywords: congruent sphere packing, touching pairs, triplets, quadruples, density, (truncated) Voronoi cell, union of balls,
isoperimetric inequality, spherical cap packing. 2010 Mathematics Subject Classiﬁcation: 52C17, 05B40, 11H31, and 52C45.
†Partially supported by a Natural Sciences and Engineering Research Council of Canada Discovery Grant.
‡Supported by an Undergraduate Student Research Award of the Natural Sciences and Engineering Research Council of
Canada.
1
arXiv:1210.5756v1  [math.MG]  21 Oct 2012
Theorem 1.
(i) The number of touching pairs in an arbitrary packing of n ≥2 unit balls in E3 is always less than
6n −0.926n
2
3 .
(ii) The number of touching pairs in an arbitrary lattice packing of n ≥2 unit balls in E3 is always less than
6n −3 3√
18π
π
n
2
3 = 6n −3.665 . . . n
2
3 .
In connection with Theorem 1 we recall from [2] that for all n = 2k3+k
3
, k ≥2, there are packings of n
unit balls in E3 such that the number of touching pairs is greater than 6n −
3√
486n
2
3 = 6n −7.862 . . . n
2
3 .
Second, as a natural extension of the above discussed problem on the number of touching pairs, we
propose to study the maximum number of touching triplets, quadruples, etc. in an arbitrary packing of n
unit balls in Ed. Harborth’s proof [7] implies in a straightforward way that the maximum number of touching
triplets in a packing of n congruent circular disks in E2 is precisely ⌊3n −√12n −3⌋−n + 1. In this paper
we study the 3-dimensional case of the problem at hand and prove the following estimates.
Theorem 2.
(i) The number of touching triplets (resp., quadruples) in an arbitrary packing of n ≥3 (resp., n ≥4) unit
balls in E3 is at most 25
3 n (resp., 11
4 n).
(ii) The number of touching triplets (resp., quadruples) in an arbitrary lattice packing of n ≥2 unit balls in
E3 is at most 8n (resp., 2n).
(iii) For all n = 2k3+k
3
, k ≥2, there are packings of n unit balls (with their centers lying on a face-centered
cubic lattice) in E3 such that the number of touching triplets (resp., quadruples) is
4
3(k −1)k(4k −5) > 8n −12
3
2n
2/3
+ 4n1/3
(resp., 4
3(k −2)(k −1)k > 2n −4(3
2n)2/3 + 2n1/3) .
Part (iii) of Theorem 2 raises the following question.
Problem 1. Prove or disprove the existence of a positive integer k3 (resp., k4) with the property that for
any positive integer k ≥k3 (rep., k ≥k4) the number of touching triplets (resp., quadruples) in an arbitrary
packing of 2k3+k
3
unit balls in E3 is at most 4
3(k −1)k(4k −5) (resp., 4
3(k −2)(k −1)k).
The proof of (i) in Theorem 2 is based on the following statement that might be of independent interest
in particular, because one can regard that statement as a spherical analogue of Harborth’s theorem [7] for
the angular radius π/6 (on the unit sphere S2 centered at the origin in E3).
Theorem 3. The number of touching pairs (resp., triplets) in an arbitrary packing of spherical caps of
angular radius π/6 on S2 is at most 25 (resp., 11).
In connection with Theorem 3 we put forward the following question.
Problem 2. Prove or disprove that the number of touching pairs (resp., triplets) in an arbitrary packing of
spherical caps of angular radius π/6 on S2 is at most 24 (resp., 10).
We note that a positive answer to Problem 2 implies the following improvement on the estimates in (i)
of Theorem 2: the number of touching triplets (resp., quadruples) in an arbitrary packing of n unit balls in
E3 is at most 8n (resp., 5
2n).
Due to the Minkowski diﬀerence body method (see for example, Chapter 6 in [13]) the family PK :=
{t1 +K, t2 +K, . . . , tn +K} of n translates of the convex body K in E3 is a packing if and only if the family
PKo := {t1+Ko, t2+Ko, . . . , tn+Ko} of n translates of the symmetric diﬀerence body Ko := 1
2(K+(−K))
of K is a packing in E3. Moreover, the number of touching pairs, triplets, and quadruples in the packing PK
is equal to the number of touching pairs, triplets, and quadruples in the packing PKo. Thus, for this reason
and for the reason that if K is a convex body of constant width in E3, then Ko is a ball of E3, Theorem 1
2
as well as Theorem 2 extend in a straightforward way to translative packings of convex bodies of constant
width in E3.
The rest of the paper is organized as follows. In Section 2 we prove (i) of Theorem 1. Section 3 proves
(ii) of Theorem 1 as well as (ii) of Theorem 2. In Section 4 we give a short proof of (i) in Theorem 2 using
Theorem 3. Sections 5 and 6 present our elementary and somewhat computational proof of Theorem 3.
Finally, Section 7 gives a proof of (iii) in Theorem 2 as well as shows that if Problem 2 has a positive
answer, then its estimates are tight.
