---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-059-proof-of-theorem-111
section_title: "Proof of Theorem 11.1"
section_number: null
pages: 365-379
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
347
one can simply take v3 = v2, but we mirror the general construction described
above). Hence,
η(θ1, θ2) = ψ1(θ1, θ2)v1 + ψ2(θ1, θ2)v2 + ψ3(θ1, θ2)v3
=

−ψ1 −ψ2 + ψ3/2 , −ψ1 + 2ψ2 + ψ3/2

,
where ψ1, ψ2, and ψ3 form a partition of unity subordinate to N1, N2, and N3,
and
Φt(θ1, θ2) = exp i(θ1, θ2) −(log 2, log 2) −δ(1 −t, 1 −t) + δtη(θ1, θ2)
for some δ > 0. When t = 1 and (θ1, θ2) ∈N1 then ψ2(θ1, θ2) = 0 since N1 and
N2 are disjoint. Thus, the cycle C in Corollary 11.10 is the image of N1 under
the map
Φ1(θ1, θ2) =
 1
2eiθ1 e−δψ1+δψ3/2, 1
2eiθ2 e−δψ1+δψ3/2
!
.
When (θ1, θ2) is suﬃciently close to the origin then it lies in N1 \ N3 and
Φ1(θ1, θ2) =
 1
2eiθ1 e−δ, 1
2eiθ2 e−δ
!
is contained in D. As (θ1, θ2) leaves the origin and approaches the boundary,
however, the coordinate-wise moduli of Φ1(θ1, θ2) increase, eventually leaving
D without intersecting V. Ultimately, we can apply the asymptotic arguments
for smooth points to analyze the integral near σ and obtain an expansion
fn,n =
4n
√πn
 1
2 −1
8n +
1
256n2 +
5
256n3 −
819
65536n4 + O
 1
n5
!!
.
◁
11.2 Proof of Theorem 11.1
In this section we prove Theorem 11.1. Our proof is split into the following
steps.
• In Section 11.2.1 we introduce the hyperbolicity of a homogeneous polyno-
mial and cones of hyperbolicity for a homogeneous polynomial. We show
how a family of cones of hyperbolicity for a homogeneous polynomial can
be deﬁned so as to vary semi-continuously. The deﬁnition of hyperbolicity
at this stage is valid only for homogeneous polynomials.
348
Cone point asymptotics
• In Section 11.2.2 we generalize to certain log-Laurent polynomials by deﬁn-
ing the cone of a function f at one of its zeros x + iy to be a choice of a
cone of hyperbolicity for the leading homogeneous part of f at x + iy. Our
constructions are well deﬁned only for certain values of x.
• Section 11.2.3 introduces notions of weak and strong hyperbolicity. The
weaker notion is equivalent to hyperbolicity of a homogenization, and the
main result of the section is that the stronger notion holds in similar circum-
stances.
• Section 11.2.4 establishes lower semi-continuity for a family of cones intro-
duced in Section 11.2.3.
• Section 11.2.5 completes the proof of Theorem 11.1.
• Section 11.2.6 extends the construction of the deformations Cδ in Theo-
rem 11.5 to a limiting log-linear deformation. This will be important later,
when computing integrals.
11.2.1 Cones of hyperbolicity in the homogeneous case
The following deﬁnition of hyperbolicity, originally developed in order to clas-
sify and study wavelike second-order partial diﬀerential equations, goes back
to [Går50].
Deﬁnition 11.12 (hyperbolicity). A homogeneous complex polynomial A of
degree m ≥1 is a hyperbolic polynomial in the direction v ∈Rd if A(v) , 0
and for all x ∈Rd the polynomial t 7→A(x + tv) has only real roots. A
seemingly weaker but actually equivalent condition is that A(v + iy) , 0 for
all y ∈Rd.
The set of v for which A is hyperbolic in direction v is an open set whose
components are convex cones in Rd, and each of these cones is called a cone
of hyperbolicity for the homogeneous polynomial A. Denote by Kv(A) the
cone of hyperbolicity of A containing a given vector v. Some multiple of A is
positive on Kv(A) and vanishing on ∂Kv(A), and for x ∈Kv(A) the roots of
A(x+tv) will all be negative. These properties are proved, among other places,
in [G¨ul97, Theorem 3.1].
Example 11.13 (hyperbolicity of a linear function). If A(x) = v · x is a real
linear function then its cones of hyperbolicity are the halfspaces {x ∈Rd :
v · x > 0} and {x ∈Rd : v · x < 0}.
◁
Example 11.14 (hyperbolicity of a quadratic function). If A(x) = x2
1 −Pd
j=2 x2
j
is the standard Lorentzian quadratic then its cones of hyperbolicity are the
11.2 Proof of Theorem 11.1
349
so-called positive and negative time-like cones
C+ =

