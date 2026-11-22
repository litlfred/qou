---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-081-vector-fields-and-differential-forms
section_title: "Vector fields and differential forms"
section_number: null
pages: 461-470
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
443
M such that E is locally a product M×Rk. More precisely, this means that there
is a collection of open sets U ⊆M covering M and maps φU : U × Rk →E
satisfying the following conditions.
1. Each φU is a diﬀeomorphism between U × Rk and π−1(U).
2. π(φU(p, v)) = p for all U and p ∈U.
3. If U and V are two of the open sets covering M and p ∈U ∩V then
there is an invertible linear transformation g = gU,V,p : Rk →Rk such that
φU(p, v) = φV(p, g(v)). In other words, the vector space structure on each
ﬁber π−1(p) is well deﬁned.
The point p is said to be the basepoint of any element of π−1(p). A section of a
bundle E is a smooth map s : M →E with s(p) ∈π−1(p), which is equivalent
to the statement that π ◦s is the identity on M.
Example A.7 (tangent bundle of S 2, intuitively). Before we deﬁne tangent
vectors formally, here is an example to help with intuition. Let M be the sphere
S 2 ⊆R3. The tangent bundle of M is the set of vectors tangent to S 2 begin-
ning at basepoints p ∈S 2, with the projection operator π taking any such
vector to its basepoint. The Hairy Ball Theorem, ﬁrst proved by Poincar´e in
1885 [Poi85], states that this tangent bundle has no section that is everywhere
non-zero. Thus, although the tangent bundle is locally diﬀeomorphic to S 2×R2
there is no such global diﬀeomorphism.
◁
We will see that the tangent bundle is functorial: a map f : M →M′
induces a map f∗between tangent bundles. As you might expect, f∗maps tan-
gent vectors over the basepoint p to those over f(p) and preserves the notion
of tangency to a curve. Conversely, we will see that the cotangent bundle of a
manifold is a contravariant functor: if f : M →M′ then the induced map f ∗
sends diﬀerential forms on M′ to diﬀerential forms on M. The formal deﬁni-
tions of such objects are full of symbols, but building intuition on key examples
helps greatly with understanding why the constructions are necessary and use-
ful. The reader is encouraged to have a favorite running example that they use
to illustrate the deﬁnitions and constructions as they go through this appendix.
A.2 Vector ﬁelds and diﬀerential forms
In this section we construct the objects necessary to do calculus on manifolds,
including the tools to integrate functions and residues over contours that are
piecewise submanifolds of algebraic varieties. This involves the use of tangent
444
Integration on manifolds
and cotangent vectors, and the exterior algebra of diﬀerential forms, so that
integrals are well deﬁned independent of speciﬁc parametrizations.
The constructions in this section formalize the following intuitive notion:
integrating f(x, y, z) dx dy on a surface S involves projecting the surface ele-
ment onto the xy-direction, multiplying by f, and organizing the sum of the
inﬁnitesimal contributions into a two-parameter integral. Describing the sur-
face element without natural coordinates requires the introduction of tangent
vectors, while describing the role of dx dy in projecting the surface element re-
quires the introduction of cotangent vectors. Together these concepts allow us
to deﬁne integrals along curves, with the framework of exterior algebra extend-
ing this to surface integrals of arbitrary dimension. We know how to integrate
in Rd, and within a chart we can map from an abstract manifold to Rd using
a chart map, so we can generalize standard deﬁnitions from Rd provided that
using diﬀerent charts for the same object provides the same answer.
A.2.1 Tangent vectors and vector ﬁelds
In an embedded manifold M ⊂Rd the tangent space of M at p is naturally de-
ﬁned as the vector space containing vectors in Rd tangent to M at p. Although
thinking about tangent vectors in this manner is concrete, it can be messy to
naturally identify tangent vectors under diﬀerent charts, and it can be diﬃcult
to generalize certain concepts to abstract manifolds. For this reason, we rein-
terpret the tangent space as a collection of (directional) derivatives.
Let M be a real m-manifold. A smooth germ in M at p is an equiva-
lence class of smooth functions deﬁned in neighborhoods of p such that two
functions f on U and g on V are equivalent if there is some neighborhood
W ⊆U ∩V of p for which f|W = g|W. Letting C∞
p (M) denote the set of smooth
germs of real-valued functions on M at p, we deﬁne a derivation on M at p
to be any linear map D : C∞
p (M) →R that satisﬁes the Leibniz property,
D( fg) = (Df)g(p) + f(p)(Dg).
The tangent space of M at p, denoted Tp(M), is the real vector space of
derivations on M at p. By analogy with embedded manifolds, we call each
element of Tp(M) a tangent vector.
Example A.8. If M = Rm then Tp(M) = Tp(Rm) is the vector space of
directional derivatives at p. Let x1, . . . , xm denote the usual coordinates of Rm
and let
∂
∂x1

