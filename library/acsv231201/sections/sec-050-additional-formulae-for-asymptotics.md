---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-050-additional-formulae-for-asymptotics
section_title: "Additional formulae for asymptotics"
section_number: null
pages: 297-309
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
279
Figure 9.7 The two critical points for Q(x, y) = 3 −3x + x2 −y in directions
(a, 1 −a) with a < 1/2, which approach the same degenerate ‘double point’ (1, 1)
when a →1/2. Only the critical points with x > 1 are minimal for such directions.
Evaluating A(0) = −P(1, 1)/yQy(1, 1) = −1/(−1) = 1, Theorem 9.38 gives
ar,r ∼1
2πC(3, 0)i−1/3(1 −ζ)r−1/3 =
√
3Γ(1/3)
6π
r−1/3 .
◁
Remark. We have given a formula holding only very near a ﬁxed direction ˆr.
Because the results for nondegenerate smooth points hold in neighborhoods of
directions, it remains to be seen whether asymptotics can be worked out that
“bridge the gap” and hold when the distance δ = ||r −|r| · ˆr|| to the ray {λ · ˆr}
satisﬁes |r| ≫δ ≫1. See Section 13.2 for further discussion.
9.4 Additional formulae for asymptotics
It is sometimes useful to have alternative or more detailed formulae for the
coeﬃcients of the asymptotic expansions derived above. We collect some such
formulae in this section.
280
Smooth point asymptotics
9.4.1 Higher order terms
We ﬁrst examine explicit expressions for the higher order asymptotic coeﬃ-
cients.
Theorem 9.40. Under the hypotheses of Theorem 9.5, the asymptotic series
Φw(r) can be expressed as
Φw(r) =
w−r
p
det(2πrd H)
X
k≥0
p−1
X
j=0
(rd + 1)(p−1−j)
(p −1 −j)! j! r−k
d Lk(Aj, φ),
where
Lk(A, φ) = (−1)k X
0≤ℓ≤2k
Dℓ+k 
A(x) · φ(x)ℓ
2ℓ+kℓ!(ℓ+ k)!

x=0
for the functions
φ(x) = φ(x) −(1/2)x · H ·xT
Aj(θ) = Rj(w◦eiθ)
Rj(z) = (−g(z◦))−p+ j
lim
zd→g(z◦) ∂j
d ((zd −g(z◦))pF(z)) ,
and D is the diﬀerential operator
D = −
X
1≤i,j≤d