x ∈Rd : x1 >
q
x2
2 + · · · + x2
d

and
C−=

x ∈Rd : x1 < −
q
x2
2 + · · · + x2
d

.
◁
The following proposition and deﬁnition deﬁne the ﬁrst version of the cones
of hyperbolicity that will ultimately lead to the family of cones in Theorem 11.1.
Proposition 11.15. Let A be a homogeneous polynomial, ﬁx x with A(x) = 0,
and let ˜A = hom(A, x) denote the leading homogeneous part of A at x. If A
is hyperbolic in the direction u then ˜A is also hyperbolic in the direction u.
Consequently, if C is any cone of hyperbolicity for A then there is some cone
of hyperbolicity for ˜A that contains C.
Proof
If P is a polynomial of degree k then we can recover its leading homo-
geneous part hom(P) by
hom(P)(y) = lim
λ→∞λkP(λ−1y) .
This limit is uniform as y varies over compact sets, since monomials of degree
k are invariant under the scaling on the right-hand side, while monomials of
degree k + j scale by λ−j, uniformly over compact sets. Thus, in our situation
˜A(y + tu) = lim
λ→∞λkA(x + λ−1(y + tu))
uniformly as t varies over compact sub-intervals of R. If A is hyperbolic in
direction u then, for any ﬁxed λ, all the zeros of this polynomial in t are real.
Hurwitz’s Theorem on the continuity of zeros [Con78b, Corollary 2.6] says
that a (uniform on bounded intervals) limit of polynomials having all real zeros
will either have all real zeros or vanish identically. The limit ˜A(y + tu) has
degree k ≥1; it does not vanish identically, so if A is hyperbolic in the direction
u then ˜A has only real roots and is also hyperbolic.
□
Deﬁnition 11.16 (family of cones in the homogeneous case). Let A be a ho-
mogeneous polynomial and let C be a cone of hyperbolicity for A. If A(x) = 0
then we deﬁne KA,C(x) to be the cone of hyperbolicity of hom(A, x) containing
C, whose existence we have just proved. If A(x) , 0 then we deﬁne KA,C(x)
to be all of Rd.
Remark 11.17. When x , 0 the cone KA,C(x) depends only on the direction
bx = x/|x|.
350
Cone point asymptotics
Example 11.18. Let S (x) = x2
1 −x2
2 −· · · −x2
d be the standard Lorentzian
quadratic and let C = C+ be the cone of hyperbolicity at the origin described
in Example 11.14. For x ∈∂B, if x , 0 then KS,C(x) is the tangent halfspace
{x + y : y · (∇S )(x) ≥0}. If x = 0 then KS,C(x) = C. A Lorentzian quadratic
is a quadratic polynomial obtained from S by a real linear transformation. The
boundary of the cone of hyperbolicity for any Lorentzian quadratic is an alge-
braic tangent cone and the cones of hyperbolicity at these points are halfspaces
whose boundaries are support hyperplanes to time-like cones.
◁
Exercise 11.4. Describe the two cones of hyperbolicity of A(x, y) = x + y at
(x, y) = (5, −5) and, letting C denote one of these cones, ﬁnd KA,C(5, −5).
11.2.2 Cones of hyperbolicity in the general case
Although the deﬁnition of hyperbolicity in the homogeneous case is valid for
complex polynomials and involves complex roots, the role played by the real
subspace is essential. In this section we generalize by deﬁning cones of hyper-
bolicity Kq,B(z) for functions q = Q ◦exp where Q is a Laurent polynomial.
Our deﬁnitions are valid only at points z = x + iy for some x on the boundary
of a component B of the complement of amoeba(Q). We do not know whether
Kq,B(z) may be deﬁned in such a way that semi-continuity results still hold
when z is not on the amoeba boundary, or when q is not a log-Laurent polyno-
mial.
Deﬁnition 11.19 (hyperbolicity and normal cones). Let Q be a Laurent poly-
nomial, let B be a component of Rd\amoeba(Q), and let exp(z) = exp(x+iy) ∈
VQ with x ∈∂B. If q = Q ◦exp then we deﬁne
K(z) = Kq,B(z) = Ku(hom(q, x + iy)) for any u ∈B
(11.6)
to be the (open) cone of hyperbolicity of A = hom(q, x + iy) that contains B.
The existence of this cone is guaranteed by Proposition 11.26 below.
Remarks.
(i) Deﬁning Kq,B using hom(q, x+iy) may seem obvious, but the
diﬃculty proving properties in this case illustrates that the extension is
quite non-trivial.
(ii) We may extend the deﬁnition of K to all of T(x) by taking K(z) = Rd
when q(z) , 0.
(iii) When z = x + iy and x is understood, we sometimes write Kq,B(y).
Before going further we give a few examples.
Example 11.20 (cones of hyperbolicity at smooth points). Suppose exp(z) =
11.2 Proof of Theorem 11.1 351