p , . . . ,
∂
∂xm

p be the maps that take a smooth function g(x) from Rm
A.2 Vector ﬁelds and diﬀerential forms
445
to R and return its partial derivatives evaluated at x = p. Then
Tp(Rm) =

m
X
k=1
ck
∂
∂xk

p
: ck ∈R

and we can identify Tp(Rm) = Rm by the mapping
m
X
k=1
ck
∂
∂xk

p
↔
c ∈Rm.
◁
If f : M →M′ is a smooth map of manifolds then the diﬀerential of f at p
is the map f∗: TpM →T f(p)M′ that takes the tangent vector X ∈TpM and
returns the tangent vector f∗X ∈T f(p)M′ such that
( f∗X)(g) = X(g ◦f) ∈R
for all smooth g : M′ →R at f(p).
Exercise A.6. Prove that f∗is an isomorphism of vector spaces when f is a
diﬀeomorphism.
If (U, φ) is a chart of M containing p then φ is a diﬀeomorphism from U to
Rm, so φ∗is an isomorphism from TpM to Tφ(p)Rm = Rm. This proves that the
dimension of the tangent space at any point of a manifold is the same as the
dimension of the manifold.
If x1, . . . , xm are the usual coordinates of Rm then, as seen in Example A.8,
the maps
∂
∂x1

φ(p) , . . . ,
∂
∂xm

φ(p) form a natural basis for Tφ(p)Rm. Thus, the tan-
gent vectors ∂1, . . . , ∂m deﬁned by
∂k = φ−1
∗
 ∂
∂xk

φ(p)
!
form a basis for TpM. Because φ maps into Rm, we can write φ = (φ1, . . . , φm)
for smooth φk : U →R. To express the dependence of this basis on p and
φ, we write ∂k =
∂
∂φk

p and call
∂
∂φ1

p , . . . ,
∂
∂φm

p the standard basis for TpM
with respect to the chart (U, φ). Explicitly, for any smooth function g ∈C∞
p (M)
we have g ◦φ−1 : Rm →R and
∂
∂φk

p
(g) =
∂
∂xk

g ◦φ−1

x=φ(p)
∈R.
To ease notation we sometimes suppress the basepoint p when it is understood,
writing the standard basis as ∂/∂φk, and also use the shorthand
∂
∂φk

p (g) =
∂g
∂φk (p).
446
Integration on manifolds
Example A.9. Let M = S 1 = {(x, y) ∈R2 : x2 + y2 = 1} be the one-
dimensional circle in R2. Suppose U is the half-circle of points in S 1 with
y > 0 and φ is the chart map φ(x, y) = x with inverse φ−1(x) = (x,
√
1 −x2). If
(a, b) ∈U and g is a smooth, real-valued function on a neighborhood of S 1 in
R2, then the chain rule applied to g and φ−1 at (a, b) implies
∂g
∂φ(a, b) = d
dx
h
g

x,
√
1 −x2i

x=a
= gx

a,
√
1 −a2
−
a
√
1 −a2 gy

a,
√
1 −a2
= gx(a, b) −a
bgy(a, b).
◁
If f : M →M′ is a smooth map of manifolds then the diﬀerential of f has
an explicit representation using local coordinates. Let (U, φ) be a chart on M
containing p and (V, ψ) be a chart on M′ containing f(p). Working through
the deﬁnitions above shows that with respect to the bases
∂
∂φk

