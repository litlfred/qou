---
doc_id: arxiv-1304.3481v1
doc_title: "Quadruply-graded colored homology of knots"
section_id: sec-002-4-examples
section_title: "Examples"
section_number: 4
pages: 35-68
source_pdf: 1304.3481v1.pdf
source_sha256: d0840f2775c0f761
doc_brief: "Quadruply-graded colored homology of knots — W e conjecture the existence of four independent gradings in the colored HOMFLY homology."
---
In this section we give some examples of the quadruply-graded color ed HOM-
FLY homology that exhibit all of the structure and satisfy all of the conjectures
from the previous sections. This gives a highly non-trivial check of t he existence
36 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
and consistency of such large and beautiful structure in the color ed HOMFLY ho-
mology.
4.1. T refoil. We start with the trefoil and its S2 and Λ 2 colored homologies.
The uncolored HOMFLY homology of the trefoil is ([ 21]):
(4.1) P (31)(a, q, t) = a2q−2 + a2q2t2 + a4t3.
The uncolored homology is the only one where two t-gradings coincide, i.e.
P (31)(a, q, tr, tc) =P (31)(a, q, t = trtc).
From (4.1) we can get the value of the S-invariant of the trefoil (that we denote Σ
in this paper):
(4.2) Σ(3 1) = 2 .
For easier visualization, triply-graded homologies are usually presen ted in a diagram
form. A generator of ( a, q, t)-degree ( i, j, k) is presented as a dot in the ( q, a)-plane
at the position ( j, i) and it is labeled by its t-degree k. The triply-graded homology
of the trefoil is presented in a diagram on the left of the Figure 12 be low.
0 2 −2
0 2 −2
3
2
a
a
q
q
2
4 2
0
−2
0
2
1 0 −1
−2
Figure 12. The uncolored homologies of the trefoil (left diagram)
and ﬁgure-eight knot (right diagram).
The (reduced) -colored HOMFLY polynomial of the trefoil knot is equal to:
P (31)(a, q) = a4q−4 + a4q2 + a4q4 + a4q8− a6− a6q2− a6q6− a6q8 + a8q6 .
The value of the four-variable -colored superpolynomial (the Poincar´ e polynomial
of the quadruply-graded H (31)) of the trefoil is given by
P (31)(a, q, tr, tc) = a4(q−4 + q2t2
rt4
c + q4t2
rt6
c + q8t4
rt8
c)+
(4.3) a6(t3
rt5
c + q2t3
rt7
c + q6t5
rt9
c + q8t5
rt11
c ) + a8q6t6
rt12
c .
The triply-graded S2-homology of the trefoil that is computed in [ 42] is obtained
from (4.1) by setting tc = 1, whereas the homology obtained in [ 2] or [20] is obtained
after setting tr = 1.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 37
For the second-symmetric representation the Q-grading is expressed as Q =
q + tr− tc. Then the tilde-version, i.e. the quadruply-graded -homology in
(a, Q, tr, tc)-gradings is given by:
~P (31)(a, Q, tr, tc) = a4(Q−4 + t2
rt4
c + t2
rt6
c + Q4t4
rt8
c)+
(4.4) a6(Q−2t3
rt5
c + Q−2t3
rt7
c + Q2t5
rt9
c + Q2t5
rt11
c ) + a8t6
rt12
c .
We note that all generators have the same δ-grading equal to +2. Moreover, the
last homology is self-symmetric: in terms of the Poincar´ e polynomial this amounts
to:
~P
(31)(a, Q−1t−1
r t−2
c , tr, tc) = ~P (31)(a, Q, tr, tc).
The quadruply-graded homologies we represent in the form of a diag ram in the
following way: for each generator we place a dot in the ( q, a)-plane. If ( q, a)-degree
of a generator x is ( i, j) then we put a dot at a point with coordinates ( i, j). The
two t-degrees are drawn as labels near the dot: the tr-grading is written above the
dot (and colored light green), while the tc-grading of a generator is written below
the corresponding dot. In such a way, the homology H (31) is presented in Figure
13.
0
a
q
−4 −2 2 4 6 8 −6
4
6
8
0
0
5 7
12
9 11
8 6 4
5
6
5
4 2
3 3
2
Figure 13. The S2-colored homology of the trefoil knot.
We can see all ﬁve non-trivial colored diﬀerentials on this diagram: Th ere are
two canceling ones dcol
1|0 and dcol
0|2, represented by blue and red arrows, respectively,
both leaving a single generator. Furthermore the two sl(n|m) colored diﬀerentials
dcol
1|1 (dash-and-dot arrows) and dcol
0|3 (dashed arrows), both leaving the homology
isomorphic to H
(31). And ﬁnally the universal one d← (magenta arrows), also
leaving the homology isomorphic to H (31). We note that the re-gradings are
exactly as predicted in Sections 3.5 and 3.7.
The diagram for the tilde-version of the homology H (31) is shown in Figure
14. The reﬁned exponential growth is indeed satisﬁed:
~P (31)(a, Q = q, tr = t, tc = 1) =
(
P (31)(a, q, t)
) 2
.
38 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
4
6
8
−6 −4 −2 0 2 4 6 0
0
0
5
3
7
3
4
2
6
2
12
6
9
5
11
5
8
4
a
Q
Figure 14. The tilde-version of the S2-colored homology of the
trefoil knot ( Q = q + tr− tc).
As for the second antisymmetric representation, we have that th e Λ 2-colored HOM-
FLY polynomial of the trefoil is given by
(4.5) P
(31)(a, q) = a4(q−8 + q−4 + q−2 + q4)− a6(q−8 + q−6 + q−2 + 1) + a8q−6
The Poincar´ e polynomial of the quadruply-graded homologyH (31) equals
P (31)(a, q, tr, tc) = a4(q−8 + q−4t6
rt2
c + q−2t4
rt2
c + q4t8
rt4
c)+
(4.6) a6(q−8t7
rt3
c + q−6t5
rt3
c + q−2t11
r t5
c + t9
rt5
c) + a8q−6t12
r t6
c.
The corresponding diagram, together with the colored diﬀerentials , is presented in
Figure 15. By comparing Figures 13 and 15 one can immediately see the mirror
5
9
5
11
2
4
2
6
6
12
4
8
0
0
3
7
3
5
a
q
−10 −8 −6 −4 −2 0 2 4
4
6
8
Figure 15. The Λ 2-colored homology of the trefoil knot.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 39
symmetry (3.11). This symmetry sends q↦→−q, and commutes with the action
of the colored diﬀerentials, as can be seen from the diagrams. We re mark that all
re-gradings from the isomorphisms induced by colored diﬀerentials a re exactly as
predicted in Sections 3.5 and 3.7.
Mirror symmetry is even better seen on the tilde-version of the hom ology. For
the second-antisymmetric representation , the Q-grading is obtained by Q = (q +
tr− tc)/2, and so we get:
~P (31)(a, Q, tr, tc) = a4(Q−4 + t6
rt2
c + t4
rt2
c + Q4t8
rt4
c)+
(4.7) a6(Q−2t7
rt3
c + Q−2t5
rt3
c + Q2t11
r t5
c + Q2t9
rt5
c) + a8t12
r t6
c .
Its diagram is given in Figure 16. Comparison of Figures 14 and 16 show s that the
4
6
8
−6 −4 −2 0 2 4 6 0
6
12
0
0
4
8
2
4
2
6
3
5
3
7
5
9
5
11
a
Q
Figure 16. The tilde-version of the Λ 2-colored homology of the
trefoil knot ( Q = q+tr−tc
2 ).
two are related by a simple exchange of tr and tc gradings, as predicted by mirror
symmetry (3.10). Also, one can easily check that the explicit form of the other
mirror symmetry (3.11) is satisﬁed, too.
Before passing to further examples, we note that with the explicit m irror sym-
metries, whenever we know the quadruply-graded λ-colored homology of a knot K,
then we automatically have λt-colored homology of K, as well:
~P λt
(K)(a, Q, tr, tc) = ~P λ(K)(a, Q, tc, tr).
Therefore, in the remaining examples we present the results only fo r one diagram
of each pair, λ and λt.
4.2. Figure-eight knot. We emphasize that our conjectures and predicted
structures are for all knots, and not just torus knots. In part icular, all homologies
computed in [ 42] (that includes S2-colored homologies of all prime knots with up
to 6 crossings) can be extended to quadruply-graded homologies w hich have all of
the wanted properties. Here we present the explicit expressions f or the S2-colored
40 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
homology of the ﬁgure-eight knot. The uncolored homology of the ﬁ gure-eight knot
is given by:
P (41)(a, q, t) = a2t2 + (q−2t−1 + 1 + q2t) + a−2t−2,
and its is S-invariant is Σ(4 1) = 0. The triply-graded homology of the ﬁgure-
eight knot is presented in a diagram on the right of the Figure 12. The -colored
HOMFLY polynomial of the ﬁgure-eight knot equals to:
P (41)(a, q) = a4q4 + a2(−q−2 + q2− q4− q6) + (q−6− q−4 + 3− q4 + q6)+
a−2(−q−6− q−4 + q−2− q2) + a−4q−4.
The quadruply-graded -colored HOMFLY homology of the ﬁgure-eight knot that
we computed is given by:
P
(41)(a, q, tr, tc) = a4q4t4
rt8
c + a2(q−2trtc + trt3
c + t2
rt2
c + q2t2
rt4
c + q4t3
rt5
c + q6t3
rt7
c )+
+(q−6t−2
r t−4
c +q−4t−1
r t−3
c +q−2t−1
r t−1
c +q−2t−2
c +3+ q2t2
c +q2trtc +q4trt3
c +q6t2
rt4
c )+
+a−2(q−6t−3
r t−7
c +q−4t−3
r t−5
c +q−2t−2
r t−4
c +t−2
r t−2
c +t−1
r t−3
c +q2t−1
r t−1
c )+a−4q−4t−4
r t−8
c .
It is presented in a diagram form in Figure 17. All generators have th e same δ-
0
0
0
0
0
0
2
0
1
1
3
1
4
2
1
1
3
1
2
2
4
2
5
3
7
3
8
4
−1
−1
−2
−2
0
2
4
a
−6 −4 −2 0 2 4 6
q−4
−2
0
−8
−4
−7
−3
−5
−3
−4
−2
−3
−1
−1
−1
−4
−2
−3
−1
−2
Figure 17. The S2-colored homology of the ﬁgure-eight knot.
degree 0, in accordance with the fact that 4 1 is a thin knot. The homology H (41)
has ﬁve colored diﬀerentials: two canceling ones dcol
1|0 and dcol
0|2, further two colored
sl(m|n) diﬀerentials dcol
1|1 and dcol
0|3 both leaving homology isomorphic to H
(41) and
the universal one d← also leaving homology isomorphic to H (41). All re-gradings
are as given in Sections 3.5 and 3.7.
The Q-grading is given by Q = q +tr−tc. So, the tilde-version of the -colored
HOMFLY homology of the ﬁgure-eight knot becomes:
~P (41)(a, Q, tr, tc) = a4t4
rt8
c +a2(Q−2trtc+Q−2trt3
c +t2
rt2
c +t2
rt4
c +Q2t3
rt5
c +Q2t3
rt7
c )+
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 41
(Q−4t−2
r t−4
c + Q−2t−1
r t−3
c + Q−2t−1
r t−1
c + t−2
c + 3 + t2
c + Q2trtc + Q2trt3
c + Q4t2
rt4
c )+
a−2(Q−2t−3
r t−7
c +Q−2t−3
r t−5
c +t−2
r t−4
c +t−2
r t−2
c +Q2t−1
r t−3
c +Q2t−1
r t−1
c )+ a−4t−4
r t−8
c .
The tilde-version is presented in Figure 18 in ( a, Q, tr, tc)-gradings. It indeed sat-
4
2
3
1
1
1
5
3
7
3
0
0
0
0
0
0 0
−2 2
0
1
1
3
1
8
4
2
2
4
2
−7
−3
−5
−3
−3
−1
−1
−1
−4
−2
−2
−2
−8
−4
−4
−2
−3
−1
−1
−1
0
2
4
a
−6 −4 −2
−4
−2
2 4
Q
0
Figure 18. The tilde-version of S2-colored homology of the ﬁgure-
eight knot.
isﬁes self-symmetry (3.8) and reﬁned exponential growth (3.36).
4.3. (3,4)-torus knot. In this section we describe the quadruply-graded S2
colored homology of the (3,4)-torus knot T3,4 (i.e. 8 19 knot) and show that it
satisﬁes all of the desired properties. This knot is a thick knot, and has nontrivial
diﬀerential d1|1 (i.e. d0) on the uncolored homology, which makes this a highly-
nontrivial consistency check of all predicted properties. The unc olored homology
of T3,4 is given by [ 21]:
P (T3,4)(a, q, t) = a6q−6 + a8q−4t3 + a6q−2t2 + a8t5 + a6q2t4 + a8q4t7 + a6q6t6+
+a10t8 + a8q−2t5 + a8q2t7 + a6t4.
Its S-invariant is Σ( T3,4) = 6. There is a non-trivial diﬀerential d0 (or d1|1) on
H (T3,4) of ( a, q, t)-degree (−2, 0,−3) leaving 5-dimensional homology isomorphic
to the knot Floer homology of T3,4:
(4.8) ( H (T3,4), d1|1) = a6q−6 + a8q−4t3 + a6t4 + a8q4t7 + a6q6t6.
42 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
The quadruply-graded -colored homology of T3,4 that we have computed has 121
generators. Its Poincar´ e polynomial is given by:
~P (T3,4)(a, Q, tr, tc) = a12(Q−12 + Q−8t2
r(t4
c + t6
c) + Q−6t4
r(t8
c + t10
c )+
Q−4t4
r(t8
c +t10
c +t12
c )+Q−2t6
r(t12
c +t14
c )+t6
r(t12
c +t14
c +t16
c +t18
c )+t8
rt16
c +Q2t8
r(t16
c +t18
c )+
Q4t8
r(t16
c + t18
c + t20
c ) + Q6t10
r (t20
c + t22
c ) + Q8t10
r (t20
c + t22
c ) + Q12t12
r t24
c )+
a14(Q−10t3
r(t5
c + t7
c) + Q−8t5
r(t9
c + t11
c ) + Q−6t5
r(t9
c + 2t11
c + t13
c )+
Q−4t7
r(2t13
c + 3t15
c + t17
c ) + Q−2t7
r(t13
c + 2t15
c + 2t17
c + t19
c )+
Q−2t9
r(t17
c +t19
c )+t9
r(2t17
c +3t19
c +t21
c )+Q2t9
r(t17
c +2t19
c +2t21
c +t23
c )+Q2t11
r (t21
c +t23
c )+
Q4t11
r (2t21
c +3t23
c +t25
c )+Q6t11
r (t21
c +2t23
c +t25
c )+Q8t13
r (t25
c +t27
c )+Q10t13
r (t25
c +t27
c ))+
+ a16(Q−8t6
rt12
c + Q−6t8
r(t14
c + 2t16
c + t18
c ) + Q−4t8
r(t16
c + t18
c ) + Q−4t10
r t20
c +
Q−2t10
r (t18
c + 3t20
c + 2t22
c ) + t10
r (t20
c + t22
c + t24
c ) + t12
r (t22
c + 2t24
c + t26
c )+
Q2t12
r (t22
c +3t24
c +2t26
c )+Q4t12
r (t24
c +t26
c )+Q4t14
r t28
c +q6t14
r (t26
c +2t28
c +t30
c )+q8t14
r t28
c )+
+ a18(Q−4t11
r (t21
c + t23
c )+ Q−2t13
r (t25
c + t27
c ) + t13
r (t25
c + t27
c ) + Q2t15
r (t29
c + t31
c )+
+ Q4t15
r (t29
c + t31
c )) + a20t16
r t32
c .
The Poincar´ e polynomial in (a, q, tr, tc)-gradings can be obtained from the above
expression by:
P
(T3,4)(a, q, tr, tc) = ~P (T3,4)(a, Q = q, tr = trq−1, tc = tcq).
This homology satisﬁes all of the expected properties: there are f our colored sl(m|n)
diﬀerentials dcol
1|0, dcol
0|2, dcol
1|1 and dcol
0|3, with the properties and re-gradings exactly
matching the predicted behaviour from Section 3.5. Moreover, the re exists a univer-
sal colored diﬀerential d← as predicted in Section 3.7. Furthermore, the homology
~H
(T3,4) satisﬁes the self-symmetry property:
~P (T3,4)(a, Q−1t−1
r t−2
c , tr, tc) = ~P (T3,4)(a, Q, tr, tc).
It also satisﬁes the reﬁned exponential growth property:
~P (T3,4)(a, Q = q, tr = t, tc = 1) =
(
P (T3,4)(a, q, t)
) 2
.
Moreover, since HFK diﬀerential d0 onH (T3,4) is nontrivial, this time the HFK-
like exponential growth property (3.44) is giving a new relation on the homolo-
gies. Indeed, there exists a diﬀerential d1|2 on ~H (T3,4) of ( a, Q, tr, tc)-degree
(−2, 0,−3,−5), so that the homology H∗(~H (T3,4), d1|2) is 25-dimensional with
the following Poincar´ e polynomial:
(~H (T3,4), d1|2)(a, Q, tr, tc) = a12(Q−12 + Q−6t4
r(t8
c + t10
c ) +t6
r(t16
c + t18
c ) +t8
rt16
c +
Q6t10
r (t20
c + t22
c ) + Q12t12
r t24
c ) + a14(Q−10t3
r(t5
c + t7
c) + Q−4t7
r(t13
c + t15
c )+
Q−2t7
r(t17
c + t19
c ) + Q2t9
r(t21
c + t23
c ) + Q4t11
r (t21
c + t23
c ) + Q10t13
r (t25
c + t27
c ))+
+ a16(Q−8t6
rt12
c + t10
r (t22
c + t24
c ) + Q8t14
r t28
c ).
Therefore
(4.9) ( ~H
(T3,4), d1|2)(a, Q = q, tr = t, tc = 1) =
(
H (T3,4), d1|1)(a, q, t)
) 2
.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 43
4.4. (2, 2) representation. In this section we describe the -colored HOM-
FLY homology of the trefoil knot. It should categorify the reduce d -colored
HOMFLY polynomial of the trefoil:
P (31)(a, q) = a16 + a14(−q−6− 2q−4− q−2− q2− 2q4− q6)
+ a12(4 + 2q−10 + 2q−8 + 2q−6 + q−4 + 3q−2 + 3q2 + q4 + 2q6 + 2q8 + 2q10)
+ a10(−2− q−14− 2q−12− q−10− q−8− 3q−6
− 4q−4− 3q−2− 3q2− 4q4− 3q6− q8− q10− 2q12− q14)
+ a8(2 + q−16 + q−10 + 2q−8 + q−6 + q−4 + q−2 + q2 + q4 + q6 + 2q8 + q10 + q16)
The -colored HOMFLY homology of the trefoil knot that we computed, h as 81
generators. Its four-variable Poincar´ e polynomial is given by:
P (31)(a, q, tr, tc) = a16t24
r t24
c + a14(q−6t19
r t17
c + q−4(t17
r t17
c + t19
r t19
c )+
q−2t17
r t19
c + q2t23
r t21
c + q4(t21
r t21
c + t23
r t23
c ) + q6t21
r t23
c )+
+ a12(q−10(t12
r t10
c + t14
r t12
c ) + 2q−8t12
r t12
c + q−6(t10
r t12
c + t12
r t14
c ) + q−4t18
r t14
c +
+ q−2(t16
r t14
c + 2t14
r t16
c ) + (3t16
r t16
c + t18
r t18
c ) + q2(t14
r t16
c + 2t16
r t18
c )+
+ q4t14
r t18
c + q6(t20
r t18
c + t22
r t20
c ) + 2q8t20
r t20
c + q10(t18
r t20
c + t20
r t22
c ))+
+ a10(q−14t7
rt5
c + q−12(t5
rt5
c + t7
rt7
c) + q−10t5
rt7
c + q−8t13
r t9
c + q−6(2t11
r t9
c + t13
r t11
c )+
+ q−4(t9
rt9
c + 3t11
r t11
c ) + q−2(2t9
rt11
c + t11
r t13
c ) + (t9
rt13
c + t17
r t13
r )+
+ q2(2t15
r t13
c + t17
r t15
c ) + q4(t13
r t13
c + 3t15
r t15
c ) + q6(2t13
r t15
c + t15
r t17
c )+
+ q8t13
r t17
c + q10t19
r t17
c + q12(t17
r t17
c + t19
r t19
c ) + q14t17
r t19
c )+
+ a8(q−16 + q−10t6
rt4
c + q−8(t4
rt4
c + t6
rt6
c) + q−6t4
rt6
c + q−4t12
r t8
c + q−2t10
r t8
c+
(t8
rt8
c+t10
r t10
c )+q2t8
rt10
c +q4t8
rt12
c +q6t14
r t12
c +q8(t12
r t12
c +t14
r t14
c )+q10t12
r t14
c +q16t16
r t16
c ).
Let us list various diﬀerentials and their ( a, q, tr, tc)-degrees. Everywhere in this
section λ =
.
1. Categoriﬁcation:
P λ(31)(a, q, tr =−1, tc = 1) = P λ(31)(a, q) =P λ(31)(a, q, tr = 1, tc =−1).
2. Canceling diﬀerentials: There exist diﬀerentials dcol
2|0 and dcol
0|2, with degrees
(−2, 4,−1,−1) and (−2,−4,−5,−5), respectively. Remaining generators have de-
grees (8 ,−16, 0, 0) and (8 , 16, 16, 16), respectively.
3. Row-removing diﬀerentials: There exist diﬀerentials dcol
3|0 and dcol
1|2 of degrees
(−2, 6,−3,−1) and (−2,−2,−7,−5), respectively, such that
H∗
(
Hλ(31), dcol
3|0
)
∼
= H
(31),
H∗
(
Hλ(31), dcol
1|2
)
∼
= H
(31).
4. Column-removing diﬀerentials: There exist diﬀerentials dcol
0|3 and dcol
2|1 of degrees
(−2,−6,−5,−7) and (−2, 2,−1,−3), respectively, such that
H∗
(
Hλ(31), dcol
0|3
)
∼
= H
(31),
H∗
(
Hλ(31), dcol
2|1
)
∼
= H
(31).
44 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
5. Universal colored diﬀerentials: There exist diﬀerentials d↑ and d← of degrees
(0, 2,−2, 0) and (0 , 2, 0, 2), respectively, such that
H∗(
Hλ(31), d↑) ∼
= H
(31),
H∗(
Hλ(31), d←) ∼
= H
(31).
The remaining properties are best seen in the ( a, Q, tr, tc)-gradings. Recall that in
this case the Q-grading can be expressed via the other ones by the equation
Q = (q + tr− tc)/2.
We denote the λ-colored homology in these four gradings by ~Hλ(31) and the cor-
responding four-variable Poincar´ e polynomial by ~P λ(31)(a, Q, tr, tc). In terms of
P λ(31), we have
~P λ(31)(a, Q, tr, tc) =P λ(31)(a, Q1/2, trQ1/2, tcQ−1/2).
6. Self-symmetry:
~Hλ
i,j,k,l(31)∼
= ~Hλ
i,−j,k−2j,l−2j (31).
7. Mirror symmetry: Since
t = , the mirror symmetry in this case is an
another, diﬀerent symmetry on ~Hλ(31):
~Hλ
i,j,k,l(31)∼
= ~Hλ
i,j,l,k(31).
8. Reﬁned exponential growth:
~P λ(31)(a, Q, tr, tc = 1) =
(
~P
(31)(a, Q, tr, tc = 1)
) 2
.
4.5. (2, 2, 2) representation. In this section we give the result for the -
colored homology of the trefoil. Although this homology is very large ( 729-dimensional)
it contains all colored diﬀerentials predicted in Section 3.5. Due to its s ize, and in
order to simplify the presentation, we give the homology and the diﬀe rentials in
(a, q, tc)-gradings, and simply denote tc by t. In ( a, q, tc)-gradings the Poincar´ e
polynomialP λ(31) is given by:
P (31)=a12(q−36+q−30t4+q−28(t4+t6)+q−26(t4+t6)+q−24(t6+t8)+q−22t8
+q−20(2t8+t10)+q−18(t8+2t10)+q−16(t8+2t10+t12)+q−14(t10+2t12)
+q−12(3t12+t14)+q−10(2t12+2t14)+q−8(t12+3t14)+q−6(t12+2t14+t16)+q−4(t14+2t16)
+2q−2t16+q0(2t16+2t18)+q2(t16+2t18)+
q4(t16+2t18+t20)+q6(t18+t20)++q8t20+q10t20+q12(t20+t22)+q14(t20+t22)+q16t22+q24t24)
+a14(q−36t5+q−34(t5+t7)+q−32(t5+t7)+q−30(t7+t9)+q−28(2t9+t11)+q−26(3t9+3t11)
+q−24(2t9+5t11+t13)+q−22(t9+4t11+3t13)+q−20(2t11+5t13+t15)+q−18(5t13+4t15)
+q−16(4t13+7t15+t17)+q−14(2t13+8t15+3t17)+q−12(t13+5t15+6t17)+q−10(2t15+7t17+2t19)
+q−8(6t17+5t19)+q−6(4t17+8t19+t21)+q−4(2t17+8t19+3t21)+q−2(t17+5t19+5t21)
+q0(2t19+5t21+t23)+q2(4t21+2t23)+q4(3t21+4t23)+q6(2t21+5t23+t25)
+q8(t21+4t23+2t25)+q10(2t23+2t25)+q12t25+q14t25+q16(t25+t27)+q18(t25+t27)+q20t27)+
+a16(q−34(t10+t12)+q−32(t10+2t12)+q−30(t10+3t12+t14)+q−28(2t12+2t14)
+q−26(t12+3t14+2t16)+q−24(3t14+5t16+t18)+q−22(2t14+8t16+3t18)
q−20(t14+7t16+6t18)+q−18(4t16+8t18+2t20)
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 45
+q−16(t16+7t18+5t20)+q−14(5t18+10t20+2t22)+q−12(2t18+11t20+5t22)+
q−10(t18+9t20+9t22+t24)+q−8(4t20+9t22+2t24)+q−6(t20+7t22+5t24)
q−4(4t22+7t24+t26)+q−2(2t22+9t24+3t26)+
+q0(t22+7t24+6t26)+q2(4t24+6t26+t28)+q4(t24+4t26+t28)+q6(2t26+2t28)+
+q8(t26+2t28)+q10(t26+3t28+t30)+q12(2t28+t30)+q14(t28+t30)+
+a18(q−32t17+q−30(t15+2t17+t19)+q−28(3t17+2t19)+q−26(2t17+3t19)+q−24(t17+3t19+2t21)+
+q−22(2t19+4t21+t23)+q−20(t19+6t21+4t23)+q−18(6t21+7t23+t25)+q−16(3t21+8t23+2t25)+
+q−14(t21+6t23+4t25)+q−12(3t23+6t25+t27)+q−10(t23+7t25+4t27)+q−8(6t25+7t27+t29)+
+q−6(3t25+8t27+2t29)+q−4(t25+5t27+3t29)+q−2(2t27+3t29)+q0(t27+3t29+t31)+
+q2(3t29+2t31)+q4(2t29+3t31)+q6(t29+2t31+t33)+q8t31)+
+a20(q−28(t22+t24)+q−26(t22+2t24)+q−24(t22+3t24+t26)+q−22(2t24+t26)+q−20(t24+2t26)
+q−18(2t26+2t28)+q−16(2t26+4t28+t30)+q−14(t26+5t28+2t30)+q−12(3t28+3t30)+
+q−10(t28+2t30)+q−8(2t30+t32)+q−6(t30+2t32)+q−4(t30+3t32+t34)+q−2(2t32+t34)+
q0(t32+t34))+a22(q−24t29+q−22(t29+t31)+q−20(t29+t31)+q−18t31+q−14t33+q−12(t33+t35)+
q−10(t33+t35)+q−8t35)+ +a24q−18t36.
On such a big homology Hλ(31) categorifying the reduced λ-colored HOMFLY
polynomial of the trefoil knot, there exist all of the predicted colo red diﬀerentials:
1. Canceling diﬀerential dcol
3|0 of ( a, q, tc)-degree (−2, 6,−1) such that the homol-
ogy H∗(Hλ(31), dcol
3|0) is one-dimensional, and the remaining generator has ( a, q, tc)-
degree (12 ,−36, 0).
2. Canceling diﬀerential dcol
0|2 of degree ( −2,−4,−5), such that the homology
H∗(Hλ(31), dcol
0|2) is one-dimensional, and the remaining generator has ( a, q, tc)-
degree (12 , 24, 24).
3. Positive row-removing diﬀerential dcol
4|0 of degree (−2, 8,−1), such that
H∗(Hλ(31), dcol
4|0)∼
=H
(31).
4. Negative row-removing diﬀerential dcol
1|2 of degree (−2,−2,−5), such that
H∗(Hλ(31), dcol
1|2)∼
=H
(31).
5. Positive row-removing diﬀerential dcol
5|0 of degree (−2, 10,−1), such that
H∗(Hλ(31), dcol
5|0)∼
=H
(31).
6. Negative row-removing diﬀerential dcol
2|2 of degree (−2, 0,−5), such that
H∗(Hλ(31), dcol
2|2)∼
=H
(31).
7. Negative column-removing diﬀerential dcol
0|3 of degree (−2,−6,−7), such that
H∗(Hλ(31), dcol
0|3)∼
=H
(31).
8. Positive column-removing diﬀerential dcol
3|1 of degree (−2,−4,−3), such that
H∗(Hλ(31), dcol
3|1)∼
=H
(31).
46 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
9. Universal colored diﬀerential d← of degree (0 , 2, 2), such that
H∗(Hλ(31), d←)∼
=H
(31).
4.6. (2, 1) “hook” representation. The -colored HOMFLY polynomial of
the trefoil is given by
P (31)(a, q) = − a12 + a10(q−6 + q−4 + q−2 + q2 + q4 + q6)
+ a8(−q−10− 2q−6− 3q−2− 3q2− 2q6− q10)
+ a6(q−10 + 2q−6− q−4 + 2q−2 + 2q2− q4 + 2q6 + q10).
This polynomial has 31 terms, and therefore any homology theory c ategorifying
it, should have at least 31 generators. This already indicates distinc tion between
rectangular and hook diagrams: this time, already for the trefoil, t he exponential
growth property cannot be satisﬁed (the uncolored homology of t he trefoil is 3-
dimensional and 31 > 33). However, some of the structural properties still exist in
the colored HOMFLY homology theories for the hook-shaped Young diagrams.
As a sl(n|m) representation, λ = has three nice isomorphisms for particular
values of n and m. Namely we have that ∼
=
as sl(2|0), as sl(1|1) and as sl(0|2)
representations. Therefore, we expect three colored diﬀerent ials, dcol
2|0, dcol
1|1 and dcol
0|2
onH
(K), such that
H∗(H (K), dcol
2|0) ∼
= H
(K),(4.10)
H∗(H (K), dcol
1|1) ∼
= H
(K),(4.11)
H∗(H (K), dcol
0|2) ∼
= H
(K).(4.12)
The ( a, q, t)-degrees of these three diﬀerentials are:
(4.13)
deg dcol
2|0 = (−2, 4,−1), deg dcol
1|1 = (−2, 0,−3), deg dcol
0|2 = (−2,−4,−5).
The requirement that H
(31) should categorify P (31)(a, q), together with the
existence of the colored diﬀerentials dcol
2|0, dcol
1|1 and dcol
0|2 essentially determine the
-colored homology of the trefoil knot. It has 41 generators and it s Poincar´ e
polynomial is given by:
(4.14) P
(31)(a, q, t) = a12t13 + a10(q−6t8 + q−4t8 + q−2t10 + t10 + t11
+ q2t12 + q4t12 + q6t14)+ a8(q−10t3 + 2q−6t5 + q−4t5 + q−4t6 + 3q−2t7 + t7 + t8 + 3q2t9
+ q4t9 + q4t10 + 2q6t11 + q10t13) + a6(q−10 + 2q−6t2 + q−4t3 + 2q−2t4 + t4 + t5
+ 2q2t6 + q4t7 + 2q6t8 + q10t10).
Additional nice properties that this homology satisﬁes, and which als o exist in the
rectangular case, is the mirror symmetry. Since t = this becomes a symmetry
onH (31):
(4.15) M :Hi,j,k(31)→H i,−j,k−j (31),
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 47
with the property that
(4.16) M
dn|m = dm|nM .
There are some properties that we predict in the case of rectangu lar representa-
tions and which do not exist for the hook diagram. First of all, already for the trefoil
the exponential growth property is not satisﬁed. The homology is 4 1-dimensional,
and the -colored HOMFLY polynomial already has 31 terms.
Second, this time the isomorphisms (4.10)-(4.12) are valid only after appropri-
ate collapse of tri-grading, i.e. after setting a = qn−m in the case of the diﬀerential
dn|m. Additionally, there is no explicit re-grading in these isomorphisms, an d we
could not ﬁnd the second t-grading. Therefore the theory that we propose is triply-
graded.
Finally, we note that there exists the SL(2) Lefschetz-like action on homology
(4.14) with raising operator of degree (0 , 4, 2). According to the “dictionary” (2.4),
this raising operator corresponds to forming a bound state with a B PS state of
D0-brane charge n = 4.
5. Colored HOMFL Y homology for torus knots
In this part we describe various algebraic and geometric approache s to the
colored homology of torus knots.
5.1. Stable HOMFL Y homology of torus knots. We will be interested
in the stable limit of the colored HOMFLY polynomials of ( n, m) torus knots at
m→∞ . Using e.g. [ 79, eq. (5.4)], one can prove the following result.
Proposition 5.1. Let κ(µ) =∑
(i,j)∈µ(i− j). Deﬁne
P λ
st(T (m, n)) := q−mnκ(λ)+ m
n κ(nλ)a− m(n−1)|λ |
2 P λ(T (m, n)).
Then
(5.1) lim
m→∞
P λ
st(T (m, n)) = P nλ(a, q).
As a corollary, one can compute the stable colored invariants of tor us knots
using the hook formula (2.12). One can easily check that the unredu ced stable
polynomial P λ(T (n,∞)) = P nλ(
; a, q) is a series in (−a) and q with nonnegative
coeﬃcients.
Let us compute the stable polynomial of the (2 ,∞) torus knot colored by the
Young diagram λ = (2, 1). By (5.1) it is the same as the polynomial of the unknot
colored by the Young diagram 2 λ = (4 , 2). The hook formula (2.12) gives the
following answer (up to an overall scaling):
P 2λ( ) = (1− aq−1)(1− a)2(1− aq)(1− aq2)(1− aq3)
(1− q)2(1− q2)2(1− q4)(1− q5) .
Note that
P λ( ) = (1− aq−1)(1− a)(1− aq)
(1− q)2(1− q3) .
The reduced polynomial P red
λ (T (2,∞)) = P λ (T (2,∞))
P λ (a,q) has positive and negative
terms in the q-expansion of the coeﬃcient at a0:
(1− q3)
(1− q2)2(1− q4)(1− q5) = 1+2 q2−q3 +4q4−q5 +6q6−2q7 +8q8−2q9 +11q10 +. . .
48 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
•i
j
(n− 1)S
Figure 19. Generators u(n)
ij
•i
j
(n− 1)S
Figure 20. Generators ξ(n)
ij
We would like to use the equation (5.1) as a deﬁnition of the stable color ed
homology of ( n,∞) torus knot. More precisely, we conjecture that as a vector
spaceHλ(n,∞) is isomorphic to Hnλ( ), moreover, the a, q, tc gradings on these
spaces match. This suggests that Hλ(n,∞) is a free supercommutative algebra
with bosonic and fermionic generators labelled by the boxes of nλ.
Let λ be an R× S rectangular Young diagram, and let K = T (p, q) be a ( p, q)-
torus knot. We assume that Hλ(K) is a quotient of Hλ(T (p,∞)), the latter space
being ( a, q, tc)-graded isomorphic to the pλ-colored homology of the unknot. Under
this assumption, the multiplicative generators of Hλ(K) coincide with the ones of
Hλ(T (p,∞)), while some additional relations are imposed. Let us determine the
gradings of these generators. The diagram pλ is a R× pS rectangle, which can be
naturally divided into p diﬀerent R× S rectangles. Let us denote by u(n)
ij a bosonic
generator in n-th rectangle from the right at box ( i, j), and by ξ(n)
ij a fermionic
generator in n-th rectangle from the left at box ( i, j), as in Figures 19 and 20 .
Their gradings are given by the following equations:
(a, q)
[
u(n)
ij
]
= (0, 2(nS− i + R− j + 1)),
(tc, tr)
[
u(n)
ij
]
= 2(nS− i), 2((n− 1)R + j− 1)),
(a, q)
[
ξ(n)
ij
]
= (2, 2((n− 1)S + i− j)),
(tc, tr)
[
ξ(n)
ij
]
= (2((n− 1)S + i)− 1, 2((n− 1)R + j)− 1).
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 49
Note that tr is constant in rows and tc is constant in columns. This explains the
notations tr and tc. Using the equation Q = q+tr−tc
R , we get
Q
[
u(n)
ij
]
= 2n, Q
[
ξ(n)
ij
]
= 2n− 2.
It is important to note that these elements generate unreducedstable homology.
To work with the reduced homology, one should consider u(n)
ij , ξ(n)
ij for n≥ 2 since
the subalgebra generated by u(1)
ij , ξ(1)
ij coincides with the unreduced homology of
the unknot.
There exists a map Mλ :Hλ(T (p,∞))→H λt
(T (p,∞)) such that for any w we
have
(5.2) ( Q, tc, tr)[Mλ(w)] = ( Q, tr, tc)[w].
The map Mλ is deﬁned by the equations
Mλ
(
u(n)
ij
)
:= u(n)
R−j+1,S−i+1, M λ
(
ξ(n)
ij
)
:= ξ(n)
ji .
One can check that it satisﬁes (5.2). The reﬁned exponential grow th conjecture
also holds for the stable homology Hλ(T (p,∞)) :
(5.3) P R×S(T (p,∞), a, Q, tr) =
(
P Λ R
(T (p,∞), a, Q, tr)
) S
.
The exponential growth conjecture follows from the fact that tr is constant in
rows: if we consider generators in ( a, Q, tr) gradings, then we get S copies of
HΛ R
(T (p,∞)) in the same gradings, which in turn implies (5.3).
Let us recall that in (3.9) we conjectured that the self-duality map Φ can be
obtained as follows: there exists a “D0-brane” operator Lλ :Hλ(K)→H λ(K) such
that
(5.4) ( a, q, Q, tr, tc)[Lλ] = (0 , R + S, 2, R, S), Φ λ(x) = L−Q(x)
λ .
We conjecture that for torus knots colored by λ = R× S rectangular diagrams such
operator Lλ coincides with the multiplication operator by u(2)
S,1. One can check that
it has the prescribed degrees. Moreover, the mirror map Mλ is chosen in such a way
that Mλ(u(2)
S,1) = u(2)
R,1, and so for the rectangular diagrams we have an equation
Mλ◦ Lλ = Lλt◦ Mλ,
and therefore
Mλ◦ Φ λ = Φ λt◦ Mλ.
This is indeed the required compatibility relation between M and Φ.
Now let us describe the action of colored diﬀerentials in this algebraic m odel.
The positive row-removing diﬀerentials are given by the equation
d+
R×S→k×S
(
ξ(n)
i,j
)
= u(n)
S+1−i,j−k, j > k.
The positive column-removing diﬀerentials are given by the equation
d+
R×S→R×l
(
ξ(n)
i,j
)
= u(n)
S+l+1−i,j, i > l.
The negative row-removing diﬀerentials are given by the equation
d−
R×S→k×S
(
ξ(2)
1,k+1
)
= 1.
50 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
The negative column-removing diﬀerentials are given by the equation
d−
R×S→R×l
(
ξ(2)
l+1,1
)
= 1.
The diﬀerentials vanish on all other generators of the colored HOMF LY homology.
One can check that the degrees of these diﬀerentials agree with th e expected ones.
The duality between positive and negative diﬀerentials is party explain ed by
the identities
d+
R×S→k×S (ξ(2)
1,k+1) = u(2)
S,1, d−
R×S→k×S (ξ(2)
1,k+1) = 1 ,
d+
R×S→R×l(ξ(2)
l+1,1) = u(2)
S,1, d−
R×S→R×l(ξ(2)
l+1,1) = 1 .
Finally, we describe the action of the universal diﬀerentials. As a mod el example,
consider the unreduced S2 homology of the unknot. It has two even generators
u1, u2 and two odd generators ξ1, ξ2. We deﬁne the universal diﬀerential on the
bottom row by the formula
d(f (u1, u2)) = u2
f (u1, u2)− f (−u1, u2)
u1
.
In other words,
d(ua
1ub
2) =
{
2ua−1
1 ub+1
2 , if a is odd ,
0, if a is even .
It is clear that d2 = 0 and the homology of d is isomorphic to C[u2
1], as predicted
by the grading restrictions in Section 3. Similarly, on higher levels we de ﬁne the
diﬀerential by the equation d(ξ1) = ξ2, so d(ξ1∧ ξ2) = 0. The total homology is a
free algebra generated by u2
1 and ξ1ξ2.
In general, we can always split variables into pairs, deﬁne a universal diﬀerential
in each pair as above and extend it to the whole algebra by the Leibnitz rule. For
example, in stable S2 homology of the (2,∞) torus knot we have two even generators
u3, u4 and two odd generators ξ3, ξ4. As in the above example, one can deﬁne a
universal diﬀerential by the equations
d(ua
3ub
4) =
{
2ua−1
3 ub+1
4 , if a is odd ,
0, if a is even , d(ξ3) = ξ4.
It clearly agrees with the description of the universal diﬀerential f or the trefoil in
Section 4.1.
5.2. Diﬀerential forms.
Definition 5.2. The unreduced moduli space
Mp,q(r) is deﬁned in the aﬃne
space with the coordinates u1, . . . , urp; v1, . . . , vrq by the equation
(5.5) (1 + u1z + u2z2 + . . . + urpzrp)q = (1 + v1z + v2z2 + . . . + vrq zrq)p.
which should hold at every coeﬃcient of its expansion in powers of z.
The spaceMp,q(r) can be also deﬁned in the aﬃne space with the coordinates
u1, . . . , urp by the coeﬃcients in the z-expansion of the equation
(1 + u1z + u2z2 + . . . + urpzrp)q/p,
starting from ( qr + 1)-st. Indeed, one can rewrite the equation (5.5) as
(1 + u1z + u2z2 + . . . + uprzpr)q/p = (1 + v1z + v2z2 + . . . + vqr zqr).
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 51
This will express vi through uj. The dimension of Mp,q(r) equals to r. Indeed, let
us forget the scheme structure and study the underlying subset of the aﬃne space.
One has U (z)q = V (z)p for coprime p and q iﬀ there exists a polynomial F (z) such
that U (z) = F (z)p, V (z) = F (z)q. Since F (z) starts from 1 and has degree r, we
have r parameters at our disposal.
Conjecture 5.3. The unreduced Sr homology of the ( p, q) torus knot is the
space of diﬀerential forms on Mp,q(r):
(5.6) H
Sr
(T (p, q)) = Ω •(Mp,q(r)) .
As an illustration of this conjecture, let us consider an example of th e unknot.
We can choose p = q = 1, so (5.5) takes the form
1 + u1z + u2z2 + . . . + urzr = 1 + v1z + v2z2 + . . . + vrzr
ThereforeMp,q(r) = Spec C[u1, . . . , ur], and
Ω•(Mp,q(r)) = C[u1, . . . , ur, du1, . . . , dur].
This agrees with the above description of the unreduced Sr-colored triply graded
homology of the unknot.
For a more interesting example, consider the S2-colored trefoil knot. The gen-
erators are u2, u3, u4, and the deﬁning equations are
(5.7) − 3
16 u3(u2
2− 4u4) = 3
128 (u4
2− 8u2u2
3− 8u2
2u4 + 16u2
4) = 0 ,
− 1
32 u3(−3u3
2 + 2u2
3 + 12u2u4) = 0 .
Definition 5.4. The reduced moduli space Mp,q(r) is deﬁned in the aﬃne
space with the coordinates ur+1, . . . , upr; vr+1, . . . , vqr by all coeﬃcients in the z-
expansion of the equation
(5.8) (1 + ur+1zr+1 + ur+2zr+2 + . . .+ uprzpr)q = (1 +vr+1z + v2z2 + . . .+ vqr zqr)p
One can check that Mp,q(r) deﬁnes a single point 0, so it is zero-dimensional.
We propose the following
Conjecture 5.5. The reducedSr homology of the ( p, q) torus knot is the space
of diﬀerential forms on Mp,q(r):
(5.9) HSr
(T (p, q)) = Ω •(Mp,q(r)) .
For r = 1 this conjecture is equivalent to the main conjecture of [ 37], since
by the results of [ 35] the right hand side of (5.9) can be identiﬁed with a certain
isotypic component of the ﬁnite-dimensional representation of ra tional Cherednik
algebra with parameter p/q. Moreover, it follows from [ 37] for r = 1 and from [ 23]
for general r that the ( a, q)-character of Ω ∗(
Mp,q(r)) is equal to the unreduced Sr-
colored HOMFLY polynomial of the (p, q) torus knot. One can also check ([ 23]) that
the ( a, q)-character of Ω ∗(Mp,q(r)) is equal to the reduced Sr-colored HOMFLY
polynomial of the same knot.
Let us describe the gradings on the space Ω ∗(Mp,q(r)). The a-grading is deﬁned
by the degree of a diﬀerential form, so that a(ui) = 0 , a (dui) = 2 . Furthermore, we
deﬁne the ( q, tr, tc) gradings by the formula
(5.10) ( q, tc, tr)[ui] =
(
2i, 2i− 2, 2
⌊ i− 1
r
⌋)
,
52 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
1 u3 u4 u2
3
du3 du4 u3du3 u3du4
du3∧ du4
0 2 4 6 8 10 12 q
Figure 21. Algebraic model for the S2 homology of the trefoil.
(q, tr, tc)[dui] =
(
2i− 2, 2i− 1, 2
⌊ i− 1
r
⌋
+ 1
)
.
It is easy to check that the deﬁning equations of Mp,q(r) are homogeneous in
q-grading and not homogeneous in t-gradings. Therefore, strictly speaking, on
Ω∗(Mp,q(r)) we get ( a, q) bigrading and a pair of ﬁltrations ( tr, tc).
For example, in the uncolored case the reduced homology of the tre foil knot
has only one bosonic generator u2, and the deﬁning equation for M2,3(1) reads as
(5.11) u2
2 = 0
Similarly, for the (3 , 4) torus knot the reduced uncolored homology has two bosonic
generators u2 and u3, with the following deﬁning equations for M3,4(1):
(5.12) u2u3 = 0, 2u3
2
9 = u2
3.
Finally, the reduced S2-colored homology of the trefoil knot has two even generators
u3 and u4 and the deﬁning equations can be obtained from (5.7) by setting u2 = 0:
u3u4 = u2
4 = u3
3 = 0.
Their diﬀerentials have the form
u3du4 + u4du3 = 2u4du4 = 3u2
3du3 = 0.
Therefore one can check that the monomial basis in Ω ∗(M2,3(2)) is given by
(5.13) 1 , u 3, u 4, u 2
3, du 3, du 4, u 3du3, u 3du4, du 3∧ du4.
We illustrate this homology with the Figure 21 (compare with the Figure s in Section
4.1).
For example, by computing the gradings of the basic elements (5.13) one ﬁnds
the Poincar´ e polynomial of the S2-colored trefoil knot (in the ( a, q, tr) grading):
(5.14)P S2
(31) = 1+ q6t2+q8t2+q12t4+a2q4t3+a2q6t3+a2q10t5+a2q12t5+a4q10t6.
More generally, for the Sr-colored reduced homology of the trefoil knot the ( a, q, tr)
gradings of the generators are given by the equations:
(a, q, tr)[ui] = (0 , 2i, 2), (a, q, tr)[dui] = (2 , 2i− 2, 3).
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 53
In particular, the monomial ui
r+1· dur+1∧ dur+2∧ dur+j has grading
i(0, 2r + 2, 2) +
j∑
l=1
(2, 2r + 2l− 2, 3) = (2 j, 2(r + 1)i + 2jr + j(j− 1), 2i + 3j)
and contributes the term a2jq2(r+1)i+2rj+j(j−1)t2i+3j
r in the Poincar´ e polynomial
(5.15) P Sr
(31) = a2rq−r ∑
i+j≤r
a2jq2(r+1)i+2rj+j(j−1)t2i+3j
r
[r]!
[i]![j]![r− i− j]! ,
obtained from the categoriﬁcation of the Volume Conjecture and t he super- A-
polynomial [ 26, 27, 28 ]. Here [ N ]! is the unbalanced quantum factorial:
[N ]! = [ N ]· [N− 1]· . . . [2]· [1]′,
[N ]′ = qN− 1
q− 1 = 1 + q + . . . + qN−1.
and one can easily verify that (5.15) satisﬁes the reﬁned exponent ial growth con-
jecture as well as the rest of the structural properties of sect ion 3.
Finally, let us match the gradings (5.10) with those in the constructio n of
Section 2.4. We have R = 1 , S = r, so there are generators u(n)
i,1 , ξ(n)
i,1 , 1≤ i≤ r
with gradings
(a, q, tc, tr)[u(n)
i,1 ] = (0 , 2 + 2rn− 2i, 2rn− 2i, 2n− 2),
(a, q, tc, tr)[ξ(n)
i,1 ] = (2 , 2r(n− 1) + 2i− 2, 2r(n− 1) + 2i− 1, 2n− 1).
Indeed, these gradings agree with (5.10) if one identiﬁes
u(n)
i,1 = urn+1−i, ξ (n)
i,1 = dur(n−1)+i.
5.3. Diﬀerentials for supergroups. It has been conjectured in [ 34, Conj.
3.22] that the diﬀerentials d0, d±n belong to a bigger algebra. In particular, for the
uncolored homology of (4 , 5) torus knot the following operators were introduced: α2
of (a, q, t) degree (−2,−2,−5), α1 of (a, q, t) degree (−2, 2,−3). Their introduction
was motivated by the observation that the “usual” diﬀerentials dN applied to the
(unique) generator with top a-degree 6 do not generate uncolored triply graded
homology: there are 7 nontrivial diﬀerentials d0, d±n, while there are 9 generators
with a-degree 4. The extra diﬀerentials solve this problem. We can now iden tify
these operators with the supergroup diﬀerentials:
α2 = d1|2, α 1 = d2|1.
In total, for the uncolored (4,5) knot we have 9 nontrivial diﬀerent ials:
d1 = d1|0, d −1 = d0|1,
d2 = d2|0, d 0 = d1|1, d −2 = d0|2,
d3 = d3|0, α 1 = d2|1, α 2 = d1|2, d −3 = d0|3.
For a general ( n, m) torus knot ( m > n ) we will have all diﬀerentials da|b with
a + b < n , of total number
2 + 3 + 4 + ... + n = n(n + 1)
2 − 1 = (n + 2)(n− 1)
2 .
It has been explained in [ 37] that the diﬀerentials are tightly related to the (conjec-
tural) action of the rational Cherednik algebra Hc on the triply graded homology
54 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
of torus knots. More precisely, [ 37, Deﬁnitions 7.2-7.3] assign a diﬀerential to every
Sn-equivariant copy of the standard ( n− 1)-dimensional irreducible representation
Vn inside Hc. These diﬀerentials satisfy some nice properties: for example, if th e
two copies α and β are pure, then by [ 37, Lemma 7.7] the corresponding diﬀerentials
dα and dβ anticommute.
The new supergroup diﬀerentials can be naturally embedded in this fr amework.
Namely, recall that Hc has generators xi, yj. We deﬁne α(m|k) to be a copy of Vn
spanned by xm
i yk
i , and
dm|k = dα(m|k).
Since this copy is pure in the sense of [ 37], the corresponding diﬀerentials anticom-
mute. Moreover, one can check that α(m|k) span HomSn (Vn, Hc), so the supergroup
diﬀerentials form a complete collection of diﬀerentials for the uncolor ed torus knot
homology. The grading conventions of [ 37] assure that dm|n have the prescribed
gradings.
5.4. Examples. We have compared the results of 4.1 with the algebraic model
in (5.13). Let us make the similar comparisons for other torus knots in Section 4.
The stable reduced
-colored homology of (2 ,∞) torus knot have 4 even and 4
odd generators u(2)
ij and ξ(2)
ij (see Section 5.1). They have the following ( a, q, tc, tr)-
degrees:
deg[u(2)
11 ] = (0 , 10, 6, 4), deg[u(2)
12 ] = (0 , 8, 6, 6),
deg[u(2)
21 ] = (0 , 8, 4, 4), deg[u(2)
22 ] = (0 , 6, 4, 6),
deg[ξ(2)
11 ] = (2 , 4, 5, 5), deg[ξ(2)
12 ] = (2 , 2, 5, 7),
deg[ξ(2)
21 ] = (2 , 6, 7, 5), deg[ξ(2)
22 ] = (2 , 4, 7, 7).
As explained in Section 5.1, Q
[
u(2)
ij
]
= 4 and Q
[
ξ(2)
ij
]
= 2. For example, the
“bottom row” of the homology (with appropriate shift of gradings) is 16-dimensional
and has monomial basis
1, u (2)
21 ,
(
u(2)
21
) 2
,
(
u(2)
21
) 3
,
(
u(2)
21
) 4
,
u(2)
11 , u (2)
11 u(2)
21 , u (2)
11
(
u(2)
21
) 2
,
u(2)
12 , u (2)
12 u(2)
21 , u (2)
12
(
u(2)
21
) 2
,
u(2)
22 , u (2)
22 u(2)
21 , u (2)
22
(
u(2)
21
) 2
,
(
u(2)
22
) 2
,
(
u(2)
11
) 2
.
The self-symmetry map Φ reﬂects ﬁrst four sets of monomials in the vertical axis,
and preserved two remaining monomials.
The stable reduced
-colored homology of (2 ,∞) torus knot have 6 even and
6 odd generators. They have the following ( a, q, tc, tr)-degrees:
deg[u(2)
11 ] = (0 , 12, 6, 6), deg[u(2)
12 ] = (0 , 10, 6, 8),
deg[u(2)
13 ] = (0 , 8, 6, 10), deg[u(2)
21 ] = (0 , 10, 4, 6),
deg[u(2)
22 ] = (0 , 8, 4, 8), deg[u(2)
23 ] = (0 , 6, 4, 10),
deg[ξ(2)
11 ] = (2 , 4, 5, 7), deg[ξ(2)
12 ] = (2 , 2, 5, 9),
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 55
deg[ξ(2)
13 ] = (2 , 0, 5, 11), deg[ξ(2)
21 ] = (2 , 6, 7, 7).
deg[ξ(2)
22 ] = (2 , 4, 7, 9), deg[ξ(2)
23 ] = (2 , 2, 7, 11).
Indeed, Q
[
u(2)
ij
]
= 4 and Q
[
ξ(2)
ij
]
= 2.
Finally, consider the S2-colored (3 , 4) torus knot. In the notations of Section
5.2, we have 4 generators u3, u4, u5, u6 of ( a, q, tc, tr) gradings
deg u3 = (0, 6, 4, 2), deg u4 = (0, 8, 6, 2),
deg u5 = (0, 10, 8, 4), deg u6 = (0, 12, 10, 4).
Note that in the notations of Section 5.1, one would have
u3 = u(2)
21 , u 4 = u(2)
11 , u 5 = u(3)
21 , u 6 = u(3)
11 ,
and the grading conventions agree. The deﬁning relations have the form
u3
3− 9u4u5− 9u3u6 = 2u2
3u4− 3(u2
5 + 2u4u6) = u3u2
4 + u2
3u5− 3u5u6 = 0,
5u4
3− 12u3
4− 72u3u4u5− 36u2
3u6 + 54u2
6 = 5u3
3u4− 9u2
4u5− 9u3(u2
5 + 2u4u6) = 0 .
One can check that the monomial basis on the “bottom row” is given b y the fol-
lowing 25 monomials:
1, u 3, u 2
3, u 3
3, u 4
3, u 5
3, u 6
3,
u4, u 4u3, u 4u2
3, u 4u3
3, u 4u4
3,
u5, u 5u3, u 5u2
3, u 5u3
3,
u6, u 6u3, u 6u2
3, u 6u3
3,
u2
4 u2
4u3, u 2
4u2
3,
u2
5, u3
4.
The self-symmetry map Φ reﬂects ﬁrst ﬁve sets of monomials in the v ertical axis,
and preserved two remaining monomials.
6. HOMFL Y homology from A-model and B-model
In this section, we wish to look for geometric and physical models for colored
HOMFLY homology, eventually formulating it in the language of symplec tic geom-
etry or the so-called A-model.
Indeed, in mirror symmetry, the so-called B-model is famous for its formulation
in the language of complex (algebraic) geometry, while the A-model s ide involves
symplectic invariants, Fukaya category, and quantum cohomology [58]. Clearly,
the algebraic model described in the previous section is closer to the B-model, and
therefore it will be our natural starting point here. Then, we will re late it to various
problems — that are interesting in their own right — in mirror symmetry and in
symplectic geometry. We will give several reformulations, in terms o f A-model and
B-model, open and closed ( i.e. with and without D-branes), in all of which colored
HOMFLY homology will be realized as cohomology of a suitable BRST oper ator
Q, such that Q2 = 0:
(6.1) Hλ(K) = Q-cohomology .
In physics literature, Q is often called “supercharge” and its cohomology is often
called the space of BPS states since its elements are the so-called BPS states (=
supersymmetric conﬁgurations). Even though precisely this inter pretation of knot
homology was proposed in [ 41] and studied from various vantage points in [ 2, 19,
39, 50, 87 ], the A-model and B-model reformulations discussed here appear to be
56 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
completely new and do not make direct contact with any of the existe nt geometric
/ physical models of knot homologies. Therefore, by pursuing some of these new
geometric descriptions further one is likely to learn a lot about colore d HOMFLY
homology and, possibly, even about homological mirror symmetry.
6.1. B-model on a supermanifold. With this goal in mind, we start by
reformulating the Conjectures 5.3 and 5.5 in terms of B-model on a s uper-manifold
Cd|d with a certain Landau-Ginzburg potential Wsuper(K; λ), such that
(6.2) Hλ(K) ∼
= J ac(Wsuper(K; λ))
Note, that Cd|d is a super-Calabi-Yau manifold (see [ 3, 77, 88 ]).
Speciﬁcally, consider the potential W (T (p, q); Sr) on the u-space given by the
formula
(6.3) W (T (p, q); Sr) = Coef (p+q)r+1(1 + u1z + . . . + uprzpr)
q+p
p .
Let us rename dui by ξi and introduce a potential Wsuper(T (p, q); Sr) on the su-
perspace Cpr|pr with coordinates ui, ξi by the formula
(6.4) Wsuper(T (p, q); Sr) :=
∑
i
∂W
∂ui
ξi .
The space of diﬀerential forms Ω •(
Mp,q(r)
)
is isomorphic to the Jacobi ring of
Wsuper(T (p, q); Sr):
(6.5) Ω
[
Mp,q(r)
]
= C[u1, . . . , upr, ξ1, . . . , ξpr]/
(∂Wsuper
∂ui
, ∂Wsuper
∂ξi
)
.
According to the Conjecture 5.3, both spaces represent the unr educed Sr-colored
homology of the ( p, q) torus knot. Indeed, the partial derivatives of W (T (p, q); Sr)
are equal to
∂W (T (p, q); Sr)
∂ui
= Coef (p+q)r+1
∂
∂ui
(1 + u1z + . . . + uprzpr)
q+p
p =
q + p
p Coef (p+q)r
[
zi(1 + u1z + . . . + uprzpr)
q
p
]
=
q + p
p Coef (p+q)r+1−i(1 + u1z + . . . + uprzpr)
q
p , i = 1 . . . pr.
Therefore the ring of functions on Mp,q(r) coincides with the Jacobi ring of W :
(6.6) C
[
Mp,q(r)
]
= C[u1, . . . , upr]/
(∂W
∂ui
)
.
The full space of diﬀerential forms Ω •(
Mp,q(r)
)
is a quotient of the space of
all diﬀerential forms on Cpr by the equations
(6.7) ∂W
∂ui
= 0,
∑
j
∂2W
∂ui∂uj
· duj = 0.
The Jacobi ring of Wsuper is deﬁned by the following equations:
∂Wsuper
∂ξi
= ∂W
∂ui
= 0
∂Wsuper
∂ui
=
∑
j
∂2W
∂uj∂ui
ξj = 0.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 57
Since these equations coincide with (6.7), we get the relation (6.5).
In the mirror symmetry literature [ 77, 78, 3, 31 ], the setup we just described
is called a Landau-Ginzburg B-model with target space Cd|d and superpotential
Wsuper(K; λ). The function Wsuper(K; λ) is called superpotential even when the
target space is an ordinary (bosonic) manifold, e.g. W (ui) in our discussion might
be called superpotential of a Landau-Ginzburg model on Cpr. As a ﬁnal clariﬁcation
of terminology, we should mention that a model is called Landau-Ginzburg model
when the superpotential is non-zero, and is referred to as the sigma-model (on a
certain target manifold) when W = 0.
In our case, the colored HOMFLY homology (of torus knots) is realiz ed as the
Jacobi ring 7 (6.2) - (6.5) of a Landau-Ginzburg model on Cpr|pr with the superpo-
tential Wsuper(T (p, q); Sr). There are several aspects of this B-model that make it
rather special and interesting, the main of which is undoubtedly the fact that the
target space Cpr|pr is a supermanifold.
It is instructive, though, to start with a more familiar and conventio nal B-
model with a target space X. Then, we will extend it to a Landau-Ginzburg model
with a superpotential W and will see why (6.2) - (6.5) can be interpreted as a ring
of observables with and without D-branes (called B-branes in the co ntext of the
B-model). In general, we shall use X for the target space of the B-model and Y for
the target space of the A-model, so that X and Y are mirror manifolds in most of
our applications.
First, as a warm-up and a lightning review of the relevant facts abou t B-model,
let us consider a B-model with target space X. The space of observables — or, to
be more precise, the space of closed (string) observables — in such model is then
identiﬁed with the ∂-cohomology of X with values in ⋀ p TX:
(6.8) H q
(
X,
p⋀
T 1,0
X
)
Indeed, every (0 , q)-form on X with values in ⋀ p TX
(6.9) A = dzk1 . . . dzkq Aj1...jp
k1...kq
∂
∂zj1
. . . ∂
∂zjp
in the topological B-model deﬁnes an observable:
(6.10) OA = η
k1 . . . ηkq Aj1...jp
k1...kq
θj1 . . . θjp
Contracting this “(−p, q)-form” with the holomorphic ( n, 0)-form Ω on X we ob-
tain an isomorphism between this space and ( n− p, q)-forms, where n is the total
(complex) dimension of X. Moreover, {Q,OA} =−O∂A, so that observables in
the B-model are Dolbeault cohomology of forms valued in exterior po wers of the
holomorphic tangent bundle, i.e. elements of (6.8).
Incorporating a superpotential W⁄= 0 leads to a Landau-Ginzburg model where
the Q-operator acts as a diﬀerential Q = ∂ + Qbdry, such that
(6.11) Q2 = W· id
As a result, the space of closed string states in the Landau-Ginzbu rg model can be
described as a Hochschild homology or, equivalently, as a hypercoho mology:
(6.12) HH∗(M F(X, W ))∼
= H∗(Λ∗Ω X , dW∧)
7also known as the “chiral ring” or “ring of observables,” see below
58 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
where Λ ∗Ω X denotes the exterior powers of the sheaf of diﬀerential forms. T he
dual cohomology theory is
(6.13) HH∗(M F(X, W ))∼
= H∗(Λ∗TX , [W,−])
where Λ∗TX denotes exterior powers of the tangent sheaf and [ W,−] denotes the
Lie bracket with W . In particular, if f1, . . . , fn are sections of line bundles Ei on a
smooth variety V , then they deﬁne a function W : Tot(⊕E∗
i )→ C and we have the
following equivalence of categories 8
(6.14) M F(Tot(⊕E∗
i ), W )∼
= QCoh({fi = 0})
that allows to describe B-branes in a Landau-Ginzburg theory with t he superpo-
tential W (i.e. objects in the category of matrix factorizations of W ) in terms of
the category of coherent sheaves on the critical variety of W .
Theorem 6.1 ([ 72]).
(6.15) H 0(M F(W ))∼
=Db
sing(W−1(0))
Note, this brings us very close to our applications (5.6) and (5.9), wh ere the
moduli spaces
Mp,q(r) andMp,q(r) are deﬁned by polynomial equations fi(uj) = 0
in the space X = Cpr of u’s. In situations like this, when the equations fi(uj) = 0
integrate to a superpotential W (uj) the chiral ring (also known as the ( c, c) ring)
of the Landau-Ginzburg model on X = Cn is isomorphic to the quotient of the ring
of polynomial functions C[u1, ..., un] by dW ,
(6.16) Rclosed(Cn, W ) = C[ui]/(dW )
When W is quasihomogeneous, this ring is graded by the R-charge symmetry U (1)R.
In order to interpret the colored HOMFLY homology, though, in the Landau-
Ginzburg model we need not only to ﬁnd a natural home for the modu li spaces
Mp,q(r) and Mp,q(r) but also to describe the corresponding spaces of diﬀerential
forms (5.6) and (5.9) in the B-model language. One way to do this is to replace the
target space Cn by the supermanifold X = Cn|n and to replace the superpotential
W (ui) by Wsuper(ui, ξi) deﬁned in (6.4). This gives then
(6.17) Rclosed(Cn|n, Wsuper) = Ω ∗(M)
whereM ={u∈ C|fi(u)≡ ∂iW (u) = 0 }. Speciﬁcally, for the superpotential
Wsuper deﬁned by (6.3) and (6.4) we get a B-model realization of the Sr-colored
HOMFLY homology of torus knots. For instance, from (5.7), (5.11) , and (5.12) we
ﬁnd the following potentials in simple examples considered earlier:
W (31; ) = u3
2,
Wsuper(31;
) = 3 u2
2ξ2,
W (819;
) =− 7u4
2
243 + 14u2u2
3
27 ,
Wsuper(819; ) =
(
− 28u3
2
243 + 14u2
3
27
)
ξ2 + 28u2u3
27 ξ3,
8The analogous statement for the topological A-model is:
F uk(Y, W) ∼
= F uk(Sing (W )) .
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 59
W (31; ) = 5
256 u3(3u4
2− 8u2u2
3− 24u2
2u4 + 48u2
4).
Although conceptually this Landau-Ginzburg model should be the eﬀ ective two-
dimensionalN = 2 theory on D in the brane construction (2.2) studied in [ 19, 27,
28], the setup appears to be surprisingly diﬀerent. Yet, in both cases , the Poincar´ e
polynomial of the colored HOMFLY homology is realized as a supersymm etric
index (character) of the two-dimensional N = 2 theory on D. One important
diﬀerence is that here we have a diﬀerent 2d N = 2 theory for each particular
value of the color, whereas in loc. cit. a single 2d N = 2 theory determines Sr-
colored superpolynomials for all values of r. It would be interesting to understand
better how the new Landau-Ginzburg realization of the colored HOM FLY homology
discussed here relates to the 2d N = 2 theory on D studied in [ 19, 27, 28 ].
6.2. B-branes and open B-model. There is another way, however, to de-
scribe the space of diﬀerential forms that is familiar to practitioner s of mirror
symmetry. This will require introducing one more ingredient in our sto ry, namely
D-branes, and considering the space of open string states, i.e. the states of open
strings stretched between branes. In the context of topologica l B-model branes are
usually called B-branes. Mathematically, B-branes are objects of t he derived cate-
gory of coherent sheaves Db(X) in the case of the sigma-model (when W = 0), or
the category of matrix factorizations M F(X, W ) in the case of Landau-Ginzburg
model with the target space X and superpotential W . We already saw both of these
categories in our previous discussion and now we will spend more time d iscussing
their objects, or B-branes.
Note that both the derived category of coherent sheaves and th e category of
matrix factorizations are also familiar to practitioners of knot homo logy: these
categories play a key role in the constructions of e.g. [13, 55, 56, 84, 89, 91 ].
Now, let us describe the “open” analogue of (6.8) and (6.16), i.e. the space
of states of open strings ending on a brane B in the B-model, starting with the
sigma-model on X (with W = 0), as we did in our previous discussion, and then
extend it to branes in more general Landau-Ginzburg models. In bo th cases, the
conclusion will be that open strings ending on B form an algebra, which is the Ext
algebra9
(6.18) Ropen(B) = Ext ∗(B,B) .
In order to see how it comes about, let us ﬁrst consider two diﬀeren t branes, B1
andB2, represented by shaves E andF supported on S⊂ X. Then, states of open
strings stretched between B1 andB2 are elements of
(6.19) H q
(
S,E∨⊗F⊗
p⋀
NS/X
)
There is a spectral sequence with (6.19) as the second page that c onverges to [ 76]:
(6.20) Ext p+q
X (E,F )
and in many cases one has
(6.21) Ext n
X (E,F ) ∼
=
⨁
p+q=n
H q
(
S,E∨⊗F⊗
p⋀
NS/X
)
9The algebra structure comes from the Yoneda product on the se lf-Ext groups.
60 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
because the spectral sequence degenerates at E2.
Now let us see how the boundary chiral ring (6.18) can help us to prod uce yet
another interpretation of (5.6) and (5.9) in open B-model. The simplest example
is the unknot colored by λ = Sr, whose HOMFLY homology H
Sr
( ) is realized
as the space of diﬀerential forms on V = Spec C[u1, . . . , ur]. The corresponding
choice of B-brane is closely related to SYZ brane [ 80] that plays an important
role in mirror symmetry. Namely, it is well known that for a “zero-bra ne” ( i.e.
a skyscraper sheaf Op) supported at a smooth point on a manifold X of complex
dimension r the open string algebra (6.18) is the exterior algebra
(6.22) Ext ∗(Op,Op) ∼
= Λ∗(V )
where V = TpX∼
= Λ∗Cr. In order to upgrade Λ ∗(V ) to the space of diﬀerential
forms Ω ∗(V ) = C[V ]⊗ Λ( V∨), one simply needs to replace X∼
= Cr by its com-
plexiﬁcation XC∼
= X× X, and consider a B-brane B =O∆ , where ∆ ∼
= Cr is the
diagonal in X× X∼
= Cr× Cr. Note, the new target space X× X∼
= C2r can be
viewed as a SYZ torus ﬁbration with a singular ﬁber at the origin. To fa cilitate a
discussion of the mirror A-model that will follow next, it is convenient to replace
X = Cr by X = ( C∗)r. Then, the target space X× X ∼
= (C∗)2r is also a T 2r
ﬁbration, but without singular ﬁbers and one has
(6.23) Ropen(B) = Ext ∗(O∆ ,O∆ ) ∼
= C[u±1
i , dui]
Before we proceed to the mirror A-model, let us brieﬂy discuss anot her interesting
feature of this example.
Note that (6.23) can be identiﬁed with HH∗(Db(X)) ∼
= C[u±1
i , dui] which,
according to our previous discussion, describes closed string states, not open. This
is an illustration of a more general phenomenon: open string states (6.18) of a
B-brane supported on the diagonal ∆ ⊂ X× X can be identiﬁed with the closed
string states (6.8) of a B-model on X. The mathematical content of this statement
is summarized in the following:
Theorem 6.2 (Hochschild-Kostant-Rosenberg isomorphism [ 48]).
(6.24) Ext n
X×X (O∆ ,O∆ ) ∼
=
⨁
p+q=n
H q
(
X,
p⋀
TX
)
where ∆ is the diagonal in X× X.
Moreover, Yekutieli [90] shows that there is an isomorphism from the hyperco-
homology to self-Ext:
(6.25) Hn(X, Dpoly(X)) = Ext n
X×X (OX ,OX )
which is compatible with the cup product on the left and the Yoneda pr oduct on
the right. And using the isomorphism between the Hochschild cohomo logy and the
polyvector ﬁeld cohomology [ 30], one has
(6.26) HH∗(Db(X)) ∼
= Ext∗
X×X (O∆ ,O∆ ) ∼
= H∗(X, Λ∗TX )
6.3. HOMFL Y homology from symplectic geometry. Now, let us see
what kind of A-models one gets by applying mirror symmetry to the op en and
closed B-models in the above discussion.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 61
In general, we denote by Y the mirror of X. The simplest example is X = (C∗)r
viewed as a (trivial) T r ﬁbration over Rr. Then, mirror symmetry is simply a T-
duality (a “Fourier transform”) along the ﬁbers, and the mirror ma nifold is Y ∼
=
T∗T r. The mirror of the statement HH∗(Db(X))∼
= C[u±1
i , dui] is the statement
about the Hochschild cohomology of the Fukaya category F (Y ),
(6.27) HH∗ (F (T∗T r)) ∼
= C[u±1
i , dui]
which, by analogy with (6.26), can be also realized as the boundary OP E algebra
in the A-model of Y×
Y , where Y denotes the space Y with the symplectic form
−ω. Indeed, in general, when a symplectic manifold Y has “enough” Lagrangians,
the Hochschild cohomology its Fukaya category F (Y ) is expected [ 1, 58, 17 ] to be
isomorphic to the Lagrangian Floer cohomology of the (anti-)diagon al ∆ Y֒→Y×Y ,
(6.28) HH∗ (F (Y )) ∼
= HF∗(∆ Y , ∆ Y )
Thus, in our basic example of (6.23) and (6.27) mirror symmetry maps a B-brane
B = O∆ X to a Lagrangian A-brane supported on the conormal bundle T∨
∆ to
T∆ ⊂ T n× T n in Y× Y = T∗T r× T∗T r, so that
(6.29) HF∗(T∨
∆ , T∨
∆ ) ∼
= C[u±1
i , dui]
This is an open A-model version of (6.27) and a concrete illustration o f (6.28).
In general, this leads us to the following picture, where the (colored ) HOMFLY
homology is realized either in terms of closed A-model of a symplectic m anifold Y
(6.30) HSr
(K) = HH∗ (F (Y ))
or in terms of open A-model (Floer homology) of a certain Lagrangia n submanifold
L,
(6.31) HSr
(K) = HF∗(L, L)
(In our previous discussion, L was the (anti-)diagonal ∆ Y֒→Y×
Y , but we al-
low more general Lagrangian submanifolds and more general symple ctic manifolds
here.) For torus knots, the closed A-model version can be obtaine d by applying the
supermanifold version of mirror symmetry [ 3, 31, 78 ] to the B-model in section
6.1. We plan to return to a systematic study of this mirror symmetry elsewhere.
Here, let us simply point out that even for non-torus knots one migh t hope to
ﬁnd a realization of the form (6.31). For example, for the ﬁgure-eig ht knot K = 4 1
and r = 1 a natural guess is
(6.32) L = S2 with 3 punctures
embedded in some symplectic manifold Y , such that HF∗(L, L)∼
= H∗(L).
7. “Bottom row” of the colored HOMFL Y homology
In this part we wish to study the “bottom row” of the colored super polynomial,
deﬁned as
(7.1) P λ
bottom(q, t) := lim
a→0
a#P λ(a, q, t) ,
where a# denotes the appropriate power of a, such that the product a#P λ(a, q, t)
contains only non-negative a-degrees starting from zero.
62 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
7.1. Combinatorial interpretation for torus knots. First, let us recall
the conjectural combinatorial description of the uncolored triply graded homology
for a ( p, q) torus knot [ 34, 36, 69 ]. Consider a p× q rectangle and a N W− SE
diagonal in it.
Proposition 7.1. ([34]) The dimension of the “bottom row” of the reduced
uncolored homology equals to the number of lattice paths in this rect angle strictly
below the diagonal:
dimHbottom(T (p, q)) = cp,q = (p + q− 1)!
p!q! .
For example, if q = p + 1, this dimension equals to the p-th Catalan number.
Proposition 7.2. ([34]) The dimension of the “ k-th row” of the reduced un-
colored homology equals to the number of lattice paths below the diag onal with k
marked corners:
dimHa=k(T (p, q)) = (p + q− k− 1)!
p· q· k!· (p− k− 1)!(q− k− 1)! .
A q-analogue of this formula was discussed in [ 11, eq. (3.46)]. Both of these
propositions motivate the following combinatorial construction, co mpleted in [ 69]
where it was matched to the algebro-geometric constructions of [ 70].
The basis inHp,q is enumerated by the lattice paths in the p× q rectangle with
marked corners. To every such path we assign three gradings, wh ere a-grading
corresponds to the number of marked corners. Let us describe q− and t− grad-
ings. For simplicity, we will focus on the bottom row, considered in det ails in [ 36].
Corrections for the higher rows can be found in [ 69].
Let us interpret a lattice path as a Young diagram D. Consider the C∗× C∗
action on the Hilbert scheme of N points on C2, and let us restrict it to a one-
parameter subgroup ( tp, tq). One can check (see e.g. [67]) that the action of this
subgroup has isolated ﬁxed points parametrized by the Young diagr ams with N
boxes. Therefore the corresponding moment map is a Morse funct ion on Hilb N (C2),
and its gradient ﬂow induces the Bialynicki-Birula cell decomposition of the Hilbert
scheme [67, 22 ]. We are interested in the dimension of the cell CD labelled by the
ﬁxed point D, which is given by the following formula:
dim CD =|D| + h+
p/q(D),
where
(7.2) h+
p/q(D) = ♯
{
c∈ D
a(c)
l(c) + 1≤ p
q < a(c) + 1
l(c)
}
.
Here a(c) and l(c) denote the arm and the leg of a cell c in a diagram D:
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 63
a(c)
l(c)
p
q
The statistics h+
p/q(D) was introduced in [ 62] in connection with some combi-
natorial models of the bigraded Catalan numbers.
Proposition 7.3. The gradings of Dyck paths are given by the following equa-
tions:
(1) The q-grading assigned to D equals to 2
[
|D| + 2h+
p/q(D)
]
.
(2) The t-grading assigned to D equals to 2|D|.
Motivated the reﬁned exponential growth conjecture, we assum e that the di-
mension of the Sr-colored homology is equal to the r-th power of the uncolored
homology, i.e. the r-th power of the generalized Catalan number cp,q. Therefore it
is natural to assume that one can ﬁnd a basis in the Sr-colored homology labelled
by all possible r-tuples of Young diagrams in p× q rectangle below the diagonal.
Conjecture 7.4. The bottom row of the Sr colored homology of the ( p, q)
torus knot has a basis labeled by the r-tuples ( D1, . . . , Dr) of the Dyck paths in
p× q rectangle. The ( Q, tr) gradings of Dyck paths are given by the following
equations:
(1) The Q-grading assigned to D equals to 2 ∑ r
i=1
[
|Di| + 2h+
p/q(Di)
]
.
(2) The tr-grading assigned to D equals to 2 ∑ r
i=1|Di|.
The q-grading (and, therefore, the tc-grading) has yet to be constructed. We
expect it to be related to the combinatorial constructions of [ 8] and [ 46].
7.2. Coupled instanton-vortex counting. The “bottom row” (7.1) has a
simple and beautiful interpretation in terms of instanton / vortex c ounting. As
a warm-up, let us start with a simple vortex counting problem that is e asy to do
“by hand” and that has all the essential features. Then, we shall upgrade it to the
equivariant instanton counting relevant to arbitrary knots and link s.
LetVm be the moduli space of m abelian vortices on a two-dimensional plane,
D = R2. In other words, Vm is the moduli space of solutions to the PDEs
(7.3) ∗FA = i|φ|2− it
∂Aφ = 0
where A is a connection on a U (1) bundle of ﬁrst Chern class m, and t is a parameter.
These equations describe supersymmetric conﬁgurations (BPS st ates) in a two-
dimensional theory on D withN = (2, 2) supersymmetry:
(7.4) Tvortex : U (1) gauge theory with a single charged ﬁeld φ
64 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
It is well known that Vm is a K¨ ahler manifold of (real) dimension 2 m. Namely,
(7.5) Vm = Sym m(C) ≡ Cm/Sm ,
where one can think of coordinates on Vm as vortex positions on D = R2∼
= C.
Since D admits a circle action, one can consider the equivariant character,
Ch q(Vm), with respect to the rotation group U (1)q acting on D. Indeed, U (1)q acts
onVm in a natural way, by equal phase rotations on all factors in the sym metric
product (7.5). Moreover, identifying the vortex moduli space Vm = Sym m(C) with
the space of monic polynomials of degree m,
(7.6) f (x) =
m∏
j=1
(x− xj ) = xm + a1xm−1 + . . . + am ,
we immediately deduce the isomorphism Vm∼
= Cm = ({a1, . . . , am}) and also learn
that U (1)q acts on the space Vm with weights (1 , 2, . . . , m). Therefore, the U (1)q-
equivariant character ofVm is
(7.7) Ch q(Vm) = 1
(1− q)(1− q2) . . . (1− qm) ,
in which a careful reader will recognize the “bottom row” of the unnormalized
Sm-colored HOMFLY polynomial of the unknot.
This is not an accident, of course, and the physics setup (2.2) pred icts that the
“bottom row” of any λ-colored HOMFLY homology of any knot K has a similar
interpretation in terms of equivariant vortex counting on D = R2. In order to
explain this relation, we need to generalize our warm-up example in two important
ways: ﬁrst, we need to introduce the homological t-grading, and secondly we need
a generalization to arbitrary knots. Both of these problems can be achieved by
embedding D = R2 into a larger space M4 = R4, and realizing our vortex counting
problem on D as a special case of counting solutions to coupled instanton-vortex
equations or, equivalently, via equivariant instanton counting on the 4-manifo ld M4
in the presence of ramiﬁcation along D⊂ M4.
However, before we proceed to generalizations, let us stay a bit lon ger in the
world of vortex equations and explore the picture which seems to em erge:
(7.8) knot K ↝ 2d vortex theory Tvortex(K) ↝ Vm(K)
so that a suitable version Ch q,t(Vm) of the equivariant character computes the
bottom row of the colored superpolynomial (7.1) with λ = Sm,
(7.9) Ch q,t(Vm) = P Sm
bottom(q, t) .
Already at this stage the reader might suspect that incorporating the t-grading and
passing to knot homologies can be addressed by considering equivar iant cohomology
or K-theory of the vortex moduli space,
(7.10) H∗
U(1)q (Vm(K)) ,
where t-grading is identiﬁed with the homological grading. Although this idea is a
little too naive, it is actually on the right track, and it is instructive to p ursue it a
little further.
Therefore, as the natural next step let us consider a non-abelian generalization
of (7.3) that describes supersymmetric solutions in the 2d theory:
(7.11) Tvortex : U (p + 1) gauge theory with p + 1 fundamental ﬁelds φi
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 65
The corresponding vortex equations
(7.12) ∗FA = i∑ p+1
i=1 φiφ†
i− it
∂Aφi = 0
involve a U (p + 1) gauge connection and p + 1 Higgs ﬁelds φi in the fundamental
representation of the gauge group. Again, the m-vortex moduli space is a K¨ ahler
manifold of real dimension
(7.13) dim V U(p+1)
m = 2m(p + 1) ,
In particular, the single-vortex moduli space is well known to be a (2 p + 2)-
dimensional space
(7.14) V U(p+1)
1 ∼
= C× CPp
where the factor C parametrized by the “center-of-mass” position, while CPp en-
codes the “internal degrees of freedom” of a single non-abelian vo rtex. The rotation
symmetry U (1)q acts on C with weight 1, so we expect that it contributes to the
equivariant character a factor 1
1−q . However, unlike our ﬁrst example (related to the
unknot), now the moduli space V U(p+1)
1 has non-trivial topology and, therefore, if
t-grading is simply the homological grading on (7.10) the suitable gener alization of
the equivariant character should be a product of 1
1−q and the Poincar´ e polynomial
of CPp,
(7.15) 1
1− q
p∑
i=0
t2i
This turns out to be the correct answer for the bottom row of the HOMFLY ho-
mology of the (2 , 2p + 1) torus knot.
Now let us explain why all these examples are “working” and where the con-
nection with vortex equations come from. The reason, in fact, is alr eady contained
in section 2.1 where we reviewed the interpretation (2.1) of homologic al knot invari-
ants in terms of supersymmetric conﬁgurations (BPS states) in th e string theory
setup (2.2). What this interpretation tells us is that specializing to th e bottom
row (7.1), i.e. taking the limit a→ 0, means the “large volume limit.” Indeed,
according to the identiﬁcation of the parameters (2.3), in this limit th e interesting
geometry (and topology) of the Calabi-Yau space X is replaced by the simplest
Calabi-Yau 3-fold, namely a ﬂat space:
(7.16) X
a→0
↝ C3 .
In other words, the bottom row of the colored HOMFLY homology is d escribed
by a much simpler “toy model” of (2.2) in which the pair ( X, LK) is replaced by
(C3, LK). (Not much happens to the Lagrangian submanifold LK in this limit.)
The next step is to look at this system from the vantage point of the 4-manifold
M4∼
= R4 and the defect (called the “surface operator” [ 44]) supported on D∼
=
R2. Before we took the limit a→ 0, the compactiﬁcation on X produces abelian
gauge theory on M4 with gauge group U (1) [ 53]. Incorporating an extra brane
in this setup means including the so-called surface operator suppor ted on D or,
mathematically speaking, ramiﬁcation in the gauge theory on M4.
LetMk,m be the moduli space of abelian instantons on M4 = R4 with rami-
ﬁcation along D⊂ M4. In other words, Mk,m is the moduli space of solutions to
66 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
the self-duality equation on M4\ D,
(7.17) F +
A = 0
with the second Chern class k, with the monopole number m = 1
2π
∫
D FA, and
with the prescribed behavior along D. The latter is what we call the ramiﬁcation
data; e.g. a simple example of the so-called tame ramiﬁcation can be obtained by
introducing a δ-function source in the self-duality equation (7.17) on M4:
(7.18) F +
A = 2 πα(δD)+ .
The gauge connections which solve this equation have a ﬁrst-order pole at D. More
generally, one can study solutions to self-duality equations with sing ularities of
arbitrarily high order,
(7.19) A = dz
(α1
z + α2
z2 + . . .
)
+ dz (. . .) .
This is called wild ramiﬁcation and is precisely how the dependence on the knot K
will enter, via the choice of the ramiﬁcation data. 10 Let us denote the corresponding
moduli space by Mk,m(K).
Much like the vortex moduli space Vm enjoyed an action of the rotation group
U (1)q, the moduli space of “ramiﬁed instantons” on M4\ D∼
= C× C∗ has an action
of the rotation group U (1)q× U (1)t, where U (1)q acts by rotations of D = C and
U (1)t acts by rotations of its normal bundle, C∗.
Then, in the limit (7.16) the physical interpretation (2.1) of the color ed HOM-
FLY homology predicts
(7.20) Ch q,t(M0,m(K)) =
P
Sm
bottom(K; q, t)
which is very close to (7.9) and, in fact, is exactly the sought-after proper gener-
alization of it. The connection with vortex equations is now easy to se e. At least
for some knots the moduli space Mk,m(K) can be equivalently described as the
moduli space of solutions to the coupled instanton-vortex equations :
F +
A = 2 πφ⊗ φ† (δD)+
∗DFB = iφ†⊗ φ− it1E(7.21)
∂A,Bφ = 0
where A is a unitary connection on the line bundle L over M4, B is a unitary
connection on the bundle E over D⊂ M4, φ is an element φ∈ H 0(Hom(E,L|D)),
and φ† is its adjoint.
As far as we know the instanton-vortex equations (7.21) are new a nd have not
appeared in the literature previously. Their closest cousin is a set of the so-called
coupled vortex equations studied e.g. in [ 9, 10 ], where both E andL are bundles
over D. In other words, our equations (7.21) can be viewed as analogs of t he coupled
vortex equations where one of the bundles is extended over M4. For instance, for a
(2, 2p + 1) torus knot T 2,2p+1 one takes E to be a unitary bundle of rank p + 1.
Then, as before, to get the “bottom row” of the unreduced Sm-colored HOM-
FLY homology we need to consider the equivariant character of M0,m(K) with
instanton number k = 0 and vortex number m. In situations where Mk,m(K)
can be identiﬁed with the moduli space of solutions to (7.21) this boils d own
10For instance, it was conjectured [ 19] that (2 ,2p + 1) torus knots correspond to wild rami-
ﬁcation of order p.
QUADRUPLY-GRADED COLORED HOMOLOGY OF KNOTS 67
to studying non-abelian vortex equations on D. Thus, for 2 p + 1 torus knots
we end up with U (p + 1) vortex equations, so that the equivariant character of
M0,m(T 2,2p+1)∼
=V U(p+1)
m essentially consists of p + 1 copies of the abelian vortex
character that we discussed earlier, cf. (7.7).
Our prediction is that the equivariant character of the m-vortex moduli space
V U(p+1)
m is the “bottom row” of the Sm-colored HOMFLY homology of the (2 , 2p+1)
torus knot, i.e.
Ch q,t(V U(p+1)
m ) = q−pm
(q; q)m
∑
0≤kp≤...≤k2≤k1≤m
[ m
k1
][ k1
k2
]
···
[ kp−1
kp
]
×
× q(2m+1)(k1+k2+...+kp)−∑ p
i=1 ki−1ki t2(k1+k2+...+kp),
with the convention k0 := m. For example, when m = 2 and p = 1, i.e. for the
(2, 3) torus knot (= trefoil knot 3 1) colored by λ =
we have
(7.22) Ch q,t(V U(2)
2 ) = q−2 1 + q3t2 + q4t2 + q6t4
(1− q)(1− q2)
which can be veriﬁed using equivariant U (2) action onV U(2)
2 , see e.g. [19] and [ 81].
It would be interesting to understand better the relation between vortex moduli
spaces and the combinatorics of the Bialynicki-Birula cell decomposit ion discussed
in Section 7.1 that also determines the bottom row of the colored HOM FLY homol-
ogy. Thus, in the above example (7.22) of the S2-colored trefoil, the corresponding
moduli space of two U (2) vorticesV U(2)
2 has been studied in the literature [ 47, 4, 5 ]
and is known to have two strata, which correspond to separated v ortices and co-
incident vortices. The ﬁrst stratum — of complex dimension 4 — is simply the
product of two single-vortex moduli spaces V U(2)
1 , modulo the permutation of the
two vortices,
(7.23) U1(V U(2)
2 ) ∼
= C× C× CP1× CP1
Z2
with the “diagonal” removed. The second stratum — of complex dimen sion 3 — is
known to be the space of Hecke modiﬁcations (times the center of m ass position),
(7.24) U2(V U(2)
2 ) ∼
= C× WCP2
(1,1,2) .
See [ 42] for color graphics illustrating the bottom row of the S2-colored HOMFLY
homology and the role of WCP2
(1,1,2) in its construction. In this, and more general
examples, it would be interesting to match the geometry of these st rata with the
Bialynicki-Birula cell decomposition discussed in Section 7.1.
Another direction for future work, already mentioned in Section 6.1 , is the
relation between theory Tvortex(K) and the surface operator theory considered in
[27, 28 ]. Indeed, here, in Section 6.1, and in [ 27, 28 ] the Poincar´ e polynomial
of the colored HOMFLY homology (a.k.a. the superpolynomial) is realize d as a
certain index (or, character) of a two-dimensional N = 2 theory that describes
the physics on D in the brane construction (2.2). Yet, the key diﬀerence is that
here and in Section 6.1 there is a diﬀerent N = 2 theory for each choice of “color”
λ; the index of such theories determines colored superpolynomials an d a priori all
such theories are unrelated. In [ 27, 28 ], on the other hand, a single N = 2 theory
68 EUGENE GORSKY, SERGEI GUKOV, AND MARKO STO ˇSI ´C
TK (that depends only on the knot K) determines the entire tower of Sm-colored
homological invariants, via specializations of its supersymmetric inde x:
(7.25) P
Sm
K (a, q, t) = ITK (x = qm; a, q, t) .
Moreover, recursion relations found in [ 27, 68, 28 ], which have a natural mean-
ing11 in theN = 2 theory TK, relate equivariant characters Ch q,t(M0,m(K)) with
diﬀerent values of the “vortex number” m = 1
2π
∫
D F . Similarly, from the vantage
point of Section 6.1, the recursion relations of [ 27, 68, 28 ] relate B-models with
target manifolds of diﬀerent (super-)dimension in a way reminiscent of the notions
of “endoscopy” and “transfer” in the geometric Langlands corre spondence [ 24].
Thus, in the case of the trefoil knot we have:
P Sm+2
bottom− (q−1− t2qm + (1 + q)q2mt2)P Sm+1
bottom(7.26)
+t4q3m−1(qm− 1)P Sm
bottom = 0
