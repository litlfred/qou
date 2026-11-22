---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-045-further-computations-for-asymptotics
section_title: "Further computations for asymptotics"
section_number: null
pages: 256-263
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
We end this section with additional computational results that will be necessary
for our asymptotic arguments in later chapters.
8.4.1 Local Hessian and quadratic degeneracy
Let S be a stratum of codimension s < d, locally deﬁned near some w ∈S
by the vanishing of functions H1, . . . , Hs, and assume that there exist distinct
coordinates {σ1, . . . , σs} such that the Jacobian matrix

H[σ1]
1
(w)
· · ·
H[σs]
1
(w)
...
...
...
H[σ1]
s
(w)
· · ·
H[σs]
s
(w)

is nonsingular, where H[b]
a
denotes the partial derivative of Ha with respect to
zb. If π = {π1, . . . , πd−s} = {1, . . . , d} \ {σ1, . . . , σs} denotes the remaining co-
ordinates, then the implicit function theorem implies the existence of analytic
functions g j(zπ1, . . . , zπd−s) for j < π and a suﬃciently small neighborhood O of
w in Cd such that for all z ∈O, z lies in S if and only if zj = gj(zπ1, . . . , zπd−s)
for all j < π.
To derive asymptotics, we will ultimately apply the saddle point analyses of
Chapters 4 and 5 to phase functions of the form
φ(θ) =
X
j<π
r j log

gj

wπ1eiθ1, . . . , wπd−seiθd−s
wj
+ i
d−s
X
j=1
rπjθj,
(8.6)
obtained by substituting z j = g j(zπ1, . . . , zπd−s) for j < π into log(zr/wr) and
then switching to exponential coordinates near w. In order to use saddle point
techniques in later chapters, we verify the following.
Lemma 8.21. If w is a critical point of S then φ(0) = 0 and (∇φ)(0) = 0.
Proof
By construction gj(wπ1, . . . , wπd−s) = w j for all j < π, so φ(0) =
P
j<π rj log(w j/wj) = 0.
8.4 Further computations for asymptotics
239
By permuting variables if necessary we may assume, without loss of gen-
erality, that (σ1, . . . , σs) = (1, . . . , s) and, to simplify notation, we write ˆz =
(zs+1, . . . , zd). Since, by construction,
H1(g1(ˆz), . . . , gs(ˆz), ˆz) = · · · = Hs(g1(ˆz), . . . , gs(ˆz), ˆz) = 0
for all ˆz suﬃciently close to (ws+1, . . . , wd), we can diﬀerentiate these equations
with respect to zs+1 and use the implicit function theorem to get the linear
system

H[1]
1 (w)
· · ·
H[s]
1 (w)
...
...
...
H[1]
s (w)
· · ·
H[s]
s (w)

|                           {z                           }
M

g[s+1]
1
( ˆw)
...
g[s+1]
s
( ˆw)

= −

H[s+1]
1
(w)
...
H[s+1]
s
(w)

|        {z        }
b
.
Because M is nonsingular, if we let Mk denote M after replacing its kth column
with the vector b then Cramer’s rule implies
g[s+1]
k
( ˆw) = −det(Mk)
det(M)
for all 1 ≤k ≤s. If w is a critical point on S then the matrix

(∇log H1)(w)
...
(∇log Hs)(w)
r1
· · ·
rd

has rank s, so the determinant of the (s + 1) × (s + 1) sub-matrix

H[1]
1 (w)
· · ·
H[s]
1 (w)
H[s+1]
1
(w)
...
...
...
...
H[1]
s (w)
· · ·
H[s]
s (w)
H[s+1]
s
(w)
r1
w1
· · ·
rs
ws
rs+1
ws+1

vanishes. A cofactor expansion of the determinant along the bottom row gives,
after carefully accounting for signs, that
0 = rs+1
ws+1
det(M) −
s
X
j=1
r j
wj
det(Mk),
so
s
X
j=1
r j
wj
g[s+1]
j
( ˆw) = −rs+1
ws+1
240
Eﬀective computations and ACSV
and thus
 ∂φ
