---
doc_id: arxiv-1202.6268v2
doc_title: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS"
section_id: sec-020-36-invariance-under-23-moves
section_title: "Invariance under 2–3 moves"
section_number: 3.6
pages: 19-22
source_pdf: 1202.6268v2.pdf
source_sha256: 209af6ae25439050
doc_brief: "THE QUANTUM CONTENT OF THE GLUING EQUATIONS — The gluing equations of a cusped hyperbolic 3-manifold M are a system of polynomial equations in the shapes of an ideal triangulation T of M that"
---
invariance ofτT under 2–3 moves. We set up the problem as in Figure 7. Namely, we suppose
that M has two diﬀerent regular triangulations T and ~T , with N and N + 1 tetrahedra,
respectively, which are related by a local 2–3 move. Let us denote t he respective (triples of)
shape parameters as
(3.19) Z := (X1,X 2,Z 3,...,Z N ), ˜Z := (W1,W 2,W 3,Z 3,...,Z N ).
20 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
We ﬁx a quad type, labeling the ﬁve tetrahedra involved in the 2–3 mov e as in the ﬁgure.
We will also assume that when calculating Neumann-Zagier matrices A and B, we choose
to ignore an edge that is not the central one of the 2–3 bipyramid.
x 1 x ′
1
x ′′ 
1
x 2
x ′
2
x ′′ 
2
x 1x ′
1
x ′′ 
1
x 2x ′
2
x ′′ 
2
w 1
w ′
1
w ′′ 
1
w 1
w ′
1
w ′′ 
1
w 2
w ′
2
w ′′ 
2
w 2
w ′
2
w ′′ 
2
w 3
w ′
3
w ′′ 
3
w 3
w ′
3
w ′′ 
3
Figure 7. The geometry of the 2–3 move: a bipyramid split into two tetra-
hedra for triangulation ⋃ N
i=1 ∆ i, and three for triangulation ⋃ N +1
i=1
~∆ i.
There are nine linear relations among the shapes of the tetrahedra involved in the move;
three come from adding dihedral angles on the equatorial edges of the bipyramid:
(3.20) W ′
1 =X1 +X2, W ′
2 =X ′
1 +X ′′
2 , W ′
3 =X ′′
1 +X ′
2,
and six from the longitudinal edges:
(3.21)
X1 =W2 +W ′′
3 , X ′
1 =W3 +W ′′
1 , X ′′
1 =W1 +W ′′
2 ,
X2 =W ′′
2 +W3, X ′
2 =W ′′
1 +W2, X ′′
2 =W ′′
3 +W1.
Moreover, due to the central edge of the bipyramid, there is an ex tra gluing constraint in ~T :
(3.22) W ′
1 +W ′
2 +W ′
3 = 2πi.
After exponentiating the relations (
3.20–3.22), and also using ziz′
iz′′
i =−1 and z′′
i +z−1
i −
1 = 0 for every tetrahedron ∆ i and ~∆ i, we ﬁnd a birational map between the shape param-
eters in the two triangulations. Explicitly,
{
w′
1 =x1x2, w′
2 = 1−x−1
2
1−x1
, w′
3 = 1−x−1
1
1−x2
}
or
{
x1 = 1−w′
2
−1
1−w′
3
, x2 = 1−w′
3
−1
1−w′
2
}
.
(3.23)
Note that the birational map is well deﬁned and one-to-one as long a s no shape parameters
(x1,x 2,w 1,w 2,w 3) equal 0, 1, or ∞. This condition is satisﬁed so long as triangulationsT
and ~T are both regular. (A necessary condition is that no univalent edges are created on
one side or the other of the 2–3 move; this is also suﬃcient when cons idering the discrete
faithful representation of M.)
We must also choose a ﬂattening in the two triangulations. Let us sup pose that for⋃ N +1
i=1
~∆ i we have a ﬂattening with (triples of) integer parameters ~f = (d1,d 2,d 3,f 3,...,f N ).
THE QUANTUM CONTENT OF THE GLUING EQUATIONS 21
This automatically determines a ﬂattening f = (e1,e 2,f 3,...,f N ) for the ⋃ N
i=1 ∆ i triangula-
tion, by simply setting
(3.24)
e1 =d2 +d′′
3, e ′
1 =d3 +d′′
1, e ′′
1 =d1 +d′′
2,
e2 =d′′
2 +d3, e ′
2 =d′′
1 +d2, e ′′
2 =d′′
3 +d1.
This is a discretized version of the six longitudinal relations (
3.21). One can check that
expected relations such as e1 +e′
1 +e′′
1 = 1 are satisﬁed by virtue of the discretized edge
constraintd′
1 +d′
2 +d′
3 = 2 ( cf. (
3.22)).
We have all the data needed to calculate τT . Let us start with determinants. In the
triangulation⋃ N
i=1 ∆ i, we write the matrices A and B schematically in columns as
(3.25) A = (a1, a2, ai), B = (b1, b2, bi),
with ai meaning (a3,a 4,...,a N ) and similarly for bi. This leads to a determinant
(3.26) det
(
A∆ z′′ + B∆ −1
z
)
= det
(
a1x′′
1 + b1
x1
, a2x′′
2 + b2
x2
, aiz′′
i + bi
zi
)
.
Alternatively, in the triangulation ⋃ N +1
i=1
~∆ i, the matrices ~A and ~B have one extra row and
one extra column. The extra gluing condition ( 3.22) causes the extra row in both ~A and ~B
to contain three −1’s. Altogether, the matrices take the form
(3.27) ~A =
(
−1 −1 −1 0
b1 +b2 a1 a2 ai
)
, ~B =
(
−1 −1 −1 0
0 a2 +b1 a1 +b2 bi
)
,
so that
~A∆ ˜z′′ +~B∆ −1
˜z =
(−w′′
1− 1
w1
−w′′
2− 1
w2
−w′′
3− 1
w3
0
(b1 +b2)w′′
1 a1w′′
2 + a2+b1
w2
a2w′′
3 + a1+b2
w3
aiz′′
i + bi
zi
)
=
( −1 −1 −1 0
(b1 +b2)w′′
1 a1w′′
2 + a2+b1
w2
a2w′′
3 + a1+b2
w3
aiz′′
i + bi
zi
)
.
It is then straightforward to check, using the map ( 3.23), that
(3.28)
(~A∆ ˜z′′ +~B∆ −1
˜z
)