exp(x + fy) is a minimal smooth point of Vg. Then the leading homogeneous
part g of q at z is a linear function g(a) = v - x, and the assumption of min-
imality implies that the vector v is a complex scalar multiple of a real vector.
As in Example 11.13 above, the cones of hyperbolicity of g at z are halfspaces
normal to v. 4

Example 11.21 (cones of hyperbolicity at multiple points). Suppose exp(z) =
exp(a + iy) is a multiple point of Vg. Then @ is a product of linear functions
defining a central hyperplane arrangement. The normal vectors to the factors
of g are scalar multiples of real vectors and the corresponding real hyperplanes
divide R¢ into projective cones, each of which is a cone of hyperbolicity for

q- 4

Exercise 11.5. Let Q = (1 — 2x -— y)(1 — x — 2y). What are the cones of hyper-
bolicity K(z) when z = exp(1/3, 1/3)? What about when z = exp(1/4, 1/2)?

Example 11.22 (cones of hyperbolicity at quadratic cone points). If O(a) =
zt - Din Fa is the standard Lorentzian quadratic then at the origin g has the
two cones of hyperbolicity C, and C_ discussed above, while the cones of
hyperbolicity of g at any other point are two halfspaces. 4

11.2.3 Strong and weak hyperbolicity

To prove the existence result Proposition 11.26 and the semi-continuity result
Lemma 11.27, we define intermediate notions of strong and weak hyperbol-
icity. These definitions are somewhat less natural than those above, and are
not used for any other purpose, so readers not interested in the proofs of our
semi-continuity results may safely skip to Section 11.2.5.

Definition 11.23 (strong and weak hyperbolicity). Let g : C4 > C vanish
at z and be holomorphic in a neighborhood of z. We say that q is strongly
hyperbolic at z in the direction of the unit vector 6 if there is an ¢ > 0 such
that g(z + tv’ + iu) # 0 whenever 0 < f < «, the vector v’ is at distance at
most € from 6, and u € R@ has magnitude at most ¢. The supremum of the
e for which this holds is called the radius of strong hyperbolicity at z in the
direction 6. We say that g is weakly hyperbolic in the direction 6 if for every
M > O there is an € > O such that g(z + t6 + iu) # 0 whenever 0 < 16| < €

and u € R@ has magnitude at most ¢ with a <M.

Proposition 11.24. The radius of strong hyperbolicity is Lipschitz continuous
with constant 1. Thus, for fixed x strong hyperbolicity at z = x + ty in the
direction 6 is a neighborhood property in y and 6.
352 Cone point asymptotics

Proof Suppose that q is strongly hyperbolic at a + iy in direction 6 with
radius ¢ and choose y’ and 6’ with max{|y’ — y|,|6’ — d|} = 6 < «. It follows
from the definition that g is strongly hyperbolic at y’ in direction 6’ with radius
at least e — 6. Hence the radius function R(y, 6) for g over x is Lipschitz in
both arguments with constant at most 1. In particular, g is continuous in both
arguments and the set of (y, v) for which q is strongly hyperbolic is open. O

As mentioned in the end of chapter notes, the next two propositions correct
the statement of [BP11, Proposition 2.11] and the proof of [BP11, Proposi-
tion 2.12].

Proposition 11.25. Let g = Q 0 exp with Q a Laurent polynomial, fix z =
a+iy, and let A = hom(q, z) be the leading homogeneous term of q(z + w) in
w. Then each of the following properties implies the next.

(i) Strong hyperbolicity of q at z in the direction 6.
(ii) Hyperbolicity of A in the direction 6.
(iii) Weak hyperbolicity of q at z in the direction 6.

Proof Assume without loss of generality that z = 0.

For the contrapositive of the first implication, suppose that A is not hyper-
bolic in direction 6. Then there is u € R¢ such that A(@ + iw) = 0. Because
the tangent cone is the limiting secant cone, by Lemma 6.48 there are two
Un, Wn Sequences of vectors going to zero in R¢ such that qn + iWn) = 0,
with v,,/|v,| > 6 and w,/|v,| > u. This contradicts the definition of strong
hyperbolicity.

