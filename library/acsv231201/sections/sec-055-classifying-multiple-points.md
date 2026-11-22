---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-055-classifying-multiple-points
section_title: "Classifying multiple points"
section_number: null
pages: 340-345
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Having discussed the coeﬃcient asymptotics of generating functions with mul-
tiple points, we turn to the problem of recognizing when they arise.
Proposition 10.48. The point p ∈V is a multiple point if and only if there is
a factorization
Q(z) =
n
Y
j=1
Q j(z)m j
(10.24)
in Op with ∇Q j(p) , 0 and Q j(p) = 0. The point p is a transverse multiple
point with n divisors if and only if in addition the gradient vectors ∇Q j for
1 ≤j ≤n are linearly independent.
10.4 Classifying multiple points
323
When mj = 1 for all j in the decomposition (10.24), we say that Q is square-
free at p.
Proof
The ring Op is a unique factorization domain [H¨or90], so Q has some
factorization into powers of distinct irreducibles. The variety V is locally the
union of the vanishing sets of the irreducibles Q j, each of which deﬁnes a
smooth hypersurface if and only if its gradient at p is non-zero. The transver-
sality assertion follows immediately from the deﬁnition.
□
To give an algebraic criterion for the multiple point p to be an arrangement
point, let Q j(z) be as in (10.24), and let ℓj(z) denote the linear polynomial
ℓj(z) = ∇Q j(p) · (z −p)
forming the leading homogeneous part of Q j at p. The leading homogeneous
part of Q at p is the homogeneous polynomial of degree n
hom(Q, p) =
n
Y
j=1
ℓj(z)m j
and therefore the zero set of hom(Q, p), which is the algebraic tangent cone
algtanp(Q) discussed previously in Chapter 6, equals the hyperplane arrange-
ment A deﬁned by the tangent planes to the Q j at p. We remark that the in-
tersection lattice of this arrangement remains the same as p varies over the
stratum S of V containing p. By deﬁnition, for p to be an arrangement point
such a product decomposition must hold and the lattice of ﬂats of A must be
isomorphic to the intersection lattice of the local surfaces V j = VQ j. Repeated
factors are allowed, so we may assume without loss of generality that each mj
is equal to 1, arriving at the following algebraic criterion.
Proposition 10.49. The point p ∈V is an arrangement point if and only if
both hom(Q, p) and Q factor into smooth factors (the former will be linear
polynomials in C[z] and the latter will be in Op) and the two intersection
lattices agree.
□
Example 10.50 (Example 10.4, continued). Let Q(x, y) be the polynomial
from Example 10.4 and let p = (1, 1). Taking the monomials of least degree of
Q(1 + x, 1 + y) gives
hom(Q, p) = 4x2 + 10xy + 4y2 .
Every homogeneous quadratic in two variables is the product of linear factors,
which are distinct unless the discriminant of the quadratic vanishes. In this
example the discriminant is 36, hence p is an arrangement point. In fact it is a
324
Multiple point asymptotics
transverse multiple point, and the local intersection lattice for both the divisors
and their tangent planes is a Boolean lattice of rank 2.
◁
It is important to work over the correct ﬁeld when analyzing multiple points.
Figure 10.14 A homogeneous polynomial whose zero set is ﬁve lines.
Example 10.51. Let f(x, y) = 2y5 + y4x −10y3x2 −5y2x3 + 8yx4 + 3x5. This
homogeneous polynomial has a zero set consisting of ﬁve distinct lines through
the origin whose slopes are the ﬁve roots (all real) of the quintic 2t5 + t4 −
10t3 −5t2 + 8t + 3. This quintic does not factor over the rationals, so one must
work over the splitting ﬁeld of f to obtain the necessary factorization. This
can be handled in many computer algebra systems, but is more complicated
than factoring directly over the rationals. See also Proposition 10.53 below for
useful criteria to determine multiple and arrangement points.
◁
Eﬀective computation of multiple points
The foregoing discussion being of a theoretical nature, we pause to consider
how the classiﬁcation of multiple points might be computed. When given a
polynomial Q, one imagines being able to “look at its zero set” to see by in-
spection whether it is locally the union of smooth sheets, but this is diﬃcult
when the dimension is high, the polynomial has many terms, or the procedure
is automated. What, then, is an eﬀective way to determine whether any of the
singular points of Q is in fact a multiple point?
In many combinatorial applications, Q factors into polynomials with non-
zero gradients at the origin, and Proposition 10.48 can be directly applied. The
diﬃculty comes when an irreducible polynomial factor Q j of Q has vanishing
gradient: it is possible that the gradient of Q j vanishes at p because p is not
a multiple point, but it could also happen because Q j is irreducible in C[z]
10.4 Classifying multiple points
325
but reducible in Op. Computing in Op is more diﬃcult than working with
polynomials, but we can often determine what we need.
Proposition 10.52. For any positive integers n and d, determining whether a
homogeneous polynomial f ∈Q[z] of degree n in d variables has a factoriza-
tion into n (possibly repeated) linear terms is decidable via computer algebra.
If f is a product of linear factors, then whether these factors are distinct is also
decidable by computer algebra.
Proof
The set of coeﬃcients of products of n homogeneous linear polynomi-
als in d dimensions forms an algebraic variety. Various sets of deﬁning poly-
nomials are known [Bri10], and containment of a point in an algebraic variety
is decidable. Such linear factors are distinct if and only if f and all its partial
derivatives have no common linear factors.
□
Exercise 10.11. In the special case d = 2, what is a quick method of deciding
whether f factors into linear factors with no repeated factor?
Replacing the polynomial Q by its square-free part if necessary, we may
assume without loss of generality that Q is square-free.
Proposition 10.53. Let Q be a square-free polynomial and let ˜Q(z) = hom(Q)
be the lowest degree homogeneous part of Q.
(i) If 0 is a multiple point for Q then ˜Q is the product of linear factors.
(ii) If 0 is an arrangement point for Q then ˜Q is the product of distinct linear
factors.
Proof
(i) Suppose 0 is a multiple point for Q. By Proposition 10.48, there is
a factorization Q(z) = Qn
j=1 Q j(z) in O0 with each ∇Q j(0) non-vanishing. If
ℓj(z) = ∇Q j(0)·z denotes the linear homogeneous term of Q j then, because ˜Q
is homogeneous of degree n, we see that ˜Q = Qn
j=1 ℓj factors into linear terms.
(ii) Suppose that 0 is an arrangement point. For each distinct i and j, exam-
ination of the sublattice {V, Vi, Vj, Vi ∩Vj} shows that the gradients at 0,
which deﬁne the linear factors, are distinct.
□
Exercise 10.12. If p is a non-smooth multiple point for Q in dimension 2 then
must it be an isolated singularity of VQ? What about in dimension d > 2?
Example 10.54. Let
Q(x, y, z) = 1 + xyz −1
3(x + y + z + xy + xz + yz)
326
Multiple point asymptotics
be the denominator of the cube grove generating function (7.23). The ideal
*
Q , ∂Q
∂x , ∂Q
∂y , ∂Q
∂z
+
has a Gr¨obner basis consisting of the polynomials [x−1, y−1, z−1], so the point
(1, 1, 1) is a non-smooth point of V. Translating this point to the origin replaces
Q by h(u, v, w) = Q(1 + u, 1 + v, 1 + w) = 2uv + 2uw + 2vw + 3uvw, and we let
˜h = 2(uv+uw+vw) be the leading homogeneous part of h. By writing down an
attempted factorization we see that ˜h does not factor into linear factors, hence
h does not and (1, 1, 1) is not a multiple point. Asymptotics for the coeﬃcients
of the cube grove generating function are discussed in Example 11.43.
◁
Unfortunately the converse to part (i) of Proposition 10.53 does not hold.
Linear factorization of the homogeneous part of Q does not imply multiple
point geometry, even if the factors are distinct and linearly independent (see
Example 10.55 below), so Proposition 10.53 helps certify that p is not a mul-
tiple or arrangement point, but doesn’t help to certify that it is one.
Another approach to certifying multiple points is a characterization using
local monodromy. Certiﬁcation in the positive direction relies on conjectured
properties of the relevant algorithms, but for those interested in the problem,
this will at least give a start.
Up to taking an invertible linear change of coordinates, we may assume that
there exists a coordinate j such that π−1(p) is always ﬁnite, where π : V →
Cd−1 is the projection map onto the coordinate plane z j = 0. Let B denote the
branch locus of π, consisting of the points w ∈Cd−1 for which the cardinality
of the ﬁber π−1(w) does not take its maximum value k. A path γ : [0, 1] →Cd−1
that avoids B deﬁnes a map from the ﬁber π−1(γ(0)) to the ﬁber π−1(γ(1)) by
so-called homotopy continuation, making continuous choices of π−1(γ(t)) for
0 ≤t ≤1. Homotopic paths in U = Cd−1 \ B deﬁne the same map, and ﬁxing
a base point z0 < B and letting γ vary over loops based at z0 deﬁnes a map
from the fundamental group of U to the permutations of the ﬁber at z0, which
we identify with the symmetric group Sk. The image in Sk is what is known as
the monodromy group of π, and is intrinsic to V in the sense that it does not
depend on the projection π. The local monodromy group at p is the image in
Sk of the subgroup of the fundamental group consisting of loops that can be
drawn so as never to leave an arbitrarily small neighborhood of p. A point p is
a multiple point if and only if the local monodromy group at p is trivial (that
is, contains only the identity permutation)1.
1 If V is locally the union of smooth surfaces then the local monodromy group is trivial
because, in a small path avoiding collisions of roots, each solution remains in the same smooth
local piece. We don’t prove the converse as it is not used in this book.
