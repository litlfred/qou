---
doc_id: m4-24
doc_title: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface"
section_id: sec-031-39-the-loop-expansion-of-the-kontsevich-invarian
section_title: "The loop expansion of the Kontsevich invariant"
section_number: 3.9
pages: 65-69
source_pdf: m4-24.pdf
source_sha256: cf7c5e29b818e647
doc_brief: "Problems on invariants of knots and 3-manifolds Edited by T. Ohtsuki Preface — 111 sections: Introduction; Polynomial invariants of knots; The Jones polynomial"
---
The loop expansion is the series of the rational presentations of the Kontsevich
invariant in loop-degrees. It was conjectured by Rozansky [357]. The existence
of such rational presentations has been proved by Kricker [231] (though such a
rational presentation itself is not necessarily a knot invariant in a general loop
degree). Further, Garoufalidis and Kricker [139] de
ned a knot invariant in any
loop degree, from which such a rational presentation can be deduced.
We have three isomorphic algebras
A(S1)=B=Bt; (21)
where the 
rst isomorphism is the formal Poincare-Birkho
-Witt isomorphism,
andB has the product structure related, by the isomorphism, to the product
structure ofA(S1) given by connected sum. Further, the second isomorphism
is the wheeling isomorphism [35] between B andBt ,w h e r eBt isB as a space
and has the product given by the disjoint union of uni-trivalent graphs.
We denote by Bconn the vector subspace of Bt spanned by connected uni-
trivalent graphs, and denote by B(loop l)
conn the vector subspace of Bconn spanned
by connected uni-trivalent graphs of loop-degree l,w h e r et h eloop-degree of a
uni-trivalent graph is de
ned to be half of the number given by the number of
trivalent vertices minus the number of univalent vertices. Then,
Bconn =
1M
l=0
B(loop l)
conn :
EachB(loop l)
conn can be presented by using the polynomial rings in H1(G)f o r
trivalent graphs G of loop-degree l subject to Aut( G) and the AS and IHX
Geometry &TopologyMonographs, Volume 4 (2002)
438 T. Ohtsuki (Editor)
relations. We will present B(loop l)
conn for l =0; 1; 2 in this way, to state the loop
expansion in these loop-degrees.
When l =0 ,w eh a v et h em a p
Q[x]−!B(loop 0)
conn ;x n7−! ; (22)
regarding x as a basis of H1(circle). Since the orientation-reversing automor-
phism of S1 takes xn to−xn by the AS relation, the above map deduces the
following isomorphism,
B(loop 0)
conn
=Q[x2]: (23)
For a knot K ,
(
logtZ(K)
(loop 0) = 1
2 log sinh(x=2)
x=2 −1
2 log K(ex); (24)
where logt is the logarithm in Bt regarding Z(K)a si n Bt , and the left
hand side is the summand of logtZ(K)2B conn inB(loop 0)
conn . This development
follows from the theory of [34]. See also [231, 139] (and references therein) for
a recent direct calculation.
When l =1 ,w eh a v et h em a p
Q[x1;x 2;x 3]−!B(loop 1)
conn ;x n1
1 xn2
2 xn3
3 7−! ;
regarding H1(-graph) as the vector space spanned by x1 , x2 , x3 subject to
the relation x1 +x2 +x3 = 0. Since Aut( -graph)= S2 S3 , the above map
deduces
B(loop 1)
conn
=Q[x1;x 2;x 3]=(S2 S3;x 1 +x2 +x3 =0 )
=

Q[x1;x 2;x 3]=(x1 +x2 +x3 =0 )
S2S3
=

Q[1; 2; 3]=(1 =0 )
(even)=Q[2; 2
3]; (25)
where i denotes the i-th elementary symmetric polynomial in x1 , x2 ,a n dx3 .
(To computeB(loop 1)
conn in a precise argument, we must also consider the space
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 439
of \dumbbell diagram" with legs. Since this space is injectively mapped to the
right hand side of the above formula, we omit its computation here.) For a
knot K there exists a polynomial P
K (t1;t 2;t 3), called the 2-loop polynomial ,
satisfying that
(
logtZ(K)
(loop 1) = P
K (ex1;ex2;ex3 )
K(ex1 )K (ex2 )K(ex3 ): (26)
The 2-loop polynomial P
K (t1;t 2;t 3)i n t1;t 2;t 3 satisfying t1t2t3 = 1 is uniquely
determined by each knot K . It is an invariant of K satisfying that
P
K (t1
i ;t1
j ;t1
k )= P
K(t1;t 2;t 3) for any signs and any fi;j;kg =f1; 2; 3g.
Problem 3.17 Find a topological construction of the 2-loop polynomial P
K .
Remark As in (24) the loop-degree 0 part of the Kontsevich invariant is pre-
sented by the Alexander polynomial, which can be constructed from the ho-
mology of the in
nite cyclic cover of the knot complement. It is shown, in
[142], that the \
rst derivative" of the 2-loop polynomial is given in terms of
linking functions associated to the in
nite cyclic cover of the knot complement.
It is expected [142] that the 2-loop polynomial would be described in terms of
invariants of the in
nite cyclic cover of the knot complement.
Remark A table of the 2-loop polynomial for knots with up to 7 crossings is
given by Rozansky [358]. See also a computer program [359], which calculates
the 2-loop polynomial of each knot. For example,
12P
31 (t1;t 2; 1
t1t2
)= −t2
1t2 +t2
1;
12P
41 (t1;t 2; 1
t1t2
)=0 ;
12P
51 (t1;t 2; 1
t1t2
)=2 t4
1t2
2−2t4
1t2 +2t4
1−t2
1t2 +t2
1:
The 2-loop polynomial for the torus knots is calculated independently by Marche
[270] and Ohtsuki [322].
The following problem is a step to Problem 3.17.
Problem 3.18 (A. Kricker) Let KT be the knot obtained from a tangle T
as shown in Figure 12. Find a presentation of the 2-loop polynomial P
KT of
KT by using the Kontsevich invariant Z(T ) of T .
Geometry &TopologyMonographs, Volume 4 (2002)
440 T. Ohtsuki (Editor)
TK T
Figure 12: The knot KT is obtained from the 2-parallel of a 2-strand tangle T by
adding the tangle depicted in solid lines in the right picture. The dotted lines imply
strands possibly knotted and linked in some fashion.
Remark (A. Kricker) P
KT might be presented by the degree  3p a r to f
Z(T ). Generalize the presentation K(t) = det(t1=2S−t−1=2ST )o ft h eA l e x a n -
der polynomial K(t)b yaS e i f e r tm a t r i xS of K .
When l =2 ,w eh a v et h em a p
xn1
1 xn2
2  xn6
6 7−! ;
which deduces the following isomorphism,
B(loop 2)
conn
=Q[x1;x 2; ;x 6]=(S4;x 1 +x2 +x3 =x1 +x6−x5 =0
x2 +x4−x6 =x3 +x5−x4 =0 ):
Corresponding to faces of a tetrahedra, we put y1 =x1−x2−x6 ,
y2 =x2−x3−x4 , y3 =x3−x1−x4 ,a n dy4 =x4 +x5 +x6 . Then,
B(loop 2)
conn
=Q[y1;y 2;y 3;y 4]=(S4;y 1 +y2 +y3 +y4 =0 )
=

Q[y1;y 2;y 3;y 4]=(y1 +y2 +y3 +y4 =0 )
S4
;
Geometry &TopologyMonographs, Volume 4 (2002)
Problems on invariants of knots and 3-manifolds 441
where the action of