∂θs+1
!
(0) = i
s
X
j=1
r j
wj
g[s+1]
j
( ˆw)ws+1 + irs+1 = 0.
Repeating this argument with indices s + 2, . . . , d shows that the gradient of φ
vanishes at θ = 0.
□
Recall from Deﬁnitions 7.11 and 7.34 that a nondegenerate critical point w
is a critical point where the Hessian of φ at the origin is nonsingular; integrals
near nondegenerate critical points are those to which we can apply the tech-
niques of Chapter 5. Although the Hessian matrix can always be computed in
terms of derivatives of the g j, which themselves can be determined through
implicit diﬀerentiation or the determinant expressions derived in our proof of
Lemma 8.21, in the smooth case things are simple enough to derive an explicit
expression for the Hessian matrix itself.
Lemma 8.22. Suppose w is a critical point where Hzd(w) , 0 and let
φ(θ) = log

g

w◦eiθ
wd
+ i(r◦· θ)
rd
in the variables θ = (θ1, . . . , θd−1), where

w◦eiθ
=

w1eiθ1, . . . , wd−1eiθd−1
.
Then the (d −1) × (d −1) Hessian matrix of φ at θ = 0 has (i, j)th entry
Hi, j =

ViVj + Ui,j −VjUi,d −ViU j,d + ViVjUd,d
: i , j
Vi + V2
i + Ui,i −2ViUi,d + V2
i Ud,d
: i = j
,
(8.7)
where
Ui,j =
wiwjHzizj(w)
wdHzd(w)
and
Vi = ri
rd
(8.8)
for all 1 ≤j ≤d. If, more generally, Hzk(w) , 0 then the same formula holds
when d is replaced by k.
Exercise 8.4. Use the chain rule to prove Lemma 8.22.
8.4.2 Numeric analytic continuation of D-ﬁnite functions
Recall from Chapter 2 that a D-ﬁnite equation is a linear diﬀerential equation
with polynomial coeﬃcients, and a D-ﬁnite function is one that satisﬁes a D-
ﬁnite equation. Because the diagonal of any multivariate rational function is
D-ﬁnite, we can use D-ﬁnite equations as data structures to manipulate and
8.4 Further computations for asymptotics
241
compute with diagonals. Given a multivariate rational function with a con-
vergent power series near the origin, an annihilating D-ﬁnite equation for the
diagonal in any ﬁxed integer direction r ∈Zd can be computed using the
methods of creative telescoping. Brieﬂy, one represents the diagonal D(z) as
a parameterized complex integral D(z) =
R
γ I(z, x)dx over a closed contour
γ, with the integrand I constructed from the rational function F and direc-
tion r. If L is a linear diﬀerential operator in z with polynomial coeﬃcients
such that L(I) = ∂x1A1(z, x) + · · · + ∂xdAd(z, x) for suitable rational functions
A1, . . . , Ad then, under mild conditions, the fact that γ is closed implies that
D(z) satisﬁes the D-ﬁnite equation L(D) = 0. Methods to compute such dif-
ferential operators have been the source of immense study in the computer
algebra community, with currently optimal techniques relying on a reduction
framework known as the Griﬃths–Dwork method [BLS13; Lai16]. An imple-
mentation of this method in the MAGMA computer algebra system was cre-
ated by Lairez [Lai16].
Consider a D-ﬁnite equation
cr(z) f (r)(z) + · · · + c1(z) f ′(z) + c0(z) f(z) = 0,
(8.9)
which admits a generating function F of interest as a solution f(z) = F(z), and
assume that F is analytic at the origin. The points ρ ∈C where the leading co-
eﬃcient cr(z) vanishes are called singular points of the ODE (8.9), and nonsin-
gular points are called ordinary points of the ODE. Because D-ﬁnite equations
are linear, the solutions to (8.9) form an r-dimensional complex vector space,
and the Cauchy existence theorem for ordinary diﬀerential equations [Poo60,
Chapter 1.2] implies that in any suﬃciently small neighborhood of an ordinary
point there exists a basis of analytic solutions to (8.9).
A collection of deep results due to Andr´e, the Chudnovsky brothers, and
Katz jointly imply that for a D-ﬁnite function with integer coeﬃcients and
at most exponential growth (i.e., the types of generating functions we con-
sider), a minimal order deﬁning equation admits only regular singular points;
see [And89, Section VI]. Skipping over the deﬁnition of a regular singular
point, this is important because if ρ is a regular singular point then in any suf-
ﬁciently small slit disk centered at ρ (a disk with a ray from its center to its
boundary removed to account for branch cuts) there is a basis of solutions of
the form
(z −ρ)ν
κ
X
k=0
φk(z) logk
 
