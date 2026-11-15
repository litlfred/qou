---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-022-analytic-versus-smooth-functions
section_title: "Analytic versus smooth functions"
section_number: null
pages: 123-132
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
105
4.3 Analytic versus smooth functions
Although most of our results above are stated for analytic amplitudes and
phases, their conclusions hold assuming only that these functions are C∞-
smooth. This indicates that there should be arguments using smooth tech-
niques, such as partitions of unity and integration by parts, rather than con-
tour deformation. Such an approach to evaluating saddle point integrals has
been developed and used extensively by harmonic analysts, who are chieﬂy
interested in the case where φ is purely imaginary. This is not covered by The-
orem 4.1, which requires that Re{φ} be strictly positive away from zero for
the contour decomposition used in our proof. Results in this section will be
used only once or twice for the analysis of generating functions in this book;
our chief reason for including this material is that any treatment of Fourier–
Laplace integrals bypassing smooth methods is pedagogically and historically
incomplete.
When the exponent φ is imaginary, the modulus of the Fourier–Laplace in-
tegrand is equal to |A(z)|, so it is no longer true that one may cut oﬀthe integral
outside of an interval [−ε, ε] and expect to introduce negligible remainders.
Instead, one assumes that A has compact support, then uses smooth partitions
of unity to reduce to integrals over small intervals. Note that neither partitions
of unity nor compactly supported functions exist in the analytic category; how-
ever, when the contour of integration γ is a closed curve, any amplitude func-
tion has compact support on γ so both the analytic and the smooth methods
apply and may be compared.
In this section we give asymptotics for the integral
I(λ) =
Z b
a
A(z) exp(iλφ(z)) dz,
where A and φ are smooth, φ is real, and A is supported on a compact sub-
interval of (a, b). Matching existing literature we use the term phase to denote φ
rather than iφ. The overall argument in the smooth case is the same as the proof
of Theorem 4.6, except for the insertion of a localization step at the beginning
and the introduction of a damping term in the step where both amplitude and
phase are monomial. Our process towards general asymptotics thus becomes:
localization, big-O estimate, monomials (with damping), monomial phase, and
then the full theorem.
Localization Lemma in C∞
Following [Ste93], we begin with a localization principle.
106
Fourier–Laplace integrals in one variable
Lemma 4.9 (Localization Lemma). Suppose φ is real and φ′(x) , 0 for all
x ∈(a, b). Then I(λ) is rapidly decreasing, meaning that for any ﬁxed N ≥0
we have I(λ) = O(λ−N) as λ →∞.
Proof
Our assumption that A is supported on a subset of the domain of in-
tegration allows us to integrate by parts without introducing boundary terms.
Integrating by parts with U = A/(iλφ′) and dV = iλφ′eiλφ dx gives
I(λ) = −
Z b
a
eiλφ(x) d
dx
 A
