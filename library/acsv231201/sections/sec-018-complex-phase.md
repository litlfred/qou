---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-018-complex-phase
section_title: "Complex phase"
section_number: null
pages: 115-123
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
where ˜b j is a polynomial in b𝓁,..., b j, c−1
k , ck+1,..., ck+ j−𝓁.
The existence of the expansion (4.6), with a j = ˜b j for all j, now follows
from the monomial exponent case in Lemma 4.4, and we compute the leading
terms (4.7) by ﬁnding ˜b𝓁 and ˜b𝓁+1. Inverting the expression
y = c1/k
k x
(
1 + ck+1
ck
x + O
(
x2))1/k
= c1/k
k x
(
1 + ck+1
k ck
x + O
(
x2))
(4.10)
to expand x as a series in y is a matter of plugging x = c−1/k
k y + ay2 + O(y3)
into (4.10), setting the result equal to x, and solving for a to obtain
x = y
c1/k
k
− 1
k
ck+1
ck

y
c1/k
k

2
+ O(y3)
x′(y) = 1
c1/k
k
− 2
c2/k
k
ck+1
k ck
y + O(y2). (4.11)
Composing A with x(y) gives
A(x(y)) = b𝓁
1
c𝓁/k
k
y𝓁 +
b𝓁
𝓁
c(𝓁−1)/k
k
−ck+1
kc1+2/k
k
+ b𝓁+1
1
c(𝓁+1)/k
k
 y𝓁+1 + O(y𝓁+2),