H−1
i j ∂i∂j.
Proof
Theorem 9.17 and Lemma 9.18 above imply that Φw(r) is obtained
from an asymptotic expansion of the saddle point integral (9.16), where the
residue Ψ is a weighted sum of terms Rk occurring in the explicit formula
(9.15). Distributing the integral over the sum of residue terms, Lemma 5.16
from Chapter 5 gives an asymptotic expansion of each. The stated result fol-
lows from simplifying the sum of these expansions, taking into account a subtle
interplay between the lower order terms in (9.15) and the higher order terms in
Lemma 5.16.
□
Remark 9.41. It is possible to expand the falling factorials in terms of the
Stirling numbers of the second kind and collect powers of rd, to give an explicit
formula for the coeﬃcients Ck in (9.4) at the cost of an even more unwieldy
formula.
Exercise 9.11. In the cases p = 1 and p = 2, explicitly compute the second
term in the asymptotic expansion of Φw(r) in descending powers of rd.
9.4 Additional formulae for asymptotics
281
9.4.2 A geometric formula for the leading term
Complementing the explicit expressions for asymptotics given above, it is pos-
sible to write down a coordinate-free representation for the leading term using
the curvature of V near the contributing singularities determining asymptotics.
In addition to an alternative, sometimes more compact, expression, coordinate-
free representations can also help with conceptual understanding, such as in
Example 9.47 below. We begin by reviewing the deﬁnition of the Gaussian
curvature of a smooth hypersurface, before extending it to certain points of
complex algebraic hypersurfaces.
Gaussian curvature of real hypersurfaces
For a smooth orientable hypersurface V ⊂Rd+1, the Gauss map G sends each
point p ∈V to a normal vector G(p), which we identify with an element of
the d-dimensional unit sphere S d. For a given patch P ⊂V containing p, let
G[P] = ∪q∈P G(q). The Gaussian curvature (also called Gauss–Kronecker
curvature) of V at p is deﬁned as the limit
K = lim
P→p
A(G[P])
A[P]
(9.21)
as P shrinks to the single point p, where A(G[P]) is the area of G[P] in S d
and A[P] is the area of P in V. When d is odd, the antipodal map on S d has
determinant −1, whence the particular choice of unit normal will inﬂuence the
sign K, which is therefore only well deﬁned up to sign. When d is even, we
take the numerator to be negative if the map G is orientation reversing and we
have a well deﬁned signed quantity. The curvature K is equal to the Jacobian
determinant of the Gauss map at the point p.
For computational purposes, it is convenient to use standard formulae for
the curvature of the graph of a function from Rd to R. If η is a homogeneous
quadratic form, we let ||η|| denote the determinant of the Hessian matrix of η
computed with respect to any orthonormal basis.
Proposition 9.42 ([Bar+10, Corollary 2.4]). Let P be the tangent plane to V
at p and let v be a unit normal vector. Suppose that V is the graph of a smooth
function h over P, meaning
V = {p + u + h(u)v : u ∈U ⊆P} .
If η is the quadratic part of h, so that h(u) = η(u)+O(|u|3), then the curvature
of V at p is K = ||η||.
□
Corollary 9.43 (curvature of the zero set of a polynomial). Suppose that V =
{x ∈Rd : Q(x) = 0} and that ∇Q(p) , 0. If η is the quadratic part of Q at p
282
Smooth point asymptotics
and η⊥is the restriction of η to the hyperplane orthogonal to ∇Q(p) then the
curvature of V at p is given by
K =
||η⊥||
||(∇Q)(p)||d−1
2
,
(9.22)
where ||(∇Q)(p)||2 denotes the Euclidean norm of the gradient of Q at p.
Proof
Replacing Q by ||(∇Q)(p)||−1
2 Q leaves V unchanged and reduces to the
case ||(∇Q)(p)||2 = 1, so we assume without loss of generality that ||(∇Q)(p)||2 =
1. Given an arbitrary vector u we write u = u⊥+ λ(u)(∇Q)(p) to denote the
decomposition of u into its components orthogonal to, and contained in, the
span of (∇Q)(p). The Taylor expansion of Q near p is
Q(p + u) = (∇Q)(p) · u + η⊥(u) + R ,
where R = O(|u⊥|3 + |λ(u)||u⊥|). Near the origin, we can solve for λ to obtain
λ(u) = η⊥(u) + O(|u|3) ,
and the result follows from Proposition 9.42.
□
Gaussian curvature at minimal points of complex hypersurfaces
Suppose now that Q is a real polynomial in d variables and that p is a minimal
smooth point of the corresponding complex algebraic hypersurface. We are
interested in the curvature at log p of the logarithmic image log V = {z ∈Cd :
(Q ◦exp)(z) = 0} of V (this image is similar to the amoeba of Q except we
do not take moduli). When p is a point with positive real coordinates then the
curvature at log p can be deﬁned (up to a factor of ±1) directly using (9.22)
from Corollary 9.43. In fact, we use this formula to deﬁne curvature in the
general complex case as it is invariant under scalar multiplications of Q and
Theorem 6.44 from Chapter 6 implies that the normal (∇log Q)(p) to Q ◦exp at
a minimal point p is a scalar multiple of a real vector.
It is useful to observe that the curvature K is a reparametrization of the
Hessian determinant in our asymptotic theorems, in the sense that they vanish
together.
Proposition 9.44. The quantity K deﬁned by (9.22) vanishes if and only if the
determinant of the Hessian matrix H in Theorem 9.5 vanishes.
Proof
Going back to its original deﬁnition in Lemma 8.22, the matrix H in
Theorem 9.5 is the Hessian matrix for the function g expressing log V as a
graph over the ﬁrst (d −1) coordinates. At such a point, the tangent plane to
log V is not perpendicular to the dth coordinate plane, and reparametrizing the
9.4 Additional formulae for asymptotics
283
graph to be over the tangent plane does not change whether the Hessian is sin-
gular. The Hessian matrix obtained from such a reparametrization represents
the quadratic form η in Proposition 9.42, so singularity of the Hessian matrix
from Theorem 9.5 is equivalent to singularity of η in Proposition 9.42.
□
Theorem 9.45 (Main Theorem of Smooth ACSV (Curvature Version)). Let
F(z) = P(z)/Q(z) be the ratio of coprime polynomials with convergent Lau-
rent series expansion F(z) = P
r∈Zd arzr. Suppose there exists a compact set
R ⊂Rd of directions such that F has a smooth strictly minimal nondegenerate
contributing point w = w( ˆr) ∈Cd
∗, where Qzd(w) , 0 whenever ˆr ∈R. Let
K( ˆr) denote the Gaussian curvature of log V at log w( ˆr). Then
ar =
 
