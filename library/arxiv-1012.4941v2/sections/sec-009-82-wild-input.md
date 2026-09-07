---
doc_id: arxiv-1012.4941v2
doc_title: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS"
section_id: sec-009-82-wild-input
section_title: "Wild Input"
section_number: 8.2
pages: 18-20
source_pdf: 1012.4941v2.pdf
source_sha256: 1932a359f3bafb83
doc_brief: "ALGORITHMS FOR HIGHLY SYMMETRIC LINEAR AND INTEGER PROGRAMS — This paper deals with exploiting symmetry for solving linea r and integer programming problems."
---
algorithms is by brute force: One can take any system Ax≤b of linear inequalities and let
the full group Sym( n) act. This way each original inequality may give up to n! inequalities
in the resulting symmetrized system. The symmetrized system of inequalities is Sym( n)-
invariant by construction. In order to produce input to our algorit hms which is less well
behaved than the hypertruncated cubes studied above we will app ly this procedure to a
special class of polytopes, which can be considered “wild”. We aim at s ymmetric polytopes
with many facets whose coordinates are not so nice, but still somew hat under control.
SYMMETRIC LINEAR AND INTEGER PROGRAMS 19
Table 1. Hypertruncated Cubes
CPLEX polymake
d time LP (s) time IP (s) time LP (s) time IP (s)
100 0.00 0.07 0.01 0.08
200 0.07 0.29 0.02 0.57
300 0.19 0.73 0.03 1.88
400 0.41 1.58 0.06 4.26
500 0.90 2.99 0.10 8.39
600 1.52 4.80 0.14 14.30
700 2.21 7.01 0.18 22.29
800 3.44 11.59 0.24 32.96
900 5.17 16.37 0.31 47.11
1000 6.77 21.66 0.38 65.11
1100 8.25 26.55 0.47 85.52
1200 11.75 35.47 0.55 111.59
1300 14.05 45.63 0.65 142.76
1400 18.96 57.23 0.74 175.23
1500 23.42 73.50 0.85 217.19
1600 28.11 78.13 0.98 263.21
1700 32.07 97.23 1.11 315.38
1800 41.82 128.88 1.25 374.63
1900 44.68 137.22 1.40 444.48
2000 50.39 154.35 1.54 511.59
The ﬁrst building block of our construction is the regular hexagon H whose vertices are
at distance 56/6 from the origin, that is,
H = conv
{ 56
6 ekπi/6
⏐⏐⏐⏐k = 0, 1,..., 5
}
.
Notice that only in the formula above the letter ‘ i’ denotes the imaginary unit, and we
identify the complex numbers with R2. The coordinates of H are irrational; however, the
subsequent steps in the construction are chosen such that we will arrive at a rational polytope
in the end. The second item is the regular cross polytope scaled by 73 /10, that is,
C(d) = conv
{
± 73
10ei
⏐⏐⏐⏐i∈ [d]
}
.
Finally, we consider the join P∗Q of two polytopes P⊂ Rδ and Q⊂ Rǫ, which is deﬁned
as
P∗Q = conv
( {
(x, 0, 1)∈ Rδ× Rǫ× R
⏐⏐x∈P
}
∪
{
(0,y,−1)∈ Rδ× Rǫ× R
⏐⏐y∈Q
})
.
IfP andQ are full-dimensional polytopes with µ andν vertices, respectively, the join P∗Q
has dimension δ +ǫ + 1 and µ +ν vertices. For the combinatorics of P∗Q the exact values
for the (δ +ǫ + 1)st coordinate are inessential, as long as they are distinct. We no w replace
the “−1” for the second factor by −11/12 to obtain the distorted join
J(d) = conv
( {
(x, 0, 1)∈ R2× Rd× R
⏐⏐x∈H
}
∪
{
(0,y,− 11
12 )∈ R2× Rd× R
⏐⏐⏐⏐y∈C(d)
} )
20 RICHARD B ¨ODI, KATRIN HERR, AND MICHAEL JOSWIG
Table 2. Symmetrized distorted joins of a hexagon with cross-polytopes
CPLEX polymake
d time LP (s) time IP (s) time LP (s) time IP (s)
3 0.00 0.01 0.00 0.00
4 0.00 0.06 0.01 0.00
5 0.00 0.17 0.01 0.02
6 0.05 0.74 0.04 0.04
7 0.13 2.71 0.09 0.13
8 0.62 10.15 0.24 0.38
9 2.08 42.06 0.69 1.03
10 8.02 135.51 1.86 2.89
of the hexagon H with the cross polytope C(d). This polytope is further modiﬁed in two
steps: First we perturb by rounding the (rational and irrational) c oordinates to three decimal
places and treating these as exact rational numbers. Since the po lytopes H,C(d), and J(d)
are simplicial this perturbation does not change the combinatorial t ypes. Secondly, we
symmetrize the polytope by letting the group Sym( d + 3) act on the facets of the perturbed
polytope. The resulting inequalities form the input of our second clas s of experiments.
The parameters 56 /6, 73/10, and 11 /12 which occur in the construction are chosen,
more or less, at random. They do not have a speciﬁc meaning. We ref rain from further
investigating these symmetrized distorted joins and the geometry of lattice points inside.
This would be tedious and at the same time irrelevant for our purpose s.
The interesting fact is that we get symmetric polytopes which are so mewhat complicated,
because they have lots of inequalities: for instance, yielding 885 ,768 inequalities for d = 10.
As a consequence CPLEX cannot deal with these examples in a fully automated way. The
best parameter settings that we found were
parallel thread count: 1
presolve indicator: no
feas. pump heuristic: -1
RINS heuristic: -1
MIP optimization emph.: 2
But even with these adjustments our implementation outperforms CPLEX by a large margin;
see Table 2. This holds in spite of the fact that polymake computes with exact rational
numbers throughout.