For the second implication, suppose that g is not weakly hyperbolic at the
origin in direction 6. This means there is some M > 0 such that for any ¢ > 0
there are t € (0,€) and u € R¢ with |u| < M such that g(t(é + iu)) = 0.
By compactness of the ball of radius M, this is equivalent to the existence of
sequences of real numbers ¢, and vectors u, such that t, > 0, u, > u and
q(t,(6 +iu,)) = 0. Again, because the tangent cone is the limiting secant cone,
this implies A(é + iw) = 0, meaning A is not hyperbolic in direction 0. oO

Proposition 11.26. Let Q be a Laurent polynomial, let B be a component of
amoeba(Q), and let x € OB, so that q = Qo exp vanishes at some point
z=a+iy. Fix u € tan,(B) and let g = hom(q, x + iy) denote the leading
homogeneous part of q(a + iy + w) with respect to w. Then

(i) q is strongly hyperbolic at z in direction u;
(ii) Gis hyperbolic in direction u;
(iii) K“(@) contains tanz(B);
(iv) some complex scalar multiple of g is real.
11.2 Proof of Theorem 11.1
353
Proof
Begin by observing a property of tangent cones in real space: if a unit
vector ˆv is in tanx(B) and vn →0 with vn/|vn| →ˆv then x + vn ∈B for
suﬃciently large n. Strong hyperbolicity of q in any direction u ∈tanx(B)
then follows from the deﬁnitions of strong hyperbolicity and B.
To derive the second conclusion, suppose for contradiction that ˜q is not
hyperbolic in unit direction u ∈Rd, meaning that ˜q(u + iθ) = 0 for some
θ ∈Rd. Because the algebraic tangent cone is the limiting secant cone by
Lemma 6.48, there must be sequences of real vectors {αn} and {βn} such that
(αn + iβn)/|αn + iβn| →(u + iθ)/|u + iθ| and ˜q(z + αn + iβn) = 0. Because
αn →0 with αn/|αn| →u, the above observation with vn = αn shows that
x + αn ∈B for all suﬃciently large n. But B is in the complement of the
amoeba, contradicting ˜q(z + αn + iβn) = 0 and proving hyperbolicity of ˜q in
direction u.
The third conclusion, Ku(˜q) ⊇tanx(B), follows immediately. For the ﬁnal
conclusion, ﬁx any non-zero real vector ξ. Then ˜q(ξ + tu) is a polynomial
of degree m with leading coeﬃcient ˜q(u) and constant term ˜q(ξ). The ratio
˜q(ξ)/˜q(u) is (−1)m times the product of all the roots. By deﬁnition of cones of
hyperbolicity, all the roots are real, therefore ˜q(ξ)/˜q(u) is real. Because ξ was
arbitrary, we conclude that ˜q(x)/˜q(u) maps Rd to R.
□
11.2.4 Semi-continuity
Near any point in any stratum of a complex algebraic variety there are one
or more cones contained in the complement of the variety. Hyperbolicity may
be thought of as a kind of orientability for families of such cones, ensuring a
consistent choice of “inward tangent cone” (see Exercise 11.10 for a related
perspective). This provides some intuition as to why it’s easier to deﬁne hy-
perbolicity for minimal points, since the meaning of “inward” can be inferred.
Hyperbolicity is also used to ensure the cones are convex.
Aiming at conclusion (iv) of Theorem 11.1, we quote and brieﬂy outline
proofs of the following semi-continuity results from [BP11, Theorem 2.14 and
Corollary 2.15], which are also discussed in [ABG70, Lemma 3.22] and [Går50;
H¨or83].
Lemma 11.27 (semi-continuity).
(i) Let A be a homogeneous polynomial
and C a cone of hyperbolicity for A. Then the cone KA,C(y) is lower
semi-continuous in y.
(ii) Let q = Q ◦exp for some Laurent polynomial Q, let B be a component
of the complement of amoeba(Q), and let x ∈∂B. Then Kq,B(z) is lower
semi-continuous as z varies over T(x).
354
Cone point asymptotics
(iii) With q as in (ii) and ˜q = hom(q, z) for ﬁxed z, suppose further that for u
in some cone of hyperbolicity K of ˜q corresponding to the component B
of amoeba(Q)c,
q(z + iy + su) , 0 for real non-zero s in some interval [−c, c] and all y .
(11.7)
Then
KA,B(z +by) ⊆lim inf Kq,B(z + yn)
as yn →0 with yn/|yn| →by.
Remark 11.28. The ﬁrst conclusion in Lemma 11.27 is nearly a specialization
of the second conclusion to homogeneous functions, except that not every ho-
mogeneous function is the homogenization of a Laurent polynomial composed
with the exponential function. Assumption (11.7) is satisﬁed whenever a gener-
ating function is symmetric under mapping all coordinates to their reciprocals.
This seems to be a common feature of recursions arising from cluster algebras.
In particular, this is true for the quadratic cone functions (Aztec diamond, cube
grove, fortress) arising later in this chapter, as well as their products with bino-
mial such as (1 −yz). Though not symmetric under reciprocals, the spacetime
generating function for quantum walks also satisﬁes Assumption (11.7) as a
consequence of the deﬁning matrix being unitary.
Proof Sketch
Suppose an analytic function q is strongly hyperbolic in the
direction v at the point z = x + iy and let A = hom(˜q, z). Theorem 2.14
of [BP11] implies that if u ∈Kv(q) then q is strongly hyperbolic in direction
tv + (1 −t)u for any t ∈[0, 1]. The ﬁrst two conclusions follow from this, and
are stated as [BP11, Corollary 2.15].
To prove (iii), let m be the lowest homogeneous degree of ˜q and write q =
˜q+R with R analytic and vanishing to degree m+1 at the origin. By our choice
of u we know ˜q(u) , 0, and by homogeneity we know that ˜q(su) = sm ˜q(u).
Using the Weierstrass Preparation Theorem, then expanding, gives
q(z + su) = h(z)