iλφ′
!
(x) dx ,
and by repeating this N ≥1 times we obtain
I(λ) =
Z b
a
eiλφ(x)(−λ−N)DN(A)(x) dx ,
(4.14)
where D is the diﬀerential operator f 7→(d/dx)( f/iφ′). If
KN = (b −a) sup
a≤x≤b
|DNA(x)|
(4.15)
then |I(λ)| ≤λ−NKN, which proves that I is a rapidly decreasing function of
λ.
□
Remarks.
(i) In the analytic case, if φ′ is nowhere vanishing then the con-
tour can be pushed down along a gradient ﬂow so that the maximum
of Re{iφ} is strictly negative, resulting in an exponentially (rather than
rapidly) decreasing integral.
(ii) Since φ′ does not vanish, we may change variables to y = φ(x) and the
conclusion of Lemma 4.9 is equivalent to the perhaps more familiar state-
ment that the Fourier transform of the smooth function ˜A(y) obtained is
rapidly decreasing.
(iii) While Lemma 4.9 is stated only for purely imaginary phase functions,
the same argument shows that I(λ) is rapidly decreasing whenever the
real part of φ is nonnegative and φ′ is nonvanishing.
Exercise 4.8. Suppose φ(x) = x and A(x) is periodic with fundamental domain
(−π, π].
(a) Show that there is no boundary term when integrating I over [−π, π].
(b) Applying the Localization Lemma with A(x) = 1 + cos(x), what value do
you get for K2 in the bound |I(λ)| ≤K2λ−2?
We call Lemma 4.9 the Localization Lemma for the following reason. Sup-
pose we allow φ′ to vanish on some ﬁnite set of points x1, . . . , xd ∈[a, b].
Then the contribution to I(λ) from any closed region not containing some xi
4.3 Analytic versus smooth functions
107
is rapidly decreasing, so the asymptotics for I(λ) may be read oﬀas the sum
of contributions local to each xi. Indeed, for each i let [ai, bi] be a tiny inter-
val containing xi, with all intervals disjoint, and let ξ1, . . . , ξd be a partition of
unity subordinate to {[ai, bi] : 1 ≤i ≤d}. Once we see how to obtain asymp-
totics in a neighborhood of xi containing no other critical points, we can write
A(x) = A0(x) + Pd
i=1 A(x)ξi(x), so that the support of A0 contains no xi. The
integral
R
A0(x)eiλφ(x) dx is rapidly decreasing by the Localization Lemma, so
as long as the integrals
Ii(λ) =
Z b
a
A(x)ξi(x)eiλφ(x) dx =
Z bi
ai
A(x)ξi(x)eiλφ(x) dx
sum to something not rapidly decreasing, the asymptotic development of I(λ)
is obtained by summing the developments of the Ii(λ).
We thus need only consider integrals over domains where the derivative of
the phase vanishes at a single point. Our main univariate result for integrals
with purely imaginary phase is the asymptotic development described in the
following result.
Theorem 4.10. Let φ and A be smooth real functions deﬁned on R with A
having compact support in an interval (a, b) whose closure contains zero. Let
k ≥2 and ℓ≥0 be integers and suppose the power series coeﬃcients for A
and φ at the origin are {bj} and {c j} as in Theorem 4.6, with ck > 0. Suppose
that φ′ vanishes in [a, b] at the origin but nowhere else, and let ˜A = (A ◦g) · g′
where g is the inverse function to x 7→(φ/ck)1/k. Then as λ →∞there is an
asymptotic development
I(λ) =
Z b
a
A(x) exp(iλφ(x)) dx ≈
∞
X
j=ℓ
α jC(k, j)(i ck λ)−(1+j)/k .
The coeﬃcients α j are obtained from the power series coeﬃcients a0, . . . , a j
for ˜A exactly as in part (iii) of Theorem 4.1. If the asymptotic expansion is
computed up to an O

λ−(N+1)/k
error term then this error term can be explicitly
bounded by a continuous function of the suprema of the ﬁrst N + 1 derivatives
of φ and A on the support of A. The kth root of i ckλ in this expansion is the
principal root.
The rest of this chapter is devoted to proving Theorem 4.10, using the steps
outlined above.
108
Fourier–Laplace integrals in one variable
The C∞Big-O Lemma
The smooth counterpart to Lemma 4.3 is established by showing that the main
contribution to I(λ) comes from an interval of size λ−1/k. The increase in length
for the proof of this result compared to the very short proof of Lemma 4.3
comes from the need to keep track of a partition of unity function and its
derivatives.
Lemma 4.11. If η is smooth and compactly supported and ℓ≥1 and k ≥2
are integers, then

Z ∞
−∞
eiλxk xℓη(x) dx

 ≤Cλ−(ℓ+1)/k
