---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-083-complex-manifolds-and-differential-forms-in-cn
section_title: "Complex manifolds and differential forms in Cn"
section_number: null
pages: 474-480
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Having reviewed the basics of diﬀerential geometry for real manifolds, we now
return to the complex case. As noted above, we may identify Cn with R2n by
mapping (x1 + iy1, . . . , xn + iyn) ∈Cn to (x1, . . . , xn, y1, . . . yn) ∈R2n so any
complex manifold is a real smooth manifold. However, this elides much of the
extra structure of a complex manifold. In particular, we want to understand
how complex analytic behavior and the multiplicative structure of the complex
numbers can be captured in a setting where complex numbers are represented
as real two-vectors. For the remainder of this section, points of R2n will be
referred to by (x1, . . . , xn, y1, . . . , yn) rather than (x1, . . . , x2n).
A.4 Complex manifolds and diﬀerential forms in Cn
457
For any smooth map u from Cn = R2n to C, deﬁne
∂u
∂z j
:= 1
2
 ∂u
∂xj
−i ∂u
∂y j
!
∂u
∂zj
:= 1
2
 ∂u
∂x j
+ i ∂u
∂yj
!
dz := dx + i dy
dz := dx −i dy
∂u :=
d
X
j=1
∂u
∂zj
dz j
∂u :=
d
X
j=1
∂u
∂z j
dz j ,
and du := ∂u + ∂u. The function u is said to be a holomorphic function if
∂u = 0. Holomorphicity of u, under this deﬁnition, is equivalent to the van-
ishing of each ∂u/∂zj, which in turn is equivalent to the Cauchy–Riemann
equations holding in each variable. Since the Cauchy–Riemann equations hold
precisely when u is complex analytic, holomorphicity is invariant under com-
plex analytic coordinate changes. In fact, the decomposition du = ∂u + ∂u
is well deﬁned when u is any smooth complex-valued function on a complex
manifold: such a manifold is deﬁned by an atlas of chart maps whose transi-
tions are complex analytic and thus preserve holomorphicity. It also follows
that for a holomorphic function u, the above formal deﬁnition of the derivation
∂/∂zj in terms of the tangent vectors ∂/∂x j and ∂/∂y j agrees with the limit
deﬁnition
∂f
∂zj
(z) = lim
t→0
u(z + te j) −u(z)
t
,
where ej is the elementary basis vector with a 1 in position j and 0 elsewhere.
Exercise A.13. Use the deﬁnition of d/dz above to compute (d/dz)u(z) when
u(z) = u(x, y) = (x+iy)2 and verify that it is equal to the deﬁnition via calculus
over the complex numbers.
The computational apparatus representing complex numbers as real two-
vectors allows us to prove an important fact about complex manifolds.
Proposition A.25. Every complex manifold is orientable.
Proof
By deﬁnition, overlapping chart maps are related by a complex ana-
lytic coordinate change f. It therefore suﬃces to prove that a bi-holomorphic
map f : U ⊆Cm →Cm always has a positive Jacobian determinant when
viewed as a map on R2m. On the complex tangent space, f∗is complex linear
represented by an m × m complex Jacobian matrix JC = J( f), so that

