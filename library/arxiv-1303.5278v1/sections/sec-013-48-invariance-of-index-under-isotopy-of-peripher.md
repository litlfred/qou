---
doc_id: arxiv-1303.5278v1
doc_title: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD"
section_id: sec-013-48-invariance-of-index-under-isotopy-of-peripher
section_title: "Invariance of index under isotopy of peripheral curve"
section_number: 4.8
pages: 26-29
source_pdf: 1303.5278v1.pdf
source_sha256: 92e417c93f8b883a
doc_brief: "1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD — In this paper we will promote the 3D index of an ideal triangulation T of an oriented cusped 3-manifold M (a collection of"
duplicate_of: "topologicalinvariance3dindex"
---
Theorem 4.7.Letϖ be an oriented simple closed curveϖ in ∂M which is a normal curve
relative to the triangulationT∂ of ∂M. Then the indexIT(ϖ) is invariant under isotopy of
the curveϖ in ∂M.
Proof. Suppose we have two isotopic oriented normal curvesϖ1,ϖ 2. Then we can convert
one into the other via a sequence of moves (and their inverses) of the form shown in Figure
11. That is, we choose a pointp on the curveϖ and an arcα, disjoint fromϖ other than at
p, and which joinsp to either a vertex or a point in the interior of an edge ofT∂. We then
push the curve along and in a regular neighbourhood ofα over the vertex or edge.
Figure 11. The two kinds of isotopy move on a curve relative to the trian-
gulation of∂M.
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 27
We will show thatIT(ϖ) is invariant under these moves. Note that the result of these
isotopies will not in general be normal curves, so we need to extend the deﬁnition of the
index to deal with these cases as well. The class of curves we work in consists of oriented
simple closed curves, transverse toT(1)
∂ and disjoint fromT(0)
∂ . For our purposes we will deal
only with curves that are non trivial inH1(∂M ), and so none of our curves is disjoint from
T(1)
∂ . Given such a curve, it enters a triangle somewhere on one edge, and can exit out either
of the two other edges, or the same edge that it entered, either to the left or the right of its
entry point. Thus there are four ways in which a component of a curve intersects a given
triangle. These contribute to the index in the following way. See Figure 12.
+ − ⊕ ⊖
Figure 12. The four ways in which a curve can travel through a triangle.
We call the last two possibilities apositive backtrack and negative backtrack
respectively.
If the curve turns either left or right around a corner of the triangle then it contributes
to the index in exactly the same way as for a normal curve: we add+1 to the entry in the
vector (¯aϖ|¯bϖ|¯cϖ) corresponding to the angle at the edge of the tetrahedron we are turning
around if we are going anticlockwise around the corner, and add−1 if we are going clockwise.
Compare with Figure 7.
Here we deﬁne the eﬀect of backtracks on the index calculation: (This is, of course, chosen
in such a way as to be consistent with the index calculated with curves without backtracks.)
We do not change the vector(¯aϖ|¯bϖ|¯cϖ). These backtracks only alter the power of(−q1/2),
either multiplying the expression by(−q1/2) for a positive backtrack (turning to the left),
or by(−q1/2)−1 for a negative backtrack (turning to the right). We indicate these using the
symbols⊕ and⊖.
Note that by (22), a positive backtrack has the same eﬀect on the index as anticlockwise
turns around each of the three corners of a triangle. Note also that by (25), an anticlockwise
loop around a vertex of the triangulation produces a power of(−q1/2)2. This follows since
adding an anticlockwise loop around an end of theith edge has the eﬀect of shifting the sum
by one in theki component. The terms are unchanged after shifting other than the term
q
∑
iki, and the eﬀect is to multiply the index byq.
Thus an anticlockwise loop around a vertex is cancelled by two negative backtracks, and
anticlockwiseturnsaroundeachofthethreecornersofatrianglearecancelledbyonenegative
backtrack.
Now all we need to do is to show that each version of the moves from Figure 11 preserves
the index, using the above rules. There are diﬀerent versions of the isotopy moves depending
on where the curve we are acting on enters or exits the triangle. We show the possibilities
in Figure 13. Here the +,−,⊕ and⊖ signs show the diﬀerencein the index calculation
28 STA VROS GAROUF ALIDIS, CRAIG D. HODGSON, J. HYAM RUBINSTEIN, AND HENRY SEGERMAN
+
+
+
+
+
+
⊖ ⊖
+
+
+
+
+
⊖
− −
+
+
+
+
+
+
⊖
⊖
+
+
+
+
+
⊖− −
+
+ +
⊖
⊕
⊖
⊖
⊕
⊖
⊕
⊖
⊖
⊕ ⊕ ⊖
⊕
Figure 13. Four cases of isotopy across a vertex and six cases of isotopy
across an edge. All other cases are symmetries of these.
under the isotopy as we change from one curve to the other in the direction following the
double head arrow. Note that reversing the arrow on the curve ﬂips all of the signs, as does
reﬂecting the picture. With combinations of these symmetries applied to the ten cases shown
we obtain all possible ways in which the isotopy can be made relative to the position of the
curve. Considering each case in turn, we can see that the signs cancel out and so the index
is unchanged by these moves.
For example, consider the second diagram in the top row of Figure 13. We start with a
curve that enters the right side of the triangle and exits the bottom. We isotope this curve
by pushing it over the top vertex of the triangle. This has the following eﬀects:
1-EFFICIENT TRIANGULATIONS AND THE INDEX OF A CUSPED HYPERBOLIC 3-MANIFOLD 29
• Remove an anticlockwise turn around the lower right corner of the triangle, this
changes the coeﬃcient at that angle by−1.
• Add a negative backtrack to the right edge of the triangle.
• Add an anticlockwise turn around each of the angles at the top vertex of the triangle
other than the top corner of the triangle itself.
• Add a clockwise turn around the lower left corner of the triangle.
We view the top corner of the triangle as having both a+ and a−, so that the total change
in the index calculation consists of one anticlockwise turn around a vertex, one negative
backtrack and clockwise turns around each of the three corners of the triangle. By our above
rules, these cancel out and so the index is unchanged. □
Remark 4.8. These calculations are exactly analogous to those for calculating the holonomy
of a peripheral curve given shapes of ideal hyperbolic tetrahedra satisfying Thurston’s gluing
equations. Thus this argument can easily be adapted to reprove the well-known fact that
the holonomy is independent of the choice of simple closed curve representing an element of
H1(∂M ; Z).