(4.16)
for a constant C depending only on k, ℓ, and the ﬁrst ℓderivatives of η.
Proof
Let α be a smooth bump function taking values in [0, 1] that is equal
to 1 on |x| ≤1 and vanishes on |x| ≥2. Choose ε > 0 and rewrite (4.16) as
Z ∞
−∞
eiλxk xℓη(x)α(x/ε) dx +
Z ∞
−∞
eiλxk xℓη(x)[1 −α(x/ε)] dx.
(4.17)
For any S ⊂R let 1S (x) denote the indicator function that equals one when
x ∈S and zero otherwise. The absolute value of the ﬁrst integrand in (4.17) is
everywhere bounded by |x|ℓ·sup|x|≤2 |η(x)|· 1|x|≤2ε, so its integral is bounded by
C1ε1+ℓwhere C1 = 2ℓ+2 sup|x|≤2 |η(x)|.
The second integral will be done by parts, and to prepare for this we examine
the iteration of the operator D : f 7→(d/dx)(f/xk−1) applied to the function
f(x) = xℓη(x)(1 −α(x/ε)). The result will be a sum of monomials, each mono-
mial being a product of a power of x, a derivative of η, a derivative of α, and a
power of ε: if [a, b, c, d] is shorthand for the term xa η(b)(x) α(c)(x/ε) εd then
D·[a, b, c, d] = (a−k+1)[a−k, b, c, d]+[a−k+1, b+1, c, d]+[a−k+1, b, c+1, d−1]
whenever a ≥0. By induction, we see that DN · [a, b, c, d] is the sum of terms
of the form C[r, s, t, u] where
r + u ≥a + d −kN,
s ≤b + N,
t ≤c + N,
and C is bounded above by the factorial of max{kN, a}. In particular, since
ε ≤x we may replace positive powers of ε by the same power of x to arrive at
the upper bound

DN h
xℓη(x)(1 −α(x/ε))
i

 ≤1|x|≥εC2|x|ℓ−kN,
(4.18)
where C2 is the product of 2 · 3N · sup j≤N,|x|∈(1,2) η( j)(x) and the maximum of 1
and sup j≤N,|x|∈(1,2) α(j)(x).
4.3 Analytic versus smooth functions
109
Now we ﬁx an N large enough so that ℓ−kN + 1 < 0, and perform inte-
gration by parts on the second integral of (4.17) N times, each time integrating
−ikλxk−1eiλxk and diﬀerentiating the rest, ending with
Z ∞
−∞
eiλxk(−ikλ)−NDN h
xℓη(x)(1 −α(x/ε))
i
dx.
By (4.18) the modulus of this integrand is at most C21|x|≥ε|x|ℓ−kN(kλ)−N so the
integral is bounded by C3λ−Nεℓ−kN+1, where C3 = 2C2/(1 −ℓ+ kN). Setting
ε = λ−1/k and adding the bounds on the two integrals yields an upper bound of
(C1 +C3)λ−(1+ℓ)/k on the modulus of the integral in (4.16). We have also shown
that C1 and C3 depend only on k, ℓ, the ﬁrst ℓderivatives of η, and the ﬁrst ℓ
derivatives of α. Fixing any valid choice of the function α thus completes our
proof.
□
Exercise 4.9. For a smooth function α taking value zero on negative arguments
and value one on arguments ε or greater, what is the least possible value of
supx |α′′(x)|? This question is motivated by the reliance on smooth partitions
of unity and the derivatives of α appearing in (4.18).
Lemma 4.11 immediately implies the following result.
Corollary 4.12. If a smooth function g vanishes in a neighborhood of the
origin and decreases rapidly at inﬁnity (or is compactly supported) then I(λ) =
R ∞
−∞g(x)eiλxk dx is rapidly decreasing.
□
A and φ are monomials and A is damped
In this section we prove the C∞version of Lemma 4.4. Since a monomial
amplitude function does not have compact support, we introduce a damping
function which will later need to be removed. For parameters λ, k, ℓ, δ ∈R
with k ≥2 deﬁne
I(λ, k, ℓ, δ) =
Z ∞
−∞
eiλxke−δ|x|k xℓdx .
(4.19)
Lemma 4.13. An asymptotic expansion
I(λ, k, ℓ, δ) = λ−(1+ℓ)/k
∞
X
j=0
C( j, k, ℓ, δ)λ−j
holds as λ →∞, where the constants C( j, k, ℓ, δ) with j > 0 go to zero as
δ →0.
110
Fourier–Laplace integrals in one variable
Proof
Let I+(λ, k, ℓ, δ) denote the integral obtained by restricting the domain
of integration in (4.19) to [0, ∞) and deﬁne I−(λ, k, ℓ, δ) by restricting the do-
main of integration to (−∞, 0]. The change of variables z = (δ−iλ)1/kx implies
I+(λ, k, ℓ, δ) = limM→∞I[M]
+ (λ, k, ℓ, δ), where
I[M]
+ (λ, k, ℓ, δ) = (δ −iλ)−(1+ℓ)/k
Z M(δ−iλ)1/k
0
e−zkzℓdz
has as its domain of integration the line segment from the origin to M(δ−iλ)1/k
in C. The integral over this line segment in complex space is the same as the
integral over the real line segment from the origin to M|δ −iλ|1/k followed by
the imaginary line segment from M|δ −iλ|1/k to M(δ −iλ)1/k. Thus, for ﬁxed λ
we can write
I[M]
+ (λ, k, ℓ, δ) = (δ−iλ)−1+ℓ
k
Z M|δ−iλ|1/k
0
e−zkzℓdz+(δ−iλ)−1+ℓ
k
Z M(δ−iλ)1/k
M|δ−iλ|1/k
e−zkzℓdz.
Since k ≥2 the modulus of the integrand e−zkzℓon the imaginary line seg-
ment decays exponentially with M, and the length of this segment grows only
linearly with M. Taking M →∞thus implies
I+(λ, k, ℓ, δ) = (δ −iλ)−(1+ℓ)/k
Z ∞
0
e−zkzℓdz ,
rotating our domain of integration back to the real axis. The deﬁnite integral
in this expression has value C(k, ℓ) = k−1Γ((1 + ℓ)/k), and expanding (δ −
iλ)−(1+ℓ)/k = (−iλ)−(1+ℓ)/k(1 + δi/λ)−(1+ℓ)/k using the binomial theorem gives
I+(λ, k, ℓ, δ) = C(k, ℓ)eiπ(1+ℓ)/(2k)λ−(1+ℓ)/k
∞
X
j=0
(iδ)j
 −(1 + ℓ)/k