and multiplying this expansion by the expression for x′(y) in (4.11) shows that
the leading series coeﬃcients of ˜A(y) = A(x(y))x′(y) are
˜b𝓁 = b𝓁
˜b𝓁+1 = b𝓁+1− b𝓁
𝓁 + 2
k
ck+1
ck
,
giving (4.7). □
Exercise 4.6. Give an example to show that the hypotheses do not imply that
φ is CM+1-smooth.
4.2 Complex phase
Extending the results of the previous section to complex amplitudes is trivial:
by linearity of the integral, the result holds separately for Im{A} and Re{A}, and
these may be recombined to give the result for complex A. When it comes to
complex phases, we are faced with a choice. If we assumeA andφ are analytic
in a neighborhood of zero then we are entitled to move the contour, which is the
quickest justiﬁcation for extending the conclusion to complex phases and is the
98 Fourier–Laplace integrals in one variable
approach taken in this section. Later, in Section 4.3, we discuss an alternative
using only smoothness instead of analyticity.
We now prove Theorem 4.1, starting with the one-sided integral I+ before
addressing the double-sided integralI.
Step 1: evaluation of the one-sided integralI+
Letγ+ : [0,ε ]→C denote the restriction ofγ to [0,ε ] so that
I+ =
∫
γ+
A(z) exp(−λφ(z)) dz.
To evaluateI+ we employ the same change of variables y = φ(z)1/k as in the
proof of Theorem 4.6, only we need to be careful in choosing a branch of the
kth root. Formula (4.8) deﬁnes k diﬀerent functions, one for each choice of
kth root for c1/k
k . It follows from Lemma 4.5 that each of these k functions
and their inverses are analytic in a neighborhood of the origin. To discuss the
principal kth root – the analytic function from theslit planeC\R<0 to the cone
K ={z :−π/k< arg(z)<π/ k} – we write p(u1/k) = z for the unique z∈ K such
that zk = u, and let v = γ′(0). Near the origin φ(z)∼ ckzk, so the requirement
that Re{φ(γ(t))}≥ 0 forces the quantity v to be in the windmill-shaped set of
preimages of the right half-plane under ckzk, shown in Figure 4.1.
K
Figure 4.1 Arrows represent v and (d/dt)|t=0 f (γ+(t)).
Deﬁne f (x) = p(φ(x)1/k). Since the pathφ(γ+(t)) remains in the positive real
half-plane for 0 < t≤ ε, it also remains in the slit plane, and hence maps the
4.2 Complex phase 99
image of γ+ bi-analytically into the cone K. With this choice of kth root, the
change of variables (4.8) becomes
y = f (x) =ηx
(
1 +··· + cM
ck
xM−k + O
(
xM−k+1))1/k
, (4.12)
whereη = v−1 p(ckvk)1/k and the branch of the kth root of the series in paren-
theses ﬁxes 1. Thus f′(0) = η and the inverse function x(y) is deﬁned as in
the proof of Theorem 4.6, with c1/k
k = η in (4.9). Analogously to the proof of
Theorem 4.6, we then have
I+ =
∫
˜γ
˜A(y) exp(−λyk) dy, (4.13)
where ˜γ = f◦γ+ is the image ofγ+ under our change of variables.
g~ b
a
Figure 4.2 The path ˜γ in the cone K and the line segmentsα andβ.
Let p = f (γ(ε)) denote the endpoint of ˜γ with real part p′ > 0 and deﬁne
the line segmentsα = [0, p′] andβ = [p′, p] in the complex plane. As seen in
Figure 4.2, the contour ˜γ is homotopic toα +β, hence
∫
˜γ h(z) dz =
∫
α h(z) dz +∫
β h(z) dz for any analytic function h. On compact subsets of K, the real part of
yk is bounded from below by a positive constant, so there are positive constants
C andρ such that
⏐⏐⏐ ˜A(y) exp(−λyk)
⏐⏐⏐≤ Ce−ρλ
onβ (the reason we chose the principal value for our root was to ensure that β
lies inside K). We conclude that
I+ =
∫
α
˜A(y) exp(−λyk) dy + Rλ
100 Fourier–Laplace integrals in one variable
for a remainder Rλ that decays exponentially, and applying Theorem 4.6 (with
complex amplitude) to the integral overα gives the asymptotic series
I+≈
∞∑
j=𝓁
a jC(k, j)(ckλ)−(1+ j)/k
satisfying conclusion (i) of Theorem 4.1.
Step 2: evaluation of the two-sided integralI
In order to reduce the two-sided integral to the one-sided case, deﬁne the con-
tourγ− : [0,ε ]→ C byγ−(t) = γ(−t). The curve γ− is oriented from 0 to−ε
so it appears with sign reversed. In other words, I =I+−I−, where
I− :=
∫
γ−
A(z) exp(−λφ(z)) dz.
The integral forI− has nearly the same data as the integral forI+: the functions
A and φ are identical so the only di ﬀerence between the two integrals is the
contour. The contour a ﬀects the integral only via the choice of η in (4.12).
Denoting the two choices byη+ andη−, we know a fortiori thatη− =η+/ζ for
someζ withζk = 1. Denoting the respective inverse functions of f (x) in (4.12)
by g+ and g− we see that g−(y) = g+(ζy). The two changes of variables produce
amplitudes ˜A+ and ˜A− in (4.13) satisfying
˜A+(y) = A(g+(y))· g′
+(y)
and
˜A−(y) = A(g−(y))· g′
−(y)
= A(g+(ζy))·ζg′
+(ζy)
=ζ ˜A+(ζy).
The coeﬃcients of the power series for ˜A+ and ˜A− are therefore related by
[y j] ˜A−(y) = ζ j+1[y j] ˜A+(y). The asymptotic expansions of ˜A± are integrated
term by term in (4.13), which implies that the coeﬃcientsα j for the two-sided
integralI are related to the coe ﬃcients a j for the one-sided integral I+ via
α j = (1−ζ j+1)a j. Thus, part ( iii) of Theorem 4.1 is reduced to the correct
identiﬁcation ofζ. The evaluation ofζ breaks into two cases, depending on the
parity of k.
Suppose ﬁrst that k is even. Sinceφ(z)∼ ckzk, the image of the smooth curve
γ underφ moves back in the same direction at the origin, with the tangents to
the imagesφ(γ−(t)) andφ(γ+(t)) coinciding at t = 0 (see Figure 4.3). Because
4.2 Complex phase 101
K
Figure 4.3 Illustration for even k:φ(γ+) is a solid curve andφ(γ−) is dotted.
Kγ
γ
+
−
Figure 4.4 Illustration for odd k:φ(γ+) andφ(γ−) and their principal 1/k powers.
γ− reverses the orientation of the parametrization, we see thatv− = γ′
−(0) and
v+ =γ′
+(0) satisfyv− =−v+. The powersvk
− andvk
+ coincide, meaning
η− =v−1
− p(ckvk
−)1/k =−v−1
+ p(ckvk
+)1/k =−η+.
Thus, when k is even ζ takes the value−1. This leads to α j = 2a j for even j
andα j = 0 for odd j, completing the proof of the theorem for even k.
When k is odd, the images ofγ+ andγ− underφ point in opposite directions
(see Figure 4.4). Since both are in the closed right half-plane, this implies
that one points in the positive imaginary direction and the other points in the
negative imaginary direction. Thus the argument of the tangent toφ(γ+) at the
origin isσπ/2, where the sign ofσ is given by
σ = sgn Im{φ(γ′(0))} .
102 Fourier–Laplace integrals in one variable
The argument of the tangent to φ(γ−) at the origin is −σπ/2 and thus di ﬀers
from the argument ofφ(γ+) by−σπ. Mapping by the principal kth root shrinks
the diﬀerence in arguments by a factor of k, thus
p(ckvk
−)1/k = e−iπσ/k p(ckvk
+)1/k.
Again the reversal of parametrization impliesv− =−v+, whence
η− = (−1)· e−iπσ/kη+ = η+
ζ
withζ =−eiπσ/k as in the statement of the theorem. □
Applications
The following classical result is a direct corollary of our machinery.
Proposition 4.7 (Watson’s Lemma). Let A :R>0→C have asymptotic devel-
opment
A(t)≈
∞∑
m=0
bmtβm
for t near the origin, where−1 < Re{β0} < Re{β1} <··· and Re{βm}→∞ as
m→∞ . Then the Laplace transform
L(λ) =
∫ ∞
0
A(t)e−λt dt
of A has an asymptotic series
L(λ)≈
∞∑
m=0
bmΓ(βm + 1)λ−(1+βm)
asλ→∞ .
Proof As in our previous arguments, we may replace the integral in the Laplace
transform by an integral on [0,ε ] while introducing only an exponentially small
error. Writing
A(t) =
N∑
m=0
bmtβm + RN(t)
for RN = O
(
tRe{βm+1}
)
at the origin, we may integrate term by term to get the
ﬁrst N terms of the expansion, up to an exponentially small correction from
truncating the integral, then use Lemma 4.3 to see that the remainder satisﬁes
⏐⏐⏐⏐⏐
∫ ε
0
RN(t)e−λt dt
⏐⏐⏐⏐⏐ = O
(
λ− Re{βm}−1)
,
4.2 Complex phase 103
proving the proposition. □
Exercise 4.7. Let y be the positive real root of x− 3xy− y3 = 0 satisfying
y∼ x1/3 as x↓ 0. Find the ﬁrst two terms of the Puiseux series for y and use
Watson’s Lemma to compute the corresponding ﬁrst two asymptotic terms of
the Laplace transform L(λ) =
∫∞
0 y(x)e−λx dx.
As discussed in Section 3.5 of Chapter 3, Theorem 4.1 is a crucial compo-
nent of the saddle point method , which is also called the method of steepest
descent. If we consider an integral
I(λ) =
∫
γ
A(z) exp(−λφ(z)) dz
where φ′ does not vanish on γ then the idea is to deform γ to pass through
a point x where φ′ vanishes while introducing a negligible error. The phrase
steepest descent comes from the fact that the real part of φ must have a local
maximum on the contour at x, rather than a minimum or inﬂection point. Hav-
ing deformed the contour to pass through x, Theorem 4.1 is then applied to
determine asymptotics.
Example 4.8. Consider the univariate power series f (z) = (1− z)−1/2, whose
power series coe ﬃcients at the origin form the sequence an = (−1)n
(−1/2
n
)
.
Instead of using a transfer theorem from Chapter 3 to obtain the asymptotic
behavior an ∼ 1/√πn, let us apply a saddle point approach to the Cauchy
integral representation
an = 1
2πi
∫
C
z−n−1(1− z)−1/2 dz,
where C is any suﬃciently small positively oriented circle around the origin.
Since we understand meromorphic integrands the best, we make the change of
variables z = 1− y2 to obtain
an = 1
2πi
∫
E
(1− y2)−n−1y−1 (−2y) dy = i
π
∫
E
(1− y2)−n−1 dy
where, as shown in Figure 4.5, E is a positively-oriented small circle in the y-
plane around either the point +1 or the point−1 (since both of these contours
map to a small contour around 0 in the z-plane). For concreteness, let us take
E to be a small circle around +1. In the y-plane, there is a critical point for
φ(y) =− log(1− y2) at the origin. Without crossing any singularities of our
integrand, we can deform the contour E to a contour ˜E passing through the
origin in the downward direction. Changing variables with y =−it gives
an = i
π
∫
R
(1 + t2)−n−1 (−i) dt = 1
π
∫
R
1
1 + t2 exp
(
−n log(1 + t2)
)
dt,
104 Fourier–Laplace integrals in one variable
and an application of Theorem 4.1 with the expansions A(t) = 1/(1 + t2) = 1 +
··· andφ(t) = log(1 + t2) = t2 +··· implies an∼
√
2/(πnφ′′(0)) = 1/√πn. ◁
 
 
 
 
 
 
 
 
 
 
 
 




































C z=1
E
E~
z = 1 − y
2
z = 1 − y
2
E
~~
Figure 4.5 Top: Circles around±1 map to a circle around the origin.Bottom: The
curve ˜E mapped back to the z-plane.
Remark. The function (1−z)−1/2 is analytic on the slit planeC\{x∈R : x≥ 1},
which we may view as half of the Riemann surface R obtained by gluing two
copies of the slit plane, with the upper half of one attaching along the slit to
the lower half of the other. The change of variables z = 1− y2 maps from R
toC. The saddle point contour ˜E, when mapped to the z-plane, comes in to +1
along one copy of the slit, does a U-turn, and goes back along the other copy
of the slit. Perturbing slightly gives a hairpin-shaped contour ˜˜E that may be
drawn in the slit plane. This shape near 1 reﬂects the design of the ∆-domain
in Figure 3.1.