1
1 −z/ρ
!
,
where ν is algebraic and each φk is analytic at ρ; see [Poo60, Chapter 5] for
details.
242
Eﬀective computations and ACSV
To determine asymptotic behavior of the power series coeﬃcients of F we
need to represent F in terms of the local basis expansions near the singular
points of (8.9) (which can contain the singularities of F, the singularities of
other solutions to the diﬀerential equation, and spurious points). In practice,
this is accomplished using the series expansion of F at the origin to express it
in terms of a basis near the origin, then approximating change of basis matrices
from analytically continuing series centered at the origin to series centered at
the singular points of (8.9). Using ideas going back to Cauchy’s method of
majorants, implemented by Mezzarobba [Mez16] in the Sage ore algebra
package, it is possible to rigorously compute numerical approximations of the
entries of the change of basis matrices to any desired accuracy.
Ultimately, one can use these techniques to compute expansions of F near
the singularities of (8.9) with rigorously approximated coeﬃcients. This can
often be used to identify the dominant singularities of F, and compute asymp-
totics of its power series coeﬃcients up to constants that are rigorously approx-
imated. Unfortunately, it is an open problem to identify when approximated
coeﬃcients that are zero to many decimal places are identically zero. This
connection problem means that it not always possible to identify the dominant
asymptotics of a D-ﬁnite function directly from a D-ﬁnite equation it satisﬁes
(although using current implementations one can get the relevant constants to
thousands of decimal places, so even if a rigorous proof can’t be found very
strong heuristic evidence is always possible).
Example 8.23. Let an denote the number of lattice paths with the set of allow-
able steps {(−1, −1), (1, −1), (−1, 1), (1, 1)} that start at the origin and stay in
the nonnegative quadrant N2. The kernel method [Mel21, Chapter 4] implies
that the generating function A(t) of (an) satisﬁes the D-ﬁnite equation
0 = t2(4t + 1)(1 −4t)2A′′′(t) + t(1 −4t)(112t2 −5)A′′(t)
+ 4(8t −1)(20t2 −3t −1)A′(t) + (128t2 −48t −4)A(t).
The dominant singularities of A occur at t = ±1/4, and the Sage package of
Mezzarobba computes expansions
A(t) =
 h
−0.636 ± 3 · 10−3i
+
h
±4 · 10−12i
i

log(t −1/4)
+
 h
2.54 ± 7 · 10−3i
+
h
±1.56 · 10−11i
i

(t −1/4) log(t −1/4) + · · ·
near t = 1/4, where the notation [a ± b] denotes a constant in the interval
[a −b, a + b], and
A(t) =
h
1 ± 7 · 10−18i
+
h
1.273 ± 3 · 10−3i
(t −1/4) log(t −1/4) + · · ·
8.4 Further computations for asymptotics
243
near t = −1/4. Translating these singular expansions into asymptotic behavior
implies
an = 4n
n
h
0.636 ± 3 · 10−3i
+ O