m
X
j=1
e jzj
=
m
X
j=1
(Jv) jej.
458
Integration on manifolds
Recalling that z is represented as [Re(z), Im(z)], the real 2m × 2m Jacobian
matrix is given by
JR =
" A
−B
B
A
#
,
where A = Re(JC) and B = Im(JC). Positivity of det JR then follows from
nonvanishing of det JC and the identity
det
" A
−B
B
A
#
= det
" A + iB
−B + iA
B
A
#
= det
" A + iB
0
B
A −iB
#
= det(A + iB) · det(A −iB)
= | det(A + iB)|2 .
□
Next, we extend the deﬁnitions of ∂, ∂, and d from functions to diﬀerential
forms as follows. For any coordinate system t1, . . . , t2n and J ⊆[2n], let dtJ
denote the wedge product of dt j for j ∈J in increasing order. For a smooth
function u deﬁne d(u dtJ) = du∧dtJ and extend linearly to all forms. The form
ω is said to be a holomorphic form if it is the sum of terms uJdzJ with no dzi
terms and each uJ is holomorphic. The space of holomorphic functions form
a subring of C∞(R2n), while the space of holomorphic forms have a (noncom-
mutative) ring structure under wedge product and are generated over the ring
of holomorphic functions by {dz1, . . . , dzn}.
Remarks A.26.
(i) Functoriality and the Cauchy–Riemann equations imply
that these deﬁnitions extend to functions on any complex manifold M.
(ii) While the same symbol is used for the boundary operator ∂σ and the
holomorphic diﬀerential ∂u, it is always clear from context which we
refer to.
Tangent and cotangent bundles, diﬀerential forms, and integration on a com-
plex manifold of dimension m can all be deﬁned via its structure as a real man-
ifold of dimension 2m. The operator d preserves holomorphicity: if ∂ω = 0
then dω = ∂ω, which is evidently holomorphic. We also deﬁne the holomor-
phic volume form dz := dz1 ∧· · · ∧dzn in Cn.
Exercise A.14. Show that the conjugation function z is not holomorphic on
C by computing ∂z and ∂z. Find a continuous, piecewise smooth function fε :
C →C that agrees with z on the disk {|z| ≤ε} and is holomorphic outside of
this disk.
The holomorphic volume form is an n-form in R2n, thus middle-dimensional,
A.4 Complex manifolds and diﬀerential forms in Cn
459
but is the highest dimensional holomorphic form in R2n. This leads to the fol-
lowing useful result.
Theorem A.27. If C is any (n + 1)-chain on a domain U ⊆Cn and ω is any
holomorphic n-form on U then
Z
∂C
ω = 0 .
Proof
The d operator preserves holomorphicity, so dω is holomorphic. There
are no holomorphic forms above rank n and ∂ω is a (n+1)-form, hence ∂ω = 0.
Stokes’s Theorem then gives
Z
∂C
ω =
Z
C
dω = 0 .
□
Exercise A.15. Let C be an n-chain supported on a complex submanifold M of
Cn, where the dimension of M is strictly less than n. Show that
R
C ω vanishes
for any holomorphic n-chain ω.
The polydisk with center w ∈Cd and radius r ∈Rd
>0 is the set {z ∈
Cd : |zj −wj| < r j for 1 ≤j ≤d}, while the torus with center w and radius r is
the set {z ∈Cd : |z j−wj| = rj for 1 ≤j ≤d}. Our asymptotic arguments always
begin by representing the power series coeﬃcients of an analytic function by
a complex integral over a polytorus, after which we apply the integration tech-
niques discussed in these appendices. We thus conclude this ﬁrst appendix by
stating and proving the multivariate Cauchy Integral Formula, which is used to
derive such representations.
Proposition A.28 (multivariate Cauchy Integral Formula). Let U ⊂Cd be an
open set and D, T ⊂Cd be a polydisk and torus with radii r ∈Rd
>0, centered
around the same point. If D ⊂U and f is an analytic function on U then, for
all w ∈D,
f(w) =
 1
2πi
!d Z
T
f(z)
(z1 −w1) · · · (zd −wd)dz .
(A.4.1)
□
Proof
Without loss of generality, we may assume that D and T are cen-
tered at the origin. When d = 1 this is the usual (univariate) Cauchy Integral
Formula. The general case follows by induction. In particular, for any ﬁxed
(a1, . . . , ad−1) ∈Cd−1 with each |a j| ≤rj we know from the univariate case that
f(a1, . . . , ad−1, wd) = 1
2πi
Z
|zd|=rd
f(a1, . . . , ad−1, wd)
zd −wd
dzd .
(A.4.2)
460
Integration on manifolds
If the Cauchy Integral Formula holds in d −1 variables then
f(w) =
 1
2πi
!d−1 Z
|z1|=r1
· · ·
Z
|zd−1|=rd−1
f(z1, . . . , zd−1, wd)
(z1 −w1) · · · (zd−1 −wd−1)dz1 · · · dzd−1 ,
and substitution with (A.4.2) implies
f(w) =
 1