1
2π∥r∥2
!(d−1)/2
w−r K( ˆr)−1/2

P(w)
∥∇log Q(w)∥2
2
+ O

∥r∥−1
2

(9.23)
uniformly as ∥r∥2 →∞with ˆr ∈R. The square-root of the matrix determinant
is the product of the principal branch square-roots of the Jacobian of the Gauss
map when the Gauss map is oriented towards −ˆr.
Proof
As in the proofs above, we let ω = z−r−1F(z)dz so that
ar =
 1
2πi
!d−1 Z
σ
Res(ω)
where σ is an intersection class on V. To work in log space we let z = exp(ζ),
so dz = zdζ and
ar =
 1
2πi
!d−1 Z
˜σ
Res

exp(−r · ζ) ˜F(ζ) dζ

,
where ˜F = F ◦exp and ˜σ = log σ. In fact, our assumptions imply that we have
a simple pole, so we can pull out the factor of z−r = exp(−r · ζ) to obtain
ar =
 1
2πi
!d−1 Z
˜σ
exp(−r · ζ) Res( ˜F(ζ) dζ).
(9.24)
Let P be the tangent space to log V at the point ζ∗= log w. This tangent
space consists of the vectors orthogonal to ˆr, so we may locally parameterize
log V near ζ∗by P using a representation
log V = {ζ∗+ ζ∥+ h(ζ∥) ˆr : ζ∥∈P} .
Pick an orthonormal basis v(2), . . . , v(d) for P so that a general point ζ ∈Cd in
a neighborhood of ζ∗has a representation
ζ = ζ∗+ u1 ˆr +
d
X
j=2
ujv(j) .
284
Smooth point asymptotics
Proposition C.8 in Appendix C implies
Res( ˜F(ζ) dζ) =
P ◦exp
∂(Q ◦exp)/∂u1
du2 ∧· · · ∧dud+1 ,
and the partial derivative in the direction of the gradient is the square of the
magnitude of the gradient. Thus,
Res( ˜F(ζ) dζ)(ζ∗) =
P(w)
∥∇log Q(w)∥2
2
dA,
(9.25)
where dA = du∥= du2 ∧· · ·∧dud is equal to the oriented holomorphic (d −1)-
area form for log V as it is immersed in Cd.
Let λ = |r| and φ(ζ) = ˆr · ζ so that (9.24) becomes
ar =
 1