1 −1 −1 0
0 1 0 0
0 0 1 0
0 0 0 1









1 0 0 0
0 1 w′
3x′′
2
x′′
1
0
0 w′
2x′′
1
x′′
2
1 0
0 0 0 1




 =
(
−1 0
∗ A∆ z′′ + B∆ −1
z
)
.
The determinant of the last matrix on the left hand side is 1 −w′
2w′
3 = 1 −w′
1
−1 = w1.
Therefore,
(3.29) det
(~A∆ ˜z′′ +~B∆ −1
˜z
)
=−w−1
1 det
(
A∆ z′′ + B∆ −1
z
)
.
We should also consider the monomial correction. However, with ﬂat tenings related as in
(
3.24), and with shapes related by the exponentiated version of ( 3.21), it is easy to check
that
(3.30) ~z
˜f ′′
~z′′− ˜f =w1(−1)d′′
2 −e′′
1zf ′′
z′′−f.
22 TUDOR DIMOFTE AND STA VROS GAROUF ALIDIS
We have thus arrived at the desired result; by combining (
3.29) and ( 3.30), we ﬁnd
(3.31) det
(~A∆ ˜z′′ +~B∆ −1
˜z
)
~z
˜f ′′
~z′′− ˜f =± det
(
A∆ z′′ + B∆ −1
z
)
zf ′′
z′′−f,
so that τT is invariant under the 2–3 move. This completes the proof of Theore m 1.4. □
