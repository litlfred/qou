---
doc_id: poincare-proof-outline
doc_title: "Poincaré Disc Model"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
---
Poincaré Disc Model
Danijela Simić
Filip Marić
Pierre Boutry
February 6, 2026
Abstract
We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL
proof assistant. The model is deﬁned within the extended complex plane (one dimensional complex projective
space CP 1), formalized in the AFP entry “Complex Geometry” [6]. Points, lines, congruence of pairs of
points, betweenness of triples of points, circles, and isometries are deﬁned within the model. It is shown that
the model satisﬁes all Tarski’s axioms except the Euclid’s axiom. It is shown that it satisﬁes its negation
and the limiting parallels axiom (which proves it to be a model of hyperbolic geometry).
Contents
1
Introduction
3
2
Background theories
3
2.1
Hyperbolic Functions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
3
3
Tarski axioms
4
4
H-lines in the Poincaré model
5
4.1
Deﬁnition and basic properties of h-lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
5
4.1.1
Collinear points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
4.1.2
H-lines and inversion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
4.1.3
Classiﬁcation of h-lines into Euclidean segments and circles . . . . . . . . . . . . . . . . .
7
4.1.4
Points on h-line . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
8
4.1.5
H-line uniqueness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
11
4.1.6
H-isometries preserve h-lines
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.1.7
Mapping h-lines to x-axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.2
Construction of the h-line between the two given points
. . . . . . . . . . . . . . . . . . . . . . .
17
4.2.1
Correctness of the construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
4.2.2
Existence of h-lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
4.2.3
Uniqueness of h-lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
4.2.4
Some consequences of line uniqueness
. . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
4.2.5
Transformations of constructed lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
4.2.6
Collinear points and h-lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
4.2.7
Points collinear with 0 h . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
32
4.3
Ideal points of h-lines
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
4.3.1
Calculation of ideal points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
34
4.3.2
Ideal points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
39
5
H-distance in the Poincaré model
44
5.1
Distance explicit formula . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
48
5.2
Existence and uniqueness of points with a given distance . . . . . . . . . . . . . . . . . . . . . . .
54
5.3
Triangle inequality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
6
H-circles in the Poincaré model
67
6.1
Intersection of circles in special positions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
71
6.2
Congruent triangles
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
74
1
7
H-betweenness in the Poincaré model
77
7.1
H-betwenness expressed by a cross-ratio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
7.1.1
H-betwenness is preserved by h-isometries . . . . . . . . . . . . . . . . . . . . . . . . . . .
77
7.1.2
Some elementary properties of h-betwenness . . . . . . . . . . . . . . . . . . . . . . . . . .
78
7.1.3
H-betwenness and h-collinearity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
78
7.1.4
H-betweeness on Euclidean segments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
79
7.1.5
H-betweenness and h-collinearity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
86
7.2
Some properties of betweenness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
87
7.3
Poincare between - sum distances . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
89
7.4
Some more properties of h-betweenness. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
94
8
Intersection of h-lines with the x-axis in the Poincaré model
96
8.1
Betweeness of x-axis intersection
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
96
8.2
Check if an h-line intersects the x-axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
97
8.3
Check if a Poincaré line intersects the y-axis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
8.4
Intersection point of a Poincaré line with the x-axis in the unit disc . . . . . . . . . . . . . . . . . 101
8.5
Check if an h-line intersects the positive part of the x-axis . . . . . . . . . . . . . . . . . . . . . . 105
8.6
Check if an h-line intersects the positive part of the y-axis . . . . . . . . . . . . . . . . . . . . . . 108
8.7
Position of the intersection point in the unit disc . . . . . . . . . . . . . . . . . . . . . . . . . . . 110
8.8
Ideal points and x-axis intersection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 112
9
H-perpendicular h-lines in the Poincaré model
114
10 Poincaré disc model types
124
10.1 H-points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
10.2 H-lines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
10.3 H-collinearity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
10.4 H-isometries . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 125
10.5 H-distance and h-congruence
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 126
10.6 H-betweennes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
11 Poincaré model satisﬁes Tarski axioms
127
11.1 Pasch axiom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
11.2 Segment construction axiom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
11.3 Five segment axiom
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 140
11.4 Upper dimension axiom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 141
11.5 Lower dimension axiom
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
11.6 Negated Euclidean axiom
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 143
11.7 Continuity axiom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 150
11.8 Limiting parallels axiom . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157
11.9 Interpretation of locales . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 170
2
1
