---
doc_id: arxiv-0707.3910v1
doc_title: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS"
section_id: sec-006-7-examples
section_title: "Examples"
section_number: 7
pages: 11-17
source_pdf: 0707.3910v1.pdf
source_sha256: ad31f3cba16c4ea4
doc_brief: "LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS — We present a rational version of the classical Landen transfor- mation for elliptic integrals."
---
In this section we present a variety of closed-form evaluations of integrals of ra-
tional functions.
Example 1. The integral
Z ∞
0
z2
(z4 + 4z2 + 1)9 dz
=
23698523 π
12230590464
√
6
12
GEORGE BOROS AND VICTOR H. MOLL
is computed by Mathematica 3.0 using (3.2) in .01 seconds. The direct calculation
took 12.27 seconds and 6.4 extra seconds to simplify the answer.
Example 2. The integral of any even rational function with denominator a power
of an even quartic polynomial can be computed directly by using Corollary 3.2. For
example:
Z ∞
0
z6 dz
(2z4 + 2z2 + 3)11
=
11π(14229567 + 4937288
√
6)
440301256704 (1 +
√
6 )21/2 .
Example 3. The case n = 0 in (3.2) deserves special attention:
N0,4(a; m)
=
π
2m+3/2(a + 1)m+1/2 Pm(a)
(7.1)
where
Pm(a)
=
2−2m
m
X
k=0
2k
2m −2k
m −k
m + k
m

(a + 1)k.
(7.2)
The polynomial Pm(a) has been studied in [1] and [2].
Example 4. The case n = m in (3.2) yields
Nm,4(a; m) =
Z ∞
0
z2m dz
(z4 + 2az2 + 1)m+1 =
π
23m+3/2(1 + a)m+1/2 ×
2m
m

