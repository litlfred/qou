---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-071-integration-of-forms
section_title: "Integration of forms"
section_number: null
pages: 470-480
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
doc_brief: "Analytic Combinatorics in Several Variables — 85 sections: Preface to the second edition; List of Symbols; Introduction"
---
The only thing remaining before deﬁning integration on manifolds is to discuss
domains of integration. For each p≥ 1, let ∆p denote the standard p-simplex
A.3 Integration of forms 453
inRp deﬁned by
∆p =
(x1,..., xp)∈Rp : xi≥ 0 for all i and
p∑
i=1
xi≤ 1
 .
By convention, if p = 0 then ∆p is deﬁned to be a single point. Associated with
the standard simplices are p+2 ways of embedding∆p as a face of∆p+1. To be
explicit, for each 1≤ i≤ p + 1 letκp
i : ∆p→ ∆p+1 be the embedding obtained
by inserting a zero in the ith position,
κp
i (x1,..., xp) = (x1,..., xi−1, 0, xi+1,..., xp),
and letκp
0 : ∆p→ ∆p+1 embed into the diagonal face,
κp
0(x1,..., xp) =
1−
p∑
i=1
xi , x1,..., xp
 .
We now ﬁx an m-manifoldM in Rn. For each 0 ≤ p≤ m, a smooth p-
simplex (or simply p-simplex) inM is deﬁned to be a map σ : ∆p → M
which extends to a smooth map of a neighborhood of ∆p inRp intoM. Deﬁne
the space Cp(M) of p-chains onM to be the space of ﬁnite formal linear
combinations ∑ ciσi of p-simplices inM with coeﬃcients ci ∈ C. A chain∑ ciσi is said to be supported on a set X⊆M whenever allσi in the sum map
into X.
Deﬁnition A.20 (boundary operator). For any 1≤ p≤ m, the boundary op-
erator on p-chains is the linear map ∂ : Cp→ Cp−1 which takes a p-simplex
σ : ∆p→M and returns the (p− 1)-chain∂σ : ∆p−1→M deﬁned by
∂σ :=
p∑
i=0
(−1)i σ◦κp−1
i . (A.3.1)
Figure A.2 illustrates the boundary operator on a singular 2-simplex.
A crucial property of the boundary operator is that it gives the zero map
when applied twice.
Proposition A.21. For any manifoldM and 1≤ p≤ d the map∂2 = 0.
Exercise A.10. Verify∂2 = 0 by proving thatκp+1
i ◦κp
j =κp+1
j+1◦κp
i for all p≥ 0
and i≤ j (whereκb
a is identically zero if a or b are negative or a> p).
For a domain A⊆ Rn with standard coordinates x1,..., xn, we deﬁne the
integral of a top level form ω = f (x)dx1∧···∧ dxn on A to be the usual
Riemann–Lebesgue integral
∫
A
ω =
∫
A
f (x) dx1∧···∧ dxn =
∫
A
f (x) dV,
454 Integration on manifolds
σ
σ(0,0)
σ(0,1)
σ(1,0)
σ    κ1
0
σ    κ1
1
σ    κ1
2
Figure A.2 A 2-simplex and its boundary.
where dV is Lebesgue measure inRn.
Remark A.22. In order for this deﬁnition of integration to be consistent, we
must write the wedge product in increasing order. For instance, in two dimen-
sions dy∧ dx =−dx∧ dy, so
∫
A
f (x, y)dy∧ dx =−
∫
A
f (x, y)dx∧ dy =−
∫
A
f (x, y)dxdy
even though ∫
A
f (x, y)dxdy =
∫
A
f (x, y)dydx
as Riemann integrals (since f is smooth).
IfM is an oriented manifold then for any p-simplexσ : ∆p→M , integra-
tion of a p-formω overσ is deﬁned by
∫
σ
ω :=
∫
∆p
σ∗(ω),
whereσ∗ is the pullback ofω byσ from a form onM to a form on ∆p⊂Rp. It
is important to note that we have deﬁned integration not over a set (the range
ofσ) but over a parametrization (σ itself). Integration over a chain is deﬁned
by linearity,
∫
∑r
i=1 aiσi
ω :=
r∑
i=1
ai
∫
σi
ω.
Example A.23. IfM =Rd then we can write anyd-simplexσ = (σ1,...,σ d),
where each σi is a smooth map from ∆d toR. Example A.19 implies that for
any d-formω = a(x)dx1∧···∧ dxd,
∫
σ
ω =
∫
∆p
σ∗(ω) =
∫
∆p
a(σ(x))(det J)dx1··· dxd,
A.3 Integration of forms 455
where J is the Jacobian matrix of σ : Rd → Rd and the ﬁnal integral is the
Riemann integral of a smooth function onRd. This mirrors the usual change of
variables formula seen in a ﬁrst calculus course. ◁
We often want to integrate over manifolds, but our formal deﬁnition of inte-
gration holds over chains. Integration over a manifold can be deﬁned by divid-
ing the manifold into a ﬁnite collection of chains, provided ( i) how we divide
up the manifold does not a ﬀect the result, and ( ii) we can orient the chains in
a consistent way so that the integral is uniquely determined up to a sign de-
pending on a global orientation. Recall from above that a manifoldM is called
oriented if for any charts ( U,φ ) and ( V,ψ ) onM with nonempty intersection
W = U∩ V the smooth function φ◦ψ−1 fromψ(W)⊂ Rm toφ(W)⊂ Rm has
positive Jacobian determinant. We do not attempt to deﬁne integration over
non-orientable manifolds.
Assume that the p-manifoldM is orientable and ﬁx one of its two orienta-
tions. We say that a p-simplexσ : ∆p→M is a positively oriented simplex
with respect to this orientation ofM if for any oriented chart ( U,φ ) ofM the
diﬀerentialσ∗ : TpRm→ Tσ(p)M with respect to the bases ∂/∂xk and∂/∂φk
of TpRm and Tσ(p)M has positive determinant. If M is also compact then a
triangulation ofM is a ﬁnite setσ1,...,σ r of positively oriented p-simplices
satisfying certain conditions set out at greater length in the deﬁnition of a sim-
plicial complex in Section B.1 of Appendix B. These conditions imply that the
simplices divideM into regions, meaning that each map is one-to-one on the
interior of ∆m, the images of the interiors are disjoint, and the union of the
images is all of M. Triangulation representsM as a p-chain ∑r
j=1σ j, so the
integral of a p-formω overM is deﬁned by linearity,
∫
M
ω :=
r∑
j=1
∫
σ j
ω. (A.3.2)
The integral does not depend on which oriented triangulation we chose [War83,
Section 4.8], so (A.3.2) deﬁnes the integral of a p-form over an orientable p-
manifold (up to a sign that depends on the orientation chosen).
Exercise A.11. Give an explicit oriented triangulation ofS 2 and use it to inte-
grate f (x, y) = xy2 on S 2.
Above we deﬁned the di ﬀerential map, which takes a smooth function on
a manifoldM – in other words, a 0-form f ∈ E0(M) – and returns a 1-form
d f∈ E1(M). We now extend this map to thediﬀerential operator (or exterior
456 Integration on manifolds
derivative operator) d : E∗(M)→ E∗(M) deﬁned locally in a chart (U,φ ) by
d( f dφI) :=
∑
1≤ j≤m
∂ f
∂φ j
dφ j∧ dφI.
The diﬀerential maps a p-form to a ( p + 1)-form, applying d twice gives the
zero map (this is usually written d2 = 0), and if ω∈ E p(M) and η∈ Eq(M)
then
d(ω∧η) = d(ω)∧η + (−1)pω∧ d(η). (A.3.3)
The diﬀerential still commutes with pullbacks, meaning d(ψ∗(ω)) = ψ∗(dω)
for any smooth mapψ.
Exercise A.12. Prove that (A.3.3) holds.
We introduce the diﬀerential to state Stokes’s Theorem, our last result on the
integration of forms.
Theorem A.24 (Stokes’s Theorem). Let p≥ 1 and suppose thatω is a (p−1)-
form on a manifoldM of dimension at least p. IfC is a p-chain onM then
∫
∂C
ω =
∫
C
dω.
Stokes’s Theorem follows from our deﬁnitions, integration by parts, and
some elementary computations; see [War83, Theorem 4.7] for details.
A.4 Complex manifolds and di ﬀerential forms inCn
Having reviewed the basics of diﬀerential geometry for real manifolds, we now
return to the complex case. As noted above, we may identify Cn withR2n by
mapping ( x1 + iy1,..., xn + iyn)∈ Cn to ( x1,..., xn, y1,... yn)∈ R2n so any
complex manifold is a real smooth manifold. However, this elides much of the
extra structure of a complex manifold. In particular, we want to understand
how complex analytic behavior and the multiplicative structure of the complex
numbers can be captured in a setting where complex numbers are represented
as real two-vectors. For the remainder of this section, points of R2n will be
referred to by (x1,..., xn, y1,..., yn) rather than (x1,..., x2n).
A.4 Complex manifolds and di ﬀerential forms inCn 457
For any smooth map u fromCn =R2n toC, deﬁne
∂u
∂z j
:= 1
2
(∂u
∂x j
− i∂u
∂y j
) ∂u
∂z j
:= 1
2
(∂u
∂x j
+ i∂u
∂y j
)
dz := dx + i dy d z := dx− i dy
∂u :=
d∑
j=1
∂u
∂z j
dz j ∂u :=
d∑
j=1
∂u
∂z j
dz j,
and du := ∂u +∂u. The function u is said to be a holomorphic function if
∂u = 0. Holomorphicity of u, under this deﬁnition, is equivalent to the van-
ishing of each ∂u/∂z j, which in turn is equivalent to the Cauchy–Riemann
equations holding in each variable. Since the Cauchy–Riemann equations hold
precisely when u is complex analytic, holomorphicity is invariant under com-
plex analytic coordinate changes. In fact, the decomposition du = ∂u + ∂u
is well deﬁned when u is any smooth complex-valued function on a complex
manifold: such a manifold is deﬁned by an atlas of chart maps whose transi-
tions are complex analytic and thus preserve holomorphicity. It also follows
that for a holomorphic function u, the above formal deﬁnition of the derivation
∂/∂z j in terms of the tangent vectors ∂/∂x j and ∂/∂y j agrees with the limit
deﬁnition
∂ f
∂z j
(z) = lim
t→0
u(z + te j)− u(z)
t ,
wheree j is the elementary basis vector with a 1 in position j and 0 elsewhere.
Exercise A.13. Use the deﬁnition of d/dz above to compute (d/dz)u(z) when
u(z) = u(x, y) = (x + iy)2 and verify that it is equal to the deﬁnition via calculus
over the complex numbers.
The computational apparatus representing complex numbers as real two-
vectors allows us to prove an important fact about complex manifolds.
Proposition A.25. Every complex manifold is orientable.
Proof By deﬁnition, overlapping chart maps are related by a complex ana-
lytic coordinate change f . It therefore suﬃces to prove that a bi-holomorphic
map f : U ⊆ Cm → Cm always has a positive Jacobian determinant when
viewed as a map on R2m. On the complex tangent space, f∗ is complex linear
represented by an m× m complex Jacobian matrix JC = J( f ), so that

