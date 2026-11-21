---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-043-computing-critical-points
section_title: "Computing critical points"
section_number: null
pages: 244-253
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
The results of Chapter 7 illustrate that the main objects involved in our asymp-
totic analysis are the critical points of F in directions r. In order to describe
the critical points of F, we must ﬁrst decompose the singular set V of F into
a Whitney stratiﬁcation. Recall from Section 7.3 (or Appendix D) that this is a
partition of V into smooth manifolds of various dimensions satisfying speciﬁc
conditions on how they ﬁt together.
8.2.1 Eﬀective Whitney stratiﬁcation
The algebraic set V(Q) = V( ˜Q) forms the singular variety V. Lemma 7.6
from Chapter 7 implies that the algebraic set W1 deﬁned by the polynomial
system
˜Q(z) = ˜Qz1(z) = · · · = ˜Qzd(z) = 0
(8.1)
8.2 Computing critical points
227
encodes the points where V is not a smooth manifold. In particular, if a Gr¨obner
basis of the ideal I = ⟨˜Q, ˜Qz1, . . . , ˜Qzd⟩contains the element 1 then W1 = ∅, so
V is everywhere a smooth manifold and a Whitney stratiﬁcation of V is just
V itself.
Remark 8.7. The algebraic Sard Theorem [BPR03, Theorem 5.56] states that
V is generically a manifold, which is unsurprising as (8.1) contains d + 1
polynomial equations in d variables; see also [Mel21, Section 5.3] for an ele-
mentary derivation in our context.
If W1 is nonempty, then it is an algebraic set whose dimension is smaller
than the dimension of V. The singularities of W1, in turn, form an algebraic
set W2 of dimension smaller than the dimension of W1. Thus, we can obtain
a nesting of structures
V = W0 ⊋W1 ⊋W2 ⊋· · · ⊋Wr = ∅
such that each diﬀerence Wk \ Wk+1 is a smooth manifold. The polynomials
deﬁning the algebraic set Wk+1 can be computed recursively from the poly-
nomials deﬁning Wk using algorithms for ideal dimension and prime decom-
position, and the Jacobian Criterion [Eis95, Corollary 16.20] for singularity.
Since V is the union of all consecutive diﬀerences Wk \ Wk+1, this gives a
partition of V into smooth manifolds.
Although conceptually simple, this approach does not, in general, compute
a Whitney stratiﬁcation of V. Thankfully, there is a Whitney stratiﬁcation of
the same form. In the early 1980s, Teissier [Tei82, Proposition VI.3.2] proved
the existence of the canonical Whitney stratiﬁcation of V, deﬁned by a nested
sequence of algebraic sets
V = F0 ⊋F1 ⊋F2 ⊋· · · ⊋Fm = ∅
(8.2)
such that the set of all connected components of Fk \ Fk+1 for all k form
a Whitney stratiﬁcation of V and every Whitney stratiﬁcation of V is a re-
ﬁnement of this canonical stratiﬁcation. Older algorithms to compute Whitney
stratiﬁcations use quantiﬁer elimination and cylindrical algebraic decomposi-
tion [Ran98; MR91], while recent work [DJ21; HN22] gives more practical
algorithms1 based around Gr¨obner basis computations.
Remark 8.8. All combinatorially interesting multivariate generating functions
that the authors have encountered in the literature have Whitney stratiﬁcations
that can be computed directly by hand. Often, this is because V is either a
1 Helmer and Nanda [HN22] give Macaulay2 implementations at
http://martin-helmer.com/Software/WhitStrat/.
228
Eﬀective computations and ACSV
smooth manifold or can be expressed as the union of smooth manifolds in-
tersecting transversely. However, even in applications with more complicated
singularities, such as the isolated quartic singularity of Example 11.47, a Whit-
ney stratiﬁcation is obvious from inspection.
Example 8.9. Recall the generating function
F(x, y) =
X
r,s≥0
arsxrys =
xy(1 −x)3
(1 −x)4 −xy(1 −x −x2 + x3 + x2y)
from Example 12.23. The singular variety V admits a Whitney stratiﬁcation
with strata {p} and V \ {p} where p = (1, 0).
◁
8.2.2 Critical point equations
From now on we assume that we have the canonical Whitney stratiﬁcation (8.2)
of V, computed either by a computer algebra system or by hand. For each
1 ≤k ≤m let Ik denote the set
Ik = {f ∈K[z] : f(z) = 0 for z ∈Fk}.
Exercise 8.3. Prove that, for each k, the set Ik is an ideal with Ik = √Ik.
Fixing a value of k ∈{0, . . . , m −1}, our goal is to compute polynomial
equalities and inequalities characterizing the critical points on each connected
component of Fk \ Fk+1 = V(Ik) \ V(Ik+1). First, we use a Gr¨obner basis based
algorithm to compute the prime decomposition Ik = P1 ∩· · · ∩Pℓ. Because all
points in an intersection V(Pi) ∩V(Pj) with i , j are non-smooth points of
Fk, they are contained in Fk+1. This means we can compute the critical points
on the zero set V(Pj) of each prime ideal in the decomposition of I, remove
the points of Fk+1, then take the union of these sets.
The dimension δ of the prime ideal Pj can be computed using a Gr¨obner
basis algorithm, from which we can compute the codimension c = d−δ. If Pj =
⟨p1, . . . , ps⟩then, after translation to the origin, the tangent space to V(Pj) at
each smooth point p ∈V(Pj) is the codimension c linear subspace of Cd
normal to all of the gradients (∇p1)(p), . . . , (∇ps)(p); see Mumford [Mum95,
Section 1.A].
Recall the logarithmic gradient ∇log f = (z1 fz1, . . . , zd fzd). Because the height
function hr is the real part of ˜hr(z) = −r · log(z), the point p is a critical point
lying in V(Pj) \ Fk+1 if and only if the gradient vector −(r1/p1, . . . , rd/pd) of
˜hr at z = p is normal to the tangent space of V(P j) at p. Since the tangent
space is a linear subspace of codimension c, and we consider only points with
8.2 Computing critical points
229
non-zero coordinates, we see that p is a critical point if and only if the matrix
M(z, r) =

