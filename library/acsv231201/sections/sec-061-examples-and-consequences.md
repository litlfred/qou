---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-061-examples-and-consequences
section_title: "Examples and consequences"
section_number: null
pages: 386-399
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
We now give several examples computing asymptotics determined by a mini-
mal point that is a Lorentzian quadratic.
Example 11.41 (power of a cone). Let F(x, y, z) = 1/Q(x, y, z)β where
Q(x, y, z) = (1 −x)(1 −y) + (1 −x)(1 −z) + (1 −y)(1 −z).
Friedrichs and Lewy [FL28] were interested in nonnegativity of the power
series coeﬃcients of F when β = 1 while they studied a discretized time-
dependent wave equation in two spatial dimensions; such nonnegativity was
proven for β > 1/2 in classical work of Szeg˝o [Sze33]. A vast generalization
of this result, applying to the reciprocal of the Tutte polynomial of a graph with
all variables e replaced by 1 −e, was later studied by Scott and Sokal [SS14].
In logarithmic coordinates (u, v, w) = exp(x, y, z), the leading homogeneous
term of Q at the singular point (0, 0, 0) of log V is the second elementary sym-
metric function q(u, v, w) = uv + uw + vw. The power series expansion of F
corresponds to the component of amoeba(Q)c containing points (−N, −N, −N)
with N suﬃciently large, and the normal cone at this singular point is the cone
of all directions (r, s, t) such that r2 + s2 + t2 < 2(rs + rt + st). This cone
is contained in the positive orthant and its boundary is tangent to the coor-
dinate hyperplanes along the directions (1, 1, 0), (1, 0, 1), and (0, 1, 1). Thus,
N = N(0,0,0)(B) is a symmetric cone inscribed in the positive orthant. Because
nonnegativity of the coeﬃcients is known for some β, the boundary of the
amoeba is contained in the real variety; the real variety does not intersect the
projective dual cone in log space, so this example satisﬁes Assumption (11.7).
Substituting the result of Proposition 11.38 into Theorem 11.40, taking β to
be greater than 1/2, we compute that the dual to q is 2(rs+st+rt)−(r2+s2+t2)
and deduce
ar ∼
41−β
√πΓ(β)Γ(β −1/2)(2rs + 2rt + 2st −r2 −s2 −t2)β−3/2
11.4 Examples and consequences
369
as r →∞, uniformly as ˆr varies over compact subsets of the interior of N.
◁
Stringing together several facts we have accumulated concerning amoebas,
tangent cones, and hyperbolicity leads to a useful one-sided bound. Given a
Laurent polynomial Q and a component B of the complement of amoeba(Q),
we know from Proposition 11.26 that any z = exp(x + iy) ∈∂B ∩V has a
cone of hyperbolicity K containing tanx(B). From the remarks following Deﬁ-
nition 11.12, we know that K is convex and is a component of the complement
of the zero set of A = hom(Q ◦exp, x) in Rd. The homogeneous polynomial
A vanishes on the boundary of the cone K. Dualizing, we see that the alge-
braic dual A∗to A vanishes on the boundary of the dual cone N(z). It follows
that N(z) is a subset of the largest subset L of the halfspace dual to u that is
bounded by the algebraic dual A∗to A. From this, it follows that for any r < L
the set local(r) is empty, whence by Theorem 11.4 the exponential rate β( ˆr)
is strictly less than β*( ˆr) = −ˆr · x. This proves an ACSV analogue of the
Paley–Wiener Theorem for Fourier transforms, which asserts that the general-
ized Fourier transform of a homogeneous function vanishes outside the dual
cone.
Theorem 11.42 (Paley–Wiener Theorem for ACSV). Let B be a component of
the complement of amoeba(Q), let Q vanish at z = exp(x + iy), and let u be
any element of tanx(B). Then β( ˆr) < −ˆr · x for any ˆr outside the closed dual
cone normalx(B) = (−tanx(B))∗. In particular, when tanx(B) is bounded by
the algebraic tangent cone then normalx(B) is bounded by the algebraic dual
cone.
□
When the point x is the origin, as it is in many probabilistic examples, The-
orem 11.42 implies that the Laurent coeﬃcients ar decay exponentially as
r →∞with ˆr bounded outside the algebraic dual cone at the origin.
Example 11.43 (cube groves). Let
F(x, y, z) =
1
1 + xyz −(x + y + z + xy + xz + yz)/3
be the cube grove creation generating function, let x = 0, and let B be the
component of amoeba(Q)c containing the negative orthant. Then
A = hom(Q ◦exp) = 2xy + 2xz + 2yz
is twice the second elementary symmetric function. This quadratic form is rep-
370
Cone point asymptotics
resented by the matrix
M =

