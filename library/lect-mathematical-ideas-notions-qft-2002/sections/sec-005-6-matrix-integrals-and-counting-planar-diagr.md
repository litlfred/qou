---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: sec-005-6-matrix-integrals-and-counting-planar-diagr
section_title: "Matrix integrals and counting planar diagrams"
section_number: "6"
pages: 38-41
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
toc_source: inferred
text_source: text rebuilt from glyph codes of the ps2pdf'd dvips PostScript (bitmap Type-3 fonts carry raw TeX OT1 codes; ps2pdf reports 'c' as U+0020, so a char-level rebuild maps it back and expands ligatures); prose good, display math flattened
doc_brief: "Mathematical ideas and notions of quantum field theory — 1. Generalities on quantum field theory 1.1. Classical mechanics. In classical mechanics, we study the motion of a par- ticle."
---
6. Matrix integrals and counting planar diagrams
6.1. The number of planar gluings. Let us return to the setting of x4. Thus,
P
2 j
we have a potential U(x) = x =2− j0 gjx =j (with gj being formal parameters),
and consider the matrix integral
Z
−N=2 −TrU(A)
ZN(~) = ~ e dA:
hN
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 39
^
Let ZN (~) = ZN (~=N). We have seen that
^
ln ZN
lim = W1;
N!1 N2
where W1 is given by summation over planar fat graphs:
e
X Y X b(−
ni ~ )
W1 = gi
e
jAut(−)j
n i −e2Gec(n)[0]
Q
ni
In particular, the coeÆcient of g is (up to a power of ~) the number of (ori-
i
entation preserving) gluings of a fat graph of genus zero out of a collection of fat
Q
ni
flowers containing ni i-valent flowers for each i, divided by i ni!.
On the other hand, one can compute W1 explicitly as a function of gi by reducing
the matrix integral to an integral over eigenvalues, and then using a fundamental
fact from the theory of random matrices: the existence of an asymptotic distribu-
tion of eigenvalues as N ! 1. This approach allows one to obtain simple closed
formulas for the numbers of planar gluings, which are quite nontrivial and for which
direct combinatorial proofs were discovered only very recently.
To illustrate this method, we will restrict ourselves to the case of the potential
2 4
U(x) = x =2 + gx (so g4 = −4g and other gi = 0), and set ~ = 1. Then W1 =
P
n
n1 cn(−g) =n!, where cn is a number of connected planar gluings of a set of n
4-valent flowers. In other words, cn is the number of ways (up to isotopy) to connect
n “crosses” in the 2-sphere so that all crosses are connected with each other, and
the connecting lines do not intersect.
Exercise. Check by drawing pictures that c1 = 2, c2 = 36.
Theorem 6.1. (Brezin, Itzykson, Parisi, Zuber, 1978). One has
n
cn = (12) (2n − 1)!=(n + 2)!
6.2. Proof of Theorem 6.1. Let us prosent the proof of this theorem (with some
omissions). We will assume that g is a positive real number, and compute the
function W1(g) explicitly. We follow the paper of Brezin, Itzykson, Parisi, and
Zuber “Planar diagrams”, Comm. Math. Phys. 59, p.35-51, 1978.
The relevant matrix integral has the form
Z
2 4
^ −NTr(A =2+gA )
ZN = e dA:
hN
Passing to eigenvalues, we get
JN (g)
^
ZN = ;
JN(0)
where
Z
P 2 P 4 Y
JN (g) = e−N( i =2+g i ) (i − j)2d:
RN
i<j
−2
Thus, W1(g) = E(g) − E(0), where E(g) = limN!1 N ln JN(g).
Proposition 6.2. (steepest descent principle) E(g) equals the maximal value of
the logarithm of the integrand.
40 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY
The proposition says, essentially, that the integrand has a suÆciently sharp max-
imum, so that the leading behavior of the integral can be computed by the steepest
descent formula. We note that we cannot apply the steepest descent formula with-
out explanations, since the integral is over a space whose dimension grows as the
perturbation parameter 1=N goes to 0. In other words, it is necessary to do some
estimates which we will omit. We will just mention that for g = 0, this result can be
derived from the explicit evaluation of the integral using Hermite polynomials (see
x4). For the general case, we refer the reader to the book of P.Deift “Orthogonal
polynomials and random matrices: a Riemann-Hilbert approach”.
P 2 P 4 Q
The integrand K(1; :::; N) = e−N( i =2+g i ) i<j(i − j)2 has a unique
maximum, because it is logarithmically concave (check it!). The maximum of the
integrand is found by equating the partial derivatives to zero. This yields
X
1 1
3
(16) = N( i + 2gi ):
i − j 2
j6=i
Let 1 < 2 < ::: < N be the unique (up to permutations) solution of this system
of equations.
P
1
Proposition 6.3. The normalized counting measures N Æ(x−i) converge weakly
to a measure (x) = f(x; g)dx, where f(x; g) is a continuous function, supported
on a finite interval [−2a; 2a], and differentiable on this interval.
For the proof we again refer the reader to the book of P.Deift (p.132 and later).
We note that for g = 0, by Wigner's semicircular law, a = 1 and f(x; 0) =
p p
1 2 1 2
4 − x ; so f(x; g) = 4 − x + O(g).
2 2
Now our job will be to find the function f(x; g). Passing to the limit in equation
16 (which requires justification that we will omit), we get
Z
2a
1 1
3
f(x; g)dx = y + 2gy ; jyj ≤ 2a
−2a y − x 2
where the integral is understood in the sense of principal value.
This is a linear integral equation on f(x; g), which can be solved in a standard
R
2a 1
way. Namely, one considers the analytic function F (y) = f(x; g)dx for y
−2a y−x
in the complex plane but outside of the interval [−2a; 2a]. For y 2 [−2a; 2a], let
F+(y), F−(y) denote the limits of F (y) from above and below. Then by the Plemelj
formula, the integral equation implies
1 1
3
(F+(y) + F−(y)) = y + 2gy :
2 2
1 3
On the other hand, F+(y) = F−(y). Hence, ReF+(y) = Re(F−(y)) = 2 y + 2gy .
−1
Now set y = a(z + z ). Then, as y runs through the exterior of [−2a; 2a],
z runs through the exterior of the unit circle. So the function G(z) := F (y) is
analytic on the outside of the unit circle, with decay at infinity, and ReG(z) =
1 −1 3 −1 3
a(z + z ) + 2ga (z + z ) , jzj = 1. This implies that G(z) is twice the sum of
2
all negative degree terms of this Laurent polynomial. In other words, we have
3 −3 3 −1
G(z) = 4ga z + (a + 12ga )z :
This yields
p
1 1
3 2 2 2 2
F (y) = y + 2gy − ( + 4ga + 2gy ) y − 4a :
2 2
MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY 41
Now f(y; g) is found as the jump of F :
p
1 1
2 2 2 2
f(y; g) = ( + 4ga + 2gy ) 4a − y :
 2