2πi
!d Z
˜σ
exp(−λφ(ζ)) Res( ˜F(ζ) dζ) ,
(9.26)
and let η denote the quadratic part of h. By Proposition 9.42 (or Corollary 9.43)
and the subsequent discussion, we see that the curvature K of log V at the point
ζ∗with respect to the unit normal ˆr is given by ||η||.
To proceed, we describe a logspace intersection cycle ˜σ. One way to con-
struct ˜σ is to pick a point x′ in the component of amoeba(Q)c giving the series
expansion under consideration, and a point x′′ in a component of amoeba(Q)c
on which the height function h is unbounded, and take the intersection cycle
of log V with a homotopy H obtained by taking a straight line from x′ to x′′
and mapping by Relog−1. A convenient choice is to make the segment x′x′′
parallel to ˆr. The real tangent space to H is then the sum of the imaginary
d-space and the real 1-space in direction ˆr. The tangent space to log V is the
sum of the real (d −1)-space orthogonal to ˆr and the imaginary (d −1)-space
orthogonal to ˆr. The tangent space to ˜σ is the intersection of these, which is
the imaginary (d −1)-space orthogonal to ˆr – in other words, just Im P.
Because ˜σ is contained in the linear space Im P + C · ˆr, we see that locally
there is a unique analytic function α : Im P →C · ˆr such that ζ + α(ζ) ∈˜σ.
Comparing to our parametrization above, we see that α = h, so the quadratic
part of α is therefore equal to η. Because our multivariate integral formulae
are in terms of real parametrizations, we reparametrize Im P by ζ = iy and
dζ = id dy. In these coordinates, locally
˜σ = {iy + h(iy) : y ∈Re P} .
(9.27)
9.4 Additional formulae for asymptotics
285
Using ˆr · y∥= 0 and ˆr · ˆr = 1, we obtain
φ(iy + h(iy)) = φ(ζ∗) + h(iy)
= φ(ζ∗) + η(iy) + O(|y|3)
= φ(ζ∗) −η(y) + O(|y|3) .
We know, by our assumptions, that φ is a smooth phase function whose real
part has a minimum on ˜σ at ζ∗, which is y = 0 in the parametrization (9.27).
Applying Theorem 5.3 to (9.26) using the evaluation (9.25) then gives (9.23),
where the square-root of the curvature is taken to be the reciprocal of the prod-
uct of the principal square-roots of the eigenvalues of −η in the positive ˆr-
direction, all of which have nonnegative real parts. The eigenvalues of −η in
direction ˆr are the same as the eigenvalues of η in direction −ˆr, which ﬁnishes
the proof of the theorem.
□
Again, minor modiﬁcations to proof extend to include the case where there
are ﬁnitely many critical points on a minimizing torus.
Corollary 9.46. Let F(z) = P(z)/Q(z) be the ratio of coprime polynomials
with convergent Laurent series expansion F(z) = P
r∈Zd arzr corresponding
to the amoeba complement component B ⊂amoeba(Q)c. Suppose there exists
a compact set R ⊂Rd of directions such that for each ˆr ∈R the function
ˆr · x is uniquely maximized at xmin ∈B, and that the set W of critical points
in Te(xmin) is ﬁnite, nonempty, and consists of smooth nondegenerate points
where some partial derivative of Q does not vanish. For each z ∈W( ˆr) write
z = exp(xmin + iy). Then
ar =
 
1
2π|r|
!(d−1)/2
e−r·x

X
z∈W( ˆr)
e−ir·y
P(z)
∥∇log Q(z)∥2
2
K (z)−1/2 + O(|r|−1)

uniformly as |r| →∞with ˆr ∈R.
□
Example 9.47 (Quantum walk). A quantum walk or quantum random walk
(QRW) is a model for a particle moving in Zd under a quantum evolution in
which the randomness is provided by a unitary evolution operator on a hidden
variable taking k states. States and position are simultaneously measurable, but
one must not measure either until the ﬁnal time n or the quantum interference
is destroyed. A one-dimensional quantum walk was brieﬂy presented in Ex-
ercise 9.8 as an example of torality. Here we illuminate the general form of
asymptotics for a QRW, using Theorem 9.45 and Corollary 9.46 to qualita-
tively describe the probability proﬁle of the particle at large time n. Further
examples of QRWs are given in Chapter 12.
A QRW is deﬁned by a k×k unitary matrix U along with k vectors v(1), . . . , v(k)
286 Smooth point asymptotics

in Z¢ representing possible steps of the walk. At each time step, the particle
chooses a new state j € [k] and then moves by a jump of v?. The amplitude
of a transition from state i to j is the entry U;,;, while the amplitude of a path
of n steps, starting in state ip and ending in states i, is aan U;,i,,,- Suppose the
particle starts, at time zero, at the origin in state 7. The amplitude of moving
from 0 to a point p in n time steps and ending in state j is obtained by summing
the amplitudes of all paths of n steps having total displacement p and ending in
state j. This description gives us everything we need to compute asymptotics
of QRWs — for more on the interpretation of quantum walks, see [Amb+01;
Bar+10].