j
!
λ−j.
Writing
C+( j, k, ℓ, δ) = k−1Γ
 ℓ+ 1
k
!
eiπ(1+ℓ+jk)/(2k)
 −(1 + ℓ)/k
j
!
δ j
(4.20)
and deﬁning constants C−( j, k, ℓ, δ) by performing the analogous computa-
tion on I−( j, k, ℓ, δ) proves the lemma by taking C( j, k, ℓ, δ) = C+( j, k, ℓ, δ) +
C−( j, k, ℓ, δ).
□
φ is a monomial and A is anything
Theorem 4.14. Let φ(x) = xk and let A be a smooth function with com-
pact support containing the origin. If the Taylor series of A at the origin
4.3 Analytic versus smooth functions
111
has coeﬃcients {bj} and ℓdenotes the smallest index such that bℓ, 0 then
I+ =
R ∞
0 A(x) exp(iλφ(x)) dx has an asymptotic development
I+ ≈
∞
X
j=ℓ
b j C(k, j) (iλ)−(1+ j)/k.
The error obtained by taking the (N −1)st partial sum is O(λ−N/k) with the
implied constant bounded in terms of the suprema of the ﬁrst N derivatives
of A near the origin. A similar result holds for the two-sided integral I with
coeﬃcients α j obtained from conclusion (iii) in Theorem 4.1 with aj = bj.
Proof
Let U be a smooth function that is 1 on the support of A and vanishes
outside of a compact set. Fix N ≥1 and δ > 0, and let P(x) = PN,δ(x) be the
Nth Taylor polynomial for eδxkA(x) (obtained by truncating its Taylor series at
the xN term). If b j,δ denotes the coeﬃcient of x j in P(x) and the normalized
remainder term R(x) = RN,δ(x) is deﬁned by eδxkA(x) = P(x) + xN+1R(x) then
I+ = B1 + B2 + B3, where
B1 =
Z ∞
0
eiλxke−δxkP(x) dx ,
B2 =
Z ∞
0
eiλxk xN+1e−δxkR(x)U(x) dx ,
B3 =
Z ∞
0
eiλxke−δxkP(x)(U(x) −1) dx .
By Lemma 4.11 with η(x) = e−δxkR(x)U(x) and ℓ= N +1, we know that |B2| ≤
Kλ−(ℓ+2)/k for some constant K > 0 that can be bounded in terms of k, ℓ, and
the ﬁrst ℓderivatives of A, the bound being uniform over δ in a neighborhood
of the origin.
Similarly, by Corollary 4.12 we see that B3 is rapidly decreasing as λ →∞.
It follows that the asymptotic series for I+ up to the λ−(ℓ+1)/k term may be
obtained by taking δ →0 in B1. Since P is a ﬁnite sum of monomials, we may
use Lemma 4.13 to compute B1 and prove the theorem. As before, we may sum
results for I+ and the analogous integral I−over the negative real half-line to
prove the result for I.
□
General A and φ
Since iφ always lies along the imaginary axis, we may use a diﬀeomorphic
change of variables to transform φ into ickxk, under which the contour remains
112
Fourier–Laplace integrals in one variable
along the imaginary axis (thus there is no need for arguments about moving
the contour).
Proof of Theorem 4.10.
By assumption, we can write φ(x) = ckxk(1 + θ(x)),
where θ(x) = O(|x|). If y = x(1 + θ(x))1/k then y(x) is a diﬀeomorphism in
a neighborhood of the origin, and we write x = g(y) for its inverse. Since
ckyk = φ(x) we may change variables to see that
Z
eiλφ(x)A(x) dx =
Z
eiλckyk ˜A(y) dy ,
and the result follows from Lemma 4.4.
□
Notes
Our chief sources for Sections 1 and 2 were [BH86] and [Won01], along
with [Hen91]. Although our main theorem follows from the extensive anal-
yses in [BH86, Chapter 7], for example, asymptotics of Fourier and Laplace
transforms are seldom treated together, and we have never seen the univariate
Fourier–Laplace Theorem stated in exactly this form. We have also not seen a
derivation by purely complex analytic methods.
Watson’s Lemma may be found in many places. The version here agrees
with the statements in [BH86, Section 4.1] and [Hen91, Section 11.5]. The
saddle point method is described very nicely in [dBru81] and [FS09, Chapter
VIII]. Our treatment is more akin to [Hen91, Section 11.8]; see also [BH86,
Chapter 7], especially for some of our exercises.
Section 4.3 borrows heavily from [Ste93], although we have attempted to
ﬁll in some details. For instance, our proof of Lemma 4.11 is summarized
as “A simple computation shows...” in [Ste93, page 335], which also omits
details as to how the argument for k = 2 extends to greater values of k. Despite
its omission of detail in elementary arguments, Stein’s book is a beautifully
written modern classic, and is a recommended addition to anyone’s bookshelf.
Additional exercises
Exercise 4.10. Let φ : R →R be deﬁned by
φ(x) =