.
The change of variable z →√z converts this integral to
Nm,4(a; m)
=
1
2
Z ∞
0
zm−1/2 dz
(z2 + 2az + 1)m+1 ,
which is [8] 3.257.9.
Example 5. A symmetric function of degree 6. The integral
I =
Z ∞
0
x8
(x6 + 4x4 + 4x2 + 1)5 dx =
Z ∞
0
x8
[(x2 + 1)(x4 + 3x2 + 1)]5 dx
can be computed by decomposing the integrand into partial fractions as
−
1
(x2 + 1)5 −
1
(x2 + 1)4 −
6
(x2 + 1)3 −
11
(x2 + 1)2 −
31
(x2 + 1)
+
1
(x4 + 3x2 + 1)5 +
2x2
(x4 + 3x2 + 1)5 −
4
(x4 + 3x2 + 1)4 −
3x2
(x4 + 3x2 + 1)4 +
12
(x4 + 3x2 + 1)3 +
6x2
(x4 + 3x2 + 1)3 −
32
(x4 + 3x2 + 1)2 −
14x2
(x4 + 3x2 + 1)2
+
73
(x4 + 3x2 + 1) +
31x2
(x4 + 3x2 + 1).
Each of these terms is now computable yielding
I
=
1407326
√
5 −3146875
160000
× π.
LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS 13
Example 6. Non-symmetric functions of degree 6. In this case we can use the
scheme (6.1) to produce numerical approximations to the integral. For example,
the evaluation of
Z ∞
0
45z4 + 25000z2 + 1230
z6 + z4 + 3000z2 + 1
dz
is shown below:
n
an
1
an
2
bn
0
bn
1
bn
2
0
1
3000
45
25000
1230
1
.415786
14.4465
126.233
63.2884
88.3741
2
2.06562
3.17262
42.2607
156.015
83.6896
3
2.98142
3.00338
75.3541
137.717
65.1111
4
2.99999
3.
69.6338
139.925
70.2771
5
3.
3.
69.9589
139.914
69.9555
6
3.
3.
69.9572
139.914
69.9572
7
3.
3.
69.9572
139.914
69.9572
Thus L ∼69.9572 and
Z ∞
0
45x4 + 25000x2 + 1230
x6 + x4 + 3000x2 + 1 dx
∼
69.9572 × π
2
∼= 109.889.
Example 7. Symmetric functions of degree 8. These integrals can be evaluated
using Theorem 4.1. For example:
Z ∞
0
dz
(z8 + 5z6 + 14z4 + 5z2 + 1)4
=
(14325195794 + 2815367209
√
26 ) π
14623232 (9 + 2
√
26 )7/2
.
Example 8. As in the case of degree 6 we can provide numerical approximations
to nonsymmetric integrals of degree 8. The iteration (6.1) is now replaced by
an+1
1
=
an
2(an
1 + an
3) + 4an
1an
3 + 10(an
1 + an
3 ) + 8(an
2 + 2)
(an
1 + an
2 + an
3 + 2)3/2
an+1
2
=
an
1an
3 + 6(an
1 + an
3) + 2(an
2 + 10)
an
1 + an
2 + a3
3 + 2
an+1
3
=
an
1 + an
3 + 8
(an
1 + an
2 + an
3 + 2)1/2
bn+1
0
=
bn
0 + bn
1 + bn
2 + bn
3
(an
1 + an
2 + an
3 + 2)3/4
bn+1
1
=
bn
3(3an
1 + an
2 + 6) + bn
2(an
1 + 4) + bn
1(an
3 + 4) + bn
0(3an
3 + an
2 + 6)
(an
1 + an
2 + an
3 + 2)5/4
bn+1
2
=
bn
3(an
1 + 5) + bn
2 + bn
1 + bn
0(an
3 + 5)
(an
1 + an
2 + an
3 + 2)3/4
bn+1
3
=
bn
0 + bn
3
(an
1 + an
2 + an
3 + 2)1/4
with initial conditions a0
1, a0
2, a0
3, b0
0, b0
1, b0
2, b0
3. Then
U8(a1, a2, a3, b0, b1, b2, b3)
:=
Z ∞
0
b0x6 + b1x4 + b2x2 + b3
x8 + a1x6 + a2x4 + a3x2 + 1 dx
(7.3)
14
GEORGE BOROS AND VICTOR H. MOLL
is invariant under these transformations.
Note. Numerical calculations show that (an
1 , an
2, an
3) →(4, 6, 4) and that (bn
0, bn
1, bn
2, bn
3) →
(1, 3, 3, 1) L for some L depending upon the initial conditions.
Example 9. A symmetric function of degree 12. We use Theorem 2.1 to evaluate
I
:=
Z ∞
0
z18 dz
(z12 + 14z10 + 15z8 + 4z6 + 15z4 + 14z2 + 1)3
as
I
=
25π(25
√
56 −54)
301989888
.
(7.4)
Here p = 3, n = 9, and m = 2, so n > (m + 1)p −1 and we need to apply the
transformation z →1/z to reduce the value of n. Indeed, we have
I
=
Z ∞
0
z16 dz
(z12 + 14z10 + 15z8 + 4z6 + 15z4 + 14z2 + 1)3 ,
and Theorem 2.1 now yields
I
=
2−17
Z ∞
0
z16 dz
131072(1 + z2)3(1 + 4z2 + z4)3 .
The new integrand is expanded in partial fractions in the variable t = z2 to produce
(7.4).
Example 10. We use Theorem 2.1 to evaluate
I
:=
Z ∞
0
z10 dz
Q2(z)
where
Q(z)
=
z20 + 6z18 + 93z16 −24z14 + 162z12 + 548z10 + 162z8 −24z6 + 93z4 + 6z2 + 1.
The factorization
Q(z)
=
(1 + z2)2T (z)T (−z)
with
T (z)
=
z8 −2z7 + 4z6 + 14z5 + 6z4 −14z3 + 4z2 + 2z + 1
leads to a partial fraction expansion containing the term
72 −501z + 1994z2 −2617z3 + 1228z4 −43z5 + 34z6 −55z7
8388608(1 −2z + 4z2 + 14z3 + 6z4 −14z5 + 4z6 + 2z7 + z8)2 ,
which we were unable to integrate; furthemore, the roots of T (z) = 0 cannot be
evaluated by radicals. The procedure described in Theorem 2.1, however, shows
that
I
=
Z ∞
0
z10(4 + z2)(z6 + 36z4 + 96z2 + 64) dz
524288(z2 + 1)2 (z8 + 3z6 + 8z4 + 3z2 + 1)2 ,
LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS 15
the integrand of which can be expanded to yield
I
=
−
9
8388608
Z ∞
0
dz
(z2 + 1)2 −
75
8388608
Z ∞
0
dz
z2 + 1
+
Z ∞
0
1921z6 + 10815z4 + 4111z2 + 1462
2097152 (z8 + 3z6 + 8z4 + 3z2 + 1)2 dz
+
Z ∞
0
91z6 + 719z4 + 1259z2 −5764
8388608(z8 + 3z6 + 8z4 + 3z2 + 1) dz.
Every piece is now computable, with the ﬁnal result
I = (6480 −509
√
15) π
24159191040
.
Example 11. The symmetric functions of degree 16 have denominator
D4(d1, d2, d3, d4; z)
=
z16 + d4z14 + d3z12 + d2z10 + 2d1z8 + d2z6 + d3z4 + d4z2 + 1,
the integral of which is computed in terms of
E4(d1, d2, d3, d4; z)
=
(1 + d1 + d2 + d3 + d4)z8 + 2(16 + d2 + 4d3 + 9d4)z6
+
8(20 + d3 + 6d4)z4 + 32(8 + d4)z2 + 128.
This new integral is symmetric provided