sm + a1(z)sm−1 + · · · + am(z)

(11.8)
= h(z)
m
Y
k=1
(s + µk(z, u)) ,
(11.9)
where h, a1, . . . , am are holomorphic functions of z with all aj vanishing at the
origin, h does not vanish at the origin, and the roots −µk(z, u) tend to zero as
z →0. Specializing to some line z = tv, we write (with a slight abuse of
11.2 Proof of Theorem 11.1 355

notation)
f(tv + su) = A(t) [|e + (0).
k=1

We claim that the ju;,(t) are real analytic functions of ¢ in a neighborhood
of 0. To see this, write uz, as a Puiseux series Y),c4, Crxt’, where Ax is an
arithmetic progression of rational numbers, containing positive entries because
lim,o 44x(t) = 0. Suppose some exponent r € A, is not an integer, and let b be
the denominator of the least non-integral r ¢ Ay. Then either for ¢ small and
positive, or t small and negative, there will be b roots with arguments asymp-
totically distributed as {2/b + 22j/b : 0 < j < b— 1}, one of which is non-real,
contradicting the real-rootedness of g(i(y + zu)). We have thus established our
claim that the 44 are real functions of t.

It follows that j,(t) ~ ta,(t), where 2, are the slopes of the lines into which
the bivariate function g(tv + sw) factors,

G(tv + su) = G(u) [|e + ta(t)).
k=1

When v is chosen in the same cone of hyperbolicity as u, this further implies
that all A, are positive and that j are increasing functions of f in a neigh-
borhood of 0. This is sufficient to derive, in the same manner as [ABG70,
Lemma 5.1, 5.9], that the local branches ju; are still increasing after perturba-
tion, which implies semi-continuity of the cones. ia)

Example 11.29. Suppose that exp(z) is a multiple point of Q, so that the
leading homogeneous part g of q at exp(z) is the product of linear factors. The
cones of hyperbolicity of g at z are projective cones that are the components
of R¢ when the hyperplanes on which the linear factors vanish are removed.
If ¢g = Qo exp, where @Q has only multiple point singularities and {z,} is a
sequence with exp(z,) > exp(z) in Vg while remaining in a single stratum
S, then exp(z) is in either S or OS. In the latter case, the partition near exp(z)
of R¢ into projective cones is finer at exp(z) than at the points exp(z’), and the
semi-continuity described in Lemma 11.27 is strict. 4

Exercise 11.6. Let X be a Whitney stratified space and let m : X — Zyo be
the dimension function m(a) = dim(S(a)). Is m lower semi-continuous, upper
semi-continuous, or neither?

11.2.5 Proof of Theorem 11.1