0
1
1
1
0
1
1
1
0

while the dual of A is represented by the matrix
M−1 = 1
2

−1
1
1
1
−1
1
1
1
−1
.
Thus
A∗(r, s, t) = rs + rt + st −1
2

r2 + s2 + t2
and the zero set of A∗is a circular cone ∂L tangent to the three bounding
planes of the positive orthant at the diagonals {x = y, z = 0}, {x = z, y = 0}, and
{y = z, x = 0} bounding a solid cone L. It follows from Theorem 11.42 that ar
decays exponentially as r →∞in any closed cone disjoint from L.
◁
Example 11.43 derives the “easy” direction for asymptotics, which follows
directly from Theorem 11.42 and the computation of the dual cone. Neverthe-
less, this computation and its counterpart for orientation probabilities (where
the denominator has an extra factor of 1 −z) are the main results in the pa-
per that introduced cube groves [PS05]. The analysis here is simpler because
the hyperbolicity results above reduce geometric questions in complex codi-
mension 1 to corresponding analyses in real codimension 1, where one can
use connectivity and natural orientations. The machinery of algebraic duals
and Theorem 11.42 combine to make it almost automatic to show exponential
decay outside a set of directions whose boundary is the algebraic dual.
The “hard” direction for asymptotics is showing that there is no exponential
decay when r is in the interior of L. This is harder to do because we typi-
cally need to evaluate the integral near the points of local( ˆr) to show that
asymptotics are indeed not decaying exponentially. In this case we can apply
Theorem 11.40 and Proposition 11.38 directly to obtain the following result
for cube grove creation rates.
Corollary 11.44. The creation rates {ar,s,t} deﬁned by the power series expan-
sion of F(x, y, z) in (11.43) satisfy
ar,s,t ∼1
π
"
rs + rt + st −1
2(r2 + s2 + t2)
#−1/2
as (r, s, t) →∞within a closed subcone in the interior of L.
□
11.4 Examples and consequences
371
Example 11.45 (Aztec Diamond). Let Q(x, y, z) = 1−(x+x−1+y+y−1)z/2+z2.
The Laurent expansion of
F(x, y, z) =
z/2
(1 −yz)Q(x, y, z)
in the domain of convergence containing the point (1, 1, 0) enumerates infor-
mation about the Aztec Diamond, a combinatorial structure we do not describe
here. The singular variety VQ is smooth except at ±(1, 1, 1), where it is rep-
resented by a Lorentzian quadratic. The homogenization ˜q of q = Q ◦exp
at the origin is the circular cone 2z2 −(x2 + y2) and the cone of hyperbol-
icity containing the negative z-axis, which is the one of interest, is the cone
B−= {(x, y, z) : z < −
p
(x2 + y2)/2}. Its dual is given by
B∗
−=
(
(r, s, t) : r2 + s2 ≤1
2t2
)
.
The other factor 1 −yz is smooth at ±(1, 1, 1) and is in fact already linear
when put in logarithmic coordinates: if (x, y, z) = exp(u, v, w) then yz = 1
becomes v + w = 0. The cones of hyperbolicity are the two halfspaces H−=
{v+w < 0} and H+ = {v+w > 0}, the former containing the negative z-axis. The
amoeba of a product is the intersection of the amoebas of the factors, hence the
component corresponding to the chosen Laurent expansion is B0 = B−∩H−.
Dualizing, B∗
0 is equal to the convex hull of B∗
−∪H∗
−. Projectively, B∗
−is the
cone over the circle {ˆr2 + ˆs2 ≤1/2} while H∗
−is the single point (0, 1). The
convex hull of the union is the teardrop shape shown in Figure 11.4. We thus
have the following consequence of Theorem 11.42.
Figure 11.4 The teardrop-shaped region in Example 11.45.
Corollary 11.46. Outside of the teardrop shaped region given by the convex
hull of B∗
−∪{(0, 1)}), the Aztec Diamond placement probabilities decay ex-
ponentially. More speciﬁcally, the north-going placement probabilities decay
372
Cone point asymptotics
exponentially unless either ˆr2 + ˆs2 ≤1/2, in which case these converge to a
quantity in (0, 1) for ﬁxed ˆr as r →∞, or ˆr2 + ˆs2 > 1/2 and ˆs > |ˆr|, in which
case the north-going placement probability converges to 1.
◁
Example 11.47 (fortress tiling). The fortress tiling ensemble is a combinato-
rial structure enumerated by a generating function of the form G/(Q1 · · · Qk·Q),
where the Qi are all smooth at the point (1, 1, 1) and Q is a nondegenerate quar-
tic and the homogeneous part of Q ◦exp at (0, 0, 0) is given by
A(x, y, z) = 200z2 
2z2 −x2 −y2
+ 9