m∑
j=1
e jz j
 =
m∑
j=1
(Jv) je j.
458 Integration on manifolds
Recalling that z is represented as [Re(z), Im(z)], the real 2 m× 2m Jacobian
matrix is given by
JR =
[ A −B
B A
]
,
where A = Re(JC) and B = Im(JC). Positivity of det JR then follows from
nonvanishing of det JC and the identity
det
[ A −B
B A
]
= det
[ A + iB −B + iA
B A
]
= det
[ A + iB 0
B A− iB
]
= det(A + iB)· det(A− iB)
=| det(A + iB)|2.
□
Next, we extend the deﬁnitions of ∂,∂, and d from functions to diﬀerential
forms as follows. For any coordinate system t1,..., t2n and J⊆ [2n], let dtJ
denote the wedge product of dt j for j∈ J in increasing order. For a smooth
function u deﬁne d(u dtJ) = du∧ dtJ and extend linearly to all forms. The form
ω is said to be a holomorphic form if it is the sum of terms uJdzJ with no dzi
terms and each uJ is holomorphic. The space of holomorphic functions form
a subring of C∞(R2n), while the space of holomorphic forms have a (noncom-
mutative) ring structure under wedge product and are generated over the ring
of holomorphic functions by{dz1,..., dzn}.
Remarks A.26. (i) Functoriality and the Cauchy–Riemann equations imply
that these deﬁnitions extend to functions on any complex manifoldM.
(ii) While the same symbol is used for the boundary operator ∂σ and the
holomorphic diﬀerential ∂u, it is always clear from context which we
refer to.
Tangent and cotangent bundles, diﬀerential forms, and integration on a com-
plex manifold of dimension m can all be deﬁned via its structure as a real man-
ifold of dimension 2 m. The operator d preserves holomorphicity: if ∂ω = 0
then dω = ∂ω, which is evidently holomorphic. We also deﬁne the holomor-
phic volume form dz := dz1∧···∧ dzn inCn.
Exercise A.14. Show that the conjugation function z is not holomorphic on
C by computing∂z and∂z. Find a continuous, piecewise smooth function fε :
C→ C that agrees with z on the disk{|z|≤ ε} and is holomorphic outside of
this disk.
The holomorphic volume form is ann-form inR2n, thus middle-dimensional,
A.4 Complex manifolds and di ﬀerential forms inCn 459
but is the highest dimensional holomorphic form in R2n. This leads to the fol-
lowing useful result.
Theorem A.27. IfC is any (n + 1)-chain on a domain U ⊆ Cn andω is any
holomorphic n-form on U then
∫
∂C
ω = 0.
Proof The d operator preserves holomorphicity, sodω is holomorphic. There
are no holomorphic forms above rankn and∂ω is a (n+1)-form, hence∂ω = 0.
Stokes’s Theorem then gives
∫
∂C
ω =
∫
C
dω = 0.
□
Exercise A.15. LetC be an n-chain supported on a complex submanifoldM of
Cn, where the dimension ofM is strictly less than n. Show that
∫
Cω vanishes
for any holomorphic n-chainω.
The polydisk with center w ∈ Cd and radius r ∈ Rd
>0 is the set {z ∈
Cd :|z j− w j|< r j for 1≤ j≤ d}, while the torus with centerw and radiusr is
the set{z∈Cd :|z j−w j| = r j for 1≤ j≤ d}. Our asymptotic arguments always
begin by representing the power series coe ﬃcients of an analytic function by
a complex integral over a polytorus, after which we apply the integration tech-
niques discussed in these appendices. We thus conclude this ﬁrst appendix by
stating and proving the multivariate Cauchy Integral Formula, which is used to
derive such representations.
Proposition A.28 (multivariate Cauchy Integral Formula). Let U⊂Cd be an
open set and D, T⊂ Cd be a polydisk and torus with radii r∈ Rd
>0, centered
around the same point. If D⊂ U and f is an analytic function on U then, for
allw∈ D,
f (w) =
( 1
2πi
)d ∫
T
f (z)
(z1− w1)··· (zd− wd)dz . (A.4.1)
□
Proof Without loss of generality, we may assume that D and T are cen-
tered at the origin. When d = 1 this is the usual (univariate) Cauchy Integral
Formula. The general case follows by induction. In particular, for any ﬁxed
(a1,..., ad−1)∈Cd−1 with each|a j|≤ r j we know from the univariate case that
f (a1,..., ad−1, wd) = 1
2πi
∫
|zd|=rd
f (a1,..., ad−1, wd)
zd− wd
dzd. (A.4.2)
460 Integration on manifolds
If the Cauchy Integral Formula holds in d− 1 variables then
f (w) =
( 1
2πi
)d−1 ∫
|z1|=r1
···
∫
|zd−1|=rd−1
f (z1,..., zd−1, wd)
(z1− w1)··· (zd−1− wd−1)dz1··· dzd−1,
and substitution with (A.4.2) implies
f (w) =
( 1
2πi
)d ∫
T
f (z)
(z1− w1)··· (zd− wd)dz ,
as desired. □
Given vectorsa,b∈ Rd
>0, the polyannulus with center w∈ Cd, inner ra-
diusa and outer radius b is the set{z∈ Cd : ak <|zk− wk| < bk for all k}.
Some of our arguments require a version of the Cauchy Integral Formula in a
polyannulus.
Proposition A.29 (Cauchy Integral Formula in a polyannulus) . Let U ⊂ Cd
be an open set and let D ⊂ Cd be a polyannulus of inner radius a and outer
radiusb. Forη∈{ a, b}d let Tη denote the torus with radiusr where
ri =

