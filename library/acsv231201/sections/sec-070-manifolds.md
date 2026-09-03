---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-070-manifolds
section_title: "Manifolds"
section_number: null
pages: 456-470
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
Our ﬁrst two appendices develop the theoretical background necessary to un-
derstand what it means to represent the series coe ﬃcients ar of an analytic
function F(z) by an integral
ar =
( 1
2πi
)d ∫
C
ω
deﬁned up to homologous cyclesC and cohomologous formsω in the domain
of holomorphicityM ofω. To make sense of this statement we deﬁne diﬀeren-
tial forms and their integrals, state the multivariate Cauchy Integral Formula,
construct singular homology and cohomology over the domain M, and con-
nect the singular homology ofM to the integration of exact forms over cycles
inM.
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
A.1 Manifolds 439
Figure A.1 Covering the sphere with two charts.
for projective spaces, the manifolds most relevant to us will be submanifolds
of Euclidean space, and we present this more concrete case ﬁrst.
A.1.1 Embedded manifolds
An embedded real d-manifold is a subsetM⊂ Rn such that every pointp∈M
has a neighborhood inRn whose intersection U withM is diﬀeomorphic to the
open unit ball in Rd. Here, diﬀeomorphic means there is a map φ : U→ Rd
such that the coordinates of φ are smooth (that is, members of the class C∞ of
inﬁnitely diﬀerentiable functions) and the rank of its Jacobian matrix at each
point is d (which implies thatφ has a smooth inverse). If (U,φ ) is a pair of such
a set and diﬀeomorphism then we call U a chart andφ a chart map.
Example A.1. The implicit function theorem implies that if Q is a smooth
function andw is a zero of Q where the gradient of Q does not vanish, then the
zero set of Q is locally diﬀeomorphically parametrized nearw by any (d− 1)
coordinates xk1,..., xkd−1 such that the span of the gradients∇xk1,..., ∇xkd−1 at
w does not contain (∇Q)(w). For instance, if S d ={x∈Rd+1 : ∑d
j=1 x2
j = 1} is
the unit d-sphere inRd+1 then taking Q(x) = ∑d
j=1 x2
j− 1 establishes that S d =
{x∈ Rd+1 : Q(x) = 0} is a manifold. The unit d-sphere can be parametrized
with as few as two charts, by projecting the points above and below certain zd
values; see Figure A.1. ◁
The deﬁnition of an embedded complex d-manifold is analogous to that of
an embedded real manifold, except we require the stricter condition that the
chart maps be holomorphic (or, equivalently, analytic) instead of smooth.
Remark A.2. BecauseCd can be identiﬁed with R2d by writing z j = x j + iy j
for real coordinates (x1, y1,..., xd, yd), subsets ofCd can also be viewed as real
manifolds. This identiﬁcation is crucial to many of our arguments.
The implicit function theorem directly implies the following result.
440 Integration on manifolds
Proposition A.3. Suppose Q is a holomorphic function of d complex variables
and letVQ be the a ﬃne holomorphic varietyVQ ={z∈ Cd : Q(z) = 0}. If
∇Q(z) is nonvanishing for everyz∈V Q thenVQ is an embedded real(2d−2)-
manifold. □
Remarks. (i) Using the complex implicit function theorem, instead of map-
ping to R2d and using the real implicit function theorem, shows that VQ will
be a complex (d− 1)-manifold. We do not need this extra structure at present.
(ii) When Q is the product of distinct irreducible polynomials then this result
is sharp: if∇ Q vanishes at somez∈V Q then no neighborhood of z in Q is
diﬀeomorphic toCd−1.
Exercise A.1. For which polynomials Q isVQ a manifold?
(1) Q(x, y) = x2 +y2 +z2−c, where c is a constant. Does the value ofc matter?
(2) Q(x, y) = y3− x2
(3) Q(x, y) = z2− (x + y)2
(4) Q(x, y) = 1− x− y− xy
Example A.4. The unit torus inCd is the set{z∈Cd :|z j| = 1 for all 1≤ j≤
d}. IdentifyingCd withR2d, this set is deﬁned by x2
j + y2
j = 1 for all 1≤ j≤ d,
and is thus always a real d-manifold. On the other hand, the unit torus is never
a complex manifold. Whend is odd this follows immediately from the fact that
it has the wrong dimension to be a complex manifold (when d is even then the
concept of tangent spaces, described below, can be used to prove the unit torus
is not a complex manifold). See Exercise A.14 for another example of lack of
complex structure. ◁
A.1.2 Abstract manifolds and projective spaces
Instead of working directly with subsets of Rd or Cd, it is possible to deﬁne
abstract manifolds whose ground sets can be anything. Although the Whitney
embedding theorem states that an abstract d-manifold can be embedded inR2d,
in some cases it is more natural to consider a deﬁnition requiring only a lo-
cal embedding into some real or complex space. In particular, expanding to
abstract manifolds helps us discuss projective spaces, which arise in the for-
mulation of critical points at inﬁnity and the singular integrals of Chapter 11.
LetM be a second-countable Hausdorﬀ space. A chart of dimension d on
M is an open subset U⊂M and a homeomorphism φ from U onto an open
subset of Rd. We say that the chart ( U,φ ) containsp ifp∈ U. Two charts
(U,φ ) and (V,ψ ) are compatible if the transition maps
φ◦ψ−1 :ψ(U∩ V)→φ(U∩ V) and ψ◦φ−1 :φ(U∩ V)→ψ(U∩ V)
A.1 Manifolds 441
are smooth as functions on Rd (this holds trivially when U∩ V =∅), and we
callM a real d-manifold if there exists a collection of pairwise-compatible
charts of dimension d that coverM. Any additional charts that are compatible
with the charts deﬁning a manifold must also be compatible with each other, so
any collection of charts covering a manifold is contained in a uniquely deﬁned
maximal set of compatible charts, known as an atlas. This makes some of the
notation easier by allowing us to assume that for any given p∈M there is a
chart map takingp to the origin inRd, since we can always subtract a constant
from a chart map to obtain another chart map.
Example A.5 (real projective d-space). LetM =
(
Rd+1\ 0
) /
(x↦→ λx) de-
note the set of non-zero vectors modulo non-zero scalar multiples, which can
be identiﬁed with the set of lines through the origin in Rd+1. It is conventional
to write an element of M as ( x0 : x1 : x2 : ··· : xd), with the colons in
place of commas indicating that multiplying every coordinate by a non-zero
real number gives a di ﬀerent representation for the same element. For each
0≤ α≤ d let Uα ={x∈M : xα , 0}, and deﬁne chart maps φα : Uα→ Rd
by φα(x) : = (x j/xα) j,α. This deﬁnes the manifold RPd of real projective d-
space. ◁
Recall from Section 8.2 that if Q is a polynomial in x1,..., xd of total de-
gree m then the homogenization of Q is the polynomial Q(x0, x1,..., xd) =
xm
0 Q(x1/x0,..., xd/x0) in x0, x1,..., xd. Because every monomial appearing in
Q has degree m by construction, Q(λx) = λmQ(x) and the zero set of Q in
Rd is closed under scalar multiples. Thus, Q deﬁnes a real projective variety
VQ ={x∈RPd−1 : Q(x) = 0}.
Exercise A.2. Let Q(x) = 1− x2− y2. (1) What subset of R3 is the union
of equivalence classes making up the real projective variety VQ? (2) Is the
projective varietyVQ a manifold? (3) Intuitively, what simple shape is VQ
equivalent to?
A complex d-manifold is deﬁned analogously to a real d-manifold, except
that the chart maps go to Cd and the transition maps between charts need to
be holomorphic. Analytic functions fromCd toCd are smooth when viewed as
maps fromR2d toR2d, so all complex d-manifolds may be viewed as real (2d)-
manifolds. We also deﬁne the complex projective d-spaceCPd analogously to
real projective space and, overloading notation, useVQ to denote the complex
projective variety deﬁned by a polynomialQ. When writingVQ, we make sure
it is understood whether we are referring to the real or complex projectiviza-
tion.
442 Integration on manifolds
Exercise A.3. Give a description of the complex projective varietyVQ when
Q(x) = 1− x2− y2.
A real m-manifold is called an orientable manifold if it can be covered by
charts (Uα,φα) such that the real transition maps φα◦φ−1
β : φβ(Uα∩ Uβ)→
φα(Uα∩ Uβ) have Jacobian matrices with positive determinants. Such a cover
yields an orientation, which is the set of all chart maps consistent with the
chosen orientation (meaning that all transition maps still have positive Jacobian
determinants).
Exercise A.4. Show that the standard 2-sphere S 2⊆R3 is orientable.
In fact, the notion of orientability is interesting only for real manifolds. The
following classical result follows from the results of Section A.4 below.
Proposition A.6. Every complex manifold is orientable when considered as a
real manifold.
A smooth map between two real manifoldsM andM′ of dimensions m and
n is a function f :M→M ′ such that for any p∈M and any chart maps
φ on a chart ofM containingp andψ on a chart ofM′ containing f (p), the
functionψ◦ f◦φ−1 from a subset of Rm toRn is smooth. Holomorphic maps
between complex manifolds are deﬁned analogously, requiring ψ◦ f◦φ−1 to
be holomorphic instead of smooth.
In this appendix we construct various objects associated with manifolds:
tangent bundles, diﬀerential forms, chain complexes, homology, etc. Without
introducing large amounts of category theory for its own sake, some categorical
terminology is useful because it guides us to what should be true and what
arguments are predictable symbol manipulation – so-called diagram chases
– that can be skipped. In particular, our constructions are functorial. In the
covariant case this means that, in addition to associating an objectG(M) with
each manifoldM, we associate a map G∗( f ) : G(M)→G (M′) with every
map f :M→M ′ between manifolds, having the property that G∗(g◦ f ) =
G∗(g)◦G∗( f ). The mapG∗( f ) between the objects G(M) andG(M′) is said
to be the induced map associated to f . In the contravariant case, the induced
mapG∗( f ) :G(M′)→G (M) goes in the other direction (as indicated by the
raised *) andG∗(g◦ f ) =G∗( f )◦G∗(g).
Exercise A.5. LetG(M) denote the space of smooth real-valued functions on
M. Determine whether this should be viewed as a covariant or contravariant
functor, and deﬁne the mapG∗ orG∗ as the case may be.
Given a manifoldM, anRk-bundle E overM is a map of manifoldsπ : E→
A.2 Vector ﬁelds and di ﬀerential forms 443
M such that E is locally a productM×Rk. More precisely, this means that there
is a collection of open sets U⊆M coveringM and maps φU : U×Rk→ E
satisfying the following conditions.
1. Each φU is a diﬀeomorphism between U×Rk andπ−1(U).
2. π(φU(p,v)) =p for all U andp∈ U.
3. If U and V are two of the open sets covering M and p ∈ U∩ V then
there is an invertible linear transformation g = gU,V,p : Rk→ Rk such that
φU(p,v) = φV(p, g(v)). In other words, the vector space structure on each
ﬁberπ−1(p) is well deﬁned.
The pointp is said to be thebasepoint of any element ofπ−1(p). A section of a
bundle E is a smooth map s :M→ E with s(p)∈π−1(p), which is equivalent
to the statement thatπ◦ s is the identity onM.
Example A.7 (tangent bundle of S 2, intuitively). Before we deﬁne tangent
vectors formally, here is an example to help with intuition. LetM be the sphere
S 2⊆ R3. The tangent bundle ofM is the set of vectors tangent to S 2 begin-
ning at basepoints p ∈ S 2, with the projection operator π taking any such
vector to its basepoint. The Hairy Ball Theorem, ﬁrst proved by Poincar ´e in
1885 [Poi85], states that this tangent bundle has no section that is everywhere
non-zero. Thus, although the tangent bundle is locally diﬀeomorphic to S 2×R2
there is no such global diﬀeomorphism. ◁
We will see that the tangent bundle is functorial: a map f : M → M′
induces a map f∗ between tangent bundles. As you might expect, f∗ maps tan-
gent vectors over the basepoint p to those over f (p) and preserves the notion
of tangency to a curve. Conversely, we will see that the cotangent bundle of a
manifold is a contravariant functor: if f :M→M ′ then the induced map f∗
sends diﬀerential forms onM′ to diﬀerential forms onM. The formal deﬁni-
tions of such objects are full of symbols, but building intuition on key examples
helps greatly with understanding why the constructions are necessary and use-
ful. The reader is encouraged to have a favorite running example that they use
to illustrate the deﬁnitions and constructions as they go through this appendix.
A.2 Vector ﬁelds and di ﬀerential forms
In this section we construct the objects necessary to do calculus on manifolds,
including the tools to integrate functions and residues over contours that are
piecewise submanifolds of algebraic varieties. This involves the use of tangent
444 Integration on manifolds
and cotangent vectors, and the exterior algebra of di ﬀerential forms, so that
integrals are well deﬁned independent of speciﬁc parametrizations.
The constructions in this section formalize the following intuitive notion:
integrating f (x, y, z) dx dy on a surface S involves projecting the surface ele-
ment onto the xy-direction, multiplying by f, and organizing the sum of the
inﬁnitesimal contributions into a two-parameter integral. Describing the sur-
face element without natural coordinates requires the introduction of tangent
vectors, while describing the role ofdx dy in projecting the surface element re-
quires the introduction of cotangent vectors. Together these concepts allow us
to deﬁne integrals along curves, with the framework of exterior algebra extend-
ing this to surface integrals of arbitrary dimension. We know how to integrate
inRd, and within a chart we can map from an abstract manifold to Rd using
a chart map, so we can generalize standard deﬁnitions from Rd provided that
using diﬀerent charts for the same object provides the same answer.
A.2.1 Tangent vectors and vector ﬁelds
In an embedded manifoldM⊂ Rd the tangent space ofM atp is naturally de-
ﬁned as the vector space containing vectors inRd tangent toM atp. Although
thinking about tangent vectors in this manner is concrete, it can be messy to
naturally identify tangent vectors under diﬀerent charts, and it can be diﬃcult
to generalize certain concepts to abstract manifolds. For this reason, we rein-
terpret the tangent space as a collection of (directional) derivatives.
LetM be a real m-manifold. A smooth germ inM at p is an equiva-
lence class of smooth functions deﬁned in neighborhoods of p such that two
functions f on U and g on V are equivalent if there is some neighborhood
W⊆ U∩V ofp for which f|W = g|W. Letting C∞
p (M) denote the set of smooth
germs of real-valued functions onM atp, we deﬁne a derivation onM atp
to be any linear map D : C∞
p (M)→R that satisﬁes the Leibniz property,
D( f g) = (D f)g(p) + f (p)(Dg).
The tangent space ofM at p, denoted Tp(M), is the real vector space of
derivations onM atp. By analogy with embedded manifolds, we call each
element of Tp(M) a tangent vector.
Example A.8. IfM = Rm then Tp(M) = Tp(Rm) is the vector space of
directional derivatives atp. Let x1,..., xm denote the usual coordinates of Rm
and let ∂
∂x1
⏐⏐⏐⏐p
,..., ∂
∂xm
⏐⏐⏐⏐p
be the maps that take a smooth functiong(x) fromRm
A.2 Vector ﬁelds and di ﬀerential forms 445
toR and return its partial derivatives evaluated atx =p. Then
Tp(Rm) =