x2 −y22
(see, for example, [Du11]). The zero set of A is a cone over the curve 400 −
200x2 −200y2 + 9

x2 −y22 = 0 depicted in Figure 11.5.
Figure 11.5 Cross-section of the homogeneous part of the fortress generating
function.
The Fourier transform of A will be computed in forthcoming work of Barysh-
nikov and Pemantle. Without this, however, we can still prove that the coeﬃ-
cients arst decay exponentially outside the algebraic dual curve. Computing a
Gr¨obner basis of the ideal ⟨r −Ax, s−Ay, t−Az, A⟩produces a basis whose ﬁrst
11.4 Examples and consequences
373
entry is the algebraic dual
A∗(r, s, t) = 729 t8 −13608 t6s2 −22896 s4t4 + 64000 s6t2 + 102400 s8
−13608 r2t6 + 412992 s2t4r2 −1104000 s4r2t2 + 870400 s6r2
−22896 r4t4 −1104000 r4s2t2 + 2054400 s4r4 + 64000 r6t2
+ 870400 r6s2 + 102400 r8 .
This projective curve is a cone over the octic aﬃne curve
q∗(r, s, t) = 729 −13608 s2 −22896 s4 + 64000 s6 + 102400 s8 −13608 r2
+ 412992 s2r2 −1104000 s4r2 + 870400 s6r2 −22896 r4
−1104000 r4s2 + 2054400 s4r4 + 64000 r6 + 870400 r6s2 + 102400 r8
whose zero set is shown in Figure 11.6. The real part of this octic curve has two
Figure 11.6 The fortress dual curve.
components, consisting of a concave aster-shaped region inside a nearly circu-
lar region. The dual cone N(1, 1, 1) must be contained within the outer curve,
leading to the following “octic circle” result, conjectured by Cohn and Peman-
tle in 1998 and proved when Kenyon and Okounkov obtained asymptotics for
this ensemble [KO07].
374
Cone point asymptotics
Theorem 11.48. Let K be the cone over the region bounded by the outer dual
curve q∗. Then, uniformly over closed cones disjoint from the closure of K, the
coeﬃcients of the fortress generating function decay exponentially. A normal-
ized vector (r/t, s/t, 1) is in the region of exponential decay if q∗is positive
there and it is not in the inner area which is separated from the outer circle by
any circle lying between them (such as ˆr2 + ˆs2 = 1/4).
□
◁
Product of a cone and a plane
The Fourier transforms for the Aztec Diamond and the cube grove probability
generating functions, which involve the product of a function with a cone point
singularity and a smooth hyperplane, are explicitly computable. The compu-
tation, contained in [BP11], is too long to include here, but the result can be
understood intuitively as follows.
The Fourier transform of a linear function is a Heaviside function, the delta
function of a ray {t ˆu : t ≥0}. The Fourier transform of a product is the con-
volution of the transforms of the factors, whence the Fourier transform of a
product L · L, where L is linear, is given by
Z ∞
0
ˆL(r −t ˆu) dt .
When ˆL is supported on a cone (e.g., by the Paley–Wiener Theorem) and for
any r the integrand vanishes for suﬃciently large t, this leads to a simple in-
tegral. Formalizing this intuition involves a lot of checking that certain lim-
its commute and appears daunting. Instead, the integral was computed in a
roundabout but rigorous manner in [BP11, Section 4.1–4.2], leading to inverse
trigonometric functions.
Theorem 11.49 ([BP11, Theorem 4.1–4.2]). Let {ar,s,t} be the series coeﬃ-
cients for
A(x, y, z) =
z/2
(1 −yz)(1 −(x + x−1 + y + y−1)/2 + z2)
corresponding to the amoeba complement component B containing the nega-
tive z-axis. These coeﬃcients satisfy
arst ∼(1 + (−1)i+ j+n+1) 1
2π arctan