(∇log p1)(z)
...
(∇log ps)(z)
r1
· · ·
rd

(8.3)
has rank c when z = p, which occurs if and only if all (c + 1) × (c + 1) minors
of M(p, r) vanish. Thus, the critical points of F contained in V(P j) \ Fk+1 are
deﬁned by the vanishing of the polynomials p1(z), . . . , ps(z) together with the
(c + 1) × (c + 1) minors of M and the nonvanishing of a generating set of Ik+1
together with the polynomial z1 · · · zd (since we only search for critical points
with non-zero coordinates). Because our Whitney stratiﬁcation is deﬁned by a
ﬁnite number of algebraic sets, we ultimately obtain the following.
Proposition 8.10. The set critical(r) of all (stratiﬁed) critical points of any
rational function F ∈Q(z) in a direction ˆr is deﬁned by a ﬁnite collection of
polynomial systems over Q[r][z], each involving polynomial equalities and in-
equalities. The polynomials in these (in)equalities can be computed explicitly.
The complexity of computing critical points, discussed in Melczer and Salvy
[MS21], is typically lower than the complexity of verifying which (if any) are
minimal points.
Example 8.11. In the simplest case V = V(Q) is a smooth manifold, so the
canonical Whitney stratiﬁcation of V is speciﬁed by F0 = V and F1 = ∅. Then
I0 = ( ˜Q) is generated by the square-free part of Q and critical(r) is deﬁned
by ˜Q(z) = 0 and the vanishing of the 2 × 2 minors of
M(z, r) =
 z1 ˜Qz1(z)
