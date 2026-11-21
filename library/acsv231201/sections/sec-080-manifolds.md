---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-080-manifolds
section_title: "Manifolds"
section_number: null
pages: 456-461
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Our ﬁrst two appendices develop the theoretical background necessary to un-
derstand what it means to represent the series coeﬃcients ar of an analytic
function F(z) by an integral
ar =
 1
2πi
!d Z
C
ω
deﬁned up to homologous cycles C and cohomologous forms ω in the domain
of holomorphicity M of ω. To make sense of this statement we deﬁne diﬀeren-
tial forms and their integrals, state the multivariate Cauchy Integral Formula,
construct singular homology and cohomology over the domain M, and con-
nect the singular homology of M to the integration of exact forms over cycles
in M.
We begin in this appendix by formally constructing the apparatus to integrate
diﬀerential forms on real and complex manifolds.
• In Section A.1 embedded and abstract manifolds are deﬁned, an important
example of the latter being projective spaces.
• In Section A.2 vector ﬁelds and diﬀerential forms are introduced.
• In Section A.3 integration of forms over chains is deﬁned, leading to Stokes’s
Theorem (Theorem A.24).
• In Section A.4 complex holomorphic forms are deﬁned and Cauchy’s inte-
gral formula in a polydisk and polyannulus (Propositions A.28 and A.29)
are stated.
A.1 Manifolds
The notion of a manifold may already be familiar to some readers, but there
are several diﬀerent formalizations so we start with basic deﬁnitions. Except
438
A.1 Manifolds
439
Figure A.1 Covering the sphere with two charts.
for projective spaces, the manifolds most relevant to us will be submanifolds
of Euclidean space, and we present this more concrete case ﬁrst.
A.1.1 Embedded manifolds
An embedded real d-manifold is a subset M ⊂Rn such that every point p ∈M
has a neighborhood in Rn whose intersection U with M is diﬀeomorphic to the
open unit ball in Rd. Here, diﬀeomorphic means there is a map φ : U →Rd
such that the coordinates of φ are smooth (that is, members of the class C∞of
inﬁnitely diﬀerentiable functions) and the rank of its Jacobian matrix at each
point is d (which implies that φ has a smooth inverse). If (U, φ) is a pair of such
a set and diﬀeomorphism then we call U a chart and φ a chart map.
Example A.1. The implicit function theorem implies that if Q is a smooth
function and w is a zero of Q where the gradient of Q does not vanish, then the
zero set of Q is locally diﬀeomorphically parametrized near w by any (d −1)
coordinates xk1, . . . , xkd−1 such that the span of the gradients ∇xk1, . . . , ∇xkd−1 at
w does not contain (∇Q)(w). For instance, if S d = {x ∈Rd+1 : Pd
j=1 x2
j = 1} is
the unit d-sphere in Rd+1 then taking Q(x) = Pd
j=1 x2
j −1 establishes that S d =
{x ∈Rd+1 : Q(x) = 0} is a manifold. The unit d-sphere can be parametrized
with as few as two charts, by projecting the points above and below certain zd
values; see Figure A.1.
◁
The deﬁnition of an embedded complex d-manifold is analogous to that of
an embedded real manifold, except we require the stricter condition that the
chart maps be holomorphic (or, equivalently, analytic) instead of smooth.
Remark A.2. Because Cd can be identiﬁed with R2d by writing z j = x j + iyj
for real coordinates (x1, y1, . . . , xd, yd), subsets of Cd can also be viewed as real
manifolds. This identiﬁcation is crucial to many of our arguments.
The implicit function theorem directly implies the following result.
440
Integration on manifolds
Proposition A.3. Suppose Q is a holomorphic function of d complex variables
and let VQ be the aﬃne holomorphic variety VQ = {z ∈Cd : Q(z) = 0}. If
∇Q(z) is nonvanishing for every z ∈VQ then VQ is an embedded real (2d−2)-
manifold.
□
Remarks. (i) Using the complex implicit function theorem, instead of map-
ping to R2d and using the real implicit function theorem, shows that VQ will
be a complex (d −1)-manifold. We do not need this extra structure at present.
(ii) When Q is the product of distinct irreducible polynomials then this result
is sharp: if ∇Q vanishes at some z ∈VQ then no neighborhood of z in Q is
diﬀeomorphic to Cd−1.
Exercise A.1. For which polynomials Q is VQ a manifold?
(1) Q(x, y) = x2 +y2 +z2 −c, where c is a constant. Does the value of c matter?
(2) Q(x, y) = y3 −x2
(3) Q(x, y) = z2 −(x + y)2
(4) Q(x, y) = 1 −x −y −xy
Example A.4. The unit torus in Cd is the set {z ∈Cd : |z j| = 1 for all 1 ≤j ≤
d}. Identifying Cd with R2d, this set is deﬁned by x2
j + y2
j = 1 for all 1 ≤j ≤d,
and is thus always a real d-manifold. On the other hand, the unit torus is never
a complex manifold. When d is odd this follows immediately from the fact that
it has the wrong dimension to be a complex manifold (when d is even then the
concept of tangent spaces, described below, can be used to prove the unit torus
is not a complex manifold). See Exercise A.14 for another example of lack of
complex structure.
◁
A.1.2 Abstract manifolds and projective spaces
Instead of working directly with subsets of Rd or Cd, it is possible to deﬁne
abstract manifolds whose ground sets can be anything. Although the Whitney
embedding theorem states that an abstract d-manifold can be embedded in R2d,
in some cases it is more natural to consider a deﬁnition requiring only a lo-
cal embedding into some real or complex space. In particular, expanding to
abstract manifolds helps us discuss projective spaces, which arise in the for-
mulation of critical points at inﬁnity and the singular integrals of Chapter 11.
Let M be a second-countable Hausdorﬀspace. A chart of dimension d on
M is an open subset U ⊂M and a homeomorphism φ from U onto an open
subset of Rd. We say that the chart (U, φ) contains p if p ∈U. Two charts
(U, φ) and (V, ψ) are compatible if the transition maps
φ ◦ψ−1 : ψ(U ∩V) →φ(U ∩V)
and
ψ ◦φ−1 : φ(U ∩V) →ψ(U ∩V)
A.1 Manifolds
441
are smooth as functions on Rd (this holds trivially when U ∩V = ∅), and we
call M a real d-manifold if there exists a collection of pairwise-compatible
charts of dimension d that cover M. Any additional charts that are compatible
with the charts deﬁning a manifold must also be compatible with each other, so
any collection of charts covering a manifold is contained in a uniquely deﬁned
maximal set of compatible charts, known as an atlas. This makes some of the
notation easier by allowing us to assume that for any given p ∈M there is a
chart map taking p to the origin in Rd, since we can always subtract a constant
from a chart map to obtain another chart map.
Example A.5 (real projective d-space). Let M =