The multiplicative nature of the amplitudes makes QRW a perfect candidate
for the transfer matrix method, the univariate version of which was discussed
in Section 2.2 and whose multivariate version will be discussed at length in
Section 12.4. Let M denote the k x k diagonal matrix whose (j, j)-entry is the
monomial z’” and let P(p, n) be the matrix whose (i, j)-entry is the amplitude
to go from the origin in state i at time zero to p in state j at time n. Define the
spacetime generating function

F(z) =D" P@,m(2°)P zig, (9.28)
pez
n>0
where z° = (z1,...,Zy) are d variables tracking walk position and zy.) is a

variable tracking walk length. The transfer matrix method easily gives
F(z) = (I~ za1MU)",
and the entries Fj; are rational functions with common denominator
Q = det(I — za41 MU). (9.29)

Exercise 9.12. Prove that Q in (9.29) satisfies the strong torality hypothesis
from Definition 9.20.

The component B of the amoeba complement that yields a series in Za41
whose coefficients are Laurent polynomials in z),...,z is contained in the
negative zy,1 halfspace and has the origin on its boundary. Its boundary is
smooth everywhere except the origin, where its dual cone K has nonempty in-
terior; see Figure 9.8. Recall the dual rate function 6" on directions from (6.5).
Whenever 0 € OB we may deduce that 6"(#) < 0 with equality only possible
if # € normal(B). The feasible velocity region of the QRW is the set R C R¢
consisting of all (7;,...,7@) such that exponential growth rate Bn, +3 Ta, 1)
from Definition 6.20 vanishes (in other words, it is the set of directions in
which the chance of finding the particle roughly at that rescaled point after a
9.4 Additional formulae for asymptotics
287
long time decays slower than exponentially). Then R ⊆Ξ, where Ξ is the rd = 1
slice of normal0(B) and is computed as an algebraic dual (see Example 6.50).
Figure 9.8 The component B and its dual cone K at the origin.
Smooth boundary points correspond to directions ˆr < K satisfying |r1| +
· · · + |rd| < |rd+1|. For each such ˆr there is one or more minimal smooth critical
points of V. To compute R, we start by computing V0 = V ∩T(0). For many
QRW’s one ﬁnds this to be a smooth manifold diﬀeomorphic to one or more
d-tori. At any smooth point z ∈V0, the space L(z) is the line in the direction
of ∇log Q(z). Thus, r ∈R if and only if r is in the closure of the image when
the logarithmic Gauss map ∇log is applied to V0, so that
R = ∇log[V0] .
This allows us to plot the feasible region by parametrizing V0 by an embedded
grid and applying ∇log to each point of the embedded grid, an example of which
is shown on the left of Figure 9.9.
The right of Figure 9.9 shows an intensity plot of the magnitude of the prob-
ability amplitude for the particle at time 200 for a QRW known as S (1/8). The
agreement of the shape of the empirically plotted feasible region (right) with
the theoretical prediction based on the Gauss map (left) is apparent. What is
also apparent is that not only do the regions agree but their ﬁne structure of
darker bands and light areas agree as well.
In particular, the image of V0 under ∇log will be more intense in places
where the Jacobian determinant of ∇log is small because the density of the
image of an embedded grid is proportional to the inverse of the Jacobian de-
terminant. The Jacobian determinant of the logarithmic Gauss map is pre-
cisely the curvature, as discussed following (9.21). In Theorem 9.45, while
288
Smooth point asymptotics
Figure 9.9 Left: The log-Gauss map on an embedded grid. Right: Probability am-
plitudes of a QRW.
the P/∥∇log Q∥2
2 term varies a little, the dominant factor is the curvature term
K−1/2. This explains why the density of the Gauss-mapped grid is a good sur-
rogate for the probability amplitudes.
◁
Changing the matrix U or the vectors v(j) changes the walk, hence there are
many quantum walks, most of which don’t have the symmetries of the S (1/8)
walk. Figure 9.10 shows the feasibility region for a more-or-less generic quan-
tum walk. Again, one sees an image of the logarithmic Gauss map. It is notable
that, as for many quantum random walks, the feasible region is nonconvex, in-
dicating that parts of the cone normal0(B) do not correspond to any minimal
points, but are instead in the region of exponential decay (the infeasible re-
gion).
Notes
Precursors to the derivations of the saddle point residue integrals in this chap-
ter were the multivariate asymptotic results [BR83]. Breaking the symmetry
among the coordinates, they wrote
F(z) =
∞
X
n=0
fn(z◦)zn
d
for (d−1)-dimensional series fn(z◦) and then used the fact that fn is sometimes
asymptotic to an nth power fn ∼C · g · hn to obtain Gaussian asymptotics when
certain minimality conditions are satisﬁed near a smooth critical point. Their
9.4 Additional formulae for asymptotics
289
Figure 9.10 Intensity plot for a quantum walk without symmetries.
language is inherently one-dimensional, so geometric concepts such as smooth
point did not arise explicitly.
The results presented in this chapter were ﬁrst obtained via a direct surgery
approach in [PW02], and are valid only for ﬁnitely minimal critical points.
In addition, the minimality hypothesis in [PW02, Theorem 3.5] (and in many
other results there) assumes an ordinary power series. The residue version of
these computations appeared in print ﬁrst in [Bar+10]. Extending the valid-
ity of the coordinate version beyond the case of ﬁnite intersection of V with
T(xmin) was accomplished in [BP11].
Between the ﬁrst and second editions of this book, a rigorous Morse theo-
retic foundation developed in [BMP22] streamlined some of the presentation of
this chapter. The ﬁnite criticality hypothesis in this second edition replaces the
strong torality hypothesis from the ﬁrst edition; there, the latter is simply called
torality. The explicit formula for higher order terms in Theorem 9.40 was ﬁrst
given by Raichev and Wilson [RW08]. Attempts to extend Algorithm 3 are
an ongoing topic of research by an AMS Mathematics Research Community
started in 2021.
The pictures in Figure 9.9 were ﬁrst produced by a Penn graduate student,
Wil Brady, in an attempt to produce rigorous computations verifying the limit
shapes of feasible regions that were suspected from simulations. At that time,
Theorem 9.45 was not known. The fact that the ﬁne structure of the two plots
agreed was a big surprise, and led to reformulated estimates such as (9.23) in
terms of curvature.
Another rewriting of the leading term of the basic nondegenerate smooth
point asymptotic formula is given in [Ben+12, Appendix B].
290
Smooth point asymptotics
Additional exercises
Exercise 9.13. Let Res be the residue map on meromorphic forms with simple
poles on a smooth variety V, as deﬁned in Proposition C.6. Prove that Res is
functorial, meaning it commutes with bi-holomorphic changes of coordinate.
Exercise 9.14. Let f(x, y) = x2 −3x + 3 −y. In Example 9.39, asymptotics in
the diagonal direction reveal a quadratic degeneracy. To see what a quadratic
degeneracy means topologically, begin by computing the critical points in the
direction r = (r, 1−r) as a function of r on the unit interval. There should usu-
ally be two critical points. At what value r∗of r is there a single critical point
of multiplicity 2? Check whether this is the same r for which the quadratic
term of h ˆr near the critical point z( ˆr) vanishes.
Exercise 9.15. Let F(x, y) = 1/(1 −x −y)ℓ. Compute the asymptotics for the
power series coeﬃcients a(ℓ)
rs and ﬁnd the relation between these and the asymp-
totics of the binomial coeﬃcients a(1)
rs =
r+s
r,s

. Verify this combinatorially by
ﬁnding the exact value of a(ℓ)
rs . Hint: When ℓ= 2, the bivariate convolution
of the binomial array with itself can be represented as divisions of r + s or-
dered balls into r balls of one color and s of another, with a marker inserted
somewhere dividing the balls into the two parts.
Exercise 9.16. (higher-order cube root asymptotics) In Example 9.39, dividing
the error when approximating the sequence by its leading asymptotic term by
the leading asymptotic term gives 0.00111 . . . when r = 100, hinting at the
fact that the next nonvanishing asymptotic term is r−m/3 for some m greater
than 2. Compute enough derivatives of A and φ at zero to determine the next
nonvanishing asymptotic term for arr.