m∑
k=1
ck
∂
∂xk
⏐⏐⏐⏐⏐p
: ck∈R

and we can identify Tp(Rm) =Rm by the mapping
m∑
k=1
ck
∂
∂xk
⏐⏐⏐⏐⏐p
↔ c∈Rm.
◁
If f :M→M ′ is a smooth map of manifolds then the diﬀerential of f atp
is the map f∗ : TpM→ T f (p)M′ that takes the tangent vector X∈ TpM and
returns the tangent vector f∗X∈ T f (p)M′ such that
( f∗X)(g) = X(g◦ f )∈R for all smooth g :M′→R at f (p).
Exercise A.6. Prove that f∗ is an isomorphism of vector spaces when f is a
diﬀeomorphism.
If (U,φ ) is a chart ofM containingp thenφ is a diﬀeomorphism from U to
Rm, soφ∗ is an isomorphism from TpM to Tφ(p)Rm =Rm. This proves that the
dimension of the tangent space at any point of a manifold is the same as the
dimension of the manifold.
If x1,..., xm are the usual coordinates of Rm then, as seen in Example A.8,
the maps ∂
∂x1
⏐⏐⏐⏐φ(p)
,..., ∂
∂xm
⏐⏐⏐⏐φ(p)
form a natural basis for Tφ(p)Rm. Thus, the tan-
gent vectors∂1,...,∂ m deﬁned by
∂k =φ−1
∗
( ∂
∂xk
⏐⏐⏐⏐⏐φ(p)
)
form a basis for TpM. Becauseφ maps intoRm, we can writeφ = (φ1,...,φ m)
for smooth φk : U → R. To express the dependence of this basis on p and
φ, we write ∂k = ∂
∂φk
⏐⏐⏐⏐p
and call ∂
∂φ1
⏐⏐⏐⏐p
,..., ∂
∂φm
⏐⏐⏐⏐p
the standard basis for TpM
with respect to the chart (U,φ ). Explicitly, for any smooth functiong∈ C∞
p (M)
we have g◦φ−1 :Rm→R and
∂
∂φk
⏐⏐⏐⏐⏐
p
(g) = ∂
∂xk
(
g◦φ−1)⏐⏐⏐⏐⏐x=φ(p)
∈R.
To ease notation we sometimes suppress the basepointp when it is understood,
writing the standard basis as ∂/∂φk, and also use the shorthand ∂
∂φk
⏐⏐⏐⏐p
(g) =
∂g
∂φk
(p).
446 Integration on manifolds
Example A.9. LetM = S 1 = {(x, y) ∈ R2 : x2 + y2 = 1} be the one-
dimensional circle in R2. Suppose U is the half-circle of points in S 1 with
y> 0 andφ is the chart mapφ(x, y) = x with inverseφ−1(x) = (x,
√
1− x2). If
(a, b)∈ U and g is a smooth, real-valued function on a neighborhood of S 1 in
R2, then the chain rule applied to g andφ−1 at (a, b) implies
∂g
∂φ(a, b) = d
dx
[
g
(
x,
√
1− x2
)]⏐⏐⏐⏐⏐x=a
= gx
(
a,
√
1− a2
)
− a√
1− a2
gy
(
a,
√
1− a2
)
= gx(a, b)− a
bgy(a, b).
◁
If f :M→M ′ is a smooth map of manifolds then the diﬀerential of f has
an explicit representation using local coordinates. Let ( U,φ ) be a chart onM
containingp and (V,ψ ) be a chart on M′ containing f (p). Working through
the deﬁnitions above shows that with respect to the bases ∂
∂φk
⏐⏐⏐⏐p
and ∂
∂ψ j
⏐⏐⏐⏐ f (p)
the linear map f∗ : TpM→ T f (p)M′ given by the diﬀerential is represented
by the m× n Jacobian matrix
J( f ) = Jp,φ,ψ( f ) =
(∂(ψ j◦ f )
∂φi
(p)
)
i, j
.
Example A.10. If f : Rm → Rn and we take standard coordinates x =
(x1,..., xm) andy = (y1,..., yn) forRm andRn respectively, then we can write
f = ( f1(x),..., fn(x)) for functions fk : Rm→ R. The Jacobian matrix has
entries ∂(yi◦ f )
∂x j
(p) = ∂ fi
∂x j
(p), so our deﬁnition of the Jacobian generalizes the
deﬁnition from a ﬁrst calculus course. ◁
Proposition A.11 (tangent vectors map functorially) . If f :M→M ′ and
g :M′→M′′ are smooth maps between manifolds then (g◦ f )∗ = g∗◦ f∗.
Exercise A.7. Prove Proposition A.11 using the deﬁnitions above.
Having developed the necessary machinery for the tangent space at a point,
we now deﬁne the tangent bundle of a d-manifoldM whose ground set is the
disjoint union of the tangent spaces at each point,
TM =
⋃
p∈M
TpM,
and whose projection map π : TM→M sends all of Tp(M) to p. For any
A.2 Vector ﬁelds and di ﬀerential forms 447
open U⊂M we write TU = ⋃
p∈U TpM and, if (U,φ ) is a chart on M, we
deﬁne fφ,U : TU→R2d by
fφ,U(v) =
(
(φ◦π)(v),φ∗(v)
)
∈φ(U)× Tφ(π(v))Rd⊂R2d.
It can be shown that as (U,φ ) ranges over an atlas ofM then the collection of
(TU, fφ,U) gives an atlas forTM as a smooth manifold (the main consideration
is proving compatibility of chart maps, which follows straightforwardly from
the deﬁnition of the di ﬀerential using coordinates; see [Tu11, Ch. 12] for a
full derivation). If ( U,φ ) is a chart on M then under this structure the map
v↦→ (π(v),φ∗(v)) is a diﬀeomorphism from TU to U×Rd. The maps φ∗ are
vector space isomorphisms, so that TM is a bundle.
Example A.12. SupposeM =Rd, with the canonical global chartU =Rd and
chart mapφ(x) =x. Unsurprisingly, if we letvp denote the tangent vector atp
that takes a smooth mapg and returns the directional derivative d
dt
⏐⏐⏐t=0 g(p+ tv)
then fφ,U(vp) = (p,v). Thus, TRd has a global product structure and (in this
trivial case) there is a canonical isomorphism between two di ﬀerent tangent
spaces Tp(Rd) and Tp′(Rd). ◁
Example A.13. LetM = S 2. If TM had a global product structure, i.e., if
there existed an isomorphism f :M×R2→ TM, then the map s(p) = f (p, e1)
would deﬁne a smooth global non-zero section ofTM, contradicting the Hairy
Ball Theorem (see Example A.7). Thus, the tangent bundle of the sphere S 2
does not admit a global product structure. ◁
A smooth vector ﬁeld onM is a section ofTM. In other words, a vector ﬁeld
is a smooth mapX that takesp∈M and returns a tangent vectorXp∈ TpM. If
(U,φ ) is a chart onM then for anyp∈ U the tangent vectors ∂
∂φ1
⏐⏐⏐⏐p
,..., ∂
∂φm
⏐⏐⏐⏐p
form a basis for TpM. Thus, for any map X :M→ TM with Xp∈ TpM we
can write
Xp =
m∑
k=1
ck(p) ∂
∂φk
⏐⏐⏐⏐⏐
p
for allp∈ U,
which deﬁnes coe ﬃcient maps ck : U→ R. The mapping X is a vector ﬁeld
(i.e., is smooth) if and only if the coe ﬃcient maps ck constructed this way are
all smooth as (U,φ ) ranges over the charts ofM.
A.2.2 Cotangent vectors and 1-forms
Having deﬁned what we need for tangent vectors, we now deﬁne cotangent
vectors by dualizing everything. It can be diﬃcult to build intuition as to why
448 Integration on manifolds
calculus on manifolds requires the extra complexity introduced by dualizing.
Roughly speaking, when there is no canonical parametrization for a manifold
then the inﬁnitesimal elements such as dx, dA, and dV that arise in integra-
tion must be deﬁned in a way that is independent of parametrization. Cotan-
gent vectors act functorially on tangent vectors, which in turn act functorially
on smooth functions, to produce numerical results invariant under changes of
parametrization. We recommend the reader work through the examples in the
section on integration below, when they come to it, to help understand how to
do computations.
Deﬁnition A.14 (Cotangent vectors). LetM be an m-manifold. The cotan-
gent space toM atp is the dual space TpM to TpM. In other words, TpM
is the space of linear maps from TpM to R. If ( U,φ ) is a chart of M con-
tainingp then the standard basis for TpM with respect to ( U,φ ) is the basis
{dφ1|p,..., dφm|p} dual to the standard basis for TpM with respect to ( U,φ ).
In other words, the standard basis for the dual is deﬁned by setting
(dφi|p)

