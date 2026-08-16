---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-053-341-quantizability-of-reﬁned-a-polynomials
section_title: "Quantizability of reﬁned A-polynomials"
section_number: 3.4.1
pages: 52-54
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
doc_brief: "Volume Conjecture: Refined and Categorified — The generalized volume conjecture relates asymptotic behavior of the colored Jones polynomials to objects naturally deﬁned on an algebra ic curve, the"
---
We can now analyze under what conditions the reﬁned A-polynomials which we found ear-
lier are quantizable. Since we already found the explicit fo rm of such reﬁned polynomials
Aref(x,y ;t), in order to test quantizability we can simply apply the condition (3.202). To this
end, we need to identify face polynomials associated to the N ewton polygons of various knots
discussed earlier. We will analyze separately of the unknot, the trefoil knot, and more general
(2, 2p + 1) torus knots. We will also discuss an interesting relatio n between Newton polygons
in the reﬁned and unreﬁned cases.
+
+
+
+
x
y
1
1 /g49
□ /g116/g51/g50 □ /g49
□ /g116/g51/g50 /g49
-
-
-
1
1-
 (  t) 3/2 
- (  t) -3/2 -
Figure 7: Newton polygon for the unknot (left). Red circles denote monomials of the reﬁned polyno-
mial, and smaller yellow crosses denote monomials of the unreﬁned poly nomial. In this example both
Newton polygons look the same, so that positions of all circles and cr osses overlap. More detailed
structure of the reﬁned A-polynomial is also shown in a matrix form on the right. Note, that the role
of rows and columns is exchanged in both pictures: the monomial ci,jxiyj is put in the place ( i,j )
in the Newton polygon, and it corresponds to the entry ci,j in the (i + 1)th row and in the (j + 1)th
column of the matrix on the right.
To start with we consider the unknot; as we will see, general f eatures of this example
will also be present for more general torus knot. The reﬁned A-polynomial of the unknot has
been found in (3.105), and in the limit t = −1 it reduces as follows:
Aref = (1 + t3x)(−t−3)1/2 − (1 −x)y − − − − − →
t→−1
(1 −x)(1 −y). (3.203)
We present Newton polygons for these two polynomials in Figu re 7 (left). Bigger red circles
denote monomials of the reﬁned polynomial, while smaller ye llow crosses denote monomials
of the unreﬁned polynomial. In the unknot case, both Newton p olygons coincide. From
the matrix presentation of the reﬁned A-polynomial given in Figure 7 we can immediately
write down face polynomials for all faces of the Newton polyg on. These face polynomials
are summarized in table 4; they are all linear in z and their roots are t3, 1, ( −t)−3/2, and
−(−t)3/2. If we insist that the criterion (3.202) should be satisﬁed, we conclude that the
deformation parameter t should be a root of unity.
Next, let us consider the class of (2 , 2p + 1) torus knots, for which the reﬁned A-
polynomials were found in section 3.3.3. When t = −1 these polynomials reduce, for general
– 51 –
face face polynomial
ﬁrst column (−t)−3/2z + (−t)3/2
last column z − 1
ﬁrst row (−t)−3/2 −z
last row (−t)3/2 +z
T able 4: Face polynomials for the unknot.
p, to the following form 13
Aref
T 2,2p+1(x,y ;t = −1) = ( x − 1)p(y − 1)(y +x2p+1)p. (3.204)
Interestingly, this form is closely related to the standard A-polynomials of (2, 2p + 1) torus
knots (y − 1)(y +x2p+1), up to an extra factor (x − 1)p and the power of p in the last factor.
While it is desirable to understand the meaning of the form (3 .204) better, here we note that
its Newton polygon is related in an interesting way to the New ton polygon of the reﬁned
A-polynomial. Namely, Newton polygons of reﬁned A-polynomials for (2, 2p + 1) knots have
hexagonal shape, as shown in Figure 8 (left) for the trefoil, and in appendix C for other torus
knots. (In all of these ﬁgures we use the same conventions as i n Figure 7.) Then, the Newton
polygons for the unreﬁned A-polynomials (3.204) have the same overall shape, with only one
small diﬀerence: in their center a “rhomboidal” collection o f points of size p ×p is absent, as
clearly seen in the ﬁgures in appendix C.
Apart from Newton polygons, in Figure 8 (right) and in append ix C we also present the
matrix form of reﬁnedA-polynomials. From this presentation it is not hard to read oﬀ the face
polynomials, and conjecture their form for general p, along each six faces of the hexagonal
shape. These face polynomials are listed in table 5. Interes tingly, all these polynomials
factor into linear factors in z, and the constraint (3.202) again leads to the aforemention ed
conclusion: the deformation parameter t must be a root of unity.
Finally, let us consider the A-polynomials for the trefoil knot in grading conventions of
[27], cf. (3.54). Newton polygons for both reﬁned and unreﬁned A-polynomials are shown
in Figure C7. They are also of a hexagonal shape, though much b igger than the Newton
polygon for the trefoil grading conventions of [44] shown in Figure 8. The matrix form of
the reﬁned A-polynomials in grading conventions of [27] is presented in Figure C14, and
the corresponding face polynomials are listed in table 6. Ag ain, it is easy to see that the
quantizability condition (3.202) is satisﬁed only if t is a root of unity. Therefore, we conclude
that, even though the explicit form of the reﬁned A-polynomial Aref(x,y ;t) may be sensitive
to the choice of grading, the quantizability is independent of this choice.
13Here and in what follows, we multiply Aref
T 2,2p+1 by a factor (1 + xt3)p to turn them into a nicer polynomial
form.
– 52 –
x
y
+
3 1 2
1
2
4
x
y
+ +
+ + +
+
+
+
/g48 /g49 /g49
/g48 /g116/g50 /g116/g51
/g48 /g50 /g116/g50/g49/g116/g48
/g116/g52 /g116/g53 /g48
/g116/g52 /g116/g54 /g48
0
0
0
t
t 0
0
0
1
4
4
-
-
2 t  (1+  t) 2
t 3-
1
t 2-
t 5
t 6
Figure 8: Newton polygons for the trefoil (left). Bigger red circles denote m onomials of the reﬁned
polynomial, and smaller yellow crosses denote monomials of the unreﬁn ed polynomial. More detailed
structure of the reﬁned A-polynomial is also shown in matrix representation (right). All conve ntions
are the same as in ﬁgure 7.
face face polynomial
ﬁrst column −t2p(p+1)(z − 1)p
last column (−1)p(z +t3)p
ﬁrst row z − 1
last row −t2p(p+1)(z −t2p)
lower diagonal (−1)pt3p(z −t2p+1)p
upper diagonal (−1)p+1(z +t2p+2)p
T able 5: Face polynomials for (2, 2p + 1) torus knots.