√
t2 −2r2 −2s2
t −2s

uniformly over compact subsets of the interior of the disconnected set which
is the teardrop-shaped region in Figure 11.4, taken to exclude the dashed line.
11.4 Examples and consequences 375

Here, the arctangent is taken in [0,2] so that it varies continuously as s/t
increases through 1/2.
Let {b,,;,} be the series coefficients of

22
(l-zd +xyz— (et yt+z4 xy + xz + yz)/3)

B(x, y,2) =

corresponding to the amoeba complement component B containing the nega-
tive diagonal. These coefficients satisfy

V2(rstrt+ st)—(P +92 +P)
rt+s-t

1
bys ~ — arctan
qT

uniformly over compact subsets of the interior of the region shown in Fig-
ure 11.7 in symmetrized coordinates. Again, the arctangent is taken in [0,7]
and the solid vertical line is excluded from the region. ia)

y=0,x=2

Figure 11.7 The dual cone in symmetrized coordinates.

Exercise 11.8. Use the same intuition to recompute asymptotics for the power
series expansion of the multiple point at (1,1, 1) in the generating function
See The Fourier transforms of the factors are delta functions in the
directions of the rays in the respective directions (1,0), (0, 1), and (1, 1). The
convolution of the first two is 1 on the positive quadrant and 0 elsewhere. Up
to a constant multiple, what do you get when you convolve this with the third

delta function? Check your answer against Example 10.47.

