---
doc_id: arxiv-2411.03801v2
doc_title: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS"
section_id: sec-003-22-essential-open-diagrams-and-their-potential
section_title: "Essential open diagrams and their potential"
section_number: 2.2
pages: 5-7
source_pdf: 2411.03801v2.pdf
source_sha256: a7f1f6fa74cb0949
doc_brief: "1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS — Motivated by the conjectured asymptotics of the Kashaev invariant, Dimofte and the first author introduced a power series associated to a suitable ideal"
---
invariant discussed below is the set of essential open diagrams of knots. An open diagram is
a planar diagram of a (1, 1)-tangle and is said to be essential if the corresponding collapsed
triangulation is essential. We postpone a detailed description of the collapsed ideal triangu-
lation to Section 3. Roughly, this is a story of how to pass from a planar diagram of a knot
to an ideal triangulation of its complement and use it to determine the complete hyperbolic
structure of a hyperbolic knot. Like so many things in hyperbolic geometry, this method
goes back to Thurston.
We here recall a potential function associated to an open diagram, introduced by Yokota
[Yok02] and motivated by the R-matrix state-sum formulas for the Kashaev invariant of a
knot.
In what follows, we fix an open diagram ˚D of a hyperbolic knot K inS3, that is, a planar
projection of a (1, 1)-tangle whose closure is K. For technical reasons, we will assume that
(†) starting from one endpoint of ˚D, we overpass the first crossing, and from the other
endpoint, we underpass the first crossing.
Viewing ˚D as an embedded 4-valent graph with two univalent vertices in R 2,
• a segment refers to an edge of the graph that is not adjacent to a univalent vertex,
• a region refers to a connected component of the complement of the graph, and
• a corner refers to a fan-shaped area around a crossing separated by segments.
6 STA VROS GAROUF ALIDIS AND SEOKBEOM YOON
We assign the constant 1 to every segment of ˚D adjacent to the unbounded region. Also,
starting from an endpoint of ˚D, if we underpass (resp., overpass) the first crossing, we assign
the constant∞ (resp., 0) to each segment until we encounter an overpass (resp., underpass).
To each segment not assigned a constant, we assign a variable so that every segment receives
either a constant or a variable. For a non-alternating diagram, consecutive segments could
be assigned with∞. If it is the case, for each crossing lying between such segments, we set
two adjacent variables, other than∞, to be equal. We do the same for consecutive segments
assigned with 0.
Example 2.4. An essential open diagram for the 6 1 knot, along with an assignment of
variables to its segments is shown in Figure 2.
x1
∞
x2
x3
0 1
1
1
1
1
1
Figure 2. An open diagram of the knot 6 1 with 3 variables x1, x2, x3 and 8
essential corners marked in red.
We now define the potential functionV of ˚D, following Yokota. We associate a dilogarithm
function with each corner as in Figure 3. Such dilogarithms could be ill-defined or constant.
This happens precisely when either x or y in Figure 3 is 0 or ∞, or when both x and y are
1. We say that a corner is essential if it is not the case, i.e. if the associated dilogarithm
is well-defined and non-constant. The Yokota potential function V is defined as the sum of
those dilogarithms over all essential corners.
x y
Li2
x
y

x y
−Li2
y
x

Figure 3. Dilogarithm functions associated with corners.
We now discuss a key point, namely an isomorphism of the critical points of the potential
function V with the solutions to the gluing and completeness equations of the collapsed
1-LOOP EQUALS TORSION FOR TWO-BRIDGE KNOTS 7
triangulationT˚D; see [MY18, Thm.4.1]. Here a critical point of V means a point x =
(x1,...,x n)∈ C n satisfying
exp

xi
∂V
∂xi

= 1, i = 1,...,n. (4)
Under this isomorphism, the essential corners of ˚D are in bijection with the tetrahedra
ofT˚D, and the the variables of the Yokota potential function are related to the shapes
of the tetrahedra of T˚D according to Figure 4. In particular, if ˚D is essential, there is
a geometric solution x◦ = (x◦
1,...,x ◦
n) to Equation (4) which gives rise to the complete
hyperbolic structure ofT˚D.
x y
0
∞
x y
Figure 4. An ideal tetrahedron at an essential corner.
Example 2.4 continued. The diagram in Figure 2 has 8 essential corners marked by red
and the Yokota potential function is given by
V = Li 2 (x1)− Li2
 1
x1

+ Li2
x2
x1

− Li2 (x2)
− Li2
 1
x2

+ Li2
x3
x2

− Li2 (x3)− Li2
 1
x3

.
The critical point equations (4) are given by
−x1 +x2
(−1 +x1)2 = 1, x1(x2−x3)
−x1 +x2
= 1, x2x3
−x2 +x3
= 1,
and equivalently, in the form
2− 5x1 + 6x2
1− 3x3
1 +x4
1 = 0, x 2 = 1−x1 +x2
1, x 3 = 1
2(1 + 2x1−x2
1 +x3
1) (5)
and the geometric solution is approximately
x◦≈ (0.895123− 1.552491i,−1.504108− 1.226851i,−0.677958− 0.157779i). (6)