· · ·
zd ˜Qzd(z)
r1
· · ·
rd
!
,
matching Lemma 7.8. Note that we can skip the step of decomposing I0 = ⟨˜Q⟩
into its prime factors: V being smooth implies that the prime factors of I0 are
distinct and each corresponds to a variety of codimension 1.
◁
Remark 8.12. Given z ∈V let L(z) denote the logarithmic normal space to
the stratum S containing z, given by the span of the logarithmic gradients of
the functions locally deﬁning S at z. Then z ∈critical(r) if and only if
r ∈L(z), and this deﬁnes a binary relation on (V, Rd).
We end this section with some examples in low dimensions.
230
Eﬀective computations and ACSV
Example 8.13 (binomial coeﬃcients). Recall the binomial coeﬃcient gener-
ating function
1
1 −x −y =
X
r,s≥0
 r + s
r, s
!
xrys.
Since Q(x, y) = 1 −x −y we ﬁnd ∇Q = (−1, −1) never vanishes, so the variety
V is a smooth manifold. The smooth critical point equations (7.8) form the
polynomial system
1 −x −y = 0
−sx = −ry,
which we solve to obtain the unique critical point (x, y) =

r
r + s,
s
r + s

= ˆr.
◁
Example 8.14 (Delannoy numbers). Recall from Example 2.7 that the denom-
inator for the Delannoy generating function is given by Q(x, y) = 1−x−y−xy.
To check whether V is a manifold, we form the ideal I = ⟨Q, Qx, Qy⟩and
compute the reduced Gr¨obner basis [1], meaning V(I) = ∅and V is a smooth
manifold.
To characterize the critical points in a direction ˆr, where r = (r, s), we
form the ideal J = ⟨Q, sxQx −ryQy⟩and compute the reduced Gr¨obner basis
G = {p(x, y), g(y)} of J, where p(x, y) = rx−sy−r + s and g(y) = sy2 +2ry−s.
Solving the quadratic g(y) for y gives
y = −r ±
√
r2 + s2
s
and back substitution into p(x, y) implies that critical(r, s) consists of the
two points

√
r2 + s2 −s
r
,
√
r2 + s2 −r
s
and

−
√
r2 + s2 −s
r
, −
√
r2 + s2 −r
s
.
(8.4)
We will see later that the ﬁrst point is the one that determines the asymptotics
of ars as r, s →∞.
◁
Example 8.15 (two intersecting planes). Let Q(x, y, z) = A(x, y, z)B(x, y, z)
with A(x, y, z) = 4 −x −2y −z and B(x, y, z) = 4 −2x −y −z. The zero set
V = V(Q) is the union of two hyperplanes V1 = V(A) and V2 = V(B)
that intersect transversely in the line ℓ= V(A, B). The canonical Whitney
stratiﬁcation of V is given by the algebraic sets
V = F0 ⊃F1 ⊃F2 = ∅
8.2 Computing critical points
231
with F1 = ℓ, and corresponding ideals I0 = ⟨AB⟩and I1 = ⟨A, B⟩. The ideal I0
has the prime decomposition I0 = ⟨AB⟩= P1∩P2 with P1 = ⟨A⟩and P2 = ⟨B⟩,
and the strata of V are
S 1 = V1 \ ℓ, S 2 = V2 \ ℓ, and S 1,2 = ℓ,
see Figure 8.1.
Figure 8.1 Critical points on diﬀerent strata when V is two intersecting planes.
Critical points in the direction ˆr, where r = (r, s, t), on the stratum S 1 are
deﬁned by the vanishing of A(x, y, z) and the 2 × 2 minors of the matrix
 xAx