Presence of a lacuna
Given the dimension d of the space and the power s of the Lorentzian quadratic
S, the Fourier transforms yn m(1r) of S~*~” in the expansion of (11.17) are well
known; see for example [BP11, Theorem 6.4]. When s = d/2 — 1, this Fourier
transform is not a function but rather a distribution (generalized function in the
terminology of [GS16]) which vanishes on the inside of the normal cone N as
376
Cone point asymptotics
well as the outside, being supported entirely on ∂N. In the optics literature, this
phenomenon is called a lacuna. For directions ˆr interior to N the asymptotic
development in Theorem 11.40, which has decreasing scales |r|−kz−r for inte-
gers k going to inﬁnity, is everywhere zero, and the result only states that the
asymptotics inside the cone are smaller in magnitude than any such term.
While Theorem 11.40 relies on Assumption (11.7) which does not hold for
this example, topological analysis [BMP19, Theorem 2.3] gives us everything
we need. It shows that for ˆr ∈N◦and x ∈B, where B is the component of the
amoeba complement corresponding to ordinary power series, the torus Te(x)
is homologous to a cycle whose maximum height is less than the height of the
cone point. This, together with a computation ruling out CPAI and a Morse
theoretic analysis along the lines of Theorem 7.35, shows that asymptotics are
characterized by critical points of lower height. We include such an example
here, pulling together many of the methods developed thus far to exhibit a
minimal point p for which np = 0 even when ˆr is interior to the normal cone
N at p, and illustrating non-zero coeﬃcients not in {±1, 0}.
Example 11.50. Gillis, Reznick, and Zeilberger [GRZ83] consider a family of
4-variable generating functions Fλ(z) = 1/(1 −z1 −z2 −z3 −z4 + λz1z2z3z4)
with λ a real parameter, having origins in the earlier work [AG72; Sze33].
The behavior of the function and its coeﬃcient array diﬀers in the cases λ <
27 and λ > 27. At the critical parameter value λ = 27 the denominator Q
fails to be smooth, having instead a singularity at the diagonal point p =
(1/3, 1/3, 1/3, 1/3) diﬀeomorphic to a Lorentzian quadratic. For a direction
ˆr in the interior of N(p), one would normally expect β( ˆr) = −P4
j=1 r j log(1/3).
In other words, if np , 0, then log |ar,s,t,u| ∼(r + s + t + u) log 3 inside the
normal cone and n−1 log an,n,n,n →log 81.
However, the number of variables d is 4, the minimum for d/2 −1 to be a
positive integer. The coeﬃcients of F27(z) = Q(z)1−d/2 = Q(z)−1 exhibit a
lacuna, and the exponential rate is in fact given by log |ar,s,t,u| ∼(r + s + t +
u)(log 3)/2 so that n−1 log an,n,n,n →log 9. The bulk of [BMP19] is devoted to
showing that the contour for the Cauchy integral for the main diagonal of the
ordinary power series expansion is homologous to a cycle Γ supported at height
less than log 81. This is not achieved by a deformation but rather by an explicit
cobordism which is the limit of deformations in perturbed varieties. Informally,
one might say there is a deformation that passes through the singularity at the
cone point. Assuming this as a black box result, we complete the analysis as
follows.
A quick Gr¨obner basis computation shows that the critical points in the di-
agonal direction are precisely p = (1/3, 1/3, 1/3, 1/3), w = (ζ, ζ, ζ, ζ), and
11.4 Examples and consequences
377
w = (ζ, ζ, ζ, ζ), where ζ = (−1 + i
√
2)/3 has modulus
√
3. Further computer
algebra shows V to have the geometry of a Lorentzian cone near p, and Al-
gorithm 1 from Chapter 8 veriﬁes that there are no CPAI in the main diagonal
direction. Applying Corollary 7.17 to the black box result, we see that the cy-
cle Γ may be pushed down further to the level of the next critical points w and
w. As these are the only two remaining critical points, and the asymptotics are
not eventually zero, we know that
ar ≈κ (Φw(r) + Φw(r)) = 2κ Re{Φw(r)}
(11.18)
for some non-zero integer κ and Φw given by (9.4).
We compute κ for the main diagonal direction, which extends automatically
to a neighborhood of the diagonal, by comparing (11.18) to asymptotics com-
puted from an analysis of the ODE obtained by representing the diagonal as
a D-ﬁnite function using the techniques described in Section 8.4.2 of Chap-
ter 8. In particular, creative telescoping methods compute that the generating
function f(z) of the main diagonal satisﬁes
z2(81z2 + 14z + 1)f (3)(z) + 3z(162z2 + 21z + 1)f (2)(z) + (21z + 1)(27z + 1)f ′(z)
+ 3(27z + 1)f(z) = 0 .
(11.19)
This ODE is Fuchsian: all singular points of solutions are regular and are
contained in the set of roots {0, ζ4, ζ4} of the leading polynomial coeﬃcient
z2(81z2 +14z+1). The techniques described in Chapter 8 for D-ﬁnite functions
compute a basis for the three-dimensional vector space of solutions to (11.19),
whose expansions at the origin begin
a1(z) = log(z)2
 1
2 −3z
2 + 9z2
2 + · · ·
!
+ log(z)