n−1
.
The constants here are given to three decimal places for readability, but can be
computed to hundreds of decimal places in under a second on modern comput-
ers.
◁
Example 8.24. Let bn denote the number of lattice paths with the set of allow-
able steps {(0, 1), (−1, −1), (0, −1), (1, −1)} that start at the origin and stay in
the nonnegative quadrant N2. The kernel method now implies that the generat-
ing function B(t) of (bn) satisﬁes a D-ﬁnite equation of order 3 whose leading
coeﬃcient has a root at t = 1/4, and no non-zero roots closer to the origin,
suggesting that this might be a dominant singularity of B(t). The Sage package
of Mezzarobba can be used to compute an expansion
B(t) =
h
±10−1000i
(t −1/4)−1/2 + · · ·
near t = 1/4, whose leading coeﬃcient is zero to 1000 decimal places. In fact,
although t = 1/4 is a singular point of this ODE satisﬁed by B, it is not a
singularity of B. The dominant singularities of B(t) occur at t = ±
√
3/6 and
bn ∼cn(2
√
3)nn−2 where cn takes one value when n is even, and another when
n is odd, but this cannot be proven without using additional information beyond
properties of this ODE.
◁
Asymptotics for many lattice path problems, including those in Examples 8.23
and 8.24, can be derived using ACSV [Mel21, Chapters 6 and 10].
Notes
Modern methods for solving polynomial systems can be traced back at least to
work of Newton in the seventeenth century. After the work of Newton, and later
work of Cramer and B´ezout bounding the number of solutions to multivariate
polynomial systems, the nineteenth century work of Sylvester illustrated the
power of the resultant in eﬀectively solving polynomial systems. Further work
by Macaulay and his contemporaries developed a mature theory of multivariate
resultants for use beyond bivariate systems; see [GKZ08] for a modern and far-
reaching generalization of these techniques. Gr¨obner bases were introduced
by Buchberger [Buc65] in his 1965 PhD thesis, and form the backbone of
much modern work in computer algebra. The theory of eﬀective methods for
algebraic geometry is eloquently presented in the splendid volumes [CLO07;
244
Eﬀective computations and ACSV
CLO05] and the monograph [Stu02], and further historical details can be found
in the survey [Cox20].
The theory of D-ﬁnite functions has a long history, going back at least to
Abel. Major contributions were made by Fuchs, Frobenius, and G. D. Birkhoﬀ,
among others. Their use in combinatorial applications was pioneered by Zeil-
berger. The book [Mel21] gives further details on computational approaches to
D-ﬁnite generating functions.
We have tried to present this book in such a way as to ensure a long shelf-
life. In the present chapter it was useful for concreteness to mention speciﬁc
implementations, even though these implementations may no longer be the
state of the art in the future. Nevertheless, the speciﬁc packages we mention,
in addition to the entire Sage computer algebra system, have open source code
and practice modern version control and archiving. We thus expect they will
prove useful for a long time to come.
Additional exercises
Exercise 8.5. Let R be an integral domain. The resultant of two polynomials
P(x) = p0 + · · · + prxr and Q(x) = q0 + · · · + qsxs in R[x] with prqs , 0 is a
polynomial resx(p, q) in p0, . . . , pr, q0, . . . , qr that vanishes if and only if P and
Q share a root in the algebraic closure of R. Let α and β be algebraic numbers
with P(α) = 0 and Q(β) = 0 for P, Q ∈Z[x]. Find annihilating polynomials in
Z[x] for the sum α + β, the product αβ, and, when β , 0, the quotient α/β in
terms of the resultants of explicit polynomials depending on P and Q.
Exercise 8.6. Suppose that a set of algebraic equations has a single solution
z = (z1, . . . , zd). Prove that z is a rational point by showing that each co-
ordinate z j is the solution to a univariate algebraic equation having only one
solution. Similarly, prove that if a zero-dimensional variety consists of two
points {z, w} then either it is reducible and the two points are rational, or it is
irreducible and both are quadratic and algebraically conjugate.