∂
∂φ j
⏐⏐⏐⏐⏐⏐p
 =

1 if i = j
0 otherwise
and extending linearly. As we did for tangent vectors, we often drop the base-
pointp from our notation when it is understood.
Analogously to our construction of the tangent bundle of anm-manifoldM,
we deﬁne the cotangent bundle T∗M whose ground set is the disjoint union
of the cotangent spaces at each point,
T∗M =
⋃
p∈M
TpM,
and whose projection map π : TM→M sends all of Tp(M) top. If (U,φ )
is a chart on M then any cotangent vector v with π(v) ∈ U is an R-linear
combinationv = ∑
k ck(v)dφk|π(v). Analogously to the tangent bundle TM, a
smooth structure can be put on T∗M using maps of the form
v↦→
(
(φ◦π)(v), c1(v),..., cm(v)
)
∈φ(U)×Rm⊂R2m,
wherev ranges overv∈ T∗M with π(v)∈ U. Under this structure the map
v↦→ (π(v), c1(v),..., cm(v)) is a local di ﬀeomorphism when restricted to the
bundle T∗U over chart neighborhoods. Changing charts preserves the vector
space structure, so T∗M is a bundle.
We can use the diﬀerential on tangent spaces to deﬁne a dual map on cotan-
gent spaces. LetM andM′ be manifolds withp∈M , let f :M→M ′ be a
smooth map, and let ξ∈ T f (p)M′ be a cotangent vector. Thenξ maps tangent
A.2 Vector ﬁelds and di ﬀerential forms 449
vectors in T f (p)M′ toR, so the composition f∗(ξ) =ξ◦ f∗ ofξ with the diﬀer-
ential of f is a map from TpM toR, which is a cotangent vector in TpM. In
other words, we have constructed a contravariant map f∗ : T f (p)M′→ TpM,
known as the pullback by f .
Exercise A.8. Let f :M→M ′ and g :M′→M ′′ be smooth maps. Prove
that (g◦ f )∗ = f∗◦ g∗.
The pullback can be computed explicitly in local coordinates. Suppose (U,φ )
is a chart ofM containingp and let (V,ψ ) be a chart onM′ containing f (p).
We have seen above that the di ﬀerential of f∗ with respect to the standard
bases{∂/∂φi} and{∂/∂ψ j} of TpM and T f (p)M′ in these charts is given by
left-multiplication of the Jacobian matrix J( f ). Plugging in the deﬁnition of
f∗,
f∗(dψi)
( ∂
∂φ j
)
= (dψi)
(
f∗
( ∂
∂φ j
))
= (dψi)