Rd+1 \ 0
 .
(x 7→λx) de-
note the set of non-zero vectors modulo non-zero scalar multiples, which can
be identiﬁed with the set of lines through the origin in Rd+1. It is conventional
to write an element of M as (x0 : x1 : x2 : · · · : xd), with the colons in
place of commas indicating that multiplying every coordinate by a non-zero
real number gives a diﬀerent representation for the same element. For each
0 ≤α ≤d let Uα = {x ∈M : xα , 0}, and deﬁne chart maps φα : Uα →Rd
by φα(x) := (x j/xα) j,α. This deﬁnes the manifold RPd of real projective d-
space.
◁
Recall from Section 8.2 that if Q is a polynomial in x1, . . . , xd of total de-
gree m then the homogenization of Q is the polynomial Q(x0, x1, . . . , xd) =
xm
0 Q(x1/x0, . . . , xd/x0) in x0, x1, . . . , xd. Because every monomial appearing in
Q has degree m by construction, Q(λx) = λmQ(x) and the zero set of Q in
Rd is closed under scalar multiples. Thus, Q deﬁnes a real projective variety
VQ = {x ∈RPd−1 : Q(x) = 0}.
Exercise A.2. Let Q(x) = 1 −x2 −y2. (1) What subset of R3 is the union
of equivalence classes making up the real projective variety VQ? (2) Is the
projective variety VQ a manifold? (3) Intuitively, what simple shape is VQ
equivalent to?
A complex d-manifold is deﬁned analogously to a real d-manifold, except
that the chart maps go to Cd and the transition maps between charts need to
be holomorphic. Analytic functions from Cd to Cd are smooth when viewed as
maps from R2d to R2d, so all complex d-manifolds may be viewed as real (2d)-
manifolds. We also deﬁne the complex projective d-space CPd analogously to
real projective space and, overloading notation, use VQ to denote the complex
projective variety deﬁned by a polynomial Q. When writing VQ, we make sure
it is understood whether we are referring to the real or complex projectiviza-
tion.
442
Integration on manifolds
Exercise A.3. Give a description of the complex projective variety VQ when
Q(x) = 1 −x2 −y2.
A real m-manifold is called an orientable manifold if it can be covered by
charts (Uα, φα) such that the real transition maps φα ◦φ−1
β
: φβ(Uα ∩Uβ) →
φα(Uα ∩Uβ) have Jacobian matrices with positive determinants. Such a cover
yields an orientation, which is the set of all chart maps consistent with the
chosen orientation (meaning that all transition maps still have positive Jacobian
determinants).
Exercise A.4. Show that the standard 2-sphere S 2 ⊆R3 is orientable.
In fact, the notion of orientability is interesting only for real manifolds. The
following classical result follows from the results of Section A.4 below.
Proposition A.6. Every complex manifold is orientable when considered as a
real manifold.
A smooth map between two real manifolds M and M′ of dimensions m and
n is a function f : M →M′ such that for any p ∈M and any chart maps
φ on a chart of M containing p and ψ on a chart of M′ containing f(p), the
function ψ ◦f ◦φ−1 from a subset of Rm to Rn is smooth. Holomorphic maps
between complex manifolds are deﬁned analogously, requiring ψ ◦f ◦φ−1 to
be holomorphic instead of smooth.
In this appendix we construct various objects associated with manifolds:
tangent bundles, diﬀerential forms, chain complexes, homology, etc. Without
introducing large amounts of category theory for its own sake, some categorical
terminology is useful because it guides us to what should be true and what
arguments are predictable symbol manipulation – so-called diagram chases
– that can be skipped. In particular, our constructions are functorial. In the
covariant case this means that, in addition to associating an object G(M) with
each manifold M, we associate a map G∗( f) : G(M) →G(M′) with every
map f : M →M′ between manifolds, having the property that G∗(g ◦f) =
G∗(g) ◦G∗( f). The map G∗( f) between the objects G(M) and G(M′) is said
to be the induced map associated to f. In the contravariant case, the induced
map G∗( f) : G(M′) →G(M) goes in the other direction (as indicated by the
raised *) and G∗(g ◦f) = G∗( f) ◦G∗(g).
Exercise A.5. Let G(M) denote the space of smooth real-valued functions on
M. Determine whether this should be viewed as a covariant or contravariant
functor, and deﬁne the map G∗or G∗as the case may be.
Given a manifold M, an Rk-bundle E over M is a map of manifolds π : E →