yAy
zAz
r
s
t
!
together with the nonvanishing of B(x, y, z). Solving
4 −x −2y −z = tx −rz = 2ty −sz = 0
in (x, y, z) gives the point σ =
1
r+s+t(4r, 2s, 4t) = (4ˆr, 2ˆs, 4ˆt), which lies in
S 1 unless 2r = s, in which case the point is in ℓ. Finding the critical point
on S 2 is analogous and gives the point τ = (2ˆr, 4ˆs, 4ˆt) unless 2s = r. These
critical points are the two points marked with dots that are not on the line of
intersection in Figure 8.1.
Critical points on ℓare deﬁned by the vanishing of A(x, y, z), B(x, y, z), and
232
Eﬀective computations and ACSV
the 3 × 3 minor (i.e., determinant) of the matrix

xAx
yAy
zAz
xBx
yBy
zBz
r
s
t
.
Solving the resulting polynomial system
4 −x −2y −z = 0
4 −2x −y −z = 0
ryz + sxz −3txy = 0
gives the point ω = (4/3)(ˆr + ˆs, ˆr + ˆs, 3ˆt), which is the unique point on ℓat
which (r, s, t) lies in the plane spanned by the logarithmic tangents (x, 2y, z)
and (2x, y, z) to the planes deﬁned by A and B.
Thus, critical(r, s, t) consists of the points σ, τ, and ω, which are distinct
unless 2r = s (in which case σ = ω) or r = 2s (in which case τ = ω). For
z ∈ℓthe space L(z) is the two-dimensional span of the log-gradient vectors
of A and B at z, while for z in S 1 (respectively S 2) the space L(z) is the one-
dimensional space deﬁned as the span of the log-normal to A (respectively B)
at z.
◁
The last three examples have critical points that are either rational functions
of r or require only square roots. In general we may obtain algebraic functions
of arbitrary complexity, and it is often best to encode critical points via their
minimal polynomials.
Example 8.16. Again consider the generating function
F(x, y) =
X
r,s≥0
arsxrys =
xy(1 −x)3
(1 −x)4 −xy(1 −x −x2 + x3 + x2y).
The smooth critical points of F in the direction ˆr, where r = (r, s), are encoded
by the ideal ⟨Q, sxQx −ryQy⟩. Writing λ = s/r, the Gr¨obner basis of this ideal
with respect to the lexicographic term order where y > x (which gives a simpler
result than x > y) contains a polynomial of the form (1 −x)5βλ(x) where
βλ(x) = (1+λ)x4 +4(1+λ)2x3 +10(λ2 +λ−1)x2 +4(2λ−1)2x+(1−λ)(1−2λ)
is irreducible for generic λ. There is some simpliﬁcation for particular values
of λ, for instance the roots of the polynomial β1/2(x) = x2(x2 + 6x −5/3) lie in
a quadratic extension of Q.
◁
8.2 Computing critical points
233
8.2.3 Critical points at inﬁnity
As seen in Chapter 7, our Morse-theoretic decompositions hold in the absence
of critical points at inﬁnity (CPAI). In this section we give an algebraic test,
using Gr¨obner bases, to certify the absence of CPAI.
So far in this chapter we have dealt with aﬃne critical points, and we now
extend this to consider points in projective space. A polynomial P(z) is a ho-
mogeneous polynomial if every monomial appearing in P has the same degree
δ; equivalently, P(λz) = λδP(z) when λ is a variable. The homogenization
of a polynomial P ∈K[z] is the homogeneous polynomial Ph ∈K[z0, z] de-
ﬁned by Ph(z0, z) = zdeg P
0
P(z1/z0, . . . , zd/z0), and the homogenization of an
ideal I ⊂K[z] is the ideal Ih = {Ph : P ∈I} ⊂K[z0, z]. If {g1, . . . , gr} is a
Gr¨obner basis of I with respect to any monomial order where zα > zβ when-
ever |α| > |β| then Ih is generated by the set of homogenizations {gh
1, . . . , gh
r}
(see [CLO07, Section 8.4]). Because Ih is generated by homogeneous polyno-
mials, p ∈V(Ih) implies λp ∈V(Ih) for all λ ∈C so we can view the variety
V(Ih) as a subset of complex projective space CPd.
Remark 8.17. The elements of V(I) can be viewed as the elements of V(Ih)
with z0 = 1, while the limit of points in V(I) “at inﬁnity” can be viewed as the
elements of V(Ih) with z0 = 0. If I = ⟨f1, . . . , fr⟩for an arbitrary generating set
{f1, . . . , fr} then J = ⟨f h
1 , . . . , f h
r ⟩is an ideal of K[z0, z] contained in Ih, how-
ever J may be strictly smaller than Ih. Nonetheless, this containment implies
that V(Ih) = ∅whenever V(J) = ∅.
Fix a direction r and let P be an element of the prime decomposition of an
ideal I(Fk) coming from the canonical Whitney stratiﬁcation F0 ⊃F1 ⊃· · · ⊃
Fm of V. As seen above, the critical points on a stratum of V(P) \ Fk+1 ⊂
Fk \ Fk+1 in a direction y are encoded by the vanishing of a ﬁnite collection C
of polynomials containing a generating set p1, . . . , ps of P together with appro-
priate minors of the matrix M(z, y) in (8.3). To detect CPAI in the direction
r, it is tempting to homogenize the polynomials in C to obtain a new set of
polynomials C′ and then search for any common solutions to the elements of
C′ where z0 = 0 and y = r. Unfortunately, this approach is too weak to form a
useful test: homogenizing the elements of C means that V(C′) can have com-
plicated behavior at inﬁnity that is completely unrelated to the behavior of
V(C).
We get around this diﬃculty by using ideal saturation. Recall from above
that the saturation of an ideal I by another ideal J is an ideal I : J∞whose
zero set V(I : J∞) is the closure of V(I)\V(J). Saturating the ideal generated
by the elements of C′ with the ideal ⟨z0⟩leaves only the points of V(C′) that
234
Eﬀective computations and ACSV
are limits of points in V(C). Note that it is crucial to leave the direction y as
a vector of variables when performing the saturation: CPAI in the direction r
are limits of critical points in directions approaching r, and substituting y = r
before performing the saturation will leave only points that are limits of critical
points in the precise direction r. Performing this saturation, then substituting
y = r and searching for non-trivial solutions at inﬁnity forms an eﬀective
test to certify the absence of CPAI. Note that CPAI also occur when one of
the variables zk is zero, and we test for this analogously. Ultimately we obtain
Algorithm 1, taken from [BMP22], along with the simpliﬁed Algorithm 2 that
works when the singular variety V is a smooth manifold.
Algorithm 1: Algorithm to compute CPAI.
Input: Polynomial Q ∈K[z], direction r and polynomial generators of
algebraic sets F0 ⊃F1 ⊃· · · ⊃Fm deﬁning the canonical
Whitney stratiﬁcation of V(Q).
Output: Set S of pairs of ideals in K[z0, z] such that if there is a CPAI
in the direction r then there exists (A, B) ∈S with
V(A) \ V(B) , {0}.
Set S = ∅
For j from 1 to m −1:
Compute the prime decomposition F j = P1 ∩· · · ∩Pr
For each I ∈{P1, . . . , Pr}:
Let c be the codimension of I
Let C be the ideal generated by I and the (c + 1) × (c + 1)
minors of M(z, y)
Homogenize C in the z variables with the new variable z0 to
obtain the ideal C′
Saturate C′ by z0z1 · · · zd to obtain the ideal D
Let A be the ideal generated by D and z0z1 · · · zd after
substituting y = r
Let B be the homogenization of I(Fj+1)
Add (A, B) into S
Return S
Example 8.18. Let
F(z1, z2, z3, z4) =
1
1 −z1 −z2 −z3 −z4 + 27z1z2z3z4
and consider the main diagonal direction. Applying Algorithm 2, we see that
there are no CPAI.
◁