d1
d2

=

15
112

+

3
−4

d3 +

−8
7

d4.
(7.5)
Introduce the new parameters
ej = dj −

8
5 −j

for 2 ≤j ≤4 and e1 = d1 −1
2
8
4

.
Then (7.5) yields

e1
e2

=

3
−4

e3 +

−8
7

e4.
(7.6)
Thus, if the original denominator has the form
D4(z)
=
(z16 + 1) + d4(z14 + z2) + d3(z12 + z4) + (112 −4d3 + 7d4)(z10 + z6)
+2(15 + 3d3 −8d4)z8,
the integral
Z ∞
0
P(z)
( D4(z) )m+1 dz
is reduced to an integral with symmetric denominator of degree 8 and these are
computable. We can thus evaluate a 2-parameter family of symmetric integrals of
degree 16.
For example, take d3 = d4 = 1 to obtain
R1(z)
=
z4
(z16 + z14 + z12 + 115z10 + 20z8 + 115z6 + z4 + z2 + 1)2 .
(7.7)
The main theorem yields
R2(z)
=
1024z4 + 2304z6 + 1792z8 + 560z10 + 60z12 + z14
27(16z8 + 36z6 + 27z4 + 36z2 + 16)2
(7.8)
16
GEORGE BOROS AND VICTOR H. MOLL
so that
Z ∞
0
R1(z) dz
=
Z ∞
0
R2(z) dz.
Letting f[n] := Nn,8[1, n, 27/32, 9/4] we obtain
Z ∞
0
R1(z) dz
=
2−15 (f[0] + 60f[1] + 1584f[2] + 4096f[3])
and conclude that
Z ∞
0
z4 dz
(z16 + z14 + z12 + 115z10 + 20z8 + 115z6 + z4 + z2 + 1)2 =
=
(149288517 + 12947003
√
131)π
1124663296
p
54925 + 4798
√
131
.
Example 12. We classify the symmetric denominators of degree 32 that yield
computable integrals. These functions depend on 8 parameters
D8(d1, · · · , d8; z)
=
8
X
k=0
d9−k(z2k + z2(16−k))
(7.9)
and the main theorem expresses the integral in terms of E8. The conditions for E8
to be symmetric yield
d1
=
−3441 + 35d5 + 64d6 −312d7 −3264d8
d2
=
34720 −56d5 −110d6 + 560d7 + 4565d8
d3
=
−3472 + 28d5 + 64d6 −329d7 −2240d8
d4
=
4960 −8d5 −19d6 + 80d7 + 938d8
and the symmetric E8 is
E8(d5, d6, d7, d8; z) = 32768(1 + z16) + (131072 + 8192d8)(z2 + z14)+
(212992 + 2048d7 + 28672d8)(z4 + z12) + (180224 + 512d6 + 6144d7 + 39424d8)(z6 + z10)+
+ (84480 + 128d5 + 1280d6 + 6912d7 + 26880d8)z8.
The symmetry of E8 now determines d5, d6 in terms of d7, d8 and we obtain


d1
d2
d3
d4
d5
d6


=
−31


63475
−100800
47936
−13664
2220
−224


+


9166
−14392
6895
−1964
322
−28


d7 +


54640
−86645
41664
−11471
2000
−189


d8.
(7.10)
The function (z2 + 1)16 is a symmetric polynomial of degree 32 and yields a par-
ticular solution to (7.10).
As before let
ej = dj −
 16
9 −j

for 2 ≤j ≤8 and e1 = d1 −1
2
16
8

.
LANDEN TRANSFORMATIONS AND THE INTEGRATION OF RATIONAL FUNCTIONS 17
Then


e1
e2
e3
e4
e5
e6


=


9166
−14392
6895
−1964
322
−28


e7 +


54640
−86645
41664
−11471
2000
−189


e8
(7.11)
and as in the case of degree 16 we can compute a 2-parameter family of symmetric
integrals of degree 32.