ai ifηi = a
bi ifηi = b
,
and let sgn(η) = (−1)#{ j :η j=a}. If D⊂ U and f is an analytic function on U,
then for allw∈ D
f (w) =
( 1
2πi
)d ∑
η∈{a,b}d
sgn(η)
∫
Tη
f (z)
(z1− w1)··· (zd− wd)dz . (A.4.3)
Proof When d = 1 the conclusion states that
f (w) = 1
2πi
[∫
|z|=b
f (z)
z− w dz−
∫
|z|=a
f (z)
z− w dz
]
,
which is the classical univariate Cauchy formula in an annulus [H ¨or90, Theo-
rem 1.2.1]. Induction now applies exactly as in the previous proposition, noting
that as chains
∑
η∈{a,b}d
sgn(η)Tη =
∑
η∈{a,b}d−1
sgn(η)Tη× (γb−γa),
whereγc is the circle of radius c oriented counterclockwise. □
A.4 Complex manifolds and di ﬀerential forms inCn 461
Notes
The material in the ﬁrst three sections of this chapter is standard graduate-
level calculus, and our presentation of the material owes a debt to the texts of
Tu [Tu11] and Warner [War83]. Additional details on complex manifolds can
be found in Griﬃths and Harris [GH94].
Additional exercises
Exercise A.16. Is there a diﬀerence betweenRP2 andCP1 as an abstract set?
As a topological space?
Exercise A.17. Let f : X → R be a smooth map on a d-manifold X for
which d f is everywhere nonvanishing. Let M be the zero set of f and let
ι :M→ X denote the inclusion map. Prove that for any ( d− 1)-form η the
equalityι∗(η) = 0 holds if and only if η∧ d f vanishes onM. Repeat this for
k≤ d functions f1,..., fk whose intersection deﬁnes a smooth surface M of
codimension k. Hint: Use the implicit function theorem to coordinatize X with
ﬁrst coordinate f and use functoriality of∧ to reduce to the case f = x1.
Exercise A.18. Do Exercise A.17 when X is a complex d-manifold and f :
X→ C is analytic. Hint: You can copy the proof, only you need the complex
form of the implicit function theorem [H¨ or90, Theorem 2.1.2] in order to be
sure your coordinates are holomorphic.
Exercise A.19. Deﬁne a 2-formω inR3 byω = x dy∧dz+y dz∧dx +z dx∧dy
and deﬁne a 2-chain C representing the unit sphere. Compute
∫
Cω directly
from the deﬁnitions, then ﬁgure out a shortcut to the same result using Stokes’s
Theorem.
Appendix B
Algebraic topology
Having established the necessary background for integration on real and com-
plex manifolds in Appendix A, we now move on to the topological results that
allow us to manipulate these integrals in order to derive asymptotics. A diﬀer-
ential formω is said to be aclosed form if dω = 0 and an exact form ifω = dτ
for some formτ. Many of the forms we care about are closed, for instance ifω
is any holomorphic n-form inCn then∂ω vanishes by holomorphicity and∂ω
vanishes because there are no holomorphic (n + 1)-forms, henceω is closed. A
chainC is called a cycle if∂C = 0 and a boundary ifC = ∂D for some chain
D. The boundaries form a subset (in fact, a sub-vector space) of the cycles
because∂2 = 0.
By the same reasoning as our proof of Theorem A.27 in the last appendix,
the integral of any closed form over a boundary is zero. Thus, by linearity of
the integral, if C is a cycle, then
∫
Cω depends only on the equivalence class
ofC in the quotient space of cycles modulo boundaries. Homology theory
is the study of this quotient space, which may be thought of simultaneously
as a topological invariant and as classifying contours of integration for closed
forms. After studying various forms of homology, we dualize our constructions
and deﬁne cohomology of diﬀerential forms. Just as
∫
Cω depends only on the
homology class of the chainC, it also depends only on the cohomology class
of the formω.