2πi
!d Z
T
f(z)
(z1 −w1) · · · (zd −wd)dz ,
as desired.
□
Given vectors a, b ∈Rd
>0, the polyannulus with center w ∈Cd, inner ra-
dius a and outer radius b is the set {z ∈Cd : ak < |zk −wk| < bk for all k}.
Some of our arguments require a version of the Cauchy Integral Formula in a
polyannulus.
Proposition A.29 (Cauchy Integral Formula in a polyannulus). Let U ⊂Cd
be an open set and let D ⊂Cd be a polyannulus of inner radius a and outer
radius b. For η ∈{a, b}d let Tη denote the torus with radius r where
ri =

ai
if ηi = a
bi
if ηi = b
,
and let sgn(η) = (−1)#{j : ηj=a}. If D ⊂U and f is an analytic function on U,
then for all w ∈D
f(w) =
 1
2πi
!d X
η∈{a,b}d
sgn(η)
Z
Tη
f(z)
(z1 −w1) · · · (zd −wd)dz .
(A.4.3)
Proof
When d = 1 the conclusion states that
f(w) = 1
2πi
"Z
|z|=b
f(z)
z −w dz −
Z
|z|=a
f(z)
z −w dz
#
,
which is the classical univariate Cauchy formula in an annulus [H¨or90, Theo-
rem 1.2.1]. Induction now applies exactly as in the previous proposition, noting
that as chains
X
η∈{a,b}d
sgn(η)Tη =
X
η∈{a,b}d−1
sgn(η)Tη × (γb −γa) ,
where γc is the circle of radius c oriented counterclockwise.
□
A.4 Complex manifolds and diﬀerential forms in Cn
461
Notes
The material in the ﬁrst three sections of this chapter is standard graduate-
level calculus, and our presentation of the material owes a debt to the texts of
Tu [Tu11] and Warner [War83]. Additional details on complex manifolds can
be found in Griﬃths and Harris [GH94].
Additional exercises
Exercise A.16. Is there a diﬀerence between RP2 and CP1 as an abstract set?
As a topological space?
Exercise A.17. Let f : X →R be a smooth map on a d-manifold X for
which d f is everywhere nonvanishing. Let M be the zero set of f and let
ι : M →X denote the inclusion map. Prove that for any (d −1)-form η the
equality ι∗(η) = 0 holds if and only if η ∧d f vanishes on M. Repeat this for
k ≤d functions f1, . . . , fk whose intersection deﬁnes a smooth surface M of
codimension k. Hint: Use the implicit function theorem to coordinatize X with
ﬁrst coordinate f and use functoriality of ∧to reduce to the case f = x1.
Exercise A.18. Do Exercise A.17 when X is a complex d-manifold and f :
X →C is analytic. Hint: You can copy the proof, only you need the complex
form of the implicit function theorem [H¨or90, Theorem 2.1.2] in order to be
sure your coordinates are holomorphic.
Exercise A.19. Deﬁne a 2-form ω in R3 by ω = x dy∧dz+y dz∧dx+z dx∧dy
and deﬁne a 2-chain C representing the unit sphere. Compute
R
C ω directly
from the deﬁnitions, then ﬁgure out a shortcut to the same result using Stokes’s
Theorem.
Appendix B
Algebraic topology
Having established the necessary background for integration on real and com-
plex manifolds in Appendix A, we now move on to the topological results that
allow us to manipulate these integrals in order to derive asymptotics. A diﬀer-
ential form ω is said to be a closed form if dω = 0 and an exact form if ω = dτ
for some form τ. Many of the forms we care about are closed, for instance if ω
is any holomorphic n-form in Cn then ∂ω vanishes by holomorphicity and ∂ω
vanishes because there are no holomorphic (n + 1)-forms, hence ω is closed. A
chain C is called a cycle if ∂C = 0 and a boundary if C = ∂D for some chain
D. The boundaries form a subset (in fact, a sub-vector space) of the cycles
because ∂2 = 0.
By the same reasoning as our proof of Theorem A.27 in the last appendix,
the integral of any closed form over a boundary is zero. Thus, by linearity of
the integral, if C is a cycle, then
R
C ω depends only on the equivalence class
of C in the quotient space of cycles modulo boundaries. Homology theory
is the study of this quotient space, which may be thought of simultaneously
as a topological invariant and as classifying contours of integration for closed
forms. After studying various forms of homology, we dualize our constructions
and deﬁne cohomology of diﬀerential forms. Just as
R
C ω depends only on the
homology class of the chain C, it also depends only on the cohomology class
of the form ω.
