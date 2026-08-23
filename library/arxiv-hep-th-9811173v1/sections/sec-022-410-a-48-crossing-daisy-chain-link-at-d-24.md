---
doc_id: arxiv-hep-th-9811173v1
doc_title: "b vol(M) = (−D)3/ 2 (2π)2n− 4 ζK(2) 2ζ(2) for a manifold M whose invariant trace ﬁeldK has a single complex place, discriminant D, degree n, and Dedekind zeta value ζK(2). The larg"
section_id: sec-022-410-a-48-crossing-daisy-chain-link-at-d-24
section_title: "A 48-crossing daisy-chain link at D = −24"
section_number: 4.10
pages: 12-13
source_pdf: 9811173v1.pdf
source_sha256: 986bf57947746523
doc_brief: "Determinations of rational Dedekind-zeta invariants of hyperbolic manifolds and Feynman knots and links — We identify 998 closed hyperbolic 3-manifolds whose volumes are ratio nally related to"
---
The attentive reader will now expect us to skip the case D = −23 and jump to the 8th
underlining in (19), at D = −24. This is precisely what we did, though the character of the
result was not what we ﬁrst supposed. It seemed to us that the ha llmark of past success,
in ﬁnding links that link Clausen values, was to achieve the largest poss ible symmetry
group. What, we asked ourselves, could pack a better symmetry- to-crossing ratio than
the remaining 4 platonic alternating links?
Let us denote the tetrahedral link of Fig. 1 by T := 24 10
tet. The 4 non-self-dual
alternating platonic links have components that mimic the vertices an d edges of the
cube C := 48 20
cub, octahedron O := 48 18
oct, dodecahedron D := 120 50
dod, and icosahedron
I := 120 42
ico, where, for example, the last has 120 alternating crossings of its 4 2-components,
which mimic the 12 vertices and 30 edges of the perfect solid with 20 fa ces. These links are
highly symmetrical, yet none of their 4 volumes yielded the sought-fo r rational relation
to a quadratic Dedekind zeta value. Later, we show that they are q uartic links.
Instead, we found an answer to our 8th question by a more child-like construction: a
non-alternating daisy chain. By a daisy chain we mean a link each of who se components
has 2 crossings with a neighbour on one side, and 2 crossings with a ne ighbour on the
other, with the whole forming a circle, as in Fig. 2. By a non-alternatin g daisy chain, we
mean one in which the 4 crossings of each component occur in an orde r over-over-under-
under, while still linking with neighbours. A little doodling should convince the reader
that non-alternating daisy-chain links must have an even number of components.
11
A delightful feature of Jeﬀ Weeks’ program SnapPea [21] is that it e nables one to draw
such chains quickly, and then ask whether the resultant non-alter nating link has quadratic
shapes in its triangulation. Using A.C. Manoharan’s port of SnapPea t o Windows95 12,
we inferred, from instances with up to 96 crossings, that the non- alternating daisy-chain
link with 2n ≥ 6 components, and hence 4 n ≥ 12 crossings, has hyperbolic volume
V2n = 8nD
(
i tan (n − 2)π
4n
)
(31)
The ﬁrst 4 hyperbolic non-alternating daisy chains yield results with −D ∈ {3, 4, 8, 20}:
V6 = 4 Z4 (32)
V8 = 2 Z8 (33)
V10 = 1
2Z20 +V6 (34)
V12 = 20 Z3 (35)
Then nothing interesting happens until we reach 24 components, w ith 48 crossings, where
V24 =Z24 +V8 (36)
hits the target, at D = −24.
SnapPea illustrates this nicely. Drawing daisy chains with 6, 8, 10, 12, 24 components,
and inspecting the triangulations, one detects the square roots o f 1, 2, 5, 3, 6. The last,
illustrated in Fig. 2, delivers a result for Z24 =V24 −V8, namely
60Cl2(θ3, 2)−18Cl2(2θ3, 2)−4Cl2(3θ3, 2)+3Cl2(4θ3, 2) = Z24 = 24
∑
k∈{ 1, 5, 7, 11}
Cl2
(
2πk
24
)
(37)
with θ3, 2 := 2 arctan
√
3/ 2. So, for the 6th time, we have a relation that is as easy to
check numerically as it appears hard to derive.