We now complete the proof of Theorem 11.1.
356
Cone point asymptotics
Proof
For every y ∈Tﬂat, deﬁne
Z(y) = Kq,B(x∗+ iy) = Ku(hom(q, x∗+ iy)),
where u is any vector in tanx∗(B). By Proposition 11.26 this cone contains
tanx∗(B), establishing conclusion (i) of Theorem 11.1. Conclusion (iv) is part
of the conclusion of Lemma 11.27. For conclusion (iii), ﬁrst suppose that z =
exp(x∗+ iy) is not a stratiﬁed critical point for h ˆr on V. Pulling back by
the exponential map, we see that x∗+ iy is not a critical point for the log-
linear map ˆr(w) = ˆr · w on the stratum S of exp−1[V] containing x∗+ iy.
Thus d(h ˆr ◦exp)|S , 0, meaning that ˆr is not orthogonal to the tangent space
Tx+iy(S ), so ˆr < N(y). By the contrapositive, this establishes the ﬁrst part of
conclusion (iii). Conversely, if ˆr < N(y) then since N(y) = (−Z(y))∗there
is some v ∈Z(y) with ˆr · v > 0. The cone Z(y) is projective, so v can be
normalized so that ˆr · v = 1.
To prove conclusion (ii), begin by ﬁxing t, x, and y. By Proposition 11.26, q
is strongly hyperbolic at x+iy in any direction u ∈tanx∗(B) with some radius
ε(u, y) > 0 that is Lipschitz-1 continuous in both arguments. This is (11.1)
with t and y ﬁxed, u = u(t, y) taken to be t⃗V(y) + (1 −t)(x −x∗), and ε set to
ε(u(t, y), y). Let (t, y) vary over the compact set [0, 1]×Tﬂat and use continuity
to see that ε(u(t, y), y) ≥ε0 > 0 for some ε0 and all (t, y). Equation (11.1) is
then satisﬁed for any δ ≤ε0.
□
11.2.6 Projective deformations
This section address a special but reasonably common case where the dominant
critical point z = exp(x + iy) governs a set of coeﬃcient asymptotics whose
directions N(z) form a set with non-empty interior. Because N(z) is a subset
of the lognormal space to the stratum containing z, this implies the stratum is
the 0-dimensional singleton {z}. The prototypical examples are quadratic cone
points, with or without additional linear divisors passing through the cone point
(Aztec diamond, cube groves), as well as the other applications mentioned in
the preliminary section of this chapter: Szeg˝o functions, the GKZ symmet-
ric rational functions, and the Kauers-Zeilberger 4-variable function. Looking
ahead at Figures 11.2 and 11.3 may help to give a mental picture of the variety
and the deformations used. A quick outline of this section and the next goes as
follows.
(i) For a hyperbolic homogeneous polynomial ˜q, construct a deformation
from the imaginary ﬁber u+iRd over a point u in a cone of hyperbolicity
K to a projective contour: a set closed under multiplication by positive
11.2 Proof of Theorem 11.1
357
real numbers. We will apply this in logarithmic space to the function
˜q = hom(q, x + iy) where q = Q ◦exp and exp(x + iy) is a minimal
point of V. The deformation will avoid the zero set V˜q of ˜q except for
touching it at a single point (the origin) at a single time (t = 1). This step
is accomplished by Lemma 11.32.
(ii) Letting q = Q ◦exp, we apply Step (i) to the homogenization ˜q of q near
each point x+iy with y ∈localarg (so that exp(x+iy) is a critical point
in direction ˆr∗for Q and ˆr∗lies in the normal cone there). We then use
a partition of unity to piece these local log-projective contours together
with the one from Theorem 11.4. This is accomplished in Theorem 11.33,
resulting in a deformation of the contour that avoids Vq except at t = 1
with y ∈localarg and is projective in a neighborhood of localarg.
(iii) We stop the homotopy a bit early near localarg in order to obtain a cy-
cle that avoids Vq = log V entirely. This is discussed in Deﬁnition 11.34.
(iv) In the next section, we will see that on the domains of integration of
interest any rational function F = P/Q has local expansions in powers of
1/A, where A is a homogenization of Q. This leads to a powerful theorem
showing the asymptotics in this case to be given essentially by the Fourier
transform of ˜q.
As above, assume we have ﬁxed Q along with a component B of amoeba(Qc)
and a point x ∈∂B, let q = Q◦exp, and ﬁx a point x+iy0 where q vanishes. We
assume without loss of generality that y0 = 0, with everything in this section
working equally well for any non-zero y0 ∈Tﬂat. Because we want a log-
projective contour, we work mainly in logarithmic coordinates. The log space
L = Rd ⊕i(R/2π)d is a discrete quotient of Rd ⊕iRd, so for analyses taking
place in a suﬃciently small neighborhood in L it makes sense to consider the
computations in Cd. In particular, while q is not a polynomial on the log space
L, it is analytic at x and its leading homogeneous term λ˜q is a complex scalar
multiple of a real homogeneous polynomial ˜q of the same degree as the leading
homogeneous part of q(x + iy + w) in w. Let V˜q denote the zero set of ˜q.
Because the homogeneous polynomial ˜q is hyperbolic with some cone of hy-
perbolicity K0 containing tanx(B), Deﬁnition 11.16 and part (i) of Lemma 11.27
imply the existence of a lower semi-continuous family of real cones K˜q,B(y)
of hyperbolicity for the homogenizations of ˜q at y as y varies, with all cones
containing tanx(B). For y < V˜q, the cone K˜q,B(y) may be taken to be all of
Rd. By homogeneity, K˜q,B(λy) = K˜q,B(y) for any real λ > 0.
Deﬁnition 11.30. Recall the normal cone normalx(B) = −tanx(B)∗. We say
358
Cone point asymptotics
Figure 11.2 Left: A variety V = VQ. Right: The corresponding variety log V =
Vq.
that a direction ˆr in the interior of normalx(B) is a non-obstructed direction
if for any y ∈V˜q the cone K˜q,B(y) contains a vector v with ˆr · v > 0.
Note that obstruction is a property of the homogenization ˜q.
Lemma 11.31. Suppose that ˆr∗is a non-obstructed direction in the interior of
normalx(B). Then there is a 1-homogeneous vector ﬁeld η on Rd, vanishing
and continuous at the origin and smooth elsewhere, such that η(y) ∈K˜q,B(y)
and ˆr · η(y) ≥| ˆr||y| for all y ∈Rd and all ˆr in a neighborhood of ˆr∗.
Proof
It suﬃces to deﬁne η smoothly on the set of unit vectors, then extend
by η(λy) = λη(y): this extension will be smooth away from the origin and
continuous at the origin, and if ˆr · η(y) is positive on the unit ball then the
inequality in the conclusion of the lemma follows.
By the deﬁnition of non-obstruction, there is always a v depending on y
with v ∈K˜q,B(y) and v · ˆr > 0. Because of the strict inequality and semi-
continuity of the cones, this same vector v works for nearby ˆr′ and nearby y′.
One may therefore cover the unit ball with ﬁnitely many open sets on which v
may be taken to be a constant. Construct η from these by a partition of unity,
noting that convex combinations preserve both v · ˆr > 0 and v ∈K˜q,B(y).
□
We ﬁnish step (i) of our outline by ﬁnding a projective deformation with
the required properties. To accomplish step (ii) we then piece these together
for ﬁnitely many values of y0 and form a single deformation. We introduce
a parameter ε that shrinks the entire deformation so that we can later keep a
piece of it close to the origin.
Lemma 11.32. Let A be a hyperbolic homogeneous polynomial with cone of
hyperbolicity K. Let ˆr∗be a ﬁxed non-obstructed direction in the interior of the
11.2 Proof of Theorem 11.1
359
normal cone −K∗, and let η be the projective vector ﬁeld from Lemma 11.31.
For ε > 0 and ﬁxed u ∈K, let Φt be the homotopy from Rd × [0, 1] into Cd
deﬁned by
Φt(y) = Φε,u,η
t
= iy + ε (1 −t)u + tη(y) .
(11.10)
Then there exists c > 0 such that ˆr · Φ1(y) ≥c|y| for all y as ˆr varies over
some neighborhood of ˆr∗. Furthermore, A(Φt(y)) , 0 for all 0 ≤t ≤1 except
when t = 1 and y = 0. Consequently, the chain u + iRd is homotopic in the
complement of VA to the projective chain C = Φ1[Rd] on which ˆr · y grows
linearly in |y|, uniformly when ˆr varies over some neighborhood N of ˆr∗.
Remark. The parameter ε that shrinks the deformation toward x + iy has
no consequence in Lemma 11.32, but will be useful later when we want the
homotopy to avoid a function f whose homogenization is A.
Proof
By deﬁnition of cones of hyperbolicity for homogeneous functions,
˜q(Φt(y)) cannot vanish except if y = 0 and t = 1. The rest is Lemma 11.31
and the deﬁnition of Φt in (11.10).
□
The next step is to glue together constructions in a neighborhood of log
space L near each point of localarg( ˆr∗). We solve several problems at the
same time. First, in order to remain in M we stop the homotopy slightly before
t = 1 when y is near the set localarg( ˆr∗). Second, we do this construction
simultaneously for all w ∈localarg( ˆr∗), gluing together the constructions in
these neighborhoods with a standard construction outside of these neighbor-
hoods. Third, we do this in small neighborhoods of Rd that can be identiﬁed
with neighborhoods in L so as to cover the space, thus ensuring that mapping
forward by the exponential map produces a homotopy of the torus to a contour
that is loglinear, with height −ˆr∗· x decreasing linearly on the contour with
distance from the nearest point in local( ˆr∗) and has height bounded above by
−x· ˆr∗−c outside of these neighborhoods for some positive constant c. Fourth,
we ensure that the homotopy remains in M. Finally, we take the opportunity
to correct the double duty played by the parameter δ in [BP11, Section 5]: we
will use the subscript ρ when restricting a chain to a neighborhood of radius ρ
and keep a superscript δ for how early to stop the homotopy and how near to
localarg to stop it. We always choose δ < ρ, ensuring the contour looks like
Figure 11.3.
Theorem 11.33 (local projective deformation). Let B be a component of the
complement of amoeba(Q). Suppose Q satisﬁes conclusion (iii) of Lemma 11.27
and that −ˆr∗·x is minimized on B uniquely at some point x ∈∂B. Assume fur-
ther that local( ˆr∗) is ﬁnite and that ˆr∗is a non-obstructed direction in the
360
Cone point asymptotics
interior of N(z) for each z ∈local( ˆr∗). Fixing x + u ∈B, there is a vector
ﬁeld η : Tﬂat →Rd and an ε > 0 such that the following are true.
(i) η is a smooth section of Kq,B.
(ii) For each y ∈localarg( ˆr∗), the vector ﬁeld η(y + ·) is 1-homogeneous
in a neighborhood of 0.
(iii) There is an ε > 0 such that the homotopy Φt = Φε,u,η
t
avoids log V except
at t = 1 and y ∈local( ˆr∗).
(iv) There is a constant c > 0 and a neighborhood R of ˆr∗such that −ˆr ·
η(w) < −c|w −y| for every w in some neighborhood of each y ∈
local( ˆr∗) and every ˆr ∈R.
Proof
We glue together vector ﬁelds on Tﬂat in small balls around each point
using a partition of unity. Fix ρ > 0 to be determined later. For a point y ∈
localarg( ˆr) deﬁne N(y) to be the ball of radius ρ centered at y, and deﬁne
the vector ﬁeld⃗Vy on N(y) to be the projective vector ﬁeld η from Lemma 11.31
for the homogenization of ˜q at y. Suppose now that y < localarg( ˆr∗). As in
the proofs of Theorems 11.4 and 11.5, we pick a vector v in the cone Z(y) from
Theorem 11.1 such that v · ˆr ≥1 for every ˆr ∈R. Deﬁne the vector ﬁeld⃗Vy(·)
to be the constant vector v on a neighborhood N(y) of y suﬃciently small
to avoid local( ˆr) for every ˆr ∈R, to avoid proper substrata of the stratum
containing y, and such that v ∈Z(y′) for every y′ ∈N(y).
We now have neighborhoods N(y) and vector ﬁelds⃗Vy on N(y) chosen for
all y ∈Tﬂat whether or not y ∈localarg( ˆr∗). Fix a subcover {N(w) : w ∈E}
indexed by some ﬁnite set E. Choose a partition of unity {ψw} subordinate to
this cover and deﬁne the vector ﬁeld η : Tﬂat →Rd by
η(y) =
X
w∈E
ψw(y)⃗V(w) ,
mirroring the deﬁnition of⃗V in (11.2).
Conclusion (i) is immediate from the partition of unity construction and the
fact that η was built from vectors⃗Vw(y) ∈Z(y) for w < localarg or⃗Vw(y) ∈
K˜q,y ⊆Z(y) for w ∈localarg, provided that ρ was chosen suﬃciently small;
see part (iii) of Lemma 11.27. Conclusions (ii) and (iv) are immediate from the
conclusion of Lemma 11.31 and the fact that each element of local( ˆr∗) is
forced to be in E. We prove Conclusion (iii) in three cases.
The easiest case occurs when y is not in N(w) for any w ∈local( ˆr∗).
Then by convexity η(y) ∈Z(y) and we already know Conclusion (iii) for
such y from Conclusion (ii) of Theorem 11.1. The second case occurs when
y ∈N′(w) = N(w) \ S
w′,w N(w′) for some w ∈local( ˆr∗). Then η is
deﬁned as in Lemma 11.31 applied to the homogenization A of ˜q near w. We
