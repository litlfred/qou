---
doc_id: 210811825v1
doc_title: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups"
section_id: sec-015-fenchel-nielsen-parameters-of-the-klein-quartic
section_title: "Fenchel-Nielsen parameters of the Klein quartic"
section_number: null
pages: 100-103
source_pdf: 2108.11825v1.pdf
source_sha256: 1c2a4b317d6239c5
toc_source: outline
doc_brief: "Properties of Eigenvalues on Riemann Surfaces with Large Symmetry Groups — 26 sections: Front matter; Introduction; Background"
---
Fenchel-Nielsen parameters of the Klein quartic
To discuss Fenchel-Nielsen parameters, we ﬁrst need to introduce the notion of a pants
decomposition. A pair of pants (sometimes called a Y-piece) is the simplest hyperbolic
surface; topologically, it is a sphere with three disks removed. A compact Riemann surface
of genus g ≥2 can be decomposed into pairs of pants by cutting along 3g −3 simple,
closed, non-intersecting geodesics. These geodesics form the boundaries of each pair of
pants. A pair of pants has a speciﬁc geometry; we can form them by gluing together two
right-angled (hyperbolic) hexagons, where alternate sides of each hexagon will be equal
to half the length of one of the boundary geodesics of the pair of pants. The lengths of
the sides in between these curves are ﬁxed, since a geodesic joining two other geodesics
90
perpendicularly is unique. This construction is shown in Figure 4.3; the bold curves on
the pair of pants (on the left) are the boundary curves γi, i ∈{1, 2, 3}, with length
li = l(γi). The pants are obtained by gluing two copies of the hexagon on the right along
the dashed lines. The bold curves in the hexagon have length li
2 . A complete derivation of
the geometry of hyperbolic hexagons, staring from a hyperbolic triangle, is given in [13].
This is also an excellent reference for the ﬁne details of pants decompositions.
Figure 4.3: A hyperbolic pair of pants can be split into two identical hexagons
The Teichmüller space Tg is the space of all Riemann surfaces of genus g up to marking
equivalence. We will not go into depth here, but again, [13] provides a thorough intro-
duction to this theory. The Fenchel-Nielsen parameters are a set of 6g −6 coordinates
that completely classify a surface in Teichmüller space. Knowing the lengths of these
geodesics provides half of these parameters. Additionally, for each geodesic we need to
know whether it is twisted at all before being glued back together. This means that we
also have 3g −3 twist parameters. The Fenchel-Nielsen parameters (or coordinates) are
given as
{l1, t1, . . . , l3g−3, t3g−3},
where li and ti, i ∈{1, . . . , 3g −3}, respectively denote the length and twist parameters
of a geodesic γi.
To obtain a decomposition of the Klein quartic into four pairs of pants, simply take
six non-intersecting curves of length equal to the systole, as is shown in Figure 4.2. This
decomposition is described in [44], along with a decomposition into hexagons that are
not right-angled. The latter decomposition is interesting in that all the twist parameters
are zero. An inspection of the number of regular heptagons enclosed by the curves in
Figure 4.2 conﬁrms that each pair of pants contains six heptagons. A heptagon is made
up of 14 triangles of area
π
42. Therefore each pair of pants has area
6(14)
 π
42

= 2π.
91
Figure 4.4: Calculating the twist parameter t1 of γ1
t1
γ1
γ2
γ3
γ3
γ4
This is the correct area for a pair of pants having constant negative curvature.
We now calculate the six twist parameters. We start with the ‘central’ pair of pants,
bounded by the geodesics γ1, γ2, and γ3 in Figure 4.4. We draw the unique geodesic
segment that meets γ1 and γ2 perpendicularly. To calculate the twist parameter t1 of γ1,
consider the other pair of pants for which γ1 is a boundary (the other two boundaries are
γ4 and γ5). We draw the unique geodesic segment that meets γ1 and γ4 perpendicularly.
When we twist along γ1, we want the two perpendicular sections (dashed lines in the
ﬁgure) to match up. The twist parameter for γ1 is the distance along the γ1 between the
points where it intersects the perpendicular geodesics. Simply by examining Figure 4.2,
we see that this is 1
8 of the systole. Therefore
t1 = arccosh
3
2 −2 sin2 π
7

≈0.4919932811037915.
We can play a similar game with the other boundary curves to conclude that the twist
parameters for each curve will be the same, that is, 1
8 of the systole. Therefore, we have
a complete set of Fenchel-Nielsen coordinates for the Klein quartic:

s(K), s(K)
8
, s(K), s(K)
8
, s(K), s(K)
8
, s(K), s(K)
8
, s(K), s(K)
8
, s(K), s(K)
8

,
where s(K) is the systole of K.
92