∑
k
∂(ψk◦ f )
∂φ j
(p) ∂
∂ψk

= ∂(ψi◦ f )
∂φ j
(p).
In other words, with respect to the dual bases {dφ j} and{dψi} the linear map
f∗ is deﬁned through right-multiplication by the Jacobian matrix.
IfM is a manifold then a diﬀerential 1-form onM is a section on T∗M.
In other words, a 1-form is a smooth map ω that takesp∈M and returns a
cotangent vectorω|p∈ TpM. If f :M→ R is a smooth function onM then
the diﬀerential of f is the 1-form d f :M→ T∗M deﬁned by
(d f|p)(Xp) = Xp( f ) for all p∈M and Xp∈ TpM.
Remark A.15. When x is the standard coordinate on R and we take p∈M
and Xp∈ TpM then
f∗(Xp) = (d f|p)(Xp) d
dx
⏐⏐⏐⏐⏐ f (p)
,
where f∗ : TpM→ T f (p)R is the di ﬀerential of f deﬁned previously. Thus,
both of our deﬁnitions of the diﬀerential agree under the identiﬁcationT f (p)R =
R given by the standard basis of the tangent space (see Example A.12).
If (U,φ ) is a chart on M then for any p∈ U the cotangent vectors dφ1|p,
..., dφm|p form a basis for TpM. Thus, for any map ω :M→ T∗M with
450 Integration on manifolds
ω|p∈ TpM we can write
ω|p =
m∑
k=1
ck(p) dφk|p for allp∈ U,
which deﬁnes coeﬃcient maps ck : U→ R. The mapping ω is a 1-form (i.e.,
is smooth) if and only if the coe ﬃcient maps constructed in this way are all
smooth as (U,φ ) ranges over the charts ofM.
A.2.3 Di ﬀerential k-forms
The concept of a diﬀerential form will allow us to integrate on manifolds, how-
ever 1-forms will only allow us to integrate on one-dimensional manifolds (i.e.,
curves). To integrate on higher-dimensional surfaces, we need to generalize 1-
forms to higher-dimensional objects. The necessary algebra can be developed
for any vector space V, although we use it only in the case when V = TpM is
the cotangent space of a manifold.
Let V be a d-dimensional real vector space. A k-form on V is a multi-linear
map α : Vk → R which is antisymmetric: swapping any two arguments of
α negates the value of the map. Note that linearity and antisymmetry imply
that the only k-form when k > d is the zero map. The vector space of k-forms
over V is denoted Λk(V), and the direct sum Λ(V) =
⨁d
k=1 Λk(V) is called
the exterior algebra of V. To give Λ(V) a ring structure, we deﬁne the wedge
product of k 1-formsα1,...,α k∈ Λ1(V) to be thek-formα1∧···∧ αk : Vk→R
determined by
(α1∧···∧ αk)(v1,..., vk) = det
(
αi(v j)
)
for allv∈ Vk.
Ifα1,...,α d are 1-forms and I∈{ 1,..., d}r then we writeαI =αi1∧···∧ αir.
Whenα1,...,α d form a basis for Λ1(V) = V then the k-formsαI, where I =
(i1,..., ik) with i1 < i2 <··· < ik, form a basis for Λk(V). Thus, the vector
space of k-forms has dimension
(d
k
)
and∧ deﬁnes a bilinear associative product
on Λ(V) which is anticommutative: if α is an a-form and β is a b-form then
α∧β = (−1)abβ∧α.
Example A.16. The space ofd-forms has dimension one, and is thus generated
by the determinant. ◁
Example A.17. Let x and y be the usual coordinates onM =R2 and V = T 0M
be the cotangent space ofR2 at the origin. Since the diﬀerentials dx and dy span
V, any 1-form on V can be written a dx + b dy for a, b∈R. The wedge product
A.2 Vector ﬁelds and di ﬀerential forms 451
of two 1-forms is computed by
(a dx + b dy)∧ (p dx + q dy) = ap(dx∧ dx) + aq(dx∧ dy)
+ bp(dy∧ dx) + bq(dy∧ dy)
= aq(dx∧ dy) + bp(dy∧ dx)
= (aq− bp)(dx∧ dy),
where dx∧ dx = dy∧ dy = 0 by anticommutativity. ◁
Bringing our discussion back to di ﬀerential geometry, letM be a smooth
m-manifold. For any 1 ≤ k≤ m the exterior k-algebra bundle ofM whose
ground set is the disjoint union
Λk(M) =
⋃
p∈M
Λk(Tp(M))
is deﬁned by the projection map π that takes ν ∈ Λk(Tp(M)) and returns
π(ν) = p. If ( U,φ ) is a chart on M then for any p∈ U the cotangent vec-
tors dφ1|p,..., dφm|p form a basis for Tp(M). Thus, the k-forms dφI|p =
dφi1|p∧···∧ dφik|p form a basis forΛk(Tp(M)) as I ranges over strictly increas-
ing tuples in{1,..., m}k. For any map ω :M→ Λk(M) with ω|p∈ Tp(M)
this means we can writeω as a sum over dΦI as I ranges over subsets of [d] of
cardinality k,
ω|p =
∑
|I|=k
cI(p) dφI|p for allp∈ U.
As for the tangent and cotangent bundles, we can give Λk(M) a smooth struc-
ture using charts (U,φ ) and the coeﬃcient functions cI. A diﬀerential k-form
onM is a section of Λk(M) under this structure, and a mapping from M to
Λk(M) is a di ﬀerential k-form if and only if the coe ﬃcient maps cI are all
smooth as (U,φ ) ranges over the charts ofM. The set of diﬀerential k-forms is
denoted Ek(M) and the union of the Ek(M) over all k is denoted E∗(M). From
now on we restrict to this diﬀerential setting and use the terms k-form and dif-
ferential k-form interchangeably. A top level form on a manifold of dimension
m is any m-form.
Example A.18. Once again, letM = S 1 be the one-dimensional circle in the
plane, let U be the halfcircle of points in S 1 with y > 0, and letφ be the chart
map φ(x, y) = x with inverse φ−1(x) = (x,
√
1− x2). If ω is a 1-form on S 1
then for (a, b)∈ U we can write ω|a,b = f (a, b)dφ|a,b, where f (x, y) is smooth
at (a, b). The criterion of smoothness means the real function ( f◦φ−1)(x) =
f (x,
√
1− x2) is smooth at x = a. ◁
452 Integration on manifolds
Exercise A.9. Let (U,φ ) be a chart onM and f1,..., fk : U→ R. Show that
the wedge product of diﬀerentials satisﬁes
(d f1)∧···∧ (d fk) =
∑
|I|=k
det JI(f,φ ) dφI,
where JI(f,φ ) is the Jacobian matrixJI(f,φ ) =
(
∂ fa
∂φib
)
1≤a,b≤k
when I = (i1,..., ik)
with i1 <··· < ik.
Let f : M → M′ be a smooth map of manifolds. If p ∈ Mthen we
saw above how to deﬁne the pullback f∗ : T f (p)M′ → TpM of cotangent
vectors from M′ toM. Working pointwise, we can also deﬁne a pullback
f∗ : Ek(M′)→ Ek(M) on forms. Concretely, ifω is a k-form onM′ then the
pullback ofω by f is the k-form f∗ω onM deﬁned for eachp∈M by
( f∗ω)|p(X1,..., Xk) =ω| f (p)( f∗X1,..., f∗Xk) for all X1,..., Xk∈ TpM.
We also deﬁne the pullback of a smooth function (which can be considered a
0-form) g :M′→R by f∗g = g◦ f . Basic properties of the pullback include
• distributivity over addition: f∗(ω +τ) = f∗ω + f∗τ,
• distributivity over wedge product: f∗(ω∧τ) = ( f∗ω)∧ ( f∗τ),
• commutativity with the diﬀerential: f∗(dg) = d( f∗g).
Example A.19. LetM =M′ = Rd with standard coordinates x1,..., xd and
let f :Rd→Rd be smooth, so f = ( f1,..., fd) with each f j :Rd→R smooth.
Ifω is a top level form onRd (i.e., a d-form) thenω = a(x) dx1∧···∧ dxd for
some smooth a :Rd→R. Since f∗xk = xk◦ f = fk, the pullback ofω under f
is given by the Jacobian determinant of f ,
f∗ω = f∗(a(x) dx1∧···∧ dxd) = a( f (x)) d( f∗x1)∧···∧ d( f∗xd)
= a( f (x)) (d f1)∧···∧ (d fd)
= a( f (x)) det
(∂ f j
∂xi
)
(dx1∧···∧ dxd),
where the ﬁnal equality follows from Exercise A.9. ◁