R
It remains to find a in terms of g. We have yF (y) ! 1, y ! 1 (as f(x; g)dx =
3
1), hence zG(z) ! 1=a, z ! 1. This yields 1=a = a + 12ga , or
4 2
12ga + a − 1 = 0:
This allows one to determine a uniquely:

1=2
(1 + 48g) − 1
1=2
a = ) :
24g
Now let us calculate E(g). It follows from the above that
Z Z Z
2a 2a 2a
1
2 4
E(g) = ln jx − yjf(x; g)f(y; g)dxdy − ( x + gx )f(x; g)dx:
−2a −2a −2a 2
On the other hand, let us integrate the integral equation defining f(x; g) with
respect to y (from 0 to u). Then we get
Z 2a
1
2 4
2 (ln jx − uj − ln jxj)f(x; g)dx = u + gu :
−2a 2
Substituting this into the expression for E(g), we get
Z
2a
1 1
2 4
E(g) = (ln juj − u − gu )f(u; g)du
−2a 4 2
Since f(u; g) is known, this integral can be computed. In fact, can be expressed via
elementary functions, and after calculations we get
1
2 2
E(g) − E(0) = ln a − (a − 1)(9 − a ):
24
Substituting here the expression for a, after a calculation one finally gets:
1
X
(2k − 1)!
k
E(g) − E(0) = (−12g) :
k!(k − 2)!
k=1
This implies the required formula for cn.
