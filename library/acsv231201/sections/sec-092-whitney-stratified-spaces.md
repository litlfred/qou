---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-092-whitney-stratified-spaces
section_title: "Whitney stratified spaces"
section_number: null
pages: 531-536
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Ideally one would use the apparatus of manifolds, developed in the previous
appendices, to do calculus on complex algebraic varieties, however many vari-
eties that appear in interesting combinatorial problems are not manifolds. The
right generalization for our purposes is the notion of a stratiﬁed space, which
can contain non-manifold points whose neighborhoods in the variety are not
diﬀeomorphic to any Euclidean space Rd. One well-known example of such
spaces are manifolds with boundary, and we begin with a recap of these ob-
jects. The following material on manifolds with boundary can be skipped if
desired, as it is subsumed by our discussion of stratiﬁed spaces, however we
include it because it is likely familiar to many readers.
A d-manifold with boundary is a subset M ⊂Rn such that every point
x ∈M has a neighborhood in Rn whose intersection N with M is either
diﬀeomorphic to Rd or diﬀeomorphic to the closed halfspace Rd−1 × [0, ∞). In
513
514
Stratiﬁcation and stratiﬁed Morse theory
the former case x is called a manifold point or interior point of M, while in
the latter case x is called a boundary point of M.
Example D.1. A closed ball in any dimension d is a manifold with boundary,
while a cube [0, 1]d and a simplex {x ∈Rd : x j ≥0 for all j and Pd
j=1 xj = 1}
are not.
◁
Example D.2. If H = {(x, y) ∈R2 : y ≥0} is the upper half-plane then H is
a manifold with boundary, the boundary points being the x-axis. Now let K =
{(x, y) ∈R2 : x, y ≥0} denote the positive quarter plane. The map φ(x, y) =
(x2 −y2, 2xy) from K to H, constructed by taking the real and imaginary parts
of (x + iy)2, is analytic and one to one, so it may seem that K is diﬀeomorphic
to H and thus a manifold with boundary. However, φ−1 is not diﬀerentiable at
the origin, and in fact no neighborhood of the origin in K is diﬀeomorphic to
a neighborhood of the origin in a half-plane. Thus, K is not a manifold with
boundary.
◁
Exercise D.1. Give an example of a manifold M ⊆Rd with closure M whose
boundary M\M is also a manifold, such that M is not a manifold with bound-
ary.
A generalization of manifolds with boundary is the notion of a d-manifold
with corners, where every point has a neighborhood diﬀeomorphic to some or-
thant Rd−k×Rk
≥0 for some k ≤d; see Figure D.1. Cubes and simplices are mani-
folds with corners, however complex algebraic varieties that are not smooth are
also typically not manifolds with corners. This diﬃculty is why we introduce
the generality of stratiﬁed spaces.
Figure D.1 The closed quadrant M is a manifold with corners, but not a manifold
with boundary.
D.1 Whitney stratiﬁed spaces
515
Stratiﬁcations
As a ﬁrst attempt to perform calculus on an algebraic variety V, one might
partition V into a ﬁnite disjoint union of smooth sets and then work on each
piece of the partition. Although such smooth partitions can be easily under-
stood, and easily computed using standard algebro-geometric techniques, they
are not suﬃcient for our (and many other) purposes. The problem is that the
pieces in an arbitrary smooth partition may not ﬁt together nicely; among other
diﬃculties, this means the local behavior of V near points in the same piece of
the partition can be very diﬀerent.
The issue of determining the “right” type of smooth partition to use for topo-
logical arguments was taken up by Whitney [Whi65b], who introduced what
we now call (Whitney) stratiﬁcations. An I-decomposition of a space X ⊆Rn
is a ﬁnite disjoint union S
α∈I Sα of smooth manifolds of various dimensions,
indexed by a partially ordered set I, such that for every α, β ∈I,
S α ∩S β , ∅
⇐⇒
S α ⊂S β
⇐⇒
α ≤β.
(D.1.1)
Deﬁnition D.3 (Whitney stratiﬁcation). Let Z be a closed subset of Rn. A
Whitney stratiﬁcation of Z is an I-decomposition of Z with the additional
property that whenever
• α < β, and
• the sequences {xi ∈S β} and {yi ∈S α} both converge to some y ∈S α, and
• the lines ℓi = xi yi converge to a line ℓ, and
• the tangent planes Txi(S β) converge to a plane T,
then ℓ⊆T. We call Z a Whitney stratiﬁed space.
Remark. In the original deﬁnition, in addition to ℓ⊆T (the so-called second
Whitney condition), it was required that Ty(Sα) ⊆T (the so-called ﬁrst Whit-
ney condition). The second condition turns out to imply the ﬁrst, so the ﬁrst
condition is usually omitted.
This deﬁnition is well crafted: the conditions are easy to fulﬁll – for ex-
ample, every algebraic variety admits a Whitney stratiﬁcation, see [Whi65b,
Theorem 18.11] or [Hir73, Theorem 4.8] – and the conditions have strong con-
sequences (for instance, they are strong enough for stratiﬁed Morse theorems
to hold). Stratiﬁcations of algebraic varieties are also eﬀectively computable.
A classic approach to algorithmic stratiﬁcation through quantiﬁer elimination
and real algebraic geometry, relying on cylindrical algebraic decomposition, is
discussed in [Ran98; MR91]. Recently, [DJ21] and [HN22] have given more
516
Stratiﬁcation and stratiﬁed Morse theory
practical algorithms1 for the stratiﬁcation of algebraic varieties using Gr¨obner
basis computations.
Proposition D.4. Every algebraic variety in Rd or Cd admits a Whitney strat-
iﬁcation.
□
In examples arising from combinatorial applications, it is often possible to
deduce a stratiﬁcation directly from the form of the polynomials under consid-
eration.
Example D.5. A smooth manifold is a stratiﬁed space with a single stratum.
◁
Example D.6. If X is a ﬁnite union of aﬃne subspaces of Rn then a Whitney
stratiﬁcation of X is obtained by taking the set A of all intersections of the
aﬃne subspaces, and choosing the elements of {A \ B : A, B ∈A with A ⊋B}
as strata.
◁
Example D.7. Let Z be a real algebraic curve {(x, y) ∈R2 : f(x, y) = 0} with f
irreducible and let Y = {(x, y) : ∇f(x, y) = 0} be the ﬁnite set of singular points
of Z. Taking Z \ Y to be one stratum and each singleton {(x, y)} for (x, y) ∈Y to
be another produces a Whitney stratiﬁcation of Z. The following ﬁgure shows
two examples of this, the ﬁrst curve x2 −y3 having a cusp at the origin and the
second curve 19 −20x −20y + 5x2 + 14xy + 5y2 −2x2y −2xy2 + x2y2 having a
self-intersection at (1, 1).
◁
Figure D.2 Two curves, each stratiﬁed by taking one stratum consisting of a sin-
gular point and another stratum consisting of the rest of the curve.
Let V be any complex variety. As discussed in Chapter 8, it is possible to
decompose V into smooth sets by determining algebraic equations for the set
1 Helmer and Nanda [HN22] give an implementation of both of these algorithms in Macaulay2,
available at http://martin-helmer.com/Software/WhitStrat/.
D.1 Whitney stratiﬁed spaces
517
Σ0 of its singular points, letting S0 = V \ Σ0 encode the smooth points of
V, then recursively computing the sets Σn+1 and Sn+1 of smooth and singular
points of Σn until arriving at some ΣN = ∅. From the previous two examples,
one might get the idea that this decomposition is always a Whitney stratiﬁca-
tion, but Exercise D.6 below shows this not to be the case. It is true, however,
that any stratiﬁcation must be at least this coarse.
Example D.8. Let Z be a complex algebraic hypersurface in C3 deﬁned by
f(x, y, z) = 0 and suppose ∇f vanishes along an algebraic curve γ. It is pos-
sible that {γ, Z \ γ} is a Whitney stratiﬁcation for Z. On the other hand, if γ is
not smooth then a Whitney stratiﬁcation of Z will have at least three strata, one
containing singularities of γ, one containing the rest of γ, and one containing
Z \ γ.
◁
Exercise D.2. Compute a Whitney stratiﬁcation of the real variety VQ where
Q(x, y, z) = z2 −x2 −y2.
The following exercise implies, with a little more work, that any manifold
with corners (including any manifold with boundary) is a Whitney stratiﬁed
space, with strata {S j : 0 ≤j ≤d} deﬁned by the union of the open j-
dimensional faces.
Exercise D.3. Let H = Rd
≥0 be the positive orthant, let F be a (open) face of
H and let x be a point of F. Prove directly that the interior S β = H◦and face
S α = F satisfy the Whitney condition (Deﬁnition D.3) at x.
One fundamental result of stratiﬁed spaces concerns their local product struc-
ture, implying that the local behavior of a stratiﬁed space “looks the same” in
neighborhoods of diﬀerent points on the same stratum. The proof of this fact
is long and diﬃcult, but we sketch some of it in the next section.
Theorem D.9 (local product structure). Let p be a point in a k-dimensional
stratum S of a stratiﬁed space Z. There is a topological space N, called the
normal slice, depending only on S and not the choice of p ∈S, such that
some neighborhood of p in Z is homeomorphic to Bk × N, where Bk is a k-
dimensional ball.
□
We end this section with the following concept.
Deﬁnition D.10 (stratiﬁcation of a pair). If Y ⊆X are closed subsets of real
space then a stratiﬁcation of the pair (X, Y) is deﬁned to be a stratiﬁcation
of X such that intersecting each stratum with Y gives a stratiﬁcation of Y and
intersecting each stratum with X \ Y gives a stratiﬁcation of X \ Y.
518
Stratiﬁcation and stratiﬁed Morse theory
A result of Whitney implies that if (X \ Y, Y) is a decomposition of X into
two smooth manifolds satisfying (D.1.1) then some Whitney stratiﬁcation of
X reﬁnes this, and is a stratiﬁcation of the pair (X, Y); see, for instance, [LT10,
Proposition 2.1]. Proposition D.4 extends to the following.
Proposition D.11. If V∗is a complex algebraic variety in Cd
∗with stratiﬁca-
tion {Sα : α ∈I} then adding the stratum M = Cd
∗\V∗produces a stratiﬁcation
of the pair (C∗
d, V∗).
□