p and
∂
∂ψj

f(p)
the linear map f∗: TpM →T f(p)M′ given by the diﬀerential is represented
by the m × n Jacobian matrix
J( f) = Jp,φ,ψ( f) =
 ∂(ψ j ◦f)
∂φi
(p)
!
i, j
.
Example A.10. If f : Rm →Rn and we take standard coordinates x =
(x1, . . . , xm) and y = (y1, . . . , yn) for Rm and Rn respectively, then we can write
f = ( f1(x), . . . , fn(x)) for functions fk : Rm →R. The Jacobian matrix has
entries ∂(yi◦f)
∂xj (p) =
∂fi
∂x j (p), so our deﬁnition of the Jacobian generalizes the
deﬁnition from a ﬁrst calculus course.
◁
Proposition A.11 (tangent vectors map functorially). If f : M →M′ and
g : M′ →M′′ are smooth maps between manifolds then (g ◦f)∗= g∗◦f∗.
Exercise A.7. Prove Proposition A.11 using the deﬁnitions above.
Having developed the necessary machinery for the tangent space at a point,
we now deﬁne the tangent bundle of a d-manifold M whose ground set is the
disjoint union of the tangent spaces at each point,
TM =
[
p∈M
TpM ,
and whose projection map π : TM →M sends all of Tp(M) to p. For any
A.2 Vector ﬁelds and diﬀerential forms
447
open U ⊂M we write TU = S
p∈U TpM and, if (U, φ) is a chart on M, we
deﬁne fφ,U : TU →R2d by
fφ,U(v) =

(φ ◦π)(v), φ∗(v)

∈φ(U) × Tφ(π(v))Rd ⊂R2d .
It can be shown that as (U, φ) ranges over an atlas of M then the collection of
(TU, fφ,U) gives an atlas for TM as a smooth manifold (the main consideration
is proving compatibility of chart maps, which follows straightforwardly from
the deﬁnition of the diﬀerential using coordinates; see [Tu11, Ch. 12] for a
full derivation). If (U, φ) is a chart on M then under this structure the map
v 7→(π(v), φ∗(v)) is a diﬀeomorphism from TU to U × Rd. The maps φ∗are
vector space isomorphisms, so that TM is a bundle.
Example A.12. Suppose M = Rd, with the canonical global chart U = Rd and
chart map φ(x) = x. Unsurprisingly, if we let vp denote the tangent vector at p
that takes a smooth map g and returns the directional derivative
d
dt

t=0 g(p+tv)
then fφ,U(vp) = (p, v). Thus, TRd has a global product structure and (in this
trivial case) there is a canonical isomorphism between two diﬀerent tangent
spaces Tp(Rd) and Tp′(Rd).
◁
Example A.13. Let M = S 2. If TM had a global product structure, i.e., if
there existed an isomorphism f : M×R2 →TM, then the map s(p) = f(p, e1)
would deﬁne a smooth global non-zero section of TM, contradicting the Hairy
Ball Theorem (see Example A.7). Thus, the tangent bundle of the sphere S 2
does not admit a global product structure.
◁
A smooth vector ﬁeld on M is a section of TM. In other words, a vector ﬁeld
is a smooth map X that takes p ∈M and returns a tangent vector Xp ∈TpM. If
(U, φ) is a chart on M then for any p ∈U the tangent vectors
∂
∂φ1

p , . . . ,
∂
∂φm

p
form a basis for TpM. Thus, for any map X : M →TM with Xp ∈TpM we
can write
Xp =
m
X
k=1
ck(p)
∂
∂φk

p
for all p ∈U,
which deﬁnes coeﬃcient maps ck : U →R. The mapping X is a vector ﬁeld
(i.e., is smooth) if and only if the coeﬃcient maps ck constructed this way are
all smooth as (U, φ) ranges over the charts of M.
A.2.2 Cotangent vectors and 1-forms
Having deﬁned what we need for tangent vectors, we now deﬁne cotangent
vectors by dualizing everything. It can be diﬃcult to build intuition as to why
448
Integration on manifolds
calculus on manifolds requires the extra complexity introduced by dualizing.
Roughly speaking, when there is no canonical parametrization for a manifold
then the inﬁnitesimal elements such as dx, dA, and dV that arise in integra-
tion must be deﬁned in a way that is independent of parametrization. Cotan-
gent vectors act functorially on tangent vectors, which in turn act functorially
on smooth functions, to produce numerical results invariant under changes of
parametrization. We recommend the reader work through the examples in the
section on integration below, when they come to it, to help understand how to
do computations.
Deﬁnition A.14 (Cotangent vectors). Let M be an m-manifold. The cotan-
gent space to M at p is the dual space T pM to TpM. In other words, T pM
is the space of linear maps from TpM to R. If (U, φ) is a chart of M con-
taining p then the standard basis for T pM with respect to (U, φ) is the basis
{dφ1|p, . . . , dφm|p} dual to the standard basis for TpM with respect to (U, φ).
In other words, the standard basis for the dual is deﬁned by setting
(dφi|p)

∂
∂φj

p
=

1
if i = j
0
otherwise
and extending linearly. As we did for tangent vectors, we often drop the base-
point p from our notation when it is understood.
Analogously to our construction of the tangent bundle of an m-manifold M,
we deﬁne the cotangent bundle T ∗M whose ground set is the disjoint union
of the cotangent spaces at each point,
T ∗M =
[
p∈M
T pM ,
and whose projection map π : TM →M sends all of T p(M) to p. If (U, φ)
is a chart on M then any cotangent vector v with π(v) ∈U is an R-linear
combination v = P
k ck(v)dφk|π(v). Analogously to the tangent bundle TM, a
smooth structure can be put on T ∗M using maps of the form
v 7→

(φ ◦π)(v), c1(v), . . . , cm(v)

∈φ(U) × Rm ⊂R2m ,
where v ranges over v ∈T ∗M with π(v) ∈U. Under this structure the map
v 7→(π(v), c1(v), . . . , cm(v)) is a local diﬀeomorphism when restricted to the
bundle T ∗U over chart neighborhoods. Changing charts preserves the vector
space structure, so T ∗M is a bundle.
We can use the diﬀerential on tangent spaces to deﬁne a dual map on cotan-
gent spaces. Let M and M′ be manifolds with p ∈M, let f : M →M′ be a
smooth map, and let ξ ∈T f(p)M′ be a cotangent vector. Then ξ maps tangent
A.2 Vector ﬁelds and diﬀerential forms
449
vectors in T f(p)M′ to R, so the composition f ∗(ξ) = ξ ◦f∗of ξ with the diﬀer-
ential of f is a map from TpM to R, which is a cotangent vector in T pM. In
other words, we have constructed a contravariant map f ∗: T f(p)M′ →T pM,
known as the pullback by f.
Exercise A.8. Let f : M →M′ and g : M′ →M′′ be smooth maps. Prove
that (g ◦f)∗= f ∗◦g∗.
The pullback can be computed explicitly in local coordinates. Suppose (U, φ)
is a chart of M containing p and let (V, ψ) be a chart on M′ containing f(p).
We have seen above that the diﬀerential of f∗with respect to the standard
bases {∂/∂φi} and {∂/∂ψ j} of TpM and T f(p)M′ in these charts is given by
left-multiplication of the Jacobian matrix J( f). Plugging in the deﬁnition of
f ∗,
f ∗(dψi)
 ∂
∂φ j
!
= (dψi)
 
f∗
 ∂
∂φj
!!
= (dψi)

X
k
∂(ψk ◦f)
∂φ j
(p) ∂
∂ψk

= ∂(ψi ◦f)
∂φ j
(p) .
In other words, with respect to the dual bases {dφj} and {dψi} the linear map
f ∗is deﬁned through right-multiplication by the Jacobian matrix.
If M is a manifold then a diﬀerential 1-form on M is a section on T ∗M.
In other words, a 1-form is a smooth map ω that takes p ∈M and returns a
cotangent vector ω|p ∈T pM. If f : M →R is a smooth function on M then
the diﬀerential of f is the 1-form d f : M →T ∗M deﬁned by
(d f|p)(Xp) = Xp( f) for all p ∈M and Xp ∈TpM.
Remark A.15. When x is the standard coordinate on R and we take p ∈M
and Xp ∈TpM then
f∗(Xp) = (d f|p)(Xp) d
dx

f(p)
,
where f∗: TpM →T f(p)R is the diﬀerential of f deﬁned previously. Thus,
both of our deﬁnitions of the diﬀerential agree under the identiﬁcation T f(p)R =
R given by the standard basis of the tangent space (see Example A.12).
If (U, φ) is a chart on M then for any p ∈U the cotangent vectors dφ1|p,
. . . , dφm|p form a basis for T pM. Thus, for any map ω : M →T ∗M with
450
Integration on manifolds
ω|p ∈T pM we can write
ω|p =
m
X
k=1
ck(p) dφk|p
for all p ∈U,
which deﬁnes coeﬃcient maps ck : U →R. The mapping ω is a 1-form (i.e.,
is smooth) if and only if the coeﬃcient maps constructed in this way are all
smooth as (U, φ) ranges over the charts of M.
A.2.3 Diﬀerential k-forms
The concept of a diﬀerential form will allow us to integrate on manifolds, how-
ever 1-forms will only allow us to integrate on one-dimensional manifolds (i.e.,
curves). To integrate on higher-dimensional surfaces, we need to generalize 1-
forms to higher-dimensional objects. The necessary algebra can be developed
for any vector space V, although we use it only in the case when V = T pM is
the cotangent space of a manifold.
Let V be a d-dimensional real vector space. A k-form on V is a multi-linear
map α : Vk →R which is antisymmetric: swapping any two arguments of
α negates the value of the map. Note that linearity and antisymmetry imply
that the only k-form when k > d is the zero map. The vector space of k-forms
over V is denoted Λk(V), and the direct sum Λ(V) =
Ld
k=1 Λk(V) is called
the exterior algebra of V. To give Λ(V) a ring structure, we deﬁne the wedge
product of k 1-forms α1, . . . , αk ∈Λ1(V) to be the k-form α1∧· · ·∧αk : Vk →R
determined by
(α1 ∧· · · ∧αk)(v1, . . . , vk) = det

αi(vj)

for all v ∈Vk.
If α1, . . . , αd are 1-forms and I ∈{1, . . . , d}r then we write αI = αi1 ∧· · · ∧αir.
When α1, . . . , αd form a basis for Λ1(V) = V then the k-forms αI, where I =
(i1, . . . , ik) with i1 < i2 < · · · < ik, form a basis for Λk(V). Thus, the vector
space of k-forms has dimension
d
k

and ∧deﬁnes a bilinear associative product
on Λ(V) which is anticommutative: if α is an a-form and β is a b-form then
α ∧β = (−1)abβ ∧α.
Example A.16. The space of d-forms has dimension one, and is thus generated
by the determinant.
◁
Example A.17. Let x and y be the usual coordinates on M = R2 and V = T 0M
be the cotangent space of R2 at the origin. Since the diﬀerentials dx and dy span
V, any 1-form on V can be written a dx + b dy for a, b ∈R. The wedge product
A.2 Vector ﬁelds and diﬀerential forms
451
of two 1-forms is computed by
(a dx + b dy) ∧(p dx + q dy) = ap(dx ∧dx) + aq(dx ∧dy)
+ bp(dy ∧dx) + bq(dy ∧dy)
= aq(dx ∧dy) + bp(dy ∧dx)
= (aq −bp)(dx ∧dy),
where dx ∧dx = dy ∧dy = 0 by anticommutativity.
◁
Bringing our discussion back to diﬀerential geometry, let M be a smooth
m-manifold. For any 1 ≤k ≤m the exterior k-algebra bundle of M whose
ground set is the disjoint union
Λk(M) =
[
p∈M
Λk(T p(M))
is deﬁned by the projection map π that takes ν ∈Λk(T p(M)) and returns
π(ν) = p. If (U, φ) is a chart on M then for any p ∈U the cotangent vec-
tors dφ1|p, . . . , dφm|p form a basis for T p(M). Thus, the k-forms dφI|p =
dφi1|p∧· · ·∧dφik|p form a basis for Λk(T p(M)) as I ranges over strictly increas-
ing tuples in {1, . . . , m}k. For any map ω : M →Λk(M) with ω|p ∈T p(M)
this means we can write ω as a sum over dΦI as I ranges over subsets of [d] of
cardinality k,
ω|p =
X
|I|=k
cI(p) dφI|p
for all p ∈U .
As for the tangent and cotangent bundles, we can give Λk(M) a smooth struc-
ture using charts (U, φ) and the coeﬃcient functions cI. A diﬀerential k-form
on M is a section of Λk(M) under this structure, and a mapping from M to
Λk(M) is a diﬀerential k-form if and only if the coeﬃcient maps cI are all
smooth as (U, φ) ranges over the charts of M. The set of diﬀerential k-forms is
denoted Ek(M) and the union of the Ek(M) over all k is denoted E∗(M). From
now on we restrict to this diﬀerential setting and use the terms k-form and dif-
ferential k-form interchangeably. A top level form on a manifold of dimension
m is any m-form.
Example A.18. Once again, let M = S 1 be the one-dimensional circle in the
plane, let U be the halfcircle of points in S 1 with y > 0, and let φ be the chart
map φ(x, y) = x with inverse φ−1(x) = (x,
√
1 −x2). If ω is a 1-form on S 1
then for (a, b) ∈U we can write ω|a,b = f(a, b)dφ|a,b, where f(x, y) is smooth
at (a, b). The criterion of smoothness means the real function ( f ◦φ−1)(x) =
f(x,
√
1 −x2) is smooth at x = a.
◁
452
Integration on manifolds
Exercise A.9. Let (U, φ) be a chart on M and f1, . . . , fk : U →R. Show that
the wedge product of diﬀerentials satisﬁes
(d f1) ∧· · · ∧(d fk) =
X
|I|=k
det JI(f, φ) dφI,
where JI(f, φ) is the Jacobian matrix JI(f, φ) =

∂fa
∂φib

1≤a,b≤k when I = (i1, . . . , ik)
with i1 < · · · < ik.
Let f : M →M′ be a smooth map of manifolds. If p ∈M then we
saw above how to deﬁne the pullback f ∗: T f(p)M′ →T pM of cotangent
vectors from M′ to M. Working pointwise, we can also deﬁne a pullback
f ∗: Ek(M′) →Ek(M) on forms. Concretely, if ω is a k-form on M′ then the
pullback of ω by f is the k-form f ∗ω on M deﬁned for each p ∈M by
( f ∗ω)|p(X1, . . . , Xk) = ω| f(p)( f∗X1, . . . , f∗Xk)
for all X1, . . . , Xk ∈TpM.
We also deﬁne the pullback of a smooth function (which can be considered a
0-form) g : M′ →R by f ∗g = g ◦f. Basic properties of the pullback include
• distributivity over addition: f ∗(ω + τ) = f ∗ω + f ∗τ,
• distributivity over wedge product: f ∗(ω ∧τ) = ( f ∗ω) ∧( f ∗τ),
• commutativity with the diﬀerential: f ∗(dg) = d( f ∗g).
Example A.19. Let M = M′ = Rd with standard coordinates x1, . . . , xd and
let f : Rd →Rd be smooth, so f = ( f1, . . . , fd) with each f j : Rd →R smooth.
If ω is a top level form on Rd (i.e., a d-form) then ω = a(x) dx1 ∧· · · ∧dxd for
some smooth a : Rd →R. Since f ∗xk = xk ◦f = fk, the pullback of ω under f
is given by the Jacobian determinant of f,
f ∗ω = f ∗(a(x) dx1 ∧· · · ∧dxd) = a( f(x)) d( f ∗x1) ∧· · · ∧d( f ∗xd)
= a( f(x)) (d f1) ∧· · · ∧(d fd)
= a( f(x)) det
 ∂f j
∂xi
!
(dx1 ∧· · · ∧dxd),
where the ﬁnal equality follows from Exercise A.9.
◁