−4z + 18z2 + · · ·

+

8z2 −48z3 + · · ·

a2(z) = log(z)

1 −3z + 9z2 + · · ·

+

−4z + 18z2 + · · ·

a3(z) = 1 −3z + 9z2 + · · · ,
378
Cone point asymptotics
and another basis of solutions whose expansions around ζ4 begin
b1(z) = 1 +

13
2 + 43
√
2
4
i
(z −ζ4)2 +

8165
48
+ 943
√
2
30
i
(z −ζ4)3 + · · ·
b2(z) =
q
z −ζ4 +
 13
3 −365
48
√
2
i
!
(z −ζ4)
3
2 −
 7071
1024 −1041
16
√
2
i
!
(z −ζ4)
5
2 + · · ·
b3(z) = (z −ζ4) +

17
3 −31
√
2
6
i
(z −ζ4)2 −

1013
72
+ 1805
√
2
36
i
(z −ζ4)3 + · · · .
In the {aj} basis, the diagonal generating function f(z) is a3(z), because this
is the only element of the span that is continuous in a neighborhood of the
origin and has constant coeﬃcient 1. A change of basis matrix between the
{aj} and {bj} bases can be computed numerically, in this case giving
f(z) = a3(z) = C1b1(z) + C2b2(z) + C3b3(z)
where C1,C2, and C3 are constants which can be rigorously approximated to
arbitrary precision. As b2(z) is the only element of the {bj} basis that is singular
at z = w, the dominant singular term in the expansion of f(z) near z = w is
C2
p
z −ζ4 where
C2 = −
 
3.5933098558743233 . . .

+ i

0.38132214909311386 . . .

.
Thus, f(z) has a singularity at z = ζ4 and the asymptotic contribution of this
singularity to an,n,n,n is
Ψ1(n) =

4i
√
2 −7
n
n3/2
 
0.543449606382202 . . .

+ i

0.259547320313100 . . .

√π
+ O(9nn−5/2) .
Repeating the same analysis at the point z = ζ
4 gives an asymptotic contribu-
tion
Ψ2(n) =

4i
√
2 + 7
n
n3/2
 
0.543449606382202 . . .

−i

0.259547320313100 . . .

