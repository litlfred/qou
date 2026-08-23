---
doc_id: arxiv-math-0008040v1
doc_title: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A"
section_id: sec-008-2-f3f1-similarly-there-is
section_title: "F3F1. Similarly, there is"
section_number: 2
pages: 10-13
source_pdf: 0008040v1.pdf
source_sha256: a72319b55dbaf20b
doc_brief: "Rectangle diagrams for the Lusztig cones of quantized enveloping algebras of type A — Let U be the quantum group associated to a Lie algebra g of type An."
---
a corresponding monomial in the Kashiwara operators which w e denote ~F (P ). So in our example,
~F (LRL−) = ~F4 ~F5 ~F2 ~F 2
3 ~F4 ~F1 ~F 2
2 ~F3 ~F1 · 1.
10
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
◦
8
7
6
5
4
3
2
1
1
2
3
4
5
6
7
8
R
R
L
L
R
L
L
R
L
L
R
R
....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... .................................................................................
................................................................................................................................................................. ...................................................................................................................................................................................................................................................................................................................................................................................................................
.................................................................................................................................................................................................................................................................................................................................. .................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... ..................................................................................................................................................................................................................................................................................................................................
................................................................................................................................................................. ...................................................................................................................................................................................................................................................................................................................................................................................................................
................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................... .................................................................................
....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
...............................................................................................................................................................................................................................................................
...............................................................................................................................................................................................................................................................
...............................................................................................................................................................................................................................................................
...............................................................................................................................................................................................................................................................
•
•
•
•
•
•
•
•
•3
2
1
4
3
2
5
4
3
A
BC
D
Figure 6: Example: Q =RRLLRL,Y = − −LL − −.
The following theorem was conjectured by Carter:
Theorem 5.3 Suppose i ∈χ n is compatible with a quiver Q, and let (c, i) be a chamber in CD (i).
LetP =P (c, i) be the corresponding partial quiver (so P ≤Q), with a =a(c, i) = (a1,a 2,... ,a k).
Alternatively, let P =j ∈ [1,n ]. In either case,
F (a1)
i1 F (a2)
i2 · · ·F (ak)
ik =F (P ).
In particular, the left hand side depends only upon P .
Proof: Suppose ﬁrst that P is a partial quiver, and let Y be a component of P . Our ﬁrst step
will be to understand where the roots in M (Y ) occur in CD( i) (as labels of crossings). Let us
suppose in the ﬁrst case that Y is of type L, with a =a(Y ) and b =b(Y ). We draw the diagram
for the arrangement corresponding to Q, deﬁned by Berenstein, Fomin and Zelevinsky. We mark
the crossing of strings i and j, i ≤ j by the root α ij = α i +α i+1 + · · · +α j−1, and we write the
quiver Q up the left hand side, so that edge j of Q appears next to the left hand end of string j,
for each j. We write Q down the right hand side also.
Draw 4 dashed lines on the diagram. The ﬁrst, A, should intersect the left vertical boundary
between strings a anda + 1, and go down and to the right at an angle of −π/ 4 (to the horizontal).
The next, B, should intersect the left vertical boundary between strin gs b and b − 1 and go up
and to the right at an angle of π/ 4. Line C should intersect the right vertical boundary between
strings a and a + 1 and go up and to the left at an angle of 3 π/ 4. Finally, line D should intersect
the right vertical boundary between strings b and b − 1, and go down and to the left, at an angle
of −3π/ 4. For an example, in type A7, where Q =RRLLRL andY = − −LL − −, with a(Y ) = 3
and b(Y ) = 6, see Figure 6.
These four dashed lines bound a rectangle in the diagram; we s hall see that the crossings inside it
form a rectangle, ρ, and that their labels are precisely the positive roots in M (Y ). (In the example,
these crossings are marked by ﬁlled circles.)
11
By construction, the lines crossing ρ parallel to A and C are parts of the strings c withc ≤a, and
the lines crossing ρ parallel to B and D are parts of the strings d with b ≤d. Thus the crossings
appearing inside ρ are those labelled with roots α cd with 1 ≤c ≤a ≤b ≤d ≤n + 1, that is, the
roots in M (Y ).
LetE be the line in the rectangle we are interested in which is para llel to C and closest to C, and
suppose it is part of string x and that this corresponds to an R in Q. Let y be the ﬁrst string
that x intersects with after changing direction at the top of the di agram. By the construction of
the diagram, the strings corresponding to the L’s ofY are below the rectangle, so y cannot be one
of these strings. Similarly, if y were a string corresponding to an L to the right of Y , it would be
parallel to E initially (i.e. in the left part of the diagram) and then woul d only be perpendicular
to E below ρ. Also, if y corresponded to an R to the right of Y in Q, x and y would intersect to
the left of the point where x changed direction. We conclude that x and y intersect inside ρ.
Thus in the corresponding chamber diagram, the top crossing of the rectangle is on row 1 (so the
corresponding simple reﬂection is s1). Suppose next that x corresponds to an L in Q. Let y be
the ﬁrst string that x intersects. Since there can in this case be no R’s to the right of Y in Q,
x intersects every string corresponding to an arrow of Q to the right of Y below the rectangle ρ;
similarly with the L’s inY . Thus y is to the left of P and x and y intersect in the rectangle.
Thus in both cases the top corner of the rectangle ρ is in row 1. Let us write the row of each
crossing in ρ next to it. The number of crossings in a side of the rectangle p arallel to A orC (equal
to the number of crossings involving E inside ρ) is equal to n + 2 −b, and the number in a side
parallel to B or D is a. Thus the labels of the crossings inside ρ are the same and in the same
conﬁguration as the numbers in ρ(Y ).
The case when Y is of type R is similar; in this case the bottom corner of the rectangle in the
arrangement diagram is labelled n.
Now suppose that Y is of type L and immediately to the right of Y inP is a component Z of type
R. By the construction of the rectangles, the leftmost crossi ngs inside them coincide. Similarly, if
Y is of type R and Z is of type L, the rightmost crossings in the rectangles coincide.
Thus the structure of the rectangles corresponding to compo nents of P in the arrangement dia-
gram, or the chamber diagram, corresponding to i, is the same as in D(P ). The result follows by
Theorem 3.1.
In the case where P = j ∈ [1,n ], let Y = j; here we consider Y to be the vertex j of Q, with no
edges. We then argue as in the above proof for Y of type L. □
Corollary 5.4 Suppose we are in the situation of the Theorem, and let ~F (P ) be the monomial in
the root operators as deﬁned in 5.2. Then ~F a1
i1
~F a2
i2 · · · ~F ak
ik · 1 = ~F (P ).
Proof: This follows immediately from the Theorem, since the only r elations in U − that are used
are commutations, which the root operators ~Fi also satisfy. □
12
D(LRL−) =
4
3
2
1
................................................................................................................................................................. ......................................... ................................................................................................................................................................. .........................................
5
4
3
......................................................................................................................... ................................................................................. ......................................................................................................................... .................................................................................
2
1
................................................................................. ......................................................................................................................... .................................................................................
........................................................................................................................................................................................................
L1
R1
L2
Figure 7: The central line in D(LRL−).