exp

−1
x2

if x , 0
0
if x = 0.
4.3 Analytic versus smooth functions
113
Show that φ is of class C∞and that all derivatives of φ vanish at 0. Explain
the relevance of this fact to the asymptotic formulae derived in the theorems in
this chapter.
Exercise 4.11. If k = 2 and ℓ= 0 then Theorem 4.1 gives
I = b0
r π
c2
λ−1/2 + α2λ−3/2 + O(λ−5/2) .
Compute the coeﬃcient α2 in terms of b0, b1, b2, c2, c3, and c4.
Exercise 4.12. The Bessel function is deﬁned by
Jm(r) = 1
2π
Z 2π
0
exp(ir sin θ −imθ) dθ ,
where m is a ﬁxed parameter (you may assume it is a positive integer). Use
Theorem 4.10 to ﬁnd the two leading terms of an asymptotic series for Jm(r)
in decreasing powers of r.
Exercise 4.13. The Airy function is deﬁned by
Ai(x) = 1
2π
Z ∞
−∞
ei(xt+t3/3) dt .
Find an asymptotic expression for Ai(x) as x →∞in R by (1) performing the
change of variables t = ix1/2u, (2) ﬁnding the critical points and deforming
the contour of integration to pass through one or more of them, and (3) com-
puting the expansion on a compactly supported interval and arguing that this
converges as the limits of integration go to inﬁnity.
Exercise 4.14. Continue the error estimation in Exercise 4.9.
(a) In terms of ε and j, what is the least value of sup0≤x≤ε |α(j)(x)| for a bump
function α that is ﬂat on the complement of [0, ε] and goes from value zero
to value one?
(b) What does this imply about a lower bound on the implied constant CM in
the O(λM) error term?
(c) Assuming this lower bound can be achieved, for ﬁxed λ what value of M
optimizes the error bound CMλM?