√π
+ O(9nn−5/2) ,
so that an,n,n,n has the asymptotic expansion an,n,n,n = Ψ1(n) + Ψ2(n).
Comparing this expansion to (11.18) gives two expressions for asymptotics:
one with complex coeﬃcients numerically determined to arbitrary precision
and another with undetermined coeﬃcients that are known to be integers. Since
one needs only 1 decimal digit to identify an unknown integer, combining these
expansions proves that the unknown integer κ = 3.
◁
11.4 Examples and consequences
379
Notes
Hyperbolicity, as deﬁned here, arose ﬁrst in the context of PDEs. If f is a com-
plex polynomial, let f(D) denote the corresponding linear partial diﬀerential
operator obtained by replacing each x j by ∂/∂x j. For example, if f is the stan-
dard Lorentzian quadratic x2
1−Pd
j=2 x2
j, then f(D) is the wave operator. Gårding
set out to investigate when the equation
f(D) u = g
with g supported on a halfspace has a solution supported in the same halfspace.
When f(D) is the wave operator, this is true and the solution is unique. It
turns out that the class of homogeneous polynomials f for which this is true is
precisely characterized as the hyperbolic homogeneous polynomials.
The concept of hyperbolicity was used in the study of lacunas by [ABG70]
to construct the deformations we have borrowed in this chapter. Later, the prop-
erty of hyperbolicity turned up in algebraic combinatorics under the name of
the real root property. Polynomials with this property are called real stable
polynomials. Hyperbolicity and real stability are linked to a wide range of the-
orems and conjectures, including the van der Waerden conjecture, the Strong
Rayleigh property, and the Kadison–Singer problem, solved in 2013 by Mar-
cus, Spielman, and Srivastava. The importance of these concepts seems to stem
from the closure of the class of real stable polynomials under a great many al-
gebraic and combinatorial operations, surveyed in [Wag11]. For polynomials
which are generating functions of joint distributions of binary variables, the
property implies a number of negative dependence properties, and this has re-
sulted in the solution of a number of outstanding conjectures in the theory of
negative dependence [BBL09]. Although Proposition 11.15 follows from the
conclusion (3.45) of [ABG70, Lemma 3.42], the self-contained proof provided
above is satisfying, and was told to the authors of [BP11] by J. Borcea (per-
sonal communication).
In this chapter, while we have mostly excerpted and condensed [BP11], we
have also taken the opportunity to correct some errors. The second implication
of Proposition 11.25 is proved in [BP11, Proposition 2.11], however the last
sentence of the cited result mistakenly claims a reverse implication (see Ex-
ercise 11.9). The implication in the wrong direction (ii) ⇒(iii) is then used
to prove Proposition 11.26, one of the key results original to [BP11, Proposi-
tion 2.12]. Our statement here of Proposition 11.25 corrects [BP11] by elim-
inating the mistaken reverse implication in [BP11, Proposition 2.11], and our
statement and proof of Proposition 11.26 derives [BP11, Proposition 2.12]
without using the mistaken converse in the previous result. Beyond this, the
380
Cone point asymptotics
ﬁrst sentence of the last paragraph of [BP11, page 3177], “We piece these to-
gether . . . with a partition of unity argument as before,” while not known to be
wrong, requires considerable justiﬁcation not provided there. While this will
be corrected in a forthcoming erratum, we have opted here to provide a more
direct ﬁx, Lemma 11.27 part (iii), whose hypotheses cover all the examples
we discuss in Section 11.4 except for one covered by a direct topological anal-
ysis. Part (iii) of Lemma 11.27 is used to amplify the problematic sentence
from [BP11] into an argument by cases consuming three paragraphs at the
end of the proof of Theorem 11.33; the lemma is used crucially in case (iii).
Most other results in Section 11.2 correspond to [BP11] as follows. Theo-
rems 11.4, 11.5, 11.33, and 11.42 above correspond to Lemma 5.1, Lemma
5.3, Theorem 5.8, and Lemma 6.8 of [BP11], respectively. Lemma 11.32 cor-
responds to [BP11, Theorem 5.6].
There is another possible approach to asymptotics governed by points other
than smooth and multiple points, namely resolution of singularities. A reso-
lution at a singular point z is a change of variables which is one-to-one away
from z and after which the local geometry at z is a normal crossing, that is, one
or more smooth, transversely intersecting sheets. Resolution of singularities
is eﬀective [BM97], however the phase function becomes highly degenerate,
complicating the integral substantially.
Additional exercises
Exercise 11.9. (weak hyperbolicity versus hyperbolicity of the homogeneous
part) Let f(x, y) = x2 + y3. Show that f is weakly hyperbolic in direction (0, 1)
at the origin but that hom( f, 0) = x2 is not hyperbolic in direction (0, 1).
Exercise 11.10. (tangent cones at a cubic point) Let f(x, y, z) = xy + z3. First,
compute a stratiﬁcation of the zero set V of f. The tangent cones to V at
(x, y, z) vary continuously as (x, y, z) moves within a stratum. Describe these,
then prove or disprove that there exists a lower semi-continuous choice of tan-
gent cone K(x, y, z) in some neighborhood of the origin.
Exercise 11.11. (Explicitly constructing the vector ﬁeld) Let f(x, y, z) = z2 −
x2 −y2 be the standard Lorentzian quadratic and let B = {(x, y, z) : z <
−
p
x2 + y2} be the cone of hyperbolicity for f containing the downward di-
rection. Let ˆr∗= e3, the elementary vector in the positive z-direction. Find a
projective vector ﬁeld v(y) such that for all y , 0, the function w 7→f(iy+w)
does not vanish on tu + (1 −t)v(y) for t ∈[0, 1]. You may use the proof of
Lemma 11.32 or provide a sketch.
