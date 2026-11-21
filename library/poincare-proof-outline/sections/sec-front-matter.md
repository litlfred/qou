---
doc_id: poincare-proof-outline
doc_title: "Formalization of the Poincare disc model of hyperbolic geometry"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: POINCARE-proof-outline.pdf
source_sha256: 8ac25ddb38d360b4
toc_source: outline
doc_brief: "Formalization of the Poincare disc model of hyperbolic geometry — We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL proof assistant."
---
Poincaré Disc Model

Danijela Simié Filip Marié Pierre Boutry

February 6, 2026

Abstract

We describe formalization of the Poincaré disc model of hyperbolic geometry within the Isabelle/HOL
proof assistant. The model is defined within the extended complex plane (one dimensional complex projective
space CP’), formalized in the AFP entry “Complex Geometry” [6]. Points, lines, congruence of pairs of
points, betweenness of triples of points, circles, and isometries are defined within the model. It is shown that
the model satisfies all Tarski’s axioms except the Euclid’s axiom. It is shown that it satisfies its negation
and the limiting parallels axiom (which proves it to be a model of hyperbolic geometry).

Contents
1 Introduction 3
2 Background theories 3
2.1 Hyperbolic Functions. 2... 0 ee 3
3 Tarski axioms 4
4 H-lines in the Poincaré model 5
4.1 Definition and basic properties of h-lines. 2... 0 ee 5
4.1.1 Collinear points. ......... 7
4.1.2 H-lines and inversion. . 2... 7
4.1.3 Classification of h-lines into Euclidean segments and circles .. 2.2... 022000008 7
4.1.4 Pointsonh-line... 2.2... 8
4.1.5 H-line uniqueness... 2... 11
4.1.6 H-isometries preserve h-lines 2.2... 2. 14
4.1.7 Mapping h-lines to x-axis 2... 16
4.2 Construction of the h-line between the two given points .. 2... 0.0.00. 00.000. ae 17
4.2.1 Correctness of the construction... 20
4.2.2 Existence of h-lines. 2... ee 28
4.2.3 Uniqueness of h-lines. 2... ee 29
4.2.4 Some consequences of line uniqueness . 2... 0... ee 30
4.2.5 Transformations of constructed lines . 1... ee 31
4.2.6 Collinear points and h-lines .. 1... ee 32
4.2.7 Points collinear with 0, 2... ee 32
4.3. Ideal points of h-lines 2... ee 34
4.3.1 Calculation of ideal points... ee 34
4.3.2 Ideal points... 39
5 H-distance in the Poincaré model 44
5.1 Distance explicit formula... ........... 48
5.2 Existence and uniqueness of points with a given dis 54
5.3 Triangle inequality 2... ee 65
6 H-circles in the Poincaré model 67
6.1 Intersection of circles in special positions. ©... ee 71
6.2 Congruent triangles 2... 0. ee 74
7 H-betweenness in the Poincaré model 77

7.1 H-betwenness expressed by a cross-ratio 2... ee 77
7.1.1 H-betwenness is preserved by h-isometries . 2... 0. ee 77
7.1.2 Some elementary properties of h-betwenness. . . 78
7.1.3 H-betwenness and h-collinearity. ......... 78
7.1.4 H-betweeness on Euclidean segments ....... 79
7.1.5 H-betweenness and h-collinearity 2... ee 86
7.2 Some properties of betweenness .. 2... 87
7.3 Poincare between - sum distances... 2... 89
7.4 Some more properties of h-betweenness. .. 2... 0 94
8 Intersection of h-lines with the x-axis in the Poincaré model 96
8.1 Betweeness of x-axis intersection 2.2... 96
8.2 Check if an h-line intersects the x-axis 2... ee 97
8.3 Check if a Poincaré line intersects the y-axis. 2... ee 100
8.4 Intersection point of a Poincaré line with the x-axis in the unit disc... 2.2... 02... 0 ee 101
8.5 Check if an h-line intersects the positive part of the x-axis... . ee eee 105
8.6 Check if an h-line intersects the positive part of the y-axis... 2... ...0040. 108
8.7 Position of the intersection point in the unit disc .... 110
8.8 Ideal points and x-axis intersection... 2... en 112
9 H-perpendicular h-lines in the Poincaré model 114
10 Poincaré disc model types 124
10.1 H-points.. 2... ee 124
10.2 H-lines. 2... 2.2... 124
10.3 H-collinearity ....... 125
10.4 H-isometries. 2... 2. ee 125
10.5 H-distance and h-congruence ............... 126
10.6 H-betweennes . 2... ee 127
11 Poincaré model satisfies Tarski axioms 127
11.1 Pasch axiom. 2... ee 127
11.2 Segment construction axiom... ee 138
11.3 Five segment axiom ©... 140
11.4 Upper dimension axiom... 2... ee 141
11.5 Lower dimension axiom . 2... ee 143
11.6 Negated Euclidean axiom 2... 143
11.7 Continuity axiom... ee

11.8 Limiting parallels axiom .
11.9 Interpretation of locales
